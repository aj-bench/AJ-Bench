"""
MCPMark Agent Module
====================

Provides agent implementations and registry for MCPMark.
"""

from .base_agent import BaseMCPAgent
from .mcpmark_agent import MCPMarkAgent
from .react_agent import ReActAgent
from .agent_judge_search import AgentJudgeSearch

AGENT_REGISTRY = {
    "mcpmark": MCPMarkAgent,
    "react": ReActAgent,
    "agent_judge_search": AgentJudgeSearch,
}

__all__ = [
    "BaseMCPAgent",
    "MCPMarkAgent",
    "ReActAgent",
    "AgentJudgeSearch",
    "AGENT_REGISTRY",
]

