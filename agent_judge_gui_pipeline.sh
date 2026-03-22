#!/bin/bash
# ============================================================================
# Agent-as-a-Judge GUI Pipeline
# ============================================================================
# Usage: bash agent_judge_gui_pipeline.sh [MODEL] [SUBDOMAIN] [MAX_WORKERS] [EFFORT]
#
# Positional arguments (all optional, fall back to defaults below):
#   MODEL         Judge model name                    (default: gpt-4o)
#   SUBDOMAIN     Subdomain to evaluate               (default: ALL, choices: ALL/PPT/Word/Excel)
#   MAX_WORKERS   Number of parallel worker processes  (default: 1)
#   EFFORT        Reasoning effort level              (default: medium, choices: low/medium/high)
#
# Any extra arguments are passed through directly to the Python pipeline.
#
# Examples:
#   # Run with all defaults
#   bash agent_judge_gui_pipeline.sh
#
#   # Evaluate PPT subdomain with 4 workers
#   bash agent_judge_gui_pipeline.sh gpt-4o PPT 4
#
#   # Full custom run with extra flags
#   bash agent_judge_gui_pipeline.sh gpt-4o ALL 8 medium --temperature 1.0
#
#   # Resume interrupted run (skip already-completed tasks by default)
#   bash agent_judge_gui_pipeline.sh gpt-4o ALL 4
# ============================================================================

# ---------------------------------------------------------------------------
# Default parameters
# ---------------------------------------------------------------------------
MODEL="${1:-gpt-4o}"
SUBDOMAIN="${2:-ALL}"
MAX_WORKERS="${3:-1}"
EFFORT="${4:-medium}"

# Shift positional args so that "$@" carries only the extras
shift "$(( $# < 4 ? $# : 4 ))"

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
PAIRS_ROOT_DIR="src/data/GUI"
OUTPUT_DIR="Agent-as-a-Judge_GUI"
ENV_FILE=".mcp_env"
OBSERVATION_TYPE="a11y_tree"

# ---------------------------------------------------------------------------
# Banner
# ---------------------------------------------------------------------------
echo "==========================================="
echo "Agent-as-a-Judge GUI Pipeline"
echo "==========================================="
echo "Model:         $MODEL"
echo "Subdomain:     $SUBDOMAIN"
echo "Max Workers:   $MAX_WORKERS"
echo "Effort:        $EFFORT"
echo "Pairs Root:    $PAIRS_ROOT_DIR"
echo "Output Dir:    $OUTPUT_DIR"
echo "==========================================="
echo ""

# ---------------------------------------------------------------------------
# Build and execute command
# ---------------------------------------------------------------------------
CMD=(
    python agent_judge_gui_pipeline.py
    --model           "$MODEL"
    --pairs-root-dir  "$PAIRS_ROOT_DIR"
    --subdomain       "$SUBDOMAIN"
    --max-workers     "$MAX_WORKERS"
    --effort          "$EFFORT"
    --observation-type "$OBSERVATION_TYPE"
    --env-file        "$ENV_FILE"
    --output-dir      "$OUTPUT_DIR"
)

# Append any extra arguments verbatim
CMD+=("$@")

echo "Running: ${CMD[*]}"
echo ""

"${CMD[@]}"

EXIT_CODE=$?
echo ""
echo "==========================================="
if [ $EXIT_CODE -eq 0 ]; then
    echo "✓ GUI pipeline completed successfully"
    echo "Results saved to: $OUTPUT_DIR"
else
    echo "✗ GUI pipeline failed (exit code: $EXIT_CODE)"
    echo "Check logs for details."
fi
echo "==========================================="

exit $EXIT_CODE
