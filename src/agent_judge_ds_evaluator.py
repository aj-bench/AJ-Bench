"""
Judge Evaluator for MCPMark

This evaluator replays previous agent trajectories and uses a judge agent
to verify whether the task was completed successfully. The judge agent can
interact with the environment to check key verification points.

Key Features:
- Load and replay previous interaction trajectories
- Initialize environment state based on trajectory replay
- Use judge agent to verify task completion by interacting with environment
- Compare judge results with ground truth labels
- **Parallel execution support**: Run multiple evaluations concurrently with isolated environments
"""

import asyncio
import atexit
import json
import multiprocessing
import os
import signal
import threading
import time
from concurrent.futures import as_completed, ProcessPoolExecutor
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from src.agents import AGENT_REGISTRY
from src.factory import MCPServiceFactory
from src.logger import get_logger
from src.model_config import ModelConfig
from src.results_reporter import ResultsReporter

logger = get_logger(__name__)

# Thread-local storage for state managers in parallel execution
_thread_local = threading.local()

# Global executor reference for cleanup on exit
_global_executor: Optional[ProcessPoolExecutor] = None
_global_child_pids: set = set()  # Track child process PIDs
_executor_lock = threading.Lock()
_main_pid = os.getpid()  # Store the main process PID


def _kill_child_processes():
    """Forcefully kill all tracked child processes."""
    global _global_child_pids
    with _executor_lock:
        for pid in list(_global_child_pids):
            try:
                os.kill(pid, signal.SIGKILL)
                logger.debug(f"Killed child process {pid}")
            except (ProcessLookupError, OSError):
                pass  # Process already dead
        _global_child_pids.clear()


def _cleanup_executor():
    """Clean up the global executor on exit."""
    global _global_executor, _global_child_pids
    with _executor_lock:
        if _global_executor is not None:
            try:
                # Get PIDs from executor's internal process dict
                if (
                    hasattr(_global_executor, "_processes")
                    and _global_executor._processes is not None
                ):
                    for pid in _global_executor._processes.keys():
                        _global_child_pids.add(pid)
                _global_executor.shutdown(wait=False, cancel_futures=True)
            except Exception:
                pass
            _global_executor = None

    # Forcefully kill any remaining child processes
    _kill_child_processes()


def _signal_handler(signum, frame):
    """Handle interrupt signals by cleaning up executor and exiting."""
    logger = get_logger(__name__)
    logger.warning(f"Received signal {signum}, shutting down all child processes...")
    _cleanup_executor()
    # Restore default signal handler and re-raise
    signal.signal(signum, signal.SIG_DFL)
    os.kill(os.getpid(), signum)


# Register cleanup handlers
atexit.register(_cleanup_executor)


def _run_judge_task_in_process(args: tuple) -> "JudgeResult":
    """
    Top-level function for running judge task in a subprocess.

    This function is defined at module level to be picklable for multiprocessing.
    Each subprocess gets its own PID, ensuring isolated backup directories.

    Args:
        args: Tuple containing (evaluator_config, traj_info_dict, task_index, total_tasks, parent_pid)

    Returns:
        JudgeResult with evaluation outcome
    """
    evaluator_config, traj_info_dict, task_index, total_tasks, parent_pid = args

    # Set up a watchdog to check if parent is still alive
    def check_parent_alive():
        """Periodically check if parent process is alive, exit if not."""
        while True:
            time.sleep(2)  # Check every 2 seconds
            try:
                os.kill(parent_pid, 0)  # Signal 0 checks if process exists
            except OSError:
                # Parent is dead, exit immediately
                logger = get_logger(__name__)
                logger.warning(
                    f"Parent process {parent_pid} died, exiting child {os.getpid()}"
                )
                os._exit(1)

    # Start watchdog thread
    watchdog = threading.Thread(target=check_parent_alive, daemon=True)
    watchdog.start()

    # Reconstruct TrajectoryInfo from dict
    traj_info = TrajectoryInfo(
        task_path=traj_info_dict["task_path"],
        trajectory_path=Path(traj_info_dict["trajectory_path"]),
        ground_truth=traj_info_dict["ground_truth"],
        category=traj_info_dict["category"],
        task_name=traj_info_dict["task_name"],
        run_id=traj_info_dict["run_id"],
    )

    # Create a new JudgeEvaluator instance in this subprocess
    evaluator = JudgeEvaluator(
        mcp_service=evaluator_config["mcp_service"],
        model=evaluator_config["model"],
        trajectory_dir=evaluator_config["trajectory_dir"],
        tasks_dir=evaluator_config["tasks_dir"],
        timeout=evaluator_config["timeout"],
        exp_name=evaluator_config["exp_name"],
        output_dir=(
            Path(evaluator_config["output_dir"])
            if evaluator_config["output_dir"]
            else None
        ),
        reasoning_effort=evaluator_config["reasoning_effort"],
        agent_name=evaluator_config["agent_name"],
        max_tasks=evaluator_config["max_tasks"],
        max_parallel_tasks=1,  # Each subprocess handles one task
    )

    # Run the task with isolated state manager
    result = evaluator._run_single_judge_task_isolated(
        traj_info, task_index, total_tasks
    )
    return result


@dataclass
class TrajectoryInfo:
    """Information about a trajectory to evaluate."""

    task_path: str  # e.g., "filesystem/desktop__music_report"
    trajectory_path: Path  # Full path to the trajectory directory
    ground_truth: str  # "success" or "fail"
    category: str  # e.g., "filesystem"
    task_name: str  # e.g., "desktop__music_report"
    run_id: str  # e.g., "claude-opus-4-1_run-1"


@dataclass
class JudgeResult:
    """Result from the judge agent's evaluation."""

    task_path: str
    trajectory_path: str
    ground_truth: str
    judge_verdict: Optional[str] = None  # "PASS" or "FAIL"
    is_correct: Optional[bool] = None
    judge_output: Optional[List[Dict[str, Any]]] = None
    token_usage: Optional[Dict[str, int]] = None
    turn_count: Optional[int] = None
    execution_time: float = 0.0
    error: Optional[str] = None


@dataclass
class JudgeStats:
    """Statistics for judge evaluation."""

    total: int = 0
    correct: int = 0
    incorrect: int = 0
    errors: int = 0

    true_positives: int = 0  # Ground truth: success, Judge: PASS
    true_negatives: int = 0  # Ground truth: fail, Judge: FAIL
    false_positives: int = 0  # Ground truth: fail, Judge: PASS
    false_negatives: int = 0  # Ground truth: success, Judge: FAIL

    # Model information
    model: Optional[str] = None
    reasoning_effort: Optional[str] = None

    # Token usage
    total_input_tokens: int = 0
    total_output_tokens: int = 0
    total_reasoning_tokens: int = 0

    @property
    def accuracy(self) -> float:
        evaluated = self.total - self.errors
        return self.correct / evaluated if evaluated > 0 else 0.0

    @property
    def precision(self) -> float:
        denom = self.true_positives + self.false_positives
        return self.true_positives / denom if denom > 0 else 0.0

    @property
    def recall(self) -> float:
        denom = self.true_positives + self.false_negatives
        return self.true_positives / denom if denom > 0 else 0.0

    @property
    def f1_score(self) -> float:
        if self.precision + self.recall == 0:
            return 0.0
        return 2 * (self.precision * self.recall) / (self.precision + self.recall)


class JudgeEvaluator:
    """
    Evaluator that replays trajectories and uses a judge agent to verify task completion.

    The workflow:
    1. Collect trajectories from the specified directory
    2. For each trajectory:
       a. Set up the environment state (same as original evaluation)
       b. Replay the trajectory to bring environment to post-execution state
       c. Create judge agent with verification prompt
       d. Let judge agent interact with environment to verify completion
       e. Extract verdict from judge output
    3. Compare verdicts with ground truth and report statistics
    """

    JUDGE_SYSTEM_PROMPT = """You are a verification agent. Your task is to verify whether a previous agent successfully completed a given task.

You have access to the same tools as the original agent. Use these tools to:
1. Inspect the current state of the environment
2. Check if the expected outputs/changes exist
3. Verify the correctness of any created or modified resources

After your investigation, provide your final verdict in the following format:
- If the task was completed successfully: "VERDICT: PASS"
- If the task was not completed or completed incorrectly: "VERDICT: FAIL"

Be thorough in your verification. Check all aspects of the task requirements."""

    def __init__(
        self,
        mcp_service: str,
        model: str,
        trajectory_dir: str = "mcpmark-trajectory-log/mcpmark-selected-v3",
        tasks_dir: str = "tasks",
        timeout: int = 300,
        exp_name: str = "judge-eval",
        output_dir: Path = None,
        reasoning_effort: str = "default",
        agent_name: str = "mcpmark",
        max_tasks: Optional[int] = None,
        max_parallel_tasks: int = 1,
        skip_completed: bool = False,
    ):
        self.mcp_service = mcp_service
        self.timeout = timeout
        self.agent_name = (agent_name or "mcpmark").lower()
        if self.agent_name not in AGENT_REGISTRY:
            raise ValueError(
                f"Unsupported agent '{agent_name}'. Available: {sorted(AGENT_REGISTRY)}"
            )

        self.reasoning_effort = reasoning_effort
        self.model_name = model
        self.max_tasks = max_tasks

        model_config = ModelConfig(self.model_name)
        self.api_key = model_config.api_key
        self.base_url = model_config.base_url
        self.litellm_input_model_name = model_config.litellm_input_model_name
        self.litellm_run_model_name = None

        # Paths
        self.base_dir = Path(".")
        self.trajectory_dir = self.base_dir / trajectory_dir
        self.tasks_dir = self.base_dir / tasks_dir

        # Initialize managers
        self.task_manager = MCPServiceFactory.create_task_manager(mcp_service)
        self.state_manager = MCPServiceFactory.create_state_manager(mcp_service)
        self.service_config = self.state_manager.get_service_config_for_agent()

        # Initialize agent (will be recreated per-task with judge prompt)
        agent_cls = AGENT_REGISTRY[self.agent_name]
        self.agent_cls = agent_cls

        # Results
        self.results: List[JudgeResult] = []
        self.stats = JudgeStats()
        self.results_reporter = ResultsReporter()

        # Parallel execution settings
        self.max_parallel_tasks: int = max_parallel_tasks
        self._results_lock = threading.Lock()  # Lock for thread-safe results collection

        # Skip completed trajectories
        self.skip_completed = skip_completed

        # Output directory
        if self.reasoning_effort != "default":
            model_slug = self.model_name.replace(".", "-") + "-" + self.reasoning_effort
        else:
            model_slug = self.model_name.replace(".", "-")

        service_for_dir = (
            "playwright" if mcp_service == "playwright_webarena" else mcp_service
        )
        self.base_experiment_dir = (
            (output_dir or Path("results"))
            / f"judge__{model_slug}__{service_for_dir}"
            / exp_name
        )
        self.base_experiment_dir.mkdir(parents=True, exist_ok=True)

    def _format_duration(self, seconds: float) -> str:
        return f"{(seconds * 1000):.2f}ms" if seconds < 1 else f"{seconds:.2f}s"

    def collect_trajectories(self) -> List[TrajectoryInfo]:
        """Collect all trajectories from the trajectory directory for the current MCP service."""
        trajectories = []

        # The structure is: trajectory_dir / category / task_name / {success,fail} / run_id
        service_dir = self.trajectory_dir / self.mcp_service
        if not service_dir.exists():
            logger.warning(f"Service directory not found: {service_dir}")
            return trajectories

        # Iterate through task directories
        for task_dir in service_dir.iterdir():
            if not task_dir.is_dir():
                continue

            task_name = task_dir.name
            task_path = f"{self.mcp_service}/{task_name}"

            # Check success and fail subdirectories
            for label_dir in ["success", "fail"]:
                label_path = task_dir / label_dir
                if not label_path.exists() or not label_path.is_dir():
                    continue

                # Iterate through individual runs
                for run_dir in label_path.iterdir():
                    if not run_dir.is_dir():
                        continue

                    # Check if messages.json exists
                    if not (run_dir / "messages.json").exists():
                        continue

                    trajectories.append(
                        TrajectoryInfo(
                            task_path=task_path,
                            trajectory_path=run_dir,
                            ground_truth=label_dir,
                            category=self.mcp_service,
                            task_name=task_name,
                            run_id=run_dir.name,
                        )
                    )

        return trajectories

    def _is_trajectory_completed(self, traj_info: TrajectoryInfo) -> bool:
        """
        Check if a trajectory has already been evaluated.

        A trajectory is considered completed if its output directory contains
        a valid judge_meta.json file with a non-null judge_verdict.

        Args:
            traj_info: Trajectory information to check

        Returns:
            True if the trajectory has already been evaluated, False otherwise
        """
        output_dir = (
            self.base_experiment_dir
            / traj_info.task_name
            / traj_info.ground_truth
            / traj_info.run_id
        )
        meta_path = output_dir / "judge_meta.json"

        if not meta_path.exists():
            return False

        try:
            with open(meta_path, "r", encoding="utf-8") as f:
                meta_data = json.load(f)
            # Consider completed if judge_verdict is not None and no error
            has_verdict = meta_data.get("judge_verdict") is not None
            no_error = meta_data.get("error") is None
            return has_verdict and no_error
        except Exception as e:
            logger.warning(f"Error reading meta file {meta_path}: {e}")
            return False

    def _filter_completed_trajectories(
        self, trajectories: List[TrajectoryInfo]
    ) -> tuple[List[TrajectoryInfo], List[TrajectoryInfo]]:
        """
        Filter out already completed trajectories.

        Args:
            trajectories: List of trajectories to filter

        Returns:
            Tuple of (pending_trajectories, completed_trajectories)
        """
        pending = []
        completed = []

        for traj in trajectories:
            if self._is_trajectory_completed(traj):
                completed.append(traj)
            else:
                pending.append(traj)

        return pending, completed

    def _load_all_results_from_output_dir(self) -> List[JudgeResult]:
        """
        Load all judge results from the output directory.

        This method scans the base_experiment_dir for all judge_meta.json files
        and reconstructs JudgeResult objects from them. This is used to calculate
        statistics from ALL results (including previously completed ones), not just
        the results from the current execution.

        Returns:
            List of JudgeResult objects loaded from the output directory
        """
        all_results = []

        # Scan the base_experiment_dir for all judge_meta.json files
        # Structure: base_experiment_dir / task_name / ground_truth / run_id / judge_meta.json
        if not self.base_experiment_dir.exists():
            logger.warning(
                f"Output directory does not exist: {self.base_experiment_dir}"
            )
            return all_results

        for task_dir in self.base_experiment_dir.iterdir():
            if not task_dir.is_dir():
                continue

            for label_dir in task_dir.iterdir():
                if not label_dir.is_dir():
                    continue

                for run_dir in label_dir.iterdir():
                    if not run_dir.is_dir():
                        continue

                    meta_path = run_dir / "judge_meta.json"
                    if not meta_path.exists():
                        continue

                    try:
                        with open(meta_path, "r", encoding="utf-8") as f:
                            meta_data = json.load(f)

                        result = JudgeResult(
                            task_path=meta_data.get("task_path", ""),
                            trajectory_path=meta_data.get("trajectory_path", ""),
                            ground_truth=meta_data.get("ground_truth", ""),
                            judge_verdict=meta_data.get("judge_verdict"),
                            is_correct=meta_data.get("is_correct"),
                            token_usage=meta_data.get("token_usage"),
                            turn_count=meta_data.get("turn_count"),
                            execution_time=meta_data.get("execution_time", 0.0),
                            error=meta_data.get("error"),
                        )
                        all_results.append(result)
                    except Exception as e:
                        logger.warning(f"Error loading result from {meta_path}: {e}")
                        continue

        logger.info(f"Loaded {len(all_results)} results from output directory")
        return all_results

    def load_trajectory(self, trajectory_path: Path) -> Optional[List[Dict[str, Any]]]:
        """Load trajectory messages from a directory."""
        messages_path = trajectory_path / "messages.json"

        if not messages_path.exists():
            return None

        try:
            with open(messages_path, "r", encoding="utf-8") as f:
                messages = json.load(f)
            return messages
        except Exception as e:
            logger.error(f"Error loading trajectory from {trajectory_path}: {e}")
            return None

    def find_task_description(self, task_path: str) -> Optional[str]:
        """Find and read the task description for a given task path."""
        # task_path format: category/subcategory__task_name
        # e.g., filesystem/desktop__music_report -> tasks/filesystem/desktop/music_report/description.md
        parts = task_path.split("/")
        if len(parts) != 2:
            return None

        category = parts[0]
        task_parts = parts[1].split("__")
        if len(task_parts) != 2:
            return None

        subcategory = task_parts[0]
        task_name = task_parts[1]

        description_path = (
            self.tasks_dir / category / subcategory / task_name / "description.md"
        )

        if description_path.exists():
            return description_path.read_text(encoding="utf-8")

        return None

    def get_task_from_path(self, task_name: str):
        """Get the task object from task name (e.g., 'desktop__music_report')."""
        # Parse task name to get category_id and task_id
        parts = task_name.split("__")
        if len(parts) != 2:
            return None

        category_id = parts[0]
        task_id = parts[1]

        # Use task manager to filter and find the specific task
        task_filter = f"{category_id}/{task_id}"
        tasks = self.task_manager.filter_tasks(task_filter)

        return tasks[0] if tasks else None

    def format_trajectory_for_judge(
        self, messages: List[Dict[str, Any]], task_description: str
    ) -> str:
        """Format trajectory and task description into a judge prompt."""
        trajectory_parts = []

        # Skip the last message if it's from assistant
        if messages and messages[-1].get("role") == "assistant":
            messages = messages[:-1]

        for msg in messages:
            role = msg.get("role")
            msg_type = msg.get("type")

            if role == "user":
                # content = msg.get("content", "")
                # if isinstance(content, str):
                #     trajectory_parts.append(f"[ORIGINAL USER]: {content[:500]}...")
                pass
            elif role == "assistant":
                content = msg.get("content", [])
                if isinstance(content, list):
                    for c in content:
                        if isinstance(c, dict) and c.get("type") == "output_text":
                            text = c.get("text", "")
                            if text:
                                trajectory_parts.append(
                                    f"[ORIGINAL AGENT]: {text[:200]}..."
                                )
                elif isinstance(content, str):
                    trajectory_parts.append(f"[ORIGINAL AGENT]: {content[:200]}...")
            elif msg_type == "function_call":
                name = msg.get("name", "unknown")
                args = msg.get("arguments", "{}")
                if len(args) > 100:
                    args = args[:100] + "..."
                trajectory_parts.append(f"[TOOL CALL] {name}: {args}")
            elif msg_type == "function_call_output":
                # output = msg.get("output", "")
                # if len(output) > 200:
                #     output = output[:200] + "... [truncated]"
                # trajectory_parts.append(f"[TOOL OUTPUT]: {output}")
                pass

        trajectory_text = "\n".join(trajectory_parts[-30:])  # Keep last 30 entries

        judge_prompt = f"""# Task Description
{task_description}

# Previous Agent Trajectory (Summary)
The following is a summary of what the previous agent did:

{trajectory_text}

# Your Verification Task
The previous agent claimed to have completed the task above. Your job is to verify whether the task was actually completed successfully.

Use the available tools to:
1. Check the current state of the environment
2. Verify that the expected outputs/changes exist
3. Confirm the correctness of any created or modified resources

After your investigation, provide your final verdict:
- "VERDICT: PASS" if the task was completed successfully
- "VERDICT: FAIL" if the task was not completed or was completed incorrectly

Be thorough and check all requirements mentioned in the task description."""

        return judge_prompt

    def extract_verdict(self, messages: List[Dict[str, Any]]) -> str:
        """Extract the verdict from judge agent's output."""
        # Search through messages in reverse order to find the verdict
        for msg in reversed(messages):
            content = msg.get("content", "")

            # Handle list content (SDK format)
            if isinstance(content, list):
                for item in content:
                    if isinstance(item, dict) and item.get("type") == "output_text":
                        text = item.get("text", "").upper()
                        if "VERDICT: PASS" in text or "VERDICT:PASS" in text:
                            return "PASS"
                        if "VERDICT: FAIL" in text or "VERDICT:FAIL" in text:
                            return "FAIL"
            elif isinstance(content, str):
                text = content.upper()
                if "VERDICT: PASS" in text or "VERDICT:PASS" in text:
                    return "PASS"
                if "VERDICT: FAIL" in text or "VERDICT:FAIL" in text:
                    return "FAIL"

        # If no explicit verdict found, try to infer from last message
        if messages:
            last_msg = messages[-1]
            content = last_msg.get("content", "")
            if isinstance(content, list):
                for item in content:
                    if isinstance(item, dict) and item.get("type") == "output_text":
                        text = item.get("text", "").upper()
                        if "PASS" in text and "FAIL" not in text:
                            return "PASS"
                        if "FAIL" in text:
                            return "FAIL"
            elif isinstance(content, str):
                text = content.upper()
                if "PASS" in text and "FAIL" not in text:
                    return "PASS"
                if "FAIL" in text:
                    return "FAIL"

        return "UNKNOWN"

    def _requires_path_replacement(self) -> bool:
        """
        Check if the current MCP service requires path replacement during trajectory replay.

        Only filesystem-based services need path replacement because they use
        backup directories with process-specific paths that differ between runs.

        Returns:
            True if path replacement is needed, False otherwise
        """
        # Only filesystem service requires path replacement
        # Other services (postgres, notion, github, etc.) don't need it
        return self.mcp_service == "filesystem"

    def _extract_original_test_directory(
        self, messages: List[Dict[str, Any]]
    ) -> Optional[str]:
        """
        Extract the original test directory from trajectory messages.
        Looks for paths matching the .mcpmark_backups pattern in tool call arguments.

        This is only relevant for filesystem MCP service.
        """
        if not self._requires_path_replacement():
            return None

        import re

        backup_pattern = re.compile(r"(/[^\"'\s]+/\.mcpmark_backups/backup_[^/\"'\s]+)")

        for msg in messages:
            if msg.get("type") == "function_call":
                args_str = msg.get("arguments", "{}")
                if isinstance(args_str, str):
                    match = backup_pattern.search(args_str)
                    if match:
                        return match.group(1)
                elif isinstance(args_str, dict):
                    args_json = json.dumps(args_str)
                    match = backup_pattern.search(args_json)
                    if match:
                        return match.group(1)
        return None

    def _replace_paths_in_args(
        self, args: Dict[str, Any], original_path: str, current_path: str
    ) -> Dict[str, Any]:
        """
        Replace original test directory paths with current test directory paths in arguments.
        """
        if not original_path or not current_path:
            return args

        def replace_in_value(value):
            if isinstance(value, str):
                return value.replace(original_path, current_path)
            elif isinstance(value, dict):
                return {k: replace_in_value(v) for k, v in value.items()}
            elif isinstance(value, list):
                return [replace_in_value(item) for item in value]
            else:
                return value

        return replace_in_value(args)

    def _replace_github_owner_in_args(self, args: Dict[str, Any]) -> Dict[str, Any]:
        """
        Replace GitHub owner from mcpmark-eval to mcpmark-eval-swtuser in arguments.

        This is needed during replay because the original trajectory was recorded
        with mcpmark-eval but we need to replay on mcpmark-eval-swtuser.
        """
        if not isinstance(args, dict):
            return args

        result = args.copy()
        if "owner" in result and result["owner"] == "mcpmark-eval":
            result["owner"] = "mcpmark-eval-swtuser"
            logger.debug("Replaced GitHub owner: mcpmark-eval -> mcpmark-eval-swtuser")

        return result

    async def _replay_trajectory_on_environment(
        self,
        task,
        messages: List[Dict[str, Any]],
        log_file_path: Optional[str] = None,
    ) -> bool:
        """
        Replay a trajectory on the environment by executing the tool calls.
        This brings the environment to the state after the original agent executed.

        Returns True if replay was successful.
        """
        # Get fresh service config after state setup (important for filesystem which needs test_directory)
        current_service_config = self.state_manager.get_service_config_for_agent()

        # Extract original test directory from trajectory for path replacement
        # This is only needed for filesystem service
        original_test_directory = None
        current_test_directory = None

        if self._requires_path_replacement():
            original_test_directory = self._extract_original_test_directory(messages)
            current_test_directory = current_service_config.get("test_directory")

            if original_test_directory and current_test_directory:
                msg = f"Path replacement enabled: {original_test_directory} -> {current_test_directory}"
                logger.info(msg)
            elif original_test_directory:
                msg = f"Original test directory found ({original_test_directory}) but no current test directory available"
                logger.warning(msg)
        else:
            logger.debug(
                f"Path replacement not required for MCP service: {self.mcp_service}"
            )

        # Create MCP server for replaying
        agent = self.agent_cls(
            litellm_input_model_name=self.litellm_input_model_name,
            api_key=self.api_key,
            base_url=self.base_url,
            mcp_service=self.mcp_service,
            timeout=self.timeout,
            service_config=current_service_config,
            service_config_provider=self.state_manager.get_service_config_for_agent,
            reasoning_effort=self.reasoning_effort,
        )

        mcp_server = await agent._create_mcp_server()

        # Track replay operations for logging
        executed_operations = []
        failed_operations = []

        # Helper function to write to log file
        def write_log(message: str):
            if log_file_path:
                with open(log_file_path, "a", encoding="utf-8") as f:
                    f.write(f"{message}\n")

        try:
            async with mcp_server:
                # Extract and execute tool calls from the trajectory
                for msg in messages:
                    msg_type = msg.get("type")

                    if msg_type == "function_call":
                        name = msg.get("name")
                        args_str = msg.get("arguments", "{}")

                        try:
                            args = (
                                json.loads(args_str)
                                if isinstance(args_str, str)
                                else args_str
                            )
                        except json.JSONDecodeError:
                            args = {}

                        # Replace paths in arguments if path replacement is enabled
                        if original_test_directory and current_test_directory:
                            args = self._replace_paths_in_args(
                                args, original_test_directory, current_test_directory
                            )

                        # Replace GitHub owner if this is a GitHub service
                        if self.mcp_service == "github":
                            args = self._replace_github_owner_in_args(args)

                        try:
                            logger.debug(f"Replaying tool call: {name}")
                            write_log(f"[Replay] | {name} {json.dumps(args)}")
                            await asyncio.wait_for(
                                mcp_server.call_tool(name, args), timeout=30
                            )
                            executed_operations.append(
                                {"name": name, "args": args, "status": "success"}
                            )
                            logger.info(f"Replay executed: {name} with args: {args}")
                        except Exception as e:
                            failed_operations.append(
                                {"name": name, "args": args, "error": str(e)}
                            )
                            logger.warning(f"Tool call replay failed for {name}: {e}")
                            write_log(f"[Replay] | [FAILED] {name}: {e}")
                            # Continue with other tool calls
                            continue

            # Log replay summary
            total_operations = len(executed_operations) + len(failed_operations)
            summary_msg = f"Replay summary: {len(executed_operations)}/{total_operations} operations succeeded"
            logger.info(summary_msg)
            write_log(f"\n{'=' * 60}")
            write_log(f"[Replay Summary] {summary_msg}")
            if executed_operations:
                executed_msg = (
                    f"Executed operations: {[op['name'] for op in executed_operations]}"
                )
                logger.info(executed_msg)
                write_log(f"[Replay Summary] {executed_msg}")
            if failed_operations:
                failed_msg = (
                    f"Failed operations: {[op['name'] for op in failed_operations]}"
                )
                logger.warning(failed_msg)
                write_log(f"[Replay Summary] {failed_msg}")
            write_log(f"{'=' * 60}\n")

            return True
        except Exception as e:
            logger.error(f"Trajectory replay failed: {e}")
            logger.error(
                f"Partial replay - executed {len(executed_operations)} operations before failure"
            )
            write_log(f"[Replay ERROR] Trajectory replay failed: {e}")
            write_log(
                f"[Replay ERROR] Partial replay - executed {len(executed_operations)} operations before failure"
            )
            return False

    def _run_single_judge_task(self, traj_info: TrajectoryInfo) -> JudgeResult:
        """Run the judge agent for a single trajectory."""
        start_time = time.time()

        result = JudgeResult(
            task_path=traj_info.task_path,
            trajectory_path=str(traj_info.trajectory_path),
            ground_truth=traj_info.ground_truth,
        )

        # Load trajectory
        messages = self.load_trajectory(traj_info.trajectory_path)
        if not messages:
            result.error = f"Could not load trajectory from {traj_info.trajectory_path}"
            result.execution_time = time.time() - start_time
            return result

        # Get task description
        task_description = self.find_task_description(traj_info.task_path)
        if not task_description:
            result.error = f"Could not find task description for {traj_info.task_path}"
            result.execution_time = time.time() - start_time
            return result

        # Get task object
        task = self.get_task_from_path(traj_info.task_name)
        if not task:
            result.error = f"Could not find task object for {traj_info.task_name}"
            result.execution_time = time.time() - start_time
            return result

        logger.info(
            f"\n┌─ Judge Evaluation: {traj_info.task_path} ({traj_info.run_id})"
        )
        logger.info(f"| Ground Truth: {traj_info.ground_truth}")

        # Create output directory for this evaluation (moved earlier to enable replay logging)
        output_dir = (
            self.base_experiment_dir
            / traj_info.task_name
            / traj_info.ground_truth
            / traj_info.run_id
        )
        output_dir.mkdir(parents=True, exist_ok=True)
        execution_log_path = output_dir / "judge_execution.log"

        # Stage 1: Set up initial state
        logger.info("| Stage 1: Setting up initial state...")
        setup_success = self.state_manager.set_up(task)
        if not setup_success:
            result.error = "State setup failed"
            result.execution_time = time.time() - start_time
            self.state_manager.clean_up(task)
            return result

        # Stage 2: Replay trajectory
        logger.info("| Stage 2: Replaying trajectory...")
        try:
            replay_success = asyncio.run(
                self._replay_trajectory_on_environment(
                    task, messages, str(execution_log_path)
                )
            )
            if not replay_success:
                logger.warning(
                    "| Trajectory replay had some failures, continuing with judge..."
                )
        except Exception as e:
            logger.error(f"| Trajectory replay failed: {e}")

        # Stage 3: Create judge prompt and execute judge agent
        logger.info("| Stage 3: Running judge agent...")
        judge_prompt = self.format_trajectory_for_judge(messages, task_description)

        # Get fresh service config after replay (important for using the environment state after replay)
        current_service_config = self.state_manager.get_service_config_for_agent()

        # Create judge agent with the environment that has been through replay
        agent = self.agent_cls(
            litellm_input_model_name=self.litellm_input_model_name,
            api_key=self.api_key,
            base_url=self.base_url,
            mcp_service=self.mcp_service,
            timeout=self.timeout,
            service_config=current_service_config,
            service_config_provider=self.state_manager.get_service_config_for_agent,
            reasoning_effort=self.reasoning_effort,
        )

        try:
            agent_result = agent.execute_sync(judge_prompt, str(execution_log_path))

            result.judge_output = agent_result.get("output", [])
            result.token_usage = agent_result.get("token_usage", {})
            result.turn_count = agent_result.get("turn_count", 0)

            if agent_result.get("litellm_run_model_name"):
                self.litellm_run_model_name = agent_result["litellm_run_model_name"]

            # Extract verdict from judge output
            result.judge_verdict = self.extract_verdict(result.judge_output)

            # Determine if judgment is correct
            expected = "PASS" if traj_info.ground_truth == "success" else "FAIL"
            result.is_correct = result.judge_verdict == expected

            logger.info(f"| Judge Verdict: {result.judge_verdict}")
            logger.info(f"| Expected: {expected}")
            logger.info(f"| Correct: {result.is_correct}")

        except Exception as e:
            result.error = str(e)
            logger.error(f"| Judge agent failed: {e}")

        # Stage 4: Cleanup
        logger.info("| Stage 4: Cleaning up...")
        self.state_manager.clean_up(task)

        result.execution_time = time.time() - start_time
        logger.info(f"└─ Completed in {self._format_duration(result.execution_time)}")

        # Save judge messages
        if result.judge_output:
            messages_path = output_dir / "judge_messages.json"
            self.results_reporter.save_messages_json(result.judge_output, messages_path)

        # Save meta info
        meta_path = output_dir / "judge_meta.json"
        meta_data = {
            "task_path": result.task_path,
            "trajectory_path": result.trajectory_path,
            "ground_truth": result.ground_truth,
            "judge_verdict": result.judge_verdict,
            "is_correct": result.is_correct,
            "token_usage": result.token_usage,
            "turn_count": result.turn_count,
            "execution_time": result.execution_time,
            "error": result.error,
            "model": self.model_name,
            "timestamp": datetime.now().isoformat(),
        }
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(meta_data, f, indent=2, ensure_ascii=False)

        return result

    def calculate_stats(self, results: Optional[List[JudgeResult]] = None):
        """Calculate statistics from results.

        Args:
            results: List of results to calculate stats from. If None, loads all results
                from the experiment output directory.
        """
        self.stats = JudgeStats()

        # Set model and reasoning effort information
        self.stats.model = self.model_name
        self.stats.reasoning_effort = self.reasoning_effort

        if results is not None:
            results_to_process = results
        else:
            # Default: load all results from output directory
            results_to_process = self._load_all_results_from_output_dir()

        for result in results_to_process:
            self.stats.total += 1

            # Accumulate token usage
            if result.token_usage:
                self.stats.total_input_tokens += result.token_usage.get(
                    "input_tokens", 0
                )
                self.stats.total_output_tokens += result.token_usage.get(
                    "output_tokens", 0
                )
                self.stats.total_reasoning_tokens += result.token_usage.get(
                    "reasoning_tokens", 0
                )

            if result.error:
                self.stats.errors += 1
                continue

            if result.is_correct:
                self.stats.correct += 1
            else:
                self.stats.incorrect += 1

            # Confusion matrix
            if result.ground_truth == "success" and result.judge_verdict == "PASS":
                self.stats.true_positives += 1
            elif result.ground_truth == "fail" and result.judge_verdict == "FAIL":
                self.stats.true_negatives += 1
            elif result.ground_truth == "fail" and result.judge_verdict == "PASS":
                self.stats.false_positives += 1
            elif result.ground_truth == "success" and result.judge_verdict == "FAIL":
                self.stats.false_negatives += 1

    def run_evaluation(self, task_filter: str = "all") -> JudgeStats:
        """Run the full judge evaluation."""
        logger.info("Collecting trajectories...")
        trajectories = self.collect_trajectories()

        # Apply task filter if specified
        if task_filter.lower() != "all":
            filtered = []
            for traj in trajectories:
                if "/" in task_filter:
                    # Specific task filter (category_id/task_id)
                    if task_filter in traj.task_path:
                        filtered.append(traj)
                else:
                    # Category filter
                    if traj.task_name.startswith(task_filter):
                        filtered.append(traj)
            trajectories = filtered

        logger.info(f"Found {len(trajectories)} trajectories to evaluate")

        if not trajectories:
            logger.warning("No trajectories to evaluate!")
            # Still calculate stats from any existing results in output directory
            self.calculate_stats()
            return self.stats

        # Limit tasks if specified
        if self.max_tasks is not None and self.max_tasks > 0:
            trajectories = trajectories[: self.max_tasks]
            logger.info(f"Limiting evaluation to {len(trajectories)} tasks")

        # Run evaluation for each trajectory
        for i, traj_info in enumerate(trajectories):
            logger.info(f"\n{'=' * 60}")
            logger.info(f"{'=' * 60}")

            result = self._run_single_judge_task(traj_info)
            self.results.append(result)

        # Calculate statistics
        self.calculate_stats()

        return self.stats

    def print_report(self):
        """Print evaluation report."""
        print("\n" + "=" * 80)
        print("JUDGE EVALUATOR REPORT")
        print("=" * 80)

        print("\n📊 OVERALL STATISTICS")
        print("-" * 40)
        print(f"Total Evaluations: {self.stats.total}")
        print(f"Correct Judgments: {self.stats.correct}")
        print(f"Incorrect Judgments: {self.stats.incorrect}")
        print(f"Errors: {self.stats.errors}")
        print(f"\n✅ Accuracy: {self.stats.accuracy:.2%}")
        print(f"📈 Precision: {self.stats.precision:.2%}")
        print(f"📉 Recall: {self.stats.recall:.2%}")
        print(f"🎯 F1 Score: {self.stats.f1_score:.2%}")

        print("\n📋 CONFUSION MATRIX")
        print("-" * 40)
        print(f"True Positives (Success -> PASS): {self.stats.true_positives}")
        print(f"True Negatives (Fail -> FAIL): {self.stats.true_negatives}")
        print(f"False Positives (Fail -> PASS): {self.stats.false_positives}")
        print(f"False Negatives (Success -> FAIL): {self.stats.false_negatives}")

        # Statistics by task
        task_stats: Dict[str, Dict] = {}
        for result in self.results:
            task = result.task_path
            if task not in task_stats:
                task_stats[task] = {
                    "total": 0,
                    "correct": 0,
                    "incorrect": 0,
                    "errors": 0,
                }

            task_stats[task]["total"] += 1
            if result.error:
                task_stats[task]["errors"] += 1
            elif result.is_correct:
                task_stats[task]["correct"] += 1
            else:
                task_stats[task]["incorrect"] += 1

        print("\n📝 STATISTICS BY TASK")
        print("-" * 40)
        for task, stats in sorted(task_stats.items()):
            valid = stats["total"] - stats["errors"]
            accuracy = stats["correct"] / valid if valid > 0 else 0
            print(f"\n{task}:")
            print(
                f"  Total: {stats['total']}, Correct: {stats['correct']}, Incorrect: {stats['incorrect']}, Errors: {stats['errors']}"
            )
            print(f"  Accuracy: {accuracy:.2%}")

        # Incorrect judgments
        incorrect = [r for r in self.results if r.is_correct is False]
        if incorrect:
            print(f"\n❌ INCORRECT JUDGMENTS ({len(incorrect)})")
            print("-" * 40)
            for result in incorrect:
                print(f"\nTask: {result.task_path}")
                print(f"Run: {result.trajectory_path.split('/')[-1]}")
                print(f"Ground Truth: {result.ground_truth}")
                print(f"Judge Verdict: {result.judge_verdict}")

        print("\n" + "=" * 80)

    def save_results(self, output_path: Optional[str] = None):
        """Save results to JSON file."""
        if output_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = self.base_experiment_dir / f"judge_results_{timestamp}.json"
        else:
            output_path = Path(output_path)

        output_data = {
            "timestamp": datetime.now().isoformat(),
            "model": self.model_name,
            "mcp_service": self.mcp_service,
            "trajectory_dir": str(self.trajectory_dir),
            "stats": {
                "total": self.stats.total,
                "correct": self.stats.correct,
                "incorrect": self.stats.incorrect,
                "errors": self.stats.errors,
                "accuracy": self.stats.accuracy,
                "precision": self.stats.precision,
                "recall": self.stats.recall,
                "f1_score": self.stats.f1_score,
                "true_positives": self.stats.true_positives,
                "true_negatives": self.stats.true_negatives,
                "false_positives": self.stats.false_positives,
                "false_negatives": self.stats.false_negatives,
            },
            "results": [
                {
                    "task_path": r.task_path,
                    "trajectory_path": r.trajectory_path,
                    "ground_truth": r.ground_truth,
                    "judge_verdict": r.judge_verdict,
                    "is_correct": r.is_correct,
                    "token_usage": r.token_usage,
                    "turn_count": r.turn_count,
                    "execution_time": r.execution_time,
                    "error": r.error,
                }
                for r in self.results
            ],
        }

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)

        logger.info(f"Results saved to {output_path}")
        return output_path

    def _run_single_judge_task_isolated(
        self, traj_info: TrajectoryInfo, task_index: int, total_tasks: int
    ) -> JudgeResult:
        """
        Run the judge agent for a single trajectory with isolated state manager.

        This method creates its own state manager instance to ensure complete isolation
        between parallel task executions. Each task operates on its own backup directory.

        Args:
            traj_info: Trajectory information to evaluate
            task_index: Index of current task (for logging)
            total_tasks: Total number of tasks (for logging)

        Returns:
            JudgeResult with evaluation outcome
        """
        process_id = os.getpid()
        start_time = time.time()

        result = JudgeResult(
            task_path=traj_info.task_path,
            trajectory_path=str(traj_info.trajectory_path),
            ground_truth=traj_info.ground_truth,
        )

        logger.info(
            f"[PID-{process_id}] Starting task {task_index + 1}/{total_tasks}: "
            f"{traj_info.task_name} ({traj_info.run_id})"
        )

        # Create isolated state manager for this thread/task
        isolated_state_manager = MCPServiceFactory.create_state_manager(
            self.mcp_service
        )

        # Load trajectory
        messages = self.load_trajectory(traj_info.trajectory_path)
        if not messages:
            result.error = f"Could not load trajectory from {traj_info.trajectory_path}"
            result.execution_time = time.time() - start_time
            return result

        # Get task description
        task_description = self.find_task_description(traj_info.task_path)
        if not task_description:
            result.error = f"Could not find task description for {traj_info.task_path}"
            result.execution_time = time.time() - start_time
            return result

        # Get task object
        task = self.get_task_from_path(traj_info.task_name)
        if not task:
            result.error = f"Could not find task object for {traj_info.task_name}"
            result.execution_time = time.time() - start_time
            return result

        logger.info(
            f"[PID-{process_id}] ┌─ Judge Evaluation: {traj_info.task_path} ({traj_info.run_id})"
        )
        logger.info(f"[PID-{process_id}] | Ground Truth: {traj_info.ground_truth}")

        # Create output directory for this evaluation
        output_dir = (
            self.base_experiment_dir
            / traj_info.task_name
            / traj_info.ground_truth
            / traj_info.run_id
        )
        output_dir.mkdir(parents=True, exist_ok=True)
        execution_log_path = output_dir / "judge_execution.log"

        # Stage 1: Set up initial state with isolated state manager
        logger.info(f"[PID-{process_id}] | Stage 1: Setting up initial state...")
        setup_success = isolated_state_manager.set_up(task)
        if not setup_success:
            result.error = "State setup failed"
            result.execution_time = time.time() - start_time
            isolated_state_manager.clean_up(task)
            return result

        # Stage 2: Replay trajectory
        logger.info(f"[PID-{process_id}] | Stage 2: Replaying trajectory...")
        try:
            replay_success = asyncio.run(
                self._replay_trajectory_on_environment_isolated(
                    task, messages, str(execution_log_path), isolated_state_manager
                )
            )
            if not replay_success:
                logger.warning(
                    f"[PID-{process_id}] | Trajectory replay had some failures, continuing with judge..."
                )
        except Exception as e:
            logger.error(f"[PID-{process_id}] | Trajectory replay failed: {e}")

        # Stage 3: Create judge prompt and execute judge agent
        logger.info(f"[PID-{process_id}] | Stage 3: Running judge agent...")
        judge_prompt = self.format_trajectory_for_judge(messages, task_description)

        # Get fresh service config after replay
        current_service_config = isolated_state_manager.get_service_config_for_agent()

        # Create judge agent with the isolated environment
        agent = self.agent_cls(
            litellm_input_model_name=self.litellm_input_model_name,
            api_key=self.api_key,
            base_url=self.base_url,
            mcp_service=self.mcp_service,
            timeout=self.timeout,
            service_config=current_service_config,
            service_config_provider=isolated_state_manager.get_service_config_for_agent,
            reasoning_effort=self.reasoning_effort,
        )

        try:
            agent_result = agent.execute_sync(judge_prompt, str(execution_log_path))

            result.judge_output = agent_result.get("output", [])
            result.token_usage = agent_result.get("token_usage", {})
            result.turn_count = agent_result.get("turn_count", 0)

            if agent_result.get("litellm_run_model_name"):
                self.litellm_run_model_name = agent_result["litellm_run_model_name"]

            # Extract verdict from judge output
            result.judge_verdict = self.extract_verdict(result.judge_output)

            # Determine if judgment is correct
            expected = "PASS" if traj_info.ground_truth == "success" else "FAIL"
            result.is_correct = result.judge_verdict == expected

            logger.info(f"[PID-{process_id}] | Judge Verdict: {result.judge_verdict}")
            logger.info(f"[PID-{process_id}] | Expected: {expected}")
            logger.info(f"[PID-{process_id}] | Correct: {result.is_correct}")

        except Exception as e:
            result.error = str(e)
            logger.error(f"[PID-{process_id}] | Judge agent failed: {e}")

        # Stage 4: Cleanup
        logger.info(f"[PID-{process_id}] | Stage 4: Cleaning up...")
        isolated_state_manager.clean_up(task)

        result.execution_time = time.time() - start_time
        logger.info(
            f"[PID-{process_id}] └─ Completed in {self._format_duration(result.execution_time)}"
        )

        # Save judge messages
        if result.judge_output:
            messages_path = output_dir / "judge_messages.json"
            self.results_reporter.save_messages_json(result.judge_output, messages_path)

        # Save meta info
        meta_path = output_dir / "judge_meta.json"
        meta_data = {
            "task_path": result.task_path,
            "trajectory_path": result.trajectory_path,
            "ground_truth": result.ground_truth,
            "judge_verdict": result.judge_verdict,
            "is_correct": result.is_correct,
            "token_usage": result.token_usage,
            "turn_count": result.turn_count,
            "execution_time": result.execution_time,
            "error": result.error,
            "model": self.model_name,
            "timestamp": datetime.now().isoformat(),
            "process_id": process_id,
        }
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(meta_data, f, indent=2, ensure_ascii=False)

        return result

    async def _replay_trajectory_on_environment_isolated(
        self,
        task,
        messages: List[Dict[str, Any]],
        log_file_path: Optional[str] = None,
        isolated_state_manager=None,
    ) -> bool:
        """
        Replay a trajectory on the environment with an isolated state manager.

        This variant uses a provided isolated state manager instead of self.state_manager,
        ensuring proper isolation in parallel execution.

        Args:
            task: The task being evaluated
            messages: List of trajectory messages
            log_file_path: Path to log file for replay operations
            isolated_state_manager: The isolated state manager for this execution

        Returns:
            True if replay was successful
        """
        state_manager = isolated_state_manager or self.state_manager

        # Get fresh service config after state setup
        current_service_config = state_manager.get_service_config_for_agent()

        # Extract original test directory from trajectory for path replacement
        # This is only needed for filesystem service
        original_test_directory = None
        current_test_directory = None

        if self._requires_path_replacement():
            original_test_directory = self._extract_original_test_directory(messages)
            current_test_directory = current_service_config.get("test_directory")

            if original_test_directory and current_test_directory:
                msg = f"Path replacement enabled: {original_test_directory} -> {current_test_directory}"
                logger.info(msg)
            elif original_test_directory:
                msg = f"Original test directory found ({original_test_directory}) but no current test directory available"
                logger.warning(msg)
        else:
            logger.debug(
                f"Path replacement not required for MCP service: {self.mcp_service}"
            )

        # Create MCP server for replaying
        agent = self.agent_cls(
            litellm_input_model_name=self.litellm_input_model_name,
            api_key=self.api_key,
            base_url=self.base_url,
            mcp_service=self.mcp_service,
            timeout=self.timeout,
            service_config=current_service_config,
            service_config_provider=state_manager.get_service_config_for_agent,
            reasoning_effort=self.reasoning_effort,
        )

        mcp_server = await agent._create_mcp_server()

        # Track replay operations for logging
        executed_operations = []
        failed_operations = []

        # Helper function to write to log file
        def write_log(message: str):
            if log_file_path:
                with open(log_file_path, "a", encoding="utf-8") as f:
                    f.write(f"{message}\n")

        try:
            async with mcp_server:
                # Extract and execute tool calls from the trajectory
                for msg in messages:
                    msg_type = msg.get("type")

                    if msg_type == "function_call":
                        name = msg.get("name")
                        args_str = msg.get("arguments", "{}")

                        try:
                            args = (
                                json.loads(args_str)
                                if isinstance(args_str, str)
                                else args_str
                            )
                        except json.JSONDecodeError:
                            args = {}

                        # Replace paths in arguments if path replacement is enabled
                        if original_test_directory and current_test_directory:
                            args = self._replace_paths_in_args(
                                args, original_test_directory, current_test_directory
                            )

                        # Replace GitHub owner if this is a GitHub service
                        if self.mcp_service == "github":
                            args = self._replace_github_owner_in_args(args)

                        try:
                            logger.debug(f"Replaying tool call: {name}")
                            write_log(f"[Replay] | {name} {json.dumps(args)}")
                            await asyncio.wait_for(
                                mcp_server.call_tool(name, args), timeout=30
                            )
                            executed_operations.append(
                                {"name": name, "args": args, "status": "success"}
                            )
                            logger.info(f"Replay executed: {name} with args: {args}")
                        except Exception as e:
                            failed_operations.append(
                                {"name": name, "args": args, "error": str(e)}
                            )
                            logger.warning(f"Tool call replay failed for {name}: {e}")
                            write_log(f"[Replay] | [FAILED] {name}: {e}")
                            continue

            # Log replay summary
            total_operations = len(executed_operations) + len(failed_operations)
            summary_msg = f"Replay summary: {len(executed_operations)}/{total_operations} operations succeeded"
            logger.info(summary_msg)
            write_log(f"\n{'=' * 60}")
            write_log(f"[Replay Summary] {summary_msg}")
            if executed_operations:
                executed_msg = (
                    f"Executed operations: {[op['name'] for op in executed_operations]}"
                )
                logger.info(executed_msg)
                write_log(f"[Replay Summary] {executed_msg}")
            if failed_operations:
                failed_msg = (
                    f"Failed operations: {[op['name'] for op in failed_operations]}"
                )
                logger.warning(failed_msg)
                write_log(f"[Replay Summary] {failed_msg}")
            write_log(f"{'=' * 60}\n")

            return True
        except Exception as e:
            logger.error(f"Trajectory replay failed: {e}")
            logger.error(
                f"Partial replay - executed {len(executed_operations)} operations before failure"
            )
            write_log(f"[Replay ERROR] Trajectory replay failed: {e}")
            write_log(
                f"[Replay ERROR] Partial replay - executed {len(executed_operations)} operations before failure"
            )
            return False

    def run_evaluation_parallel(
        self, task_filter: str = "all", max_workers: Optional[int] = None
    ) -> JudgeStats:
        """
        Run the full judge evaluation in parallel with isolated environments.

        This method executes multiple trajectory evaluations concurrently, with each
        evaluation running in its own isolated backup environment to prevent interference.

        Args:
            task_filter: Filter for selecting trajectories ("all" or specific task pattern)
            max_workers: Maximum number of parallel workers (defaults to self.max_parallel_tasks)

        Returns:
            JudgeStats with aggregated evaluation statistics
        """
        logger.info("=" * 70)
        logger.info("PARALLEL JUDGE EVALUATION")
        logger.info("=" * 70)

        # Determine number of workers
        num_workers = max_workers or self.max_parallel_tasks
        logger.info(f"Max parallel workers: {num_workers}")

        # Collect trajectories
        logger.info("Collecting trajectories...")
        trajectories = self.collect_trajectories()

        # Apply task filter if specified
        if task_filter.lower() != "all":
            filtered = []
            for traj in trajectories:
                if "/" in task_filter:
                    if task_filter in traj.task_path:
                        filtered.append(traj)
                else:
                    if traj.task_name.startswith(task_filter):
                        filtered.append(traj)
            trajectories = filtered

        logger.info(f"Found {len(trajectories)} trajectories to evaluate")

        if not trajectories:
            logger.warning("No trajectories to evaluate!")
            # Still calculate stats from any existing results in output directory
            self.calculate_stats()
            return self.stats

        # Filter out completed trajectories if skip_completed is enabled
        skipped_count = 0
        if self.skip_completed:
            pending_trajectories, completed_trajectories = (
                self._filter_completed_trajectories(trajectories)
            )
            skipped_count = len(completed_trajectories)
            if skipped_count > 0:
                logger.info(f"Skipping {skipped_count} already completed trajectories")
                for traj in completed_trajectories:
                    logger.debug(f"  - Skipped: {traj.task_name} ({traj.run_id})")
            trajectories = pending_trajectories

            if not trajectories:
                logger.info("All trajectories have already been evaluated!")
                # Calculate stats from all existing results in output directory
                self.calculate_stats()
                return self.stats

        # Limit tasks if specified
        if self.max_tasks is not None and self.max_tasks > 0:
            trajectories = trajectories[: self.max_tasks]
            logger.info(f"Limiting evaluation to {len(trajectories)} tasks")

        total_tasks = len(trajectories)
        start_time = time.time()

        # Use ProcessPoolExecutor for parallel execution with process isolation
        # Each process gets its own PID, ensuring isolated backup directories via os.getpid()
        logger.info(
            f"\n🚀 Starting parallel evaluation with {num_workers} workers (multiprocessing)..."
        )
        logger.info("-" * 70)

        completed_count = 0
        error_count = 0

        # Prepare evaluator config for subprocess reconstruction
        # base_experiment_dir structure: output_dir / judge__model__service / exp_name
        # We need to extract the original output_dir (parent.parent) to avoid path duplication
        evaluator_config = {
            "mcp_service": self.mcp_service,
            "model": self.model_name,
            "trajectory_dir": str(self.trajectory_dir),
            "tasks_dir": str(self.tasks_dir),
            "timeout": self.timeout,
            "exp_name": self.base_experiment_dir.name,
            "output_dir": str(self.base_experiment_dir.parent.parent),
            "reasoning_effort": self.reasoning_effort,
            "agent_name": self.agent_name,
            "max_tasks": self.max_tasks,
        }

        # Prepare task arguments for multiprocessing
        # Include parent PID so children can detect if parent dies
        parent_pid = os.getpid()
        task_args = []
        for i, traj_info in enumerate(trajectories):
            traj_info_dict = {
                "task_path": traj_info.task_path,
                "trajectory_path": str(traj_info.trajectory_path),
                "ground_truth": traj_info.ground_truth,
                "category": traj_info.category,
                "task_name": traj_info.task_name,
                "run_id": traj_info.run_id,
            }
            task_args.append(
                (evaluator_config, traj_info_dict, i, total_tasks, parent_pid)
            )

        # Use spawn context for clean subprocess isolation
        mp_context = multiprocessing.get_context("spawn")

        # Set up signal handlers for graceful shutdown
        original_sigint = signal.signal(signal.SIGINT, _signal_handler)
        original_sigterm = signal.signal(signal.SIGTERM, _signal_handler)

        global _global_executor, _global_child_pids
        executor = ProcessPoolExecutor(max_workers=num_workers, mp_context=mp_context)

        with _executor_lock:
            _global_executor = executor
            _global_child_pids.clear()

        try:
            with executor:
                # Submit all tasks
                future_to_traj = {
                    executor.submit(_run_judge_task_in_process, args): trajectories[i]
                    for i, args in enumerate(task_args)
                }

                # Collect results as they complete
                for future in as_completed(future_to_traj):
                    traj_info = future_to_traj[future]
                    try:
                        result = future.result()

                        # Process-safe results collection (lock still works in main process)
                        with self._results_lock:
                            self.results.append(result)
                            completed_count += 1
                            if result.error:
                                error_count += 1

                            # Log progress
                            status = (
                                "✓"
                                if result.is_correct
                                else ("✗" if result.is_correct is False else "⚠")
                            )
                            logger.info(
                                f"[{completed_count}/{total_tasks}] {status} {traj_info.task_name} "
                                f"({traj_info.run_id}) - {result.judge_verdict or 'ERROR'}"
                            )

                    except Exception as e:
                        logger.error(
                            f"Task {traj_info.task_name} ({traj_info.run_id}) failed with exception: {e}"
                        )
                        with self._results_lock:
                            error_count += 1
                            self.results.append(
                                JudgeResult(
                                    task_path=traj_info.task_path,
                                    trajectory_path=str(traj_info.trajectory_path),
                                    ground_truth=traj_info.ground_truth,
                                    error=str(e),
                                )
                            )

        except KeyboardInterrupt:
            logger.warning("\nKeyboard interrupt received, shutting down...")
            # Forcefully terminate all child processes
            with _executor_lock:
                if hasattr(executor, "_processes") and executor._processes is not None:
                    for pid in executor._processes.keys():
                        try:
                            os.kill(pid, signal.SIGKILL)
                            logger.info(f"Killed child process {pid}")
                        except (ProcessLookupError, OSError):
                            pass
            executor.shutdown(wait=False, cancel_futures=True)
            raise
        finally:
            # Restore original signal handlers
            signal.signal(signal.SIGINT, original_sigint)
            signal.signal(signal.SIGTERM, original_sigterm)
            # Clean up executor and kill any remaining children
            with _executor_lock:
                if hasattr(executor, "_processes") and executor._processes is not None:
                    for pid in executor._processes.keys():
                        try:
                            os.kill(pid, signal.SIGTERM)
                        except (ProcessLookupError, OSError):
                            pass
                _global_executor = None
                _global_child_pids.clear()

        # Calculate total time
        total_time = time.time() - start_time

        logger.info("-" * 70)
        logger.info(
            f"✅ Parallel evaluation completed in {self._format_duration(total_time)}"
        )
        logger.info(
            f"   Completed: {completed_count}/{total_tasks}, Errors: {error_count}"
        )
        if self.skip_completed and skipped_count > 0:
            logger.info(f"   Skipped (already completed): {skipped_count}")

        # Average time per task (accounting for parallelism)
        if completed_count > 0:
            avg_time = total_time / completed_count * num_workers
            logger.info(
                f"   Average time per task (wall clock): {self._format_duration(avg_time)}"
            )

        # Load all existing results from output directory and calculate stats for ALL results
        all_results = self._load_all_results_from_output_dir()
        logger.info(
            f"\n📊 Calculating statistics from ALL {len(all_results)} results in output directory..."
        )

        # Calculate statistics using all results (not just this run)
        self.calculate_stats(all_results)

        return self.stats
