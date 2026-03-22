#! debug script
# python -m agent_judge_search_pipeline \
#     --mcp playwright \
#     --models gpt-4.1 \
#     --agent agent_judge_search \
#     --tasks Mind2Web2-Gemini-2024_film_premiere/2024_film_premiere-Gemini-row_1 \
#     --exp-name debug \
#     --k 1 \
#     --timeout 3600 \
#     --temperature 1.0 \
#     --summarization-temperature 1.0 \
#     --output-dir results \
#     --tasks-root tasks/agent_as_a_judge \
#     --ground-truth-file tasks/agent_as_a_judge/ground_truth/Mind2Web2-single-ground_truth.json \
#     --env-file ".mcp_env" \
#     --worker-id "0"



# !/bin/bash
# ============================================================================
# Parallel Agent-as-a-Judge Pipeline
# ============================================================================
# Usage: bash agent_judge_pipeline.sh [MODELS] [TASK_IDS] [MAX_PARALLEL]
#   MODELS: Comma-separated model names (default: "Gemini,Grok,Perplexity")
#   TASK_IDS: Comma-separated task IDs (default: "2024_film_premiere")
#   MAX_PARALLEL: Maximum number of parallel workers (default: 3)

# Examples:
#   # Run with defaults (3 parallel workers)
#   bash agent_judge_pipeline.sh

#   # Run specific models and tasks with 4 parallel workers
#   bash agent_judge_pipeline.sh "Gemini,Grok" "task1,task2" 4

#   # Run single task (sequential)
#   bash agent_judge_pipeline.sh "Gemini" "task1" 1
# ============================================================================

# Default parameters

#! Mind2Web2 Configuration
MODELS="${1:-Gemini,Grok,Perplexity}"
TASK_IDS="${2:-2024_film_premiere,active_stock,ad_patent,apple_watch,artifact_repatriation,buy_kobe_shoes_reverse_swoosh,captain_america_starring,chinese_dish,chris_evans,closet_picks,county_AQI,cyberpunk_music,dc_comics_injustice,drone_delivery,esport_player,female_scholarships,find_parks,game_awards,gcg_followup,goodreads_winner,hf_vqa_dataset,hypeawards_twice_brand,instrument_in_met,jojo_references,just_bieber_friend,marvel_rivals,meditation_app,mllm_researcher,nba_career_high,nba_player_china_tour,nlp_faculty,openreview_papers,origami_chinese_zodiac,overleaf_template,paper_collaboration,perplexity_failure,plan_nlp_learning,plants_italy,popular_ai_books,pritzker_prize_winner,protein_vis_software,rare_disease,rhone_top_wine,rl_course_book,startups_series_b,supreme_court_230,telescopes_list,tesla_travel,tofu_lunch,tokyo_filming_location,wssa_female_65,yu_lineage}"
MAX_PARALLEL="${3:-3}"

# Configuration
TASKS_ROOT="tasks/agent_as_a_judge"
OUTPUT_DIR="results/Mind2Web2"
GROUND_TRUTH="tasks/agent_as_a_judge/ground_truth/Mind2Web2-single-ground_truth.json"
LOG_DIR="logs/Mind2Web2"

#! WideSearch Configuration
# MODELS="${1:-Gemini,Grok,Perplexity}"
# TASK_IDS="${2:-ws_en_003,ws_en_012,ws_en_014,ws_en_018,ws_en_021,ws_en_022,ws_en_024,ws_en_032,ws_en_040}"
# MAX_PARALLEL="${3:-3}"

# # Configuration
# TASKS_ROOT="tasks/agent_as_a_judge"
# OUTPUT_DIR="results/WideSearch"
# GROUND_TRUTH="tasks/agent_as_a_judge/ground_truth/WideSearch-single-ground_truth.json"
# LOG_DIR="logs/WideSearch"

# Create log directory
mkdir -p "$LOG_DIR"

# Convert comma-separated strings to arrays
IFS=',' read -ra MODEL_ARRAY <<< "$MODELS"
IFS=',' read -ra TASK_ID_ARRAY <<< "$TASK_IDS"

# Validate models
for MODEL in "${MODEL_ARRAY[@]}"; do
    case "$MODEL" in
        Gemini|Grok|Perplexity)
            ;;
        *)
            echo "Error: Invalid model '$MODEL'. Must be one of: Gemini, Grok, Perplexity"
            exit 1
            ;;
    esac
done

# Build list of all task combinations
TASK_COMBINATIONS=()
for MODEL in "${MODEL_ARRAY[@]}"; do
    for TASK_ID in "${TASK_ID_ARRAY[@]}"; do
        TASK_COMBINATIONS+=("${MODEL}:${TASK_ID}")
    done
done

TOTAL_TASKS=${#TASK_COMBINATIONS[@]}

echo "==========================================="
echo "Parallel Agent-as-a-Judge Pipeline"
echo "==========================================="
echo "Models: ${MODEL_ARRAY[*]}"
echo "Task IDs: ${TASK_ID_ARRAY[*]}"
echo "Total combinations: $TOTAL_TASKS"
echo "Max parallel workers: $MAX_PARALLEL"
echo "Output Dir: $OUTPUT_DIR"
echo "Log Dir: $LOG_DIR"
echo "==========================================="

# Function to run a single task
run_task() {
    local WORKER_ID=$1
    local MODEL=$2
    local TASK_ID=$3
    local TASK_NAME="Mind2Web2-${MODEL}-${TASK_ID}"
    local LOG_FILE="${LOG_DIR}/${TASK_NAME}_worker${WORKER_ID}.log"
    
    echo "[Worker $WORKER_ID] Starting: $TASK_NAME"

    # * gpt-5-mini
    # python -m agent_judge_search_pipeline \
    #     --mcp playwright \
    #     --models gpt-5-mini \
    #     --agent agent_judge_search \
    #     --tasks "$TASK_NAME" \
    #     --exp-name debug \
    #     --k 1 \
    #     --timeout 3600 \
    #     --temperature 1.0 \
    #     --summarization-temperature 1.0 \
    #     --reasoning-effort low \
    #     --summarization-reasoning-effort low \
    #     --output-dir "$OUTPUT_DIR" \
    #     --tasks-root "$TASKS_ROOT" \
    #     --ground-truth-file "$GROUND_TRUTH" \
    #     --env-file ".mcp_env" \
    #     --worker-id "$WORKER_ID" \
    #     > "$LOG_FILE" 2>&1
    
    # * deepseek-v3.2-instruct
    python -m agent_judge_search_pipeline \
        --mcp playwright \
        --models deepseek-v3.2-instruct \
        --agent agent_judge_search \
        --tasks "$TASK_NAME" \
        --exp-name debug \
        --k 1 \
        --timeout 3600 \
        --temperature 1.0 \
        --summarization-temperature 1.0 \
        --output-dir "$OUTPUT_DIR" \
        --tasks-root "$TASKS_ROOT" \
        --ground-truth-file "$GROUND_TRUTH" \
        --env-file ".mcp_env" \
        --worker-id "$WORKER_ID" \
        > "$LOG_FILE" 2>&1
    
    local EXIT_CODE=$?
    if [ $EXIT_CODE -eq 0 ]; then
        echo "[Worker $WORKER_ID] Completed: $TASK_NAME"
    else
        echo "[Worker $WORKER_ID] Failed: $TASK_NAME (exit code: $EXIT_CODE)"
    fi
    return $EXIT_CODE
}

# Arrays to track PIDs and task names (using index as worker ID)
PIDS=()
TASK_NAMES=()

# Counter for completed tasks
COMPLETED=0
FAILED=0

# Function to check and clean up finished processes
check_finished_processes() {
    local i=0
    while [ $i -lt ${#PIDS[@]} ]; do
        if [ -n "${PIDS[$i]}" ]; then
            if ! kill -0 "${PIDS[$i]}" 2>/dev/null; then
                # Process finished
                wait "${PIDS[$i]}" 2>/dev/null
                local EXIT_CODE=$?
                if [ $EXIT_CODE -eq 0 ]; then
                    COMPLETED=$((COMPLETED + 1))
                else
                    FAILED=$((FAILED + 1))
                    echo "Task failed: ${TASK_NAMES[$i]} (see logs for details)"
                fi
                # Clear the slot
                PIDS[$i]=""
                TASK_NAMES[$i]=""
                echo "Progress: $((COMPLETED + FAILED))/$TOTAL_TASKS completed (${FAILED} failed)"
            fi
        fi
        i=$((i + 1))
    done
}

# Function to count active processes
count_active() {
    local count=0
    for pid in "${PIDS[@]}"; do
        if [ -n "$pid" ]; then
            count=$((count + 1))
        fi
    done
    echo $count
}

# Function to find an empty slot
find_empty_slot() {
    local i=0
    while [ $i -lt ${#PIDS[@]} ]; do
        if [ -z "${PIDS[$i]}" ]; then
            echo $i
            return
        fi
        i=$((i + 1))
    done
    # No empty slot found, return next index
    echo ${#PIDS[@]}
}

# Function to wait for a worker slot
wait_for_slot() {
    while [ $(count_active) -ge $MAX_PARALLEL ]; do
        check_finished_processes
        sleep 1
    done
}

# Start tasks
echo ""
echo "Starting parallel execution..."
echo "-------------------------------------------"

WORKER_COUNTER=0
for COMBO in "${TASK_COMBINATIONS[@]}"; do
    # Wait for available slot
    wait_for_slot
    
    # Check for any finished processes
    check_finished_processes
    
    # Parse model and task_id
    MODEL="${COMBO%%:*}"
    TASK_ID="${COMBO##*:}"
    
    # Get worker ID (use counter for unique IDs)
    WORKER_COUNTER=$((WORKER_COUNTER + 1))
    WORKER_ID=$WORKER_COUNTER
    
    # Find empty slot
    SLOT=$(find_empty_slot)
    
    # Start task in background
    run_task "$WORKER_ID" "$MODEL" "$TASK_ID" &
    PID=$!
    PIDS[$SLOT]=$PID
    TASK_NAMES[$SLOT]="Mind2Web2-${MODEL}-${TASK_ID}"
done

# Wait for all remaining tasks to complete
echo "-------------------------------------------"
echo "Waiting for remaining tasks to complete..."

for pid in "${PIDS[@]}"; do
    if [ -n "$pid" ]; then
        wait "$pid" 2>/dev/null
        EXIT_CODE=$?
        if [ $EXIT_CODE -eq 0 ]; then
            COMPLETED=$((COMPLETED + 1))
        else
            FAILED=$((FAILED + 1))
        fi
    fi
done

echo ""
echo "==========================================="
echo "Pipeline completed!"
echo "Total: $TOTAL_TASKS | Completed: $COMPLETED | Failed: $FAILED"
echo "Results saved to: $OUTPUT_DIR"
echo "Logs saved to: $LOG_DIR"
echo "==========================================="

# Exit with error if any tasks failed
if [ $FAILED -gt 0 ]; then
    exit 1
fi