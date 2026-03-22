import json
import ssl
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Optional

import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from tqdm import tqdm
from transformers import HfArgumentParser
from urllib3.util.retry import Retry

DEFAULT_LLM_SINGLE_ROW_JUDGE_PROMPT = """# LLM-as-a-Judge Task

You will verify the factual correctness of ONE Single-Row extracted from a Response.
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

### Single-Row (One extracted item)

[The Start of Single-Row]

{single_row}

[The End of Single-Row]

------------------------------------------------------------
## Core Principle

Your task is NOT to evaluate whether the Single-Row answers the entire Query. Your task IS ONLY to evaluate whether THIS Single-Row:

1. Correctly reflects the part of the Response it was extracted from;
2. Is factually correct according to your knowledge.

You MUST ignore completeness. You MUST evaluate only the correctness of THIS Single-Row's own claims.

------------------------------------------------------------
## Role and High-Level Objective

Act as a neutral, impartial judge.

------------------------------------------------------------
## Step-by-Step Evaluation Procedure

### Step 1 — Initial Read
- Read the Query, Response, and Single-Row fully.

### Step 2 — Trace Source in the Response
- Locate the corresponding content in the Response.
- Confirm the Single-Row faithfully reflects the Response.

### Step 3 — Verify Each Claim Individually
- Focus strictly on content relevant to the Query.
- Do not let style, language, or level of detail influence judgment.
- Treat "N/A", "NA", or "Data Unavailable" as problematic unless explicitly allowed.
- Verify every field if the item contains multiple attributes (e.g., in a table row).
- Numeric values must strictly match authoritative sources—no tolerance allowed.

### Step 4 — Record Verification Results
For every claim in the Single-Row record:
- Supported / Contradicted / Not verifiable

------------------------------------------------------------
## Final Judgment Rules

A Single-Row is labeled **[1]** ONLY IF:
1. It contains at least one claim relevant to the Query; AND
2. Every claim is factually correct; AND
3. It faithfully represents the Response.

Otherwise, assign **[0]**.

### If ANY claim is:
- incorrect, OR
- missing, OR
- unverifiable
→ assign **[0]**

------------------------------------------------------------
## Strict Requirements

- You MUST NOT add or infer information beyond what is provided.

------------------------------------------------------------
## Output Format (Strict)

Your final output must be exactly one line:

Response: [1]
or
Response: [0]

Nothing else.
"""

SYSTEM_PROMPT = """You are a helpful llm that completes the user's task, and when finished, provides the final answer or simply states "Task completed"."""


@dataclass
class APIClientConfig:
    base_url: Optional[str] = field(default="YOUR_API_BASE_URL")
    api_key: Optional[str] = field(default="YOUR_API_KEY")
    response_label_path: str = field(
        default="src/data/Search/wide_llm_judge_single_row.jsonl",
        metadata={"help": "Path to JSONL file containing response and label data"},
    )
    output: Optional[str] = field(
        default="results/WideSearch/debug/llm-as-a-judge/Gemini/gpt-5__llm_as_a_judge-run-1.json",
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

    def __init__(self, response_label_path: str):
        self.response_label_path = Path(response_label_path)

        if not self.response_label_path.exists():
            raise FileNotFoundError(
                f"Response label data file not found: {self.response_label_path}"
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
            DataFrame with columns: task_id, model, row_number, query, response, single_row, ground_truth_label
        """
        df = pd.read_json(self.response_label_path, lines=True)

        records = []
        model_mapping = {
            "response1": "Gemini",
            "response2": "Grok",
            "response3": "Perplexity",
        }

        skipped_count = 0
        valid_task_model_keys = []

        for idx, row in df.iterrows():
            task_id = row["task_id"]
            query = row["query"]

            for response_key in ["response1", "response2", "response3"]:
                if response_key not in row:
                    continue

                model_name = model_mapping[response_key]

                if filter_model and model_name != filter_model:
                    continue

                task_model_key = f"{task_id}-{model_name}"

                if task_filter and task_filter != task_model_key:
                    continue

                # Get extracted single rows and labels
                extracted_key = f"{response_key}_extracted"
                label_key = f"{response_key}_label"

                if extracted_key not in row or label_key not in row:
                    continue

                extracted_rows = row[extracted_key]
                response_content = row[response_key]
                ground_truth_label = row[label_key]

                # Skip if no extracted rows
                if not extracted_rows or len(extracted_rows) == 0:
                    continue

                # Validate: Parse ground_truth_label and check length match
                try:
                    # Parse label (expected to be comma-separated string or list)
                    if isinstance(ground_truth_label, str):
                        label_list = [
                            label.strip()
                            for label in ground_truth_label.split(",")
                            if label.strip()
                        ]
                    elif isinstance(ground_truth_label, list):
                        label_list = [str(label) for label in ground_truth_label]
                    else:
                        print(
                            f"Warning: Unexpected label format for {task_id}-{model_name}: {type(ground_truth_label)}"
                        )
                        skipped_count += 1
                        continue

                    # Check if lengths match
                    if len(extracted_rows) != len(label_list):
                        skipped_count += 1
                        continue

                except Exception as e:
                    print(
                        f"Warning: Failed to parse label for {task_id}-{model_name}: {e}"
                    )
                    skipped_count += 1
                    continue

                if task_model_key not in valid_task_model_keys:
                    valid_task_model_keys.append(task_model_key)

                if num_tasks and len(valid_task_model_keys) > num_tasks:
                    break

                # Create record for each single row
                for row_idx, (single_row, label) in enumerate(
                    zip(extracted_rows, label_list), start=1
                ):
                    records.append(
                        {
                            "task_id": task_id,
                            "model": model_name,
                            "response_key": response_key,
                            "row_number": row_idx,
                            "row_id": f"{task_id}-{model_name}-row_{row_idx}",
                            "query": query,
                            "response": response_content,
                            "single_row": single_row,
                            "ground_truth_label": label,
                        }
                    )

            if num_tasks and len(valid_task_model_keys) >= num_tasks:
                break

        result_df = pd.DataFrame(records)

        if filter_model:
            print(f"Filtered by model: {filter_model}")
        if skipped_count > 0:
            print(
                f"Skipped {skipped_count} task-response pairs due to mismatch or errors"
            )
        if num_tasks:
            print(f"Limited to first {num_tasks} valid tasks (after skipping)")

        if not result_df.empty:
            print(
                f"Loaded {len(result_df)} row-level tasks from {len(set(result_df['task_id'].astype(str) + '-' + result_df['model']))} unique task-model combinations"
            )
        else:
            print("No data loaded.")

        return result_df


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
        single_row: str,
        model: str = "gpt-3.5-turbo",
        temperature: Optional[float] = None,
        reasoning_effort: str = None,
    ) -> Dict[str, Any]:
        """Judge a single row using the LLM."""
        user_prompt_content = DEFAULT_LLM_SINGLE_ROW_JUDGE_PROMPT.format(
            query=query,
            response=response,
            single_row=single_row,
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
                    single_row=row_data["single_row"],
                    model=model,
                    temperature=temperature,
                    reasoning_effort=reasoning_effort,
                )

                results[row_id] = {
                    "task_id": row_data["task_id"],
                    "model": row_data["model"],
                    "row_number": row_data["row_number"],
                    "query": row_data["query"],
                    "response": judge_result["choices"][0]["message"]["content"],
                    "ground_truth": row_data["ground_truth_label"],
                }

            except Exception as e:
                row_id = (
                    row_data.get("row_id", f"unknown_{idx}")
                    if "row_data" in locals()
                    else f"unknown_{idx}"
                )
                results[row_id] = {
                    "query": row_data.get("query", "unknown"),
                    "error": str(e),
                    "status": "failed",
                }
                print(f"Failed to process row {idx + 1}: {e}")

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
                    if original_key not in row_id_to_data:
                        print(f"Warning: Cannot find data for key {original_key}")
                        continue

                    row_data = row_id_to_data[original_key]

                    print(f"Retrying key '{original_key}'")

                    judge_result = self.judge_single_row(
                        query=row_data["query"],
                        response=row_data["response"],
                        single_row=row_data["single_row"],
                        model=model,
                        temperature=temperature,
                        reasoning_effort=reasoning_effort,
                    )

                    existing_results[original_key] = {
                        "task_id": row_data["task_id"],
                        "model": row_data["model"],
                        "row_number": row_data["row_number"],
                        "query": row_data["query"],
                        "response": judge_result["choices"][0]["message"]["content"],
                        "ground_truth": row_data["ground_truth_label"],
                    }

                    print(f"Successfully retried key '{original_key}'")

                except Exception as e:
                    print(f"Failed to retry key '{original_key}': {e}")
                    existing_results[original_key] = {
                        "query": row_data.get("query", "unknown")
                        if "row_data" in locals()
                        else "unknown",
                        "error": f"Retry failed: {str(e)}",
                        "status": "failed",
                    }

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
        response_label_path=script_args.response_label_path,
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
                print("No data to process. Exiting.")
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
