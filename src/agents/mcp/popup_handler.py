"""
Popup Handler for MCP Playwright
=================================

Automatically handles common website popups (cookie consent, bot verification)
after navigation events.
"""

import asyncio
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)


class PlaywrightPopupHandler:
    """
    Wraps MCP Playwright tool calls to automatically handle common popups.

    This ensures that cookie consent dialogs and similar interruptions are
    automatically dismissed after navigation, without interfering with task
    execution or requiring manual intervention.
    """

    # Tools that trigger navigation and should be followed by popup handling
    NAVIGATION_TOOLS = {
        "browser_navigate",
        "browser_navigate_back",
        "browser_click",  # May trigger navigation
        "browser_fill_form",  # May trigger navigation after form submit
    }

    # Playwright code to handle common popups
    POPUP_HANDLER_CODE = """
// Use the same pattern as RESULT_CHECK_CODE - direct page.evaluate with console.log
await page.evaluate(() => {
    const acceptTexts = [
        'accept all', 'accept cookies', 'accept', 'i agree', 'agree', 'ok',
        'alles accepteren', 'accepteren',
        'tout accepter', 'accepter',
        'alle akzeptieren', 'akzeptieren',
        'aceptar todo', 'aceptar',
        '同意', '接受', '全部接受'
    ];
    
    // Find all potential buttons
    const buttons = Array.from(document.querySelectorAll('button, a[role="button"]'));
    
    for (const btn of buttons) {
        const text = btn.textContent || btn.innerText;
        if (text) {
            const lower = text.toLowerCase();
            // Check if text matches any pattern
            if (acceptTexts.some(p => lower.includes(p))) {
                // Check visibility
                const style = window.getComputedStyle(btn);
                const rect = btn.getBoundingClientRect();
                const isVisible = style.display !== 'none' && 
                                style.visibility !== 'hidden' && 
                                style.opacity !== '0' &&
                                rect.width > 0 && 
                                rect.height > 0;
                                
                if (isVisible) {
                    // Try native click first (fastest)
                    btn.click();
                    const clickedText = text.trim().substring(0, 40);
                    const result = { clicked: true, text: clickedText };
                    console.log('POPUP_HANDLER_RESULT:', JSON.stringify(result));
                    return result;
                }
            }
        }
    }
    
    // No popup found in page.evaluate
    const result = { clicked: false };
    console.log('POPUP_HANDLER_RESULT:', JSON.stringify(result));
    return result;
});
"""
    RESULT_CHECK_CODE = """
// Use console.log to output JSON so MCP can capture it
await page.evaluate(() => {
    const title = document.title;
    const bodyText = document.body.innerText;

    // Check for Cloudflare challenge indicators
    const isCloudflare = 
        title.includes('请稍候') || 
        title.includes('Just a moment') || 
        title.includes('One moment') ||
        bodyText.includes('Cloudflare') ||
        bodyText.includes('正在验证您是否是真人') ||
        bodyText.includes('Checking your browser') ||
        bodyText.includes('Verifying you are human') ||
        bodyText.includes('Please wait while we check your browser') ||
        bodyText.includes('This process is automatic') ||
        bodyText.includes('Your browser will redirect automatically') ||
        bodyText.includes('Checking if the site connection is secure') ||
        bodyText.includes('DDoS protection by Cloudflare') ||
        bodyText.includes('Ray ID');

    // Check for visible cookie buttons using DOM API
    const buttons = Array.from(document.querySelectorAll('button, a[role="button"]'));
    let hasCookiePopup = false;
    
    for (const btn of buttons) {
        const text = btn.textContent || btn.innerText;
        if (text) {
            const lower = text.toLowerCase();
            if (lower.includes('cookie') || 
                lower.includes('accept') ||
                lower.includes('同意')) {
                
                // Check visibility
                const style = window.getComputedStyle(btn);
                const rect = btn.getBoundingClientRect();
                const isVisible = style.display !== 'none' && 
                                style.visibility !== 'hidden' && 
                                style.opacity !== '0' &&
                                rect.width > 0 && 
                                rect.height > 0;
                                
                if (isVisible) {
                    hasCookiePopup = true;
                    break;
                }
            }
        }
    }

    // Log as JSON with marker for easy extraction
    const result = {
        isCloudflare,
        hasCookiePopup
    };
    console.log('POPUP_CHECK_RESULT:', JSON.stringify(result));
    return result;
});
"""

    def __init__(self, enable_logging: bool = True):
        """
        Initialize popup handler.

        Args:
            enable_logging: Whether to log popup handling actions
        """
        self.enable_logging = enable_logging
        self._last_url = None
        self._in_popup_handling = False  # Flag to prevent recursive calls

    async def wrap_tool_call(
        self, tool_name: str, arguments: Dict[str, Any], call_fn: Any
    ) -> Any:
        """
        Wrap a tool call and handle popups after navigation.

        Args:
            tool_name: Name of the MCP tool being called
            arguments: Tool arguments
            call_fn: Async function to call the actual tool (signature: async fn(name, args))

        Returns:
            Tool call result (updated with post-verification page state if applicable)
        """
        # Execute the original tool call
        result = await call_fn(tool_name, arguments)

        # If this was a navigation tool, try to handle popups
        # BUT: Skip if we're already in popup handling (prevent recursive re-navigate)
        if tool_name in self.NAVIGATION_TOOLS and not self._in_popup_handling:
            try:
                self._in_popup_handling = True  # Set flag before handling
                updated_result = await self._handle_popups_after_navigation(
                    call_fn, tool_name, arguments
                )
                # If popup handling returned updated page state, use it
                if updated_result is not None:
                    result = updated_result
            except Exception as e:
                # Don't fail the task if popup handling fails
                if self.enable_logging:
                    logger.debug(f"Popup handling failed for {tool_name}: {e}")
            finally:
                self._in_popup_handling = False  # Always reset flag

        return result

    async def _handle_popups_after_navigation(
        self, call_fn: Any, tool_name: str, arguments: Dict[str, Any]
    ) -> Any:
        """
        Attempt to handle common popups after navigation.

        Args:
            call_fn: Function to call MCP tools
            tool_name: Original tool name that was called
            arguments: Original tool arguments

        Returns:
            Updated page state after handling Cloudflare/cookies
        """
        try:
            check_result = await asyncio.wait_for(
                call_fn("browser_run_code", {"code": self.RESULT_CHECK_CODE}),
                timeout=10.0,
            )
            check_content = self._extract_content(check_result)
            reuse_tool = False

            # Try to parse as JSON
            if check_content:
                import json
                import re

                try:
                    match = re.search(
                        r"POPUP_CHECK_RESULT:\s*(\{.*?\})", check_content, re.DOTALL
                    )
                    if match:
                        json_candidate = match.group(1).strip()
                        try:
                            check_data = json.loads(json_candidate.split("\n")[0])
                        except json.JSONDecodeError:
                            check_data = {}
                    else:
                        # Fallback: try to parse the entire content as JSON
                        check_data = json.loads(check_content)

                    if self.enable_logging:
                        logger.info(f"Parsed check data: {check_data}")

                    # Handle Cloudflare: wait for verification text to disappear
                    if check_data.get("isCloudflare"):
                        if self.enable_logging:
                            logger.info(
                                "Detected Cloudflare challenge, waiting for verification..."
                            )
                        await call_fn("browser_wait_for", {"time": 6.0})
                        reuse_tool = True

                    # Handle Cookie popup
                    elif check_data.get("hasCookiePopup"):
                        if self.enable_logging:
                            logger.info("Detected cookie popup, handling it...")
                        reuse_tool = True

                except (json.JSONDecodeError, ValueError) as e:
                    if self.enable_logging:
                        logger.debug(f"Could not parse check result as JSON: {e}")

            # Try to handle cookie popups (with timeout)
            popup_result = await asyncio.wait_for(
                call_fn("browser_run_code", {"code": self.POPUP_HANDLER_CODE}),
                timeout=10.0,
            )

            if self.enable_logging and popup_result:
                content = self._extract_content(popup_result)
                if content:
                    import json
                    import re

                    # Try to extract JSON from console.log output
                    match = re.search(
                        r"POPUP_HANDLER_RESULT:\s*(\{.*?\})", content, re.DOTALL
                    )
                    if match:
                        try:
                            json_str = match.group(1).strip()
                            popup_data = json.loads(json_str.split("\n")[0])

                            if popup_data.get("clicked"):
                                if "text" in popup_data:
                                    logger.info(
                                        f"Auto-handled popup: {popup_data['text']}"
                                    )
                                elif "selector" in popup_data:
                                    logger.info(
                                        f"Auto-handled popup via selector: {popup_data['selector']}"
                                    )
                                else:
                                    logger.info("Auto-handled popup successfully")

                                await call_fn("browser_wait_for", {"time": 1.0})
                                reuse_tool = True
                        except (json.JSONDecodeError, ValueError) as e:
                            if self.enable_logging:
                                logger.debug(
                                    f"Could not parse popup result as JSON: {e}"
                                )
                    elif "Clicked" in content:
                        # Fallback for old format
                        logger.info(f"Auto-handled popup: {content}")
                        await call_fn("browser_wait_for", {"time": 1.0})
                        reuse_tool = True

            if reuse_tool:
                if self.enable_logging:
                    logger.info(
                        f"Popup handling completed, re-calling {tool_name} to get verified page result"
                    )

                # Re-call the original tool with same arguments
                # Since Cloudflare/cookies are already handled, this won't trigger them again
                # Note: _in_popup_handling flag prevents recursive loop
                updated_result = await call_fn(tool_name, arguments)
                return updated_result

            # No issues detected, return None to use original result
            return None

        except asyncio.TimeoutError:
            if self.enable_logging:
                logger.warning("Popup handling timed out, using original result")
            return None
        except Exception as e:
            # Don't fail the task if popup handling fails
            if self.enable_logging:
                logger.debug(f"Popup handling skipped or failed: {e}")
            return None

    def _extract_content(self, result: Any) -> Any:
        """
        Extract content from MCP tool result.

        Args:
            result: MCP tool call result

        Returns:
            Extracted content
        """
        # Handle different result formats
        if hasattr(result, "content"):
            # MCP SDK format with .content attribute
            content_list = result.content
            if isinstance(content_list, list) and len(content_list) > 0:
                first_item = content_list[0]
                if hasattr(first_item, "text"):
                    return first_item.text
                elif isinstance(first_item, dict) and "text" in first_item:
                    return first_item["text"]
        elif isinstance(result, dict):
            # MCP result format: {"content": [{"type": "text", "text": "..."}]}
            content = result.get("content", [])
            if isinstance(content, list) and len(content) > 0:
                first_item = content[0]
                if isinstance(first_item, dict):
                    return first_item.get("text")
        return None
