#!/usr/bin/env python3
"""
Verification script for LLM-as-a-Judge single-row search task.
"""

import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, Optional

LABEL_PATTERN = r"Response:\s*\[([01])\]"


def extract_label(text: str) -> Optional[int]:
    """Extract single label from Response: [0] or Response: [1] format.
    Returns:
        Integer label (0 or 1) if found, None otherwise
    """
    match = re.search(LABEL_PATTERN, text, re.IGNORECASE | re.MULTILINE)
    if match:
        return int(match.group(1))
    return None


def extract_content_from_message(message: Dict[str, Any]) -> str:
    """Extract text content from a message, handling various formats."""
    content = message.get("content", "")

    if isinstance(content, str):
        return content
    elif isinstance(content, list):
        text_parts = []
        for item in content:
            if isinstance(item, dict):
                if item.get("type") == "text":
                    text_parts.append(item.get("text", ""))
                elif item.get("type") == "thinking":
                    thinking_text = item.get("thinking", "")
                    if thinking_text:
                        text_parts.append(f"<thinking>{thinking_text}</thinking>")
                else:
                    text_parts.append(str(item.get("text", item)))
            else:
                text_parts.append(str(item))
        return " ".join(text_parts)
    else:
        return str(content)


def parse_ai_results(
    result_file_path: str = None,
) -> Dict[str, Any]:
    """Parse the AI agent's results from LLM judge result format with single label extraction."""
    result_file = Path(result_file_path)
    if not result_file.exists():
        return {"success": False, "error": f"No result file found at {result_file}"}

    try:
        with open(result_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        return {"success": False, "error": f"Failed to read {result_file.name}: {e}"}

    if isinstance(data, dict):
        response_results = []

        for entry_id, entry in data.items():
            if not isinstance(entry, dict):
                continue

            response_content = entry.get("response", "")
            ground_truth = entry.get("ground_truth")

            # if response_content:
            extracted_label = extract_label(response_content)
            is_correct = (
                extracted_label is not None
                and ground_truth is not None
                and int(extracted_label) == int(ground_truth)
            )

            response_results.append(
                {
                    "entry_id": entry_id,
                    "content": response_content,
                    "extracted_label": extracted_label,
                    "ground_truth": ground_truth,
                    "is_correct": is_correct,
                }
            )

        if not response_results:
            return {
                "success": True,
                "found_answer": False,
                "error": "No responses found in LLM judge format",
                "response_results": [],
                "total_responses": 0,
            }

        correct_count = sum(1 for r in response_results if r["is_correct"])
        total_count = len(response_results)
        success_rate = correct_count / total_count if total_count > 0 else 0.0

        return {
            "success": True,
            "response_results": response_results,
            "total_responses": total_count,
            "correct_responses": correct_count,
            "success_rate": success_rate,
            "found_answer": success_rate > 0.0,
        }

    else:
        return {
            "success": False,
            "error": "Unknown JSON format - expected dict",
        }


def verify_task(
    result_file_path=None,
    output_file=None,
) -> bool:
    """Verify the AI agent found the correct answer with single-row label analysis."""
    result_file = Path(result_file_path)
    print(f"| Result file: {result_file}")

    if not result_file.exists():
        print(f"| ❌ No result file found at {result_file}")
        return False

    ai_results = parse_ai_results(result_file_path=result_file_path)

    if not ai_results["success"]:
        print(f"| ❌ Could not parse AI results: {ai_results.get('error')}")
        return False

    response_results = ai_results.get("response_results", [])
    total_responses = ai_results.get("total_responses", 0)
    correct_responses = ai_results.get("correct_responses", 0)
    success_rate = ai_results.get("success_rate", 0.0)

    print(f"| Total responses: {total_responses}")

    for result in response_results:
        entry_id = result.get("entry_id")
        extracted_label = result.get("extracted_label")
        ground_truth = result.get("ground_truth")
        is_correct = result.get("is_correct")

        status = "✅" if is_correct else "❌"
        print(f"| Response {entry_id}: {status}")

        if extracted_label is not None:
            print(f"|   Extracted label: {extracted_label}")
        else:
            print("|   No label found in response")

        if ground_truth is not None:
            print(f"|   Ground truth: {ground_truth}")

        if not is_correct and extracted_label is not None:
            print(f"|   Label mismatch: expected {ground_truth}, got {extracted_label}")

    print(f"| Correct responses: {correct_responses}")
    print(f"| Success rate: {success_rate:.2%}")

    overall_success = success_rate >= 1.0
    print(f"| Overall result: {'✅ PASS' if overall_success else '❌ FAIL'}")

    if output_file:
        import datetime

        summary_result = {
            "metadata": {
                "result_file": str(result_file),
                "total_responses": total_responses,
                "correct_responses": correct_responses,
                "success_rate": success_rate,
                "overall_success": overall_success,
                "timestamp": datetime.datetime.now().isoformat(),
            },
            "detailed_results": response_results,
        }

        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(summary_result, f, indent=4, ensure_ascii=False)
            print(f"| Results saved to: {output_file}")
        except Exception as e:
            print(f"| Warning: Failed to save results to {output_file}: {e}")

    return overall_success


def main():
    """Main verification function."""
    import argparse

    parser = argparse.ArgumentParser(description="Verify LLM judge single-row results")
    parser.add_argument(
        "--result-file",
        type=str,
        default="results/WideSearch/debug/llm-as-a-judge/Gemini/run-1/gpt-5__llm_as_a_judge-run-1.json",
        help="Path to the result file to verify",
    )
    parser.add_argument(
        "--output-file",
        type=str,
        default="results/WideSearch/debug/llm-as-a-judge/Gemini/run-1/result-gpt-5__llm_as_a_judge-run-1.json",
        help="Path to save the verification results as JSON",
    )
    args = parser.parse_args()

    try:
        success = verify_task(
            result_file_path=args.result_file,
            output_file=args.output_file,
        )
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n💥 Verification error: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
