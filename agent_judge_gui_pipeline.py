"""
Batch Evaluator For GUI Domain
"""

import os
import sys
import json
import logging
import argparse
import time
import signal
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional
from multiprocessing import Process, Manager, Queue, Event, current_process
from threading import Lock
from queue import Empty
from dotenv import load_dotenv

# Add project root to path
current_dir = Path(__file__).resolve().parent
project_root = current_dir
sys.path.insert(0, str(project_root))

# Import SingleJudgeAgentMCP and RequeueTaskError
from src.agent_judge_gui_evaluator import SingleJudgeAgentMCP, RequeueTaskError

logger = logging.getLogger(__name__)

# ============================================================================
# AWS Configuration - User Configurable
# ============================================================================
# These values can be adjusted based on your AWS account limits
AWS_MAX_VCPUS = 32              # Total vCPU limit for your AWS account
AWS_INSTANCE_TYPE = 't3.medium' # Instance type to use for workers
AWS_VCPUS_PER_INSTANCE = 2      # vCPUs per instance (t3.medium = 2)
AWS_STABILITY_BUFFER = 1        # Reserve N instances for stability (avoid hitting exact limit)

# Calculate maximum workers based on AWS limits
# Formula: (MAX_VCPUS / VCPUS_PER_INSTANCE) - STABILITY_BUFFER
AWS_MAX_WORKER_INSTANCES = (AWS_MAX_VCPUS // AWS_VCPUS_PER_INSTANCE) - AWS_STABILITY_BUFFER
# ============================================================================

# Global variables for signal handling
active_environments = []
processes = []
is_terminating = False
termination_event: Optional[Event] = None
# Track AWS instance IDs for each worker
worker_instance_map: Dict[str, str] = {}
worker_instance_lock = Lock()


def run_evaluation_worker(
    task_queue: Queue,
    args_dict: Dict[str, Any],
    shared_results: list,
    worker_activity: dict = None,
    stop_event: Optional[Event] = None,
    task_status_map: Optional[dict] = None
):
    """
    Worker process function that processes evaluation tasks from a queue
    
    Args:
        task_queue: Queue containing trajectory tasks to process
        args_dict: Dictionary containing all configuration parameters
        shared_results: Shared list to store results
        worker_activity: Shared dict to track worker activity status
    """
    worker_name = current_process().name
    worker_pid = os.getpid()
    logger = logging.getLogger(f"osworld.batch_evaluator_mcp.{worker_name}")
    logger.info(f"🚀 [{worker_name}] [WORKER_START] Worker process started (PID={worker_pid})")
    
    # Store current agent/task for cleanup on signal
    current_agent = None
    current_task_key = None
    current_task_data: Optional[tuple] = None

    def update_task_status(status: str, extra: Optional[Dict[str, Any]] = None):
        """Safely update shared task status map from worker context."""
        nonlocal current_task_key, current_task_data
        if task_status_map is None or current_task_key is None or current_task_data is None:
            return
        trajectory_id, trajectory_type = current_task_data
        payload = {
            "trajectory_id": trajectory_id,
            "trajectory_type": trajectory_type,
            "status": status,
            "worker": worker_name if status != "pending" else None,
            "timestamp": time.time()
        }
        if extra:
            payload.update(extra)
        task_status_map[current_task_key] = payload
    
    # Signal handling for worker process
    def worker_signal_handler(signum, frame):
        nonlocal current_agent  # Declare as nonlocal to access outer scope variable
        logger.info(f"[{worker_name}] Received signal {signum}, shutting down...")
        
        # CRITICAL: Clean up current agent if exists
        if current_agent is not None:
            try:
                logger.info(f"[{worker_name}] Cleaning up agent before exit...")
                if hasattr(current_agent, '_cleanup_environment'):
                    # Give cleanup enough time to complete
                    current_agent._cleanup_environment()
                    logger.info(f"[{worker_name}] Agent cleanup completed")
                current_agent = None
            except Exception as cleanup_e:
                logger.error(f"[{worker_name}] Error during agent cleanup: {cleanup_e}")
                import traceback
                logger.error(f"[{worker_name}] Cleanup traceback: {traceback.format_exc()}")
                
                # Fallback: Try to get instance_id and terminate directly
                try:
                    instance_id = get_agent_instance_id(current_agent)
                    if instance_id:
                        logger.warning(f"[{worker_name}] Cleanup failed, attempting direct AWS termination for {instance_id}...")
                        try:
                            import boto3
                            region = args_dict.get('region', 'us-east-1')
                            ec2 = boto3.client('ec2', region_name=region)
                            ec2.terminate_instances(InstanceIds=[instance_id])
                            logger.info(f"[{worker_name}] ✅ Directly terminated AWS instance {instance_id}")
                        except Exception as term_e:
                            logger.warning(f"[{worker_name}] Failed to directly terminate instance: {term_e}")
                except Exception as fallback_e:
                    logger.warning(f"[{worker_name}] Fallback termination also failed: {fallback_e}")
        
        # Unregister worker instance
        unregister_worker_instance(worker_name)
        
        # Small delay to ensure cleanup completes
        time.sleep(1)
        
        sys.exit(0)
    
    signal.signal(signal.SIGINT, worker_signal_handler)
    signal.signal(signal.SIGTERM, worker_signal_handler)
    
    logger.info(f"Worker {worker_name} started")
    
    # Initialize worker activity tracking
    if worker_activity is not None:
        worker_activity[worker_name] = {
            'status': 'starting',
            'timestamp': time.time(),
            'current_task': None,
            'last_completed': None
        }
    
    # Track save failures - if too many, terminate worker
    save_failure_count = 0
    max_save_failures = 3  # Threshold: terminate worker after 3 save failures
    
    try:
        if stop_event is not None and stop_event.is_set():
            logger.info(f"[{worker_name}] Stop event detected before start, exiting")
            return

        while True:
            if stop_event is not None and stop_event.is_set():
                logger.info(f"🛑 [{worker_name}] [WORKER_LOOP] Stop event set, shutting down")
                break
            if stop_event is None:
                logger.debug(f"[{worker_name}] [WORKER_LOOP] stop_event is None (sequential mode)")
            try:
                # Get next task with timeout
                logger.debug(f"⏳ [{worker_name}] [WORKER_LOOP] Waiting for task from queue (timeout=5s)...")
                task = task_queue.get(timeout=5)
                trajectory_id, trajectory_type = task
                task_key = f"{trajectory_id}_{trajectory_type}"
                current_task_key = task_key
                current_task_data = (trajectory_id, trajectory_type)
                update_task_status("processing")
                logger.info(f"[{worker_name}] Processing trajectory: {trajectory_id} ({trajectory_type})")
                
                # Update worker activity
                if worker_activity is not None:
                    worker_activity[worker_name].update({
                        'status': 'processing',
                        'timestamp': time.time(),
                        'current_task': f"{trajectory_id}_{trajectory_type}"
                    })
            
            except Empty:
                if stop_event is not None and stop_event.is_set():
                    logger.info(f"🛑 [{worker_name}] [WORKER_LOOP] Stop event set while waiting for task, shutting down")
                else:
                    logger.info(f"✅ [{worker_name}] [WORKER_LOOP] Queue timeout (no more tasks), shutting down")
                if worker_activity is not None:
                    worker_activity[worker_name].update({
                        'status': 'finished',
                        'timestamp': time.time(),
                        'current_task': None
                    })
                break
            except Exception:
                # Queue is empty or timeout, exit worker
                logger.info(f"[{worker_name}] No more tasks, shutting down")
                if worker_activity is not None:
                    worker_activity[worker_name].update({
                        'status': 'finished',
                        'timestamp': time.time(),
                        'current_task': None
                    })
                break
            
            try:
                # Build paths (for validation only)
                pairs_root_dir = Path(args_dict['pairs_root_dir'])
                output_dir = Path(args_dict['output_dir'])
                
                # Search for task_id in PPT/Word/Excel subdirectories
                pair_dir = None
                for category in ['PPT', 'Word', 'Excel']:
                    candidate = pairs_root_dir / category / trajectory_id
                    if candidate.exists():
                        pair_dir = candidate
                        break
                
                if pair_dir is None:
                    raise FileNotFoundError(
                        f"Task {trajectory_id} not found in any category (PPT/WORD/EXCEL)"
                    )
                
                task_config_path = pair_dir / trajectory_type / f"{trajectory_id}.json"
                trajectory_path = pair_dir / trajectory_type / "traj.jsonl"
                
                # Validate paths exist
                if not task_config_path.exists():
                    raise FileNotFoundError(f"Task config not found: {task_config_path}")
                if not trajectory_path.exists():
                    raise FileNotFoundError(f"Trajectory file not found: {trajectory_path}")
                
                # Add delay to avoid resource conflicts
                import random
                delay = random.uniform(2, 5)
                logger.info(f"[{worker_name}] Waiting {delay:.1f}s before starting...")
                time.sleep(delay)
                
                # Create agent (MCP version)
                agent = SingleJudgeAgentMCP(
                    model=args_dict['model'],
                    temperature=args_dict.get('temperature', 1.0),
                    observation_type=args_dict['observation_type'],
                    provider=args_dict['provider'],
                    region=args_dict['region'],
                    trajectory_id=f"{trajectory_id}_{trajectory_type}",
                    effort=args_dict['effort'],
                    output_dir=str(output_dir),
                    trajectory_type=trajectory_type,
                    worker_activity=worker_activity,
                    worker_name=worker_name
                )
                
                # Store agent reference for signal handler cleanup
                current_agent = agent
                
                # Try to register AWS instance ID for this worker
                instance_id = None
                try:
                    instance_id = get_agent_instance_id(agent)
                    if instance_id:
                        register_worker_instance(worker_name, instance_id)
                except Exception as reg_e:
                    logger.debug(f"[{worker_name}] Failed to register instance ID: {reg_e}")
                
                # Run evaluation with retry mechanism and proper cleanup
                max_retries = 2
                result = None
                agent_created = True
                
                for attempt in range(max_retries + 1):
                    try:
                        # reset global error counter
                        try:
                            from src.mcp_services.gui.osworld_modules.replay import lib_replay_trajectory
                            lib_replay_trajectory._consecutive_a11y_errors = 0
                            lib_replay_trajectory._consecutive_connection_refused = 0
                            logger.warning(f"[{worker_name}] Reset error counter (attempt {attempt + 1})")
                        except Exception as reset_e:
                            logger.warning(f"[{worker_name}] Failed to reset error counter: {reset_e}")
                        
                        result = agent.evaluate_task(
                            pairs_root_dir=str(pairs_root_dir),
                            task_id=trajectory_id,
                            trajectory_type=trajectory_type
                        )
                        
                        # Try to register instance ID AFTER evaluate_task succeeds
                        if not instance_id:
                            try:
                                instance_id = get_agent_instance_id(agent)
                                if instance_id:
                                    register_worker_instance(worker_name, instance_id)
                                    logger.info(f"[{worker_name}] Registered instance {instance_id} after evaluation")
                                else:
                                    logger.warning(f"[{worker_name}] Could not get instance ID after evaluation - instance may not be cleaned up automatically")
                            except Exception as reg_e:
                                logger.warning(f"[{worker_name}] Failed to register instance ID after evaluation: {reg_e}")
                        
                        break  # Success, exit retry loop
                    
                    except RuntimeError as e:
                        error_msg = str(e)
                        # a11y_tree save failed repeatedly -> requeue (handled by outer except)
                        if "A11Y_TREE_SAVE_FAILED_REQUEUE" in error_msg:
                            raise
                        # check VM service crash error
                        is_vm_crash = "VM service crashed" in error_msg or "Connection Refused" in error_msg
                        # check save failure error
                        is_save_failure = "Failed to save evaluation result" in error_msg or "Failed to write json" in error_msg
                        
                        if is_save_failure:
                            save_failure_count += 1
                            logger.error(f"[{worker_name}] 💾 Save failure #{save_failure_count}/{max_save_failures}: {e}")
                            if save_failure_count >= max_save_failures:
                                logger.error(f"[{worker_name}] 🚨 Too many save failures ({save_failure_count}), terminating worker to restart")
                                # Clean up before exit
                                try:
                                    if hasattr(agent, '_cleanup_environment'):
                                        agent._cleanup_environment()
                                except Exception:
                                    pass
                                unregister_worker_instance(worker_name)
                                sys.exit(1)  # Exit with error code to trigger restart
                        
                        if is_vm_crash:
                            logger.error(f"[{worker_name}] 🚨 Detected VM service crash: {e}")
                            # Note: this error is not recoverable by retry; worker will mark the task as failed
                            logger.error(f"[{worker_name}] VM service crash error cannot be resolved by retry, will clean up environment and record failure")
                        else:
                            logger.warning(f"[{worker_name}] Attempt {attempt + 1} failed for trajectory {trajectory_id}_{trajectory_type}: {e}")
                        
                        # Clean up agent environment on failure
                        try:
                            if hasattr(agent, '_cleanup_environment'):
                                logger.info(f"[{worker_name}] Cleaning up environment after failure...")
                                agent._cleanup_environment()
                        except Exception as cleanup_e:
                            logger.error(f"[{worker_name}] Error during cleanup: {cleanup_e}")
                        
                        # VM crash is a serious error, should not be retried
                        if is_vm_crash:
                            logger.error(f"[{worker_name}] 💀 VM crash error, will not retry, will fail directly")
                            # set result to None, let subsequent code handle the error
                            result = None
                            # record error message to result
                            raise RuntimeError(f"VM crash error: {error_msg}")
                        
                        if attempt < max_retries:
                            wait_time = 5
                            logger.info(f"[{worker_name}] Retrying in {wait_time} seconds...")
                            time.sleep(wait_time)
                            # Recreate agent for retry
                            try:
                                agent = SingleJudgeAgentMCP(
                                    model=args_dict['model'],
                                    temperature=args_dict.get('temperature', 1.0),
                                    observation_type=args_dict['observation_type'],
                                    provider=args_dict['provider'],
                                    region=args_dict['region'],
                                    trajectory_id=f"{trajectory_id}_{trajectory_type}",
                                    effort=args_dict['effort'],
                                    output_dir=str(output_dir),
                                    trajectory_type=trajectory_type,
                                    worker_activity=worker_activity,
                                    worker_name=worker_name
                                )
                                # Update current_agent reference for signal handler
                                current_agent = agent
                                
                                # Register new instance ID for the recreated agent
                                try:
                                    instance_id = get_agent_instance_id(agent)
                                    if instance_id:
                                        register_worker_instance(worker_name, instance_id)
                                        logger.info(f"[{worker_name}] Registered new instance {instance_id} after retry")
                                except Exception as reg_e:
                                    logger.debug(f"[{worker_name}] Failed to register instance ID after retry: {reg_e}")
                            except Exception as recreate_e:
                                logger.error(f"[{worker_name}] Failed to recreate agent: {recreate_e}")
                                raise
                        else:
                            raise
                    
                    except RequeueTaskError:
                        raise
                    except Exception as e:
                        error_msg = str(e)
                        # check save failure error
                        is_save_failure = "Failed to save evaluation result" in error_msg or "Failed to write json" in error_msg
                        
                        if is_save_failure:
                            save_failure_count += 1
                            logger.error(f"[{worker_name}] 💾 Save failure #{save_failure_count}/{max_save_failures}: {e}")
                            if save_failure_count >= max_save_failures:
                                logger.error(f"[{worker_name}] 🚨 Too many save failures ({save_failure_count}), terminating worker to restart")
                                # Clean up before exit
                                try:
                                    if hasattr(agent, '_cleanup_environment'):
                                        agent._cleanup_environment()
                                except Exception:
                                    pass
                                unregister_worker_instance(worker_name)
                                sys.exit(1)  # Exit with error code to trigger restart
                        
                        logger.warning(f"[{worker_name}] Attempt {attempt + 1} failed for trajectory {trajectory_id}_{trajectory_type}: {e}")
                        
                        # Clean up agent environment on failure
                        try:
                            if hasattr(agent, '_cleanup_environment'):
                                logger.info(f"[{worker_name}] Cleaning up environment after failure...")
                                agent._cleanup_environment()
                        except Exception as cleanup_e:
                            logger.error(f"[{worker_name}] Error during cleanup: {cleanup_e}")
                        
                        if attempt < max_retries:
                            wait_time = 5
                            logger.info(f"[{worker_name}] Retrying in {wait_time} seconds...")
                            time.sleep(wait_time)
                            # Recreate agent for retry
                            try:
                                agent = SingleJudgeAgentMCP(
                                    model=args_dict['model'],
                                    temperature=args_dict.get('temperature', 1.0),
                                    observation_type=args_dict['observation_type'],
                                    provider=args_dict['provider'],
                                    region=args_dict['region'],
                                    trajectory_id=f"{trajectory_id}_{trajectory_type}",
                                    effort=args_dict['effort'],
                                    output_dir=str(output_dir),
                                    trajectory_type=trajectory_type,
                                    worker_activity=worker_activity,
                                    worker_name=worker_name
                                )
                                # Update current_agent reference for signal handler
                                current_agent = agent
                                
                                # Register new instance ID for the recreated agent
                                try:
                                    instance_id = get_agent_instance_id(agent)
                                    if instance_id:
                                        register_worker_instance(worker_name, instance_id)
                                        logger.info(f"[{worker_name}] Registered new instance {instance_id} after retry")
                                except Exception as reg_e:
                                    logger.debug(f"[{worker_name}] Failed to register instance ID after retry: {reg_e}")
                            except Exception as recreate_e:
                                logger.error(f"[{worker_name}] Failed to recreate agent: {recreate_e}")
                                raise
                        else:
                            raise  # Final attempt failed, re-raise exception
                
                if result is None:
                    raise RuntimeError("Evaluation failed after all retries")
                
                # Add metadata
                result["trajectory_id"] = trajectory_id
                result["trajectory_type"] = trajectory_type
                result["evaluation_timestamp"] = datetime.utcnow().isoformat()
                result["model"] = args_dict['model']
                result["effort"] = args_dict['effort']
                result["observation_type"] = args_dict['observation_type']
                result["worker_name"] = worker_name
                
                # Add to shared results
                shared_results.append(result)
                update_task_status("done", {"result": "success"})
                current_task_key = None
                current_task_data = None
                
                # Update worker activity
                if worker_activity is not None:
                    worker_activity[worker_name].update({
                        'status': 'idle',
                        'timestamp': time.time(),
                        'current_task': None,
                        'last_completed': f"{trajectory_id}_{trajectory_type}"
                    })
                
                logger.info(f"[{worker_name}] Completed evaluation for trajectory: {trajectory_id}_{trajectory_type}")
                
                # Reset save failure count on successful completion
                save_failure_count = 0
                
                # Ensure agent cleanup is called
                try:
                    if 'agent' in locals() and hasattr(agent, '_cleanup_environment'):
                        logger.info(f"[{worker_name}] Ensuring agent cleanup after successful completion...")
                        agent._cleanup_environment()
                        logger.info(f"[{worker_name}] Agent cleanup completed")
                except Exception as cleanup_e:
                    logger.warning(f"[{worker_name}] Error during post-completion cleanup: {cleanup_e}")
                
                # Unregister instance ID after successful completion
                unregister_worker_instance(worker_name)
                
                # Clear agent reference after successful completion
                current_agent = None
            
            except RequeueTaskError as e:
                logger.warning(f"[{worker_name}] 🔁 a11y_tree load failed repeatedly, requeue task {trajectory_id}_{trajectory_type}: {e}")
                try:
                    task_queue.put((trajectory_id, trajectory_type))
                    update_task_status("pending")
                    logger.info(f"[{worker_name}] Re-queued task {trajectory_id}_{trajectory_type} for re-evaluation")
                except Exception as requeue_e:
                    logger.error(f"[{worker_name}] Failed to requeue task: {requeue_e}")
                try:
                    if 'agent' in locals() and hasattr(agent, '_cleanup_environment'):
                        agent._cleanup_environment()
                except Exception:
                    pass
                unregister_worker_instance(worker_name)
                current_task_key = None
                current_task_data = None
                current_agent = None
                sys.exit(1)
            
            except RuntimeError as e:
                if "A11Y_TREE_SAVE_FAILED_REQUEUE" in str(e):
                    logger.warning(f"[{worker_name}] 🔁 a11y_tree save failed repeatedly, requeue task {trajectory_id}_{trajectory_type}: {e}")
                    try:
                        task_queue.put((trajectory_id, trajectory_type))
                        update_task_status("pending")
                        logger.info(f"[{worker_name}] Re-queued task {trajectory_id}_{trajectory_type} for re-evaluation")
                    except Exception as requeue_e:
                        logger.error(f"[{worker_name}] Failed to requeue task: {requeue_e}")
                    try:
                        if 'agent' in locals() and hasattr(agent, '_cleanup_environment'):
                            agent._cleanup_environment()
                    except Exception:
                        pass
                    unregister_worker_instance(worker_name)
                    current_task_key = None
                    current_task_data = None
                    current_agent = None
                    sys.exit(1)
                raise
            
            except Exception as e:
                logger.error(f"[{worker_name}] Failed to evaluate trajectory {trajectory_id}_{trajectory_type}: {e}")
                import traceback
                logger.error(f"[{worker_name}] Traceback: {traceback.format_exc()}")
                
                # Clean up agent environment on final failure
                try:
                    if 'agent' in locals() and hasattr(agent, '_cleanup_environment'):
                        logger.info(f"[{worker_name}] Final cleanup of environment after failure...")
                        agent._cleanup_environment()
                    # Also clear current_agent reference
                    current_agent = None
                except Exception as cleanup_e:
                    logger.error(f"[{worker_name}] Error during final cleanup: {cleanup_e}")
                    current_agent = None
                
                # Add error result
                error_result = {
                    "trajectory_id": trajectory_id,
                    "trajectory_type": trajectory_type,
                    "success": False,
                    "error": str(e),
                    "evaluation_timestamp": datetime.utcnow().isoformat(),
                    "model": args_dict['model'],
                    "effort": args_dict['effort'],
                    "observation_type": args_dict['observation_type'],
                    "worker_name": worker_name
                }
                shared_results.append(error_result)
                update_task_status("done", {"result": "failed", "error": str(e)})
                current_task_key = None
                current_task_data = None
    
    except Exception as e:
        logger.error(f"[{worker_name}] Worker-level error: {e}")
        import traceback
        logger.error(f"[{worker_name}] Traceback: {traceback.format_exc()}")
    
    finally:
        # Requeue unfinished task if worker exits unexpectedly
        if current_task_key is not None and current_task_data is not None:
            trajectory_id, trajectory_type = current_task_data
            logger.warning(
                f"[{worker_name}] Re-queuing unfinished task {trajectory_id}_{trajectory_type} due to worker shutdown"
            )
            try:
                task_queue.put(current_task_data)
            except Exception as requeue_e:
                logger.error(f"[{worker_name}] Failed to requeue task {trajectory_id}_{trajectory_type}: {requeue_e}")
            update_task_status("pending")
            current_task_key = None
            current_task_data = None

        # Final cleanup of agent if still exists
        if current_agent is not None:
            try:
                logger.info(f"[{worker_name}] Final cleanup of agent in finally block...")
                if hasattr(current_agent, '_cleanup_environment'):
                    # Ensure cleanup is called even if previous cleanup failed
                    try:
                        current_agent._cleanup_environment()
                        logger.info(f"[{worker_name}] Agent cleanup completed in finally block")
                    except Exception as cleanup_inner_e:
                        logger.error(f"[{worker_name}] Error during agent._cleanup_environment(): {cleanup_inner_e}")
                        import traceback
                        logger.error(f"[{worker_name}] Cleanup traceback: {traceback.format_exc()}")
                
                # Also try to get instance_id and terminate directly if cleanup failed
                provider = args_dict.get('provider', 'aws')
                if provider == "aws":
                    try:
                        instance_id = get_agent_instance_id(current_agent)
                        if instance_id:
                            logger.warning(f"[{worker_name}] Cleanup may have failed, attempting direct AWS termination for {instance_id}...")
                            try:
                                import boto3
                                region = args_dict.get('region', 'us-east-1')
                                ec2 = boto3.client('ec2', region_name=region)
                                response = ec2.describe_instances(InstanceIds=[instance_id])
                                state = response['Reservations'][0]['Instances'][0]['State']['Name']
                                if state not in ['terminated', 'shutting-down']:
                                    ec2.terminate_instances(InstanceIds=[instance_id])
                                    logger.info(f"[{worker_name}] ✅ Directly terminated AWS instance {instance_id} in finally block")
                            except Exception as term_e:
                                logger.warning(f"[{worker_name}] Failed to directly terminate instance {instance_id}: {term_e}")
                    except Exception as instance_e:
                        logger.debug(f"[{worker_name}] Could not get instance ID for direct termination: {instance_e}")
                
                current_agent = None
            except Exception as cleanup_e:
                logger.error(f"[{worker_name}] Error during final cleanup in finally: {cleanup_e}")
                import traceback
                logger.error(f"[{worker_name}] Final cleanup traceback: {traceback.format_exc()}")
                current_agent = None
        
        # Unregister worker instance
        unregister_worker_instance(worker_name)
        
        logger.info(f"[{worker_name}] Worker shutdown complete")


def get_host_instance_id() -> Optional[str]:
    """Get the AWS instance ID of the current host machine"""
    try:
        import requests
        response = requests.get(
            "http://169.254.169.254/latest/meta-data/instance-id",
            timeout=1
        )
        if response.status_code == 200:
            return response.text.strip()
    except Exception:
        pass
    return None


def cleanup_orphaned_aws_instances():
    """Clean up any orphaned AWS instances that might be left running"""
    try:
        import boto3
        ec2 = boto3.client('ec2', region_name=os.getenv('AWS_REGION', 'us-east-1'))
        
        # Find instances that might be orphaned
        response = ec2.describe_instances(
            Filters=[
                {'Name': 'instance-state-name', 'Values': ['running']},
                {'Name': 'instance-type', 'Values': [AWS_INSTANCE_TYPE]}
            ]
        )
        
        orphaned_instances = []
        current_time = datetime.utcnow()
        
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                launch_time = instance['LaunchTime'].replace(tzinfo=None)
                running_time = (current_time - launch_time).total_seconds() / 3600  # hours
                
                # If instance has been running for more than 2 hours, consider it potentially orphaned
                if running_time > 2:
                    orphaned_instances.append(instance['InstanceId'])
        
        if orphaned_instances:
            logger.warning(f"Found {len(orphaned_instances)} potentially orphaned instances: {orphaned_instances}")
            logger.info("You may want to manually check and terminate these instances if they are no longer needed")
        
    except Exception as e:
        logger.warning(f"Could not check for orphaned instances: {e}")


def terminate_worker_aws_instances(region: str = "us-east-1"):
    """
    Terminate all AWS instances corresponding to worker processes
    
    Uses two strategies:
    1. Terminate tracked instances
    2. If tracking is empty, find recently created instances as a fallback
    
    Args:
        region: AWS region
    """
    global worker_instance_map, worker_instance_lock
    
    # get host instance ID, avoid killing the host instance
    host_instance_id = get_host_instance_id()
    if host_instance_id:
        logger.info(f"🖥️  [AWS_CLEANUP] Host instance ID: {host_instance_id} (will not terminate)")
    
    # strategy 1: use tracked instance IDs
    with worker_instance_lock:
        tracked_instance_ids = list(worker_instance_map.values())
    
    instance_ids_to_terminate = tracked_instance_ids.copy()
    
    # strategy 2: if tracking is empty, find recently created instances as a fallback
    if not instance_ids_to_terminate:
        logger.info("[AWS_CLEANUP] No tracked instances, searching for recent worker instances...")
        recent_instances = find_recent_worker_instances(region=region, time_window_minutes=30)
        if recent_instances:
            logger.info(f"🔍 [AWS_CLEANUP] Found {len(recent_instances)} recent instances: {recent_instances}")
            instance_ids_to_terminate = recent_instances
        else:
            logger.info("[AWS_CLEANUP] No recent instances found")
    else:
        logger.info(f"🧹 [AWS_CLEANUP] Found {len(instance_ids_to_terminate)} tracked worker instances: {instance_ids_to_terminate}")
    
    if not instance_ids_to_terminate:
        logger.info("[AWS_CLEANUP] No instances to terminate")
        return
    
    try:
        import boto3
        ec2 = boto3.client('ec2', region_name=region)
        
        # filter out host instance
        safe_instance_ids = []
        for instance_id in instance_ids_to_terminate:
            if instance_id == host_instance_id:
                logger.warning(f"[AWS_CLEANUP] Skipping host instance {instance_id}")
                continue
            safe_instance_ids.append(instance_id)
        
        if not safe_instance_ids:
            logger.info("[AWS_CLEANUP] No instances to terminate (all are host instance)")
            return
        
        # check instance status
        try:
            response = ec2.describe_instances(InstanceIds=safe_instance_ids)
            running_instances = []
            for reservation in response['Reservations']:
                for instance in reservation['Instances']:
                    state = instance['State']['Name']
                    instance_id = instance['InstanceId']
                    if state in ['running', 'pending']:
                        running_instances.append(instance_id)
                        logger.info(f"  📋 [AWS_CLEANUP] Instance {instance_id} is {state}, will terminate")
                    else:
                        logger.info(f"[AWS_CLEANUP] Instance {instance_id} is {state}, skipping")
            
            if running_instances:
                logger.info(f"💀 [AWS_CLEANUP] Terminating {len(running_instances)} AWS instances: {running_instances}")
                ec2.terminate_instances(InstanceIds=running_instances)
                logger.info(f"✅ [AWS_CLEANUP] Termination request sent for {len(running_instances)} instances")
            else:
                logger.info("[AWS_CLEANUP] No running instances to terminate")
        except Exception as describe_e:
            logger.error(f"❌ [AWS_CLEANUP] Error describing instances: {describe_e}")
            # even if description fails, try to terminate
            logger.info(f"💀 [AWS_CLEANUP] Attempting to terminate instances anyway: {safe_instance_ids}")
            try:
                ec2.terminate_instances(InstanceIds=safe_instance_ids)
                logger.info(f"✅ [AWS_CLEANUP] Termination request sent")
            except Exception as term_e:
                logger.error(f"❌ [AWS_CLEANUP] Error terminating instances: {term_e}")
        
        # clear tracking map
        with worker_instance_lock:
            worker_instance_map.clear()
            logger.info("✅ [AWS_CLEANUP] Cleared worker instance tracking map")
        
    except Exception as e:
        logger.error(f"❌ [AWS_CLEANUP] Failed to terminate worker AWS instances: {e}")
        import traceback
        logger.error(f"❌ [AWS_CLEANUP] Traceback: {traceback.format_exc()}")


def register_worker_instance(worker_name: str, instance_id: Optional[str]):
    """
    Register the AWS instance ID corresponding to the worker
    
    Args:
        worker_name: Worker process name
        instance_id: AWS instance ID
    """
    global worker_instance_map, worker_instance_lock
    
    if instance_id:
        with worker_instance_lock:
            worker_instance_map[worker_name] = instance_id
            logger.info(f"📝 [INSTANCE_TRACK] Registered instance {instance_id} for worker {worker_name}")
    else:
        logger.debug(f"INSTANCE_TRACK] No instance ID available for worker {worker_name}")


def unregister_worker_instance(worker_name: str):
    """Unregister the instance ID corresponding to the worker"""
    global worker_instance_map, worker_instance_lock
    
    with worker_instance_lock:
        if worker_name in worker_instance_map:
            instance_id = worker_instance_map.pop(worker_name)
            logger.info(f"[INSTANCE_TRACK] Unregistered instance {instance_id} for worker {worker_name}")


def get_agent_instance_id(agent) -> Optional[str]:
    """
    Try to get the AWS instance ID from the agent
    Args:
        agent: SingleJudgeAgentMCP instance
        
    Returns:
        AWS instance ID, if not available, return None
    """
    try:
        # Check if agent has instance_id property
        if hasattr(agent, 'instance_id') and agent.instance_id:
             return agent.instance_id

        # try to get instance ID from env
        if hasattr(agent, 'env') and agent.env:
            # GUIMCPAdapter accesses through mcp_client
            if hasattr(agent.env, 'mcp_client'):
                mcp_client = agent.env.mcp_client
                # try to get instance information from MCP server
                # Note: this requires MCP server to expose instance ID, if not available, return None
                pass
            
            # try to get instance ID from env.provider
            if hasattr(agent.env, 'provider'):
                provider = agent.env.provider
                if hasattr(provider, 'path_to_vm'):
                    # path_to_vm might be the instance ID
                    return provider.path_to_vm
        
        # try to get instance ID from mcp_client
        if hasattr(agent, 'mcp_client') and agent.mcp_client:
            # MCP client might not directly expose instance ID
            pass
        
    except Exception as e:
        logger.debug(f"Failed to get instance ID from agent: {e}")
    
    return None


def find_recent_worker_instances(region: str = "us-east-1", time_window_minutes: int = 30) -> List[str]:
    """
    Find recently created instances
    
    Args:
        region: AWS region
        time_window_minutes: time window, find instances created within this time range
        
    Returns:
        list of instance IDs
    """
    try:
        import boto3
        from datetime import timedelta
        
        ec2 = boto3.client('ec2', region_name=region)
        host_instance_id = get_host_instance_id()
        
        # calculate time window
        current_time = datetime.utcnow()
        time_threshold = current_time - timedelta(minutes=time_window_minutes)
        
        # find running instances
        response = ec2.describe_instances(
            Filters=[
                {'Name': 'instance-state-name', 'Values': ['running', 'pending']},
                {'Name': 'instance-type', 'Values': [AWS_INSTANCE_TYPE]}
            ]
        )
        
        recent_instances = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                launch_time = instance['LaunchTime'].replace(tzinfo=None)
                
                # skip host instance
                if instance_id == host_instance_id:
                    continue
                
                # check if within time window
                if launch_time >= time_threshold:
                    recent_instances.append(instance_id)
        
        return recent_instances
        
    except Exception as e:
        logger.warning(f"Failed to find recent worker instances: {e}")
        return []


def signal_handler(signum, frame):
    """Handle termination signals (SIGINT, SIGTERM) to gracefully shutdown processes."""
    global is_terminating, processes, termination_event
    
    logger.debug(f"🔔 [SIGNAL_HANDLER] Signal {signum} received (SIGINT={signal.SIGINT}, SIGTERM={signal.SIGTERM})")
    
    # Avoid duplicate handling
    if is_terminating:
        logger.warning(f"⚠️  [SIGNAL_HANDLER] Already terminating, ignoring duplicate signal")
        return
    
    is_terminating = True
    logger.info(f"✅ [SIGNAL_HANDLER] Set is_terminating=True")
    logger.info(f"[SIGNAL_HANDLER] Current processes list: {len(processes) if processes else 0} processes")
    
    # Log process status before termination
    if processes:
        logger.info(f"📊 [SIGNAL_HANDLER] Process status before termination:")
        for idx, p in enumerate(processes):
            if p is not None:
                alive = p.is_alive()
                pid = p.pid if hasattr(p, 'pid') else 'N/A'
                exitcode = p.exitcode if hasattr(p, 'exitcode') else 'N/A'
                logger.info(f"  [{idx}] {p.name}: PID={pid}, alive={alive}, exitcode={exitcode}")
    
    # Set termination event
    if termination_event is not None:
        try:
            termination_event.set()
            logger.info(f"✅ [SIGNAL_HANDLER] Set termination_event")
        except Exception as e:
            logger.warning(f"❌ [SIGNAL_HANDLER] Failed to set termination event: {e}")
    else:
        logger.warning(f"[SIGNAL_HANDLER] termination_event is None (may be sequential mode)")
    
    # Send termination signal to all child processes
    if processes:
        logger.info(f"[SIGNAL_HANDLER] Sending termination signal to {len(processes)} child processes...")
        terminated_count = 0
        for idx, p in enumerate(processes):
            if p is not None and p.is_alive():
                try:
                    pid = p.pid if hasattr(p, 'pid') else 'N/A'
                    logger.info(f"  [{idx}] Terminating process {p.name} (PID={pid})...")
                    p.terminate()
                    terminated_count += 1
                    logger.info(f"  [{idx}] ✅ terminate() called on {p.name}")
                except Exception as e:
                    logger.error(f"  [{idx}] ❌ Error sending termination signal to process {p.name}: {e}")
            else:
                if p is None:
                    logger.info(f"  [{idx}] Process is None, skipping")
                else:
                    logger.info(f"  [{idx}] Process {p.name} already dead (alive={p.is_alive()})")
        logger.info(f"📊 [SIGNAL_HANDLER] Called terminate() on {terminated_count} processes")
    else:
        logger.info(f"[SIGNAL_HANDLER] No processes list (may be sequential mode)")
    
    # Allow more time for processes to handle their own cleanup
    # This gives workers time to clean up agents, MCP servers, and AWS instances
    logger.info(f"⏳ [SIGNAL_HANDLER] Waiting 5 seconds for processes to clean up...")
    time.sleep(5)  # Give processes more time to clean up
    
    # Check process status after waiting
    if processes:
        logger.info(f"📊 [SIGNAL_HANDLER] Process status after 2s wait:")
        still_alive = []
        for idx, p in enumerate(processes):
            if p is not None:
                alive = p.is_alive()
                pid = p.pid if hasattr(p, 'pid') else 'N/A'
                exitcode = p.exitcode if hasattr(p, 'exitcode') else 'N/A'
                logger.info(f"  [{idx}] {p.name}: PID={pid}, alive={alive}, exitcode={exitcode}")
                if alive:
                    still_alive.append((idx, p))
        
        if still_alive:
            logger.warning(f"[SIGNAL_HANDLER] {len(still_alive)} processes still alive, will force kill")
        else:
            logger.info(f"✅ [SIGNAL_HANDLER] All processes terminated gracefully")
    
    # Forcefully terminate any processes that didn't exit
    if processes:
        force_killed_count = 0
        for p in processes:
            if p is not None and p.is_alive():
                try:
                    pid = p.pid if hasattr(p, 'pid') else 'N/A'
                    logger.warning(f"💀 [SIGNAL_HANDLER] Forcefully killing process {p.name} (PID={pid})...")
                    import signal as sig
                    os.kill(p.pid, sig.SIGKILL)
                    force_killed_count += 1
                    logger.info(f"  ✅ SIGKILL sent to {p.name} (PID={pid})")
                except (ProcessLookupError, OSError) as e:
                    # Process already dead, ignore
                    logger.debug(f"Process {p.name} already terminated: {e}")
                except Exception as e:
                    logger.error(f"  ❌ Error forcefully terminating process {p.name}: {e}")
        if force_killed_count > 0:
            logger.warning(f"💀 [SIGNAL_HANDLER] Force killed {force_killed_count} processes")
    
    # Find and terminate all MCP server processes 
    try:
        logger.info(f"🔍 [SIGNAL_HANDLER] Searching for orphaned MCP server processes...")
        try:
            import psutil
            psutil_available = True
        except ImportError:
            psutil_available = False
        
        if psutil_available:
            mcp_server_processes = []
            current_pid = os.getpid()
            
            for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                try:
                    if proc.info['pid'] == current_pid:
                        continue  # Skip self
                    
                    cmdline = proc.info.get('cmdline', [])
                    if cmdline and any('gui_mcp_server.py' in str(arg) for arg in cmdline):
                        mcp_server_processes.append(proc)
                        logger.info(f"  📋 Found MCP server process: PID={proc.info['pid']}, cmdline={cmdline[:3]}")
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
            
            if mcp_server_processes:
                logger.warning(f"💀 [SIGNAL_HANDLER] Found {len(mcp_server_processes)} orphaned MCP server processes, terminating...")
                for proc_info in mcp_server_processes:
                    try:
                        proc = psutil.Process(proc_info.info['pid'])
                        logger.info(f"  💀 Terminating MCP server process PID={proc.pid}...")
                        proc.terminate()
                        try:
                            proc.wait(timeout=5)
                            logger.info(f"  ✅ MCP server process {proc.pid} terminated")
                        except psutil.TimeoutExpired:
                            logger.warning(f"  ⚠️  MCP server process {proc.pid} did not terminate, force killing...")
                            proc.kill()
                            proc.wait(timeout=2)
                            logger.info(f"  ✅ MCP server process {proc.pid} force killed")
                    except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
                        logger.debug(f"Process {proc_info.info['pid']} already gone: {e}")
                    except Exception as e:
                        logger.warning(f"  ⚠️  Error terminating MCP server process {proc_info.info['pid']}: {e}")
            else:
                logger.info(f"✅ [SIGNAL_HANDLER] No orphaned MCP server processes found")
        else:
            logger.warning(f"⚠️  [SIGNAL_HANDLER] psutil not available, cannot search for MCP server processes")
            # Fallback: Try to find processes using pgrep
            try:
                import subprocess
                result = subprocess.run(
                    ['pgrep', '-f', 'gui_mcp_server.py'],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.returncode == 0:
                    pids = result.stdout.strip().split('\n')
                    logger.warning(f"💀 [SIGNAL_HANDLER] Found {len(pids)} MCP server processes via pgrep: {pids}")
                    for pid_str in pids:
                        try:
                            pid = int(pid_str.strip())
                            if pid != os.getpid():
                                logger.info(f"  💀 Killing MCP server process PID={pid}...")
                                os.kill(pid, signal.SIGKILL)
                                logger.info(f"  ✅ Killed MCP server process {pid}")
                        except (ValueError, ProcessLookupError, OSError) as e:
                            logger.debug(f"Could not kill process {pid_str}: {e}")
            except Exception as pgrep_e:
                logger.debug(f"⚠️  [SIGNAL_HANDLER] pgrep fallback also failed: {pgrep_e}")
    except Exception as e:
        logger.warning(f"⚠️  [SIGNAL_HANDLER] Error searching for MCP server processes: {e}")
    
    # Terminate worker AWS instances
    try:
        logger.info(f"[SIGNAL_HANDLER] Terminating worker AWS instances...")
        region = os.getenv('AWS_REGION', 'us-east-1')
        terminate_worker_aws_instances(region=region)
    except Exception as e:
        logger.error(f"❌ [SIGNAL_HANDLER] Error terminating worker AWS instances: {e}")
        import traceback
        logger.error(f"❌ [SIGNAL_HANDLER] Traceback: {traceback.format_exc()}")
    
    # Check for orphaned instances (as backup)
    try:
        logger.info(f"🧹 [SIGNAL_HANDLER] Checking for orphaned AWS instances...")
        cleanup_orphaned_aws_instances()
    except Exception as e:
        logger.warning(f"⚠️  [SIGNAL_HANDLER] Error during orphaned instance cleanup: {e}")
    
    logger.info(f"🏁 [SIGNAL_HANDLER] Shutdown complete. Exiting with sys.exit(0)")
    sys.exit(0)


class BatchEvaluatorMCP:
    """Batch evaluator"""
    
    def __init__(self, pairs_root_dir: str, output_dir: str = None,
                 model: str = "gpt-4o", effort: str = "medium",
                 observation_type: str = "screenshot", provider: str = "aws",
                 region: str = "us-east-1", max_workers: int = 1,
                 temperature: float = 1.0, subdomain: str = "ALL"):
        """
        Initialize batch evaluator
        
        Args:
            pairs_root_dir: root directory containing pairs
            output_dir: output directory
            model: model name
            effort: effort level
            observation_type: observation type ("screenshot", "a11y_tree", "screenshot_a11y_tree")
            provider: provider
            region: region
            max_workers: maximum number of concurrent workers
            temperature: temperature parameter
        """
        self.pairs_root_dir = Path(pairs_root_dir)
        self.output_dir = Path(output_dir) if output_dir else self.pairs_root_dir / "batch_results_mcp"
        self.model = model
        self.effort = effort
        self.observation_type = observation_type
        self.provider = provider
        self.region = region
        self.max_workers = max_workers
        self.temperature = temperature
        self.subdomain = subdomain.upper() if subdomain else "ALL"
        
        # Create output directory
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Results tracking
        self.results = []
        self.results_lock = Lock()
        
        # Setup logging
        self.setup_logging()
        
        logger.info(f"Batch Evaluator (MCP) initialized with {max_workers} workers")
        logger.info(f"Pairs root: {self.pairs_root_dir}")
        logger.info(f"Output dir: {self.output_dir}")
    
    def setup_logging(self):
        """Setup logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(sys.stdout)
            ]
        )
        # Explicitly set root logger level to INFO to suppress DEBUG messages
        logging.getLogger().setLevel(logging.INFO)
        
        logging.getLogger('boto3').setLevel(logging.WARNING)
        logging.getLogger('botocore').setLevel(logging.WARNING)
        logging.getLogger('urllib3').setLevel(logging.WARNING)
        logging.getLogger('s3transfer').setLevel(logging.WARNING)
        logging.getLogger('boto').setLevel(logging.WARNING)
    
    def check_existing_results(self) -> set:
        """
        Check completed tasks
        
        Returns:
            Set of completed trajectory identifiers (format: "pair_id_trajectory_type")
        """
        completed_trajectories = set()
        try:
            for path in self.output_dir.rglob("unified_evaluation_result.json"):
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                except Exception as e:
                    logger.warning(f"Failed to read result file {path}: {e}")
                    continue

                metadata = data.get("metadata", {})
                stats = data.get("statistics_summary", {})

                # 判断是否有有效 judgment（不是 N/A）
                agent_judgment = stats.get("agent_judgment", "N/A")
                if agent_judgment in ["N/A", None]:
                    continue

                ground_truth = stats.get("ground_truth", metadata.get("ground_truth", "N/A"))
                if ground_truth not in ["true", "false"]:
                    continue

                pair_id = metadata.get("trajectory_id")
                if not pair_id:
                    name_parts = path.parent.name.split('_')
                    if name_parts:
                        pair_id = name_parts[0]
                    else:
                        continue

                trajectory_id = f"{pair_id}_{ground_truth}"
                completed_trajectories.add(trajectory_id)
                logger.info(f"Found completed trajectory with valid judgment: {trajectory_id}")
        except Exception as e:
            logger.warning(f"Failed to scan existing results in output_dir: {e}")
        
        return completed_trajectories
    
    def discover_trajectories(self, skip_completed: bool = True) -> List[tuple]:
        """Discover all valid trajectories"""
        trajectories = []
        completed_trajectories = set()
        
        if skip_completed:
            completed_trajectories = self.check_existing_results()
        
        # Search in PPT, Word, Excel subdirectories
        categories = ['PPT', 'Word', 'Excel']
        if self.subdomain in categories:
            categories = [self.subdomain]
        for category in categories:
            category_dir = self.pairs_root_dir / category
            if not category_dir.exists():
                logger.warning(f"Category directory not found: {category}")
                continue
            
            for item in category_dir.iterdir():
                if item.is_dir():
                    pair_id = item.name
                    
                    # Check for required directories
                    true_dir = item / "true"
                    false_dir = item / "false"
                    
                    def find_task_config() -> Optional[Path]:
                        """try to find the configuration file in the false/true/root directory"""
                        candidates = [
                            false_dir / f"{pair_id}.json",
                            true_dir / f"{pair_id}.json",
                            item / f"{pair_id}.json",
                        ]
                        for c in candidates:
                            if c.exists():
                                return c
                        return None
                    
                    task_config = find_task_config()
                    traj_true = true_dir / "traj.jsonl"
                    traj_false = false_dir / "traj.jsonl"
                    
                    for trajectory_type, traj_path in [("true", traj_true), ("false", traj_false)]:
                        trajectory_id_full = f"{pair_id}_{trajectory_type}"
                        
                        # if the trajectory file does not exist, skip this type
                        if not traj_path.exists():
                            continue
                        
                        # if the task config is not found, skip
                        if task_config is None:
                            logger.warning(f"Missing task config for {trajectory_id_full}, skip")
                            continue
                        
                        if skip_completed and trajectory_id_full in completed_trajectories:
                            logger.info(f"Skipping completed: {trajectory_id_full}")
                        else:
                            trajectories.append((pair_id, trajectory_type))
                            logger.info(f"Adding: {trajectory_id_full} (category: {category})")
        
        logger.info(f"Discovered {len(trajectories)} valid trajectories to process")
        if skip_completed:
            logger.info(f"Skipped {len(completed_trajectories)} already completed trajectories")
        return trajectories
    
    def evaluate_single_trajectory(self, trajectory_id: str, trajectory_type: str) -> Dict[str, Any]:
        """
        Evaluate a single trajectory
        
        Args:
            trajectory_id: Trajectory ID to evaluate
            trajectory_type: Type of trajectory (true or false)
            
        Returns:
            Evaluation result
        """
        logger.info(f"Starting evaluation for trajectory: {trajectory_id}_{trajectory_type}")
        
        try:
            # Create single judge agent
            agent = SingleJudgeAgentMCP(
                model=self.model,
                temperature=self.temperature,
                observation_type=self.observation_type,
                provider=self.provider,
                region=self.region,
                trajectory_id=f"{trajectory_id}_{trajectory_type}",
                effort=self.effort,
                output_dir=str(self.output_dir),
                trajectory_type=trajectory_type
            )
            
            # Run evaluation
            result = agent.evaluate_task(
                pairs_root_dir=str(self.pairs_root_dir),
                task_id=trajectory_id,
                trajectory_type=trajectory_type
            )
            
            # Add metadata
            result["trajectory_id"] = trajectory_id
            result["trajectory_type"] = trajectory_type
            result["evaluation_timestamp"] = datetime.utcnow().isoformat()
            result["model"] = self.model
            result["effort"] = self.effort
            result["observation_type"] = self.observation_type
            
            logger.info(f"Completed evaluation for trajectory: {trajectory_id}_{trajectory_type}")
            return result
            
        except Exception as e:
            logger.error(f"Failed to evaluate trajectory {trajectory_id}_{trajectory_type}: {e}")
            return {
                "trajectory_id": trajectory_id,
                "trajectory_type": trajectory_type,
                "success": False,
                "error": str(e),
                "evaluation_timestamp": datetime.utcnow().isoformat(),
                "model": self.model,
                "effort": self.effort,
                "observation_type": self.observation_type
            }
    
    def run_batch_evaluation(self, skip_completed: bool = True) -> Dict[str, Any]:
        """
        Run batch evaluation on all discovered trajectories using multiprocessing
        
        Returns:
            Summary of batch evaluation
        """
        global processes
        logger.info("Starting single trajectory batch evaluation (MCP version)...")
        initial_completed_count = len(self.check_existing_results()) if skip_completed else 0
        
        # Discover trajectories
        trajectories = self.discover_trajectories(skip_completed=skip_completed)
        
        if not trajectories:
            # Check if all trajectories are already completed
            existing_results = self.check_existing_results()
            if existing_results:
                logger.info(f"All trajectories already completed ({len(existing_results)} trajectories)")
                return {
                    "success": True,
                    "message": "All trajectories already completed",
                    "total_trajectories": len(existing_results),
                    "completed_trajectories": len(existing_results),
                    "failed_trajectories": 0,
                    "skipped_trajectories": len(existing_results)
                }
            else:
                logger.warning("No valid trajectories found")
                return {
                    "success": False,
                    "error": "No valid trajectories found",
                    "total_trajectories": 0,
                    "completed_trajectories": 0,
                    "failed_trajectories": 0
                }
        
        logger.info(f"Processing {len(trajectories)} trajectories with {self.max_workers} workers")
        
        # Adjust worker count to not exceed number of tasks
        if self.max_workers > len(trajectories):
            original_workers = self.max_workers
            self.max_workers = len(trajectories)
            logger.info(f"Adjusting worker count from {original_workers} to {self.max_workers} (matching task count)")
        
        # Check AWS resources and adjust worker count
        if self.max_workers > 1 and self.provider == "aws":
            recommended_workers = self.check_aws_resources()
            if recommended_workers < self.max_workers:
                logger.warning(f"Adjusting worker count from {self.max_workers} to {recommended_workers} based on AWS resources")
                self.max_workers = recommended_workers
        
        logger.info("=" * 60)
        
        # Record start time for performance metrics
        start_time = time.time()
        
        # Process trajectories
        completed = 0
        failed = 0
        
        global termination_event, is_terminating
        task_status_snapshot: Dict[str, Any] = {}

        if self.max_workers == 1:
            # Sequential processing
            for i, (trajectory_id, trajectory_type) in enumerate(trajectories, 1):
                # Check for termination signal
                if is_terminating:
                    logger.info("Termination flag detected, stopping sequential processing...")
                    break
                
                result = self.evaluate_single_trajectory(trajectory_id, trajectory_type)
                self.save_result(result)
                
                with self.results_lock:
                    self.results.append(result)
                    if result.get("success", False):
                        completed += 1
                    else:
                        failed += 1
                    
                    # Real-time progress update
                    total_processed = completed + failed
                    success_rate = (completed / total_processed) * 100 if total_processed > 0 else 0
                    logger.info(f"[{i:3d}/{len(trajectories)}] Success: {completed:3d} | Failed: {failed:3d} | Rate: {success_rate:5.1f}%")
        
        else:
            # Multiprocess parallel processing
            global termination_event
            termination_event = Event()
            with Manager() as manager:
                shared_results = manager.list()
                task_queue = manager.Queue()
                worker_activity = manager.dict()
                task_status_map = manager.dict()
                
                # Add tasks to queue
                for trajectory_id, trajectory_type in trajectories:
                    task_queue.put((trajectory_id, trajectory_type))
                    task_key = f"{trajectory_id}_{trajectory_type}"
                    task_status_map[task_key] = {
                        "trajectory_id": trajectory_id,
                        "trajectory_type": trajectory_type,
                        "status": "pending",
                        "worker": None,
                        "timestamp": time.time(),
                        "retry_count": 0  # Track retry attempts
                    }
                
                # Prepare arguments
                args_dict = {
                    'pairs_root_dir': str(self.pairs_root_dir),
                    'output_dir': str(self.output_dir),
                    'model': self.model,
                    'effort': self.effort,
                    'observation_type': self.observation_type,
                    'provider': self.provider,
                    'region': self.region,
                    'temperature': self.temperature
                }
                
                # Create and start worker processes
                global processes
                processes = []

                def requeue_tasks_for_worker(dead_worker_name: str) -> int:
                    """Requeue tasks that were in progress on a dead worker."""
                    if task_status_map is None:
                        return 0
                    requeued = 0
                    for task_key, meta in list(task_status_map.items()):
                        if (
                            isinstance(meta, dict)
                            and meta.get("worker") == dead_worker_name
                            and meta.get("status") == "processing"
                        ):
                            trajectory_id = meta.get("trajectory_id")
                            trajectory_type = meta.get("trajectory_type")
                            if trajectory_id is None or trajectory_type is None:
                                continue
                            task_queue.put((trajectory_id, trajectory_type))
                            new_meta = meta.copy()
                            new_meta.update({
                                "status": "pending",
                                "worker": None,
                                "timestamp": time.time(),
                                "requeued": True
                            })
                            task_status_map[task_key] = new_meta
                            requeued += 1
                    if requeued:
                        logger.warning(f"🔁 [TASK_RECOVERY] Requeued {requeued} tasks from worker {dead_worker_name}")
                    return requeued
                logger.info(f"[PROCESS_CREATE] Creating {self.max_workers} worker processes...")
                for i in range(self.max_workers):
                    p = Process(
                        target=run_evaluation_worker,
                        args=(task_queue, args_dict, shared_results, worker_activity, termination_event, task_status_map),
                        name=f"MCPEvalWorker-{i+1}"
                    )
                    p.daemon = True
                    logger.debug(f"  [{i}] Creating process {p.name} (daemon={p.daemon})...")
                    p.start()
                    processes.append(p)
                    logger.debug(f"✅ [{i}] Started worker process {p.name} with PID {p.pid}")
                logger.info(f"✅ [PROCESS_CREATE] All {len(processes)} worker processes started")
                
                try:
                    # Monitor progress and restart dead processes
                    last_progress_check = time.time()
                    last_result_count = 0
                    
                    while True:
                        # Check for termination signal
                        if termination_event is not None and termination_event.is_set():
                            logger.info("🛑 [MONITOR_LOOP] Termination event detected, shutting down...")
                            logger.info(f"[MONITOR_LOOP] Current process status:")
                            for idx, p in enumerate(processes):
                                if p is not None:
                                    logger.info(f"  [{idx}] {p.name}: alive={p.is_alive()}, exitcode={p.exitcode if hasattr(p, 'exitcode') else 'N/A'}")
                            break
                        if is_terminating:
                            logger.info("🛑 [MONITOR_LOOP] Termination flag (is_terminating) detected, shutting down...")
                            logger.info(f"[MONITOR_LOOP] Current process status:")
                            for idx, p in enumerate(processes):
                                if p is not None:
                                    logger.info(f"  [{idx}] {p.name}: alive={p.is_alive()}, exitcode={p.exitcode if hasattr(p, 'exitcode') else 'N/A'}")
                            break
                        
                        current_result_count = len(shared_results)

                        alive_count = sum(1 for p in processes if p is not None and p.is_alive())

                        for idx, p in enumerate(processes):
                            if not p.is_alive():
                                exit_code = p.exitcode if hasattr(p, 'exitcode') else None
                                pid = p.pid if hasattr(p, 'pid') else 'N/A'
                                
                                # distinguish normal exit and abnormal exit
                                is_normal_exit = (exit_code == 0)
                                if is_normal_exit:
                                    logger.debug(f"[MONITOR_LOOP] Process {p.name} (PID={pid}) exited normally (exit_code=0)")
                                else:
                                    logger.warning(f"💀 [MONITOR_LOOP] Process {p.name} (PID={pid}) died abnormally (exit_code={exit_code})")
                                
                                # Worker exits, clean up the corresponding AWS instance
                                if self.provider == "aws":
                                    try:
                                        with worker_instance_lock:
                                            instance_id = worker_instance_map.get(p.name)
                                        
                                        if instance_id:
                                            logger.info(f"[MONITOR_LOOP] Terminating AWS instance {instance_id} for dead worker {p.name}")
                                            try:
                                                import boto3
                                                ec2 = boto3.client('ec2', region_name=self.region)
                                                ec2.terminate_instances(InstanceIds=[instance_id])
                                                logger.info(f"✅ [MONITOR_LOOP] Termination request sent for instance {instance_id}")
                                            except Exception as term_e:
                                                logger.warning(f"⚠️  [MONITOR_LOOP] Failed to terminate instance {instance_id}: {term_e}")
                                        
                                        # remove from the mapping
                                        unregister_worker_instance(p.name)
                                    except Exception as cleanup_e:
                                        logger.warning(f"⚠️  [MONITOR_LOOP] Error cleaning up AWS instance for {p.name}: {cleanup_e}")
                                
                                requeued = requeue_tasks_for_worker(p.name)
                                if requeued > 0:
                                    logger.info(f"🔁 [TASK_RECOVERY] Requeued {requeued} in-flight tasks from {p.name}")
                                
                                # Check if all tasks are completed
                                all_tasks_completed = task_queue.empty() and current_result_count >= len(trajectories)
                                
                                # Check if we have capacity to create new AWS instances
                                can_create_new_instance = True
                                if self.provider == "aws" and not all_tasks_completed:
                                    try:
                                        can_create_new_instance = self._check_aws_capacity_available()
                                        if not can_create_new_instance:
                                            logger.warning(f"⚠️  [MONITOR_LOOP] No AWS capacity available for new instances, cannot restart worker {p.name}")
                                    except Exception as aws_check_e:
                                        logger.warning(f"⚠️  [MONITOR_LOOP] Failed to check AWS capacity: {aws_check_e}, assuming available")
                                        can_create_new_instance = True  # 默认假设可用，避免阻塞

                                # Check if any workers are currently processing tasks
                                workers_processing = False
                                if worker_activity is not None:
                                    for activity in worker_activity.values():
                                        if isinstance(activity, dict) and activity.get('status') == 'processing':
                                            workers_processing = True
                                            break
                                
                                needs_restart = False
                                if not task_queue.empty() and can_create_new_instance:
                                    # Queue has tasks, need workers
                                    needs_restart = True
                                    reason = "tasks remaining in queue, will create new instance"
                                elif not all_tasks_completed and alive_count < self.max_workers and not workers_processing and can_create_new_instance:
                                    # No tasks in queue, but tasks not completed and no workers processing
                                    if task_queue.empty():
                                        # Identify which tasks are incomplete by checking shared_results
                                        completed_task_keys = set()
                                        if shared_results is not None:
                                            for result in shared_results:
                                                if isinstance(result, dict):
                                                    traj_id = result.get("trajectory_id")
                                                    traj_type = result.get("trajectory_type")
                                                    # Only count successful results as completed
                                                    if traj_id and traj_type and result.get("success", False):
                                                        completed_task_keys.add(f"{traj_id}_{traj_type}")
                                        
                                        # Identify tasks currently being processed
                                        processing_task_keys = set()
                                        if task_status_map is not None:
                                            for task_key, meta in list(task_status_map.items()):
                                                if isinstance(meta, dict) and meta.get("status") == "processing":
                                                    processing_task_keys.add(task_key)
                                        
                                        # Find incomplete tasks from original trajectory list
                                        incomplete_tasks = []
                                        max_retries = 3  # Maximum retry attempts
                                        permanently_failed_tasks = []
                                        
                                        for trajectory_id, trajectory_type in trajectories:
                                            task_key = f"{trajectory_id}_{trajectory_type}"
                                            
                                            # Skip if already successfully completed
                                            if task_key in completed_task_keys:
                                                continue
                                            
                                            # Skip if currently being processed (prevent duplicate AWS instances)
                                            if task_key in processing_task_keys:
                                                logger.debug(f"⏭️  [MONITOR_LOOP] Skipping {task_key}: already being processed by active worker")
                                                continue
                                            
                                            # Check retry count
                                            retry_count = 0
                                            if task_status_map is not None and task_key in task_status_map:
                                                meta = task_status_map[task_key]
                                                if isinstance(meta, dict):
                                                    retry_count = meta.get("retry_count", 0)
                                            
                                            # Skip if exceeded retry limit
                                            if retry_count >= max_retries:
                                                logger.warning(f"❌ [MONITOR_LOOP] Skipping {task_key}: exceeded max retries ({retry_count}/{max_retries})")
                                                permanently_failed_tasks.append((trajectory_id, trajectory_type))
                                                continue
                                            
                                            # Task is incomplete, not being processed, and hasn't exceeded retry limit
                                            incomplete_tasks.append((trajectory_id, trajectory_type))
                                        
                                        # Log permanently failed tasks
                                        if permanently_failed_tasks:
                                            logger.error(f"💀 [MONITOR_LOOP] {len(permanently_failed_tasks)} tasks permanently failed after {max_retries} retries: {[f'{t[0]}_{t[1]}' for t in permanently_failed_tasks]}")
                                        
                                        # Repopulate queue with incomplete tasks
                                        if incomplete_tasks:
                                            logger.info(f"📋 [MONITOR_LOOP] Repopulating queue with {len(incomplete_tasks)} incomplete tasks (skipped {len(processing_task_keys)} processing, {len(permanently_failed_tasks)} permanently failed)")
                                            for trajectory_id, trajectory_type in incomplete_tasks:
                                                task_queue.put((trajectory_id, trajectory_type))
                                                task_key = f"{trajectory_id}_{trajectory_type}"
                                                # Update task status to pending and increment retry count
                                                if task_status_map is not None and task_key in task_status_map:
                                                    old_meta = task_status_map[task_key]
                                                    if isinstance(old_meta, dict):
                                                        new_meta = old_meta.copy()
                                                        current_retry_count = old_meta.get("retry_count", 0)
                                                        new_meta.update({
                                                            "status": "pending",
                                                            "worker": None,
                                                            "timestamp": time.time(),
                                                            "requeued": True,
                                                            "retry_count": current_retry_count + 1  # Increment retry count
                                                        })
                                                        task_status_map[task_key] = new_meta
                                                        logger.debug(f"  🔄 Requeued {task_key} (retry {current_retry_count + 1}/{max_retries})")
                                            needs_restart = True
                                            reason = f"repopulated {len(incomplete_tasks)} incomplete tasks (skipped {len(processing_task_keys)} active), below target worker count ({alive_count} < {self.max_workers}), will create new instance"
                                        else:
                                            # No incomplete tasks found, all tasks must be done or being processed
                                            # Don't restart workers
                                            logger.debug(f"[MONITOR_LOOP] Not restarting {p.name}: no incomplete tasks to requeue ({len(completed_task_keys)} completed, {len(processing_task_keys)} processing, {len(permanently_failed_tasks)} permanently failed)")
                                            needs_restart = False
                                    else:
                                        # Queue not empty, restart worker
                                        needs_restart = True
                                        reason = f"tasks not completed, below target worker count ({alive_count} < {self.max_workers}), and no workers processing, will create new instance"
                                elif not all_tasks_completed and alive_count < self.max_workers and workers_processing:
                                    # Tasks are being processed, don't restart even if worker count is low
                                    logger.debug(f"[MONITOR_LOOP] Not restarting {p.name}: tasks are being processed by other workers (alive={alive_count}, processing={workers_processing})")
                                
                                if needs_restart:
                                    logger.info(f"🔄 [MONITOR_LOOP] Restarting process {p.name} because {reason}...")
                                    new_p = Process(
                                        target=run_evaluation_worker,
                                        args=(task_queue, args_dict, shared_results, worker_activity, termination_event, task_status_map),
                                        name=f"MCPEvalWorker-Restart-{idx+1}-{int(time.time())}"
                                    )
                                    new_p.daemon = True
                                    new_p.start()
                                    processes[idx] = new_p
                                    logger.info(f"✅ [MONITOR_LOOP] Restarted process {new_p.name} with PID {new_p.pid} (replacing {p.name}, will create new AWS instance)")
                                    alive_count += 1
                                elif not can_create_new_instance:
                                    logger.error(f"❌ [MONITOR_LOOP] Cannot restart worker {p.name}: No AWS capacity available. Remaining tasks may fail.")
                                elif is_normal_exit and all_tasks_completed:
                                    logger.debug(f"✅ [MONITOR_LOOP] Process {p.name} finished normally (all tasks completed - no restart needed)")
                                else:
                                    logger.info(f"[MONITOR_LOOP] Process {p.name} finished (sufficient workers alive - no restart needed)")
                        
                        # Log current worker status if count doesn't match target
                        queue_size = task_queue.qsize()
                        if alive_count != self.max_workers:
                            if queue_size > 0 or current_result_count < len(trajectories):
                                logger.info(f"📊 Worker count: {alive_count}/{self.max_workers} (queue: {queue_size}, completed: {current_result_count}/{len(trajectories)})")
                            else:
                                logger.debug(f"Worker count: {alive_count}/{self.max_workers} (queue empty, tasks completed - normal worker shutdown)")
                        
                        # Progress reporting
                        if current_result_count > last_result_count:
                            logger.info(f"Progress: {current_result_count}/{len(trajectories)} trajectories completed")
                            last_result_count = current_result_count
                            last_progress_check = time.time()
                        
                        # Check if all tasks are done
                        # Only exit if:
                        # 1. Queue is empty (no more tasks to process)
                        # 2. We have results for all trajectories
                        # 3. All processes have finished (not just died)
                        if task_queue.empty() and current_result_count >= len(trajectories):
                            # Check if all processes have actually finished (not just died)
                            all_finished = True
                            for p in processes:
                                if p is not None and p.is_alive():
                                    all_finished = False
                                    break
                            
                            if all_finished:
                                logger.info("All tasks completed and all processes finished, waiting for final cleanup...")
                                break
                            else:
                                # Some processes are still alive, wait for them
                                logger.debug(f"All tasks have results, but {sum(1 for p in processes if p is not None and p.is_alive())} processes still running...")
                        
                        # Check for stalled progress and stuck workers
                        current_time = time.time()
                        # if there is no new result for 5 minutes, consider it as long-term progress, trigger a detailed check
                        if current_time - last_progress_check > 300:  # 5 minutes without progress
                            logger.warning(f"No progress for {int((current_time - last_progress_check) / 60)} minutes, checking worker status...")
                            
                            # Check individual worker activity
                            stuck_workers = []
                            for worker_name, activity in worker_activity.items():
                                if activity.get('status') == 'processing':
                                    time_since_update = current_time - activity.get('timestamp', current_time)
                                    
                                    # find the corresponding worker process
                                    worker_process = None
                                    for p in processes:
                                        if p is not None and p.name == worker_name:
                                            worker_process = p
                                            break
                                    
                                    # check if the process is truly stuck
                                    is_truly_stuck = False
                                    if worker_process is None:
                                        # process does not exist, but status is 'processing',说明进程异常退出
                                        is_truly_stuck = True
                                        logger.warning(f"Worker {worker_name} process not found but status is 'processing'")
                                    elif not worker_process.is_alive():
                                        # process is dead, but status is 'processing'
                                        is_truly_stuck = True
                                        logger.warning(f"Worker {worker_name} process is dead but status is 'processing'")
                                    elif time_since_update > 600:  # if there is no update for 10 minutes, it is considered that the process is truly stuck
                                        is_truly_stuck = True
                                        logger.warning(f"Worker {worker_name} stuck on task {activity.get('current_task')} for {time_since_update/60:.1f} minutes (process alive but no update)")
                                    
                                    if is_truly_stuck:
                                        stuck_workers.append(worker_name)
                            
                            # Terminate stuck workers and their AWS instances
                            if stuck_workers:
                                logger.warning(f"Found {len(stuck_workers)} truly stuck workers: {stuck_workers}")
                                for worker_name in stuck_workers:
                                    # terminate the corresponding AWS instance
                                    if self.provider == "aws":
                                        try:
                                            with worker_instance_lock:
                                                instance_id = worker_instance_map.get(worker_name)
                                            
                                            if instance_id:
                                                logger.warning(f"🧹 [STUCK_WORKER] Terminating AWS instance {instance_id} for stuck worker {worker_name}")
                                                try:
                                                    import boto3
                                                    ec2 = boto3.client('ec2', region_name=self.region)
                                                    ec2.terminate_instances(InstanceIds=[instance_id])
                                                    logger.info(f"✅ [STUCK_WORKER] Termination request sent for instance {instance_id}")
                                                except Exception as term_e:
                                                    logger.warning(f"⚠️  [STUCK_WORKER] Failed to terminate instance {instance_id}: {term_e}")
                                            
                                            # remove from the mapping
                                            unregister_worker_instance(worker_name)
                                        except Exception as cleanup_e:
                                            logger.warning(f"⚠️  [STUCK_WORKER] Error cleaning up AWS instance for {worker_name}: {cleanup_e}")
                                    
                                    # 然后终止 worker 进程（会被 dead process detection 重启）
                                    for idx, p in enumerate(processes):
                                        if p is not None and p.name == worker_name and p.is_alive():
                                            logger.warning(f"💀 [STUCK_WORKER] Terminating stuck worker {worker_name} (will be restarted with new instance)")
                                            p.terminate()
                                            break
                            else:
                                # 没有真正卡死的 worker，只是任务执行时间较长
                                logger.info(f"All workers are active (some tasks may take longer than expected, e.g., deepseek-reasoner API calls)")
                            
                            if alive_count == 0:
                                # Check if we have results for all tasks
                                if current_result_count >= len(trajectories):
                                    logger.warning("All processes died, but all tasks have results. Exiting.")
                                    break
                                else:
                                    logger.error(f"All processes died and no progress (only {current_result_count}/{len(trajectories)} tasks completed). Exiting.")
                                    break
                            
                            # Log current worker status
                            logger.info("Current worker status:")
                            for worker_name, activity in worker_activity.items():
                                status = activity.get('status', 'unknown')
                                current_task = activity.get('current_task', 'none')
                                last_update = current_time - activity.get('timestamp', current_time)
                                logger.info(f"  {worker_name}: {status}, task: {current_task}, last_update: {last_update:.1f}s ago")
                            
                            last_progress_check = current_time
                        
                        time.sleep(10)  # Check every 10 seconds
                    
                    # Wait for all processes to complete with timeout
                    # But check for termination signal first
                    if termination_event is not None and termination_event.is_set():
                        logger.info("🛑 [JOIN_PROCESSES] Termination event set, skipping process join...")
                    elif is_terminating:
                        logger.info("🛑 [JOIN_PROCESSES] Termination flag set, skipping process join...")
                    else:
                        logger.info("⏳ [JOIN_PROCESSES] Waiting for all processes to complete...")
                        for idx, p in enumerate(processes):
                            if p is not None and p.is_alive():
                                pid = p.pid if hasattr(p, 'pid') else 'N/A'
                                logger.info(f"  [{idx}] Joining process {p.name} (PID={pid}) with 10s timeout...")
                                p.join(timeout=10)  # Reduced timeout for faster shutdown
                                if p.is_alive():
                                    logger.warning(f"  ⚠️  [{idx}] Process {p.name} did not finish in time, terminating...")
                                    p.terminate()
                                    logger.info(f"  📤 [{idx}] Called terminate() on {p.name}, waiting 2s...")
                                    p.join(timeout=2)  # Reduced timeout
                                    if p.is_alive():
                                        # Force kill if still alive
                                        logger.warning(f"  💀 [{idx}] Process {p.name} still alive, sending SIGKILL...")
                                        try:
                                            import signal as sig
                                            os.kill(p.pid, sig.SIGKILL)
                                            logger.info(f"  ✅ [{idx}] SIGKILL sent to {p.name} (PID={pid})")
                                        except Exception as kill_e:
                                            logger.error(f"  ❌ [{idx}] Failed to kill {p.name}: {kill_e}")
                                else:
                                    exitcode = p.exitcode if hasattr(p, 'exitcode') else 'N/A'
                                    logger.info(f"  ✅ [{idx}] Process {p.name} completed (exitcode={exitcode})")
                    
                    # Process results
                    self.results = list(shared_results)
                    for result in self.results:
                        if result.get("success", True):  # Default to success if not specified
                            completed += 1
                        else:
                            failed += 1
                        # Save individual result for progress tracking
                        self.save_result(result)
                
                except KeyboardInterrupt:
                    logger.info("🔔 [KEYBOARD_INTERRUPT] Batch evaluation received KeyboardInterrupt. Initiating graceful shutdown...")
                    is_terminating = True
                    logger.info("✅ [KEYBOARD_INTERRUPT] Set is_terminating=True")
                    if termination_event is not None:
                        termination_event.set()
                        logger.info("✅ [KEYBOARD_INTERRUPT] Set termination_event")
                    else:
                        logger.warning("[KEYBOARD_INTERRUPT] termination_event is None")
                    
                    # Terminate all processes
                    logger.info(f"[KEYBOARD_INTERRUPT] Terminating {len(processes)} processes...")
                    for idx, p in enumerate(processes):
                        if p is not None and p.is_alive():
                            try:
                                pid = p.pid if hasattr(p, 'pid') else 'N/A'
                                logger.info(f"  [{idx}] Terminating process {p.name} (PID={pid}) due to KeyboardInterrupt...")
                                p.terminate()
                                logger.info(f"  ✅ [{idx}] terminate() called on {p.name}")
                            except Exception as term_e:
                                logger.error(f"  ❌ [{idx}] Error terminating process {p.name}: {term_e}")
                        else:
                            if p is None:
                                logger.info(f"  [{idx}] Process is None, skipping")
                            else:
                                logger.info(f"  [{idx}] Process {p.name} already dead")
                    raise
                except Exception as e:
                    logger.error(f"Unexpected error during batch evaluation: {e}", exc_info=True)
                    for p in processes:
                        if p.is_alive():
                            try:
                                logger.info(f"Terminating process {p.name} due to error...")
                                p.terminate()
                            except Exception as term_e:
                                logger.error(f"Error terminating process {p.name}: {term_e}")
                    raise
            termination_event = None
            try:
                task_status_snapshot = dict(task_status_map)
            except (BrokenPipeError, EOFError, OSError) as e:
                logger.warning(f"⚠️  [FINALLY] Failed to read task_status_map (manager connection lost): {e}")
                task_status_snapshot = {}
        
        # Ensure any unfinished tasks are recorded as failures
        if task_status_snapshot:
            unfinished_tasks = [
                meta for meta in task_status_snapshot.values()
                if isinstance(meta, dict) and meta.get("status") != "done"
            ]
            if unfinished_tasks:
                logger.error(f"❌ Detected {len(unfinished_tasks)} unfinished trajectories after worker shutdown")
                for meta in unfinished_tasks:
                    trajectory_id = meta.get("trajectory_id")
                    trajectory_type = meta.get("trajectory_type", "unknown")
                    if trajectory_id is None:
                        continue
                    error_msg = "Worker exited before completing trajectory"
                    error_result = {
                        "trajectory_id": trajectory_id,
                        "trajectory_type": trajectory_type,
                        "success": False,
                        "error": error_msg,
                        "evaluation_timestamp": datetime.utcnow().isoformat(),
                        "model": self.model,
                        "effort": self.effort,
                        "observation_type": self.observation_type
                    }
                    self.results.append(error_result)
                    self.save_result(error_result)
                    failed += 1
        # Count existing results for summary
        existing_results = self.check_existing_results()
        total_trajectories_in_directory = len([item for item in self.pairs_root_dir.iterdir() if item.is_dir()]) * 2  # Each pair has 2 trajectories
        total_processed_this_run = completed + failed
        total_completed_overall = len(existing_results)
        skipped_trajectories = initial_completed_count if skip_completed else 0
        
        # Retry failed trajectories if any
        failed_trajectories_to_retry = []
        if failed > 0:
            logger.info(f"🔄 Checking {failed} failed trajectories for retry...")
            for result in self.results:
                if not result.get("success", True):
                    trajectory_id = result.get("trajectory_id")
                    trajectory_type = result.get("trajectory_type")
                    if trajectory_id and trajectory_type:
                        # Check if this trajectory already has a successful result
                        trajectory_key = f"{trajectory_id}_{trajectory_type}"
                        if trajectory_key not in existing_results:
                            # No successful result exists, add to retry list
                            failed_trajectories_to_retry.append((trajectory_id, trajectory_type))
                            logger.info(f"  📋 Will retry: {trajectory_key}")
                        else:
                            logger.debug(f"  ✅ Skipping {trajectory_key} (already has successful result)")
        
        # Retry failed trajectories
        retry_completed = 0
        retry_failed = 0
        if failed_trajectories_to_retry and not is_terminating:
            logger.info(f"🔄 Retrying {len(failed_trajectories_to_retry)} failed trajectories...")
            
            retry_start_time = time.time()
            
            # Use the same processing method (sequential or parallel)
            if self.max_workers == 1:
                # Sequential retry
                for i, (trajectory_id, trajectory_type) in enumerate(failed_trajectories_to_retry, 1):
                    if is_terminating:
                        logger.info("Termination flag detected, stopping retry...")
                        break
                    
                    logger.debug(f"[Retry {i}/{len(failed_trajectories_to_retry)}] Retrying: {trajectory_id}_{trajectory_type}")
                    result = self.evaluate_single_trajectory(trajectory_id, trajectory_type)
                    self.save_result(result)
                    
                    with self.results_lock:
                        # Remove old failed result and add new result
                        self.results = [r for r in self.results if not (
                            r.get("trajectory_id") == trajectory_id and 
                            r.get("trajectory_type") == trajectory_type and 
                            not r.get("success", True)
                        )]
                        self.results.append(result)
                        
                        if result.get("success", False):
                            retry_completed += 1
                            completed += 1
                            failed -= 1
                        else:
                            retry_failed += 1
            else:
                # Parallel retry (reuse the same multiprocessing logic)
                termination_event = Event()
                with Manager() as manager:
                    shared_results_retry = manager.list()
                    task_queue_retry = manager.Queue()
                    worker_activity_retry = manager.dict()
                    task_status_map_retry = manager.dict()
                    
                    # Add retry tasks to queue
                    for trajectory_id, trajectory_type in failed_trajectories_to_retry:
                        task_queue_retry.put((trajectory_id, trajectory_type))
                        task_key = f"{trajectory_id}_{trajectory_type}"
                        task_status_map_retry[task_key] = {
                            "trajectory_id": trajectory_id,
                            "trajectory_type": trajectory_type,
                            "status": "pending",
                            "worker": None,
                            "timestamp": time.time()
                        }
                    
                    # Prepare arguments
                    args_dict = {
                        'pairs_root_dir': str(self.pairs_root_dir),
                        'output_dir': str(self.output_dir),
                        'model': self.model,
                        'effort': self.effort,
                        'observation_type': self.observation_type,
                        'provider': self.provider,
                        'region': self.region,
                        'temperature': self.temperature
                    }
                    
                    # Create and start worker processes for retry
                    # Adjust worker count to match retry task count (don't create more workers than tasks)
                    retry_worker_count = min(self.max_workers, len(failed_trajectories_to_retry))
                    if retry_worker_count < self.max_workers:
                        logger.info(f"⚙️  Adjusting retry worker count from {self.max_workers} to {retry_worker_count} (matching retry task count: {len(failed_trajectories_to_retry)})")
                    
                    retry_processes = []
                    for i in range(retry_worker_count):
                        p = Process(
                            target=run_evaluation_worker,
                            args=(task_queue_retry, args_dict, shared_results_retry, worker_activity_retry, termination_event, task_status_map_retry),
                            name=f"MCPEvalWorker-Retry-{i+1}"
                        )
                        p.daemon = True
                        p.start()
                        retry_processes.append(p)
                    
                    logger.info(f"✅ Started {len(retry_processes)} worker processes for retry ({len(failed_trajectories_to_retry)} tasks)")
                    
                    try:
                        # Monitor retry progress
                        while True:
                            if termination_event.is_set() or is_terminating:
                                logger.info("Termination detected, stopping retry...")
                                break
                            
                            # Check if all retry tasks are done
                            if task_queue_retry.empty() and len(shared_results_retry) >= len(failed_trajectories_to_retry):
                                # Check if all processes have finished
                                all_finished = all(not p.is_alive() for p in retry_processes)
                                if all_finished:
                                    break
                            
                            time.sleep(5)  # Check every 5 seconds
                        
                        # Wait for all retry processes to complete
                        for p in retry_processes:
                            if p.is_alive():
                                p.join(timeout=10)
                                if p.is_alive():
                                    p.terminate()
                                    p.join(timeout=2)
                    
                    except Exception as retry_e:
                        logger.error(f"Error during retry: {retry_e}")
                    
                    # Process retry results
                    retry_results = list(shared_results_retry)
                    for result in retry_results:
                        # Remove old failed result and add new result
                        self.results = [r for r in self.results if not (
                            r.get("trajectory_id") == result.get("trajectory_id") and 
                            r.get("trajectory_type") == result.get("trajectory_type") and 
                            not r.get("success", True)
                        )]
                        self.results.append(result)
                        self.save_result(result)
                        
                        if result.get("success", False):
                            retry_completed += 1
                            completed += 1
                            failed -= 1
                        else:
                            retry_failed += 1
                    
                    logger.debug(f"Retry completed: {retry_completed} succeeded, {retry_failed} failed")
            
            retry_time = time.time() - retry_start_time
            logger.debug(f"Retry耗时: {retry_time:.1f}秒")
        
        # Generate detailed summary
        execution_time = time.time() - start_time
        
        summary = {
            "success": failed == 0,
            "total_trajectories_in_directory": total_trajectories_in_directory,
            "trajectories_processed_this_run": total_processed_this_run,
            "completed_trajectories_this_run": completed,
            "failed_trajectories_this_run": failed,
            "skipped_trajectories": skipped_trajectories,
            "total_completed_trajectories": total_completed_overall,
            "success_rate_this_run": (completed / total_processed_this_run) * 100 if total_processed_this_run else 0,
            "overall_success_rate": (total_completed_overall / total_trajectories_in_directory) * 100 if total_trajectories_in_directory else 0,
            "execution_time_seconds": execution_time,
            "average_time_per_trajectory": execution_time / total_processed_this_run if total_processed_this_run else 0,
            "evaluation_timestamp": datetime.utcnow().isoformat(),
            "model": self.model,
            "effort": self.effort,
            "observation_type": self.observation_type,
            "max_workers": self.max_workers,
            "trajectories_details_this_run": [f"{tid}_{tt}" for tid, tt in trajectories],
            "detailed_statistics": {
                "execution_summary": {
                    "start_time": start_time,
                    "end_time": time.time(),
                    "total_duration_seconds": execution_time,
                    "trajectories_per_minute": (total_processed_this_run / execution_time) * 60 if execution_time > 0 else 0
                },
                "success_breakdown": {
                    "this_run_successful": completed,
                    "this_run_failed": failed,
                    "previously_completed": initial_completed_count,
                    "total_successful": total_completed_overall,
                    "remaining_trajectories": max(total_trajectories_in_directory - total_completed_overall, 0)
                },
                "model_configuration": {
                    "model": self.model,
                    "effort": self.effort,
                    "observation_type": self.observation_type,
                    "max_workers": self.max_workers,
                    "provider": self.provider,
                    "region": self.region
                }
            }
        }
        
        logger.info("=" * 60)
        logger.info(f"🎯 single trajectory batch evaluation completed!")
        run_success_rate = (completed / total_processed_this_run) * 100 if total_processed_this_run else 0
        logger.info(f"Final result: {completed} successful, {failed} failed (success rate: {run_success_rate:.1f}%)")
        if total_completed_overall:
            overall_rate = (total_completed_overall / total_trajectories_in_directory) * 100 if total_trajectories_in_directory else 0
            logger.info(f"Total completed: {total_completed_overall}/{total_trajectories_in_directory} ({overall_rate:.1f}%)")
        if skipped_trajectories:
            logger.info(f"Skipped: {skipped_trajectories} completed tasks")
        logger.info(f"Total time: {execution_time:.1f} seconds")
        logger.info(f"Results saved to: {self.output_dir}")
        logger.info("=" * 60)
        
        return summary
    
    def save_result(self, result: Dict[str, Any]):
        """Persist per-trajectory outputs via SingleJudgeAgentMCP only; avoid extra JSON in output_dir root."""
        trajectory_id = result.get("trajectory_id", "unknown")
        trajectory_type = result.get("trajectory_type", "unknown")
        if not result.get("success"):
            logger.warning(f"Trajectory {trajectory_id}_{trajectory_type}: evaluation failed - {result.get('error')}")
        try:
            totals = self.compute_current_success_rate()
            logger.info(
                f"✅[Progress] Aggregated success rate in {self.output_dir}: "
                f"{totals['success_rate']:.1f}% (correct={totals['correct']}, total={totals['total']})"
            )
        except Exception as e:
            logger.warning(f"Failed to compute aggregated success rate: {e}")
    
    def compute_current_success_rate(self) -> Dict[str, Any]:
        """
        scan the unified_evaluation_result.json in all subdirectories of output_dir,
        count the success rate based on statistics_summary.is_judgment_correct.
        return {correct, total, success_rate}.
        """
        correct = 0
        total = 0
        try:
            for path in self.output_dir.rglob("unified_evaluation_result.json"):
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    stats = data.get("statistics_summary", {})
                    is_correct = stats.get("is_judgment_correct")
                    if isinstance(is_correct, bool):
                        total += 1
                        if is_correct:
                            correct += 1
                except Exception:
                    continue
        except Exception as e:
            raise e
        
        success_rate = (correct / total * 100.0) if total > 0 else 0.0
        return {"correct": correct, "total": total, "success_rate": success_rate}
    
    def _check_aws_capacity_available(self) -> bool:
        """
        check if there is capacity to create new AWS instances for workers
        
        Returns:
            True if there is capacity to create new AWS instances for workers, False otherwise
        """
        try:
            import boto3
            ec2 = boto3.client('ec2', region_name=self.region)
            
            # Get current running/pending instances
            host_instance_id = get_host_instance_id()
            response = ec2.describe_instances(
                Filters=[
                    {'Name': 'instance-state-name', 'Values': ['running', 'pending']},
                    {'Name': 'instance-type', 'Values': [AWS_INSTANCE_TYPE]}
                ]
            )
            
            worker_instance_count = 0
            for reservation in response['Reservations']:
                for instance in reservation['Instances']:
                    instance_id = instance['InstanceId']
                    # exclude host instance
                    if instance_id != host_instance_id:
                        worker_instance_count += 1
            
            max_worker_instances = AWS_MAX_WORKER_INSTANCES
            available = worker_instance_count < max_worker_instances
            
            if not available:
                logger.warning(f"⚠️  [AWS_CAPACITY] No AWS capacity available (current: {worker_instance_count}/{max_worker_instances} worker instances)")
            else:
                logger.debug(f"✅ [AWS_CAPACITY] AWS capacity available (current: {worker_instance_count}/{max_worker_instances} worker instances)")
            
            return available
            
        except Exception as e:
            logger.warning(f"⚠️  [AWS_CAPACITY] Failed to check AWS capacity: {e}")
            return True
    
    def check_aws_resources(self) -> int:
        """
        Check AWS resources and return the maximum number of workers that can be supported
        
        Returns:
            Maximum number of workers that can be supported (at least 1)
        """
        try:
            import boto3
            ec2 = boto3.client('ec2', region_name=self.region)
            
            # Get current running instances
            response = ec2.describe_instances(
                Filters=[
                    {'Name': 'instance-state-name', 'Values': ['running', 'pending']}
                ]
            )
            
            current_vcpus = 0
            instance_count = 0
            for reservation in response['Reservations']:
                for instance in reservation['Instances']:
                    instance_type = instance['InstanceType']
                    instance_count += 1
                    # Count vCPUs based on configured instance type
                    if instance_type == AWS_INSTANCE_TYPE:
                        current_vcpus += AWS_VCPUS_PER_INSTANCE
                    elif instance_type.startswith('t3.'):
                        # Other t3 instances, estimate using configured vCPU count
                        current_vcpus += AWS_VCPUS_PER_INSTANCE
                    else:
                        # Unknown instance type, estimate using configured vCPU count
                        current_vcpus += AWS_VCPUS_PER_INSTANCE
            
            logger.info(f"AWS Resource Check: Found {instance_count} instances using {current_vcpus} vCPUs")
            
            # AWS limit (configurable at file top: AWS_MAX_VCPUS, AWS_VCPUS_PER_INSTANCE)
            # Each worker needs 1 environment, each environment needs 1 instance (see AWS_INSTANCE_TYPE config)
            available_vcpus = AWS_MAX_VCPUS - current_vcpus
            max_workers_by_vcpu = max(1, available_vcpus // AWS_VCPUS_PER_INSTANCE)
            
            # Also consider a practical limit to avoid overwhelming AWS
            # Leave buffer for stability (calculated from global config)
            max_workers_practical = min(max_workers_by_vcpu, AWS_MAX_WORKER_INSTANCES)
            
            recommended_workers = min(self.max_workers, max_workers_practical)
            
            logger.info(f"AWS Resource Analysis:")
            logger.info(f"  Available vCPUs: {available_vcpus}")
            logger.info(f"  Max workers by vCPU: {max_workers_by_vcpu}")
            logger.info(f"  Requested workers: {self.max_workers}")
            logger.info(f"  Recommended workers: {recommended_workers}")
            
            return recommended_workers
            
        except Exception as e:
            logger.warning(f"Could not check AWS resources: {e}")
            # If we can't check, be conservative and allow only 1 worker
            return 1


def main():
    """Main function"""
    global termination_event, is_terminating
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    
    # Register signal handlers
    logger.info(f"[MAIN] Registering signal handlers (SIGINT={signal.SIGINT}, SIGTERM={signal.SIGTERM})...")
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    logger.info(f"✅ [MAIN] Signal handlers registered successfully")
    
    parser = argparse.ArgumentParser(description="Agent-as-a-Judge GUI Batch Evaluator")
    parser.add_argument(
        "--pairs-root-dir",
        "--pairs_root_dir",
        dest="pairs_root_dir",
        default="src/data/GUI",
        help="root directory containing GUI pairs (default: src/data/GUI)",
    )
    parser.add_argument(
        "--output-dir",
        "--output_dir",
        dest="output_dir",
        default=None,
        help="output directory for results (default: Agent-as-a-Judge_GUI)",
    )
    parser.add_argument("--model", default="gpt-4o", help="model name")
    parser.add_argument("--effort", default="medium", choices=["low", "medium", "high"], help="effort level")
    parser.add_argument(
        "--observation-type",
        "--observation_type",
        dest="observation_type",
        default="a11y_tree",
        choices=["screenshot", "a11y_tree", "screenshot_a11y_tree"],
        help="observation type",
    )
    parser.add_argument("--provider", default="aws", help="provider")
    parser.add_argument("--region", default="us-east-1", help="region")
    parser.add_argument(
        "--max-workers",
        "--max_workers",
        dest="max_workers",
        type=int,
        default=1,
        help="maximum number of concurrent workers",
    )
    parser.add_argument("--temperature", type=float, default=None, help="temperature parameter")
    parser.add_argument(
        "--skip-completed",
        action="store_true",
        help="skip already-completed tasks",
    )
    parser.add_argument(
        "--no-resume",
        "--no_resume",
        dest="no_resume",
        action="store_true",
        help="do not skip already-completed tasks (re-evaluate everything)",
    )
    parser.add_argument(
        "--subdomain",
        default="ALL",
        choices=["ALL", "PPT", "Word", "Excel"],
        help="which subdomain under pairs_root_dir to evaluate (default: ALL)",
    )
    parser.add_argument(
        "--env-file",
        "--env_file",
        dest="env_file",
        default=".mcp_env",
        help="path to env file with API keys (default: .mcp_env)",
    )
    
    args = parser.parse_args()

    # Backward-compatible behavior: --skip-completed and --no-resume are opposite controls.
    # If both are passed, --no-resume takes priority.
    if args.skip_completed and not args.no_resume:
        args.no_resume = False

    # Load environment variables before checking API keys
    load_dotenv(dotenv_path=args.env_file, override=False)

    if args.output_dir is None:
        args.output_dir = "Agent-as-a-Judge_GUI"
    
    # At least one API key must be present
    model = args.model or "gpt-4o"
    if not (os.getenv("OPENAI_API_KEY") or os.getenv("DEEPSEEK_API_KEY")):
        logger.error(
            "Please set API Key before running the batch evaluator."
        )
        sys.exit(1)
    
    try:
        # Create evaluator
        evaluator = BatchEvaluatorMCP(
            pairs_root_dir=args.pairs_root_dir,
            output_dir=args.output_dir,
            model=model,
            effort=args.effort,
            observation_type=args.observation_type,
            provider=args.provider,
            region=args.region,
            max_workers=args.max_workers,
            temperature=args.temperature,
            subdomain=args.subdomain
        )
        
        # Run evaluation
        skip_completed = args.skip_completed or (not args.no_resume)
        summary = evaluator.run_batch_evaluation(skip_completed=skip_completed)
        
        print("\n" + "="*50)
        print("BATCH EVALUATION SUMMARY (MCP)")
        print("="*50)
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        print("="*50)
    
    except KeyboardInterrupt:
        print("\n🔔 [MAIN] Main process received KeyboardInterrupt.", flush=True)
        logger.info("🔔 [MAIN] KeyboardInterrupt caught in main()")
        # Signal handler will take care of cleanup
        is_terminating = True
        logger.info("✅ [MAIN] Set is_terminating=True")
        if termination_event is not None:
            termination_event.set()
            logger.info("✅ [MAIN] Set termination_event")
        else:
            logger.warning("⚠️  [MAIN] termination_event is None")
    except Exception as e:
        if not is_terminating:
            logger.error(f"Unexpected error in main process: {e}", exc_info=True)
            # Also trigger cleanup for unhandled exceptions
            is_terminating = True
            if termination_event is not None:
                termination_event.set()
            signal_handler(signal.SIGTERM, None)
    finally:
        # Final cleanup in case any processes remain
        logger.info("🧹 [MAIN_FINALLY] Entering finally block for final cleanup...")
        if not is_terminating:
            logger.info("[MAIN_FINALLY] is_terminating=False, performing final cleanup...")
        else:
            logger.info("[MAIN_FINALLY] is_terminating=True, cleanup already in progress...")
        
        if termination_event is not None:
            try:
                termination_event.set()
                logger.info("✅ [MAIN_FINALLY] Set termination_event")
            except Exception as e:
                logger.warning(f"⚠️  [MAIN_FINALLY] Failed to set termination_event: {e}")
            finally:
                termination_event = None
                logger.info("[MAIN_FINALLY] Cleared termination_event reference")
        
        # Check process status before cleanup
        if processes:
            logger.info(f"📊 [MAIN_FINALLY] Process status before cleanup ({len(processes)} processes):")
            alive_count = 0
            for idx, p in enumerate(processes):
                if p is not None:
                    alive = p.is_alive()
                    if alive:
                        alive_count += 1
                    pid = p.pid if hasattr(p, 'pid') else 'N/A'
                    exitcode = p.exitcode if hasattr(p, 'exitcode') else 'N/A'
                    logger.info(f"  [{idx}] {p.name}: PID={pid}, alive={alive}, exitcode={exitcode}")
            logger.info(f"📊 [MAIN_FINALLY] {alive_count}/{len(processes)} processes still alive")
        
        # First try gentle termination
        if processes:
            logger.info("📤 [MAIN_FINALLY] Attempting gentle termination...")
            terminated_count = 0
            for idx, p in enumerate(processes):
                if p is not None and p.is_alive():
                    try:
                        pid = p.pid if hasattr(p, 'pid') else 'N/A'
                        logger.info(f"  [{idx}] Calling terminate() on {p.name} (PID={pid})...")
                        p.terminate()
                        terminated_count += 1
                        logger.info(f"  ✅ [{idx}] terminate() called on {p.name}")
                    except Exception as e:
                        logger.error(f"  ❌ [{idx}] Error terminating {p.name}: {e}")
            logger.info(f"📊 [MAIN_FINALLY] Called terminate() on {terminated_count} processes")
        
        # Wait briefly for processes to terminate
        logger.info("⏳ [MAIN_FINALLY] Waiting 0.5s for processes to terminate...")
        time.sleep(0.5)
        
        # Check status after wait
        if processes:
            still_alive = []
            for idx, p in enumerate(processes):
                if p is not None and p.is_alive():
                    still_alive.append((idx, p))
            if still_alive:
                logger.warning(f"⚠️  [MAIN_FINALLY] {len(still_alive)} processes still alive after wait")
            else:
                logger.info(f"✅ [MAIN_FINALLY] All processes terminated gracefully")
        
        # Then force kill if needed
        if processes:
            logger.info("💀 [MAIN_FINALLY] Force killing remaining processes...")
            force_killed_count = 0
            for idx, p in enumerate(processes):
                if p is not None and p.is_alive():
                    try:
                        pid = p.pid if hasattr(p, 'pid') else 'N/A'
                        logger.warning(f"  [{idx}] Sending SIGKILL to {p.name} (PID={pid})...")
                        os.kill(p.pid, signal.SIGKILL)
                        force_killed_count += 1
                        logger.info(f"  ✅ [{idx}] SIGKILL sent to {p.name}")
                    except (ProcessLookupError, OSError) as e:
                        logger.debug(f"  [{idx}] Process {p.name} already dead: {e}")
                    except Exception as e:
                        logger.error(f"  ❌ [{idx}] Error killing {p.name}: {e}")
            if force_killed_count > 0:
                logger.warning(f"💀 [MAIN_FINALLY] Force killed {force_killed_count} processes")
        
        # Terminate worker AWS instances as final cleanup
        try:
            logger.info("🧹 [MAIN_FINALLY] Terminating worker AWS instances as final cleanup...")
            region = os.getenv('AWS_REGION', 'us-east-1')
            terminate_worker_aws_instances(region=region)
        except Exception as e:
            logger.error(f"❌ [MAIN_FINALLY] Error terminating worker AWS instances: {e}")
        
        logger.info("🏁 [MAIN_FINALLY] Final cleanup complete")


if __name__ == "__main__":
    main()

