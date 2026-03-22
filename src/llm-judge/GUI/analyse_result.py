import json
import os
from pathlib import Path
from typing import Dict, List, Tuple
from collections import defaultdict


def read_result_file(file_path: str) -> Dict:
    """Read a single result.json file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None


def find_all_result_files(result_dir: str) -> List[str]:
    """Find all result.json files under a directory"""
    result_files = []
    for root, dirs, files in os.walk(result_dir):
        for file in files:
            if file == "result.json":
                result_files.append(os.path.join(root, file))
    return result_files


def parse_task_id(task_id: str) -> Tuple[str, str]:
    """Parse task_id and return (task_base_id, type) """
    if task_id.endswith("_true"):
        return task_id[:-5], "true"
    elif task_id.endswith("_false"):
        return task_id[:-6], "false"
    else:
        return task_id, "unknown"


def map_snapshot_to_category(snapshot: str, related_apps=None) -> str:
    """Infer sub-type (Excel/Word/PPT/unknown) from snapshot metadata"""
    related_apps = related_apps or []
    candidates = [snapshot] + related_apps
    for s in candidates:
        if not s:
            continue
        s_lower = s.lower()
        if s_lower == "libreoffice_calc":
            return "Excel"
        if s_lower == "libreoffice_writer":
            return "Word"
        if s_lower == "libreoffice_impress":
            return "PPT"
    # Fallback: if still unknown, try keyword-based heuristics
    for s in candidates:
        s_lower = (s or "").lower()
        if any(key in s_lower for key in ["calc", "excel", "sheet"]):
            return "Excel"
        if any(key in s_lower for key in ["writer", "word"]):
            return "Word"
        if any(key in s_lower for key in ["impress", "powerpoint", "ppt"]):
            return "PPT"
    return "unknown"


def find_task_in_pairs(pairs_dir: str, task_base_id: str):
    for domain in ["PPT", "Word", "Excel"]:
        task_root = os.path.join(pairs_dir, domain, task_base_id)
        if os.path.isdir(task_root):
            return task_root, domain
    return None, None


def get_task_category(task_base_id: str, pairs_dir: str, task_root: str = None) -> str:
    if task_root is None:
        task_root, _ = find_task_in_pairs(pairs_dir, task_base_id)
    if task_root is None:
        return "unknown"
    for variant in ["true", "false"]:
        json_path = os.path.join(task_root, variant, f"{task_base_id}.json")
        if not os.path.exists(json_path):
            continue
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            snapshot = data.get("snapshot", "")
            related_apps = data.get("related_apps", [])
            return map_snapshot_to_category(snapshot, related_apps)
        except Exception as e:
            print(f"Failed to read task type from {json_path}: {e}")
            return "unknown"
    return "unknown"


def analyze_results(result_dir: str, pairs_dir: str = "./pairs"):
    """Analyze all result.json files and print aggregated statistics"""
    
    # List of base task IDs to ignore (all related true/false variants and timestamps will be skipped).
    IGNORED_BASE_IDS = {
        "39be0d19-634d-4475-8768-09c130f5425d"
    }
    
    result_files = find_all_result_files(result_dir)
    print(f"Found {len(result_files)} result files")
    
    all_results = {}
    task_pairs = defaultdict(dict)  # {task_base_id: {"true": result, "false": result}}
    ignored_count = 0
    not_in_pairs_count = 0
    
    for file_path in result_files:
        result = read_result_file(file_path)
        if result is None:
            continue
            
        task_id = result.get("task_id", "")
        task_base_id, task_type = parse_task_id(task_id)
        
        should_ignore = any(task_id.startswith(ignored_id) for ignored_id in IGNORED_BASE_IDS)
        if should_ignore:
            ignored_count += 1
            print(f"Ignoring task (in ignore list): {task_id}")
            continue
        
        task_root, _ = find_task_in_pairs(pairs_dir, task_base_id)
        if task_root is None:
            not_in_pairs_count += 1
            ignored_count += 1
            if not_in_pairs_count <= 10:
                print(f"Ignoring task (not found in pairs directory): {task_id}")
            continue
        
        all_results[task_id] = result
        task_pairs[task_base_id][task_type] = result
    
    if not_in_pairs_count > 10:
        print(f"  ... and {not_in_pairs_count - 10} more not found in pairs directory.")
    print(f"Loaded {len(all_results)} results")
    if ignored_count > 0:
        print(f"Ignored {ignored_count} task(s) with specified IDs or not found in pairs directory")
    print(f"Found {len(task_pairs)} task pairs")

    task_categories = {}
    for task_base_id in task_pairs.keys():
        task_root, _ = find_task_in_pairs(pairs_dir, task_base_id)
        task_categories[task_base_id] = get_task_category(task_base_id, pairs_dir, task_root=task_root)

    subtype_stats = defaultdict(lambda: {"total": 0, "correct": 0})
    for task_id, result in all_results.items():
        task_base_id, _ = parse_task_id(task_id)
        subtype = task_categories.get(task_base_id, "unknown")
        subtype_stats[subtype]["total"] += 1
        if result.get("correct") is True:
            subtype_stats[subtype]["correct"] += 1
    
    total_tasks = len(all_results)
    correct_tasks = sum(1 for r in all_results.values() if r.get("correct") is True)
    incorrect_tasks = sum(1 for r in all_results.values() if r.get("correct") is False)
    error_tasks = sum(1 for r in all_results.values() if r.get("correct") is None)
    
    def normalize_bool(value):
        """Normalize different representations of booleans to a Python bool."""
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            return value.lower() in ["true", "1", "yes"]
        return False
    
    # Confusion matrix
    tp = 0  # True Positive: predicted true, ground truth true
    fp = 0  # False Positive: predicted true, ground truth false
    tn = 0  # True Negative: predicted false, ground truth false
    fn = 0  # False Negative: predicted false, ground truth true
    
    for result in all_results.values():
        verdict = normalize_bool(result.get("verdict"))
        ground_truth = normalize_bool(result.get("ground_truth"))
        
        if verdict and ground_truth:
            tp += 1
        elif verdict and not ground_truth:
            fp += 1
        elif not verdict and not ground_truth:
            tn += 1
        elif not verdict and ground_truth:
            fn += 1
    
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
    accuracy = (tp + tn) / (tp + fp + tn + fn) if (tp + fp + tn + fn) > 0 else 0.0
    
    if total_tasks == 0:
        print("Total tasks: 0. No tasks loaded; skipping further statistics.")
        return
    valid_results = correct_tasks + incorrect_tasks
    print("📊 Overall summary:")
    print(f"   Total results: {total_tasks}")
    print(f"   Valid judgments (with ground truth): {valid_results}")
    print(f"   Correct judgments: {correct_tasks}")
    print(f"   Failed or missing-result evaluations: {error_tasks}")
    print(f"   Accuracy: {accuracy*100:.2f}%  (Precision: {precision*100:.2f}%, Recall: {recall*100:.2f}%, F1: {f1_score*100:.2f}%)")
    print()

    print("📊 Subdomain summary:")
    for subtype in ["PPT", "Word", "Excel"]:
        stats = subtype_stats.get(subtype, {"total": 0, "correct": 0})
        total = stats["total"]
        correct = stats["correct"]
        if total == 0:
            print(f"   {subtype}: Correct=0, Total=0, F1=N/A")
        else:
            subtype_tp = 0
            subtype_fp = 0
            subtype_tn = 0
            subtype_fn = 0
            for task_id, result in all_results.items():
                task_base_id, _ = parse_task_id(task_id)
                if task_categories.get(task_base_id, "unknown") != subtype:
                    continue
                verdict = normalize_bool(result.get("verdict"))
                ground_truth = normalize_bool(result.get("ground_truth"))
                if verdict and ground_truth:
                    subtype_tp += 1
                elif verdict and not ground_truth:
                    subtype_fp += 1
                elif not verdict and not ground_truth:
                    subtype_tn += 1
                elif not verdict and ground_truth:
                    subtype_fn += 1
            subtype_f1 = 0.0
            if subtype_tp + subtype_fp > 0 and subtype_tp + subtype_fn > 0:
                sp = subtype_tp / (subtype_tp + subtype_fp)
                sr = subtype_tp / (subtype_tp + subtype_fn)
                subtype_f1 = 2 * sp * sr / (sp + sr) if (sp + sr) > 0 else 0.0
            acc_pct = correct / total * 100
            print(f"   {subtype}: Correct={correct}, Total={total}, Accuracy={acc_pct:.2f}%, F1={subtype_f1*100:.2f}%")
    if "unknown" in subtype_stats and subtype_stats["unknown"]["total"] > 0:
        s = subtype_stats["unknown"]
        print(f"   unknown: Correct={s['correct']}, Total={s['total']}")
    print()


def main():
    import argparse
    
    _default_pairs_dir = str(Path(__file__).resolve().parent.parent.parent / "data" / "GUI")
    parser = argparse.ArgumentParser(description="Analyze trajectory evaluation results.")
    parser.add_argument("--result_dir", type=str, default="./results", help="Directory containing evaluation results")
    parser.add_argument("--pairs_dir", type=str, default=_default_pairs_dir, help="Directory of pairs metadata, optional")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.result_dir):
        print(f"Error: result directory {args.result_dir} does not exist.")
        return
    
    analyze_results(args.result_dir, args.pairs_dir)


if __name__ == "__main__":
    main()
