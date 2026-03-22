"""
OSWorld MCP Client
"""

import os
import sys
import json
import logging
import subprocess
import asyncio
import threading
from typing import Any, Dict, Optional, List
from pathlib import Path
from contextlib import AsyncExitStack

try:
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client
    MCP_SDK_AVAILABLE = True
except ImportError:
    MCP_SDK_AVAILABLE = False
    logger = logging.getLogger(__name__)
    logger.warning("MCP SDK not available, using fallback implementation")

logger = logging.getLogger(__name__)

class GUIMCPClient:
    """
    OSWorld MCP Client - communicates with OSWorld MCP Server via the MCP protocol.
    Provides an interface similar to the original DesktopEnv and can be used as a drop-in replacement.
    """
    
    def __init__(self, server_script: Optional[str] = None):
        self.initialized = False
        self._async_stack: Optional[AsyncExitStack] = None
        self._session: Optional[Any] = None
        self._loop: Optional[asyncio.AbstractEventLoop] = None
        self._stderr_thread: Optional[threading.Thread] = None
        self._stop_stderr_thread = False
        self.instance_id: Optional[str] = None
        
        if server_script is None:
            current_dir = Path(__file__).parent
            server_script = str(current_dir / "gui_mcp_server.py")
        
        self.server_script = server_script
        
        server_path = Path(self.server_script)
        if not server_path.exists():
            current_dir = Path(__file__).parent
            expected_path = current_dir / "gui_mcp_server.py"
            raise FileNotFoundError(
                f"MCP Server script not found: {self.server_script}\n"
                f"Expected location: {expected_path}\n"
                f"Current file location: {__file__}\n"
                f"Current directory: {current_dir}\n"
                f"Files in current directory: {list(current_dir.iterdir()) if current_dir.exists() else 'N/A'}"
            )
        
        if not os.access(self.server_script, os.R_OK):
            raise PermissionError(f"MCP Server script is not readable: {self.server_script}")
        
        logger.debug(f"MCP Server script verified: {self.server_script}")
        
        self.use_sdk = MCP_SDK_AVAILABLE
        
        if not self.use_sdk:
            self.server_process: Optional[subprocess.Popen] = None
        
        logger.info(f"OSWorld MCP Client initialized with server: {self.server_script}")
        logger.info(f"Using MCP SDK: {self.use_sdk}")
    
    def _forward_stderr_logs(self):
        """Forward MCP Server stderr logs to the main process logging system."""
        if self.server_process is None or self.server_process.stderr is None:
            return
        
        try:
            for line in iter(self.server_process.stderr.readline, ''):
                if self._stop_stderr_thread:
                    break
                if line:
                    # Strip trailing newline characters and forward logs
                    line = line.rstrip('\n\r')
                    if line:
                        # Write directly to stderr so we can see real-time logs
                        print(line, file=sys.stderr, flush=True)
        except Exception as e:
            logger.debug(f"Stderr forwarding thread error: {e}")
    
    def start_server(self):
        """Start the MCP Server process."""
        if self.use_sdk and MCP_SDK_AVAILABLE:
            # Use MCP SDK
            try:
                logger.info(f"Starting MCP Server via SDK: {self.server_script}")
                
                # Check whether the server script exists
                if not Path(self.server_script).exists():
                    raise FileNotFoundError(f"MCP Server script not found: {self.server_script}")
                
                # Create a new event loop
                logger.info("Creating new event loop for MCP Client (multi-process safe)")
                
                # Ensure there is no existing event loop
                try:
                    existing_loop = asyncio.get_event_loop()
                    if not existing_loop.is_closed():
                        logger.warning("Existing event loop found, closing it first...")
                        existing_loop.close()
                except RuntimeError:
                    # No existing event loop; this is expected
                    pass
                
                # Create a new event loop
                self._loop = asyncio.new_event_loop()
                asyncio.set_event_loop(self._loop)
                logger.debug("New event loop created and set")
                
                # Start MCP client
                self._async_stack = AsyncExitStack()
                
                env = os.environ.copy()
                server_script_path = Path(self.server_script)
                mcpmark_root = server_script_path.parent.parent.parent.parent
                mcpmark_src = mcpmark_root / "src"
                
                # Update PYTHONPATH
                pythonpath = env.get("PYTHONPATH", "")
                if pythonpath:
                    pythonpath = f"{str(mcpmark_src)}:{pythonpath}"
                else:
                    pythonpath = str(mcpmark_src)
                env["PYTHONPATH"] = pythonpath
                
                logger.debug(f"Setting PYTHONPATH for MCP Server: {pythonpath}")
                logger.debug(f"MCP Server script: {self.server_script}")
                logger.debug(f"MCP root: {mcpmark_root}")
                
                params = StdioServerParameters(
                    command=sys.executable,
                    args=[self.server_script],
                    env=env
                )
                
                logger.info(f"MCP Server parameters: command={sys.executable}, args={self.server_script}")
                logger.info("Step 1: Entering stdio_client context (this will start the server process)...")
                
                # Run async initialization with detailed error handling
                try:
                    read, write = self._loop.run_until_complete(
                        asyncio.wait_for(
                            self._async_stack.enter_async_context(stdio_client(params)),
                            timeout=30
                        )
                    )
                    logger.info("✅ Step 1 completed: stdio_client context entered")
                except asyncio.TimeoutError:
                    error_msg = "MCP Server process failed to start within 30 seconds"
                    logger.error(error_msg)
                    raise RuntimeError(error_msg)
                
                logger.info("Step 2: Creating ClientSession...")
                try:
                    self._session = self._loop.run_until_complete(
                        asyncio.wait_for(
                            self._async_stack.enter_async_context(ClientSession(read, write)),
                            timeout=10
                        )
                    )
                    logger.info("✅ Step 2 completed: ClientSession created")
                except asyncio.TimeoutError:
                    error_msg = "ClientSession creation timed out after 10 seconds"
                    logger.error(error_msg)
                    # Clean up already-created resources
                    try:
                        if self._async_stack:
                            self._loop.run_until_complete(self._async_stack.aclose())
                    except Exception:
                        pass
                    raise RuntimeError(error_msg)
                
                logger.info("Step 3: Initializing MCP session (this may take a while)...")
                try:
                    # Increase timeout to 120 seconds
                    self._loop.run_until_complete(
                        asyncio.wait_for(self._session.initialize(), timeout=120)
                    )
                    logger.info("✅ Step 3 completed: MCP session initialized")
                except asyncio.TimeoutError:
                    error_msg = "MCP Server initialization timed out after 120 seconds"
                    logger.error(error_msg)
                    logger.error("This may indicate that the MCP Server process is stuck or taking too long to initialize")
                    # Clean up resources
                    try:
                        if self._async_stack:
                            # Clean up in the same event loop
                            self._loop.run_until_complete(self._async_stack.aclose())
                    except Exception as cleanup_e:
                        logger.warning(f"Error during cleanup after timeout: {cleanup_e}")
                    raise RuntimeError(error_msg)
                
                logger.info("✅ MCP Server started and initialized via SDK")
            except asyncio.TimeoutError:
                # This exception should already be handled above, but keep it for safety
                error_msg = "MCP Server initialization timed out"
                logger.error(error_msg)
                raise RuntimeError(error_msg)
            except FileNotFoundError as e:
                error_msg = f"MCP Server script not found: {e}"
                logger.error(error_msg)
                raise
            except RuntimeError:
                # Re-raise RuntimeError (including timeout errors)
                raise
            except Exception as e:
                error_msg = f"Failed to start MCP Server via SDK: {e}"
                logger.error(error_msg)
                import traceback
                logger.error(f"Traceback: {traceback.format_exc()}")
                # Clean up resources
                try:
                    if hasattr(self, '_async_stack') and self._async_stack:
                        if hasattr(self, '_loop') and self._loop and not self._loop.is_closed():
                            self._loop.run_until_complete(self._async_stack.aclose())
                except Exception as cleanup_e:
                    logger.warning(f"Error during cleanup: {cleanup_e}")
                raise RuntimeError(error_msg) from e
        else:
            # Fallback: use subprocess
            if self.server_process is not None:
                logger.warning("MCP Server already running")
                return
            
            try:
                logger.info(f"Starting MCP Server via subprocess: {self.server_script}")
                
                # Check whether the server script exists
                if not Path(self.server_script).exists():
                    raise FileNotFoundError(f"MCP Server script not found: {self.server_script}")
                
                # Set PYTHONPATH so that the subprocess can find modules
                env = os.environ.copy()
                server_script_path = Path(self.server_script)
                mcpmark_root = server_script_path.parent.parent.parent.parent
                mcpmark_src = mcpmark_root / "src"
                
                # Update PYTHONPATH
                pythonpath = env.get("PYTHONPATH", "")
                if pythonpath:
                    pythonpath = f"{str(mcpmark_src)}:{pythonpath}"
                else:
                    pythonpath = str(mcpmark_src)
                env["PYTHONPATH"] = pythonpath
                
                logger.debug(f"Setting PYTHONPATH for MCP Server: {pythonpath}")
                
                self.server_process = subprocess.Popen(
                    [sys.executable, self.server_script],
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    bufsize=1,
                    env=env
                )
                logger.info(f"✅ MCP Server started with PID: {self.server_process.pid}")
                
                # Wait briefly to check whether the process exits immediately
                import time
                time.sleep(0.5)
                if self.server_process.poll() is not None:
                    # Process has exited; read stderr for error information
                    stderr_output = ""
                    try:
                        stderr_output = self.server_process.stderr.read(1024)
                    except Exception:
                        pass
                    error_msg = f"MCP Server process exited immediately with code {self.server_process.returncode}. Stderr: {stderr_output}"
                    logger.error(error_msg)
                    raise RuntimeError(error_msg)
                
                # Start log forwarding thread
                self._stop_stderr_thread = False
                self._stderr_thread = threading.Thread(
                    target=self._forward_stderr_logs,
                    daemon=True,
                    name="MCP-Server-Stderr-Forwarder"
                )
                self._stderr_thread.start()
                logger.debug("Started stderr log forwarding thread")
            except FileNotFoundError as e:
                error_msg = f"MCP Server script not found: {e}"
                logger.error(error_msg)
                raise
            except Exception as e:
                error_msg = f"Failed to start MCP Server: {e}"
                logger.error(error_msg)
                import traceback
                logger.error(f"Traceback: {traceback.format_exc()}")
                raise RuntimeError(error_msg) from e
    
    def stop_server(self):
        """Stop the MCP Server process."""
        if self.use_sdk:
            # Use MCP SDK
            try:
                logger.info("Stopping MCP Server (SDK)...")
                # Make sure we clean up within the same event loop
                if self._async_stack and self._loop and not self._loop.is_closed():
                    try:
                        # Use run_until_complete with a timeout to avoid hanging
                        self._loop.run_until_complete(
                            asyncio.wait_for(self._async_stack.aclose(), timeout=5)
                        )
                    except asyncio.TimeoutError:
                        logger.warning("MCP Server cleanup timed out, forcing close...")
                    except Exception as cleanup_e:
                        logger.warning(f"Error during async cleanup: {cleanup_e}")
                        # Try to close the event loop directly
                        try:
                            # Cancel all pending tasks
                            pending = asyncio.all_tasks(self._loop)
                            for task in pending:
                                task.cancel()
                            # Run once to process cancellations
                            if pending:
                                self._loop.run_until_complete(
                                    asyncio.gather(*pending, return_exceptions=True)
                                )
                        except Exception:
                            pass
                
                self._async_stack = None
                self._session = None
                
                # Close the event loop
                if self._loop and not self._loop.is_closed():
                    try:
                        self._loop.close()
                    except Exception as close_e:
                        logger.debug(f"Error closing event loop: {close_e}")
                
                self._loop = None
                logger.info("MCP Server stopped (SDK)")
            except Exception as e:
                logger.warning(f"Error stopping MCP Server (SDK): {e}")
                import traceback
                logger.debug(f"Stop server traceback: {traceback.format_exc()}")
        else:
            # Fallback: use subprocess
            if not hasattr(self, 'server_process') or self.server_process is None:
                logger.debug("MCP Server process not found (may have already been stopped)")
                return
            
            try:
                # Stop stderr forwarding thread
                if self._stderr_thread and self._stderr_thread.is_alive():
                    self._stop_stderr_thread = True
                    # Wait for the thread to finish
                    self._stderr_thread.join(timeout=1.0)
                    if self._stderr_thread.is_alive():
                        logger.debug("Stderr forwarding thread did not stop in time")
                
                logger.info("Stopping MCP Server...")
                if self.server_process and self.server_process.poll() is None:
                    # Process is still running
                    try:
                        self.server_process.terminate()
                        self.server_process.wait(timeout=10)
                        logger.info("MCP Server stopped gracefully")
                    except subprocess.TimeoutExpired:
                        logger.warning("MCP Server did not terminate in time, force killing...")
                        try:
                            # Try SIGKILL to force termination
                            import signal
                            os.kill(self.server_process.pid, signal.SIGKILL)
                            self.server_process.wait(timeout=5)
                            logger.info("MCP Server force killed")
                        except (ProcessLookupError, OSError) as kill_e:
                            logger.warning(f"Process already dead or cannot kill: {kill_e}")
                        except Exception as kill_e:
                            logger.error(f"Error force killing MCP Server: {kill_e}")
                    except Exception as e:
                        logger.error(f"Error stopping MCP Server: {e}")
                        # Try to force terminate again
                        try:
                            import signal
                            if self.server_process.poll() is None:
                                os.kill(self.server_process.pid, signal.SIGKILL)
                                self.server_process.wait(timeout=5)
                                logger.info("MCP Server force killed after error")
                        except Exception as kill_e:
                            logger.error(f"Failed to force kill MCP Server: {kill_e}")
                else:
                    logger.debug("MCP Server process already stopped")
            except Exception as e:
                logger.error(f"Error stopping MCP Server: {e}")
            finally:
                # Ensure process is cleaned up
                if self.server_process:
                    try:
                        if self.server_process.poll() is None:
                            # Process still running; force kill
                            import signal
                            os.kill(self.server_process.pid, signal.SIGKILL)
                            logger.warning("Force killed MCP Server process in finally block")
                    except (ProcessLookupError, OSError):
                        # Process already gone; ignore
                        pass
                    except Exception as final_e:
                        logger.warning(f"Error in finally block cleanup: {final_e}")
                
                self.server_process = None
                self._stderr_thread = None
                self._stop_stderr_thread = False
    
    def call_tool(self, tool_name: str, arguments: dict) -> dict:
        return self._call_tool(tool_name, arguments)
    
    def _call_tool(self, tool_name: str, arguments: dict) -> dict:
        if self.use_sdk and self._session and self._loop:
            # Use MCP SDK
            try:
                logger.debug(f"Calling MCP tool '{tool_name}' via SDK with arguments: {arguments}")

                # Ensure argument types are JSON-serializable
                cleaned_arguments = {}
                for key, value in arguments.items():
                    if isinstance(value, (int, float, bool, list, dict, type(None))):
                        cleaned_arguments[key] = value
                    else:
                        cleaned_arguments[key] = str(value)
                
                # Call tool via MCP SDK
                async def _async_call():
                    # Use different timeouts depending on tool type
                    if tool_name == "osworld_replay_trajectory":
                        timeout = 1800
                    elif tool_name == "osworld_initialize":
                        timeout = 600
                    else:
                        timeout = 300
                    
                    try:
                        result = await asyncio.wait_for(
                            self._session.call_tool(tool_name, cleaned_arguments),
                            timeout=timeout
                        )
                        # Parse result
                        if hasattr(result, 'content') and result.content:
                            # MCP SDK returns a list of Content objects
                            content_text = result.content[0].text if result.content[0].text else "{}"
                            if not content_text or not content_text.strip():
                                logger.warning(f"Empty response from tool '{tool_name}', using default")
                                return {"success": False, "error": "Empty response from server"}
                            try:
                                return json.loads(content_text)
                            except json.JSONDecodeError as e:
                                logger.error(f"Failed to parse JSON response from '{tool_name}': {e}")
                                logger.error(f"Response content: {content_text[:200]}...")
                                return {"success": False, "error": f"Invalid JSON response: {str(e)}"}
                            if hasattr(result, 'model_dump'):
                                return result.model_dump()
                            return {"success": False, "error": "Unexpected result format"}
                    except asyncio.TimeoutError:
                        logger.error(f"Tool '{tool_name}' timed out after {timeout} seconds")
                        return {"success": False, "error": f"Operation timed out after {timeout} seconds"}
                
                result = self._loop.run_until_complete(_async_call())
                return result
                
            except Exception as e:
                logger.error(f"Failed to call MCP tool '{tool_name}' via SDK: {e}")
                import traceback
                logger.error(f"Traceback: {traceback.format_exc()}")
                raise
        else:
            # Fallback: use subprocess
            if self.server_process is None:
                raise RuntimeError("MCP Server not started")
            
            try:
                cleaned_arguments = {}
                for key, value in arguments.items():
                    if isinstance(value, (int, float)):
                        cleaned_arguments[key] = value
                    elif isinstance(value, bool):
                        cleaned_arguments[key] = value
                    elif isinstance(value, (list, dict)):
                        cleaned_arguments[key] = value
                    else:
                        cleaned_arguments[key] = str(value)
                
                request = {
                    "jsonrpc": "2.0",
                    "id": 1,
                    "method": "tools/call",
                    "params": {
                        "name": tool_name,
                        "arguments": cleaned_arguments
                    }
                }
                
                logger.debug(f"Calling MCP tool '{tool_name}' with arguments: {cleaned_arguments}")

                # Send request
                request_json = json.dumps(request, ensure_ascii=False) + "\n"
                self.server_process.stdin.write(request_json)
                self.server_process.stdin.flush()
                
                response_line = self.server_process.stdout.readline()
                
                if not response_line:
                    stderr_output = ""
                    try:
                        import select
                        if select.select([self.server_process.stderr], [], [], 0.1)[0]:
                            stderr_output = self.server_process.stderr.read(1024).decode('utf-8', errors='ignore')
                    except:
                        try:
                            stderr_output = self.server_process.stderr.read(1024).decode('utf-8', errors='ignore')
                        except:
                            pass
                    raise RuntimeError(f"No response from MCP Server. Stderr: {stderr_output}")
                
                response = json.loads(response_line.strip())
                
                # Parse response
                if "error" in response:
                    error_info = response['error']
                    logger.error(f"MCP Server error: {error_info}")
                    raise RuntimeError(f"MCP Server error: {error_info}")
                
                result_content = response.get("result", {})
                if isinstance(result_content, dict):
                    content_list = result_content.get("content", [])
                    if content_list and len(content_list) > 0:
                        result_text = content_list[0].get("text", "{}")
                        result = json.loads(result_text)
                    else:
                        result = result_content
                else:
                    result = result_content
                
                return result
            
            except json.JSONDecodeError as e:
                logger.error(f"JSON decode error when calling tool '{tool_name}': {e}")
                logger.error(f"Response line: {response_line if 'response_line' in locals() else 'N/A'}")
                raise
            except Exception as e:
                logger.error(f"Failed to call MCP tool '{tool_name}': {e}")
                import traceback
                logger.error(f"Traceback: {traceback.format_exc()}")
                raise
    
    # ==================== Public methods compatible with DesktopEnv ====================
    
    def initialize_environment(self, task_config_path: str, provider: str = "aws", 
                              region: str = "us-east-1", screen_width: int = 1920, 
                              screen_height: int = 1080) -> bool:
        """
        Initialize the environment

        Args:
            task_config_path: Path to the task configuration file.
            provider: Virtualization provider.
            region: AWS region.
            screen_width: Screen width.
            screen_height: Screen height.

        Returns:
            Whether initialization succeeded.
        """
        # Ensure argument types are correct (MCP SDK requires strict type matching)
        result = self._call_tool("osworld_initialize", {
            "task_config_path": str(task_config_path),
            "provider": str(provider),
            "region": str(region),
            "screen_width": int(screen_width),
            "screen_height": int(screen_height)
        })
        
        self.initialized = result.get("success", False)
        # Store instance_id if available
        if self.initialized and "instance_id" in result:
            self.instance_id = result["instance_id"]
            logger.info(f"💾 Stored instance ID: {self.instance_id}")
        return self.initialized
    
    def replay_trajectory(self, trajectory_path: str, result_dir: Optional[str] = None, save_screenshots: bool = False) -> bool:
        result = self._call_tool("osworld_replay_trajectory", {
            "trajectory_path": trajectory_path,
            "result_dir": result_dir,
            "save_screenshots": save_screenshots
        })
        
        return result.get("success", False)
    
    def render(self, mode: str = 'rgb_array') -> Optional[Any]:
        result = self._call_tool("osworld_get_observation", {
            "observation_type": "screenshot"
        })
        
        if result.get("success"):
            observation = result.get("observation", {})
            screenshot_b64 = observation.get("screenshot_b64")
            
            if screenshot_b64:
                import base64
                return base64.b64decode(screenshot_b64)
            
        return None
    
    def get_observation(self, observation_type: str = "screenshot") -> Dict[str, Any]:
        result = self._call_tool("osworld_get_observation", {
            "observation_type": observation_type
        })
        
        if result.get("success"):
            return result.get("observation", {})
        else:
            raise RuntimeError(f"Failed to get observation: {result.get('error')}")
    
    def step(self, action_command: str, pause: float = 1.0):
        if not action_command or not action_command.strip():
            logger.warning("Empty action command, skipping execution")
            return
        
        try:
            result = self._call_tool("osworld_execute_action", {
                "action_command": action_command,
                "pause": pause
            })
        
            if result is None:
                logger.warning(f"Received None result for action: {action_command[:50]}...")
                return
            
            if not result.get("success"):
                error_msg = result.get('error', 'Unknown error')
                logger.warning(f"Action execution returned error: {error_msg}")
                return
        except Exception as e:
            logger.warning(f"Exception during action execution: {e}")
            return
    
    def close(self):
        """Close environment and clean up resources."""
        if self.initialized:
            try:
                self._call_tool("osworld_close", {})
            except Exception as e:
                logger.warning(f"Error closing environment via MCP: {e}")
        
        self.stop_server()
        self.initialized = False
    
    def get_status(self) -> dict:
        """Get environment status."""
        result = self._call_tool("osworld_get_status", {})
        return result
    
    def __enter__(self):
        """Context manager entry."""
        self.start_server()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


# ==================== Compatibility Adapter ====================

class GUIMCPAdapter:
    def __init__(self, mcp_client: GUIMCPClient):
        self.mcp_client = mcp_client
        self.controller = MCPControllerAdapter(mcp_client)
    
    def render(self, mode: str = 'rgb_array'):
        return self.mcp_client.render(mode)
    
    def step(self, action_command: str, pause: float = 1.0):
        return self.mcp_client.step(action_command, pause)
    
    def close(self):
        return self.mcp_client.close()


class MCPControllerAdapter:
    def __init__(self, mcp_client: GUIMCPClient):
        self.mcp_client = mcp_client
    
    def get_accessibility_tree(self) -> Optional[str]:
        try:
            observation = self.mcp_client.get_observation("a11y_tree")
            return observation.get("a11y_tree")
        except Exception as e:
            logger.warning(f"Failed to get accessibility tree: {e}")
            return None


