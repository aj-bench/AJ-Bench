#!/usr/bin/env python3
"""
Analysis script for single_judge evaluation results.
Aggregates correctness statistics from a result_output directory.
"""

import ast
import os
import json
import glob
from pathlib import Path
from tkinter import FALSE
from typing import Dict, List, Any, Optional, Tuple
from collections import defaultdict
from datetime import datetime

def calculate_f1_score(true_correct: int, true_incorrect: int, false_correct: int, false_incorrect: int) -> Tuple[float, float, float]:
    """
    Compute precision, recall and F1 score
    """
    tp = true_correct
    fp = false_incorrect
    fn = true_incorrect
    
    if tp + fp > 0:
        precision = tp / (tp + fp)
    else:
        precision = 0.0
    
    if tp + fn > 0:
        recall = tp / (tp + fn)
    else:
        recall = 0.0
    
    # Compute F1 score
    if precision + recall > 0:
        f1_score = 2 * (precision * recall) / (precision + recall)
    else:
        f1_score = 0.0
    
    return precision, recall, f1_score

def load_app_type_from_pairs(pairs_root: str, pair_id: str) -> Optional[str]:
    """
    Read application type from the pairs directory JSON files.

    Args:
        pairs_root: root path of the pairs directory
        pair_id: pair ID

    Returns:
        Application type
    """
    pairs_path = Path(pairs_root)
    domain_to_app = {"PPT": "impress", "Word": "writer", "Excel": "calculator"}
    for domain_dir, app_type in domain_to_app.items():
        if (pairs_path / domain_dir / pair_id).exists():
            return app_type
    return None

def save_domain_f1_scores_to_summary(model_name: str, app_type_stats: dict, avg_tool_rounds: float, total_tasks: int, summary_dir: str = "~/agentjudgebench_data/result"):
    """
    Write precision, recall, F1 score, average tool rounds and total task count
    for PPT/WORD/EXCEL into a summary.py file
    
    Args:
        model_name: model name (derived from result directory name)
        app_type_stats: statistics grouped by application type
        avg_tool_rounds: average number of tool interaction rounds
        total_tasks: total number of tasks
        summary_dir: directory where summary.py is stored (default: ~/agentjudgebench_data/result)
    """
    summary_dir_path = Path(summary_dir).expanduser()
    summary_dir_path.mkdir(parents=True, exist_ok=True)
    summary_file = summary_dir_path / "summary.py"
    
    # Domain mapping: impress=PPT, writer=Word, calculator=Excel
    domain_mapping = {
        "impress": "PPT",
        "writer": "Word",
        "calculator": "Excel"
    }
    
    domain_stats = {}
    for app_type, domain_name in domain_mapping.items():
        if app_type in app_type_stats:
            stats = app_type_stats[app_type]
            precision, recall, f1_score = calculate_f1_score(
                stats["true_correct"], stats["true_incorrect"],
                stats["false_correct"], stats["false_incorrect"]
            )
            domain_stats[domain_name] = {
                "precision": precision * 100,
                "recall": recall * 100,
                "f1_score": f1_score * 100
            }
        else:
            domain_stats[domain_name] = {
                "precision": 0.0,
                "recall": 0.0,
                "f1_score": 0.0
            }

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result_entry = {
        "model": model_name,
        "timestamp": timestamp,
        "total_tasks": total_tasks,
        "avg_tool_rounds": avg_tool_rounds,
        "domain_stats": domain_stats
    }
    
    existing_results = []
    if summary_file.exists():
        try:
            with open(summary_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if "results = " in content:
                    # Simple parsing: slice out "results = [...]"
                    start_idx = content.find("results = ") + len("results = ")
                    end_idx = content.rfind("]")
                    if end_idx > start_idx:
                        results_str = content[start_idx:end_idx+1]
                        existing_results = ast.literal_eval(results_str)  # parse Python literal
        except Exception as e:
            print(f"⚠️  Failed to read existing summary.py, creating a new file: {e}")
    
    # Check if this model already has an entry
    model_exists = False
    for i, existing_entry in enumerate(existing_results):
        if existing_entry.get("model") == model_name:
            # Overwrite existing entry for this model
            existing_results[i] = result_entry
            model_exists = True
            print(f"📝 Found existing model '{model_name}', overriding previous record")
            break
    
    # Append a new record if it does not exist
    if not model_exists:
        existing_results.append(result_entry)
        print(f"➕ New model '{model_name}', appending record")
    
    # Write data back to summary.py (Python module format)
    try:
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write("# Model evaluation summary\n")
            f.write("# Auto-generated at: " + timestamp + "\n\n")
            f.write("results = [\n")
            for result in existing_results:
                f.write("    {\n")
                f.write(f"        'model': '{result['model']}',\n")
                f.write(f"        'timestamp': '{result['timestamp']}',\n")
                f.write(f"        'total_tasks': {result['total_tasks']},\n")
                f.write(f"        'avg_tool_rounds': {result['avg_tool_rounds']:.2f},\n")
                f.write("        'domain_stats': {\n")
                for domain in ['PPT', 'Word', 'Excel']:
                    f.write(f"            '{domain}': {{\n")
                    f.write(f"                'precision': {result['domain_stats'][domain]['precision']:.2f},\n")
                    f.write(f"                'recall': {result['domain_stats'][domain]['recall']:.2f},\n")
                    f.write(f"                'f1_score': {result['domain_stats'][domain]['f1_score']:.2f},\n")
                    f.write("            },\n")
                f.write("        },\n")
                f.write("    },\n")
            f.write("]\n")
        
        print(f"\n✅ Summary saved to: {summary_file}")
        print(f"   Total tasks: {total_tasks}")
        print(f"   Model: {model_name}")
        print(f"   Average tool rounds: {avg_tool_rounds:.2f}")
        print(f"   PPT - Precision: {domain_stats['PPT']['precision']:.2f}%, Recall: {domain_stats['PPT']['recall']:.2f}%, F1: {domain_stats['PPT']['f1_score']:.2f}%")
        print(f"   Word - Precision: {domain_stats['Word']['precision']:.2f}%, Recall: {domain_stats['Word']['recall']:.2f}%, F1: {domain_stats['Word']['f1_score']:.2f}%")
        print(f"   Excel - Precision: {domain_stats['Excel']['precision']:.2f}%, Recall: {domain_stats['Excel']['recall']:.2f}%, F1: {domain_stats['Excel']['f1_score']:.2f}%\n")
    except Exception as e:
        print(f"❌ Failed to save summary.py: {e}")

def analyze_results(result_dir: str = None, pairs_root: str = None):
    """
    Analyze all evaluation results under a result_output directory.

    Args:
        result_dir: path to the result directory
    """
    if result_dir is None:
        print("❌ Please provide a result directory path")
        return
    
    result_dir = Path(result_dir)
    
    if not result_dir.exists():
        print(f"❌ Result directory does not exist: {result_dir}")
        return
    
    print(f"📁 Analyzing directory: {result_dir}")
    print("=" * 80)

    def _is_na(value: Any) -> bool:
        if value is None:
            return True
        if isinstance(value, str):
            v = value.strip().lower()
            return v in {"", "n/a", "na", "none", "null"}
        return False
    
    total_results = 0
    correct_judgments = 0
    incorrect_judgments = 0
    no_ground_truth = 0
    failed_evaluations = 0
    
    true_correct = 0
    true_incorrect = 0
    false_correct = 0
    false_incorrect = 0
    
    model_stats = defaultdict(lambda: {"correct": 0, "incorrect": 0, "no_gt": 0, "failed": 0})
    
    app_type_stats = defaultdict(lambda: {
        "correct": 0, 
        "incorrect": 0, 
        "no_gt": 0, 
        "failed": 0,
        "true_correct": 0,
        "true_incorrect": 0,
        "false_correct": 0,
        "false_incorrect": 0
    })
    
    pair_stats = {}
    
    duplicate_tracker = defaultdict(list)
    
    detailed_results = []
    
    tool_call_rounds = []
    
    ignored_task_ids = [
        "39be0d19-634d-4475-8768-09c130f5425d"
    ]
    
    pair_app_types = {}
    if pairs_root:
        pairs_path = Path(pairs_root)
        if pairs_path.exists():
            print(f"📂 Loading application types from pairs_root: {pairs_root}")
    
    missing_result_file_skips = 0
    na_skips = 0
    for item in result_dir.iterdir():
        if not item.is_dir():
            continue
            
        result_file = item / "unified_evaluation_result.json"
        if not result_file.exists():
            missing_result_file_skips += 1
            if missing_result_file_skips <= 10:
                print(f"⚠️  Skipping directory {item.name}: unified_evaluation_result.json not found")
            continue
        
        try:
            with open(result_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Extract basic metadata and statistics
            metadata = data.get("metadata", {})
            final_judgment = data.get("final_judgment", {})
            statistics = data.get("statistics_summary", {})
            
            trajectory_id = metadata.get("trajectory_id", "unknown")
            model = metadata.get("model", "unknown")
            # Try to get ground_truth from statistics_summary first, then from metadata
            ground_truth = statistics.get("ground_truth", "N/A")
            if ground_truth == "N/A":
                ground_truth = metadata.get("ground_truth", "N/A")
            
            agent_judgment = statistics.get("agent_judgment", "N/A")
            is_correct = statistics.get("is_judgment_correct", "N/A")
            
            # Skip entries with any N/A fields (treat as non-existent)
            if _is_na(ground_truth) or _is_na(agent_judgment) or _is_na(is_correct):
                na_skips += 1
                if na_skips <= 10:
                    print(f"⏭️  Skipping directory {item.name}: contains N/A")
                continue
            
            # Convert is_correct to boolean or None for easier handling
            if isinstance(is_correct, bool):
                is_correct_value = is_correct
            elif isinstance(is_correct, str):
                # Handle string representations
                if is_correct.lower() in ["true", "1", "yes"]:
                    is_correct_value = True
                elif is_correct.lower() in ["false", "0", "no"]:
                    is_correct_value = False
                else:
                    is_correct_value = None
            else:
                is_correct_value = bool(is_correct) if is_correct else None

            # Treat unparseable correctness as N/A (ignore)
            if is_correct_value is None:
                na_skips += 1
                if na_skips <= 10:
                    print(f"⏭️  Skipping directory {item.name}: is_correct is not parseable")
                continue
            
            # Extract trajectory_type and pair_id from directory name
            dir_name = item.name
            if "_true_" in dir_name:
                trajectory_type = "true"
                parts = dir_name.split("_true_")
                pair_id = parts[0]
                timestamp = parts[1] if len(parts) > 1 else "00000000_000000"
            elif "_false_" in dir_name:
                trajectory_type = "false"
                parts = dir_name.split("_false_")
                pair_id = parts[0]
                timestamp = parts[1] if len(parts) > 1 else "00000000_000000"
            else:
                trajectory_type = "unknown"
                pair_id = "unknown"
                timestamp = "00000000_000000"
            
            # Skip tasks that are explicitly ignored
            if pair_id in ignored_task_ids:
                print(f"⏭️  Skipping ignored task: {pair_id} ({dir_name})")
                continue
            
            # Get application type
            app_type = None
            if pairs_root and pair_id != "unknown":
                if pair_id not in pair_app_types:
                    pair_app_types[pair_id] = load_app_type_from_pairs(pairs_root, pair_id)
                app_type = pair_app_types[pair_id]
            
            total_results += 1
            
            # Record number of tool interaction rounds if available
            tool_rounds = metadata.get("total_interactions")
            if tool_rounds is not None:
                tool_call_rounds.append(tool_interactions := tool_rounds)
            else:
                tool_interactions = "N/A"
            
            # Update correctness statistics using normalized is_correct_value
            if isinstance(is_correct_value, bool):
                if is_correct_value:
                    correct_judgments += 1
                    if trajectory_type == "true":
                        true_correct += 1
                    elif trajectory_type == "false":
                        false_correct += 1
                else:
                    incorrect_judgments += 1
                    if trajectory_type == "true":
                        true_incorrect += 1
                    elif trajectory_type == "false":
                        false_incorrect += 1
                
                # Per-model statistics
                if is_correct_value:
                    model_stats[model]["correct"] += 1
                else:
                    model_stats[model]["incorrect"] += 1
                
                # Per-application-type statistics
                if app_type:
                    if is_correct_value:
                        app_type_stats[app_type]["correct"] += 1
                        if trajectory_type == "true":
                            app_type_stats[app_type]["true_correct"] += 1
                        elif trajectory_type == "false":
                            app_type_stats[app_type]["false_correct"] += 1
                    else:
                        app_type_stats[app_type]["incorrect"] += 1
                        if trajectory_type == "true":
                            app_type_stats[app_type]["true_incorrect"] += 1
                        elif trajectory_type == "false":
                            app_type_stats[app_type]["false_incorrect"] += 1
            elif is_correct_value is None or is_correct == "N/A":
                # Check if ground_truth exists - if it does, this is a failed evaluation, not missing ground_truth
                if ground_truth in ["true", "false"]:
                    failed_evaluations += 1
                    model_stats[model]["failed"] += 1
                    if app_type:
                        app_type_stats[app_type]["failed"] += 1
                else:
                    no_ground_truth += 1
                    model_stats[model]["no_gt"] += 1
                    if app_type:
                        app_type_stats[app_type]["no_gt"] += 1
            else:
                failed_evaluations += 1
                model_stats[model]["failed"] += 1
                if app_type:
                    app_type_stats[app_type]["failed"] += 1
            
            # Track duplicates: record all results for this (pair_id, trajectory_type)
            if pair_id != "unknown" and trajectory_type in ["true", "false"]:
                task_key = (pair_id, trajectory_type)
                duplicate_tracker[task_key].append({
                    "timestamp": timestamp,
                    "is_correct": is_correct_value,
                    "directory": item.name,
                    "result_file": str(result_file),
                    "trajectory_type": trajectory_type,
                    "model": model,
                    "app_type": app_type,
                    "tool_interactions": tool_interactions
                })
            
            # Update pair-level stats (keeping only the latest result)
            if pair_id != "unknown":
                if pair_id not in pair_stats:
                    pair_stats[pair_id] = {"true_result": None, "false_result": None, "true_timestamp": None, "false_timestamp": None}
                
                if trajectory_type == "true":
                    if pair_stats[pair_id]["true_timestamp"] is None or timestamp > pair_stats[pair_id]["true_timestamp"]:
                        pair_stats[pair_id]["true_result"] = is_correct_value  # Use converted value
                        pair_stats[pair_id]["true_timestamp"] = timestamp
                elif trajectory_type == "false":
                    if pair_stats[pair_id]["false_timestamp"] is None or timestamp > pair_stats[pair_id]["false_timestamp"]:
                        pair_stats[pair_id]["false_result"] = is_correct_value  # Use converted value
                        pair_stats[pair_id]["false_timestamp"] = timestamp
            
            # Record detailed result entry
            detailed_results.append({
                "trajectory_id": trajectory_id,
                "pair_id": pair_id,
                "trajectory_type": trajectory_type,
                "app_type": app_type or "unknown",
                "model": model,
                "ground_truth": ground_truth,
                "agent_judgment": agent_judgment,
                "is_correct": is_correct_value,
                "tool_interactions": tool_interactions,
                "directory": item.name,
                "timestamp": timestamp
            })
            
        except Exception as e:
            print(f"❌ Failed to read file {result_file}: {e}")
            failed_evaluations += 1
            continue
    
    if missing_result_file_skips > 0:
        print(f"⚠️  Total skipped (no unified_evaluation_result.json): {missing_result_file_skips}")
    if na_skips > 0:
        print(f"⚠️  Total skipped (contains N/A): {na_skips}")
    print()
    duplicate_tasks = {}
    duplicate_summary = []
    results_to_count = set()
    
    for task_key, results in duplicate_tracker.items():
        if len(results) > 1:
            pair_id, trajectory_type = task_key
            # Sort by timestamp (oldest first)
            results_sorted = sorted(results, key=lambda x: x["timestamp"])
            
            first_success = None
            for r in results_sorted:
                if r["is_correct"] is True:
                    first_success = r
                    break
            
            selected_result = first_success if first_success else results_sorted[0]
            results_to_count.add(selected_result["directory"])
            
            duplicate_tasks[task_key] = {
                "selected": selected_result,
                "all_results": results_sorted,
                "count": len(results)
            }
            
            duplicate_summary.append({
                "pair_id": pair_id,
                "trajectory_type": trajectory_type,
                "duplicate_count": len(results),
                "selected_timestamp": selected_result["timestamp"],
                "selected_correct": selected_result["is_correct"],
                "selection_reason": "first_success" if first_success else "first_attempt",
                "all_timestamps": [r["timestamp"] for r in results_sorted],
                "all_results": [r["is_correct"] for r in results_sorted]
            })
            
            print(f"   📋 {pair_id}_{trajectory_type}: {len(results)} attempts")
            for idx, r in enumerate(results_sorted, 1):
                marker = "✅ [selected]" if r == selected_result else "⏭️  [skipped]"
                if r["is_correct"] is True:
                    status = "success"
                elif r["is_correct"] is False:
                    status = "failure"
                else:
                    status = "no_gt"
                print(f"      {marker} attempt#{idx} ({r['timestamp']}): {status}")
        else:
            results_to_count.add(results[0]["directory"])
    
    if duplicate_tasks:
        print(f"\n   Found {len(duplicate_tasks)} duplicate tasks")
    print()
    
    total_results = 0
    correct_judgments = 0
    incorrect_judgments = 0
    no_ground_truth = 0
    failed_evaluations = 0
    true_correct = 0
    true_incorrect = 0
    false_correct = 0
    false_incorrect = 0
    model_stats = defaultdict(lambda: {"correct": 0, "incorrect": 0, "no_gt": 0, "failed": 0})
    app_type_stats = defaultdict(lambda: {
        "correct": 0, 
        "incorrect": 0, 
        "no_gt": 0, 
        "failed": 0,
        "true_correct": 0,
        "true_incorrect": 0,
        "false_correct": 0,
        "false_incorrect": 0
    })
    tool_call_rounds = []
    
    for result in detailed_results:
        if result["directory"] not in results_to_count:
            continue
        
        total_results += 1
        is_correct = result["is_correct"]
        trajectory_type = result["trajectory_type"]
        model = result["model"]
        app_type = result["app_type"]
        tool_interactions = result["tool_interactions"]
        
        if tool_interactions != "N/A":
            tool_call_rounds.append(tool_interactions)
        
        if isinstance(is_correct, bool):
            if is_correct:
                correct_judgments += 1
                if trajectory_type == "true":
                    true_correct += 1
                elif trajectory_type == "false":
                    false_correct += 1
            else:
                incorrect_judgments += 1
                if trajectory_type == "true":
                    true_incorrect += 1
                elif trajectory_type == "false":
                    false_incorrect += 1
            
            if is_correct:
                model_stats[model]["correct"] += 1
            else:
                model_stats[model]["incorrect"] += 1
            
            if app_type and app_type != "unknown":
                if is_correct:
                    app_type_stats[app_type]["correct"] += 1
                    if trajectory_type == "true":
                        app_type_stats[app_type]["true_correct"] += 1
                    elif trajectory_type == "false":
                        app_type_stats[app_type]["false_correct"] += 1
                else:
                    app_type_stats[app_type]["incorrect"] += 1
                    if trajectory_type == "true":
                        app_type_stats[app_type]["true_incorrect"] += 1
                    elif trajectory_type == "false":
                        app_type_stats[app_type]["false_incorrect"] += 1
        elif is_correct == "N/A" or is_correct is None:
            ground_truth = result.get("ground_truth", "N/A")
            if ground_truth in ["true", "false"]:
                failed_evaluations += 1
                model_stats[model]["failed"] += 1
                if app_type and app_type != "unknown":
                    app_type_stats[app_type]["failed"] += 1
            else:
                no_ground_truth += 1
                model_stats[model]["no_gt"] += 1
                if app_type and app_type != "unknown":
                    app_type_stats[app_type]["no_gt"] += 1
    
    valid_results = correct_judgments + incorrect_judgments
    overall_precision, overall_recall, overall_f1 = calculate_f1_score(
        true_correct, true_incorrect, false_correct, false_incorrect
    )
    print("📊 GUI domain overall summary:")
    print(f"   Total results: {total_results}")
    print(f"   Valid judgments (with ground truth): {valid_results}")
    print(f"   Correct judgments: {correct_judgments}")
    failed_or_no_result = failed_evaluations + no_ground_truth
    print(f"   Failed or missing-result evaluations: {failed_or_no_result}")
    print(f"   Precision: {overall_precision*100:.2f}%, Recall: {overall_recall*100:.2f}%, F1: {overall_f1*100:.2f}%")
    print()

    # Per-domain statistics (impress, writer, calculator) -> PPT/Word/Excel
    print("📊 Subdomain summary:")
    mapping = {
        "impress": "PPT",
        "writer": "Word",
        "calculator": "Excel",
    }
    for app_type in ["impress", "writer", "calculator"]:
        domain_name = mapping[app_type]
        if app_type in app_type_stats:
            stats = app_type_stats[app_type]
            total_valid = stats["correct"] + stats["incorrect"]
            if total_valid > 0:
                tp = stats["true_correct"]
                fp = stats["false_incorrect"]
                fn = stats["true_incorrect"]
                tn = stats["false_correct"]
                app_precision, app_recall, app_f1 = calculate_f1_score(tp, fn, tn, fp)
                fpr = (fp / (fp + tn)) if (fp + tn) > 0 else None
                fnr = (fn / (fn + tp)) if (fn + tp) > 0 else None
                fpr_str = f"{(fpr*100):.2f}%" if fpr is not None else "N/A"
                fnr_str = f"{(fnr*100):.2f}%" if fnr is not None else "N/A"
                print(
                    f"   {domain_name}: "
                    f"TP={tp}, FP={fp}, FN={fn}, TN={tn}, "
                    f"Correct={stats['correct']}, Total={total_valid}, "
                    f"Precision={app_precision*100:.2f}%, Recall={app_recall*100:.2f}%, F1={app_f1*100:.2f}%, "
                    f"FPR={fpr_str}, FNR={fnr_str}"
                )
            else:
                print(f"   {domain_name}: TP=0, FP=0, FN=0, TN=0, Correct=0, Total=0, Precision=N/A, Recall=N/A, F1=N/A, FPR=N/A, FNR=N/A")
        else:
            print(f"   {domain_name}: TP=0, FP=0, FN=0, TN=0, Correct=0, Total=0, Precision=N/A, Recall=N/A, F1=N/A, FPR=N/A, FNR=N/A")
    print()
    
    avg_tool_rounds = 0
    if tool_call_rounds:
        avg_tool_rounds = sum(tool_call_rounds) / len(tool_call_rounds)
    tool_rounds_dist = {}
    
    # Use the result folder name as model name when saving summary
    folder_name = result_dir.name

    # Save three-domain statistics into ~/agentjudgebench_data/result/summary.py
    # save_domain_f1_scores_to_summary(folder_name, app_type_stats, avg_tool_rounds, total_results)

def main():
    """Entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Analyze single_judge evaluation results."
    )
    parser.add_argument(
        "--result_dir",
        type=str,
        required=True,
        help="Path to the result directory."
    )
    _default_pairs = str(Path(__file__).resolve().parent / "data" / "GUI")
    parser.add_argument(
        "--pairs_root",
        type=str,
        default=None,
        help="Root path of pairs directory"
    )
    
    args = parser.parse_args()
    
    pairs_root = args.pairs_root
    if pairs_root is None:
        pairs_root = _default_pairs
        if Path(pairs_root).exists():
            print(f"ℹ️  Using default pairs directory: {pairs_root}")
        else:
            print("⚠️  Default pairs path does not exist, skipping app-type-based statistics.")
    
    analyze_results(result_dir=args.result_dir, pairs_root=pairs_root)

if __name__ == "__main__":
    main()