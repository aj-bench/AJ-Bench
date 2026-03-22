#!/usr/bin/env python3
"""
MCPMark Judge Evaluation Pipeline
==================================

This script provides an automated pipeline for evaluating Agent-as-a-Judge performance
on previously recorded agent trajectories. The judge agent replays trajectories
and verifies whether tasks were completed successfully.
"""

import argparse
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from src.agent_judge_ds_evaluator import JudgeEvaluator
from src.agents import AGENT_REGISTRY
from src.factory import MCPServiceFactory
from src.logger import get_logger
from src.model_config import ModelConfig


# Initialize logger
logger = get_logger(__name__)


def main():
    """Main entry point for the judge evaluation pipeline."""
    parser = argparse.ArgumentParser(description="MCPMark Judge Evaluation Pipeline.")

    supported_mcp_services = MCPServiceFactory.get_supported_mcp_services()
    supported_models = ModelConfig.get_supported_models()

    # Main configuration
    parser.add_argument(
        "--mcp",
        default="filesystem",
        choices=supported_mcp_services,
        help="MCP service to evaluate trajectories for (default: filesystem)",
    )
    parser.add_argument(
        "--models",
        required=True,
        help="Comma-separated list of judge models to use (e.g., 'o3,gpt-4.1')",
    )
    parser.add_argument(
        "--agent",
        default="mcpmark",
        choices=sorted(AGENT_REGISTRY.keys()),
        help="Agent implementation to use for judge (default: mcpmark)",
    )
    parser.add_argument(
        "--tasks",
        default="all",
        help='Tasks to evaluate: (1). "all"; (2). "category"; or (3). "category/task".',
    )
    parser.add_argument(
        "--exp-name",
        default=None,
        help="Experiment name; results are saved under results/judge__<model>__<mcp>/<exp-name>/ (default: YYYY-MM-DD-HH-MM-SS)",
    )

    # Trajectory configuration
    parser.add_argument(
        "--trajectory-dir",
        default="src/data/DS",
        help="Directory containing trajectories to evaluate (default: mcpmark-trajectory-log/mcpmark-selected-v4)",
    )
    parser.add_argument(
        "--tasks-dir",
        default="tasks/agent_as_a_judge/mcp_tasks",
        help="Directory containing task descriptions (default: tasks)",
    )

    # Execution configuration
    parser.add_argument(
        "--timeout",
        type=int,
        default=300,
        help="Timeout in seconds for judge agent execution (default: 300)",
    )
    parser.add_argument(
        "--reasoning-effort",
        default="default",
        choices=["default", "minimal", "low", "medium", "high"],
        help="Reasoning effort level for supported models (default: default)",
    )
    parser.add_argument(
        "--max-tasks",
        type=int,
        default=None,
        help="Maximum number of trajectories to evaluate (default: all)",
    )

    # Output configuration
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("./Agent-as-a-Judge_DS"),
        help="Directory to save results (default: ./Agent-as-a-Judge)",
    )
    parser.add_argument(
        "--env-file",
        type=str,
        default=".mcp_env",
        help="Path to environment file with API keys (default: .mcp_env)",
    )

    parser.add_argument(
        "--max_parallel_tasks",
        type=int,
        default=1,
        help="Maximum number of tasks to run in parallel (default: 1)",
    )
    parser.add_argument(
        "--skip-completed",
        action="store_true",
        default=False,
        help="Skip trajectories that have already been evaluated (checks for existing judge_meta.json with verdict)",
    )

    # Load arguments and environment variables
    args = parser.parse_args()
    load_dotenv(dotenv_path=args.env_file, override=False)

    # Generate default exp-name if not provided
    if args.exp_name is None:
        args.exp_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    # Parse models (no validation - allow unsupported models)
    model_list = [m.strip() for m in args.models.split(",") if m.strip()]
    if not model_list:
        parser.error("No valid models provided")

    # Log warning for unsupported models but don't error
    unsupported_models = [m for m in model_list if m not in supported_models]
    if unsupported_models:
        logger.warning(
            f"Using unsupported models: {', '.join(unsupported_models)}. "
            "Will use OPENAI_BASE_URL and OPENAI_API_KEY from environment."
        )

    logger.info("MCPMark Judge Evaluation")
    logger.info(
        f"Experiment: {args.exp_name} | {len(model_list)} Judge Model(s): {', '.join(model_list)}"
    )
    logger.info(f"Trajectory Directory: {args.trajectory_dir}")
    logger.info(f"MCP Service: {args.mcp}")

    # Run evaluation for each judge model
    for i, model in enumerate(model_list, 1):
        logger.info(f"\n{'=' * 60}")
        logger.info(f"Starting judge evaluation {i}/{len(model_list)}: {model}")
        logger.info(f"{'=' * 60}\n")

        # Initialize and run the judge evaluation pipeline
        judge = JudgeEvaluator(
            mcp_service=args.mcp,
            model=model,
            trajectory_dir=args.trajectory_dir,
            tasks_dir=args.tasks_dir,
            timeout=args.timeout,
            exp_name=args.exp_name,
            output_dir=args.output_dir,
            reasoning_effort=args.reasoning_effort,
            agent_name=args.agent,
            max_tasks=args.max_tasks,
            max_parallel_tasks=args.max_parallel_tasks,
            skip_completed=args.skip_completed,
        )

        # Run evaluation
        stats = judge.run_evaluation_parallel(args.tasks)

        # Print report
        judge.print_report()

        # Save results
        output_path = judge.save_results()

        logger.info(f"\n📊 Judge Evaluation Summary for {model}:")
        logger.info(
            f"   Total: {stats.total}, Correct: {stats.correct}, Incorrect: {stats.incorrect}, Errors: {stats.errors}"
        )
        logger.info(f"   Accuracy: {stats.accuracy:.2%}")
        logger.info(
            f"   Precision: {stats.precision:.2%}, Recall: {stats.recall:.2%}, F1: {stats.f1_score:.2%}"
        )
        logger.info(f"📁 Results: {judge.base_experiment_dir}")
        logger.info(f"📄 JSON: {output_path}")

    logger.info(f"\n{'=' * 60}")
    logger.info(f"✓ All judge evaluations completed for {len(model_list)} model(s)")
    logger.info(f"{'=' * 60}")


if __name__ == "__main__":
    main()
