import json
import re
import ssl
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from tqdm import tqdm
from transformers import HfArgumentParser
from urllib3.util.retry import Retry

DEFAULT_MIND2WEB2_LLM_SINGLE_ROW_JUDGE_PROMPT = """# LLM-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

{query}

[The End of Query]

### Response

[The Start of Response]

{response}

[The End of Response]

### Rubric

[The Start of Rubric]

{rubric}

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

{single_row}

[The End of Single-Row]

------------------------------------------------------------
## Core Principle

**Your task is NOT to evaluate whether the Single-Row answers the entire Query. Your task IS ONLY to evaluate whether THIS extracted Single-Row:**

1. **Directly corresponds to exactly ONE scoring unit in the Rubric;**
2. **Correctly reflects the part of the Response it was extracted from;**
3. **Is factually correct according to your knowledge;**
4. **Meets ALL requirements of the corresponding Rubric scoring unit;**
5. **Contains at least one claim relevant to the Query.**

You MUST ignore completeness.
You MUST evaluate only the correctness of THIS Single-Row's own claims.

------------------------------------------------------------
## Structural Constraints (Very Important)

1. **Single-Row = One scoring unit**
    - The "Extracted From Rubric" ID in the Single-Row must match exactly one scoring unit in the overall Rubric.

2. **No mixing**
    - The Single-Row must not combine multiple rubric units into one claim.

3. **Strict multi-condition requirement**
    - If the matched Rubric scoring unit contains multiple requirements, **the Single-Row must satisfy ALL of them. Partial fulfillment = label [0].**

4. **"N/A" rule (mandatory)**
    - If the Single-Row contains "N/A", **you must immediately label it as [0], regardless of any other information.**

------------------------------------------------------------
## Distinguishing Requirement Types (CRITICAL)

You MUST determine whether the matched Rubric scoring unit requires:

### A. Factual content
(e.g., a person's name, a date, a fact, an explanation)
→ You MAY use your own prior knowledge to verify factual claims.

### B. A URL, page link, or reference link
→ You MUST evaluate the correctness of a link using ALL of the following sources:
- your own prior knowledge,
- your ability to judge whether a link is plausible, internally consistent, or matches well-known link patterns.

→ You MUST NOT:
- generate a new link,
- search for the correct link,
- fix the link,
- replace anything missing,
- assume a link is correct based solely on its appearance.

You MUST NOT judge a link as correct ONLY based on formatting, domain familiarity, or similarity to known sites. You MAY use your internal knowledge to assess whether the provided link is likely to be correct.

If the Rubric requires a link and the Single-Row does not provide one → label [0].

------------------------------------------------------------
## Verification Procedure

### Step 1 — Identify the Target Rubric Unit
- Locate the scoring unit whose index matches "Extracted From Rubric" in the Single-Row.
- All evaluation must be restricted to the requirements of that scoring unit.

### Step 2 — Trace Source in the Response
- Identify where in the Response the Single-Row was extracted from.
- Confirm the Single-Row content faithfully reflects the Response.

### Step 3 — Evidence Verification
You MUST:
- Follow all explicit references in the Response that are relevant to the Single-Row, including URLs, footnotes (e.g., `[^1]`, `<sup>1</sup>`), or entries in "Work Cited" / "Key Citations".
- Validate every claim in the Single-Row that attempts to satisfy the Rubric.

### Step 4 — Handling "Unverifiable"
If a claim remains unverifiable after:
- reviewing all Response references, and
- applying your own prior knowledge and reasoning,

then mark the claim as Not verifiable and assign label [0].

A link is Not verifiable ONLY if:
- you have no relevant knowledge of its expected structure, AND
- the Response provides no context that helps determine correctness.

------------------------------------------------------------
## Final Judgment Rules

Label the Single-Row as **[1]** only if:

1. It makes at least one claim relevant to the Query AND
2. Every claim is factually correct AND
3. It satisfies ALL requirements of the matched Rubric scoring unit AND
4. It faithfully represents its source in the Response AND
5. No part of the claim is "N/A".

Otherwise, assign **[0]**.

------------------------------------------------------------
## Output Format (Strict)

You MUST output only:

- Response: [1]

or

- Response: [0]

Nothing else.
"""


def extract_rubric_parts(text: str) -> List[List[str]]:
    """
    Extract rubric parts from structured text.

    Parses text containing rubric entries in the format:
    RubricX-PartY: "content"

    Args:
        text: Input text containing rubric entries

    Returns:
        List of lists, where each inner list contains parts for one rubric
        Example: [["Part1 content", "Part2 content"], ["Part1 content"]]
    """
    rubric_dict = {}

    # Method1: Find standard Parts with ending quotes
    pattern_standard = r'Rubric(\d+)-Part(\d+):\s*"([^"]*)"'
    matches = re.findall(pattern_standard, text)

    for rubric_num, part_num, content in matches:
        rubric_num = int(rubric_num)
        part_num = int(part_num)
        if rubric_num not in rubric_dict:
            rubric_dict[rubric_num] = {}
        rubric_dict[rubric_num][part_num] = content

    # Method2: Find Parts missing ending quotes
    # Match from "RubricX-PartY: " to the next "Rubric" or end of string
    pattern_incomplete = r'Rubric(\d+)-Part(\d+):\s*"([^"]*)(?:$|(?=\nRubric))'
    matches_incomplete = re.findall(pattern_incomplete, text, re.MULTILINE | re.DOTALL)

    for rubric_num, part_num, content in matches_incomplete:
        rubric_num = int(rubric_num)
        part_num = int(part_num)
        if rubric_num not in rubric_dict:
            rubric_dict[rubric_num] = {}
        if part_num not in rubric_dict[rubric_num]:
            rubric_dict[rubric_num][part_num] = content.rstrip()

    if not rubric_dict:
        return []

    result = []
    for rubric_num in sorted(rubric_dict.keys()):
        parts = rubric_dict[rubric_num]
        rubric_parts = [parts[part_num] for part_num in sorted(parts.keys())]
        result.append(rubric_parts)

    return result


SYSTEM_PROMPT = """You are a helpful llm that completes the user's task, and when finished, provides the final answer or simply states "Task completed"."""


@dataclass
class APIClientConfig:
    base_url: Optional[str] = field(default="YOUR_API_BASE_URL")
    api_key: Optional[str] = field(default="YOUR_API_KEY")
    single_row_data_path: str = field(
        default="src/data/Search/deep_llm_judge_single_row.json",
        metadata={"help": "Path to JSON file containing single-row extracted data"},
    )
    query_label_data_path: str = field(
        default="src/data/Search/deep_llm_judge_origin.jsonl",
        metadata={"help": "Path to JSONL file containing query and label data"},
    )
    output: Optional[str] = field(
        default="results/Mind2Web2/debug/llm-as-a-judge/Gemini/gpt-5__llm_as_a_judge-run-1.json",
        metadata={"help": "Output file path for judge results (JSON)"},
    )
    judge_model: Optional[str] = field(
        default="gpt-5",
        metadata={"help": "Judge model (LLM that evaluates); distinct from filter_model (models being evaluated: Gemini/Grok/Perplexity)"},
    )
    temperature: Optional[float] = field(default=None)
    reasoning_effort: Optional[str] = field(default=None)
    retry_mode: bool = field(default=False)
    task_filter: Optional[str] = field(
        default=None,
        metadata={"help": "Optional task_id-model filter (e.g., 'ws_en_067-Grok')"},
    )
    filter_model: Optional[str] = field(
        default="Gemini",
        metadata={"help": "Filter tasks by model name (Gemini, Grok, or Perplexity)"},
    )
    num_tasks: Optional[int] = field(
        default=None,
        metadata={
            "help": "Limit to first N tasks (after filtering by model if specified)"
        },
    )


class DataLoader:
    """Load and process single-row data for LLM judging."""

    def __init__(self, single_row_data_path: str, query_label_data_path: str):
        self.single_row_data_path = Path(single_row_data_path)
        self.query_label_data_path = Path(query_label_data_path)

        if not self.single_row_data_path.exists():
            raise FileNotFoundError(
                f"Single row data file not found: {self.single_row_data_path}"
            )
        if not self.query_label_data_path.exists():
            raise FileNotFoundError(
                f"Query label data file not found: {self.query_label_data_path}"
            )

    def load_data(
        self,
        task_filter: Optional[str] = None,
        filter_model: Optional[str] = None,
        num_tasks: Optional[int] = None,
    ) -> pd.DataFrame:
        """
        Load and flatten single-row data into a DataFrame.

        Args:
            task_filter: Optional filter in format 'task_id-model' (e.g., 'ws_en_067-Grok')
            filter_model: Optional model name filter (Gemini, Grok, or Perplexity)
            num_tasks: Optional limit to first N unique tasks (after filtering and skipping invalid tasks)

        Returns:
            DataFrame with columns: task_id, model, row_id, query, response, rubric,
                                    single_row_part, ground_truth_label
        """
        with open(self.single_row_data_path, "r", encoding="utf-8") as f:
            single_row_data = json.load(f)

        query_label_df = pd.read_json(self.query_label_data_path, lines=True)

        model_mapping = {
            "response1": "Gemini",
            "response2": "Grok",
            "response3": "Perplexity",
        }

        records = []
        skipped_count = 0
        valid_task_model_keys = []

        for task_key, task_info in single_row_data.items():
            task_id = task_info.get("task_id")
            query = task_info.get("query")
            rubric = task_info.get("rubric", "")

            matching_labels = query_label_df[query_label_df["task_id"] == task_id]
            if matching_labels.empty:
                continue

            for response_key in ["response1", "response2", "response3"]:
                if response_key not in task_info:
                    continue

                model_name = model_mapping[response_key]

                if filter_model and model_name != filter_model:
                    continue

                task_model_key = f"{task_id}-{model_name}"

                if task_filter and task_filter != task_model_key:
                    continue

                extracted_response = task_info[response_key]
                single_row_parts = extract_rubric_parts(extracted_response)

                response_content = matching_labels.iloc[0][response_key]
                label_key = f"{response_key}_label"

                if label_key not in task_info:
                    continue

                ground_truth_label = task_info[label_key]

                try:
                    parsed_labels = json.loads(ground_truth_label)

                    labels_shape = [
                        len(rubric_labels) for rubric_labels in parsed_labels
                    ]
                    parts_shape = [len(parts) for parts in single_row_parts]

                    if labels_shape != parts_shape:
                        skipped_count += 1
                        continue

                    if task_model_key not in valid_task_model_keys:
                        valid_task_model_keys.append(task_model_key)

                    if num_tasks is not None and len(valid_task_model_keys) > num_tasks:
                        if task_model_key not in valid_task_model_keys[:num_tasks]:
                            continue

                    flattened_labels_list = [
                        label
                        for rubric_labels in parsed_labels
                        for label in rubric_labels
                    ]

                    flattened_single_row_parts = [
                        f"Extracted From Rubric-{i + 1}:\n" + single_row_parts[i][j]
                        for i in range(len(single_row_parts))
                        for j in range(len(single_row_parts[i]))
                    ]

                    for row_idx, (single_row_part, label) in enumerate(
                        zip(flattened_single_row_parts, flattened_labels_list), start=1
                    ):
                        records.append(
                            {
                                "task_id": task_id,
                                "model": model_name,
                                "row_id": f"{task_id}-{model_name}-row_{row_idx}",
                                "query": query,
                                "response": response_content,
                                "rubric": rubric,
                                "single_row_part": single_row_part,
                                "ground_truth_label": label,
                            }
                        )

                except (json.JSONDecodeError, TypeError):
                    skipped_count += 1
                    continue

        df = pd.DataFrame(records)

        if filter_model:
            print(f"Filtered by model: {filter_model}")
        if skipped_count > 0:
            print(f"Skipped {skipped_count} task-response pairs due to shape mismatch")
        if num_tasks:
            print(f"Limited to first {num_tasks} valid tasks (after skipping)")
        print(
            f"Loaded {len(df)} row-level tasks from {len(set(df['task_id'].astype(str) + '-' + df['model']))} unique task-model combinations"
        )

        return df


class OpenAIClient:
    def __init__(
        self,
        base_url: str,
        api_key: str,
        timeout: int = 600,
        max_retries: int = 5,
        backoff_factor: float = 2.0,
    ):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout
        self.max_retries = max_retries

        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

        self.session = requests.Session()
        retry_strategy = Retry(
            total=max_retries,
            backoff_factor=backoff_factor,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=[
                "HEAD",
                "GET",
                "PUT",
                "DELETE",
                "OPTIONS",
                "TRACE",
                "POST",
            ],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def _make_request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        url = f"{self.base_url}{endpoint}"
        last_exception = None

        for attempt in range(self.max_retries):
            try:
                response = self.session.request(
                    method, url, headers=self.headers, timeout=self.timeout, **kwargs
                )
                response.raise_for_status()
                return response.json()
            except (ssl.SSLError, requests.exceptions.SSLError) as e:
                last_exception = e
                wait_time = min(60, (2**attempt) * 2)
                print(
                    f"SSL error on attempt {attempt + 1}/{self.max_retries}, retrying in {wait_time}s: {e}"
                )
                time.sleep(wait_time)
            except requests.exceptions.ConnectionError as e:
                last_exception = e
                wait_time = min(60, (2**attempt) * 2)
                print(
                    f"Connection error on attempt {attempt + 1}/{self.max_retries}, retrying in {wait_time}s: {e}"
                )
                time.sleep(wait_time)
            except requests.exceptions.Timeout as e:
                last_exception = e
                wait_time = min(60, (2**attempt) * 2)
                print(
                    f"Timeout on attempt {attempt + 1}/{self.max_retries}, retrying in {wait_time}s: {e}"
                )
                time.sleep(wait_time)
            except requests.exceptions.RequestException as e:
                raise Exception(f"Request failed: {str(e)}")

        raise Exception(
            f"Request failed after {self.max_retries} retries: {str(last_exception)}"
        )

    def get_chat_completion(
        self,
        messages: list,
        model: str = "gpt-3.5-turbo",
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        reasoning_effort: str = None,
    ) -> Dict[str, Any]:
        payload = {
            "messages": messages,
            "model": model,
        }
        if max_tokens is not None:
            payload["max_tokens"] = max_tokens
        if reasoning_effort is not None:
            payload["reasoning_effort"] = reasoning_effort
        if temperature is not None:
            payload["temperature"] = temperature

        if model == "glm-4.6":
            response = self._make_request("POST", "/v4/chat/completions", json=payload)
        else:
            response = self._make_request("POST", "/v1/chat/completions", json=payload)
        return response

    def judge_single_row(
        self,
        query: str,
        response: str,
        rubric: str,
        single_row_part: str,
        model: str = "gpt-3.5-turbo",
        temperature: Optional[float] = None,
        reasoning_effort: str = None,
    ) -> Dict[str, Any]:
        """Judge a single row using the LLM."""
        user_prompt_content = DEFAULT_MIND2WEB2_LLM_SINGLE_ROW_JUDGE_PROMPT.format(
            query=query,
            response=response,
            rubric=rubric,
            single_row=single_row_part,
        )

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt_content},
        ]

        return self.get_chat_completion(
            messages=messages,
            model=model,
            temperature=temperature,
            reasoning_effort=reasoning_effort,
        )

    def get_models(self) -> Dict[str, Any]:
        return self._make_request("GET", "/v1/models")

    def save_response(
        self, response_data: Dict[str, Any], filename: str = "response.json"
    ) -> None:
        try:
            output_path = Path(filename)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(response_data, f, indent=4, ensure_ascii=False)
            print(f"Response saved to {filename}")
        except Exception as e:
            print(f"Failed to save file: {e}")
            raise

    def process_batch_rows(
        self,
        data: pd.DataFrame,
        output_file: str,
        model: str = "gpt-3.5-turbo",
        temperature: Optional[float] = None,
        reasoning_effort: str = None,
    ) -> Dict[str, Any]:
        """Process all rows in the DataFrame and save results."""
        results = {}

        for idx, row_data in tqdm(
            data.iterrows(), total=len(data), desc="Processing rows"
        ):
            try:
                row_id = row_data["row_id"]

                judge_result = self.judge_single_row(
                    query=row_data["query"],
                    response=row_data["response"],
                    rubric=row_data["rubric"],
                    single_row_part=row_data["single_row_part"],
                    model=model,
                    temperature=temperature,
                    reasoning_effort=reasoning_effort,
                )

                results[row_id] = {
                    "task_id": row_data["task_id"],
                    "model": row_data["model"],
                    "row_id": row_id,
                    "query": row_data["query"],
                    "judge_response": judge_result["choices"][0]["message"]["content"],
                    "ground_truth_label": row_data["ground_truth_label"],
                }

            except Exception as e:
                row_id = row_data.get("row_id", f"unknown_{idx}")
                results[row_id] = {
                    "task_id": row_data.get("task_id", "unknown"),
                    "model": row_data.get("model", "unknown"),
                    "row_id": row_id,
                    "error": str(e),
                    "status": "failed",
                }
                print(f"Failed to process row {row_id}: {e}")

        self.save_response(results, output_file)
        return results

    def retry_failed_queries(
        self,
        result_file: str,
        data_loader: DataLoader,
        task_filter: Optional[str] = None,
        filter_model: Optional[str] = None,
        num_tasks: Optional[int] = None,
        model: str = "gpt-3.5-turbo",
        temperature: Optional[float] = None,
        reasoning_effort: str = None,
    ) -> Dict[str, Any]:
        """Retry failed queries from a previous run."""
        try:
            with open(result_file, "r", encoding="utf-8") as f:
                existing_results = json.load(f)
            print(f"Loaded {len(existing_results)} existing results from {result_file}")

            failed_entries = [
                (key, result)
                for key, result in existing_results.items()
                if isinstance(result, dict) and result.get("status") == "failed"
            ]

            if not failed_entries:
                print("No failed entries found. Nothing to retry.")
                return existing_results

            print(f"Found {len(failed_entries)} failed entries to retry")

            all_data = data_loader.load_data(
                task_filter=task_filter,
                filter_model=filter_model,
                num_tasks=num_tasks,
            )
            row_id_to_data = {row["row_id"]: row for _, row in all_data.iterrows()}

            for original_key, failed_result in tqdm(
                failed_entries, desc="Retrying failed queries"
            ):
                try:
                    row_id = failed_result.get("row_id", original_key)

                    if row_id not in row_id_to_data:
                        print(f"Warning: Cannot find data for row {row_id}")
                        continue

                    row_data = row_id_to_data[row_id]

                    judge_result = self.judge_single_row(
                        query=row_data["query"],
                        response=row_data["response"],
                        rubric=row_data["rubric"],
                        single_row_part=row_data["single_row_part"],
                        model=model,
                        temperature=temperature,
                        reasoning_effort=reasoning_effort,
                    )

                    existing_results[original_key] = {
                        "task_id": row_data["task_id"],
                        "model": row_data["model"],
                        "row_id": row_id,
                        "query": row_data["query"],
                        "judge_response": judge_result["choices"][0]["message"][
                            "content"
                        ],
                        "ground_truth_label": row_data["ground_truth_label"],
                    }

                    print(f"Successfully retried row '{row_id}'")

                except Exception as e:
                    print(f"Failed to retry row '{original_key}': {e}")
                    existing_results[original_key]["error"] = f"Retry failed: {str(e)}"

            self.save_response(existing_results, result_file)

            still_failed = sum(
                1
                for result in existing_results.values()
                if isinstance(result, dict) and result.get("status") == "failed"
            )
            print(
                f"\nRetry complete! Total: {len(existing_results)}, "
                f"Successfully retried: {len(failed_entries) - still_failed}, "
                f"Still failed: {still_failed}"
            )

            return existing_results

        except Exception as e:
            raise Exception(f"Failed to retry queries: {str(e)}")


def main():
    parser = HfArgumentParser(APIClientConfig)
    script_args = parser.parse_args_into_dataclasses()[0]

    print(
        f"Configuration: judge_model={script_args.judge_model}, "
        f"temperature={script_args.temperature}, "
        f"retry_mode={script_args.retry_mode}"
    )

    if script_args.filter_model:
        print(f"Model filter: {script_args.filter_model}")
    if script_args.num_tasks:
        print(f"Task limit: {script_args.num_tasks}")
    if script_args.task_filter:
        print(f"Specific task filter: {script_args.task_filter}")

    client = OpenAIClient(
        base_url=script_args.base_url,
        api_key=script_args.api_key,
        timeout=600,
        max_retries=5,
        backoff_factor=2.0,
    )

    data_loader = DataLoader(
        single_row_data_path=script_args.single_row_data_path,
        query_label_data_path=script_args.query_label_data_path,
    )

    try:
        if script_args.retry_mode:
            print("Running in RETRY mode...")
            client.retry_failed_queries(
                result_file=script_args.output,
                data_loader=data_loader,
                task_filter=script_args.task_filter,
                filter_model=script_args.filter_model,
                num_tasks=script_args.num_tasks,
                model=script_args.judge_model,
                temperature=script_args.temperature,
                reasoning_effort=script_args.reasoning_effort,
            )
        else:
            print("Running in NORMAL mode...")
            data = data_loader.load_data(
                task_filter=script_args.task_filter,
                filter_model=script_args.filter_model,
                num_tasks=script_args.num_tasks,
            )

            if data.empty:
                print("No data to process. Check your filters or input files.")
                return

            client.process_batch_rows(
                data=data,
                output_file=script_args.output,
                model=script_args.judge_model,
                temperature=script_args.temperature,
                reasoning_effort=script_args.reasoning_effort,
            )

            print(f"Processing complete! Results saved to {script_args.output}")

    except Exception as e:
        print(f"Failed: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
