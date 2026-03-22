#!/usr/bin/env python3
"""
OSWorld MCP Server
Through stdio communication, the single_judge can call the MCP Client.

Usage:
    python -m src.mcp_services.gui.gui_mcp_server
"""

import asyncio
import json
import sys
import os
import logging
import base64
import time
from pathlib import Path
from typing import Any, Dict, Optional

try:
    from .osworld_modules.desktop_env.desktop_env import DesktopEnv
    from .osworld_modules.replay.task_replay import TaskReplayManager
    from .osworld_modules.replay.lib_replay_trajectory import load_trajectory, replay_trajectory
except ImportError:
    import sys
    from pathlib import Path
    if "PYTHONPATH" in os.environ:
        pythonpath_dirs = os.environ["PYTHONPATH"].split(os.pathsep)
        for path_dir in pythonpath_dirs:
            if path_dir and path_dir not in sys.path:
                sys.path.insert(0, path_dir)
    src_dir = Path(__file__).parent.parent.parent
    if str(src_dir) not in sys.path:
        sys.path.insert(0, str(src_dir))
    
    mcpmark_root = src_dir.parent
    if str(mcpmark_root) not in sys.path:
        sys.path.insert(0, str(mcpmark_root))
    
    try:
        from mcp_services.gui.osworld_modules.desktop_env.desktop_env import DesktopEnv
        from mcp_services.gui.osworld_modules.replay.task_replay import TaskReplayManager
        from mcp_services.gui.osworld_modules.replay.lib_replay_trajectory import load_trajectory, replay_trajectory
    except ImportError as e:
        print(f"Error: Failed to import OSWorld modules", file=sys.stderr)
        print(f"Current sys.path: {sys.path}", file=sys.stderr)
        print(f"PYTHONPATH: {os.environ.get('PYTHONPATH', 'Not set')}", file=sys.stderr)
        print(f"__file__: {__file__}", file=sys.stderr)
        print(f"src_dir: {src_dir}", file=sys.stderr)
        print(f"mcpmark_root: {mcpmark_root}", file=sys.stderr)
        raise

# MCP SDK
try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import Tool, TextContent
except ImportError:
    print("Error: MCP SDK not installed. Please run: pip install mcp", file=sys.stderr)
    sys.exit(1)

logger = logging.getLogger(__name__)

class OSWorldEnvironmentState:
    """Manage OSWorld environment state"""
    
    def __init__(self):
        self.env: Optional[Any] = None
        self.replay_manager: Optional[Any] = None
        self.task_config: Optional[Dict] = None
        self.trajectory: Optional[list] = None
        self.initialized: bool = False
    
    def reset(self):
        """Reset state"""
        if self.env:
            try:
                self.env.close()
            except Exception as e:
                logger.warning(f"Error closing environment: {e}")
        
        self.env = None
        self.replay_manager = None
        self.task_config = None
        self.trajectory = None
        self.trajectory_path = None
        self.replay_result_dir = None
        self.initialized = False

env_state = OSWorldEnvironmentState()

server = Server("osworld-mcp")

@server.list_tools()
async def list_tools() -> list[Tool]:
    tools = [
        Tool(
            name="osworld_initialize",
            description="Initialize OSWorld environment",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_config_path": {"type": "string", "description": "Path to task configuration file"},
                    "provider": {"type": "string", "default": "aws", "description": "Virtualization provider"},
                    "region": {"type": "string", "default": "us-east-1", "description": "AWS region"},
                    "screen_width": {"type": "integer", "default": 1920},
                    "screen_height": {"type": "integer", "default": 1080}
                },
                "required": ["task_config_path"]
            }
        ),
        Tool(
            name="osworld_replay_trajectory",
            description="Replay a trajectory in the environment",
            inputSchema={
                "type": "object",
                "properties": {
                    "trajectory_path": {"type": "string", "description": "Path to trajectory file"},
                    "result_dir": {"type": "string", "description": "Directory to save replay results"},
                    "save_screenshots": {"type": "boolean", "description": "Whether to save screenshots for each step", "default": False}
                },
                "required": ["trajectory_path"]
            }
        ),
        Tool(
            name="osworld_get_observation",
            description="Get environment observation (screenshot and/or accessibility tree)",
            inputSchema={
                "type": "object",
                "properties": {
                    "observation_type": {
                        "type": "string",
                        "enum": ["screenshot", "a11y_tree", "screenshot_a11y_tree", "raw_a11y_tree"],
                        "default": "screenshot"
                    }
                }
            }
        ),
        Tool(
            name="osworld_close",
            description="Close environment and clean up resources",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="osworld_get_status",
            description="Get environment status",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="click",
            description="Click mouse button",
            inputSchema={
                "type": "object",
                "properties": {
                    "x": {"type": "number", "description": "X coordinate"},
                    "y": {"type": "number", "description": "Y coordinate"},
                    "button": {"type": "string", "enum": ["left", "right", "middle"], "default": "left", "description": "Mouse button"},
                    "num_clicks": {"type": "integer", "default": 1, "description": "Number of clicks"}
                }
            }
        ),
        Tool(
            name="double_click",
            description="Double click mouse",
            inputSchema={
                "type": "object",
                "properties": {
                    "x": {"type": "number", "description": "X coordinate"},
                    "y": {"type": "number", "description": "Y coordinate"}
                }
            }
        ),
        Tool(
            name="right_click",
            description="Right click mouse",
            inputSchema={
                "type": "object",
                "properties": {
                    "x": {"type": "number", "description": "X coordinate"},
                    "y": {"type": "number", "description": "Y coordinate"}
                }
            }
        ),
        Tool(
            name="mouse_down",
            description="Press mouse button down",
            inputSchema={
                "type": "object",
                "properties": {
                    "button": {"type": "string", "enum": ["left", "right", "middle"], "default": "left", "description": "Mouse button"}
                }
            }
        ),
        Tool(
            name="mouse_up",
            description="Release mouse button",
            inputSchema={
                "type": "object",
                "properties": {
                    "button": {"type": "string", "enum": ["left", "right", "middle"], "default": "left", "description": "Mouse button"}
                }
            }
        ),
        Tool(
            name="drag_to",
            description="Drag to position",
            inputSchema={
                "type": "object",
                "properties": {
                    "x": {"type": "number", "description": "Target X coordinate"},
                    "y": {"type": "number", "description": "Target Y coordinate"}
                },
                "required": ["x", "y"]
            }
        ),
        Tool(
            name="scroll",
            description="Scroll screen",
            inputSchema={
                "type": "object",
                "properties": {
                    "dx": {"type": "integer", "description": "Horizontal scroll amount"},
                    "dy": {"type": "integer", "description": "Vertical scroll amount"}
                }
            }
        ),
        Tool(
            name="typing",
            description="Type text",
            inputSchema={
                "type": "object",
                "properties": {
                    "text": {"type": "string", "description": "Text to type"}
                },
                "required": ["text"]
            }
        ),
        Tool(
            name="press",
            description="Press key",
            inputSchema={
                "type": "object",
                "properties": {
                    "key": {"type": "string", "description": "Key to press"}
                },
                "required": ["key"]
            }
        ),
        Tool(
            name="key_down",
            description="Press key down",
            inputSchema={
                "type": "object",
                "properties": {
                    "key": {"type": "string", "description": "Key to press down"}
                },
                "required": ["key"]
            }
        ),
        Tool(
            name="key_up",
            description="Release key",
            inputSchema={
                "type": "object",
                "properties": {
                    "key": {"type": "string", "description": "Key to release"}
                },
                "required": ["key"]
            }
        ),
        Tool(
            name="hotkey",
            description="Press hotkey",
            inputSchema={
                "type": "object",
                "properties": {
                    "keys": {"type": "array", "items": {"type": "string"}, "description": "Keys to press in combination"}
                },
                "required": ["keys"]
            }
        ),
        Tool(
            name="done",
            description="Mark evaluation as done",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="wait",
            description="Wait",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="view_trajectory_step",
            description="View trajectory step",
            inputSchema={
                "type": "object",
                "properties": {
                    "step": {"type": "integer", "description": "Step number (1-indexed)"}
                },
                "required": ["step"]
            }
        ),
        Tool(
            name="osworld_execute_action",
            description="Execute an action in the environment using a pyautogui command string. Prefer specific tools (click, typing, etc.) when possible.",
            inputSchema={
                "type": "object",
                "properties": {
                    "action_command": {"type": "string", "description": "pyautogui command string"}
                },
                "required": ["action_command"]
            }
        )
    ]
    return tools

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    try:
        logger.info(f"Calling tool '{name}' with arguments: {arguments}")
        
        if isinstance(arguments, dict):
            cleaned_args = {}
            for key, value in arguments.items():
                if key in ["screen_width", "screen_height", "step", "num_clicks", "dx", "dy"]:
                    cleaned_args[key] = int(value) if value is not None else None
                elif key in ["x", "y"]:
                    cleaned_args[key] = float(value) if value is not None else None
                elif key in ["task_config_path", "trajectory_path", "result_dir", "provider", "region", "observation_type", "action_command", "text", "key", "button"]:
                    cleaned_args[key] = str(value) if value is not None else ""
                elif key == "keys":
                    cleaned_args[key] = value if isinstance(value, list) else []
                elif key in ["save_screenshots"]:
                    cleaned_args[key] = bool(value) if value is not None else False
                else:
                    cleaned_args[key] = value
            arguments = cleaned_args
        
        if name == "osworld_initialize":
            result = await _initialize_environment(arguments)
        elif name == "osworld_replay_trajectory":
            result = await _replay_trajectory(arguments)
        elif name == "osworld_get_observation":
            result = await _get_observation(arguments)
        elif name == "osworld_close":
            result = await _close_environment(arguments)
        elif name == "osworld_get_status":
            result = await _get_status(arguments)
        elif name == "click":
            result = await _execute_click(arguments)
        elif name == "double_click":
            result = await _execute_double_click(arguments)
        elif name == "right_click":
            result = await _execute_right_click(arguments)
        elif name == "mouse_down":
            result = await _execute_mouse_down(arguments)
        elif name == "mouse_up":
            result = await _execute_mouse_up(arguments)
        elif name == "drag_to":
            result = await _execute_drag_to(arguments)
        elif name == "scroll":
            result = await _execute_scroll(arguments)
        elif name == "typing":
            result = await _execute_typing(arguments)
        elif name == "press":
            result = await _execute_press(arguments)
        elif name == "key_down":
            result = await _execute_key_down(arguments)
        elif name == "key_up":
            result = await _execute_key_up(arguments)
        elif name == "hotkey":
            result = await _execute_hotkey(arguments)
        elif name == "done":
            result = await _execute_done(arguments)
        elif name == "wait":
            result = await _execute_wait(arguments)
        elif name == "view_trajectory_step":
            result = await _execute_view_trajectory_step(arguments)
        elif name == "osworld_execute_action":
            result = await _execute_action(arguments)
        else:
            result = {"success": False, "error": f"Unknown tool: {name}"}
        
        logger.info(f"Tool '{name}' completed with result: {result.get('success', 'N/A')}")
        return [TextContent(type="text", text=json.dumps(result, ensure_ascii=False))]
    
    except Exception as e:
        logger.error(f"Tool execution failed: {e}")
        import traceback
        error_traceback = traceback.format_exc()
        logger.error(f"Traceback: {error_traceback}")
        return [TextContent(type="text", text=json.dumps({
            "success": False,
            "error": str(e),
            "traceback": error_traceback
        }, ensure_ascii=False))]

# ===================Helper Functions ========================

def _wait_for_accessibility_service(env, timeout: int = 30) -> bool:
    logger.info("Waiting for accessibility service to be ready...")
    
    start_time = time.time()
    max_attempts = timeout // 3
    
    for attempt in range(max_attempts):
        try:
            if hasattr(env, "controller") and hasattr(env.controller, "get_accessibility_tree"):
                a11y_tree = env.controller.get_accessibility_tree()
                if a11y_tree and len(a11y_tree) > 10000:
                    elapsed = time.time() - start_time
                    logger.info(f"✅ Accessibility service ready (took {elapsed:.1f}s, tree size: {len(a11y_tree)} bytes)")
                    return True
                else:
                    logger.info(f"⏳ Accessibility service not ready yet (attempt {attempt + 1}/{max_attempts})...")
            else:
                logger.warning("⚠️ Environment doesn't support accessibility tree")
                return False
                
        except Exception as e:
            logger.debug(f"Accessibility check failed (attempt {attempt + 1}): {e}")
        
        time.sleep(3)
    
    logger.warning(f"⚠️ Accessibility service didn't become ready within {timeout}s, continuing anyway...")
    return False

# ==================== Tool Implementation Functions ====================


async def _initialize_environment(args: dict) -> dict:
    task_config_path = args["task_config_path"]
    provider = args.get("provider", "aws")
    region = args.get("region", "us-east-1")
    screen_width = args.get("screen_width", 1920)
    screen_height = args.get("screen_height", 1080)
    
    try:
        with open(task_config_path, 'r', encoding='utf-8') as f:
            env_state.task_config = json.load(f)
        
        logger.info("Starting environment initialization in main thread...")
        
        try:
            env_state.replay_manager = TaskReplayManager(provider=provider, region=region)
            
            env_state.env = env_state.replay_manager.initialize_environment(
                env_state.task_config,
                screen_width=screen_width,
                screen_height=screen_height,
                headless=True
            )
            
            if env_state.env is None:
                raise RuntimeError("Failed to initialize environment (env is None)")
            
            try:
                from .osworld_modules.replay.lib_replay_trajectory import _wait_for_vnc_ready
            except ImportError:
                from mcp_services.gui.osworld_modules.replay.lib_replay_trajectory import _wait_for_vnc_ready
            if not _wait_for_vnc_ready(env_state.env, 60):
                raise RuntimeError("Environment VNC service not ready")
            
            logger.info("Verifying HTTP service (port 5000) availability...")
            try:
                import requests
                if hasattr(env_state.env, 'controller') and hasattr(env_state.env.controller, 'http_server'):
                    http_server = env_state.env.controller.http_server
                    max_wait = 120
                    check_interval = 2
                    waited = 0
                    service_ready = False
                    
                    endpoints_to_try = ["/terminal", "/screenshot", "/"]
                    
                    while waited < max_wait:
                        for endpoint in endpoints_to_try:
                            try:
                                response = requests.get(http_server + endpoint, timeout=2)
                                if response.status_code in [200, 404, 405]:
                                    logger.info(f"✅ HTTP service is ready after {waited}s (endpoint: {endpoint}, status: {response.status_code})")
                                    service_ready = True
                                    break
                            except requests.exceptions.Timeout:
                                pass
                            except requests.exceptions.ConnectionError:
                                pass
                            except Exception as e:
                                logger.debug(f"HTTP service check failed for {endpoint} (waited {waited}s): {e}")
                        
                        if service_ready:
                            break
                        
                        if waited % 10 == 0 and waited > 0:
                            logger.info(f"Still waiting for HTTP service... (waited {waited}s)")
                        
                        time.sleep(check_interval)
                        waited += check_interval
                    
                    if not service_ready:
                        logger.warning(f"⚠️ HTTP service not ready after {max_wait}s, but continuing (reset() will retry with its own timeout)")
                        logger.warning("This may indicate a network issue or the service needs more time to start")
                else:
                    logger.warning("⚠️ Cannot verify HTTP service (no http_server info)")
            except Exception as e:
                logger.warning(f"⚠️ HTTP service verification failed: {e}, but continuing")
            
            logger.info("Executing setup steps from task config...")
            try:
                env_state.env.reset(task_config=env_state.task_config)
                logger.info("✅ Setup steps completed successfully")
            except Exception as e:
                logger.error(f"❌ Setup steps failed: {e}")
                import traceback
                logger.error(f"Setup traceback: {traceback.format_exc()}")
                raise RuntimeError(f"Setup steps execution failed: {e}") from e
            
            logger.info("Waiting for accessibility service to be ready...")
            _wait_for_accessibility_service(env_state.env, timeout=30)
            
            env_state.initialized = True
            logger.info("Environment initialization completed successfully")
        except Exception as e:
            logger.error(f"Environment initialization failed: {e}")
            env_state.reset()
            raise
        
        result = {
            "success": True,
            "message": "Environment initialized successfully",
            "task_instruction": env_state.task_config.get("instruction", "N/A")
        }
        
        # Add instance ID if available
        if env_state.env and hasattr(env_state.env, "path_to_vm"):
            result["instance_id"] = env_state.env.path_to_vm
            logger.info(f"Environment initialized with instance ID: {result['instance_id']}")
            
        return result
    
    except Exception as e:
        logger.error(f"Failed to initialize environment: {e}")
        import traceback
        logger.error(f"Traceback: {traceback.format_exc()}")
        env_state.reset()
        return {"success": False, "error": str(e)}

async def _replay_trajectory(args: dict) -> dict:
    if not env_state.initialized or env_state.env is None:
        return {"success": False, "error": "Environment not initialized"}
    
    trajectory_path = args["trajectory_path"]
    result_dir = args.get("result_dir")
    
    try:
        env_state.trajectory_path = trajectory_path
        env_state.replay_result_dir = result_dir
        
        env_state.trajectory = load_trajectory(trajectory_path)
        logger.info(f"Loaded trajectory with {len(env_state.trajectory)} steps")
        
        def _run_replay():
            """Synchronous function running in thread."""
            try:
                logger.info("Starting trajectory replay (env.reset will be called to ensure clean state)...")
                
                logger.info("Checking service availability before reset()...")
                try:
                    import requests
                    if hasattr(env_state.env, 'controller') and hasattr(env_state.env.controller, 'http_server'):
                        http_server = env_state.env.controller.http_server
                        logger.info(f"Quick check for service at {http_server}...")
                        
                        max_wait = 10
                        check_interval = 1
                        waited = 0
                        service_ready = False
                        
                        endpoints_to_try = ["/terminal", "/screenshot", "/"]
                        
                        while waited < max_wait:
                            for endpoint in endpoints_to_try:
                                try:
                                    response = requests.get(http_server + endpoint, timeout=1)
                                    if response.status_code in [200, 404, 405]:
                                        logger.info(f"✅ Service is ready (endpoint: {endpoint}, status: {response.status_code})")
                                        service_ready = True
                                        break
                                except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
                                    pass
                                except Exception:
                                    pass
                            
                            if service_ready:
                                break
                            
                            time.sleep(check_interval)
                            waited += check_interval
                        
                        if not service_ready:
                            logger.info(f"Service not immediately available (checked {max_wait}s), but setup() will retry with timeout protection")
                    else:
                        logger.info("⚠️ Cannot check service availability (no http_server info), proceeding with reset()")
                except Exception as e:
                    logger.debug(f"Service readiness check failed: {e}, but proceeding with reset() (setup() will handle retries)")
                
                save_screenshots = args.get("save_screenshots", False)
                
                replay_trajectory(
                    env=env_state.env,
                    trajectory=env_state.trajectory,
                    sleep_after_execution=0.5,
                    save_replay_results=True if result_dir else False,
                    replay_result_dir=result_dir,
                    wait_for_vnc=True,
                    vnc_wait_timeout=30,
                    task_config=env_state.task_config,
                    target_screen_size=(env_state.task_config.get("screen_width", 1920), 
                                       env_state.task_config.get("screen_height", 1080)),
                    debug_mode=False,
                    enable_click=True,
                    save_screenshots=save_screenshots
                )
                
                logger.info("✅ Trajectory replay completed, a11y_tree files saved to replay_result_dir/a11y_tree/")
                return True
            except Exception as e:
                logger.error(f"Replay failed in thread: {e}")
                raise
        
        import concurrent.futures
        loop = asyncio.get_event_loop()
        
        logger.info("Starting trajectory replay in thread pool...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            future = loop.run_in_executor(executor, _run_replay)
            try:
                await asyncio.wait_for(future, timeout=1800)
                logger.info("Trajectory replay completed successfully")
            except asyncio.TimeoutError:
                logger.error("Trajectory replay timed out after 30 minutes")
                return {"success": False, "error": "Trajectory replay timed out after 30 minutes"}
        
        return {
            "success": True,
            "message": f"Trajectory replayed successfully ({len(env_state.trajectory)} steps)"
        }
    
    except Exception as e:
        logger.error(f"Failed to replay trajectory: {e}")
        import traceback
        logger.error(f"Traceback: {traceback.format_exc()}")
        return {"success": False, "error": str(e)}

async def _get_observation(args: dict) -> dict:
    if not env_state.initialized or env_state.env is None:
        return {"success": False, "error": "Environment not initialized"}
    
    observation_type = args.get("observation_type", "screenshot")
    
    try:
        def _get_obs_sync():
            """Synchronous function running in thread."""
            obs = {}
            
            if observation_type in ["screenshot", "screenshot_a11y_tree"]:
                try:
                    img = env_state.env.render(mode='rgb_array')
                    if img is not None:
                        if isinstance(img, (bytes, bytearray)):
                            screenshot_b64 = base64.b64encode(img).decode('utf-8')
                        else:
                            from PIL import Image
                            import numpy as np
                            from io import BytesIO
                            
                            if hasattr(img, 'save'):
                                buffer = BytesIO()
                                img.save(buffer, format='PNG')
                                screenshot_b64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
                            else:
                                image = Image.fromarray(np.asarray(img))
                                buffer = BytesIO()
                                image.save(buffer, format='PNG')
                                screenshot_b64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
                        
                        obs["screenshot_b64"] = screenshot_b64
                except Exception as e:
                    logger.warning(f"Failed to get screenshot: {e}")
                    obs["screenshot_b64"] = None
            
            if observation_type == "raw_a11y_tree":
                try:
                    if hasattr(env_state.env, "controller") and hasattr(env_state.env.controller, "get_accessibility_tree"):
                        raw_a11y_tree = env_state.env.controller.get_accessibility_tree()
                        obs["raw_a11y_tree"] = raw_a11y_tree if raw_a11y_tree else None
                    else:
                        obs["raw_a11y_tree"] = None
                except Exception as e:
                    logger.warning(f"Failed to get raw a11y_tree: {e}")
                    obs["raw_a11y_tree"] = None
            
            if observation_type in ["a11y_tree", "screenshot_a11y_tree"]:
                try:
                    if hasattr(env_state.env, "controller") and hasattr(env_state.env.controller, "get_accessibility_tree"):
                        raw_a11y_tree = env_state.env.controller.get_accessibility_tree()
                        
                        if raw_a11y_tree:
                            try:
                                from .osworld_modules.mm_agents.agent import linearize_accessibility_tree
                            except ImportError:
                                from mcp_services.gui.osworld_modules.mm_agents.agent import linearize_accessibility_tree
                            linearized_tree = linearize_accessibility_tree(raw_a11y_tree, platform="ubuntu")
                            
                            max_chars = 15000
                            if len(linearized_tree) > max_chars:
                                truncated = linearized_tree[:max_chars]
                                truncation_marker = f"\n\n[TRUNCATED] Tree truncated at {max_chars:,} chars.\n"
                                obs["a11y_tree"] = truncated + truncation_marker
                            else:
                                obs["a11y_tree"] = linearized_tree
                        else:
                            obs["a11y_tree"] = "Accessibility tree not available"
                except Exception as e:
                    logger.warning(f"Failed to get a11y_tree: {e}")
                    obs["a11y_tree"] = "Accessibility tree not available"
            
            return obs
        
        import concurrent.futures
        loop = asyncio.get_event_loop()
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            future = loop.run_in_executor(executor, _get_obs_sync)
            observation = await asyncio.wait_for(future, timeout=60)
        
        return {
            "success": True,
            "observation": observation
        }
    
    except asyncio.TimeoutError:
        logger.error("Get observation timed out after 60 seconds")
        return {"success": False, "error": "Get observation timed out"}
    except Exception as e:
        logger.error(f"Failed to get observation: {e}")
        import traceback
        logger.error(f"Traceback: {traceback.format_exc()}")
        return {"success": False, "error": str(e)}

# ==================== Action Execution Functions ====================

def _convert_action_to_command(action: dict) -> str:
    action_type = action.get("action_type", "").upper()
    parameters = action.get("parameters", {})
    
    if action_type == "CLICK":
        if not parameters or parameters == {}:
            return "pyautogui.click()"
        elif "button" in parameters and "x" in parameters and "y" in parameters:
            button = parameters["button"]
            x = parameters["x"]
            y = parameters["y"]
            if "num_clicks" in parameters:
                num_clicks = parameters["num_clicks"]
                return f"pyautogui.click(button='{button}', x={x}, y={y}, clicks={num_clicks})"
            else:
                return f"pyautogui.click(button='{button}', x={x}, y={y})"
        elif "button" in parameters and "x" not in parameters and "y" not in parameters:
            button = parameters["button"]
            if "num_clicks" in parameters:
                num_clicks = parameters["num_clicks"]
                return f"pyautogui.click(button='{button}', clicks={num_clicks})"
            else:
                return f"pyautogui.click(button='{button}')"
        elif "button" not in parameters and "x" in parameters and "y" in parameters:
            x = parameters["x"]
            y = parameters["y"]
            if "num_clicks" in parameters:
                num_clicks = parameters["num_clicks"]
                return f"pyautogui.click(x={x}, y={y}, clicks={num_clicks})"
            else:
                return f"pyautogui.click(x={x}, y={y})"
        else:
            return "pyautogui.click()"
    
    elif action_type == "DOUBLE_CLICK":
        if "x" in parameters and "y" in parameters:
            x = parameters["x"]
            y = parameters["y"]
            return f"pyautogui.doubleClick(x={x}, y={y})"
        else:
            return "pyautogui.doubleClick()"
    
    elif action_type == "RIGHT_CLICK":
        if "x" in parameters and "y" in parameters:
            x = parameters["x"]
            y = parameters["y"]
            return f"pyautogui.rightClick(x={x}, y={y})"
        else:
            return "pyautogui.rightClick()"
    
    elif action_type == "MOUSE_DOWN":
        if "button" in parameters:
            button = parameters["button"]
            return f"pyautogui.mouseDown(button='{button}')"
        else:
            return "pyautogui.mouseDown()"
    
    elif action_type == "MOUSE_UP":
        if "button" in parameters:
            button = parameters["button"]
            return f"pyautogui.mouseUp(button='{button}')"
        else:
            return "pyautogui.mouseUp()"
    
    elif action_type == "DRAG_TO":
        if "x" in parameters and "y" in parameters:
            x = parameters["x"]
            y = parameters["y"]
            return f"pyautogui.dragTo({x}, {y}, duration=1.0, button='left', mouseDownUp=True)"
        else:
            raise ValueError("DRAG_TO requires x and y parameters")
    
    elif action_type == "SCROLL":
        if "dx" in parameters and "dy" in parameters:
            dx = parameters["dx"]
            dy = parameters["dy"]
            return f"pyautogui.hscroll({dx})\npyautogui.vscroll({dy})"
        elif "dx" in parameters:
            dx = parameters["dx"]
            return f"pyautogui.hscroll({dx})"
        elif "dy" in parameters:
            dy = parameters["dy"]
            return f"pyautogui.vscroll({dy})"
        else:
            raise ValueError("SCROLL requires at least dx or dy parameter")
    
    elif action_type == "TYPING":
        if "text" not in parameters:
            raise ValueError("TYPING requires text parameter")
        text = parameters["text"]
        escaped_text = json.dumps(text)
        return f"pyautogui.typewrite({escaped_text})"
    
    elif action_type == "PRESS":
        if "key" not in parameters:
            raise ValueError("PRESS requires key parameter")
        key = parameters["key"]
        return f"pyautogui.press('{key}')"
    
    elif action_type == "KEY_DOWN":
        if "key" not in parameters:
            raise ValueError("KEY_DOWN requires key parameter")
        key = parameters["key"]
        return f"pyautogui.keyDown('{key}')"
    
    elif action_type == "KEY_UP":
        if "key" not in parameters:
            raise ValueError("KEY_UP requires key parameter")
        key = parameters["key"]
        return f"pyautogui.keyUp('{key}')"
    
    elif action_type == "HOTKEY":
        if "keys" not in parameters or not isinstance(parameters["keys"], list):
            raise ValueError("HOTKEY requires keys parameter as a list")
        keys = parameters["keys"]
        keys_str = "', '".join(keys)
        return f"pyautogui.hotkey('{keys_str}')"
    
    elif action_type in ["WAIT", "DONE", "FAIL"]:
        return f"# {action_type}"
    
    else:
        raise ValueError(f"Unknown action type: {action_type}")

async def _execute_action_unified(action: dict) -> dict:
    if not env_state.initialized or env_state.env is None:
        return {"success": False, "error": "Environment not initialized"}
    
    try:
        action_command = _convert_action_to_command(action)
        return await _execute_action({"action_command": action_command})
    
    except Exception as e:
        logger.error(f"Failed to execute action: {e}")
        import traceback
        logger.error(f"Traceback: {traceback.format_exc()}")
        return {"success": False, "error": str(e)}

def _execute_action_dict(action: dict) -> dict:
    if not env_state.initialized or env_state.env is None:
        return {"success": False, "error": "Environment not initialized"}
    
    try:
        if hasattr(env_state.env, "action_space") and env_state.env.action_space == "computer_13":
            env_state.env.controller.execute_action(action)
        else:
            env_state.env.step(action, pause=1.0)
        
        return {
            "success": True,
            "message": f"Action executed: {action.get('action_type', 'unknown')}"
        }
    except Exception as e:
        logger.error(f"Failed to execute action: {e}")
        import traceback
        logger.error(f"Traceback: {traceback.format_exc()}")
        return {"success": False, "error": str(e)}

# ==================== Mouse Action Handlers ====================

async def _execute_click(args: dict) -> dict:
    action = {
        "action_type": "CLICK",
        "parameters": {}
    }
    
    if "x" in args and args["x"] is not None:
        action["parameters"]["x"] = args["x"]
    if "y" in args and args["y"] is not None:
        action["parameters"]["y"] = args["y"]
    if "button" in args and args["button"]:
        action["parameters"]["button"] = args["button"]
    if "num_clicks" in args and args["num_clicks"] is not None:
        action["parameters"]["num_clicks"] = args["num_clicks"]
    
    return await _execute_action_unified(action)

async def _execute_double_click(args: dict) -> dict:
    action = {
        "action_type": "DOUBLE_CLICK",
        "parameters": {}
    }
    
    if "x" in args and args["x"] is not None:
        action["parameters"]["x"] = args["x"]
    if "y" in args and args["y"] is not None:
        action["parameters"]["y"] = args["y"]
    
    return await _execute_action_unified(action)

async def _execute_right_click(args: dict) -> dict:
    action = {
        "action_type": "RIGHT_CLICK",
        "parameters": {}
    }
    
    if "x" in args and args["x"] is not None:
        action["parameters"]["x"] = args["x"]
    if "y" in args and args["y"] is not None:
        action["parameters"]["y"] = args["y"]
    
    return await _execute_action_unified(action)

async def _execute_mouse_down(args: dict) -> dict:
    action = {
        "action_type": "MOUSE_DOWN",
        "parameters": {}
    }
    
    if "button" in args and args["button"]:
        action["parameters"]["button"] = args["button"]
    
    return await _execute_action_unified(action)

async def _execute_mouse_up(args: dict) -> dict:
    action = {
        "action_type": "MOUSE_UP",
        "parameters": {}
    }
    
    if "button" in args and args["button"]:
        action["parameters"]["button"] = args["button"]
    
    return await _execute_action_unified(action)

async def _execute_drag_to(args: dict) -> dict:
    action = {
        "action_type": "DRAG_TO",
        "parameters": {}
    }
    
    if "x" in args and args["x"] is not None:
        action["parameters"]["x"] = args["x"]
    if "y" in args and args["y"] is not None:
        action["parameters"]["y"] = args["y"]
    
    return await _execute_action_unified(action)

async def _execute_scroll(args: dict) -> dict:
    action = {
        "action_type": "SCROLL",
        "parameters": {}
    }
    
    if "dx" in args and args["dx"] is not None:
        action["parameters"]["dx"] = args["dx"]
    if "dy" in args and args["dy"] is not None:
        action["parameters"]["dy"] = args["dy"]
    
    return await _execute_action_unified(action)

# ==================== Keyboard Action Handlers ====================

async def _execute_typing(args: dict) -> dict:
    if "text" not in args or not args["text"]:
        return {"success": False, "error": "Missing required parameter: text"}
    
    action = {
        "action_type": "TYPING",
        "parameters": {
            "text": args["text"]
        }
    }
    
    return await _execute_action_unified(action)

async def _execute_press(args: dict) -> dict:
    if "key" not in args or not args["key"]:
        return {"success": False, "error": "Missing required parameter: key"}
    
    action = {
        "action_type": "PRESS",
        "parameters": {
            "key": args["key"]
        }
    }
    
    return await _execute_action_unified(action)

async def _execute_key_down(args: dict) -> dict:
    if "key" not in args or not args["key"]:
        return {"success": False, "error": "Missing required parameter: key"}
    
    action = {
        "action_type": "KEY_DOWN",
        "parameters": {
            "key": args["key"]
        }
    }
    
    return await _execute_action_unified(action)

async def _execute_key_up(args: dict) -> dict:
    if "key" not in args or not args["key"]:
        return {"success": False, "error": "Missing required parameter: key"}
    
    action = {
        "action_type": "KEY_UP",
        "parameters": {
            "key": args["key"]
        }
    }
    
    return await _execute_action_unified(action)

async def _execute_hotkey(args: dict) -> dict:
    if "keys" not in args or not args["keys"] or not isinstance(args["keys"], list):
        return {"success": False, "error": "Missing required parameter: keys (must be a list)"}
    
    action = {
        "action_type": "HOTKEY",
        "parameters": {
            "keys": args["keys"]
        }
    }
    
    return await _execute_action_unified(action)

# ==================== Control Action Handlers ====================

async def _execute_done(args: dict) -> dict:
    action = {
        "action_type": "DONE"
    }
    
    return await _execute_action_unified(action)

async def _execute_wait(args: dict) -> dict:
    action = {
        "action_type": "WAIT"
    }
    
    return await _execute_action_unified(action)

async def _execute_view_trajectory_step(args: dict) -> dict:
    if "step" not in args or args["step"] is None:
        return {"success": False, "error": "Missing required parameter: step"}
    
    step_num = int(args["step"])
    
    if not env_state.trajectory:
        return {
            "success": False,
            "error": "Trajectory not loaded. Please call osworld_replay_trajectory first."
        }
    
    step_index = step_num - 1 if step_num > 0 else 0
    
    if step_index < 0 or step_index >= len(env_state.trajectory):
        max_step = len(env_state.trajectory)
        return {
            "success": False,
            "error": f"Step {step_num} not found in trajectory (valid range: 1-{max_step})"
        }
    
    step_data = env_state.trajectory[step_index]
    
    observation = {
        "trajectory_step_info": {
            "step": step_num,
            "action": step_data.get("action", {}),
            "timestamp": step_data.get("timestamp", "N/A")
        }
    }
    
    if env_state.replay_result_dir:
        try:
            from pathlib import Path
            import glob
            import base64
            
            replay_dir = Path(env_state.replay_result_dir)
            
            replay_screenshots_dir = replay_dir / "replay_screenshots"
            if replay_screenshots_dir.exists():
                screenshot_pattern = str(replay_screenshots_dir / f"step_{step_num}_*.png")
                matching_files = glob.glob(screenshot_pattern)
                if matching_files:
                    screenshot_path = Path(matching_files[0])
                    with open(screenshot_path, 'rb') as f:
                        screenshot_data = f.read()
                        screenshot_b64 = base64.b64encode(screenshot_data).decode('utf-8')
                        observation["trajectory_screenshot_b64"] = screenshot_b64
                        observation["trajectory_screenshot_file"] = screenshot_path.name
            
            a11y_tree_dir = replay_dir / "a11y_tree"
            if a11y_tree_dir.exists():
                processed_pattern = str(a11y_tree_dir / f"step_{step_num}_*_processed_a11y_tree.json")
                processed_matching_files = glob.glob(processed_pattern)
                if processed_matching_files:
                    processed_a11y_tree_path = Path(processed_matching_files[0])
                    with open(processed_a11y_tree_path, 'r', encoding='utf-8') as f:
                        processed_a11y_tree = json.load(f)
                        observation["trajectory_a11y_tree"] = processed_a11y_tree
        except Exception as e:
            logger.warning(f"Failed to load screenshot/a11y_tree from replay directory: {e}")
    
    formatted_obs = f"Trajectory Step {step_num}:\n"
    formatted_obs += f"Action: {step_data.get('action', 'N/A')}\n"
    
    if "trajectory_screenshot_b64" in observation:
        formatted_obs += f"Screenshot: Available ({observation.get('trajectory_screenshot_file', 'unknown')})\n"
    else:
        formatted_obs += f"Screenshot: Not available in replay directory\n"
    
    if "trajectory_a11y_tree" in observation:
        a11y_tree = observation["trajectory_a11y_tree"]
        a11y_tree_str = str(a11y_tree)
        if len(a11y_tree_str) > 15000:
            formatted_obs += f"Accessibility Tree: {a11y_tree_str[:7500]}...{a11y_tree_str[-7500:]}\n"
        else:
            formatted_obs += f"Accessibility Tree: {a11y_tree}\n"
    else:
        formatted_obs += f"Accessibility Tree: Not available in replay directory\n"
    
    observation["formatted_observation"] = formatted_obs
    
    return {
        "success": True,
        "observation": observation,
        "executed_action": f"VIEW_TRAJECTORY_STEP: step {step_num}"
    }

# ==================== Backward Compatibility Functions ====================

async def _execute_action(args: dict) -> dict:
    if not env_state.initialized or env_state.env is None:
        return {"success": False, "error": "Environment not initialized"}
    
    action_command = args.get("action_command", "")
    
    if not action_command:
        return {"success": False, "error": "Missing required parameter: action_command"}
    
    try:
        env_state.env.step(action_command, pause=1.0)
        
        return {
            "success": True,
            "message": f"Action executed: {action_command}"
        }
    
    except Exception as e:
        logger.error(f"Failed to execute action: {e}")
        return {"success": False, "error": str(e)}

async def _close_environment(args: dict) -> dict:
    try:
        env_state.reset()
        return {"success": True, "message": "Environment closed"}
    except Exception as e:
        logger.error(f"Failed to close environment: {e}")
        return {"success": False, "error": str(e)}

async def _get_status(args: dict) -> dict:
    status = {
        "initialized": env_state.initialized,
        "has_env": env_state.env is not None,
        "has_task_config": env_state.task_config is not None,
        "trajectory_steps": len(env_state.trajectory) if env_state.trajectory else 0
    }
    
    # Add instance ID if available
    if env_state.env is not None and hasattr(env_state.env, "path_to_vm"):
        status["instance_id"] = env_state.env.path_to_vm
        
    return status

# ==================== Start Server ====================
async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler(sys.stderr)],
        force=True
    )
    
    logging.getLogger('boto3').setLevel(logging.WARNING)
    logging.getLogger('botocore').setLevel(logging.WARNING)
    logging.getLogger('urllib3').setLevel(logging.WARNING)
    logging.getLogger('s3transfer').setLevel(logging.WARNING)
    logging.getLogger('boto').setLevel(logging.WARNING)
    logging.getLogger('mcp.server').setLevel(logging.INFO)
    
    logger.info("OSWorld MCP Server starting...")
    logger.info("OSWorld modules are integrated into mcpmark (no external OSWORLD_PATH needed)")
    
    logger.info("Starting OSWorld MCP Server...")
    
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())


