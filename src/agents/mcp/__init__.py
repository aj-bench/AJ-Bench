"""
MCP (Model Context Protocol) Components
========================================

Minimal MCP server implementations for MCPMark.
"""

from .stdio_server import MCPStdioServer
from .http_server import MCPHttpServer
from .popup_handler import PlaywrightPopupHandler

__all__ = ["MCPStdioServer", "MCPHttpServer", "PlaywrightPopupHandler"]