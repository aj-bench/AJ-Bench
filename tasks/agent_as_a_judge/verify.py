import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, Optional

LABEL_PATTERN = r"Response:\s*\[([01])\]"


def extract_label(text: str) -> Optional[int]:
    match = re.search(LABEL_PATTERN, text, re.IGNORECASE | re.MULTILINE)
    if match:
        return int(match.group(1))
    return None


def get_expected_answer(work_dir, ground_truth_file=None):
    if isinstance(work_dir, str):
        work_dir = Path(work_dir)

    work_dir_str = str(work_dir)
    task_id = work_dir_str.split("__")[-1].strip()
    print(f"| Detected task_id from path: {task_id}")

    if not ground_truth_file:
        print("| Warning: No ground truth file provided")
        return None

    try:
        with open(ground_truth_file, "r", encoding="utf-8") as f:
            ground_truth_data = json.load(f)

        if task_id in ground_truth_data:
            if type(ground_truth_data[task_id]) is list:
                ground_truth_label = int(ground_truth_data[task_id][0])
            else:
                ground_truth_label = int(ground_truth_data[task_id])
            print(f"| Found ground truth for {task_id}: {ground_truth_label}")
            return ground_truth_label
        else:
            print(f"| Warning: Task {task_id} not found in ground truth file")
            return None
    except (json.JSONDecodeError, IOError, FileNotFoundError) as e:
        print(f"| Warning: Could not read ground truth file: {e}")
        return None


def get_working_directory() -> Path:
    messages_path = os.getenv("MCP_MESSAGES")
    if messages_path and Path(messages_path).exists():
        return Path(messages_path).parent.resolve()

    work_dir = os.getenv("PLAYWRIGHT_WORK_DIR")
    if work_dir:
        work_path = Path(work_dir).resolve()
        if (work_path / "messages.json").exists():
            return work_path

    current_dir = Path.cwd()
    if (current_dir / "messages.json").exists():
        return current_dir

    return Path(".").resolve()


def extract_content_from_message(message: Dict[str, Any]) -> str:
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


def parse_ai_results(work_dir: Path) -> Dict[str, Any]:
    messages_file = work_dir / "messages.json"
    if not messages_file.exists():
        return {"success": False, "error": "No messages.json found"}

    try:
        with open(messages_file, "r", encoding="utf-8") as f:
            messages = json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        return {"success": False, "error": f"Failed to read messages.json: {e}"}

    if not isinstance(messages, list):
        return {
            "success": False,
            "error": "messages.json should contain a list of messages",
        }

    ai_responses = []
    all_ai_content = []

    for message in messages:
        if not isinstance(message, dict):
            continue

        if message.get("role") == "assistant":
            content = extract_content_from_message(message)
            ai_responses.append({"content": content, "message": message})
            all_ai_content.append(content)

    if not ai_responses:
        return {
            "success": True,
            "found_label": False,
            "error": "No assistant responses found",
            "ai_responses": [],
            "total_responses": 0,
        }

    combined_content = "\n\n".join(all_ai_content)
    extracted_label = extract_label(combined_content)

    return {
        "success": True,
        "found_label": extracted_label is not None,
        "extracted_label": extracted_label,
        "ai_responses": [r["content"] for r in ai_responses],
        "total_responses": len(ai_responses),
        "combined_content": combined_content,
    }


def verify_task(ground_truth_file=None) -> bool:
    work_dir = get_working_directory()
    print(f"| Working directory: {work_dir}")

    ground_truth_label = get_expected_answer(work_dir, ground_truth_file)

    if ground_truth_label is None:
        print("| ❌ Could not find expected answer in ground truth file")
        return False

    print(f"| Expected label: {ground_truth_label}")

    ai_results = parse_ai_results(work_dir)

    if not ai_results["success"]:
        print(f"| ❌ Could not parse AI results: {ai_results.get('error')}")
        return False

    print(f"| Total AI responses: {ai_results['total_responses']}")

    extracted_label = ai_results.get("extracted_label")

    if extracted_label is not None:
        print(f"| Extracted label: {extracted_label}")

        if int(extracted_label) == int(ground_truth_label):
            print("| ✅ Label matches ground truth")

            with open(
                work_dir / "verification_summary.json", "w", encoding="utf-8"
            ) as f:
                json.dump(
                    {
                        "ground_truth_label": ground_truth_label,
                        "extracted_label": extracted_label,
                        "match": True,
                        "ai_responses_count": ai_results["total_responses"],
                    },
                    f,
                    indent=4,
                )
            print(
                f"| Verification summary saved to {work_dir / 'verification_summary.json'}"
            )
            return True
        else:
            print(
                f"| ❌ Label mismatch: expected {ground_truth_label}, got {extracted_label}"
            )

            with open(
                work_dir / "verification_summary.json", "w", encoding="utf-8"
            ) as f:
                json.dump(
                    {
                        "ground_truth_label": ground_truth_label,
                        "extracted_label": extracted_label,
                        "match": False,
                        "ai_responses_count": ai_results["total_responses"],
                    },
                    f,
                    indent=4,
                )
            print(
                f"| Verification summary saved to {work_dir / 'verification_summary.json'}"
            )
            return False
    else:
        print("| ❌ No label found in AI response")

        if ai_results.get("combined_content"):
            preview = ai_results["combined_content"][:500]
            print(f"| AI response preview: {preview}...")

        with open(work_dir / "verification_summary.json", "w", encoding="utf-8") as f:
            json.dump(
                {
                    "ground_truth_label": ground_truth_label,
                    "extracted_label": None,
                    "match": False,
                    "error": "No label found in response",
                    "ai_responses_count": ai_results["total_responses"],
                },
                f,
                indent=4,
            )
        print(
            f"| Verification summary saved to {work_dir / 'verification_summary.json'}"
        )
        return False


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--ground-truth-file",
        type=str,
        default="tasks/agent_as_a_judge/ground_truth/Mind2Web2-single-ground_truth.json",
    )
    args = parser.parse_args()

    try:
        success = verify_task(args.ground_truth_file)
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n💥 Verification error: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
