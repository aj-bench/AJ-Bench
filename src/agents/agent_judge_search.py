"""
Agent-as-a-Judge Search Implementation
=======================================

Agent judge with web content summarization support, built on the new BaseMCPAgent
infrastructure.
"""

from __future__ import annotations

import asyncio
import json
import os
import tempfile
import time
import uuid
from typing import Any, Callable, Dict, List, Optional

import httpx
import litellm
import nest_asyncio
from pydantic import AnyUrl

from src.logger import get_logger
from tasks.agent_as_a_judge.prompt import SINGLE_ROW_SUMMARY_PROMPT

from .base_agent import BaseMCPAgent
from .mcp import MCPHttpServer, MCPStdioServer, PlaywrightPopupHandler

# Apply nested asyncio support
nest_asyncio.apply()

# Configure LiteLLM
litellm.suppress_debug_info = True

logger = get_logger(__name__)


# To fix the "Object of type AnyUrl is not JSON serializable" error.
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, AnyUrl):
            return str(obj)
        return super().default(obj)


class AgentJudgeSearch(BaseMCPAgent):
    """
    Agent-as-a-Judge with web content search and summarization.
    """

    # Service categories matching the old AgentJudge
    STDIO_SERVICES = [
        "notion",
        "filesystem",
        "playwright",
        "playwright_webarena",
        "postgres",
    ]
    HTTP_SERVICES = ["github"]

    MAX_TURNS = 100
    SYSTEM_PROMPT = (
        "You are a helpful agent that uses tools iteratively to complete the user's task, "
        'and when finished, provides the final answer or simply states "Task completed" '
        "without further tool calls."
    )

    # When enabled, reorder the judge prompt so that all static content
    # (task-independent instructions + the per-task Query/Response/Rubric) forms
    # a cache-stable prefix and the only per-row variable -- the extracted
    # "Single-Row" -- is placed last. Across the many single-row judgments of one
    # task this keeps the shared prefix identical, so provider-side prompt
    # caching (e.g. DeepSeek context caching) is reused instead of re-billed.
    CACHE_FRIENDLY_PROMPT_ORDER = True
    COMPACTION_PROMPT = (
        "You are performing a CONTEXT CHECKPOINT COMPACTION.\n"
        "Summarize the conversation so far for another model to continue.\n\n"
        "Include:\n"
        "- Current progress and key decisions made\n"
        "- Important context, constraints, or user preferences\n"
        "- What remains to be done (clear next steps)\n"
        "- Any critical data, examples, or references needed to continue\n\n"
        "Be concise and structured. Do NOT call tools."
    )

    def __init__(
        self,
        litellm_input_model_name: str,
        api_key: str,
        base_url: str,
        mcp_service: str,
        timeout: int = BaseMCPAgent.DEFAULT_TIMEOUT,
        service_config: Optional[Dict[str, Any]] = None,
        service_config_provider: Optional[Callable[[], Dict[str, Any]]] = None,
        reasoning_effort: Optional[str] = "default",
        compaction_token: int = BaseMCPAgent.COMPACTION_DISABLED_TOKEN,
        temperature: Optional[float] = 0.0,
        summarization_reasoning_effort: Optional[str] = "default",
        summarization_temperature: Optional[float] = 0.0,
        deepseek_thinking: bool = False,
        summarization_deepseek_thinking: bool = False,
    ):
        """
        Initialize the Agent-as-a-Judge Search agent.

        Args:
            litellm_input_model_name: Name of the LLM model (LiteLLM format)
            api_key: API key for the model provider
            base_url: Base URL for the API
            mcp_service: MCP service type
            timeout: Execution timeout in seconds
            service_config: Service-specific configuration
            service_config_provider: Optional provider for dynamic config
            reasoning_effort: Reasoning effort level ("default", "low", "medium", "high")
            compaction_token: Token threshold for context compaction
            temperature: Temperature for the main agent LLM calls
            summarization_reasoning_effort: Reasoning effort for summarization calls
            summarization_temperature: Temperature for summarization calls
            deepseek_thinking: Enable DeepSeek thinking mode for main agent
            summarization_deepseek_thinking: Enable DeepSeek thinking for summarization
        """
        super().__init__(
            litellm_input_model_name=litellm_input_model_name,
            api_key=api_key,
            base_url=base_url,
            mcp_service=mcp_service,
            timeout=timeout,
            service_config=service_config,
            service_config_provider=service_config_provider,
            reasoning_effort=reasoning_effort,
            compaction_token=compaction_token,
        )

        self.temperature = temperature
        self.summarization_reasoning_effort = summarization_reasoning_effort
        self.summarization_temperature = summarization_temperature
        self.deepseek_thinking = deepseek_thinking
        self.summarization_deepseek_thinking = summarization_deepseek_thinking

        # Initialize popup handler for Playwright services
        self.popup_handler = None
        if mcp_service in ("playwright", "playwright_webarena"):
            self.popup_handler = PlaywrightPopupHandler(enable_logging=True)
            logger.debug(
                "Initialized PlaywrightPopupHandler for automatic popup handling"
            )

        logger.debug(
            "Initialized AgentJudgeSearch for '%s' with model '%s' "
            "(Claude: %s, Thinking: %s, Reasoning: %s)",
            mcp_service,
            litellm_input_model_name,
            self.is_claude,
            self.use_claude_thinking,
            reasoning_effort,
        )

    # ==================== MCP Server Management (Override) ====================

    def _create_stdio_server(self) -> MCPStdioServer:
        """
        Create stdio-based MCP server.

        Overrides the base class to provide a more detailed Playwright configuration
        with isolated user data directories, anti-detection browser args, and
        custom context options (locale, timezone, viewport, userAgent, extraHTTPHeaders).
        """
        if self.mcp_service == "notion":
            notion_key = self.service_config.get("notion_key")
            if not notion_key:
                raise ValueError("Notion API key required")
            return MCPStdioServer(
                command="npx",
                args=["-y", "@notionhq/notion-mcp-server"],
                env={
                    "OPENAPI_MCP_HEADERS": (
                        '{"Authorization": "Bearer ' + notion_key + '", '
                        '"Notion-Version": "2022-06-28"}'
                    )
                },
            )

        if self.mcp_service == "filesystem":
            test_directory = self.service_config.get("test_directory")
            if not test_directory:
                raise ValueError("Test directory required for filesystem service")
            return MCPStdioServer(
                command="npx",
                args=[
                    "-y",
                    "@modelcontextprotocol/server-filesystem",
                    str(test_directory),
                ],
            )

        if self.mcp_service in ("playwright", "playwright_webarena"):
            browser = self.service_config.get("browser", "chromium")
            headless = self.service_config.get("headless", True)
            viewport_width = self.service_config.get("viewport_width", 1280)
            viewport_height = self.service_config.get("viewport_height", 720)
            worker_id = self.service_config.get("worker_id")

            # Create isolated user data directory for parallel execution
            if worker_id:
                user_data_dir = f"/tmp/playwright/playwright-worker-{worker_id}"
            else:
                user_data_dir = f"/tmp/playwright/playwright-{uuid.uuid4().hex[:8]}"

            os.makedirs(user_data_dir, exist_ok=True)

            config = {
                "browser": {
                    "browserName": browser,
                    "isolated": True,
                    "userDataDir": user_data_dir,
                    "launchOptions": {
                        "headless": headless,
                        "executablePath": self.service_config.get(
                            "executable_path",
                            os.environ.get("PLAYWRIGHT_EXECUTABLE_PATH", ""),
                        ) or None,
                        "args": [
                            "--disable-blink-features=AutomationControlled",
                        ],
                    },
                    "contextOptions": {
                        "locale": "en-US",
                        "timezoneId": "America/New_York",
                        "viewport": {
                            "width": viewport_width,
                            "height": viewport_height,
                        },
                        "userAgent": (
                            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/131.0.0.0 Safari/537.36"
                        ),
                        "extraHTTPHeaders": {
                            "Accept-Language": "en-US,en;q=0.9",
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                            "Accept-Encoding": "gzip, deflate, br",
                            "Sec-Ch-Ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                            "Sec-Ch-Ua-Mobile": "?0",
                            "Sec-Ch-Ua-Platform": '"macOS"',
                        },
                        "javaScriptEnabled": True,
                        "hasTouch": False,
                        "isMobile": False,
                    },
                }
            }

            logger.debug(f"Playwright userDataDir: {user_data_dir}")

            config_file = tempfile.NamedTemporaryFile(
                mode="w+", suffix=".json", delete=False
            )
            json.dump(config, config_file)
            config_file.close()

            args = ["-y", "@playwright/mcp@latest", "--config", config_file.name]

            # Suppress EventEmitter MaxListenersExceededWarning from Playwright MCP Server
            env = {"NODE_NO_WARNINGS": "1"}

            return MCPStdioServer(
                command="npx",
                args=args,
                env=env,
                cleanup_files=[config_file.name],
            )

        if self.mcp_service == "postgres":
            host = self.service_config.get("host", "localhost")
            port = self.service_config.get("port", 5432)
            username = self.service_config.get("username")
            password = self.service_config.get("password")
            database = self.service_config.get(
                "current_database"
            ) or self.service_config.get("database")
            if not all([username, password, database]):
                raise ValueError("PostgreSQL requires username, password, and database")
            database_url = (
                f"postgresql://{username}:{password}@{host}:{port}/{database}"
            )
            return MCPStdioServer(
                command="pipx",
                args=["run", "postgres-mcp", "--access-mode=unrestricted"],
                env={"DATABASE_URI": database_url},
            )

        raise ValueError(f"Unsupported stdio service: {self.mcp_service}")

    def _create_http_server(self) -> MCPHttpServer:
        """
        Create HTTP-based MCP server.

        Overrides the base class to route GitHub via HTTP (matching old AgentJudge).
        """
        if self.mcp_service == "github":
            github_token = self.service_config.get("github_token")
            if not github_token:
                raise ValueError("GitHub token required")
            return MCPHttpServer(
                url="https://api.githubcopilot.com/mcp/",
                headers={
                    "Authorization": f"Bearer {github_token}",
                    "User-Agent": "MCPMark/1.0",
                },
            )
        raise ValueError(f"Unsupported HTTP service: {self.mcp_service}")

    # ==================== Public Interface ====================

    async def execute(
        self, instruction: str, tool_call_log_file: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Execute instruction with the agent.

        Args:
            instruction: The instruction/prompt to execute
            tool_call_log_file: Optional path to log tool calls

        Returns:
            Dictionary containing execution results
        """
        start_time = time.time()

        try:
            self._reset_progress()
            self._refresh_service_config()

            async def _execute_with_strategy():
                if self.use_claude_thinking:
                    return await self._execute_claude_native_with_tools(
                        instruction, tool_call_log_file
                    )
                else:
                    return await self._execute_litellm_with_tools(
                        instruction, tool_call_log_file
                    )

            result = await asyncio.wait_for(
                _execute_with_strategy(), timeout=self.timeout
            )

            execution_time = time.time() - start_time

            self.usage_tracker.update(
                success=result["success"],
                token_usage=result.get("token_usage", {}),
                turn_count=result.get("turn_count", 0),
                execution_time=execution_time,
            )

            result["execution_time"] = execution_time
            return result

        except Exception as e:
            execution_time = time.time() - start_time
            if isinstance(e, asyncio.TimeoutError):
                error_msg = f"Execution timed out after {self.timeout} seconds"
                logger.error(error_msg)
            else:
                error_msg = f"Agent execution failed: {e}"
                logger.error(error_msg, exc_info=True)

            self.usage_tracker.update(
                success=False,
                token_usage=self._partial_token_usage or {},
                turn_count=self._partial_turn_count or 0,
                execution_time=execution_time,
            )

            if self._partial_messages:
                if not self.is_claude:
                    final_msg = self._convert_to_sdk_format(self._partial_messages)
                else:
                    final_msg = self._partial_messages
            else:
                final_msg = []

            return {
                "success": False,
                "output": final_msg,
                "token_usage": self._partial_token_usage or {},
                "turn_count": self._partial_turn_count or 0,
                "execution_time": execution_time,
                "error": error_msg,
                "litellm_run_model_name": self.litellm_run_model_name,
            }

    # ==================== Claude Native API Execution Path ====================

    async def _execute_claude_native_with_tools(
        self, instruction: str, tool_call_log_file: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Execute Claude with thinking using native Anthropic API.
        Creates MCP server, gets tools, and executes with thinking.
        """
        logger.debug("Using Claude native API with thinking")

        thinking_budget = self._get_claude_thinking_budget()

        mcp_server = await self._create_mcp_server()

        async with mcp_server:
            tools = await mcp_server.list_tools()
            anthropic_tools = self._convert_to_anthropic_format(tools)

            return await self._execute_anthropic_native_tool_loop(
                instruction,
                anthropic_tools,
                mcp_server,
                thinking_budget,
                tool_call_log_file,
            )

    async def _call_claude_native_api(
        self,
        messages: List[Dict],
        thinking_budget: int,
        tools: Optional[List[Dict]] = None,
        mcp_servers: Optional[List[Dict]] = None,
        system: Optional[str] = None,
    ) -> tuple:
        """
        Call Claude's native API directly using httpx.

        Returns:
            Tuple of (response_json, error_message)
        """
        api_base = os.getenv("ANTHROPIC_API_BASE", "https://api.anthropic.com")
        headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
            "anthropic-beta": "context-1m-2025-08-07",
        }

        max_tokens = max(thinking_budget + 4096, 4096)
        payload = {
            "model": self.litellm_input_model_name.replace("anthropic/", ""),
            "max_tokens": max_tokens,
            "temperature": self.temperature or 1.0,
            "messages": messages,
        }

        if thinking_budget:
            payload["thinking"] = {"type": "enabled", "budget_tokens": thinking_budget}

        if tools:
            payload["tools"] = tools
            payload["tool_choice"] = {"type": "auto"}

        if mcp_servers:
            headers["anthropic-beta"] = "mcp-client-2025-04-04"
            payload["mcp_servers"] = mcp_servers

        if system:
            payload["system"] = system

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{api_base}/v1/messages",
                    headers=headers,
                    json=payload,
                    timeout=self.timeout,
                )
                response.raise_for_status()
                return response.json(), None
            except httpx.HTTPStatusError as e:
                return None, e.response.text
            except Exception as e:
                return None, str(e)

    async def _count_claude_input_tokens(
        self,
        messages: List[Dict[str, Any]],
        tools: Optional[List[Dict]] = None,
        system: Optional[str] = None,
    ) -> int:
        """Count input tokens using Claude's token counting API."""
        api_base = os.getenv("ANTHROPIC_API_BASE", "https://api.anthropic.com")
        headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        }
        payload: Dict[str, Any] = {
            "model": self.litellm_input_model_name.replace("anthropic/", ""),
            "messages": messages,
        }
        if tools:
            payload["tools"] = tools
        if system:
            payload["system"] = system

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{api_base}/v1/messages/count_tokens",
                headers=headers,
                json=payload,
                timeout=self.timeout,
            )
            response.raise_for_status()
            data = response.json() or {}
            return int(data.get("input_tokens", 0) or 0)

    def _extract_litellm_text(self, response: Any) -> str:
        """Extract text content from a LiteLLM response."""
        try:
            choices = getattr(response, "choices", None) or []
            if not choices:
                return ""
            msg = getattr(choices[0], "message", None)
            if msg is not None:
                return str(getattr(msg, "content", "") or "")
            return str(getattr(choices[0], "text", "") or "")
        except Exception:
            return ""

    def _extract_anthropic_text(self, response_json: Dict[str, Any]) -> str:
        """Extract text content from a Claude API response."""
        pieces: List[str] = []
        for block in response_json.get("content", []) or []:
            if isinstance(block, dict) and block.get("type") == "text":
                text = block.get("text")
                if text:
                    pieces.append(str(text))
        return "\n".join(pieces).strip()

    def _merge_usage(self, total_tokens: Dict[str, int], usage: Dict[str, Any]) -> None:
        """Merge usage data into total_tokens dict."""
        try:
            input_tokens = int(usage.get("input_tokens", 0) or 0)
            output_tokens = int(usage.get("output_tokens", 0) or 0)
            total_tokens_count = int(
                usage.get("total_tokens", 0) or (input_tokens + output_tokens)
            )
            total_tokens["input_tokens"] += input_tokens
            total_tokens["output_tokens"] += output_tokens
            total_tokens["total_tokens"] += total_tokens_count
        except Exception:
            return

    # ==================== Context Compaction ====================

    async def _maybe_compact_litellm_messages(
        self,
        messages: List[Dict[str, Any]],
        total_tokens: Dict[str, int],
        tool_call_log_file: Optional[str],
        current_prompt_tokens: int,
    ) -> List[Dict[str, Any]]:
        """Compact messages if prompt tokens exceed threshold."""
        if not self._compaction_enabled():
            return messages
        if current_prompt_tokens < self.compaction_token:
            return messages

        logger.info(
            f"| [compaction] Triggered at prompt tokens: {current_prompt_tokens:,}"
        )
        if tool_call_log_file:
            try:
                with open(tool_call_log_file, "a", encoding="utf-8") as f:
                    f.write(
                        f"| [compaction] Triggered at prompt tokens: {current_prompt_tokens:,}\n"
                    )
            except Exception:
                pass

        compact_messages = [
            {"role": "system", "content": self.COMPACTION_PROMPT},
            {"role": "user", "content": json.dumps(messages, ensure_ascii=False)},
        ]
        completion_kwargs = {
            "model": self.litellm_input_model_name,
            "messages": compact_messages,
            "api_key": self.api_key,
        }
        if self.base_url:
            completion_kwargs["base_url"] = self.base_url
        response = await litellm.acompletion(**completion_kwargs)

        usage = getattr(response, "usage", None)
        if usage:
            input_tokens = (
                getattr(usage, "prompt_tokens", None)
                or getattr(usage, "input_tokens", None)
                or 0
            )
            output_tokens = (
                getattr(usage, "completion_tokens", None)
                or getattr(usage, "output_tokens", None)
                or 0
            )
            total_tokens_count = getattr(usage, "total_tokens", None)
            if total_tokens_count is None:
                total_tokens_count = input_tokens + output_tokens
            total_tokens["input_tokens"] += int(input_tokens or 0)
            total_tokens["output_tokens"] += int(output_tokens or 0)
            total_tokens["total_tokens"] += int(total_tokens_count or 0)

        summary = self._extract_litellm_text(response).strip() or "(no summary)"
        system_msg = (
            messages[0]
            if messages
            else {"role": "system", "content": self.SYSTEM_PROMPT}
        )
        first_user = (
            messages[1] if len(messages) > 1 else {"role": "user", "content": ""}
        )
        return [
            system_msg,
            first_user,
            {
                "role": "user",
                "content": f"Context summary (auto-compacted due to token limit):\n{summary}",
            },
        ]

    async def _maybe_compact_anthropic_messages(
        self,
        messages: List[Dict[str, Any]],
        total_tokens: Dict[str, int],
        thinking_budget: int,
        tool_call_log_file: Optional[str],
        current_input_tokens: int,
    ) -> List[Dict[str, Any]]:
        """Compact messages for Claude path if input tokens exceed threshold."""
        if not self._compaction_enabled():
            return messages
        if current_input_tokens < self.compaction_token:
            return messages

        logger.info(
            f"| [compaction] Triggered at input tokens: {current_input_tokens:,}"
        )
        if tool_call_log_file:
            try:
                with open(tool_call_log_file, "a", encoding="utf-8") as f:
                    f.write(
                        f"| [compaction] Triggered at input tokens: {current_input_tokens:,}\n"
                    )
            except Exception:
                pass

        compact_messages = [
            {"role": "user", "content": self.COMPACTION_PROMPT},
            {"role": "user", "content": json.dumps(messages, ensure_ascii=False)},
        ]
        response, error_msg = await self._call_claude_native_api(
            messages=compact_messages,
            thinking_budget=thinking_budget,
            tools=None,
            system=None,
        )
        if error_msg or not response:
            logger.warning(f"| [compaction] Failed: {error_msg}")
            return messages

        usage = response.get("usage", {}) or {}
        input_tokens = usage.get("input_tokens", 0) or 0
        output_tokens = usage.get("output_tokens", 0) or 0
        total_tokens["input_tokens"] += int(input_tokens)
        total_tokens["output_tokens"] += int(output_tokens)
        total_tokens["total_tokens"] += int(input_tokens + output_tokens)

        summary = self._extract_anthropic_text(response) or "(no summary)"
        first_user = messages[0] if messages else {"role": "user", "content": ""}
        return [
            first_user,
            {
                "role": "user",
                "content": f"Context summary (auto-compacted due to token limit):\n{summary}",
            },
        ]

    # ==================== Claude Native Tool Loop ====================

    async def _execute_anthropic_native_tool_loop(
        self,
        instruction: str,
        tools: List[Dict],
        mcp_server: Any,
        thinking_budget: int,
        tool_call_log_file: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Execute Claude thinking loop with function calling.
        Handles thinking blocks, tool calls, and message formatting.
        """
        messages = [{"role": "user", "content": instruction}]
        total_tokens = {
            "input_tokens": 0,
            "output_tokens": 0,
            "total_tokens": 0,
            "reasoning_tokens": 0,
        }
        turn_count = 0
        max_turns = self.MAX_TURNS
        hit_turn_limit = False
        ended_normally = False
        error_msg = None

        system_text = self.SYSTEM_PROMPT
        self._update_progress(messages, total_tokens, turn_count)

        for _ in range(max_turns):
            turn_count += 1

            # Compaction check
            current_input_tokens = 0
            if self._compaction_enabled():
                try:
                    current_input_tokens = await self._count_claude_input_tokens(
                        messages=messages,
                        tools=tools,
                        system=system_text,
                    )
                except Exception as exc:
                    logger.debug("Claude token counting failed: %s", exc)

            messages = await self._maybe_compact_anthropic_messages(
                messages=messages,
                total_tokens=total_tokens,
                thinking_budget=thinking_budget,
                tool_call_log_file=tool_call_log_file,
                current_input_tokens=current_input_tokens,
            )
            self._update_progress(messages, total_tokens, turn_count)

            # Call Claude native API
            response, error_msg = await self._call_claude_native_api(
                messages=messages,
                thinking_budget=thinking_budget,
                tools=tools,
                system=system_text,
            )
            if turn_count == 1 and response:
                self.litellm_run_model_name = response["model"].split("/")[-1]

            if error_msg:
                break

            # Update token usage
            if "usage" in response:
                usage = response["usage"]
                input_tokens = usage.get("input_tokens", 0)
                output_tokens = usage.get("output_tokens", 0)
                total_tokens_count = output_tokens + input_tokens

                total_tokens["input_tokens"] += input_tokens
                total_tokens["output_tokens"] += output_tokens
                total_tokens["total_tokens"] += total_tokens_count

            # Extract blocks from response
            blocks = response.get("content", [])
            tool_uses = [b for b in blocks if b.get("type") == "tool_use"]
            thinking_blocks = [b for b in blocks if b.get("type") == "thinking"]
            text_blocks = [b for b in blocks if b.get("type") == "text"]

            # Log text output
            for tb in text_blocks:
                if tb.get("text") and tool_call_log_file:
                    with open(tool_call_log_file, "a", encoding="utf-8") as f:
                        f.write(f"{tb['text']}\n")
                if tb.get("text"):
                    for line in tb["text"].splitlines():
                        logger.info(f"| {line}")

            # Build assistant message with all blocks
            assistant_content = []

            for tb in thinking_blocks:
                assistant_content.append(
                    {
                        "type": "thinking",
                        "thinking": tb.get("thinking", ""),
                        "signature": tb.get("signature", ""),
                    }
                )

            for tb in text_blocks:
                if tb.get("text"):
                    assistant_content.append({"type": "text", "text": tb["text"]})

            for tu in tool_uses:
                assistant_content.append(
                    {
                        "type": "tool_use",
                        "id": tu.get("id"),
                        "name": tu.get("name"),
                        "input": tu.get("input", {}),
                    }
                )

            messages.append({"role": "assistant", "content": assistant_content})
            self._update_progress(messages, total_tokens, turn_count)

            # If no tool calls, we're done
            if not tool_uses:
                ended_normally = True
                break

            # Execute tools and add results
            tool_results = []
            for tu in tool_uses:
                name = tu.get("name")
                inputs = tu.get("input", {})

                args_str = json.dumps(inputs, separators=(",", ": "))
                display_args = (
                    args_str[:140] + "..." if len(args_str) > 140 else args_str
                )
                logger.info(f"| \033[1m{name}\033[0m \033[2;37m{display_args}\033[0m")

                if tool_call_log_file:
                    with open(tool_call_log_file, "a", encoding="utf-8") as f:
                        f.write(f"| {name} {args_str}\n")

                try:
                    result = await asyncio.wait_for(
                        self._call_tool_with_popup_handling(mcp_server, name, inputs),
                        timeout=180,
                    )
                    tool_results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": tu["id"],
                            "content": [
                                {
                                    "type": "text",
                                    "text": json.dumps(result, cls=CustomJSONEncoder),
                                }
                            ],
                        }
                    )
                except Exception as e:
                    logger.error(f"Tool call failed: {e}")
                    tool_results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": tu["id"],
                            "content": [{"type": "text", "text": f"Error: {str(e)}"}],
                        }
                    )

            messages.append({"role": "user", "content": tool_results})
            self._update_progress(messages, total_tokens, turn_count)

        # Handle exit conditions
        if not ended_normally:
            if turn_count >= max_turns:
                hit_turn_limit = True
                logger.warning(
                    f"| Max turns ({max_turns}) exceeded; returning failure with partial output."
                )
                if tool_call_log_file:
                    try:
                        with open(tool_call_log_file, "a", encoding="utf-8") as f:
                            f.write(f"| Max turns ({max_turns}) exceeded\n")
                    except Exception:
                        pass
            elif error_msg:
                logger.warning(f"| {error_msg}\n")
                if tool_call_log_file:
                    try:
                        with open(tool_call_log_file, "a", encoding="utf-8") as f:
                            f.write(f"| {error_msg}\n")
                    except Exception:
                        pass

        # Display final token usage
        if total_tokens["total_tokens"] > 0:
            log_msg = (
                f"|\n| Token usage: Total: {total_tokens['total_tokens']:,} | "
                f"Input: {total_tokens['input_tokens']:,} | "
                f"Output: {total_tokens['output_tokens']:,}"
            )
            if total_tokens.get("reasoning_tokens", 0) > 0:
                log_msg += f" | Reasoning: {total_tokens['reasoning_tokens']:,}"
            logger.info(log_msg)
            logger.info(f"| Turns: {turn_count}")

        sdk_format_messages = self._convert_to_sdk_format(messages)

        if hit_turn_limit:
            return {
                "success": False,
                "output": sdk_format_messages,
                "token_usage": total_tokens,
                "turn_count": turn_count,
                "error": f"Max turns ({max_turns}) exceeded",
                "litellm_run_model_name": self.litellm_run_model_name,
            }

        if error_msg:
            return {
                "success": False,
                "output": sdk_format_messages,
                "token_usage": total_tokens,
                "turn_count": turn_count,
                "error": error_msg,
                "litellm_run_model_name": self.litellm_run_model_name,
            }

        return {
            "success": True,
            "output": sdk_format_messages,
            "token_usage": total_tokens,
            "turn_count": turn_count,
            "error": None,
            "litellm_run_model_name": self.litellm_run_model_name,
        }

    # ==================== LiteLLM Execution Path ====================

    async def _execute_litellm_with_tools(
        self, instruction: str, tool_call_log_file: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Execute with manual MCP server management.
        Used for all non-Anthropic models and Anthropic models with STDIO services.
        """
        logger.debug("Using manual MCP execution with function calling loop")

        mcp_server = await self._create_mcp_server()

        try:
            async with mcp_server:
                tools = await mcp_server.list_tools()
                functions = self._convert_to_openai_format(tools)

                return await self._execute_litellm_tool_loop(
                    instruction, functions, mcp_server, tool_call_log_file
                )
        except Exception as e:
            logger.error(f"Manual MCP execution failed: {e}")
            raise

    def _build_initial_messages(self, instruction: str) -> List[Dict[str, str]]:
        """Build the initial [system, user] messages for a single-row judgment.

        With ``CACHE_FRIENDLY_PROMPT_ORDER`` the rendered task instruction is
        reordered so the static parts become a cache-stable prefix and the
        variable ``Single-Row`` comes last. Content is unchanged -- only the
        order differs. Falls back to the original layout when the expected
        section markers are absent.
        """
        markers = ("### Query", "### Single-Row", "## Core Principle")
        if self.CACHE_FRIENDLY_PROMPT_ORDER and all(m in instruction for m in markers):
            i_query = instruction.index("### Query")
            i_single = instruction.index("### Single-Row")
            i_rules = instruction.index("## Core Principle")
            static_intro = instruction[:i_query]          # header / role framing
            task_context = instruction[i_query:i_single]   # Query + Response + Rubric (static per task)
            single_row = instruction[i_single:i_rules]     # extracted Single-Row (variable, per row)
            static_rules = instruction[i_rules:]           # procedure / judgment rules / output format
            return [
                {"role": "system", "content": self.SYSTEM_PROMPT + "\n\n" + static_intro + static_rules},
                {"role": "user", "content": task_context + single_row},
            ]
        return [
            {"role": "system", "content": self.SYSTEM_PROMPT},
            {"role": "user", "content": instruction},
        ]

    async def _execute_litellm_tool_loop(
        self,
        instruction: str,
        functions: List[Dict],
        mcp_server: Any,
        tool_call_log_file: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Execute function calling loop with LiteLLM, including web content summarization."""
        messages = self._build_initial_messages(instruction)
        total_tokens = {
            "input_tokens": 0,
            "output_tokens": 0,
            "total_tokens": 0,
            "reasoning_tokens": 0,
        }
        turn_count = 0
        max_turns = self.MAX_TURNS
        consecutive_failures = 0
        max_consecutive_failures = 6
        hit_turn_limit = False
        ended_normally = False

        # Convert functions to tools format for newer models
        tools = (
            [{"type": "function", "function": func} for func in functions]
            if functions
            else None
        )

        if tool_call_log_file and tools:
            max_name_length = (
                max(len(tool.get("function", {}).get("name", "")) for tool in tools)
                if tools
                else 15
            )
            with open(tool_call_log_file, "a", encoding="utf-8") as f:
                f.write("===== Available Tools =====\n")
                for tool in tools:
                    function_info = tool.get("function", {})
                    tool_name = function_info.get("name", "N/A")
                    description = function_info.get("description", "N/A")
                    f.write(
                        f"- ToolName: {tool_name:<{max_name_length}} Description: {description}\n"
                    )
                f.write("\n===== Execution Logs =====\n")

        self._update_progress(messages, total_tokens, turn_count)

        try:
            while turn_count < max_turns:
                # Compaction check
                current_prompt_tokens = 0
                if self._compaction_enabled():
                    current_prompt_tokens = self._count_prompt_tokens_litellm(messages)

                messages = await self._maybe_compact_litellm_messages(
                    messages=messages,
                    total_tokens=total_tokens,
                    tool_call_log_file=tool_call_log_file,
                    current_prompt_tokens=current_prompt_tokens,
                )
                self._update_progress(messages, total_tokens, turn_count)

                # Build completion kwargs
                completion_kwargs = {
                    "model": self.litellm_input_model_name,
                    "messages": messages,
                    "api_key": self.api_key,
                    "temperature": self.temperature or 1.0,
                }

                if tools:
                    completion_kwargs["tools"] = tools
                    completion_kwargs["tool_choice"] = "auto"

                if self.reasoning_effort != "default":
                    completion_kwargs["reasoning_effort"] = self.reasoning_effort
                if self.base_url:
                    completion_kwargs["base_url"] = self.base_url

                # DeepSeek thinking mode
                if self.deepseek_thinking:
                    completion_kwargs["extra_body"] = {"thinking": {"type": "enabled"}}
                    completion_kwargs["max_tokens"] = 16384

                try:
                    individual_timeout = min(self.timeout * 0.8, 300)
                    response = await asyncio.wait_for(
                        litellm.acompletion(**completion_kwargs),
                        timeout=individual_timeout,
                    )
                    consecutive_failures = 0
                except asyncio.TimeoutError:
                    logger.warning(f"| ✗ LLM call timed out on turn {turn_count + 1}")
                    consecutive_failures += 1
                    if consecutive_failures >= max_consecutive_failures:
                        raise Exception(
                            f"Too many consecutive failures ({consecutive_failures})"
                        )
                    wait_time = min(30, 5 * consecutive_failures)
                    logger.info(f"| Retrying after timeout in {wait_time} seconds...")
                    await asyncio.sleep(wait_time)
                    continue
                except Exception as e:
                    error_msg = str(e)
                    logger.error(f"| ✗ LLM call failed on turn {turn_count + 1}: {e}")

                    if hasattr(e, "response") and e.response:
                        logger.debug(f"| Error response details: {e.response}")
                    if hasattr(e, "status_code"):
                        logger.debug(f"| HTTP status code: {e.status_code}")

                    consecutive_failures += 1

                    is_retryable = False
                    wait_time = 2**consecutive_failures

                    if "RateLimitError" in error_msg:
                        is_retryable = True
                        if "internal_error" in error_msg:
                            wait_time = min(120, 30 * consecutive_failures)
                            logger.warning(
                                f"| Internal error detected, waiting {wait_time}s before retry"
                            )
                        else:
                            wait_time = min(60, 20 * consecutive_failures)
                            logger.warning(
                                f"| Rate limit detected, waiting {wait_time}s before retry"
                            )
                    elif "ContextWindowExceededError" in error_msg:
                        is_retryable = False
                        logger.error("| Context window exceeded, cannot retry")
                        # Best-effort fallback: compact and retry once
                        messages = await self._maybe_compact_litellm_messages(
                            messages=messages,
                            total_tokens=total_tokens,
                            tool_call_log_file=tool_call_log_file,
                            current_prompt_tokens=self.compaction_token,
                        )
                        self._update_progress(messages, total_tokens, turn_count)
                        continue
                    elif any(
                        keyword in error_msg.lower()
                        for keyword in [
                            "timeout",
                            "connection",
                            "network",
                            "503",
                            "502",
                            "500",
                        ]
                    ):
                        is_retryable = True
                        wait_time = min(45, 8 * consecutive_failures)
                        logger.warning(
                            f"| Network/server error detected, waiting {wait_time}s before retry"
                        )
                    elif "BadRequestError" in error_msg or "400" in error_msg:
                        is_retryable = False
                        logger.error("| Bad request error, cannot retry")
                        raise
                    else:
                        is_retryable = True
                        logger.warning(
                            f"| Unknown error type, attempting retry with {wait_time}s wait"
                        )

                    if consecutive_failures >= max_consecutive_failures:
                        logger.error(
                            f"| Too many consecutive failures ({consecutive_failures}), giving up"
                        )
                        raise

                    if is_retryable:
                        logger.info(
                            f"| Retrying in {wait_time} seconds... "
                            f"(attempt {consecutive_failures}/{max_consecutive_failures})"
                        )
                        await asyncio.sleep(wait_time)
                        continue
                    else:
                        raise

                # Extract actual model name from response (first turn only)
                if turn_count == 0 and hasattr(response, "model") and response.model:
                    self.litellm_run_model_name = response.model.split("/")[-1]

                # Update token usage including reasoning tokens
                if hasattr(response, "usage") and response.usage:
                    input_tokens = response.usage.prompt_tokens or 0
                    total_tokens_count = response.usage.total_tokens or 0
                    output_tokens = (
                        total_tokens_count - input_tokens
                        if total_tokens_count > 0
                        else (response.usage.completion_tokens or 0)
                    )

                    total_tokens["input_tokens"] += input_tokens
                    total_tokens["output_tokens"] += output_tokens
                    total_tokens["total_tokens"] += total_tokens_count

                    if hasattr(response.usage, "completion_tokens_details"):
                        details = response.usage.completion_tokens_details
                        if hasattr(details, "reasoning_tokens"):
                            total_tokens["reasoning_tokens"] += (
                                details.reasoning_tokens or 0
                            )

                    # Track provider-side prompt cache hits when reported
                    # (OpenAI-style prompt_tokens_details.cached_tokens and/or
                    # DeepSeek-style prompt_cache_hit_tokens) for observability.
                    prompt_details = getattr(
                        response.usage, "prompt_tokens_details", None
                    )
                    cached_tokens = 0
                    if prompt_details is not None:
                        cached_tokens = getattr(prompt_details, "cached_tokens", 0) or 0
                    if not cached_tokens:
                        cached_tokens = (
                            getattr(response.usage, "prompt_cache_hit_tokens", 0) or 0
                        )
                    if cached_tokens:
                        total_tokens["cached_input_tokens"] = (
                            total_tokens.get("cached_input_tokens", 0) + cached_tokens
                        )

                # Get response message
                choices = response.choices
                if len(choices):
                    message = choices[0].message
                    message_dict = (
                        message.model_dump()
                        if hasattr(message, "model_dump")
                        else dict(message)
                    )

                    # Preserve function_call if present
                    if hasattr(message, "function_call") and message.function_call:
                        if (
                            "function_call" not in message_dict
                            or not message_dict["function_call"]
                        ):
                            fc = message.function_call
                            message_dict["function_call"] = (
                                fc.model_dump() if hasattr(fc, "model_dump") else fc
                            )

                # Log assistant's text content if present
                if hasattr(message, "content") and message.content:
                    for line in message.content.splitlines():
                        logger.info(f"| {line}")

                    if tool_call_log_file:
                        with open(tool_call_log_file, "a", encoding="utf-8") as f:
                            f.write(f"{message.content}\n")

                # Check for tool calls
                if hasattr(message, "tool_calls") and message.tool_calls:
                    messages.append(message_dict)
                    turn_count += 1
                    self._update_progress(messages, total_tokens, turn_count)

                    for tool_call in message.tool_calls:
                        func_name = tool_call.function.name

                        # Parse function arguments with error handling
                        try:
                            func_args = json.loads(tool_call.function.arguments)
                        except json.JSONDecodeError as e:
                            logger.warning(
                                f"Failed to parse tool call arguments for '{func_name}': {e}. "
                                f"Raw arguments: {tool_call.function.arguments[:200]}..."
                            )
                            messages.append(
                                {
                                    "role": "tool",
                                    "tool_call_id": tool_call.id,
                                    "content": (
                                        f"Error: Invalid JSON in function arguments - {e}. "
                                        "Please retry with valid JSON."
                                    ),
                                }
                            )
                            continue

                        try:
                            result = await asyncio.wait_for(
                                self._call_tool_with_popup_handling(
                                    mcp_server, func_name, func_args
                                ),
                                timeout=180,
                            )

                            # Summarize & Extract web information
                            result_content = json.dumps(result, cls=CustomJSONEncoder)
                            query = (
                                instruction.split("[The Start of Query]\n")[1]
                                .split("\n[The End of Query]")[0]
                                .strip()
                            )
                            single_row = (
                                instruction.split("[The Start of Single-Row]\n")[1]
                                .split("\n[The End of Single-Row]")[0]
                                .strip()
                            )
                            summarized_response = await self._summarize_web_content(
                                query=query,
                                single_row=single_row,
                                result=result_content,
                            )
                            if type(summarized_response) is str:
                                # Summarization failed, return original content
                                messages.append(
                                    {
                                        "role": "tool",
                                        "tool_call_id": tool_call.id,
                                        "content": summarized_response,
                                    }
                                )
                            else:
                                # Update token usage from summarization
                                if (
                                    hasattr(summarized_response, "usage")
                                    and summarized_response.usage
                                ):
                                    s_input = (
                                        summarized_response.usage.prompt_tokens or 0
                                    )
                                    s_total = (
                                        summarized_response.usage.total_tokens or 0
                                    )
                                    s_output = (
                                        s_total - s_input
                                        if s_total > 0
                                        else (
                                            summarized_response.usage.completion_tokens
                                            or 0
                                        )
                                    )

                                    total_tokens["input_tokens"] += s_input
                                    total_tokens["output_tokens"] += s_output
                                    total_tokens["total_tokens"] += s_total

                                    if hasattr(
                                        summarized_response.usage,
                                        "completion_tokens_details",
                                    ):
                                        details = summarized_response.usage.completion_tokens_details
                                        if hasattr(details, "reasoning_tokens"):
                                            total_tokens["reasoning_tokens"] += (
                                                details.reasoning_tokens or 0
                                            )

                                summarized_response = summarized_response.choices[
                                    0
                                ].message.content
                                messages.append(
                                    {
                                        "role": "tool",
                                        "tool_call_id": tool_call.id,
                                        "content": summarized_response,
                                    }
                                )

                        except asyncio.TimeoutError:
                            err = f"Tool call '{func_name}' timed out after 180 seconds"
                            logger.error(err)
                            messages.append(
                                {
                                    "role": "tool",
                                    "tool_call_id": tool_call.id,
                                    "content": f"Error: {err}",
                                }
                            )
                        except Exception as e:
                            logger.error(f"Tool call failed: {e}")
                            messages.append(
                                {
                                    "role": "tool",
                                    "tool_call_id": tool_call.id,
                                    "content": f"Error: {str(e)}",
                                }
                            )

                        # Log tool call
                        args_str = json.dumps(func_args, separators=(",", ": "))
                        display_arguments = (
                            args_str[:140] + "..." if len(args_str) > 140 else args_str
                        )
                        logger.info(
                            f"| \033[1m{func_name}\033[0m \033[2;37m{display_arguments}\033[0m"
                        )

                        if tool_call_log_file:
                            with open(tool_call_log_file, "a", encoding="utf-8") as f:
                                f.write(f"| {func_name} {args_str}\n")

                    self._update_progress(messages, total_tokens, turn_count)
                    continue
                else:
                    # Check for empty response
                    has_content = hasattr(message, "content") and message.content
                    has_tool_calls = (
                        hasattr(message, "tool_calls") and message.tool_calls
                    )

                    if not has_content and not has_tool_calls:
                        reasoning_tokens = total_tokens.get("reasoning_tokens", 0)
                        output_tokens = total_tokens.get("output_tokens", 0)

                        if (
                            reasoning_tokens > 0
                            and reasoning_tokens >= output_tokens * 0.9
                        ):
                            logger.warning(
                                f"| ⚠️ Model produced no content or tool calls. "
                                f"Reasoning tokens ({reasoning_tokens}) consumed most of output ({output_tokens}). "
                                f"This may indicate the response was truncated due to thinking mode."
                            )
                        else:
                            logger.warning(
                                "| ⚠️ Model produced no content or tool calls in this turn."
                            )

                    # Log end reason
                    if not choices:
                        logger.info(
                            "|\n|\n| Task ended with no messages generated by the model."
                        )
                    elif choices[0].finish_reason == "stop":
                        logger.info(
                            "|\n|\n| Task ended with the finish reason from messages being 'stop'."
                        )
                    elif choices[0].finish_reason == "length":
                        logger.warning(
                            "|\n|\n| Task ended due to max token limit (finish_reason='length'). "
                            "Response may be incomplete."
                        )

                    messages.append(message_dict)
                    turn_count += 1
                    self._update_progress(messages, total_tokens, turn_count)
                    ended_normally = True
                    break

        except Exception as loop_error:
            logger.error(f"Manual MCP loop failed: {loop_error}", exc_info=True)
            sdk_format_messages = self._convert_to_sdk_format(messages)
            return {
                "success": False,
                "output": sdk_format_messages,
                "token_usage": total_tokens,
                "turn_count": turn_count,
                "error": str(loop_error),
                "litellm_run_model_name": self.litellm_run_model_name,
            }

        # Detect if we exited due to hitting the turn limit
        if (not ended_normally) and (turn_count >= max_turns):
            hit_turn_limit = True
            logger.warning(
                f"| Max turns ({max_turns}) exceeded; returning failure with partial output."
            )
            if tool_call_log_file:
                try:
                    with open(tool_call_log_file, "a", encoding="utf-8") as f:
                        f.write(f"| Max turns ({max_turns}) exceeded\n")
                except Exception:
                    pass

        # Display final token usage
        if total_tokens["total_tokens"] > 0:
            log_msg = (
                f"| Token usage: Total: {total_tokens['total_tokens']:,} | "
                f"Input: {total_tokens['input_tokens']:,} | "
                f"Output: {total_tokens['output_tokens']:,}"
            )
            if total_tokens.get("reasoning_tokens", 0) > 0:
                log_msg += f" | Reasoning: {total_tokens['reasoning_tokens']:,}"
            logger.info(log_msg)
            logger.info(f"| Turns: {turn_count}")

        sdk_format_messages = self._convert_to_sdk_format(messages)

        return {
            "success": not hit_turn_limit,
            "output": sdk_format_messages,
            "token_usage": total_tokens,
            "turn_count": turn_count,
            "error": (f"Max turns ({max_turns}) exceeded" if hit_turn_limit else None),
            "litellm_run_model_name": self.litellm_run_model_name,
        }

    # ==================== Popup Handling ====================

    async def _call_tool_with_popup_handling(
        self, mcp_server: Any, tool_name: str, arguments: Dict[str, Any]
    ) -> Any:
        """
        Call MCP tool with automatic popup handling for Playwright services.

        Args:
            mcp_server: MCP server instance
            tool_name: Name of the tool to call
            arguments: Tool arguments

        Returns:
            Tool call result
        """
        if self.popup_handler:

            async def call_fn(name, args):
                return await mcp_server.call_tool(name, args)

            return await self.popup_handler.wrap_tool_call(
                tool_name, arguments, call_fn
            )
        else:
            return await mcp_server.call_tool(tool_name, arguments)

    # ==================== Web Content Summarization ====================

    def _truncate_by_tokens(self, text: str, reserve_ratio: float = 0.15) -> str:
        """
        Truncate text based on model's token limit, reserving space for response.

        Args:
            text: Text to truncate
            reserve_ratio: Ratio of context to reserve for model response

        Returns:
            Truncated text if needed, otherwise original text
        """
        model_limit = None

        try:
            tokens = litellm.encode(model=self.litellm_input_model_name, text=text)
            current_count = len(tokens)

            # Hardcoded limits for DeepSeek models
            if self.litellm_input_model_name in (
                "deepseek/deepseek-chat",
                "deepseek/deepseek-reasoner",
            ):
                model_limit = 128000
            else:
                model_limit = litellm.get_model_info(self.litellm_input_model_name)[
                    "max_input_tokens"
                ]
            if model_limit is None:
                model_limit = 128000

            max_input_tokens = int(model_limit * (1 - reserve_ratio))

            if current_count <= max_input_tokens:
                return text

            logger.warning(
                f"Content exceeds limit ({current_count:,} > {max_input_tokens:,} tokens), "
                f"truncating (model: {self.litellm_input_model_name}, limit: {model_limit:,})"
            )

            truncated_tokens = tokens[:max_input_tokens]
            truncated_text = litellm.decode(
                model=self.litellm_input_model_name, tokens=truncated_tokens
            )

            return truncated_text

        except Exception as e:
            logger.warning(
                f"Token truncation failed: {e}, using character-based fallback"
            )
            if model_limit is None:
                model_limit = 128000
            max_chars = int(model_limit * (1 - reserve_ratio) * 4)
            if len(text) > max_chars:
                return text[:max_chars]
            return text

    async def _summarize_web_content(
        self, query: str, single_row: str, result: str
    ) -> Any:
        """
        Summarize web content using SINGLE_ROW_SUMMARY_PROMPT.

        Args:
            query: The user query
            single_row: The candidate answer to verify
            result: Raw web page content

        Returns:
            LiteLLM response object on success, or original result string on failure
        """
        # Use more aggressive truncation to reduce input size
        result = self._truncate_by_tokens(result, reserve_ratio=0.2)

        completion_kwargs = {
            "model": self.litellm_input_model_name,
            "messages": [
                {
                    "role": "user",
                    "content": SINGLE_ROW_SUMMARY_PROMPT.format(
                        query=query, single_row=single_row, result=result
                    ),
                }
            ],
            "api_key": self.api_key,
            "temperature": self.summarization_temperature or 1.0,
        }
        if self.base_url:
            completion_kwargs["base_url"] = self.base_url
        if self.summarization_reasoning_effort != "default":
            completion_kwargs["reasoning_effort"] = self.summarization_reasoning_effort

        # DeepSeek thinking mode for summarization
        if self.summarization_deepseek_thinking:
            completion_kwargs["extra_body"] = {"thinking": {"type": "enabled"}}
            completion_kwargs["max_tokens"] = 8192

        max_retries = 3
        consecutive_failures = 0

        while consecutive_failures < max_retries:
            try:
                summary_response = await asyncio.wait_for(
                    litellm.acompletion(**completion_kwargs),
                    timeout=300,
                )
                return summary_response
            except asyncio.TimeoutError:
                consecutive_failures += 1
                logger.warning(
                    f"Summarization attempt {consecutive_failures}/{max_retries} timed out after 300s"
                )
                if consecutive_failures >= max_retries:
                    break

                wait_time = min(30, 5 * consecutive_failures)
                logger.info(
                    f"| Retrying summarization after timeout in {wait_time} seconds..."
                )
                await asyncio.sleep(wait_time)
                continue

            except Exception as e:
                consecutive_failures += 1
                error_msg = str(e)
                logger.warning(
                    f"Summarization attempt {consecutive_failures}/{max_retries} failed: {e}"
                )

                if consecutive_failures >= max_retries:
                    break

                is_retryable = False
                wait_time = 2**consecutive_failures

                if "RateLimitError" in error_msg:
                    is_retryable = True
                    if "internal_error" in error_msg:
                        wait_time = min(60, 30 * consecutive_failures)
                    else:
                        wait_time = min(30, 10 * consecutive_failures)
                elif "ContextWindowExceededError" in error_msg:
                    is_retryable = False
                    logger.error(
                        "| Context window exceeded during summarization, cannot retry"
                    )
                    break
                elif any(
                    keyword in error_msg.lower()
                    for keyword in [
                        "timeout",
                        "connection",
                        "network",
                        "503",
                        "502",
                        "500",
                    ]
                ):
                    is_retryable = True
                    wait_time = min(30, 5 * consecutive_failures)
                elif "BadRequestError" in error_msg or "400" in error_msg:
                    is_retryable = False
                    logger.error(
                        "| Bad request error during summarization, cannot retry"
                    )
                    break
                else:
                    is_retryable = True

                if is_retryable:
                    logger.info(f"| Retrying summarization in {wait_time} seconds...")
                    await asyncio.sleep(wait_time)
                else:
                    break

        logger.warning("All summarization attempts failed, returning original content")
        return result
