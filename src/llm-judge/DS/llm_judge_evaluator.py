"""
LLM-as-a-Judge Evaluator for MCPMark

This script performs parallel evaluation of agent trajectories using ChatGPT API.
It compares the LLM judge's results with the ground truth labels and calculates success rates.
"""

import os
import json
import asyncio
import argparse
from pathlib import Path
from dataclasses import dataclass
from typing import Optional
import time
from dotenv import load_dotenv
from datetime import datetime

from openai import AsyncOpenAI
from prompt_mcpmark_llmjudge_single import DEFAULT_AGENT_JUDGE_WIDESEARCH_PROMPT


@dataclass
class EvaluationResult:
    """Stores the evaluation result for a single trajectory."""

    task_path: str
    trajectory_path: str
    ground_truth: str  # "success" or "fail"
    llm_judgment: Optional[str] = None  # "PASS" or "FAIL"
    raw_response: Optional[str] = None
    error: Optional[str] = None
    is_correct: Optional[bool] = None  # Whether LLM judgment matches ground truth


@dataclass
class EvaluationStats:
    """Stores aggregate statistics for the evaluation."""

    total: int = 0
    correct: int = 0
    incorrect: int = 0
    errors: int = 0

    # Breakdown by ground truth
    true_positives: int = 0  # Ground truth: success, LLM: PASS
    true_negatives: int = 0  # Ground truth: fail, LLM: FAIL
    false_positives: int = 0  # Ground truth: fail, LLM: PASS
    false_negatives: int = 0  # Ground truth: success, LLM: FAIL

    @property
    def accuracy(self) -> float:
        if self.total - self.errors == 0:
            return 0.0
        return self.correct / (self.total - self.errors)

    @property
    def precision(self) -> float:
        if self.true_positives + self.false_positives == 0:
            return 0.0
        return self.true_positives / (self.true_positives + self.false_positives)

    @property
    def recall(self) -> float:
        if self.true_positives + self.false_negatives == 0:
            return 0.0
        return self.true_positives / (self.true_positives + self.false_negatives)

    @property
    def f1_score(self) -> float:
        if self.precision + self.recall == 0:
            return 0.0
        return 2 * (self.precision * self.recall) / (self.precision + self.recall)


class LLMJudgeEvaluator:
    """Main evaluator class for LLM-as-a-Judge evaluation."""

    def __init__(
        self,
        base_dir: str,
        tasks_dir: str = "tasks",
        trajectory_dir: str = "mcpmark-trajectory-log/mcpmark-selected",
        model: str = "gpt-4o",
        max_concurrent: int = 10,
        max_tasks: Optional[int] = None,
        reasoning_effort: Optional[str] = None,
        category: Optional[str] = None,
        file_name: Optional[str] = None,
    ):
        self.base_dir = Path(base_dir)
        self.tasks_dir = self.base_dir / tasks_dir
        self.trajectory_dir = self.base_dir / trajectory_dir
        self.model = model
        self.max_concurrent = max_concurrent
        self.max_tasks = max_tasks
        self.reasoning_effort = reasoning_effort
        self.category = category
        self.file_name = file_name

        # Initialize OpenAI client
        self.client = AsyncOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_BASE_URL"),
        )

        self.results: list[EvaluationResult] = []
        self.stats = EvaluationStats()

    def find_task_description(self, task_path: str) -> Optional[str]:
        """
        Find and read the task description for a given task path.

        task_path format: category/subcategory__task_name
        e.g., filesystem/desktop__music_report -> tasks/filesystem/desktop/music_report/description.md
        """
        parts = task_path.split("/")
        if len(parts) != 2:
            return None

        category = parts[0]
        task_parts = parts[1].split("__")
        if len(task_parts) != 2:
            return None

        subcategory = task_parts[0]
        task_name = task_parts[1]

        description_path = (
            self.tasks_dir / category / subcategory / task_name / "description.md"
        )

        if description_path.exists():
            return description_path.read_text(encoding="utf-8")

        return None

    def load_trajectory(self, trajectory_path: Path) -> Optional[str]:
        """Load and format the trajectory from messages.json."""
        messages_path = trajectory_path / "messages.json"

        if not messages_path.exists():
            return None

        try:
            with open(messages_path, "r", encoding="utf-8") as f:
                messages = json.load(f)

            # Format the trajectory as a readable string
            # Skip the last message if it's from assistant
            if messages and messages[-1].get("role") == "assistant":
                messages = messages[:-1]

            trajectory_parts = []
            for msg in messages:
                if msg.get("role") == "user":
                    # trajectory_parts.append(f"[USER]: {msg.get('content', '')}")
                    pass  # Skip user messages
                elif msg.get("role") == "assistant":
                    content = msg.get("content", [])
                    if isinstance(content, list):
                        for c in content:
                            if isinstance(c, dict) and c.get("type") == "output_text":
                                trajectory_parts.append(
                                    f"[ASSISTANT]: {c.get('text', '')}"
                                )
                    elif isinstance(content, str):
                        trajectory_parts.append(f"[ASSISTANT]: {content}")
                elif msg.get("type") == "function_call":
                    name = msg.get("name", "unknown")
                    args = msg.get("arguments", "{}")
                    trajectory_parts.append(f"[FUNCTION CALL] {name}: {args}")
                elif msg.get("type") == "function_call_output":
                    # output = msg.get("output", "")
                    # # Truncate long outputs
                    # if len(output) > 1000:
                    #     output = output[:1000] + "... [truncated]"
                    # trajectory_parts.append(f"[FUNCTION OUTPUT]: {output}")
                    pass  # Skip function call outputs

            return "\n\n".join(trajectory_parts)
        except Exception as e:
            print(f"Error loading trajectory from {trajectory_path}: {e}")
            return None

    async def evaluate_single(
        self, task_description: str, trajectory: str
    ) -> tuple[str, str]:
        """
        Call the LLM API to evaluate a single trajectory.
        Returns (judgment, raw_response).
        """
        prompt = DEFAULT_AGENT_JUDGE_WIDESEARCH_PROMPT.format(
            task=task_description, trajectory=trajectory
        )

        try:
            # Build API request parameters
            api_params = {
                "model": self.model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0,
                "max_tokens": 8192,
            }

            # Add reasoning_effort if specified (for models that support it)
            if self.reasoning_effort:
                api_params["reasoning_effort"] = self.reasoning_effort

            response = await self.client.chat.completions.create(**api_params)

            raw_response = response.choices[0].message.content

            # Extract judgment from response
            if (
                "RESULT: PASS" in raw_response.upper()
                or raw_response.strip().upper().endswith("PASS")
            ):
                judgment = "PASS"
            elif (
                "RESULT: FAIL" in raw_response.upper()
                or raw_response.strip().upper().endswith("FAIL")
            ):
                judgment = "FAIL"
            else:
                # Try to find PASS or FAIL in the last line
                lines = raw_response.strip().split("\n")
                last_line = lines[-1].upper()
                if "PASS" in last_line:
                    judgment = "PASS"
                elif "FAIL" in last_line:
                    judgment = "FAIL"
                else:
                    judgment = "UNKNOWN"

            return judgment, raw_response

        except Exception as e:
            raise Exception(f"API call failed: {str(e)}")

    def collect_evaluation_items(self) -> list[tuple[str, Path, str]]:
        """
        Collect all evaluation items from the trajectory directory.
        Returns list of (task_path, trajectory_path, ground_truth).

        If self.category is set, only collect items from that category.
        Otherwise, collect from all categories.
        """
        items = []

        # Determine which categories to iterate through
        if self.category:
            # Test only the specified category
            category_path = self.trajectory_dir / self.category
            if not category_path.exists() or not category_path.is_dir():
                print(
                    f"Warning: Category '{self.category}' not found in {self.trajectory_dir}"
                )
                return items
            category_dirs = [category_path]
        else:
            # Test all categories
            category_dirs = [d for d in self.trajectory_dir.iterdir() if d.is_dir()]

        # Iterate through categories (filesystem, notion, postgres, etc.)
        for category_dir in category_dirs:
            category = category_dir.name

            # Iterate through task directories
            for task_dir in category_dir.iterdir():
                if not task_dir.is_dir():
                    continue

                task_name = task_dir.name
                task_path = f"{category}/{task_name}"

                # Check success and fail subdirectories
                for label_dir in ["success", "fail"]:
                    label_path = task_dir / label_dir
                    if not label_path.exists() or not label_path.is_dir():
                        continue

                    # Iterate through individual runs
                    for run_dir in label_path.iterdir():
                        if not run_dir.is_dir():
                            continue

                        items.append((task_path, run_dir, label_dir))

        return items

    async def evaluate_item(
        self,
        task_path: str,
        trajectory_path: Path,
        ground_truth: str,
        semaphore: asyncio.Semaphore,
    ) -> EvaluationResult:
        """Evaluate a single item with rate limiting."""
        result = EvaluationResult(
            task_path=task_path,
            trajectory_path=str(trajectory_path),
            ground_truth=ground_truth,
        )

        async with semaphore:
            # Load task description
            task_description = self.find_task_description(task_path)
            if not task_description:
                result.error = f"Could not find task description for {task_path}"
                return result

            # Load trajectory
            trajectory = self.load_trajectory(trajectory_path)
            if not trajectory:
                result.error = f"Could not load trajectory from {trajectory_path}"
                return result

            try:
                # Call LLM for evaluation
                judgment, raw_response = await self.evaluate_single(
                    task_description, trajectory
                )
                result.llm_judgment = judgment
                result.raw_response = raw_response

                # Determine if judgment is correct
                # Ground truth "success" should match "PASS", "fail" should match "FAIL"
                expected = "PASS" if ground_truth == "success" else "FAIL"
                result.is_correct = judgment == expected

            except Exception as e:
                result.error = str(e)

        return result

    async def run_evaluation(self) -> EvaluationStats:
        """Run the full evaluation in parallel."""
        print("Collecting evaluation items...")
        items = self.collect_evaluation_items()
        total_found = len(items)
        print(f"Found {total_found} trajectories to evaluate")

        if not items:
            print("No items to evaluate!")
            return self.stats

        # Limit the number of tasks if max_tasks is set
        if self.max_tasks is not None and self.max_tasks > 0:
            items = items[: self.max_tasks]
            print(
                f"Limiting evaluation to {len(items)} tasks (max_tasks={self.max_tasks})"
            )

        # Create semaphore for rate limiting
        semaphore = asyncio.Semaphore(self.max_concurrent)

        # Create tasks for parallel evaluation
        tasks = [
            self.evaluate_item(task_path, traj_path, ground_truth, semaphore)
            for task_path, traj_path, ground_truth in items
        ]

        print(
            f"Starting parallel evaluation with max {self.max_concurrent} concurrent requests..."
        )
        start_time = time.time()

        # Run all evaluations
        self.results = await asyncio.gather(*tasks)

        elapsed_time = time.time() - start_time
        print(f"Evaluation completed in {elapsed_time:.2f} seconds")

        # Calculate statistics
        self.calculate_stats()

        return self.stats

    def calculate_stats(self):
        """Calculate evaluation statistics from results."""
        self.stats = EvaluationStats()

        for result in self.results:
            self.stats.total += 1

            if result.error:
                self.stats.errors += 1
                continue

            if result.is_correct:
                self.stats.correct += 1
            else:
                self.stats.incorrect += 1

            # Calculate confusion matrix components
            if result.ground_truth == "success" and result.llm_judgment == "PASS":
                self.stats.true_positives += 1
            elif result.ground_truth == "fail" and result.llm_judgment == "FAIL":
                self.stats.true_negatives += 1
            elif result.ground_truth == "fail" and result.llm_judgment == "PASS":
                self.stats.false_positives += 1
            elif result.ground_truth == "success" and result.llm_judgment == "FAIL":
                self.stats.false_negatives += 1

    def get_stats_by_task(self) -> dict[str, dict]:
        """Get statistics grouped by task."""
        task_stats = {}

        for result in self.results:
            task_path = result.task_path
            if task_path not in task_stats:
                task_stats[task_path] = {
                    "total": 0,
                    "correct": 0,
                    "incorrect": 0,
                    "errors": 0,
                    "results": [],
                }

            stats = task_stats[task_path]
            stats["total"] += 1

            if result.error:
                stats["errors"] += 1
            elif result.is_correct:
                stats["correct"] += 1
            else:
                stats["incorrect"] += 1

            stats["results"].append(
                {
                    "trajectory": result.trajectory_path,
                    "ground_truth": result.ground_truth,
                    "judgment": result.llm_judgment,
                    "is_correct": result.is_correct,
                    "error": result.error,
                }
            )

        # Calculate accuracy for each task
        for task_path, stats in task_stats.items():
            valid = stats["total"] - stats["errors"]
            stats["accuracy"] = stats["correct"] / valid if valid > 0 else 0.0

        return task_stats

    def get_stats_by_category(self) -> dict[str, dict]:
        """Get statistics grouped by category (filesystem, notion, etc.)."""
        category_stats = {}

        for result in self.results:
            category = result.task_path.split("/")[0]
            if category not in category_stats:
                category_stats[category] = {
                    "total": 0,
                    "correct": 0,
                    "incorrect": 0,
                    "errors": 0,
                }

            stats = category_stats[category]
            stats["total"] += 1

            if result.error:
                stats["errors"] += 1
            elif result.is_correct:
                stats["correct"] += 1
            else:
                stats["incorrect"] += 1

        # Calculate accuracy for each category
        for category, stats in category_stats.items():
            valid = stats["total"] - stats["errors"]
            stats["accuracy"] = stats["correct"] / valid if valid > 0 else 0.0

        return category_stats

    def print_report(self):
        """Print a comprehensive evaluation report."""
        print("\n" + "=" * 80)
        print("LLM-AS-A-JUDGE EVALUATION REPORT")
        print("=" * 80)

        # Overall statistics
        print("\n📊 OVERALL STATISTICS")
        print("-" * 40)
        print(f"Total Evaluations: {self.stats.total}")
        print(f"Correct Judgments: {self.stats.correct}")
        print(f"Incorrect Judgments: {self.stats.incorrect}")
        print(f"Errors: {self.stats.errors}")
        print(f"\n✅ Accuracy: {self.stats.accuracy:.2%}")
        print(f"📈 Precision: {self.stats.precision:.2%}")
        print(f"📉 Recall: {self.stats.recall:.2%}")
        print(f"🎯 F1 Score: {self.stats.f1_score:.2%}")

        # Confusion Matrix
        print("\n📋 CONFUSION MATRIX")
        print("-" * 40)
        print(f"True Positives (Success -> PASS): {self.stats.true_positives}")
        print(f"True Negatives (Fail -> FAIL): {self.stats.true_negatives}")
        print(f"False Positives (Fail -> PASS): {self.stats.false_positives}")
        print(f"False Negatives (Success -> FAIL): {self.stats.false_negatives}")

        # Statistics by category
        print("\n📁 STATISTICS BY CATEGORY")
        print("-" * 40)
        category_stats = self.get_stats_by_category()
        for category, stats in sorted(category_stats.items()):
            print(f"\n{category.upper()}:")
            print(
                f"  Total: {stats['total']}, Correct: {stats['correct']}, "
                f"Incorrect: {stats['incorrect']}, Errors: {stats['errors']}"
            )
            print(f"  Accuracy: {stats['accuracy']:.2%}")

        # Statistics by task
        print("\n📝 STATISTICS BY TASK")
        print("-" * 40)
        task_stats = self.get_stats_by_task()
        for task_path, stats in sorted(task_stats.items()):
            print(f"\n{task_path}:")
            print(
                f"  Total: {stats['total']}, Correct: {stats['correct']}, "
                f"Incorrect: {stats['incorrect']}, Errors: {stats['errors']}"
            )
            print(f"  Accuracy: {stats['accuracy']:.2%}")

        # List incorrect judgments
        incorrect_results = [r for r in self.results if r.is_correct is False]
        if incorrect_results:
            print("\n❌ INCORRECT JUDGMENTS")
            print("-" * 40)
            for result in incorrect_results:
                print(f"\nTask: {result.task_path}")
                print(f"Trajectory: {result.trajectory_path}")
                print(f"Ground Truth: {result.ground_truth}")
                print(f"LLM Judgment: {result.llm_judgment}")

        # List errors
        error_results = [r for r in self.results if r.error]
        if error_results:
            print("\n⚠️ ERRORS")
            print("-" * 40)
            for result in error_results:
                print(f"\nTask: {result.task_path}")
                print(f"Trajectory: {result.trajectory_path}")
                print(f"Error: {result.error}")

        print("\n" + "=" * 80)

    def save_results(self, output_path: Optional[str] = None):
        """Save detailed results to a JSON file."""
        if output_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            result_subdir = self.file_name or self.category or "all"
            output_path = (
                self.base_dir
                / "LLM-as-a-Judge"
                / result_subdir
                / f"evaluation_results_{timestamp}.json"
            )
        else:
            output_path = Path(output_path)

        output_data = {
            "timestamp": datetime.now().isoformat(),
            "model": self.model,
            "overall_stats": {
                "total": self.stats.total,
                "correct": self.stats.correct,
                "incorrect": self.stats.incorrect,
                "errors": self.stats.errors,
                "accuracy": self.stats.accuracy,
                "precision": self.stats.precision,
                "recall": self.stats.recall,
                "f1_score": self.stats.f1_score,
                "true_positives": self.stats.true_positives,
                "true_negatives": self.stats.true_negatives,
                "false_positives": self.stats.false_positives,
                "false_negatives": self.stats.false_negatives,
            },
            "category_stats": self.get_stats_by_category(),
            "task_stats": self.get_stats_by_task(),
            "detailed_results": [
                {
                    "task_path": r.task_path,
                    "trajectory_path": r.trajectory_path,
                    "ground_truth": r.ground_truth,
                    "llm_judgment": r.llm_judgment,
                    "is_correct": r.is_correct,
                    "error": r.error,
                    "raw_response": r.raw_response,
                }
                for r in self.results
            ],
        }

        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)

        print(f"\n📄 Detailed results saved to: {output_path}")


async def main():
    parser = argparse.ArgumentParser(description="LLM-as-a-Judge Evaluator for MCPMark")
    parser.add_argument(
        "--base-dir",
        type=str,
        default=".",
        help="Base directory of the MCPMark project",
    )
    parser.add_argument(
        "--tasks-dir",
        type=str,
        default="tasks",
        help="Directory containing task descriptions (relative to base-dir)",
    )
    parser.add_argument(
        "--trajectory-dir",
        type=str,
        default="mcpmark-trajectory-log/mcpmark-selected-v4",
        help="Directory containing trajectories (relative to base-dir)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="deepseek-chat",
        help="OpenAI model to use for evaluation",
    )
    parser.add_argument(
        "--max-concurrent",
        type=int,
        default=10,
        help="Maximum number of concurrent API requests",
    )
    parser.add_argument(
        "--max-tasks",
        type=int,
        default=None,
        help="Maximum number of tasks to evaluate (for testing/debugging)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output file path for detailed results (JSON)",
    )
    parser.add_argument(
        "--env-file",
        type=str,
        default=".mcp_env",
        help="Path to the environment file containing API keys (default: .mcp_env)",
    )
    parser.add_argument(
        "--reasoning-effort",
        type=str,
        default=None,
        choices=["low", "medium", "high"],
        help="Reasoning effort level for models that support it (e.g., DeepSeek R1, OpenAI o1)",
    )
    parser.add_argument(
        "--category",
        type=str,
        default=None,
        help="Specific category to test (e.g., 'filesystem', 'notion', 'postgres'). If not specified, all categories will be tested.",
    )
    parser.add_argument(
        "--file-name",
        type=str,
        default=None,
        help="Subdirectory name under LLM-as-a-Judge for saving results (default: category name, or 'all').",
    )

    args = parser.parse_args()

    load_dotenv(dotenv_path=args.env_file, override=False)

    # Create evaluator
    evaluator = LLMJudgeEvaluator(
        base_dir=args.base_dir,
        tasks_dir=args.tasks_dir,
        trajectory_dir=args.trajectory_dir,
        model=args.model,
        max_concurrent=args.max_concurrent,
        max_tasks=args.max_tasks,
        reasoning_effort=args.reasoning_effort,
        category=args.category,
        file_name=args.file_name,
    )

    # Print category info
    if args.category:
        print(f"Testing category: {args.category}")
    else:
        print("Testing all categories")

    # Run evaluation
    await evaluator.run_evaluation()

    # Print report
    evaluator.print_report()

    # Save results
    evaluator.save_results(args.output)


if __name__ == "__main__":
    asyncio.run(main())
