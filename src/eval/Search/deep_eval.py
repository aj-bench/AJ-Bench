import glob
import json
import os
from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Tuple


def save_results_to_file(
    results: Dict, output_path: str, evaluator_type: str = "agent_judge"
):
    """
    Save evaluation results to a JSON file.

    Args:
        results: The evaluation results dictionary from get_results()
        output_path: Path to save the JSON file
        evaluator_type: Type of evaluator ("agent_judge" or "llm_judge")
    """
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Prepare output data
    output_data = {
        "evaluator_type": evaluator_type,
        "timestamp": datetime.now().isoformat(),
        "model_metrics": results.get("model_metrics", {}),
        "overall_metrics": results.get("overall_metrics", {}),
        "model_accuracies": results.get("model_accuracies", {}),
        "overall_accuracy": results.get("overall_accuracy", 0.0),
        "model_stats": results.get("model_stats", {}),
        "model_task_accuracies": results.get("model_task_accuracies", {}),
    }

    # Save to file
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)

    print(f"Results saved to: {output_path}")


def calculate_metrics(
    predictions: List[int], ground_truths: List[int]
) -> Dict[str, float]:
    """
    Calculate precision, recall, F1, and accuracy for binary classification.

    Args:
        predictions: List of predicted labels (0 or 1)
        ground_truths: List of ground truth labels (0 or 1)

    Returns:
        Dict with precision, recall, f1, accuracy
    """
    if len(predictions) != len(ground_truths) or len(predictions) == 0:
        return {
            "precision": 0.0,
            "recall": 0.0,
            "f1": 0.0,
            "accuracy": 0.0,
            "correct": 0,
            "total": len(predictions),
        }

    # Calculate TP, FP, TN, FN
    tp = sum(1 for pred, gt in zip(predictions, ground_truths) if pred == 1 and gt == 1)
    fp = sum(1 for pred, gt in zip(predictions, ground_truths) if pred == 1 and gt == 0)
    tn = sum(1 for pred, gt in zip(predictions, ground_truths) if pred == 0 and gt == 0)
    fn = sum(1 for pred, gt in zip(predictions, ground_truths) if pred == 0 and gt == 1)

    total = len(predictions)
    correct = tp + tn

    # Accuracy: (TP + TN) / Total
    accuracy = (correct / total * 100) if total > 0 else 0.0

    # Precision: TP / (TP + FP)
    precision = (tp / (tp + fp) * 100) if (tp + fp) > 0 else 0.0

    # Recall: TP / (TP + FN)
    recall = (tp / (tp + fn) * 100) if (tp + fn) > 0 else 0.0

    # F1: 2 * (Precision * Recall) / (Precision + Recall)
    f1 = (
        (2 * precision * recall / (precision + recall))
        if (precision + recall) > 0
        else 0.0
    )

    return {
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "accuracy": accuracy,
        "correct": correct,
        "total": total,
        "tp": tp,
        "fp": fp,
        "tn": tn,
        "fn": fn,
    }


class AgentJudge_Mind2Web2Evaluator:
    def __init__(self, base_path: str, models: list = None, task_ids: list = None):
        """
        Args:
            base_path: Path to results directory
            models: List of model names to evaluate (e.g., ["Gemini", "Grok"])
                    If None, evaluates all models found
        """
        self.base_path = base_path
        self.models = models  # None means evaluate all models
        self.task_ids = set(task_ids) if task_ids else None
        self.model_stats = defaultdict(
            lambda: {"correct": 0, "total": 0, "tasks": defaultdict(list)}
        )
        self.task_stats = {}
        # {model: {task_id: [results]}}
        self.model_task_results = defaultdict(lambda: defaultdict(list))

    def _parse_directory_name(self, dir_name: str) -> Tuple[str, str, str, str]:
        """Parse directory name to extract task_id, model_name, and row_info"""
        # Example: Mind2Web2-Gemini-2024_film_premiere__2024_film_premiere-Gemini-row_1
        parts = dir_name.split("__")
        if len(parts) < 2:
            return None, None, None, None

        # parts[0] = Mind2Web2-Gemini-2024_film_premiere
        # parts[1] = 2024_film_premiere-Gemini-row_1

        # Extract model from the beginning: Mind2Web2-{model}-{task_id}
        prefix_parts = parts[0].split("-", 2)  # Split into at most 3 parts
        if len(prefix_parts) < 3:
            return None, None, None, None

        model_name = prefix_parts[1]  # Gemini
        task_id = prefix_parts[2]  # 2024_film_premiere

        # Extract row_info from parts[1]: {task_id}-{model}-row_{num}
        # We want the full row part: row_1
        row_parts = parts[1].rsplit("-", 1)
        if len(row_parts) < 2:
            return None, None, None, None
        row_info = row_parts[1]  # row_1

        # task_key is the full directory name minus row info
        task_key = f"Mind2Web2-{model_name}-{task_id}"

        return task_key, task_id, model_name, row_info

    def _load_verification_data(self, verification_file: str) -> Dict:
        with open(verification_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def collect_results(self):
        task_dirs = glob.glob(os.path.join(self.base_path, "Mind2Web2-*-*__*-row_*"))

        for task_dir in sorted(task_dirs):
            verification_file = os.path.join(task_dir, "verification_summary.json")

            if not os.path.exists(verification_file):
                raise ValueError(f"Verification file not found: {verification_file}")

            try:
                dir_name = os.path.basename(task_dir)
                task_key, task_id, model_name, row_info = self._parse_directory_name(
                    dir_name
                )

                # Skip if parsing failed
                if task_id is None:
                    print(f"Warning: Could not parse directory name: {dir_name}")
                    continue

                # Skip if model not in the list of models to evaluate
                if self.models is not None and model_name not in self.models:
                    print(
                        f"Warning: Skipping model {model_name} not in evaluation list"
                    )
                    continue

                # Skip if task_id not in the whitelist
                if self.task_ids is not None and task_id not in self.task_ids:
                    print(f"Warning: Skipping task_id {task_id} not in evaluation list")
                    continue

                data = self._load_verification_data(verification_file)
                match = data.get("match", False)

                if task_key not in self.task_stats:
                    self.task_stats[task_key] = []

                self.task_stats[task_key].append(
                    {
                        "row": row_info,
                        "match": match,
                        "ground_truth": data.get("ground_truth_label"),
                        "extracted": data.get("extracted_label"),
                    }
                )

                # Store results by model and task_id
                self.model_task_results[model_name][task_id].append(
                    {
                        "row": row_info,
                        "task_key": task_key,
                        "match": match,
                        "ground_truth": data.get("ground_truth_label"),
                        "extracted": data.get("extracted_label"),
                    }
                )

                self.model_stats[model_name]["total"] += 1
                if match:
                    self.model_stats[model_name]["correct"] += 1
                self.model_stats[model_name]["tasks"][task_key].append(match)

            except Exception as e:
                print(f"Error processing {verification_file}: {e}")

    def calculate_model_metrics(self) -> Dict[str, Dict[str, float]]:
        """Calculate precision, recall, F1, and accuracy for each model"""
        metrics = {}
        # Use specified models or all models found in results
        models_to_evaluate = (
            self.models if self.models is not None else ["Gemini", "Grok", "Perplexity"]
        )

        for model_name in models_to_evaluate:
            if model_name in self.model_stats:
                stats = self.model_stats[model_name]
                if stats["total"] > 0:
                    # Collect extracted and ground truth labels for this model
                    predictions = []
                    ground_truths = []
                    for task_results in self.model_task_results[model_name].values():
                        for r in task_results:
                            extracted = r["extracted"]
                            gt = r["ground_truth"]
                            # If extracted is None/null, treat as wrong prediction
                            if extracted is None:
                                # Predict opposite of ground truth to ensure error
                                extracted = 1 - gt if gt in [0, 1] else 0
                            predictions.append(extracted)
                            ground_truths.append(gt)
                    metrics[model_name] = calculate_metrics(predictions, ground_truths)
                else:
                    metrics[model_name] = {
                        "precision": 0.0,
                        "recall": 0.0,
                        "f1": 0.0,
                        "accuracy": 0.0,
                        "correct": 0,
                        "total": 0,
                    }
            else:
                metrics[model_name] = {
                    "precision": 0.0,
                    "recall": 0.0,
                    "f1": 0.0,
                    "accuracy": 0.0,
                    "correct": 0,
                    "total": 0,
                }
        return metrics

    def calculate_model_accuracies(self) -> Dict[str, float]:
        """Legacy method for backward compatibility"""
        metrics = self.calculate_model_metrics()
        return {model: m["accuracy"] for model, m in metrics.items()}

    def calculate_overall_metrics(self) -> Dict[str, float]:
        """Calculate overall precision, recall, F1, and accuracy"""
        all_predictions = []
        all_ground_truths = []
        for model_results in self.model_task_results.values():
            for task_results in model_results.values():
                for r in task_results:
                    extracted = r["extracted"]
                    gt = r["ground_truth"]
                    # If extracted is None/null, treat as wrong prediction
                    if extracted is None:
                        # Predict opposite of ground truth to ensure error
                        extracted = 1 - gt if gt in [0, 1] else 0
                    all_predictions.append(extracted)
                    all_ground_truths.append(gt)
        return calculate_metrics(all_predictions, all_ground_truths)

    def calculate_overall_accuracy(self) -> float:
        """Legacy method for backward compatibility"""
        return self.calculate_overall_metrics()["accuracy"]

    def get_task_accuracy_by_model(self, model_name: str) -> Dict[str, Dict]:
        """Get accuracy for each task_id for a specific model"""
        task_accuracies = {}
        for task_id, results in self.model_task_results[model_name].items():
            correct = sum(1 for r in results if r["match"])
            total = len(results)
            task_accuracies[task_id] = {
                "correct": correct,
                "total": total,
                "accuracy": (correct / total * 100) if total > 0 else 0.0,
                "results": results,
            }
        return task_accuracies

    def get_results(self) -> Dict:
        model_metrics = self.calculate_model_metrics()
        overall_metrics = self.calculate_overall_metrics()
        model_accuracies = {model: m["accuracy"] for model, m in model_metrics.items()}
        overall_accuracy = overall_metrics["accuracy"]

        # Get task-level results for each model
        model_task_accuracies = {}
        for model_name in self.model_task_results.keys():
            model_task_accuracies[model_name] = self.get_task_accuracy_by_model(
                model_name
            )

        return {
            "model_accuracies": model_accuracies,
            "model_metrics": model_metrics,
            "overall_accuracy": overall_accuracy,
            "overall_metrics": overall_metrics,
            "model_stats": dict(self.model_stats),
            "task_stats": self.task_stats,
            "model_task_results": dict(self.model_task_results),
            "model_task_accuracies": model_task_accuracies,
        }


class LLMJudge_Mind2Web2Evaluator:
    def __init__(
        self, result_files: Dict[str, str], models: list = None, task_ids: list = None
    ):
        """
        Args:
            result_files: Dict mapping model names to result file paths
            e.g., {"Gemini": "path/to/gemini.json", "Grok": "path/to/grok.json", ...}
            models: List of model names to evaluate (e.g., ["Gemini", "Grok"])
                    If None, evaluates all models in result_files
        """
        self.result_files = result_files
        self.models = models  # None means evaluate all models
        self.task_ids = set(task_ids) if task_ids else None
        self.model_task_results = defaultdict(
            lambda: defaultdict(list)
        )  # {model: {task_id: [results]}}
        self.model_stats = defaultdict(lambda: {"correct": 0, "total": 0})

    def _load_result(self, file_path: str) -> Dict:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _parse_entry_id(self, entry_id: str) -> Tuple[str, str, str]:
        """Parse entry_id to extract task_id, model, and row_num"""
        # Example: ws_en_067-Gemini-row_1
        parts = entry_id.rsplit("-row_", 1)
        if len(parts) != 2:
            return None, None, None

        task_model = parts[0]  # ws_en_067-Gemini
        row_num = parts[1]  # 1

        # Extract task_id and model
        task_parts = task_model.rsplit("-", 1)
        if len(task_parts) != 2:
            return None, None, None

        task_id = task_parts[0]  # ws_en_067
        model = task_parts[1]  # Gemini

        return task_id, model, row_num

    def collect_results(self):
        for model_name, result_file in self.result_files.items():
            # Skip if model not in the list of models to evaluate
            if self.models is not None and model_name not in self.models:
                continue

            llm_result = self._load_result(result_file)

            for entry in llm_result.get("detailed_results", []):
                entry_id = entry.get("entry_id", "")
                task_id, model, row_num = self._parse_entry_id(entry_id)

                if task_id is None:
                    continue

                if self.task_ids is not None and task_id not in self.task_ids:
                    continue

                extracted_label = entry.get("extracted_label")
                ground_truth = entry.get("ground_truth")
                is_correct = entry.get("is_correct", False)

                # Store results by model and task_id
                self.model_task_results[model][task_id].append(
                    {
                        "row": f"row_{row_num}",
                        "entry_id": entry_id,
                        "match": is_correct,
                        "ground_truth": ground_truth,
                        "extracted": extracted_label,
                    }
                )

                # Update statistics
                self.model_stats[model]["total"] += 1
                if is_correct:
                    self.model_stats[model]["correct"] += 1

    def calculate_model_metrics(self) -> Dict[str, Dict[str, float]]:
        """Calculate precision, recall, F1, and accuracy for each model"""
        metrics = {}
        # Use specified models or all models found in results
        models_to_evaluate = (
            self.models if self.models is not None else ["Gemini", "Grok", "Perplexity"]
        )

        for model_name in models_to_evaluate:
            if model_name in self.model_stats:
                stats = self.model_stats[model_name]
                if stats["total"] > 0:
                    # Collect extracted and ground truth labels for this model
                    predictions = []
                    ground_truths = []
                    for task_results in self.model_task_results[model_name].values():
                        for r in task_results:
                            extracted = r["extracted"]
                            gt = r["ground_truth"]
                            # If extracted is None/null, treat as wrong prediction
                            if extracted is None:
                                # Predict opposite of ground truth to ensure error
                                extracted = 1 - gt if gt in [0, 1] else 0
                            predictions.append(extracted)
                            ground_truths.append(gt)
                    metrics[model_name] = calculate_metrics(predictions, ground_truths)
                else:
                    metrics[model_name] = {
                        "precision": 0.0,
                        "recall": 0.0,
                        "f1": 0.0,
                        "accuracy": 0.0,
                        "correct": 0,
                        "total": 0,
                    }
            else:
                metrics[model_name] = {
                    "precision": 0.0,
                    "recall": 0.0,
                    "f1": 0.0,
                    "accuracy": 0.0,
                    "correct": 0,
                    "total": 0,
                }
        return metrics

    def calculate_model_accuracies(self) -> Dict[str, float]:
        """Legacy method for backward compatibility"""
        metrics = self.calculate_model_metrics()
        return {model: m["accuracy"] for model, m in metrics.items()}

    def calculate_overall_metrics(self) -> Dict[str, float]:
        """Calculate overall precision, recall, F1, and accuracy"""
        all_predictions = []
        all_ground_truths = []
        for model_results in self.model_task_results.values():
            for task_results in model_results.values():
                for r in task_results:
                    extracted = r["extracted"]
                    gt = r["ground_truth"]
                    # If extracted is None/null, treat as wrong prediction
                    if extracted is None:
                        # Predict opposite of ground truth to ensure error
                        extracted = 1 - gt if gt in [0, 1] else 0
                    all_predictions.append(extracted)
                    all_ground_truths.append(gt)
        return calculate_metrics(all_predictions, all_ground_truths)

    def calculate_overall_accuracy(self) -> float:
        """Legacy method for backward compatibility"""
        return self.calculate_overall_metrics()["accuracy"]

    def get_task_accuracy_by_model(self, model_name: str) -> Dict[str, Dict]:
        """Get accuracy for each task_id for a specific model"""
        task_accuracies = {}
        for task_id, results in self.model_task_results[model_name].items():
            correct = sum(1 for r in results if r["match"])
            total = len(results)
            task_accuracies[task_id] = {
                "correct": correct,
                "total": total,
                "accuracy": (correct / total * 100) if total > 0 else 0.0,
                "results": results,
            }
        return task_accuracies

    def get_results(self) -> Dict:
        model_metrics = self.calculate_model_metrics()
        overall_metrics = self.calculate_overall_metrics()
        model_accuracies = {model: m["accuracy"] for model, m in model_metrics.items()}
        overall_accuracy = overall_metrics["accuracy"]

        # Get task-level results for each model
        model_task_accuracies = {}
        for model_name in self.model_task_results.keys():
            model_task_accuracies[model_name] = self.get_task_accuracy_by_model(
                model_name
            )

        return {
            "model_accuracies": model_accuracies,
            "model_metrics": model_metrics,
            "overall_accuracy": overall_accuracy,
            "overall_metrics": overall_metrics,
            "model_stats": dict(self.model_stats),
            "model_task_results": dict(self.model_task_results),
            "model_task_accuracies": model_task_accuracies,
        }


def main_agent_judge(
    base_path: str, models: list = None, task_ids: list = None, output_path: str = None
):
    """
    Evaluate Agent Judge results

    Args:
        base_path: Path to Agent Judge results directory
        models: List of model names to evaluate (e.g., ["Gemini", "Grok"])
                If None, evaluates all models
        task_ids: List of task_ids to evaluate; if None, evaluate all
        output_path: Path to save results JSON file; if None, no file is saved
    """
    if base_path is None:
        raise ValueError("base_path is required for agent judge evaluation")

    evaluator = AgentJudge_Mind2Web2Evaluator(
        base_path, models=models, task_ids=task_ids
    )
    evaluator.collect_results()
    results = evaluator.get_results()

    # Save results if output_path is provided
    if output_path:
        save_results_to_file(results, output_path, "agent_judge")

    print("=" * 60)
    print("AGENT JUDGE EVALUATION RESULTS")
    print("=" * 60)

    # Get models to display (use specified models or all found models)
    models_to_display = (
        models if models is not None else sorted(results["model_accuracies"].keys())
    )

    # Print results for each model
    for model_name in models_to_display:
        print(f"\n{'=' * 60}")
        print(f"MODEL: {model_name}")
        print(f"{'=' * 60}")

        model_task_accuracies = results["model_task_accuracies"].get(model_name, {})

        if not model_task_accuracies:
            print(f"No results found for {model_name}")
            continue

        # Print task-level results
        for task_id in sorted(model_task_accuracies.keys()):
            task_info = model_task_accuracies[task_id]
            print(f"\nTask: {task_id}")
            print(
                f"  Accuracy: {task_info['correct']}/{task_info['total']} ({task_info['accuracy']:.2f}%)"
            )

            # Show detailed results for each row
            for row_result in sorted(task_info["results"], key=lambda x: x["row"]):
                status = "✅" if row_result["match"] else "❌"
                print(
                    f"    {status} {row_result['row']}: GT={row_result['ground_truth']}, Pred={row_result['extracted']}"
                )

        # Print model summary
        model_accuracy = results["model_accuracies"][model_name]
        print(f"\n{model_name} Overall Accuracy: {model_accuracy:.2f}%")

    # Print overall statistics
    print(f"\n{'=' * 60}")
    print("OVERALL STATISTICS")
    print(f"{'=' * 60}")
    for model_name in models_to_display:
        if model_name in results["model_accuracies"]:
            print(f"{model_name}: {results['model_accuracies'][model_name]:.2f}%")
    print(f"Overall: {results['overall_accuracy']:.2f}%")


def main_llm_judge(
    result_files: Dict[str, str],
    models: list = None,
    task_ids: list = None,
    output_path: str = None,
):
    """
    Evaluate LLM Judge results

    Args:
        result_files: Dict mapping model names to result file paths
        models: List of model names to evaluate (e.g., ["Gemini", "Grok"])
                If None, evaluates all models in result_files
        task_ids: List of task_ids to evaluate; if None, evaluate all
        output_path: Path to save results JSON file; if None, no file is saved
    """
    if not result_files:
        raise ValueError("result_files is required for llm judge evaluation")

    evaluator = LLMJudge_Mind2Web2Evaluator(
        result_files, models=models, task_ids=task_ids
    )
    evaluator.collect_results()
    results = evaluator.get_results()

    # Save results if output_path is provided
    if output_path:
        save_results_to_file(results, output_path, "llm_judge")

    print("=" * 60)
    print("LLM JUDGE EVALUATION RESULTS")
    print("=" * 60)

    # Get models to display (use specified models or all found models)
    models_to_display = (
        models if models is not None else sorted(results["model_accuracies"].keys())
    )

    # Print results for each model
    for model_name in models_to_display:
        print(f"\n{'=' * 60}")
        print(f"MODEL: {model_name}")
        print(f"{'=' * 60}")

        model_task_accuracies = results["model_task_accuracies"].get(model_name, {})

        if not model_task_accuracies:
            print(f"No results found for {model_name}")
            continue

        # Print task-level results
        for task_id in sorted(model_task_accuracies.keys()):
            task_info = model_task_accuracies[task_id]
            print(f"\nTask: {task_id}")
            print(
                f"  Accuracy: {task_info['correct']}/{task_info['total']} ({task_info['accuracy']:.2f}%)"
            )

            # Show detailed results for each row
            for row_result in sorted(task_info["results"], key=lambda x: x["row"]):
                status = "✅" if row_result["match"] else "❌"
                print(
                    f"    {status} {row_result['row']}: GT={row_result['ground_truth']}, Pred={row_result['extracted']}"
                )

        # Print model summary
        model_accuracy = results["model_accuracies"][model_name]
        print(f"\n{model_name} Overall Accuracy: {model_accuracy:.2f}%")

    # Print overall statistics
    print(f"\n{'=' * 60}")
    print("OVERALL STATISTICS")
    print(f"{'=' * 60}")
    for model_name in models_to_display:
        if model_name in results["model_accuracies"]:
            print(f"{model_name}: {results['model_accuracies'][model_name]:.2f}%")
    print(f"Overall: {results['overall_accuracy']:.2f}%")


def compare_evaluators(
    base_path: str,
    result_files: Dict[str, str],
    models: list = None,
    task_ids: list = None,
    agent_output_path: str = None,
    llm_output_path: str = None,
):
    """
    Compare Agent Judge and LLM Judge results side by side

    Args:
        models: List of model names to evaluate (e.g., ["Gemini", "Grok"])
                If None, evaluates ["Gemini"]
        base_path: Path to Agent Judge results directory
        result_files: Dict mapping model names to result file paths
        task_ids: List of task_ids to evaluate; if None, evaluate all
        agent_output_path: Path to save Agent Judge results; if None, no file is saved
        llm_output_path: Path to save LLM Judge results; if None, no file is saved
    """
    if models is None:
        models = ["Gemini"]  # Default to Gemini only

    if base_path is None:
        raise ValueError("base_path is required for comparison")
    if not result_files:
        raise ValueError("result_files is required for comparison")

    # Agent Judge setup
    agent_evaluator = AgentJudge_Mind2Web2Evaluator(
        base_path, models=models, task_ids=task_ids
    )
    agent_evaluator.collect_results()
    agent_results = agent_evaluator.get_results()

    # Save Agent Judge results if output_path is provided
    if agent_output_path:
        save_results_to_file(agent_results, agent_output_path, "agent_judge")

    # LLM Judge setup
    llm_evaluator = LLMJudge_Mind2Web2Evaluator(
        result_files, models=models, task_ids=task_ids
    )
    llm_evaluator.collect_results()
    llm_results = llm_evaluator.get_results()

    # Save LLM Judge results if output_path is provided
    if llm_output_path:
        save_results_to_file(llm_results, llm_output_path, "llm_judge")

    print("=" * 100)
    print("COMPARATIVE EVALUATION: AGENT JUDGE vs LLM JUDGE")
    print("=" * 100)

    # Compare each model
    for model_name in models:
        print(f"\n{'=' * 100}")
        print(f"MODEL: {model_name}")
        print(f"{'=' * 100}")

        agent_task_accuracies = agent_results["model_task_accuracies"].get(
            model_name, {}
        )
        llm_task_accuracies = llm_results["model_task_accuracies"].get(model_name, {})

        if not agent_task_accuracies and not llm_task_accuracies:
            print(f"No results found for {model_name}")
            continue

        # Get all unique task_ids from both evaluators
        all_task_ids = set(agent_task_accuracies.keys()) | set(
            llm_task_accuracies.keys()
        )

        # Print task-level comparison
        for task_id in sorted(all_task_ids):
            agent_task = agent_task_accuracies.get(task_id, {})
            llm_task = llm_task_accuracies.get(task_id, {})

            print(f"\n┌─ Task: {task_id} {'─' * (85 - len(task_id))}")

            # Print accuracy comparison
            agent_acc = agent_task.get("accuracy", 0.0)
            llm_acc = llm_task.get("accuracy", 0.0)
            agent_stats = f"{agent_task.get('correct', 0)}/{agent_task.get('total', 0)}"
            llm_stats = f"{llm_task.get('correct', 0)}/{llm_task.get('total', 0)}"

            print(f"│ Agent Judge: {agent_stats:>6} ({agent_acc:>6.2f}%)")
            print(f"│ LLM Judge:   {llm_stats:>6} ({llm_acc:>6.2f}%)")
            print(f"│ Difference:  {agent_acc - llm_acc:>6.2f}%")

            # Get all unique rows
            agent_results_dict = {r["row"]: r for r in agent_task.get("results", [])}
            llm_results_dict = {r["row"]: r for r in llm_task.get("results", [])}
            all_rows = set(agent_results_dict.keys()) | set(llm_results_dict.keys())

            print("│")
            print(
                f"│ {'Row':8} │ {'Agent Judge':15} │ {'LLM Judge':15} │ {'Match':7} │ GT → Pred"
            )
            print(f"│ {'-' * 8}─┼─{'-' * 15}─┼─{'-' * 15}─┼─{'-' * 7}─┼─{'-' * 30}")

            for row in sorted(all_rows):
                agent_row = agent_results_dict.get(row, {})
                llm_row = llm_results_dict.get(row, {})

                agent_match = agent_row.get("match", False)
                llm_match = llm_row.get("match", False)

                agent_status = "✅" if agent_match else "❌"
                llm_status = "✅" if llm_match else "❌"

                # Check if both evaluators agree
                if agent_row and llm_row:
                    if agent_match == llm_match:
                        match_status = "✅ Agree"
                    else:
                        match_status = "⚠️ Differ"
                elif agent_row:
                    match_status = "A only"
                elif llm_row:
                    match_status = "L only"
                else:
                    match_status = "N/A"

                # Get ground truth and predictions
                gt = agent_row.get("ground_truth") or llm_row.get("ground_truth", "N/A")
                agent_pred = agent_row.get("extracted", "-")
                llm_pred = llm_row.get("extracted", "-")

                print(
                    f"│ {row:8} │ {agent_status:>15} │ {llm_status:>15} │ {match_status:7} │ {gt} → A:{agent_pred}, L:{llm_pred}"
                )

            print(f"└{'─' * 98}")

        # Print model summary with all metrics
        agent_metrics = agent_results["model_metrics"].get(model_name, {})
        llm_metrics = llm_results["model_metrics"].get(model_name, {})

        print(f"\n{'─' * 100}")
        print(f"{model_name} Overall Summary:")
        print(
            f"  {'Metric':12} │ {'Agent Judge':>12} │ {'LLM Judge':>12} │ {'Difference':>12}"
        )
        print(f"  {'-' * 12}─┼─{'-' * 12}─┼─{'-' * 12}─┼─{'-' * 12}")
        for metric in ["precision", "recall", "f1", "accuracy"]:
            agent_val = agent_metrics.get(metric, 0.0)
            llm_val = llm_metrics.get(metric, 0.0)
            diff = agent_val - llm_val
            print(
                f"  {metric.capitalize():12} │ {agent_val:>11.2f}% │ {llm_val:>11.2f}% │ {diff:>+11.2f}%"
            )

    # Print overall statistics comparison
    print(f"\n{'=' * 100}")
    print("OVERALL STATISTICS COMPARISON")
    print(f"{'=' * 100}")

    # Print header for all metrics
    print(
        f"\n{'Model':12} │ {'Metric':12} │ {'Agent Judge':>12} │ {'LLM Judge':>12} │ {'Difference':>12}"
    )
    print(f"{'-' * 12}─┼─{'-' * 12}─┼─{'-' * 12}─┼─{'-' * 12}─┼─{'-' * 12}")

    for model_name in models:
        agent_metrics = agent_results["model_metrics"].get(model_name, {})
        llm_metrics = llm_results["model_metrics"].get(model_name, {})
        for i, metric in enumerate(["precision", "recall", "f1", "accuracy"]):
            agent_val = agent_metrics.get(metric, 0.0)
            llm_val = llm_metrics.get(metric, 0.0)
            diff = agent_val - llm_val
            model_col = model_name if i == 0 else ""
            print(
                f"{model_col:12} │ {metric.capitalize():12} │ {agent_val:>11.2f}% │ {llm_val:>11.2f}% │ {diff:>+11.2f}%"
            )
        print(f"{'-' * 12}─┼─{'-' * 12}─┼─{'-' * 12}─┼─{'-' * 12}─┼─{'-' * 12}")

    # Print overall metrics
    agent_overall = agent_results["overall_metrics"]
    llm_overall = llm_results["overall_metrics"]
    print(
        f"\n{'Overall':12} │ {'Metric':12} │ {'Agent Judge':>12} │ {'LLM Judge':>12} │ {'Difference':>12}"
    )
    print(f"{'-' * 12}─┼─{'-' * 12}─┼─{'-' * 12}─┼─{'-' * 12}─┼─{'-' * 12}")
    for metric in ["precision", "recall", "f1", "accuracy"]:
        agent_val = agent_overall.get(metric, 0.0)
        llm_val = llm_overall.get(metric, 0.0)
        diff = agent_val - llm_val
        print(
            f"{'':12} │ {metric.capitalize():12} │ {agent_val:>11.2f}% │ {llm_val:>11.2f}% │ {diff:>+11.2f}%"
        )
    print("=" * 100)


if __name__ == "__main__":
    # ========================================
    # Configuration: Choose models to evaluate
    # ========================================
    # Options:
    # - ["Gemini"] - Evaluate only Gemini
    # - ["Gemini", "Grok"] - Evaluate Gemini and Grok
    # - ["Gemini", "Grok", "Perplexity"] - Evaluate all three models
    # - None - Evaluate all models found in results

    MODELS_TO_EVALUATE = ["Gemini", "Grok", "Perplexity"]

    TASK_IDS = [
        "2024_film_premiere",
        "active_stock",
        "ad_patent",
        "apple_watch",
        "artifact_repatriation",
        "buy_kobe_shoes_reverse_swoosh",
        "captain_america_starring",
        "chinese_dish",
        "chris_evans",
        "closet_picks",
        "county_AQI",
        "cyberpunk_music",
        "dc_comics_injustice",
        "drone_delivery",
        "esport_player",
        "female_scholarships",
        "find_parks",
        "game_awards",
        "gcg_followup",
        "goodreads_winner",
        "hf_vqa_dataset",
        "hypeawards_twice_brand",
        "instrument_in_met",
        "jojo_references",
        "just_bieber_friend",
        "marvel_rivals",
        "meditation_app",
        "mllm_researcher",
        "nba_career_high",
        "nba_player_china_tour",
        "nlp_faculty",
        "openreview_papers",
        "origami_chinese_zodiac",
        "overleaf_template",
        "paper_collaboration",
        "perplexity_failure",
        "plan_nlp_learning",
        "plants_italy",
        "popular_ai_books",
        "pritzker_prize_winner",
        "protein_vis_software",
        "rare_disease",
        "rhone_top_wine",
        "rl_course_book",
        "startups_series_b",
        "supreme_court_230",
        "telescopes_list",
        "tesla_travel",
        "tofu_lunch",
        "tokyo_filming_location",
        "wssa_female_65",
        "yu_lineage",
    ]

    JUDGE_MODELS_LIST = [
        "claude-opus-4.5",
        "claude-sonnet-4.5",
        "deepseek-chat",
        "gemini-2.5-pro",
        "gemini-3-pro-preview",
        "glm-4.6",
        "gpt-5-mini-low",
        "gpt-5.1",
        "grok-4",
        "kimi-k2-0905-preview",
        "LongCat-Flash-Chat",
        "qwen3-235b-a22b",
    ]

    RUN_ID_LIST = [
        "run-1",
        "run-2",
        "run-3",
    ]

    #! Agent-as-a-Judge Evaluation
    BASE_PATH = "results/Mind2Web2/debug/gpt-5-mini-low__playwright/run-1"
    RESULT_FILES = {
        "Gemini": "results/Mind2Web2/debug/llm-as-a-judge/Gemini/run-1/result-glm-4.6__llm_as_a_judge-run-1.json",
        "Grok": "results/Mind2Web2/debug/llm-as-a-judge/Grok/run-1/result-glm-4.6__llm_as_a_judge-run-1.json",
        "Perplexity": "results/Mind2Web2/debug/llm-as-a-judge/Perplexity/run-1/result-glm-4.6__llm_as_a_judge-run-1.json",
    }

    # Run comparison and save results
    compare_evaluators(
        base_path=BASE_PATH,
        result_files=RESULT_FILES,
        models=MODELS_TO_EVALUATE,
        task_ids=TASK_IDS,
        agent_output_path="results/Mind2Web2/debug/eval_results/run-1/gpt-5-mini-low.json",
        llm_output_path="results/Mind2Web2/debug/llm-as-a-judge/eval_results/run-1/glm-4.6.json",
    )

    #! LLM-as-a-Judge Evaluation
    # BASE_PATH = "results/Mind2Web2/debug/deepseek-chat__playwright/run-3"
    # for judge_model in JUDGE_MODELS_LIST:
    #     for run_id in RUN_ID_LIST:
    #         RESULT_FILES = {}
    #         for model in MODELS_TO_EVALUATE:
    #             RESULT_FILES[model] = (
    #                 f"results/Mind2Web2/debug/llm-as-a-judge/{model}/{run_id}/result-{judge_model}__llm_as_a_judge-{run_id}.json"
    #             )
    #         compare_evaluators(
    #             base_path=BASE_PATH,
    #             result_files=RESULT_FILES,
    #             models=MODELS_TO_EVALUATE,
    #             task_ids=TASK_IDS,
    #             llm_output_path=f"results/Mind2Web2/debug/llm-as-a-judge/eval_results/{run_id}/{judge_model}.json",
    #         )
