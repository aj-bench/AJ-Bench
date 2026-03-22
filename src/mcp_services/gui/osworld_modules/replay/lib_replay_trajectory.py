import json
import logging
import time
import re
import ast
import xml.etree.ElementTree as ET
import tiktoken
from typing import List, Dict, Any, Optional
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import io

logger = logging.getLogger(__name__)

from ..mm_agents.accessibility_tree_wrap.heuristic_retrieve import filter_nodes
from ..mm_agents.agent import linearize_accessibility_tree, trim_accessibility_tree

# Global counter for tracking consecutive 500/503 errors during replay
_consecutive_a11y_errors = 0
_max_consecutive_a11y_errors = 10  # Maximum allowed consecutive errors before failing

# Global counter for tracking connection refused errors (indicating VM service crash)
_consecutive_connection_refused = 0
_max_consecutive_connection_refused = 3  # Maximum allowed consecutive connection refused errors before terminating VM

def load_trajectory(trajectory_path: str) -> List[Dict[str, Any]]:
    """Load trajectory file."""
    trajectory = []
    with open(trajectory_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                trajectory.append(json.loads(line.strip()))
    return trajectory

def scale_coordinates(action: str, original_screen_size: tuple, target_screen_size: tuple) -> str:
    """
    Scale coordinates in action from original screen size to target screen size.
    
    Args:
        action: String containing pyautogui commands.
        original_screen_size: (width, height) Original screen size.
        target_screen_size: (width, height) Target screen size.
    
    Returns:
        Scaled action string.
    """
    if not action or not isinstance(action, str):
        return action
    
    orig_width, orig_height = original_screen_size
    target_width, target_height = target_screen_size
    
    scale_x = target_width / orig_width
    scale_y = target_height / orig_height
    
    logger.info(f"Coordinate scaling: original({orig_width}x{orig_height}) -> target({target_width}x{target_height})")
    logger.info(f"Scale ratio: X={scale_x:.3f}, Y={scale_y:.3f}")
    
    pattern = r'(pyautogui\.\w+\([^)]*\))'
    matches = re.findall(pattern, action)
    
    scaled_action = action
    
    for match in matches:
        func_name_pattern = r'(pyautogui\.\w+)\((.*)\)'
        func_match = re.match(func_name_pattern, match, re.DOTALL)
        
        if not func_match:
            continue
            
        func_name = func_match.group(1)
        args_str = func_match.group(2)
        
        try:
            parsed = ast.parse(f"func({args_str})").body[0].value
            parsed_args = parsed.args
            parsed_keywords = parsed.keywords
        except SyntaxError:
            continue
        
        function_parameters = {
            'click': ['x', 'y', 'clicks', 'interval', 'button', 'duration', 'pause'],
            'moveTo': ['x', 'y', 'duration', 'tween', 'pause'],
            'moveRel': ['xOffset', 'yOffset', 'duration', 'tween', 'pause'],
            'dragTo': ['x', 'y', 'duration', 'button', 'mouseDownUp', 'pause'],
            'dragRel': ['xOffset', 'yOffset', 'duration', 'button', 'mouseDownUp', 'pause'],
            'doubleClick': ['x', 'y', 'interval', 'button', 'duration', 'pause'],
            'rightClick': ['x', 'y', 'duration', 'pause'],
            'middleClick': ['x', 'y', 'duration', 'pause'],
        }
        
        func_base_name = func_name.split('.')[-1]
        param_names = function_parameters.get(func_base_name, [])
        
        args = {}
        for idx, arg in enumerate(parsed_args):
            if idx < len(param_names):
                param_name = param_names[idx]
                try:
                    arg_value = ast.literal_eval(arg)
                    args[param_name] = arg_value
                except (ValueError, SyntaxError):
                    continue
        
        for kw in parsed_keywords:
            param_name = kw.arg
            try:
                arg_value = ast.literal_eval(kw.value)
                args[param_name] = arg_value
            except (ValueError, SyntaxError):
                continue
        
        scaled_args = args.copy()
        if 'x' in args and isinstance(args['x'], (int, float)):
            scaled_args['x'] = int(round(args['x'] * scale_x))
            logger.debug(f"Scale X coordinate: {args['x']} -> {scaled_args['x']}")
        
        if 'y' in args and isinstance(args['y'], (int, float)):
            scaled_args['y'] = int(round(args['y'] * scale_y))
            logger.debug(f"Scale Y coordinate: {args['y']} -> {scaled_args['y']}")
        
        new_args = []
        for param_name in param_names:
            if param_name in scaled_args:
                new_args.append(f"{param_name}={scaled_args[param_name]}")
        
        new_func_call = f"{func_name}({', '.join(new_args)})"
        scaled_action = scaled_action.replace(match, new_func_call)
    
    return scaled_action

def _wait_for_vnc_ready(env, timeout: int = 60) -> bool:
    """Wait for VNC and desktop_env services to be ready."""
    import requests
    
    logger.info("Waiting for VNC and desktop_env services to be ready...")
    
    vnc_info = _get_vnc_info(env)
    if vnc_info:
        vnc_url, public_ip = vnc_info
        logger.info(f"🌐 VNC access URL: {vnc_url}")
        logger.info(f"📍 Public IP: {public_ip}")
    
    logger.info("✅ desktop_env service is ready (verified during setup phase)")
    return True

def _get_vnc_info(env) -> Optional[tuple]:
    """Get VNC access information."""
    try:
        if hasattr(env, 'provider') and hasattr(env.provider, 'get_vnc_info'):
            return env.provider.get_vnc_info()
        elif hasattr(env, 'vm_ip'):
            public_ip = getattr(env, 'public_ip', env.vm_ip)
            vnc_url = f"http://{public_ip}:5910"
            return (vnc_url, public_ip)
    except Exception as e:
        logger.warning(f"Failed to get VNC info: {e}")
    
    return None

def _save_step_screenshot(env, step_num: int, action_timestamp: str, 
                         result_dir: Optional[str] = None, 
                         action: str = None, debug_mode: bool = False) -> Optional[str]:
    """Save step screenshot."""
    if not result_dir:
        return None
    
    result_path = Path(result_dir)
    result_path.mkdir(parents=True, exist_ok=True)
    
    for attempt in range(3):
        try:
            screenshot = env.render(mode='rgb_array')
            if screenshot is not None:
                screenshot_file = f"step_{step_num}_{action_timestamp}.png"
                screenshot_path = result_path / screenshot_file
                
                if isinstance(screenshot, (bytes, bytearray)):
                    screenshot_data = screenshot
                elif hasattr(screenshot, 'save'):
                    screenshot.save(screenshot_path)
                    logger.info(f"📸 Screenshot saved: {screenshot_path}")
                    return str(screenshot_path)
                else:
                    import numpy as np
                    if isinstance(screenshot, np.ndarray):
                        image = Image.fromarray(screenshot)
                        screenshot_data = None
                    else:
                        screenshot_array = np.asarray(screenshot)
                        image = Image.fromarray(screenshot_array)
                        screenshot_data = None
                
                if debug_mode and action and screenshot_data is None:
                    coordinates = _extract_coordinates_from_action(action)
                    if coordinates:
                        logger.info(f"🔍 Debug mode: coordinates {coordinates} (annotation feature needs further implementation)")
                
                if screenshot_data is not None:
                    with open(screenshot_path, 'wb') as f:
                        f.write(screenshot_data)
                else:
                    image.save(screenshot_path)
                
                logger.info(f"📸 Screenshot saved: {screenshot_path}")
                return str(screenshot_path)
        except Exception as e:
            logger.warning(f"Screenshot attempt {attempt + 1}/3 failed: {e}")
            if attempt < 2:
                time.sleep(2)
    
    error_file = result_path / f"step_{step_num}_{action_timestamp}_screenshot_error.txt"
    with open(error_file, 'w') as f:
        f.write(f"Screenshot failed for step {step_num} at {action_timestamp}\n")
    
    logger.error(f"❌ Screenshot failed, error file created: {error_file}")
    return None

def _save_screenshot(env, filename: str, result_dir: Optional[str] = None) -> Optional[str]:
    """
    Save screenshot (general function for saving screenshots before/after replay).
    
    Args:
        env: Environment instance.
        filename: Filename (without extension).
        result_dir: Save directory.
        
    Returns:
        Saved file path, or None on failure.
    """
    if not result_dir:
        return None
    
    result_path = Path(result_dir)
    result_path.mkdir(parents=True, exist_ok=True)
    
    screenshot_path = result_path / f"{filename}.png"
    
    for attempt in range(3):
        try:
            screenshot = env.render(mode='rgb_array')
            if screenshot is not None:
                if isinstance(screenshot, (bytes, bytearray)):
                    with open(screenshot_path, 'wb') as f:
                        f.write(screenshot)
                elif hasattr(screenshot, 'save'):
                    screenshot.save(screenshot_path)
                else:
                    import numpy as np
                    if isinstance(screenshot, np.ndarray):
                        image = Image.fromarray(screenshot)
                    else:
                        screenshot_array = np.asarray(screenshot)
                        image = Image.fromarray(screenshot_array)
                    image.save(screenshot_path)
                
                logger.info(f"📸 Screenshot saved: {screenshot_path}")
                return str(screenshot_path)
        except Exception as e:
            logger.warning(f"Screenshot attempt {attempt + 1}/3 failed: {e}")
            if attempt < 2:
                time.sleep(2)
    
    logger.error(f"❌ Screenshot failed: {screenshot_path}")
    return None

def _annotate_screenshot_with_coordinates(screenshot_bytes: bytes, coordinates: List[tuple], 
                                        action_type: str = "click") -> bytes:
    """
    Annotate coordinates on screenshot.
    
    Args:
        screenshot_bytes: Original screenshot byte data.
        coordinates: Coordinate list [(x, y), ...].
        action_type: Action type (click, moveTo, etc.).
    
    Returns:
        Annotated screenshot byte data.
    """
    try:
        image = Image.open(io.BytesIO(screenshot_bytes))
        draw = ImageDraw.Draw(image)
        
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
        except:
            font = ImageFont.load_default()
        
        for i, (x, y) in enumerate(coordinates):
            circle_radius = 25
            draw.ellipse([(x-circle_radius, y-circle_radius), 
                         (x+circle_radius, y+circle_radius)], 
                        outline="red", width=5)
            
            inner_radius = 15
            draw.ellipse([(x-inner_radius, y-inner_radius), 
                         (x+inner_radius, y+inner_radius)], 
                        outline="yellow", width=3)
            
            cross_size = 30
            draw.line([(x-cross_size, y), (x+cross_size, y)], fill="red", width=5)
            draw.line([(x, y-cross_size), (x, y+cross_size)], fill="red", width=5)
            
            center_size = 8
            draw.ellipse([(x-center_size, y-center_size), 
                         (x+center_size, y+center_size)], 
                        fill="red")
            
            text = f"{action_type}({x},{y})"
            text_bbox = draw.textbbox((0, 0), text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            
            text_x = x + 35
            text_y = y - text_height - 10
            draw.rectangle([(text_x-5, text_y-5), (text_x+text_width+5, text_y+text_height+5)], 
                          fill="yellow", outline="red", width=2)
            draw.text((text_x, text_y), text, fill="black", font=font)
            
            if len(coordinates) > 1:
                num_text = str(i+1)
                num_bbox = draw.textbbox((0, 0), num_text, font=font)
                num_width = num_bbox[2] - num_bbox[0]
                num_height = num_bbox[3] - num_bbox[1]
                
                num_x = x - num_width // 2
                num_y = y - num_height // 2
                draw.rectangle([(num_x-3, num_y-3), (num_x+num_width+3, num_y+num_height+3)], 
                              fill="white", outline="red", width=2)
                draw.text((num_x, num_y), num_text, fill="red", font=font)
        
        output = io.BytesIO()
        image.save(output, format='PNG')
        return output.getvalue()
        
    except Exception as e:
        logger.warning(f"Coordinate annotation failed: {e}")
        return screenshot_bytes

def _extract_coordinates_from_action(action: str) -> List[tuple]:
    """
    Extract coordinates from action string.
    
    Args:
        action: Action string.
    
    Returns:
        Coordinate list [(x, y), ...].
    """
    coordinates = []
    
    patterns = [
        r'pyautogui\.\w+\([^)]*x=(\d+)[^)]*y=(\d+)[^)]*\)',
        r'pyautogui\.\w+\((\d+),\s*(\d+)\)',
        r'pyautogui\.\w+\((\d+),\s*(\d+),',
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, action)
        for match in matches:
            try:
                x, y = int(match[0]), int(match[1])
                coordinates.append((x, y))
            except (ValueError, IndexError):
                continue
    
    return coordinates

def _perform_initial_click_in_replay(env, task_config: Dict[str, Any], target_screen_size: Optional[tuple], debug_mode: bool = False):
    """
    Automatically detect and close initialization popups during replay.
    
    Uses accessibility tree to automatically detect infobars and close all detected infobars.
    Replaces the previous fixed coordinate clicking approach.
    
    Args:
        env: Environment instance.
        task_config: Task configuration.
        target_screen_size: Target screen size.
        debug_mode: Debug mode.
    """
    try:
        try:
            from .infobar_detector import InfobarDetector
        except ImportError:
            logger.error("❌ Failed to import InfobarDetector from replay.infobar_detector, skipping automatic infobar closing")
            return
        
        try:
            from replay.click_coordinates import click_coordinates
        except ImportError:
            try:
                from click_coordinates import click_coordinates
            except ImportError:
                from mcp_services.gui.osworld_modules.replay.click_coordinates import click_coordinates
        
        app_type = click_coordinates.detect_app_type_from_config(task_config)
        
        screen_width = target_screen_size[0] if target_screen_size else 1920
        screen_height = target_screen_size[1] if target_screen_size else 1080
        
        infobar_detector = InfobarDetector(
            screen_width=screen_width,
            screen_height=screen_height,
            app_type=app_type
        )
        
        extra_wait = 5
        logger.info(f"Waiting {extra_wait} seconds to ensure popup fully appears...")
        time.sleep(extra_wait)
        
        logger.info(f"Starting automatic infobar detection and closing - Application: {app_type}")
        
        max_attempts = 10
        closed_count = 0
        
        for attempt in range(1, max_attempts + 1):
            a11y_tree = None
            try:
                if hasattr(env, 'controller') and hasattr(env.controller, 'get_accessibility_tree'):
                    a11y_tree = env.controller.get_accessibility_tree()
                elif hasattr(env, 'get_accessibility_tree'):
                    a11y_tree = env.get_accessibility_tree()
            except Exception as e:
                logger.warning(f"Failed to get accessibility tree: {e}")
                break
            
            if a11y_tree is None:
                logger.warning("Unable to get accessibility tree, skipping infobar detection")
                break
            
            if not infobar_detector.has_infobars(a11y_tree):
                logger.info(f"✅ No infobars detected (attempt {attempt})")
                break
            
            close_coord = infobar_detector.get_topmost_infobar_close_coord(a11y_tree)
            
            if close_coord is None:
                logger.warning("Infobar detected but unable to calculate close button coordinates")
                break
            
            x, y = close_coord
            logger.info(f"Attempt {attempt}/{max_attempts}: Infobar detected, close button coordinates: ({x}, {y})")
            
            try:
                click_action = f"pyautogui.click({x}, {y})"
                env.controller.execute_python_command(click_action)
                time.sleep(1.5)
                closed_count += 1
                logger.info(f"✅ Successfully closed infobar #{closed_count}")
                
                time.sleep(1)
                
            except Exception as e:
                logger.error(f"Failed to close infobar: {e}")
                break
        
        if closed_count > 0:
            logger.info(f"✅ Successfully closed {closed_count} infobars in total")
        else:
            logger.info("No infobars detected that need closing")
                
    except Exception as e:
        logger.error(f"Automatic infobar closing failed: {e}")
        import traceback
        logger.debug(f"Error details: {traceback.format_exc()}")

def replay_trajectory(env, trajectory: List[Dict[str, Any]],
                     sleep_after_execution: float = 0.3,
                     save_replay_results: bool = True,
                     replay_result_dir: Optional[str] = None,
                     wait_for_vnc: bool = True,
                     vnc_wait_timeout: int = 30,
                     task_config: Optional[Dict[str, Any]] = None,
                     original_screen_size: Optional[tuple] = None,
                     target_screen_size: Optional[tuple] = None,
                     debug_mode: bool = False,
                     enable_click: bool = False,
                     save_screenshots: bool = False) -> Dict[str, Any]:
    """
    Replay trajectory with a11y_tree error detection and retry mechanism.
    
    Args:
        env: DesktopEnv instance.
        trajectory: Trajectory data list.
        sleep_after_execution: Wait time after execution.
        save_replay_results: Whether to save replay results.
        replay_result_dir: Replay result save directory.
        wait_for_vnc: Whether to wait for VNC to be ready.
        vnc_wait_timeout: VNC wait timeout.
        task_config: Task configuration.
        original_screen_size: Original screen size (width, height).
        target_screen_size: Target screen size (width, height).
        debug_mode: Debug mode.
        enable_click: Whether to enable click functionality.
        save_screenshots: Whether to save screenshots for each step.
    """
    global _consecutive_a11y_errors
    _consecutive_a11y_errors = 0
    logger.info(f"Starting trajectory replay with {len(trajectory)} steps")

    logger.info("📋 Environment initialized, skipping reset, starting replay directly")

    if wait_for_vnc:
        if not _wait_for_vnc_ready(env, vnc_wait_timeout):
            raise RuntimeError("VNC and desktop_env services did not become ready within the specified time")
    
    if not _wait_for_accessibility_ready(env, vnc_wait_timeout):
        logger.warning("⚠️ Accessibility service not ready, will skip a11y_tree saving")
    
    if enable_click and task_config:
        logger.info("Environment fully ready, executing initial click...")
        _perform_initial_click_in_replay(env, task_config, target_screen_size, debug_mode)
    
    if replay_result_dir:
        screenshots_dir = Path(replay_result_dir) / "replay_screenshots"
        screenshots_dir.mkdir(parents=True, exist_ok=True)
        logger.info("Saving initial state screenshot before replay...")
        try:
            before_replay_path = _save_screenshot(env, "before_replay", str(screenshots_dir))
            if before_replay_path:
                logger.info(f"✅ Screenshot before replay saved: {before_replay_path}")
            else:
                logger.warning("⚠️ Failed to save screenshot before replay")
        except Exception as e:
            logger.error(f"❌ Error saving screenshot before replay: {e}")
            import traceback
            logger.debug(f"Error details: {traceback.format_exc()}")

    results = {
        "total_steps": len(trajectory),
        "successful_steps": 0,
        "failed_steps": 0,
        "screenshots": [],
        "errors": [],
        "replay_actions": [],
        "action_differences": [],
        "step_timings": []
    }

    for i, step in enumerate(trajectory):
        step_num = step.get("step_num", i + 1)
        action_timestamp = step.get("action_timestamp", f"step_{step_num}")
        original_action = step.get("action", "")
        
        step_start_time = time.time()
        
        task_id = task_config.get('id', 'unknown') if task_config else 'unknown'
        logger.info(f"[Task ID: {task_id}] Executing step {step_num}/{len(trajectory)}: {action_timestamp}")
        
        if debug_mode:
            logger.info("=" * 80)
            logger.info(f"🔍 Debug info - Step {step_num}")
            logger.info("=" * 80)
            logger.info(f"📝 Original action:")
            logger.info(f"   {original_action}")
            logger.info("-" * 40)
        
        try:
            action = original_action
            action_modified = False
            
            if original_screen_size and target_screen_size and original_screen_size != target_screen_size:
                logger.info(f"Applying coordinate scaling: {original_screen_size} -> {target_screen_size}")
                action = scale_coordinates(action, original_screen_size, target_screen_size)
                action_modified = True
                
                if debug_mode:
                    logger.info(f"🔄 Scaled action:")
                    logger.info(f"   {action}")
                    logger.info("-" * 40)
            
            if debug_mode:
                logger.info(f"⚡ Action to execute:")
                logger.info(f"   {action}")
                logger.info("=" * 80)
            
            vm_check_result = _check_vm_service_health(env)
            if not vm_check_result:
                global _consecutive_connection_refused, _max_consecutive_connection_refused
                _consecutive_connection_refused += 1
                logger.error(f"❌ VM service unavailable before execution (consecutive count: {_consecutive_connection_refused})")
                
                if _consecutive_connection_refused >= _max_consecutive_connection_refused:
                    error_msg = f"🔥 VM service unavailable {_consecutive_connection_refused} consecutive times, VM service crashed, need to terminate VM and retry"
                    logger.error(error_msg)
                    raise RuntimeError(error_msg)
            
            env.step(action, pause=sleep_after_execution)
            results["successful_steps"] += 1
            _consecutive_connection_refused = 0
            
            step_end_time = time.time()
            step_duration = step_end_time - step_start_time
            
            results["replay_actions"].append({
                "step_num": step_num,
                "action_timestamp": action_timestamp,
                "original_action": original_action,
                "executed_action": action,
                "action_modified": action_modified,
                "execution_time": round(step_duration, 3),
                "success": True
            })
            
            if action_modified and original_action != action:
                results["action_differences"].append({
                    "step_num": step_num,
                    "original_action": original_action,
                    "executed_action": action,
                    "modification_type": "coordinate_scaling"
                })
            
            results["step_timings"].append({
                "step_num": step_num,
                "start_time": step_start_time,
                "end_time": step_end_time,
                "duration": round(step_duration, 3)
            })
            
            if save_replay_results and replay_result_dir:
                if save_screenshots:
                    screenshots_dir = Path(replay_result_dir) / "replay_screenshots"
                    screenshots_dir.mkdir(parents=True, exist_ok=True)
                    screenshot_path = _save_step_screenshot(env, step_num, action_timestamp, 
                                                          str(screenshots_dir), action, debug_mode)
                    if screenshot_path:
                        results["screenshots"].append(screenshot_path)
                
                if not save_screenshots or True:
                    a11y_tree_path = _save_step_a11y_tree(env, step_num, action_timestamp, replay_result_dir)
                    if a11y_tree_path:
                        results.setdefault("a11y_trees", []).append(a11y_tree_path)
            
            task_id = task_config.get('id', 'unknown') if task_config else 'unknown'
            logger.info(f"✅ [Task ID: {task_id}] Step {step_num} executed successfully (duration: {step_duration:.3f}s)")
            
        except Exception as e:
            step_end_time = time.time()
            step_duration = step_end_time - step_start_time
            
            task_id = task_config.get('id', 'unknown') if task_config else 'unknown'
            logger.error(f"❌ [Task ID: {task_id}] Step {step_num} execution failed: {e}")
            results["failed_steps"] += 1
            
            results["replay_actions"].append({
                "step_num": step_num,
                "action_timestamp": action_timestamp,
                "original_action": original_action,
                "executed_action": action if 'action' in locals() else None,
                "action_modified": action_modified if 'action_modified' in locals() else False,
                "execution_time": round(step_duration, 3),
                "success": False,
                "error": str(e)
            })
            
            results["step_timings"].append({
                "step_num": step_num,
                "start_time": step_start_time,
                "end_time": step_end_time,
                "duration": round(step_duration, 3),
                "success": False
            })
            
            results["errors"].append({
                "step": step_num,
                "error": str(e),
                "original_action": original_action,
                "executed_action": action if 'action' in locals() else None,
                "execution_time": round(step_duration, 3)
            })
    
    logger.info(f"Trajectory replay completed: {results['successful_steps']}/{results['total_steps']} steps successful")
    
    if replay_result_dir:
        screenshots_dir = Path(replay_result_dir) / "replay_screenshots"
        screenshots_dir.mkdir(parents=True, exist_ok=True)
        logger.info("Saving final screenshot after replay...")
        try:
            after_replay_path = _save_screenshot(env, "after_replay", str(screenshots_dir))
            if after_replay_path:
                logger.info(f"✅ Screenshot after replay saved: {after_replay_path}")
                results.setdefault("final_screenshot", after_replay_path)
            else:
                logger.warning("⚠️ Failed to save screenshot after replay")
        except Exception as e:
            logger.error(f"❌ Error saving screenshot after replay: {e}")
            import traceback
            logger.debug(f"Error details: {traceback.format_exc()}")
    
    success_rate = results['successful_steps'] / results['total_steps'] if results['total_steps'] > 0 else 0
    results['final_result'] = success_rate
    
    return results


def _check_vm_service_health(env) -> bool:
    """
    Check VM service health status.
    Determines if service is normal by attempting to access VM's HTTP service.
    
    Returns:
        True if service is healthy, False otherwise.
    """
    if not hasattr(env, "controller") or not hasattr(env.controller, "http_server"):
        return True
    
    try:
        import requests
        http_server = env.controller.http_server
        response = requests.get(http_server + "/terminal", timeout=2)
        return response.status_code == 200
    except requests.exceptions.ConnectionError as e:
        error_msg = str(e)
        if "Connection refused" in error_msg or "[Errno 111]" in error_msg:
            logger.error("VM service health check failed: Connection Refused")
            return False
        return True
    except requests.exceptions.Timeout:
        logger.warning("VM service health check timeout")
        return True
    except Exception as e:
        logger.debug(f"VM service health check exception: {e}")
        return True

def _get_a11y_tree_with_error_detection(env) -> tuple:
    """
    Get a11y_tree and detect HTTP error codes.
    
    Returns:
        (raw_a11y_tree, error_code, success)
        raw_a11y_tree: Returns tree on success, None on failure.
        error_code: HTTP error code (e.g., 500, 503) or 'CONNECTION_REFUSED', None if no error.
        success: Whether retrieval was successful.
    """
    global _consecutive_a11y_errors, _consecutive_connection_refused
    
    if hasattr(env, "controller") and hasattr(env.controller, "get_accessibility_tree"):
        try:
            import requests
            if hasattr(env.controller, "http_server"):
                http_server = env.controller.http_server
                try:
                    response = requests.get(http_server + "/accessibility", timeout=15)
                    if response.status_code == 200:
                        _consecutive_a11y_errors = 0
                        _consecutive_connection_refused = 0
                        try:
                            return (response.json()["AT"], None, True)
                        except:
                            return (None, None, False)
                    elif response.status_code in [500, 503]:
                        _consecutive_a11y_errors += 1
                        logger.error(f"Failed to get a11y_tree, HTTP error code: {response.status_code} (consecutive errors: {_consecutive_a11y_errors})")
                        return (None, response.status_code, False)
                    else:
                        logger.warning(f"Failed to get a11y_tree, HTTP error code: {response.status_code}")
                        return (None, response.status_code, False)
                except requests.exceptions.Timeout:
                    logger.warning("Getting a11y_tree timeout (>15s)")
                    return (None, None, False)
                except requests.exceptions.ConnectionError as e:
                    error_msg = str(e)
                    if "Connection refused" in error_msg or "[Errno 111]" in error_msg:
                        _consecutive_connection_refused += 1
                        logger.error(f"❌ VM service connection refused (Connection Refused) - service may have crashed (consecutive count: {_consecutive_connection_refused})")
                        return (None, "CONNECTION_REFUSED", False)
                    else:
                        logger.warning(f"HTTP connection error: {e}")
                        return (None, None, False)
                except Exception as e:
                    logger.warning(f"HTTP request failed: {e}")
        except:
            pass
        
        import threading
        result = {"v": None, "error": None}
        def _worker():
            try:
                result["v"] = env.controller.get_accessibility_tree()
            except Exception as e:
                result["error"] = e
        t = threading.Thread(target=_worker, daemon=True)
        t.start()
        t.join(timeout=15)
        if t.is_alive():
            logger.warning("Getting a11y_tree timeout (>15s)")
            return (None, None, False)
        if result["v"] is not None:
            _consecutive_a11y_errors = 0
            return (result["v"], None, True)
        else:
            return (None, None, False)
    elif hasattr(env, "get_accessibility_tree"):
        try:
            tree = env.get_accessibility_tree()
            if tree is not None:
                _consecutive_a11y_errors = 0
                return (tree, None, True)
            else:
                return (None, None, False)
        except Exception as e:
            logger.warning(f"Exception getting a11y_tree: {e}")
            return (None, None, False)
    
    return (None, None, False)


def _save_step_a11y_tree(env, step_num: int, action_timestamp: str, 
                        result_dir: Optional[str] = None) -> Optional[str]:
    """
    Save step a11y_tree and process it (filter, linearize, truncate).
    Detects HTTP 500/503 errors and Connection Refused errors, raises exception if consecutive failures exceed threshold.
    """
    global _consecutive_a11y_errors, _max_consecutive_a11y_errors
    global _consecutive_connection_refused, _max_consecutive_connection_refused
    
    if not result_dir:
        return None
    
    result_path = Path(result_dir)
    a11y_tree_dir = result_path / "a11y_tree"
    a11y_tree_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        raw_a11y_tree, error_code, success = _get_a11y_tree_with_error_detection(env)
        
        if error_code == "CONNECTION_REFUSED" and _consecutive_connection_refused >= _max_consecutive_connection_refused:
            error_msg = f"🔥 VM service connection refused {_consecutive_connection_refused} consecutive times (Connection Refused), VM service crashed, need to terminate VM and retry"
            logger.error(error_msg)
            raise RuntimeError(error_msg)
        
        if error_code in [500, 503] and _consecutive_a11y_errors >= _max_consecutive_a11y_errors:
            error_msg = f"Failed to get a11y_tree {_consecutive_a11y_errors} consecutive times (HTTP {error_code}), reached max retry count, replay failed"
            logger.error(error_msg)
            _consecutive_a11y_errors = 0
            raise RuntimeError(error_msg)
        
        if raw_a11y_tree is not None:
            linearized_tree = linearize_accessibility_tree(raw_a11y_tree, platform="ubuntu")
            logger.info(f"🔄 Linearization completed, length: {len(linearized_tree)} characters")
            
            max_tokens = 10000
            processed_tree = trim_accessibility_tree(linearized_tree, max_tokens)
            logger.info(f"✂️ Truncation completed, final length: {len(processed_tree)} characters")
            
            processed_a11y_tree_file = f"step_{step_num}_{action_timestamp}_processed_a11y_tree.json"
            processed_a11y_tree_path = a11y_tree_dir / processed_a11y_tree_file
            
            max_save_retries = 3
            for save_attempt in range(max_save_retries):
                try:
                    with open(processed_a11y_tree_path, 'w', encoding='utf-8') as f:
                        json.dump(processed_tree, f, ensure_ascii=False, indent=2)
                    logger.info(f"📋 Saved processed a11y_tree (JSON): {processed_a11y_tree_path}")
                    return str(processed_a11y_tree_path)
                except Exception as save_err:
                    logger.warning(f"⚠️ a11y_tree save failed (attempt {save_attempt + 1}/{max_save_retries}): {save_err}")
                    if save_attempt < max_save_retries - 1:
                        time.sleep(1)
            logger.error(f"🚨 a11y_tree save failed after {max_save_retries} attempts, requeue task")
            raise RuntimeError("A11Y_TREE_SAVE_FAILED_REQUEUE")
        else:
            logger.warning(f"⚠️ Unable to get a11y_tree for step {step_num}")
            return None
            
    except RuntimeError as e:
        if "A11Y_TREE_SAVE_FAILED_REQUEUE" in str(e):
            raise
        logger.warning(f"⚠️ Failed to save a11y_tree: {e}")
        return None
    except Exception as e:
        logger.warning(f"⚠️ Failed to save a11y_tree: {e}")
        return None


def _wait_for_accessibility_ready(env, timeout: int = 30) -> bool:
    """Wait for accessibility service to be ready, avoiding concurrent access conflicts."""
    logger.info("Waiting for accessibility service to be ready...")
    
    start_time = time.time()
    max_attempts = timeout // 3
    
    for attempt in range(max_attempts):
        try:
            if hasattr(env, "controller") and hasattr(env.controller, "get_accessibility_tree"):
                import threading
                result = {"v": None}
                def _worker():
                    try:
                        result["v"] = env.controller.get_accessibility_tree()
                    except Exception:
                        result["v"] = None
                t = threading.Thread(target=_worker, daemon=True)
                t.start()
                t.join(timeout=10)
                a11y_tree = result["v"] if not t.is_alive() else None
                if t.is_alive():
                    logger.info(f"⏳ Accessibility check timeout, waiting 3 seconds before retry... ({attempt + 1}/{max_attempts})")
                elif a11y_tree is not None:
                    logger.info(f"✅ Accessibility service ready (took {time.time() - start_time:.1f}s)")
                    return True
                else:
                    logger.info(f"⏳ Accessibility service not ready, waiting 3 seconds before retry... ({attempt + 1}/{max_attempts})")
            else:
                logger.warning("⚠️ Environment does not support accessibility tree")
                return False
                
        except Exception as e:
            logger.debug(f"Accessibility service check failed: {e}")
            
        time.sleep(3)
    
    logger.warning(f"⚠️ Accessibility service did not become ready within {timeout}s")
    return False