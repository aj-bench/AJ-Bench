#!/bin/bash
# ============================================================================
# Agent-as-a-Judge DS Pipeline
# ============================================================================
# Usage: bash agent_judge_ds_pipeline.sh [MODELS] [MCP] [EXP_NAME] [MAX_PARALLEL] [MAX_TASKS]
#
# Positional arguments (all optional, fall back to defaults below):
#   MODELS        Comma-separated judge model names  (default: gpt-5-mini)
#   MCP           MCP service to evaluate            (default: filesystem)
#   EXP_NAME      Experiment name / result sub-dir   (default: 2026-02-17-18-30-25-exp-1)
#   MAX_PARALLEL  Internal parallel worker count      (default: 2)
#   MAX_TASKS     Cap on trajectories evaluated       (default: 2)
#
# Any extra arguments are passed through directly to the Python pipeline.
#
# Examples:
#   # Run with all defaults
#   bash agent_judge_ds_pipeline.sh
#
#   # Override model and parallelism
#   bash agent_judge_ds_pipeline.sh "deepseek-v3.2-instruct" filesystem my-exp 4
#
#   # Run multiple models, no task cap
#   bash agent_judge_ds_pipeline.sh "gpt-5-mini,deepseek-v3.2-instruct" filesystem my-exp 2 ""
#
#   # Pass extra flags (e.g. --tasks, --reasoning-effort) after positional args
#   bash agent_judge_ds_pipeline.sh "gpt-5-mini" filesystem my-exp 2 10 --tasks votenet
# ============================================================================

# ---------------------------------------------------------------------------
# Default parameters
# ---------------------------------------------------------------------------
MODELS="${1:-gpt-5-mini}"
MCP="${2:-filesystem}"
EXP_NAME="${3:-2026-02-17-18-30-25-exp-1}"
MAX_PARALLEL="${4:-2}"
MAX_TASKS="${5:-2}"

# Shift positional args so that "$@" carries only the extras
shift "$(( $# < 5 ? $# : 5 ))"

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
OUTPUT_DIR="Agent-as-a-Judge_DS"
TRAJECTORY_DIR="src/data/DS"
TASKS_DIR="tasks/agent_as_a_judge/mcp_tasks"
ENV_FILE=".mcp_env"
TIMEOUT=300

# ---------------------------------------------------------------------------
# Banner
# ---------------------------------------------------------------------------
echo "MCPMark Judge Evaluation"
IFS=',' read -ra MODEL_ARRAY <<< "$MODELS"
echo "Experiment: $EXP_NAME | ${#MODEL_ARRAY[@]} Judge Model(s): $MODELS"
echo "Trajectory Directory: $TRAJECTORY_DIR"
echo "MCP Service: $MCP"
echo ""

# ---------------------------------------------------------------------------
# Build command
# ---------------------------------------------------------------------------
CMD=(
    python agent_judge_ds_pipeline.py
    --mcp           "$MCP"
    --models        "$MODELS"
    --exp-name      "$EXP_NAME"
    --max_parallel_tasks "$MAX_PARALLEL"
    --trajectory-dir "$TRAJECTORY_DIR"
    --tasks-dir     "$TASKS_DIR"
    --output-dir    "$OUTPUT_DIR"
    --env-file      "$ENV_FILE"
    --timeout       "$TIMEOUT"
    --skip-completed
)

# Append --max-tasks only when a value was provided
if [ -n "$MAX_TASKS" ]; then
    CMD+=(--max-tasks "$MAX_TASKS")
fi

# Append any extra arguments verbatim
CMD+=("$@")

# ---------------------------------------------------------------------------
# Execute
# ---------------------------------------------------------------------------
"${CMD[@]}"
