#!/usr/bin/env python3
"""
Task replay program.
Supports initializing task environment and re-executing saved trajectories.
"""
import argparse
import datetime
import json
import logging
import os
import sys
import time
from pathlib import Path
from typing import Dict, Any, Optional, List

import sys
import os
from pathlib import Path

current_dir = Path(__file__).parent
osworld_modules_dir = current_dir.parent
src_dir = osworld_modules_dir.parent.parent
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

try:
    from mcp_services.gui.osworld_modules.desktop_env.desktop_env import DesktopEnv
except ImportError:
    from ..desktop_env.desktop_env import DesktopEnv

from .lib_replay_trajectory import load_trajectory, replay_trajectory

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s %(levelname)s %(name)s] %(message)s',
    handlers=[
        logging.StreamHandler(),
    ]
)
logger = logging.getLogger(__name__)


class TaskReplayManager:
    """Task replay manager."""
    
    def __init__(self, provider: str = "aws", region: str = "us-east-1"):
        self.provider = provider
        self.region = region
        self.env = None
        
    def find_task_config(self, task_id: str, base_dir: str = "../evaluation_examples") -> Optional[str]:
        """
        Find task configuration file by task ID.
        
        Args:
            task_id: Task ID
            base_dir: Base directory for configuration files.
            
        Returns:
            Task configuration file path, or None if not found.
        """
        base_path = Path(base_dir) / "examples"
        
        for domain_dir in base_path.iterdir():
            if domain_dir.is_dir():
                config_file = domain_dir / f"{task_id}.json"
                if config_file.exists():
                    logger.info(f"Found task config: {config_file}")
                    return str(config_file)
        
        logger.error(f"Task config not found for task ID: {task_id}")
        return None
    
    def load_task_config(self, config_path: str) -> Dict[str, Any]:
        """
        Load task configuration file.
        
        Args:
            config_path: Configuration file path.
            
        Returns:
            Task configuration dictionary.
        """
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Task config file not found: {config_path}")
        
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        logger.info(f"Loaded task config from: {config_path}")
        logger.info(f"Task instruction: {config.get('instruction', 'N/A')}")
        return config
    
    def initialize_environment(self, task_config: Dict[str, Any], 
                             screen_width: int = 1920, screen_height: int = 1080,
                             headless: bool = True) -> DesktopEnv:
        """
        Initialize task environment.
        
        Args:
            task_config: Task configuration.
            screen_width: Screen width.
            screen_height: Screen height.
            headless: Whether to run in headless mode.
            
        Returns:
            Initialized desktop environment.
        """
        logger.info(f"Initializing environment with provider: {self.provider}")
        
        observation_type = "screenshot"
        require_a11y_tree = False
        
        try:
            if self.provider == "aws":
                if (screen_width, screen_height) != (1920, 1080):
                    logger.warning(f"Screen size ({screen_width}, {screen_height}) not supported on AWS {self.region}. Falling back to (1920, 1080)")
                    screen_width, screen_height = 1920, 1080
            env = DesktopEnv(
                provider_name=self.provider,
                region=self.region if self.provider == "aws" else None,
                action_space="pyautogui",
                screen_size=(screen_width, screen_height),
                headless=headless,
                os_type="Ubuntu",
                require_a11y_tree=require_a11y_tree,
            )
            
            logger.info("Desktop environment created successfully")
            
            self.env = env
            return env
            
        except Exception as e:
            logger.error(f"Failed to initialize environment: {e}")
            raise
    
    def parse_trajectory_actions(self, trajectory: List[Dict[str, Any]]) -> List[str]:
        """
        Parse actions from trajectory.
        
        Args:
            trajectory: Trajectory data.
            
        Returns:
            List of actions.
        """
        actions = []
        for step in trajectory:
            action = step.get("action")
            if action:
                actions.append(action)
                logger.debug(f"Step {step.get('step_num', '?')}: {action}")
        
        logger.info(f"Parsed {len(actions)} actions from trajectory")
        return actions
    
    def _perform_initial_click(self, env, task_config: Dict[str, Any], screen_width: int, screen_height: int, debug_mode: bool = False):
        """
        Execute initial click to close default popup.
        
        Args:
            env: Environment instance.
            task_config: Task configuration.
            screen_width: Screen width.
            screen_height: Screen height.
            debug_mode: Debug mode.
        """
        try:
            app_type = self._detect_app_type(task_config)
            click_x, click_y = self._get_click_coordinate(app_type, screen_width, screen_height)
            
            logger.info(f"Executing initial click - Application: {app_type}, Coordinates: ({click_x}, {click_y})")
            
            click_action = f"pyautogui.click({click_x}, {click_y})"
            env.step(click_action, pause=1.0)
            
            logger.info("✅ Initial click executed successfully")
                    
        except Exception as e:
            logger.error(f"Initial click execution failed: {e}")
    
    def _detect_app_type(self, task_config: Dict[str, Any]) -> str:
        """Detect application type."""
        try:
            from .click_coordinates import click_coordinates
        except ImportError:
            from click_coordinates import click_coordinates
        return click_coordinates.detect_app_type_from_config(task_config)
    
    def _get_click_coordinate(self, app_type: str, screen_width: int, screen_height: int) -> tuple:
        """Get click coordinates."""
        try:
            from .click_coordinates import click_coordinates
        except ImportError:
            from click_coordinates import click_coordinates
        return click_coordinates.get_coordinate(app_type, screen_width, screen_height)
    
    def _capture_coordinate_grid(self, env, result_dir: str):
        """Capture screenshot with coordinate grid."""
        try:
            try:
                from .coordinate_detector import CoordinateDetector
            except ImportError:
                from coordinate_detector import CoordinateDetector
            
            detector = CoordinateDetector()
            grid_path = detector.capture_screenshot_with_grid(env, result_dir)
            
            if grid_path:
                logger.info(f"Coordinate grid image saved to: {grid_path}")
                logger.info("Please check the image to determine click coordinates, then update coordinate configuration")
            else:
                logger.warning("Unable to generate coordinate grid image")
                
        except Exception as e:
            logger.error(f"Coordinate detection failed: {e}")
    
    def replay_task(self, trajectory_path: str, task_id: str = None, 
                   task_config_path: str = None, result_dir: str = None,
                   sleep_after_execution: float = 1.0, wait_for_vnc: bool = True,
                   vnc_wait_timeout: int = 60, screen_width: int = 1920, 
                   screen_height: int = 1080, original_screen_size: tuple = None,
                   debug_mode: bool = False, enable_click: bool = False) -> Dict[str, Any]:
        """
        Replay task.
        
        Args:
            trajectory_path: Trajectory file path.
            task_id: Task ID (if task_config_path not provided).
            task_config_path: Task configuration file path.
            result_dir: Result save directory.
            
        Returns:
            Replay results.
        """
        logger.info("Starting task replay...")
        
        trajectory = load_trajectory(trajectory_path)
        logger.info(f"Loaded trajectory with {len(trajectory)} steps")
        
        if task_config_path:
            config_path = task_config_path
        elif task_id:
            config_path = self.find_task_config(task_id)
            if not config_path:
                raise ValueError(f"Cannot find task config for task ID: {task_id}")
        else:
            raise ValueError("Either task_id or task_config_path must be provided")
        
        task_config = self.load_task_config(config_path)
        
        if not result_dir:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            result_dir = f"replay_results/{task_id or 'unknown'}_{timestamp}"
        
        os.makedirs(result_dir, exist_ok=True)
        logger.info(f"Results will be saved to: {result_dir}")
        
        start_time = time.time()
        start_timestamp = datetime.datetime.now()
        
        try:
            env = self.initialize_environment(task_config, screen_width=screen_width, screen_height=screen_height)
            
            if hasattr(self, '_detect_coordinates') and self._detect_coordinates:
                self._capture_coordinate_grid(env, result_dir)
            
            actions = self.parse_trajectory_actions(trajectory)
            
            target_screen_size = (screen_width, screen_height)
            replay_results = replay_trajectory(
                env=env,
                trajectory=trajectory,
                sleep_after_execution=sleep_after_execution,
                save_replay_results=True,
                replay_result_dir=result_dir,
                wait_for_vnc=wait_for_vnc,
                vnc_wait_timeout=vnc_wait_timeout,
                task_config=task_config,
                original_screen_size=original_screen_size,
                target_screen_size=target_screen_size,
                debug_mode=debug_mode,
                enable_click=enable_click
            )
            
            config_copy_path = os.path.join(result_dir, "original_task_config.json")
            with open(config_copy_path, 'w', encoding='utf-8') as f:
                json.dump(task_config, f, indent=2, ensure_ascii=False)
            
            end_time = time.time()
            end_timestamp = datetime.datetime.now()
            total_duration = end_time - start_time
            
            log_data = {
                "basic_info": {
                    "task_id": task_id,
                    "instruction": task_config.get("instruction", "N/A"),
                    "start_time": start_timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                    "end_time": end_timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                    "total_duration": f"{int(total_duration // 60)}m{int(total_duration % 60)}s",
                    "total_steps": len(trajectory),
                    "successful_steps": replay_results["successful_steps"],
                    "failed_steps": replay_results["failed_steps"],
                    "success_rate": f"{replay_results['successful_steps'] / len(trajectory) * 100:.1f}%" if len(trajectory) > 0 else "0%"
                },
                "action_execution_details": []
            }
            
            for i, step in enumerate(trajectory):
                step_num = step.get("step_num", i + 1)
                original_action = step.get("action", "")
                
                replay_action_info = None
                for replay_action in replay_results.get("replay_actions", []):
                    if replay_action.get("step_num") == step_num:
                        replay_action_info = replay_action
                        break
                
                step_info = {
                    "step": step_num,
                    "original_action": original_action,
                    "execution_status": "success" if replay_action_info and replay_action_info.get("success") else "failed"
                }
                
                if replay_action_info:
                    executed_action = replay_action_info.get("executed_action", "")
                    step_info["executed_action"] = executed_action
                    step_info["execution_time"] = f"{replay_action_info.get('execution_time', 0):.3f}s"
                    
                    if original_action != executed_action:
                        step_info["action_modified"] = "yes"
                        step_info["modification_reason"] = "coordinate_scaling" if replay_action_info.get("action_modified") else "other"
                    else:
                        step_info["action_modified"] = "no"
                    
                    if not replay_action_info.get("success") and replay_action_info.get("error"):
                        step_info["error"] = replay_action_info.get("error")
                else:
                    step_info["executed_action"] = "not_executed"
                    step_info["execution_time"] = "0.000s"
                    step_info["action_modified"] = "no"
                
                log_data["action_execution_details"].append(step_info)
            
            log_path = os.path.join(result_dir, "replay_summary.json")
            with open(log_path, 'w', encoding='utf-8') as f:
                json.dump(log_data, f, indent=2, ensure_ascii=False)
            
            logger.info("Task replay completed successfully")
            logger.info(f"Total execution time: {log_data['basic_info']['total_duration']}")
            logger.info(f"Original steps: {len(trajectory)}")
            logger.info(f"Successful steps: {replay_results['successful_steps']}")
            logger.info(f"Failed steps: {replay_results['failed_steps']}")
            logger.info(f"Success rate: {log_data['basic_info']['success_rate']}")
            logger.info(f"Final result: {replay_results['final_result']}")
            logger.info(f"Replay log saved to: {log_path}")
            
            return replay_results
            
        except Exception as e:
            logger.error(f"Task replay failed: {e}")
            raise
        finally:
            if self.env:
                try:
                    self.env.close()
                    logger.info("Environment closed successfully")
                except Exception as e:
                    logger.warning(f"Failed to close environment: {e}")


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Task Replay Tool")
    
    parser.add_argument("--trajectory_path", required=True,
                       help="Path to the trajectory file (traj.jsonl)")
    
    parser.add_argument("--task_id", 
                       help="Task ID (UUID format)")
    parser.add_argument("--task_config_path",
                       help="Path to task configuration file")
    
    parser.add_argument("--provider", default="aws", 
                       choices=["aws", "vmware", "docker", "virtualbox"],
                       help="Virtualization provider")
    parser.add_argument("--region", default="us-east-1",
                       help="AWS region (only for AWS provider)")
    
    parser.add_argument("--screen_width", type=int, default=1920,
                       help="Screen width (default: 1920 for AWS)")
    parser.add_argument("--screen_height", type=int, default=1080,
                       help="Screen height (default: 1080 for AWS)")
    parser.add_argument("--original_screen_width", type=int,
                       help="Original screen width when trajectory was recorded (for coordinate scaling)")
    parser.add_argument("--original_screen_height", type=int,
                       help="Original screen height when trajectory was recorded (for coordinate scaling)")
    parser.add_argument("--headless", action="store_true", default=True,
                       help="Run in headless mode")
    parser.add_argument("--enable_click", action="store_true",
                       help="Enable initial click to close default popup before replaying trajectory")
    parser.add_argument("--detect_coordinates", action="store_true",
                       help="Capture screenshot with coordinate grid to help determine click coordinates")
    
    parser.add_argument("--result_dir",
                       help="Directory to save replay results")
    
    parser.add_argument("--sleep_after_execution", type=float, default=1.0,
                       help="Sleep time after each step execution (seconds)")
    parser.add_argument("--vnc_wait_timeout", type=int, default=120,
                       help="Timeout for waiting VNC to be ready (seconds)")
    parser.add_argument("--no_wait_vnc", action="store_true",
                       help="Skip waiting for VNC to be ready")
    parser.add_argument("--debug", action="store_true",
                       help="Enable debug mode with detailed action logging and coordinate annotation")
    
    args = parser.parse_args()
    
    if not args.task_id and not args.task_config_path:
        parser.error("Either --task_id or --task_config_path must be provided")
    
    if not os.path.exists(args.trajectory_path):
        parser.error(f"Trajectory file not found: {args.trajectory_path}")
    
    try:
        replay_manager = TaskReplayManager(
            provider=args.provider,
            region=args.region
        )
        
        original_screen_size = None
        if args.original_screen_width and args.original_screen_height:
            original_screen_size = (args.original_screen_width, args.original_screen_height)
            logger.info(f"Will use coordinate scaling: original({args.original_screen_width}x{args.original_screen_height}) -> target({args.screen_width}x{args.screen_height})")
        
        if args.detect_coordinates:
            replay_manager._detect_coordinates = True
        
        results = replay_manager.replay_task(
            trajectory_path=args.trajectory_path + "/traj.jsonl",
            task_id=args.task_id,
            task_config_path=args.task_config_path,
            result_dir=args.result_dir,
            sleep_after_execution=args.sleep_after_execution,
            wait_for_vnc=not args.no_wait_vnc,
            vnc_wait_timeout=args.vnc_wait_timeout,
            screen_width=args.screen_width,
            screen_height=args.screen_height,
            original_screen_size=original_screen_size,
            debug_mode=args.debug,
            enable_click=args.enable_click
        )
        
        print("\n" + "="*60)
        print("TASK REPLAY COMPLETED")
        print("="*60)
        print(f"Original steps: {results['total_steps']}")
        print(f"Successful steps: {results['successful_steps']}")
        print(f"Failed steps: {results['failed_steps']}")
        print(f"Final result: {results['final_result']}")
        
        if results['final_result'] is not None:
            success_rate = results['final_result']
            print(f"Success rate: {success_rate:.2%}")
        
    except Exception as e:
        logger.error(f"Program failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
