#!/usr/bin/env python3
"""
Single Judge Agent
"""

import os
import sys
import json
import logging
import time
import base64
from typing import Dict, Any, Optional, List
from pathlib import Path
from datetime import datetime, timezone

# add project root to path (so that "src" is found); remove script dir to avoid shadowing installed "mcp" package
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent
sys.path.insert(0, str(project_root))
script_dir = str(current_dir)
if script_dir in sys.path:
    sys.path.remove(script_dir)

# Import MCP Client
from src.mcp_services.gui.gui_mcp_client import GUIMCPClient, GUIMCPAdapter

# Import OpenAI
import openai

# Import OSWorld dependencies
from src.mcp_services.gui.osworld_modules.replay.lib_replay_trajectory import load_trajectory
from src.mcp_services.gui.osworld_modules.mm_agents.agent import linearize_accessibility_tree

# Import prompt templates
from src.agents.prompt.prompt_gui import (
    SINGLE_SYSTEM_PROMPT,
    SINGLE_USER_PROMPT,
    SINGLE_OBSERVATION_PROMPT,
    ACTION_SPACE_PROMPT,
    SINGLE_FINAL_JUDGMENT_PROMPT,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logging.getLogger('boto3').setLevel(logging.WARNING)
logging.getLogger('botocore').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)
logging.getLogger('s3transfer').setLevel(logging.WARNING)
logging.getLogger('boto').setLevel(logging.WARNING)


class RequeueTaskError(Exception):
    """Raised when a11y_tree load/save fails repeatedly; task should be re-queued for re-evaluation."""
    pass


class SingleJudgeAgentMCP:
    """
    Single Judge Agent
    """
    
    def __init__(self, model: str = "gpt-4o", temperature: Optional[float] = None, 
                 provider: str = "aws", region: str = "us-east-1",
                 screen_width: int = 1920, screen_height: int = 1080,
                 observation_type: str = "screenshot", trajectory_id: str = "unknown",
                 effort: str = "medium", output_dir: Optional[str] = None,
                 mcp_server_script: Optional[str] = None,
                 trajectory_type: Optional[str] = None,
                 worker_activity: Optional[dict] = None,
                 worker_name: Optional[str] = None):
        """
        Initialize the Single Judge Agent
        
        Args:
            model: model name
            temperature: temperature parameter (default: model default)
            provider: virtualization provider (now only support "aws")
            region: AWS region (default: "us-east-1", depends on the ami used)
            screen_width: screen width
            screen_height: screen height
            observation_type: observation type ("screenshot", "a11y_tree", "screenshot_a11y_tree")
            trajectory_id: trajectory id
            effort: effort level for models that support reasoning parameter
            output_dir: output directory
            mcp_server_script: MCP Server script path (optional)
            trajectory_type: trajectory type (optional: "true" or "false")
            worker_activity: shared worker activity tracking dictionary (optional)
            worker_name: Worker name (optional)
        """
        self.model = model
        self.temperature = temperature
        self.provider = provider
        self.region = region
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.observation_type = observation_type
        self.effort = effort
        self.trajectory_id = trajectory_id
        
        # Worker activity tracking (for stuck worker detection)
        self.worker_activity = worker_activity
        self.worker_name = worker_name
        
        # Initialize OpenAI client
        if self.model.startswith("deepseek"):
            api_key = os.getenv("DEEPSEEK_API_KEY")
            if not api_key:
                raise RuntimeError(
                    "DEEPSEEK_API_KEY not set, cannot create DeepSeek client."
                    "Please set DEEPSEEK_API_KEY in environment variables before running evaluation."
                )
            self.client = openai.OpenAI(
                base_url="https://api.deepseek.com",
                api_key=api_key
            )
        else:
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise RuntimeError(
                    "OPENAI_API_KEY not set, cannot create OpenAI client."
                    "Please set OPENAI_API_KEY in environment variables before running evaluation."
                )
            self.client = openai.OpenAI(
                api_key=api_key,
                base_url=os.getenv("OPENAI_BASE_URL") or None
            )
        
        # Initialize MCP Client
        self.mcp_client = GUIMCPClient(server_script=mcp_server_script)
        self.env = None
        self.replay_manager = None
        
        # Trajectory data
        self.trajectory = None
        self.task_config = None
        
        # Conversation history
        self.conversation_history = []
        
        # Ground truth tracking
        self.trajectory_path = None
        self.ground_truth = None
        self.trajectory_type = trajectory_type  # user specified trajectory type (true/false)
        
        # Pairs directory info (for loading screenshots from original trajectory)
        self.pairs_root_dir = None
        self.trajectory_dir = None  # pair_dir / trajectory_type
        
        # Logging directory
        self.session_timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        default_root_dir = Path(project_root) / "Agent-as-a-Judge_GUI"
        replay_root = Path(output_dir) if output_dir else default_root_dir
        
        # Extract trajectory type from trajectory_id
        if "_" in trajectory_id and trajectory_id.split("_")[-1] in ["true", "false"]:
            base_trajectory_id = "_".join(trajectory_id.split("_")[:-1])
            trajectory_type = trajectory_id.split("_")[-1]
            self.log_dir = replay_root / f"{base_trajectory_id}_{trajectory_type}_{self.session_timestamp}"
        else:
            self.log_dir = replay_root / f"{trajectory_id}_{self.session_timestamp}"
        
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.eval_log: List[Dict[str, Any]] = []
        
        # a11y_tree truncation configuration
        self._a11y_tree_max_chars = 15000
        # Consecutive a11y_tree load failures (VIEW_TRAJECTORY_STEP); if >= threshold, raise RequeueTaskError
        self._consecutive_a11y_load_failures = 0
        self._max_consecutive_a11y_load_failures = 3
        
        logger.info(f"Single Judge Agent initialized with model: {model}")
    
    def load_task_data(self, pairs_root_dir: str, task_id: str, trajectory_type: str):
        """
        Load task configuration and trajectory from pairs directory
        
        Args:
            pairs_root_dir: pairs root directory path
            task_id: task id
            trajectory_type: trajectory type ("true" or "false")
        """
        logger.info(f"Loading task data from pairs directory...")
        
        pairs_root = Path(pairs_root_dir)
        
        # Search for task_id in PPT/Word/Excel subdirectories
        pair_dir = None
        for category in ['PPT', 'Word', 'Excel']:
            candidate = pairs_root / category / task_id
            if candidate.exists():
                pair_dir = candidate
                logger.info(f"Found task {task_id} in category: {category}")
                break
        
        if pair_dir is None:
            raise FileNotFoundError(
                f"Task {task_id} not found in any category (PPT/Word/Excel) under {pairs_root_dir}"
            )
        
        task_config_path = pair_dir / trajectory_type / f"{task_id}.json"
        if not task_config_path.exists():
            # try to find in pair root directory
            task_config_path = pair_dir / f"{task_id}.json"
            if not task_config_path.exists():
                raise FileNotFoundError(f"Task config not found: {pair_dir / 'false' / f'{task_id}.json'}")
        
        # trajectory file in specified type directory
        trajectory_dir = pair_dir / trajectory_type
        if not trajectory_dir.exists():
            raise FileNotFoundError(f"Trajectory directory not found: {trajectory_dir}")
        
        trajectory_path = trajectory_dir / "traj.jsonl"
        if not trajectory_path.exists():

            raise FileNotFoundError(f"Trajectory file not found: {trajectory_dir / 'traj.jsonl'}")
        
        logger.info(f"Task config: {task_config_path}")
        logger.info(f"Trajectory: {trajectory_path}")

        # Load task configuration
        with open(task_config_path, 'r', encoding='utf-8') as f:
            self.task_config = json.load(f)

        # Persist path
        self.trajectory_path = str(trajectory_path)
        
        # Save pairs directory info for loading screenshots
        self.pairs_root_dir = str(pairs_root)
        self.trajectory_dir = str(trajectory_dir)  # pair_dir / trajectory_type

        # Load trajectory
        self.trajectory = load_trajectory(str(trajectory_path))
        
        # Infer ground truth from trajectory_type
        self.ground_truth = trajectory_type
        logger.info(f"Ground truth: {self.ground_truth}")
        
        logger.info(f"Task instruction: {self.task_config.get('instruction', 'N/A')}")
        logger.info(f"Trajectory: {len(self.trajectory)} steps")

    def initialize_environment(self) -> bool:
        """
        initialize environment
        
        Returns:
            whether the environment is initialized successfully
        """
        logger.info("Initializing environment...")
        
        try:
            # start MCP Server
            self.mcp_client.start_server()
            
            # prepare task configuration file path
            task_config_temp = self.log_dir / "task_config.json"
            with open(task_config_temp, 'w', encoding='utf-8') as f:
                json.dump(self.task_config, f, ensure_ascii=False, indent=2)
            
            # initialize environment via MCP
            success = self.mcp_client.initialize_environment(
                task_config_path=str(task_config_temp),
                provider=self.provider,
                region=self.region,
                screen_width=self.screen_width,
                screen_height=self.screen_height
            )
            
            if not success:
                raise RuntimeError("Failed to initialize environment via MCP")
            
            # create adapter
            self.env = GUIMCPAdapter(self.mcp_client)
            
            logger.info("✅ Environment initialized successfully")
            
            return True
        
        except Exception as e:
            logger.error(f"Failed to initialize environment: {e}")
            self._cleanup_environment()
            return False

    def replay_trajectory(self) -> bool:
        """
        replay trajectory
        
        Args:
            observation_type: observation type ("screenshot", "a11y_tree", "screenshot_a11y_tree")
        
        Returns:
            whether the trajectory is replayed successfully
        """
        # Update worker activity before replay starts
        if self.worker_activity is not None and self.worker_name:
            self.worker_activity[self.worker_name].update({
                'timestamp': time.time(),
                'status': 'replaying_trajectory'
            })
            logger.debug(f"[{self.worker_name}] Updated activity timestamp before replay")
        
        # Note: initial click is now executed inside the MCP replay_trajectory tool (after reset())
        # The tool will automatically call _perform_initial_click_in_replay() to ensure the popup is closed correctly
        
        # based on observation_type, decide the saving method
        if self.observation_type == "screenshot":
            # only save screenshots
            return self._replay_trajectory_with_screenshots()
        elif self.observation_type == "a11y_tree":
            # use MCP's replay_trajectory tool to save a11y_tree
            return self._replay_trajectory_with_tree()
        elif self.observation_type == "screenshot_a11y_tree":
            # save both a11y_tree and screenshots
            logger.debug("Replay mode: saving both a11y_tree and screenshots in single pass")
            return self._replay_trajectory_with_screenshots()
        else:
            # default save a11y_tree
            logger.warning(f"Unknown observation_type: {self.observation_type}, using a11y_tree mode")
            result = self._replay_trajectory_with_tree()
            
            # Update worker activity after replay completes
            if self.worker_activity is not None and self.worker_name:
                self.worker_activity[self.worker_name].update({
                    'timestamp': time.time(),
                    'status': 'processing'
                })
                logger.debug(f"[{self.worker_name}] Updated activity timestamp after replay")
            
            return result
    
    def _replay_trajectory_with_tree(self) -> bool:
        """
       replay trajectory and save a11y_tree
        """
        logger.debug("Replaying trajectory with a11y_tree...")
        
        try:
            result_dir = str(self.log_dir / "replay")
            success = self.mcp_client.replay_trajectory(
                trajectory_path=self.trajectory_path,
                result_dir=result_dir
            )
            
            if not success:
                raise RuntimeError("Failed to replay trajectory via MCP")
            
            logger.info("✅ Trajectory replay completed via MCP tool, a11y_tree files saved")
            
            # Update worker activity after replay completes
            if self.worker_activity is not None and self.worker_name:
                self.worker_activity[self.worker_name].update({
                    'timestamp': time.time(),
                    'status': 'processing'
                })
                logger.debug(f"[{self.worker_name}] Updated activity timestamp after replay (tree)")
            
            return True
        
        except Exception as e:
            logger.error(f"Failed to replay trajectory: {e}")
            # Update timestamp even on failure to prevent stuck detection
            if self.worker_activity is not None and self.worker_name:
                self.worker_activity[self.worker_name].update({
                    'timestamp': time.time(),
                    'status': 'processing'
                })
            self._cleanup_environment()
            return False
    
    def _replay_trajectory_with_screenshots(self) -> bool:
        """
        replay trajectory and save screenshots
        """
        logger.debug("Replaying trajectory with screenshots...")
        
        try:
            result_dir = str(self.log_dir / "replay")
            
            # 通过 MCP 重放轨迹（会自动保存截图到 replay/replay_screenshots 目录）
            success = self.mcp_client.replay_trajectory(
                trajectory_path=self.trajectory_path,
                result_dir=result_dir,
                save_screenshots=True
            )
            
            if not success:
                raise RuntimeError("Failed to replay trajectory via MCP")
            
            logger.info("✅ Trajectory replay completed via MCP tool, screenshots saved")
            
            # Update worker activity after replay completes
            if self.worker_activity is not None and self.worker_name:
                self.worker_activity[self.worker_name].update({
                    'timestamp': time.time(),
                    'status': 'processing'
                })
                logger.debug(f"[{self.worker_name}] Updated activity timestamp after replay (screenshots)")
            
            return True
        
        except Exception as e:
            logger.error(f"Failed to replay trajectory: {e}")
            # Update timestamp even on failure to prevent stuck detection
            if self.worker_activity is not None and self.worker_name:
                self.worker_activity[self.worker_name].update({
                    'timestamp': time.time(),
                    'status': 'processing'
                })
            self._cleanup_environment()
            return False
    
    def get_environment_observation(self) -> Dict[str, Any]:
        """
        Get environment observation
        
        Returns:
            observation data
        """
        if self.env is None:
            raise RuntimeError("Environment not initialized")
        
        observation = {}

        try:
            mcp_observation = self.mcp_client.get_observation(self.observation_type)
            if "screenshot_b64" in mcp_observation:
                observation["screenshot_b64"] = mcp_observation["screenshot_b64"]
            if "a11y_tree" in mcp_observation:
                observation["a11y_tree"] = mcp_observation["a11y_tree"]
        
        except Exception as e:
            logger.warning(f"Failed to get observation via MCP: {e}")
        
        return observation
    
    def execute_action(self, action: Dict[str, Any]) -> Dict[str, Any]:
        """
        execute action
        
        Args:
            action: action dictionary, contains action_type and parameters
            
        Returns:
            execution result and new observation
        """
        action_type = action.get("action_type", "").upper()
        
        # Handle special VIEW_TRAJECTORY_STEP action
        if action_type == "VIEW_TRAJECTORY_STEP":
            return self._handle_view_trajectory_step(action)
        
        # Handle DONE, WAIT, FAIL actions - these don't execute or get observations
        if action_type in ["DONE", "WAIT", "FAIL"]:
            logger.warning(f"Action type {action_type} reached execute_action - this should have been handled earlier. Returning without observation.")
            return {
                "success": True,
                "observation": None,  # Explicitly return None observation
                "executed_action": f"# {action_type}"
            }
        
        if self.env is None or self.mcp_client is None:
            raise RuntimeError("Environment not initialized")
        
        try:
            # Map action_type to MCP tool name
            tool_name_map = {
                "CLICK": "click",
                "DOUBLE_CLICK": "double_click",
                "RIGHT_CLICK": "right_click",
                "MOUSE_DOWN": "mouse_down",
                "MOUSE_UP": "mouse_up",
                "DRAG_TO": "drag_to",
                "SCROLL": "scroll",
                "TYPING": "typing",
                "PRESS": "press",
                "KEY_DOWN": "key_down",
                "KEY_UP": "key_up",
                "HOTKEY": "hotkey",
                "DONE": "done",
                "WAIT": "wait",
            }
            
            tool_name = tool_name_map.get(action_type)
            if not tool_name:
                raise ValueError(f"Unknown action type: {action_type}")
            
            # Prepare tool arguments from action dict
            # Remove action_type from arguments, keep all other fields
            tool_args = {k: v for k, v in action.items() if k != "action_type"}
            
            # Call MCP tool
            result = self.mcp_client.call_tool(tool_name, tool_args)
            
            if not result.get("success"):
                error_msg = result.get("error", "Unknown error")
                logger.error(f"MCP tool '{tool_name}' failed: {error_msg}")
                return {
                    "success": False,
                    "error": error_msg,
                    "observation": None
                }
            
            # Get new observation after action execution
            observation = self.get_environment_observation()
            
            return {
                "success": True,
                "observation": observation,
                "executed_action": f"{action_type}({tool_args})"
            }
        
        except Exception as e:
            logger.error(f"Failed to execute action: {e}")
            import traceback
            logger.error(f"Traceback: {traceback.format_exc()}")
            return {
                "success": False,
                "error": str(e),
                "observation": None
            }
    
    def _convert_action_to_command(self, action: Dict[str, Any]) -> str:
        """convert action dictionary to pyautogui command string"""
        action_type = action.get("action_type", "").upper()
        
        if action_type == "CLICK":
            x = action.get("x", "")
            y = action.get("y", "")
            if x and y:
                return f"pyautogui.click({x}, {y})"
            else:
                return "pyautogui.click()"
        
        elif action_type == "MOVE_TO":
            x = action.get("x")
            y = action.get("y")
            return f"pyautogui.moveTo({x}, {y})"
        
        elif action_type == "TYPING":
            text = action.get("text", "")
            return f"pyautogui.typewrite('{text}')"
        
        elif action_type == "PRESS":
            key = action.get("key", "")
            return f"pyautogui.press('{key}')"
        
        elif action_type == "HOTKEY":
            keys = action.get("keys", [])
            keys_str = "', '".join(keys)
            return f"pyautogui.hotkey('{keys_str}')"
        
        elif action_type == "SCROLL":
            dy = action.get("dy", 0)
            return f"pyautogui.scroll({dy})"
        
        elif action_type == "DOUBLE_CLICK":
            x = action.get("x", "")
            y = action.get("y", "")
            if x and y:
                return f"pyautogui.doubleClick({x}, {y})"
            else:
                return "pyautogui.doubleClick()"
        
        elif action_type == "RIGHT_CLICK":
            x = action.get("x", "")
            y = action.get("y", "")
            if x and y:
                return f"pyautogui.rightClick({x}, {y})"
            else:
                return "pyautogui.rightClick()"
        
        elif action_type == "DRAG_TO":
            x = action.get("x")
            y = action.get("y")
            return f"pyautogui.dragTo({x}, {y})"
        
        elif action_type in ["WAIT", "DONE", "FAIL"]:
            return f"# {action_type}"
        
        elif action_type == "VIEW_TRAJECTORY_STEP":
            step = action.get("step", 0)
            return f"# VIEW_TRAJECTORY_STEP: step {step}"
        
        else:
            raise ValueError(f"Unknown action type: {action_type}")
    
    def _trim_a11y_tree_with_marker(self, linearized_tree: str, max_chars: int) -> str:
        """
        truncate a11y_tree and add marker
        
        Args:
            linearized_tree: linearized a11y_tree string
            max_chars: maximum number of characters
            
        Returns:
            truncated string, if truncated, it will contain a clear marker
        """
        if len(linearized_tree) <= max_chars:
            return linearized_tree
        truncated = linearized_tree[:max_chars]

        truncation_marker = f"\n\n[TRUNCATED_WARNING] Tree truncated at {max_chars:,} chars. Remaining content omitted. Missing elements may exist. Use VIEW_TRAJECTORY_STEP if needed.\n"
        
        return truncated + truncation_marker
    
    def _handle_view_trajectory_step(self, action: Dict[str, Any]) -> Dict[str, Any]:
        """
        handle VIEW_TRAJECTORY_STEP action
        
        Args:
            action: action dictionary, contains step information
            
        Returns:
            result dictionary, contains trajectory step information
        """
        try:
            step_num = action.get("step", 0)
            
            step_index = step_num - 1 if step_num > 0 else 0
            
            if not self.trajectory or step_index < 0 or step_index >= len(self.trajectory):
                max_step = len(self.trajectory) if self.trajectory else 0
                return {
                    "success": False,
                    "error": f"Step {step_num} not found in trajectory (valid range: 1-{max_step})",
                    "observation": None
                }
            
            # Get step data
            step_data = self.trajectory[step_index]
            
            # Find screenshot and a11y_tree based on observation_type
            observation = {}
            
            # Find screenshot
            # If failed, read from original pair path
            if self.observation_type in ["screenshot", "screenshot_a11y_tree"]:
                screenshot_loaded = False
                try:
                    replay_dir = self.log_dir / "replay"
                    replay_screenshots_dir = replay_dir / "replay_screenshots"
                    
                    if not replay_screenshots_dir.exists():
                        logger.warning(f"⚠️ replay_screenshots directory does not exist: {replay_screenshots_dir}")
                    else:
                        import glob
                        
                        # Find screenshot files saved during replay
                        screenshot_pattern = str(replay_screenshots_dir / f"step_{step_num}_*.png")
                        matching_files = glob.glob(screenshot_pattern)
                        
                        if matching_files:
                            screenshot_path = Path(matching_files[0])
                            with open(screenshot_path, 'rb') as f:
                                screenshot_data = f.read()
                                screenshot_b64 = base64.b64encode(screenshot_data).decode('utf-8')
                                observation["trajectory_screenshot_b64"] = screenshot_b64
                                observation["trajectory_screenshot_file"] = screenshot_path.name
                                logger.info(f"✅ Successfully loaded trajectory screenshot from replay directory: {screenshot_path.name} (path: {screenshot_path})")
                                screenshot_loaded = True
                        else:
                            logger.warning(f"⚠️ Step {step_num} screenshot file not found (search pattern: {screenshot_pattern}, search directory: {replay_screenshots_dir})")
                except Exception as e:
                    logger.warning(f"⚠️ Failed to load trajectory screenshot file from replay directory: {e}")
                
                # Backup: read screenshot from original pair path
                if not screenshot_loaded and self.trajectory_dir:
                    try:
                        import glob
                        trajectory_dir_path = Path(self.trajectory_dir)
                        
                        # Try to get screenshot_file from trajectory data
                        screenshot_file = None
                        if step_data and isinstance(step_data, dict):
                            screenshot_file = step_data.get("screenshot_file")
                        
                        if screenshot_file:
                            # Use screenshot file name recorded in trajectory
                            screenshot_path = trajectory_dir_path / screenshot_file
                            if screenshot_path.exists():
                                with open(screenshot_path, 'rb') as f:
                                    screenshot_data = f.read()
                                    screenshot_b64 = base64.b64encode(screenshot_data).decode('utf-8')
                                    observation["trajectory_screenshot_b64"] = screenshot_b64
                                    observation["trajectory_screenshot_file"] = screenshot_file
                                    logger.info(f"✅ Successfully loaded trajectory screenshot from original pair path: {screenshot_file} (path: {screenshot_path})")
                                    screenshot_loaded = True
                            else:
                                logger.warning(f"⚠️ Screenshot file recorded in trajectory does not exist: {screenshot_path}")
                        
                    except Exception as e:
                        logger.warning(f"⚠️ Failed to load trajectory screenshot file from original pair path: {e}")
                
                # record error information
                if not screenshot_loaded:
                    observation["trajectory_screenshot_not_found"] = True
                    observation["trajectory_screenshot_error"] = f"Step {step_num} screenshot not found in replay directory or original pair directory. Please try another step."
            
            # Find a11y_tree (from replay directory) with retry; after repeated failures, requeue task
            if self.observation_type in ["a11y_tree", "screenshot_a11y_tree"]:
                tree_loaded = False
                max_load_retries = 3
                for load_attempt in range(max_load_retries):
                    try:
                        replay_dir = self.log_dir / "replay"
                        a11y_tree_dir = replay_dir / "a11y_tree"
                        
                        if not a11y_tree_dir.exists():
                            logger.warning(f"⚠️ a11y_tree directory does not exist: {a11y_tree_dir}")
                        else:
                            import glob
                            
                            processed_pattern = str(a11y_tree_dir / f"step_{step_num}_*_processed_a11y_tree.json")
                            processed_matching_files = glob.glob(processed_pattern)
                            
                            if processed_matching_files:
                                processed_a11y_tree_path = Path(processed_matching_files[0])
                                with open(processed_a11y_tree_path, 'r', encoding='utf-8') as f:
                                    processed_a11y_tree = json.load(f)
                                    observation["trajectory_a11y_tree"] = processed_a11y_tree
                                    tree_loaded = True
                                    self._consecutive_a11y_load_failures = 0
                                    logger.info(f"✅ Successfully loaded processed trajectory a11y_tree from replay directory: {processed_a11y_tree_path.name} (path: {processed_a11y_tree_path})")
                                    
                                    print(f"\n{'='*80}")
                                    print(f"🌳 Processed trajectory Accessibility Tree (Step {step_num}):")
                                    print(f"{'='*80}")
                                    print(f"📊 Tree size: {len(str(processed_a11y_tree)):,} characters")
                                    print(f"📋 Preview of first 500 characters:")
                                    print(f"{str(processed_a11y_tree)[:500]}...")
                                    print(f"{'='*80}\n")
                                break
                            else:
                                logger.warning(f"⚠️ Processed a11y_tree JSON file not found (attempt {load_attempt + 1}/{max_load_retries}, pattern: {processed_pattern})")
                        if not tree_loaded and load_attempt < max_load_retries - 1:
                            time.sleep(1)
                    except Exception as e:
                        logger.warning(f"⚠️ Failed to load trajectory a11y_tree file (attempt {load_attempt + 1}/{max_load_retries}): {e}")
                        if load_attempt < max_load_retries - 1:
                            time.sleep(1)
                
                if not tree_loaded:
                    self._consecutive_a11y_load_failures += 1
                    observation["trajectory_a11y_tree_not_found"] = True
                    observation["trajectory_a11y_tree_error"] = f"Step {step_num} accessibility tree not found in replay directory. Please try another step."
                    if self._consecutive_a11y_load_failures >= self._max_consecutive_a11y_load_failures:
                        logger.error(f"🚨 a11y_tree load failed {self._consecutive_a11y_load_failures} times, requeue task for re-evaluation")
                        raise RequeueTaskError("a11y_tree load failed repeatedly in VIEW_TRAJECTORY_STEP")
                else:
                    self._consecutive_a11y_load_failures = 0
            
            # Add step metadata
            observation["trajectory_step_info"] = {
                "step": step_num,
                "action": step_data.get("action", {}),
                "timestamp": step_data.get("timestamp", "N/A")
            }
            
            # Create formatted observation text
            formatted_obs = f"Trajectory Step {step_num}:\n"
            formatted_obs += f"Action: {step_data.get('action', 'N/A')}\n"
            
            # Add screenshot information
            if self.observation_type in ["screenshot", "screenshot_a11y_tree"]:
                if "trajectory_screenshot_b64" in observation:
                    screenshot_file = observation.get("trajectory_screenshot_file", "unknown")
                    formatted_obs += f"Screenshot: Available ({screenshot_file})\n"
                elif "trajectory_screenshot_not_found" in observation:
                    error_msg = observation.get("trajectory_screenshot_error", f"Step {step_num} screenshot not found.")
                    formatted_obs += f"Screenshot: {error_msg}\n"
                else:
                    formatted_obs += f"Screenshot: Step {step_num} screenshot not available. Please try another step.\n"
            
            # Add a11y_tree information
            if self.observation_type in ["a11y_tree", "screenshot_a11y_tree"]:
                if "trajectory_a11y_tree" in observation:
                    a11y_tree = observation["trajectory_a11y_tree"]
                    a11y_tree_str = str(a11y_tree)
                    a11y_tree_length = len(a11y_tree_str)
                    
                    logger.debug(f"a11y_tree size: {a11y_tree_length:,} characters")
                    if len(str(a11y_tree)) > 15000:
                        formatted_obs += f"Accessibility Tree: {str(a11y_tree)[:7500]}...{str(a11y_tree)[-7500:]}\n"
                    else:
                        formatted_obs += f"Accessibility Tree: {a11y_tree}\n"
                elif "trajectory_a11y_tree_not_found" in observation:
                    # explicitly inform that tree is not found, suggest to try another step
                    error_msg = observation.get("trajectory_a11y_tree_error", f"Step {step_num} accessibility tree not found.")
                    formatted_obs += f"Accessibility Tree: {error_msg} Please try another step.\n"
                else:
                    formatted_obs += f"Accessibility Tree: Step {step_num} accessibility tree not available. Please try another step.\n"
            
            observation["formatted_observation"] = formatted_obs
            
            return {
                "success": True,
                "observation": observation,
                "executed_action": f"VIEW_TRAJECTORY_STEP: step {step_num}"
            }
            
        except Exception as e:
            logger.error(f"Failed to handle VIEW_TRAJECTORY_STEP: {e}")
            return {
                "success": False,
                "error": str(e),
                "observation": None
            }
    
    def start_evaluation(self) -> Dict[str, Any]:
        """
        Start evaluation process
        
        Returns:
            Evaluation result
        """
        logger.info("Starting trajectory evaluation...")
        
        # Initialize conversation with system prompt
        self.conversation_history = [
            {"role": "system", "content": SINGLE_SYSTEM_PROMPT}
        ]
        
        # Create initial user prompt
        trajectory_summary = self._create_trajectory_summary(self.trajectory)
        
        initial_prompt = SINGLE_USER_PROMPT.format(
            task_instruction=self.task_config.get('instruction', 'N/A'),
            trajectory=trajectory_summary
        )
        
        # Add action space information
        initial_prompt += "\n\n" + ACTION_SPACE_PROMPT
        
        # Get initial observation metadata to inform agent about available observation types
        try:
            obs = self.get_environment_observation()
        except Exception as e:
            logger.warning(f"Failed to get initial observation: {e}")
            obs = {}
        
        def _summarize_observation_metadata(obs: Dict[str, Any]) -> str:
            """Generate metadata summary only (no actual content)"""
            parts = [f"Environment initial observation (metadata only, observation_type={self.observation_type}):"]
            
            # Display information based on observation_type
            if self.observation_type in ["screenshot", "screenshot_a11y_tree"]:
                if "screenshot_b64" in obs:
                    parts.append("- screenshot: available (base64 encoded)")
                else:
                    parts.append("- screenshot: not available")
            
            if self.observation_type in ["a11y_tree", "screenshot_a11y_tree"]:
                if "a11y_tree" in obs and obs["a11y_tree"] is not None:
                    tree_str = str(obs["a11y_tree"])
                    parts.append(f"- a11y_tree: provided (length={len(tree_str)} chars)")
                else:
                    parts.append("- a11y_tree: not available")
            
            return "\n".join(parts)
        
        # Add metadata summary only (no actual content)
        initial_prompt += "\n\n" + _summarize_observation_metadata(obs)
        
        self.conversation_history.append({"role": "user", "content": initial_prompt})
        
        # Send FULL TRAJECTORY as a single complete message
        try:
            if self.trajectory:                
                full_traj_raw = json.dumps(self.trajectory, ensure_ascii=False)
                self.conversation_history.append({
                    "role": "user",
                    "content": "FULL TRAJECTORY:\n" + full_traj_raw
                })
                logger.info(f"✅ Successfully added full trajectory to conversation history (size: {len(full_traj_raw):,} characters)")
        except Exception as e:
            logger.warning(f"Failed to attach full trajectory: {e}")

        # Get initial response
        response = self._get_agent_response()
        # Print and log the initial response
        try:
            banner = "\n===== Agent Initial Response =====\n"
            print(banner + str(response) + "\n" + ("=" * 34))
        except Exception:
            pass
        logger.info(f"Agent initial response:\n{response}")
        
        # Parse response
        parsed_response = self._parse_agent_response(response)
        
        if not parsed_response:
            return {"success": False, "error": "Failed to parse initial agent response", "log_directory": str(self.log_dir)}
        else:
            logger.debug(f"Parsed response: {parsed_response}")
        
        # Start interaction loop
        return self._interaction_loop(parsed_response)
    
    def _create_trajectory_summary(self, trajectory: List[Dict]) -> str:
        """Create trajectory summary"""
        summary = f"Trajectory ({len(trajectory)} steps):\n"
        for i, step in enumerate(trajectory[:5]):
            action = step.get("action", "No action")
            summary += f"  Step {i+1}: {action}\n"
        
        if len(trajectory) > 5:
            summary += f"  ... and {len(trajectory) - 5} more steps\n"
        
        return summary
    
    def _get_agent_response(self) -> str:
        """Get Agent response"""
        max_retries = 10
        base_delay = 2
        
        model_lower = str(self.model).lower()
        is_deepseek_reasoner = model_lower.startswith("deepseek-reasoner")
        
        for attempt in range(max_retries):
            try:
                # Prepare request parameters
                request_params = {
                    "model": self.model,
                    "messages": self.conversation_history,
                    "max_tokens": 8192
                }
                # Only pass temperature if explicitly provided
                if self.temperature is not None:
                    request_params["temperature"] = self.temperature
                
                # Select corresponding API client
                if str(self.model).startswith("deepseek"):
                    # DeepSeek
                    client = openai.OpenAI(
                        api_key=os.getenv("DEEPSEEK_API_KEY"),
                        base_url="https://api.deepseek.com",
                        max_retries=0
                    )
                    # DeepSeek does not support reasoning parameter
                    request_params.pop("reasoning", None)
                    request_params.pop("max_completion_tokens", None)
                else:
                    # OpenAI/Other
                    client = openai.OpenAI(
                        api_key=os.getenv("OPENAI_API_KEY"),
                        base_url=os.getenv("OPENAI_BASE_URL") or None,
                        max_retries=0
                    )
                    
                    REASONING_MODELS = ["o3-mini", "gpt-5-mini", "gpt-5.1"]
                    
                    is_reasoning_model = self.model in REASONING_MODELS
                    is_official_api = not os.getenv("OPENAI_BASE_URL")
                    
                    if is_reasoning_model and is_official_api:
                        request_params["reasoning"] = {"effort": self.effort}
                        # o3-mini needs max_completion_tokens
                        if self.model == "o3-mini":
                            request_params["max_completion_tokens"] = request_params.pop("max_tokens")
                        logger.debug(f"Added reasoning parameter with effort={self.effort} for model {self.model}")
                    elif is_reasoning_model and not is_official_api:
                        # Remove possible incompatible parameters for custom API endpoint
                        request_params.pop("reasoning", None)
                        request_params.pop("max_completion_tokens", None)
                        logger.debug(f"Removed reasoning parameters for model {self.model} (custom API endpoint)")
                    elif not is_reasoning_model and self.effort != "medium":
                        # If model does not support reasoning.effort parameter, and effort is not default value, record warning
                        logger.debug(f"Model {self.model} does not support reasoning.effort parameter, effort={self.effort} will be ignored")
                
                timeout = 200 if attempt == 0 else 300
                
                response = client.chat.completions.create(
                    **request_params,
                    timeout=timeout
                )
                
                if hasattr(response, "choices") and response.choices:
                    choice = response.choices[0]
                    
                    if hasattr(choice, "message") and hasattr(choice.message, "content"):
                        content = choice.message.content
                        
                        if content and content.strip():
                            self.conversation_history.append({"role": "assistant", "content": content})
                            logger.info(f"✅ API call successful (attempt {attempt + 1}/{max_retries})")
                            return content
                        else:
                            raise Exception(f"API returned empty content: content='{content}', type={type(content)}")
                    else:
                        raise Exception("Response does not have content field")
                else:
                    # 记录完整响应以便调试
                    logger.error(f"API response format exception - full response: {response}")
                    logger.error(f"Response type: {type(response)}")
                    logger.error(f"Response attributes: {dir(response)}")
                    if hasattr(response, 'model_dump'):
                        logger.error(f"Response dump: {response.model_dump()}")
                    raise Exception("Response does not have choices field or choices is empty")
            
            except Exception as e:
                error_str = str(e).lower()
                # Check context length error
                is_context_error = (
                    "context_length" in error_str or
                    "maximum context length" in error_str or
                    "token limit" in error_str or
                    "exceeds maximum" in error_str or
                    "too many tokens" in error_str
                )
                
                if is_context_error and self._a11y_tree_max_chars > 10000:
                    # Decrease a11y_tree truncation length
                    logger.warning(f"Context length error detected, decreasing a11y_tree maximum length from {self._a11y_tree_max_chars} to 10000")
                    self._a11y_tree_max_chars = 10000
                    # Reduce conversation history to free up space
                    if len(self.conversation_history) > 10:
                        # Keep system prompt and recent 5 rounds of conversation
                        logger.warning(f"Clearing conversation history, reducing from {len(self.conversation_history)} to recent 10")
                        system_msg = self.conversation_history[0] if self.conversation_history else None
                        recent_msgs = self.conversation_history[-9:] if len(self.conversation_history) > 9 else self.conversation_history[1:]
                        self.conversation_history = ([system_msg] if system_msg else []) + recent_msgs
                    continue
                
                logger.warning(f"API call failed (attempt {attempt + 1}/{max_retries}): {e}")
                
                if attempt < max_retries - 1:
                    # Fixed 1 second delay to avoid waiting too long
                    delay = 5
                    logger.info(f"Waiting {delay} seconds before retrying...")
                    time.sleep(delay)
                else:
                    logger.error(f"All retries failed: {e}")
                    return ""
        
        return ""
    
    def _parse_agent_response(self, response: str) -> Optional[Dict[str, Any]]:
        """Parse Agent response"""
        lines = response.strip().split('\n')
        parsed = {}
        
        for line in lines:
            line = line.strip()
            if line.startswith("ACTION:"):
                action_str = line.split(":", 1)[1].strip()
                parsed["action_str"] = action_str
                try:
                    parsed["action"] = self._parse_action_string(action_str)
                except Exception as e:
                    logger.warning(f"Failed to parse action: {e}")
            elif line.startswith("REASONING:"):
                reasoning = line.split(":", 1)[1].strip()
                parsed["reasoning"] = reasoning
        
        if "reasoning" not in parsed:
            parsed["reasoning"] = "No reasoning provided"
        if "action_str" not in parsed:
            parsed["action_str"] = "No action"
        
        return parsed if "action" in parsed else None
    
    def _parse_action_string(self, action_str: str) -> Dict[str, Any]:
        """Parse action string"""
        action_str = action_str.strip()
        
        # Try to parse as JSON first
        if action_str.startswith("{") and action_str.endswith("}"):
            try:
                parsed = json.loads(action_str)
                # Extract action_type from the parsed JSON
                if "action_type" in parsed:
                    return parsed
                elif "action" in parsed:
                    # Handle nested action format
                    return {"action_type": parsed["action"]}
            except:
                pass
        
        # Handle malformed JSON-like strings
        if "action_type" in action_str:
            try:
                # Try to extract action_type from malformed JSON
                import re
                action_type_match = re.search(r'"action_type":\s*"([^"]+)"', action_str)
                if action_type_match:
                    action_type = action_type_match.group(1)
                    
                    # Extract parameters if they exist
                    params_match = re.search(r'"parameters":\s*\{([^}]+)\}', action_str)
                    if params_match:
                        params_str = "{" + params_match.group(1) + "}"
                        try:
                            params = json.loads(params_str)
                            return {"action_type": action_type, **params}
                        except:
                            pass
                    
                    return {"action_type": action_type}
            except:
                pass
        
        # Parse simple action formats
        action_str_upper = action_str.upper()
        if "CLICK" in action_str_upper:
            return {"action_type": "CLICK"}
        elif "MOVE_TO" in action_str_upper:
            return {"action_type": "MOVE_TO"}
        elif "TYPING" in action_str_upper:
            return {"action_type": "TYPING"}
        elif "PRESS" in action_str_upper:
            return {"action_type": "PRESS"}
        elif "HOTKEY" in action_str_upper:
            return {"action_type": "HOTKEY"}
        elif "DONE" in action_str_upper:
            return {"action_type": "DONE"}
        elif "WAIT" in action_str_upper:
            return {"action_type": "WAIT"}
        elif "VIEW_TRAJECTORY_STEP" in action_str_upper:
            # Try to extract step from the action string
            try:
                import re
                step_match = re.search(r'"step":\s*(\d+)', action_str)
                step = int(step_match.group(1)) if step_match else 0
                return {"action_type": "VIEW_TRAJECTORY_STEP", "step": step}
            except:
                return {"action_type": "VIEW_TRAJECTORY_STEP", "step": 0}
        
        # Default action
        return {"action_type": "WAIT"}
    
    def _interaction_loop(self, initial_parsed_response: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main interaction loop
        """
        current_response = initial_parsed_response
        max_interactions = 50
        interaction_count = 0
        final_judgment = None
        
        # Record the initial response as the first step
        interaction_count += 1
        logger.info(f"Interaction {interaction_count}/{max_interactions} (Initial Response)")
        
        action = current_response.get("action")
        
        if not action:
            logger.error("Invalid initial response from agent")
            return {"success": False, "error": "Invalid initial response", "log_directory": str(self.log_dir)}
        
        if action.get("action_type") == "DONE":
            logger.warning("Agent attempted to finish without any interaction! Forcing at least one interaction.")
            # Force agent to interact first by rejecting DONE action
            self.conversation_history.append({
                "role": "user",
                "content": "ERROR: You cannot use DONE action before performing at least one interaction with the environment. The prompt requires you to gather evidence through interactions (CLICK, VIEW_TRAJECTORY_STEP, etc.) before making a final judgment. Please choose an action that interacts with the environment to gather evidence."
            })
            response = self._get_agent_response()
            current_response = self._parse_agent_response(response)
            
            if not current_response:
                return {"success": False, "error": "Failed to parse agent response after rejecting premature DONE", "log_directory": str(self.log_dir)}
            
            # Update action to the new response
            action = current_response.get("action")
            
            # If agent still tries to use DONE, treat it as an error
            if action and action.get("action_type") == "DONE":
                logger.error("Agent persisted with DONE after warning. This is not allowed.")
                return {"success": False, "error": "Agent refused to interact with environment", "log_directory": str(self.log_dir)}
        
        # Track actual interactions 
        actual_interactions_count = 0

        # # Redundant defensive check
        # if action.get("action_type") == "DONE":
        #     logger.error("DONE action should not reach execution point. This is a bug.")
        #     return {"success": False, "error": "DONE action should not be executed", "log_directory": str(self.log_dir)}
        
        # Execute the initial action and record it
        result = self.execute_action(action)
        # all actions except DONE/WAIT/FAIL count as one interaction
        if result["success"] and action.get("action_type") not in ["DONE", "WAIT", "FAIL"]:
            actual_interactions_count += 1
        
        if result["success"]:
            observation = result["observation"]
            
            # # Redundant defensive check
            # if action.get("action_type") in ["DONE", "FAIL"]:
            #     logger.warning(f"Action {action.get('action_type')} should not reach observation processing. Skipping.")
            #     return {"success": False, "error": f"Invalid action type: {action.get('action_type')}", "log_directory": str(self.log_dir)}
            
            # Save screenshot after action execution (only if observation_type includes screenshot)
            screenshot_path = None
            if self.observation_type in ["screenshot", "screenshot_a11y_tree"]:
                screenshot_name = f"interaction_{interaction_count}_after_action"
                screenshot_path = self._save_env_screenshot(self.env, screenshot_name)
            
            # Append evaluation step log for initial response
            log_entry = {
                "step": interaction_count,
                "action": action,
                "action_str": current_response.get("action_str", ""),
                "reasoning": current_response.get("reasoning", ""),
                "screenshot": str(screenshot_path) if screenshot_path else None,
                "observation": self._format_observation(observation),
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
            
            # Add trajectory step data to log if available
            if action.get("action_type") != "VIEW_TRAJECTORY_STEP":
                if "trajectory_step_info" in observation:
                    log_entry["trajectory_step_info"] = observation["trajectory_step_info"]
                if "trajectory_a11y_tree" in observation:
                    log_entry["trajectory_a11y_tree"] = observation["trajectory_a11y_tree"]
            
            self.eval_log.append(log_entry)
            
            # Create observation prompt and attach image if available
            if action.get("action_type") == "VIEW_TRAJECTORY_STEP":
                obs_prompt_text = f"Trajectory Step Information:\n{self._format_observation(observation)}\n\nBased on this trajectory step information, choose your next action:"
            else:
                obs_prompt_text = SINGLE_OBSERVATION_PROMPT.format(
                    observation_type=self.observation_type,
                    observation=self._format_observation(observation)
                )

            if self.observation_type in ["screenshot", "screenshot_a11y_tree"]:
                if "screenshot_b64" in observation:
                    data_url = f"data:image/png;base64,{observation['screenshot_b64']}"
                    content_parts = [
                        {"type": "text", "text": obs_prompt_text},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": data_url,
                                "detail": "high"
                            }
                        }
                    ]
                    self.conversation_history.append({"role": "user", "content": content_parts})
                elif "trajectory_screenshot_b64" in observation:
                    data_url = f"data:image/png;base64,{observation['trajectory_screenshot_b64']}"
                    content_parts = [
                        {"type": "text", "text": obs_prompt_text},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": data_url,
                                "detail": "high"
                            }
                        }
                    ]
                    self.conversation_history.append({"role": "user", "content": content_parts})
                else:
                    # screenshot mode but no screenshot_b64 found in observation, record warning but still send text
                    logger.warning(f"Screenshot mode but no screenshot_b64 found in observation")
                    self.conversation_history.append({"role": "user", "content": obs_prompt_text})
            else:
                # a11y_tree mode, only send text
                self.conversation_history.append({"role": "user", "content": obs_prompt_text})
            
            # Get next response from agent
            response = self._get_agent_response()
            try:
                banner = f"\n===== Agent Response (Interaction {interaction_count}) =====\n"
                print(banner + str(response) + "\n" + ("=" * 50))
            except Exception:
                pass
            logger.info(f"Agent response at interaction {interaction_count}:\n{response}")
            current_response = self._parse_agent_response(response)
            
            if not current_response:
                logger.error("Failed to parse agent response")
                return {"success": False, "error": "Failed to parse agent response", "log_directory": str(self.log_dir)}
        else:
            # Handle execution error for initial action
            error_prompt = f"Initial action execution failed: {result['error']}"
            self.conversation_history.append({"role": "user", "content": error_prompt})
            
            response = self._get_agent_response()
            current_response = self._parse_agent_response(response)
            
            if not current_response:
                return {"success": False, "error": "Failed to parse agent response after initial error", "log_directory": str(self.log_dir)}
        
        # Continue with the main interaction loop        
        while interaction_count < max_interactions:
            interaction_count += 1
            logger.info(f"Interaction {interaction_count}/{max_interactions}")
            
            action = current_response.get("action")
            
            if not action:
                logger.error("Invalid response from agent")
                break
            
            # Check if agent wants to finish
            if action.get("action_type") == "DONE":
                # Ensure at least one actual interaction has been performed
                if actual_interactions_count == 0:
                    logger.warning(f"Agent attempted DONE after {interaction_count} interactions but no actual environment interactions. Requiring at least one interaction.")
                    self.conversation_history.append({
                        "role": "user",
                        "content": "ERROR: You must perform at least one interaction with the environment (CLICK, TYPING, VIEW_TRAJECTORY_STEP, etc.) before using DONE. Please gather evidence first."
                    })
                    response = self._get_agent_response()
                    current_response = self._parse_agent_response(response)
                    
                    if not current_response:
                        logger.error("Failed to parse agent response after rejecting premature DONE")
                        break
                    
                    # Update action and continue loop
                    action = current_response.get("action")
                    
                    # If agent still tries to use DONE, treat it as an error
                    if action and action.get("action_type") == "DONE":
                        logger.error("Agent persisted with DONE after warning. This is not allowed.")
                        break
                    else:
                        # Continue with the new action
                        continue
                
                logger.info("Agent indicated completion!")
                # Always request explicit final judgment
                self.conversation_history.append({
                    "role": "user",
                    "content": SINGLE_FINAL_JUDGMENT_PROMPT
                })
                fj_response = self._get_agent_response()
                parsed_fj = self._parse_final_judgment(fj_response)
                if parsed_fj and parsed_fj.get("judgment") in ["true", "false"]:
                    final_judgment = parsed_fj
                break
            
            # Handle actions
            result = self.execute_action(action)
            # Count actual interactions (include VIEW_TRAJECTORY_STEP; exclude DONE/WAIT/FAIL)
            if result["success"] and action.get("action_type") not in ["DONE", "WAIT", "FAIL"]:
                actual_interactions_count += 1
            
            if result["success"]:
                observation = result["observation"]
                
                # Handle trajectory step viewing
                if action.get("action_type") == "VIEW_TRAJECTORY_STEP":
                    screenshot_path = None
                else:
                    # Save screenshot after action execution (only if observation_type includes screenshot)
                    if self.observation_type in ["screenshot", "screenshot_a11y_tree"]:
                        screenshot_name = f"interaction_{interaction_count}_after_action"
                        screenshot_path = self._save_env_screenshot(self.env, screenshot_name)
                    else:
                        screenshot_path = None
                
                # Append evaluation step log
                log_entry = {
                    "step": interaction_count,
                    "action": action,
                    "action_str": current_response.get("action_str", ""),
                    "reasoning": current_response.get("reasoning", ""),
                    "screenshot": str(screenshot_path) if screenshot_path else None,
                    "observation": self._format_observation(observation),
                    "timestamp": datetime.now(timezone.utc).isoformat()
                }
                
                if action.get("action_type") != "VIEW_TRAJECTORY_STEP":
                    if "trajectory_step_info" in observation:
                        log_entry["trajectory_step_info"] = observation["trajectory_step_info"]
                    if "trajectory_a11y_tree" in observation:
                        log_entry["trajectory_a11y_tree"] = observation["trajectory_a11y_tree"]
                
                self.eval_log.append(log_entry)
                
                # Create observation prompt
                if action.get("action_type") == "VIEW_TRAJECTORY_STEP":
                    obs_prompt_text = f"Trajectory Step Information:\n{self._format_observation(observation)}\n\nBased on this trajectory step information, choose your next action:"
                else:
                    obs_prompt_text = SINGLE_OBSERVATION_PROMPT.format(
                        observation_type=self.observation_type,
                        observation=self._format_observation(observation)
                    )

                if self.observation_type in ["screenshot", "screenshot_a11y_tree"]:
                    if "screenshot_b64" in observation:
                        data_url = f"data:image/png;base64,{observation['screenshot_b64']}"
                        content_parts = [
                            {"type": "text", "text": obs_prompt_text},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": data_url,
                                    "detail": "low"
                                }
                            }
                        ]
                        self.conversation_history.append({"role": "user", "content": content_parts})
                    elif "trajectory_screenshot_b64" in observation:
                        data_url = f"data:image/png;base64,{observation['trajectory_screenshot_b64']}"
                        content_parts = [
                            {"type": "text", "text": obs_prompt_text},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": data_url,
                                    "detail": "low"
                                }
                            }
                        ]
                        self.conversation_history.append({"role": "user", "content": content_parts})
                    else:
                        # screenshot mode but no screenshot_b64 found in observation, record warning but still send text
                        logger.warning(f"Screenshot mode but no screenshot_b64 found in observation")
                        self.conversation_history.append({"role": "user", "content": obs_prompt_text})
                else:
                    # a11y_tree mode, only send text
                    self.conversation_history.append({"role": "user", "content": obs_prompt_text})
                
                # Get next response
                response = self._get_agent_response()
                try:
                    banner = f"\n===== Agent Response (Interaction {interaction_count}) =====\n"
                    print(banner + str(response) + "\n" + ("=" * 50))
                except Exception:
                    pass
                logger.info(f"Agent response at interaction {interaction_count}:\n{response}")
                current_response = self._parse_agent_response(response)
                
                if not current_response:
                    logger.error("Failed to parse agent response")
                    break
            else:
                # Handle execution error
                error_prompt = f"Action execution failed: {result['error']}"
                self.conversation_history.append({"role": "user", "content": error_prompt})
                
                response = self._get_agent_response()
                current_response = self._parse_agent_response(response)
                
                if not current_response:
                    break
        
        # Get final judgment
        if final_judgment is not None:
            return self._get_final_judgment(final_judgment)
        else:
            return self._get_final_judgment()
    
    def _format_observation(self, observation: Dict[str, Any]) -> str:
        """
        Format observation for the prompt
        """
        formatted = ""
        
        # Handle trajectory step observations
        if "formatted_observation" in observation:
            # VIEW_TRAJECTORY_STEP already provided formatted text, return directly
            formatted += observation["formatted_observation"]
            return formatted
        
        # Handle regular environment observations
        if self.observation_type in ["screenshot", "screenshot_a11y_tree"]:
            if "screenshot_b64" in observation or "trajectory_screenshot_b64" in observation:
                formatted += "Screenshot: Available (showing current state of the environment)\n"
            elif "screenshot" in observation:
                formatted += "Screenshot: Available (showing current state of the environment)\n"
        
        if self.observation_type in ["a11y_tree", "screenshot_a11y_tree"]:
            if "a11y_tree" in observation:
                a11y_tree = observation["a11y_tree"]
                max_chars = self._a11y_tree_max_chars
                tree_str = str(a11y_tree)
                
                # Simplified: directly use _trim_a11y_tree_with_marker for all cases
                # It handles length check internally, eliminating redundant checks
                tree_display = self._trim_a11y_tree_with_marker(tree_str, max_chars)
                logger.debug(f"Accessibility Tree length: {len(tree_str)} chars (already linearized)")
                formatted += f"Accessibility Tree (linearized TSV): {tree_display}\n"
            else:
                formatted += "Accessibility Tree: Not available\n"
        
        return formatted
    
    def _parse_final_judgment(self, response: str) -> Dict[str, Any]:
        """
        Parse the final judgment response
        """
        text = (response or "").strip()
        judgment: Dict[str, Any] = {}
        
        if not text:
            logger.warning("Empty response received for final judgment")
            return {"judgment": None, "reasoning": "No reasoning provided", "confidence": "Medium"}
        
        # 1) If the model returned a fenced code block, extract the inner text
        try:
            if text.startswith("```") and text.endswith("```"):
                parts = (response or "").split("```")
                if len(parts) >= 3:
                    text = parts[1].strip()
        except Exception:
            pass
        
        # 2) Try JSON first
        import re as _re
        try:
            json_candidate = text.strip()
            if json_candidate.startswith('{') and json_candidate.endswith('}'):
                obj = json.loads(json_candidate)
                # Accept common key variants (case-insensitive)
                def _pick(d, *keys):
                    for k in keys:
                        for dk in d.keys():
                            if dk.strip().lower() == k:
                                return d[dk]
                    return None
                jdg = _pick(obj, 'judgment', 'result')
                rsn = _pick(obj, 'detailed_reasoning', 'reasoning')
                conf = _pick(obj, 'confidence')
                if jdg:
                    judgment['judgment'] = str(jdg).strip().lower()
                if rsn is not None:
                    judgment['reasoning'] = str(rsn)
                if conf is not None:
                    judgment['confidence'] = str(conf)
        except Exception:
            pass
        
        # 3) If not JSON or partial, parse line-by-line
        if 'judgment' not in judgment or judgment.get('judgment') not in ['true', 'false', 'correct', 'incorrect']:
            lines = text.split('\n')
            collecting_reason = False
            reason_buf = []
            key_judgment = _re.compile(r"(?i)\s*judgment\s*:\s*(.+)$")
            key_reason = _re.compile(r"(?i)\s*detailed_reasoning\s*:\s*(.*)$")
            key_conf = _re.compile(r"(?i)\s*confidence\s*:\s*(.+)$")
            
            def _is_any_key(s: str) -> bool:
                return bool(key_judgment.match(s) or key_reason.match(s) or key_conf.match(s))
            
            for raw in lines:
                line_orig = raw
                line = raw.strip()
                line_for_key = _re.sub(r"^[*-]\s*", "", line)
                line_for_key = line_for_key.replace("**", "")
                
                if collecting_reason:
                    if line and _is_any_key(line_for_key):
                        collecting_reason = False
                    else:
                        reason_buf.append(line_orig)
                        continue
                
                if not line:
                    continue
                
                m = key_judgment.match(line_for_key)
                if m:
                    judgment['judgment'] = m.group(1).strip().lower()
                    continue
                
                m = key_reason.match(line_for_key)
                if m:
                    first = m.group(1)
                    if first:
                        reason_buf.append(first)
                    collecting_reason = True
                    continue
                
                m = key_conf.match(line_for_key)
                if m:
                    judgment['confidence'] = m.group(1).strip()
                    continue
            
            if reason_buf and not judgment.get('reasoning'):
                judgment['reasoning'] = "\n".join([s.rstrip('\n') for s in reason_buf]).strip()
        
        # Normalize and validate outputs
        judgment_val = (judgment.get("judgment") or "").strip().lower()
        if judgment_val not in ["true", "false"]:
            judgment["judgment"] = None
        else:
            judgment["judgment"] = judgment_val
        
        # Default confidence if missing
        if not judgment.get("confidence"):
            judgment["confidence"] = "Medium"
        
        # Default reasoning if missing
        if not judgment.get("reasoning"):
            judgment["reasoning"] = "No reasoning provided"
        
        return judgment
    
    def _get_final_judgment(self, pre_parsed_judgment: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Get final judgment from the agent
        """
        logger.info("Getting final judgment...")
        
        if pre_parsed_judgment:
            # Use pre-parsed judgment from DONE action
            judgment = pre_parsed_judgment
        else:
            max_retries = 5
            judgment = None
            
            for attempt in range(max_retries + 1):
                try:
                    if attempt > 0:
                        retry_prompt = SINGLE_FINAL_JUDGMENT_PROMPT + "\n\nIMPORTANT: Please provide your judgment in the exact format:\nJUDGMENT: true\nor\nJUDGMENT: false\n\nYour response must include either 'true' or 'false' for the judgment."
                        self.conversation_history.append({
                            "role": "user",
                            "content": retry_prompt
                        })
                        logger.warning(f"Retrying final judgment request (attempt {attempt + 1}/{max_retries + 1})")
                    else:
                        self.conversation_history.append({
                            "role": "user",
                            "content": SINGLE_FINAL_JUDGMENT_PROMPT
                        })
                    
                    response = self._get_agent_response()
                    
                    # Parse final judgment
                    judgment = self._parse_final_judgment(response)

                    if judgment.get("judgment") in ["true", "false"]:
                        logger.info(f"Successfully extracted judgment: {judgment.get('judgment')} (attempt {attempt + 1})")
                        break
                    else:
                        logger.warning(f"Failed to extract valid judgment from attempt {attempt + 1}. Response preview: {response[:200] if response else 'None'}")
                        if attempt < max_retries:
                            time.sleep(1)
                        
                except Exception as e:
                    logger.error(f"Error getting final judgment (attempt {attempt + 1}): {e}")
                    import traceback
                    logger.error(f"Traceback: {traceback.format_exc()}")
                    if attempt < max_retries:
                        time.sleep(1)
                    else:
                        judgment = {
                            "judgment": None,
                            "reasoning": f"Failed to get judgment after {max_retries + 1} attempts: {str(e)}",
                            "confidence": "Low"
                        }
            
            if judgment is None or judgment.get("judgment") not in ["true", "false"]:
                judgment = {
                    "judgment": None,
                    "reasoning": f"Failed to get valid judgment after {max_retries + 1} attempts",
                    "confidence": "Low"
                }
        
        # Persist evaluation log and metadata in unified format
        try:
            # clean eval_log, remove all base64 data to avoid JSON file too large
            cleaned_eval_log = self._clean_eval_log_for_json(self.eval_log)
            
            # create unified evaluation result
            unified_result = {
                "metadata": {
                    "task_instruction": self.task_config.get("instruction", "N/A"),
                    "model": self.model,
                    "temperature": self.temperature,
                    "observation_type": self.observation_type,
                    "effort": self.effort,
                    "timestamp": self.session_timestamp,
                    "trajectory_id": self.log_dir.name.split('_')[0],
                    "total_interactions": len(self.eval_log),
                    "conversation_summary": {
                        "total_messages": len(self.conversation_history),
                        "user_messages": len([msg for msg in self.conversation_history if msg.get("role") == "user"]),
                        "assistant_messages": len([msg for msg in self.conversation_history if msg.get("role") == "assistant"])
                    },
                    "ground_truth": self.ground_truth
                },
                "evaluation_steps": cleaned_eval_log,
                "final_judgment": {
                    "judgment": judgment.get("judgment", "N/A"),
                    "detailed_reasoning": judgment.get("reasoning", "N/A"),
                    "confidence": judgment.get("confidence", "N/A"),
                    "judgment_timestamp": datetime.now(timezone.utc).isoformat()
                },
                "statistics_summary": {
                    "evaluation_quality": f"{judgment.get('confidence', 'N/A')} confidence evaluation",
                    "ground_truth": (self.ground_truth or "N/A"),
                    "agent_judgment": judgment.get("judgment", "N/A"),
                    "is_judgment_correct": (
                        (judgment.get("judgment") == self.ground_truth)
                        if self.ground_truth in ["true", "false"] else "N/A"
                    )
                }
            }
            
            # save unified evaluation result file
            self._write_json(self.log_dir / "unified_evaluation_result.json", unified_result)
            
            logger.info(f"✅ Unified evaluation result saved to: {self.log_dir / 'unified_evaluation_result.json'}")
            logger.info(f"📊 Total interactions: {len(self.eval_log)}")
            logger.info(f"🏆 Agent judgment: {judgment.get('judgment', 'N/A')}")
            logger.info(f"🎯 Ground truth: {self.ground_truth or 'N/A'}")
            if self.ground_truth in ["true", "false"]:
                is_correct = judgment.get('judgment') == self.ground_truth
                logger.info(f"✅ Judgment is correct: {'Yes' if is_correct else 'No'}")
                logger.info(f"📈 Judgment accuracy: {is_correct}")
        
        except Exception as e:
            logger.warning(f"Failed to write evaluation logs: {e}")
        
        return {
            "success": True,
            "judgment": judgment,
            "conversation_history": self.conversation_history,
            "log_directory": str(self.log_dir),
            "total_interactions": len(self.eval_log)
        }
    
    def _clean_eval_log_for_json(self, eval_log: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        clean eval_log, remove all base64 encoded screenshot data, only keep file path or metadata         
        Args:
            eval_log: original evaluation log list
        Returns:
            cleaned evaluation log list
        """
        cleaned_log = []
        
        for entry in eval_log:
            cleaned_entry = entry.copy()
            
            # clean trajectory_step_info from base64 if exists
            if "trajectory_step_info" in cleaned_entry and isinstance(cleaned_entry["trajectory_step_info"], dict):
                step_info = cleaned_entry["trajectory_step_info"].copy()
                # remove possible base64 fields
                step_info.pop("screenshot_b64", None)
                step_info.pop("trajectory_screenshot_b64", None)
                cleaned_entry["trajectory_step_info"] = step_info
            
            # clean trajectory_a11y_tree: if too long, only keep summary
            if "trajectory_a11y_tree" in cleaned_entry:
                tree_data = cleaned_entry["trajectory_a11y_tree"]
                if isinstance(tree_data, str):

                    if len(tree_data) > 50000:
                        cleaned_entry["trajectory_a11y_tree"] = (
                            tree_data[:1000] + 
                            f"\n\n[... truncated {len(tree_data) - 2000} chars ...]\n\n" + 
                            tree_data[-1000:]
                        )
                        logger.debug(f"Truncated large trajectory_a11y_tree from {len(tree_data)} to ~2000 chars")
            
            # screenshot: check if it contains base64 by mistake
            if "screenshot" in cleaned_entry and cleaned_entry["screenshot"]:
                screenshot_val = cleaned_entry["screenshot"]
                # if screenshot looks like base64, replace with placeholder
                if isinstance(screenshot_val, str) and len(screenshot_val) > 5000 and not any(
                    screenshot_val.startswith(prefix) for prefix in ["/", "./", "interaction_", "step_"]
                ):
                    cleaned_entry["screenshot"] = "[Base64 data removed - screenshot should be file path]"
                    logger.warning("Found base64 data in screenshot field, replaced with placeholder")
            
            cleaned_log.append(cleaned_entry)
        
        return cleaned_log
    
    def _write_json(self, path: Path, data: Dict[str, Any]):
        try:
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            logger.error(f"Failed to write json to {path}: {e}")
            raise RuntimeError(f"Failed to save evaluation result to {path}: {e}") from e
    
    def _write_jsonl(self, path: Path, rows: List[Dict[str, Any]]):
        try:
            with open(path, 'w', encoding='utf-8') as f:
                for row in rows:
                    f.write(json.dumps(row, ensure_ascii=False) + "\n")
        except Exception as e:
            logger.warning(f"Failed to write jsonl to {path}: {e}")
    
    def _save_env_screenshot(self, env: Any, name: str, include_timestamp: bool = False) -> Optional[Path]:
        """
        save environment screenshot
        Args:
            env: environment object
            name: file name (without extension)
            include_timestamp: whether to include timestamp in file name
        """
        try:
            img = env.render(mode='rgb_array')
            if img is None:
                raise RuntimeError("render() returned None")

            if include_timestamp:
                timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S_%f")[:-3]  # 精确到毫秒
                name = f"{name}_{timestamp}"
            
            # handle path
            if "/" in name:
                parts = name.split("/")
                dir_path = self.log_dir / "/".join(parts[:-1])
                dir_path.mkdir(parents=True, exist_ok=True)
                file_path = dir_path / f"{parts[-1]}.png"
            else:
                file_path = self.log_dir / f"{name}.png"
            
            if isinstance(img, (bytes, bytearray)):
                with open(file_path, 'wb') as f:
                    f.write(img)
            else:
                from PIL import Image
                import numpy as np
                
                if hasattr(img, 'save'):
                    img.save(file_path)
                else:
                    image = Image.fromarray(np.asarray(img))
                    image.save(file_path)
            
            logger.debug(f"Saved screenshot: {file_path}")
            return file_path
        
        except Exception as e:
            logger.warning(f"Failed to save screenshot: {e}")
            import traceback
            logger.debug(f"Screenshot save error details: {traceback.format_exc()}")
            return None
    
    def _cleanup_environment(self):
        """
        Clean up environment with enhanced error handling and forced cleanup
        """
        logger.info("Cleaning up environment...")
        
        # Clean up environment
        if self.env:
            try:
                logger.info("Closing environment...")
                self.env.close()
                logger.info("Environment closed successfully")
            except Exception as e:
                logger.warning(f"Error closing environment: {e}")
                # Force cleanup even if close() fails
                try:
                    if hasattr(self.env, 'provider') and hasattr(self.env.provider, 'stop_emulator'):
                        self.env.provider.stop_emulator(self.env.path_to_vm)
                        logger.info("Force terminated environment")
                except Exception as force_e:
                    logger.error(f"Force cleanup failed for environment: {force_e}")
        
        # Clean up replay manager
        if self.replay_manager:
            try:
                logger.info("Cleaning up replay manager...")
                # Add any specific cleanup for replay manager if needed
            except Exception as e:
                logger.warning(f"Error cleaning up replay manager: {e}")
        
        # Clean up MCP client
        if self.mcp_client:
            try:
                logger.info("Stopping MCP server...")
                self.mcp_client.stop_server()
                logger.info("MCP server stopped successfully")
            except Exception as e:
                logger.warning(f"Error stopping MCP server: {e}")
        
        # Reset all references
        self.env = None
        self.replay_manager = None
        self.mcp_client = None
        
        logger.info("Environment cleanup completed")
        
        # Add a small delay to ensure AWS instances have time to terminate
        time.sleep(2)
    
    def evaluate_task(self, pairs_root_dir: str, task_id: str, trajectory_type: str) -> Dict[str, Any]:
        """
        Complete evaluation workflow
        
        Args:
            pairs_root_dir: pairs root directory path
            task_id: task ID
            trajectory_type: trajectory type ("true" or "false")
            
        Returns:
            evaluation result
        """
        try:
            # Step 1: Load task data
            logger.info("Step 1: Loading task data...")
            self.load_task_data(pairs_root_dir, task_id, trajectory_type)
            
            # Step 2: Initialize environment
            logger.info("Step 2: Initializing environment...")
            if not self.initialize_environment():
                return {"success": False, "error": "Failed to initialize environment"}
            
            # Step 3: Replay trajectory
            logger.info("Step 3: Replaying trajectory...")
            if not self.replay_trajectory():
                return {"success": False, "error": "Failed to replay trajectory"}
            
            # Step 4: Start evaluation
            logger.info("Step 4: Starting evaluation...")
            result = self.start_evaluation()
            
            return result
        
        except Exception as e:
            logger.error(f"Evaluation failed: {e}")
            import traceback
            logger.error(f"Traceback: {traceback.format_exc()}")
            return {"success": False, "error": str(e)}
        
        finally:
            # Cleanup
            logger.info("Step 5: Cleanup...")
            self._cleanup_environment()


def main():
    """Test entry"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Single Judge Agent")
    parser.add_argument("--task_id", required=True, help="task ID（pair directory name）")
    parser.add_argument("--trajectory_type", required=True, choices=["true", "false"], help="trajectory type: true or false")
    parser.add_argument("--output_dir", help="output directory")
    parser.add_argument("--pairs_root_dir", default="/home/ubuntu/AJ-Bench/src/data/GUI", help="pairs root directory path")
    parser.add_argument("--model", default="gpt-4o", help="model name")
    parser.add_argument("--observation_type", default="a11y_tree", help="observation type")
    parser.add_argument("--provider", default="aws", help="virtualization provider")
    parser.add_argument("--region", default="us-east-1", help="AWS region")
    parser.add_argument("--screen_width", type=int, default=1920, help="screen width")
    parser.add_argument("--screen_height", type=int, default=1080, help="screen height")
    parser.add_argument("--effort", default="medium", choices=["low", "medium", "high"], help="effort level")
    parser.add_argument(
        "--temperature",
        type=float,
        default=None,
        help="API called temperature parameter (if not provided, use model default temperature)"
    )
    
    args = parser.parse_args()
    
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    # Explicitly set root logger level to INFO to suppress DEBUG messages
    logging.getLogger().setLevel(logging.INFO)
    
    logging.getLogger('boto3').setLevel(logging.WARNING)
    logging.getLogger('botocore').setLevel(logging.WARNING)
    logging.getLogger('urllib3').setLevel(logging.WARNING)
    logging.getLogger('s3transfer').setLevel(logging.WARNING)
    logging.getLogger('boto').setLevel(logging.WARNING)
    
    # build trajectory_id for output directory naming
    trajectory_id = f"{args.task_id}_{args.trajectory_type}"
    
    # Create agent
    agent = SingleJudgeAgentMCP(
        model=args.model,
        temperature=args.temperature,
        observation_type=args.observation_type,
        trajectory_id=trajectory_id,
        output_dir=args.output_dir,
        trajectory_type=args.trajectory_type,
        provider=args.provider,
        region=args.region,
        screen_width=args.screen_width,
        screen_height=args.screen_height,
        effort=args.effort
    )
    
    # Run evaluation
    result = agent.evaluate_task(
        pairs_root_dir=args.pairs_root_dir,
        task_id=args.task_id,
        trajectory_type=args.trajectory_type
    )
    
    print("\nEvaluation Result:")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

