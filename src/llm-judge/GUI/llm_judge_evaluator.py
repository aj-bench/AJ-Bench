import argparse
import json
import os
import datetime
from typing import Dict, List, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from dotenv import load_dotenv


def read_json(path: str) -> Dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def read_jsonl(path: str) -> List[Dict]:
    rows: List[Dict] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except Exception:
                continue
    return rows


def load_single_traj_prompt(prompt_py_path: str) -> str:
    namespace: Dict[str, str] = {}
    with open(prompt_py_path, "r", encoding="utf-8") as f:
        code = f.read()
    exec(compile(code, prompt_py_path, "exec"), namespace, namespace)
    single_traj_prompt: str = namespace.get("single_traj_prompt")
    if not single_traj_prompt:
        raise ValueError("single_traj_prompt not found in prompt.py")
    return single_traj_prompt


def get_api_config(model: str) -> tuple[str, str]:
    """Get base URL and API key according to model name."""
    model_lower = model.lower()
    if "deepseek" in model_lower:
        base_url = os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
        api_key = os.environ.get("DEEPSEEK_API_KEY", "")
        if not api_key:
            raise ValueError("DeepSeek models require DEEPSEEK_API_KEY to be set in environment variables.")
        return base_url, api_key
    
    else:
        base_url = os.environ.get("OPENAI_BASE_URL", os.environ.get("BASE_URL", "https://api.openai.com"))
        api_key = os.environ.get("OPENAI_API_KEY", "")
        if not api_key:
            raise ValueError("Please set OPENAI_API_KEY in environment variables.")
        return base_url, api_key


def call_llm(model: str, system_prompt: str, user_prompt: str, screenshot_path: str = None, effort_level: Optional[str] = None, temperature: Optional[float] = None) -> tuple[str, Dict]:
    import requests
    import time
    
    # Get API configuration based on model type
    base_url, api_key = get_api_config(model)

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    # all models use text-only trajectories
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    # Detect whether this is a reasoning model (o1, o3, gpt-5.1, grok, etc.)
    is_reasoning_model = any(
        keyword in model.lower()
        for keyword in ['o1', 'o3', 'o4', 'gpt-5.1', 'reasoning', 'grok']
    )
    
    payload = {
        "model": model,
        "messages": messages,
    }
    
    if is_reasoning_model:
        messages = [msg for msg in messages if msg.get("role") != "system"]
        if not messages:
            messages = [{"role": "user", "content": user_prompt}]
        payload["messages"] = messages
        payload["max_completion_tokens"] = 20000
    else:
        if temperature is not None:
            payload["temperature"] = temperature
        if not(model=="deepseek-chat"):payload["max_tokens"] = 20000
        else:payload["max_tokens"] = 8000
    
    if effort_level and any(keyword in model.lower() for keyword in ['o3', 'gpt-5-mini']):
        if effort_level not in ["low", "medium", "high"]:
            print(f"Warning: effort_level '{effort_level}' is invalid, using 'medium' instead.")
            effort_level = "medium"
        
        if "o3" in model.lower():
            payload["reasoning_effort"] = effort_level
        elif "gpt-5-mini" in model.lower():
            payload["effort"] = {"effort": effort_level}
    
    if base_url.endswith('/v1'):
        url = f"{base_url}/chat/completions"
    elif base_url.endswith('/v4/'):
        url = f"{base_url}chat/completions"
    else:
        url = f"{base_url}/v1/chat/completions"
    
    # Simple retry mechanism
    max_retries = 5
    for attempt in range(max_retries):
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=300, verify=True)
            resp.raise_for_status()
            
            data = resp.json()
            if "choices" in data and len(data["choices"]) > 0:
                content = data["choices"][0]["message"].get("content", "")
                usage_info = data.get("usage", {})
                return content, usage_info
            else:
                raise ValueError("Response Format Error")
        
        except requests.exceptions.HTTPError as e:
            if e.response is not None:
                status_code = e.response.status_code
                if status_code == 429 or status_code >= 500:
                    if attempt < max_retries - 1:
                        wait_time = (attempt + 1) * 5
                        print(f"⚠️  API request error ({status_code}), retrying in {wait_time} seconds... ({attempt + 1}/{max_retries})")
                        time.sleep(wait_time)
                        continue
                
                print(f"❌ API client error ({status_code}): {e}")
                raise RuntimeError(f"API Client Error: {e}")
            else:
                pass

        except (requests.exceptions.SSLError, requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 2
                print(f"⚠️  Network error, retrying in {wait_time} seconds... ({attempt + 1}/{max_retries})")
                time.sleep(wait_time)
            else:
                raise RuntimeError(f"LLM Request Failed after {max_retries} retries: {e}")
        except Exception as e:
             if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 2
                print(f"⚠️  Unexpected error: {e}, retrying in {wait_time} seconds... ({attempt + 1}/{max_retries})")
                time.sleep(wait_time)
             else:
                raise RuntimeError(f"LLM Request Failed: {e}")
    
    raise RuntimeError(f"LLM Request Failed after {max_retries} retries")


def verify_api_config(model: str) -> bool:
    """Validate API configuration for the given model. Return True if it is usable."""
    try:
        base_url, api_key = get_api_config(model)
    except ValueError as e:
        print("\n" + "=" * 60)
        print("Verifying API configuration...")
        print(f"Model: {model}")
        print(f"❌ Error: {e}")
        print("=" * 60 + "\n")
        return False
    
    print("\n" + "=" * 60)
    print("Verifying API configuration...")
    print(f"Model: {model}")
    print(f"Base URL: {base_url}")
    print(f"API Key: {'*' * 8 + api_key[-4:] if len(api_key) > 4 else 'NOT SET'}")
    print("=" * 60)
    
    import requests
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    
    is_reasoning_model = any(keyword in model.lower() for keyword in ['o1', 'o3', 'o4', 'gpt-5.1', 'reasoning'])
    
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": "Test"}
        ]
    }
    
    if base_url.endswith('/v1'):
        # Base URL already includes /v1, just append chat/completions.
        url = f"{base_url}/chat/completions"
    elif base_url.endswith('/v4/'):
        # Some OpenAI-compatible providers (e.g., BigModel) use a v4-style endpoint.
        url = f"{base_url}chat/completions"
    else:
        # Default: append /v1/chat/completions to the base URL.
        url = f"{base_url}/v1/chat/completions"
    
    try:
        print(f"\nTesting API connectivity: {url}")
        resp = requests.post(url, headers=headers, json=payload, timeout=30)
        resp.raise_for_status()
        
        data = resp.json()
        if "choices" in data:
            print("✅ API configuration verified successfully!")
            if is_reasoning_model:
                print("   (reasoning model detected)")
            print("=" * 60 + "\n")
            return True
        else:
            print("❌ Invalid API response format")
            print(f"Response: {data}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ API configuration verification failed: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Status Code: {e.response.status_code}")
            print(f"Response: {e.response.text[:500]}")
        print("=" * 60 + "\n")
        return False
    except Exception as e:
        print(f"❌ Error during verification: {e}")
        print("=" * 60 + "\n")
        return False


def parse_verdict(output_text: str) -> Optional[bool]:
    """Parse a single trajectory evaluation result and return True/False/None."""
    text = output_text.strip()
    
    patterns = [
        "[[TRUE]]", "[[FALSE]]",
        "[TRUE]", "[FALSE]",
        "(TRUE)", "(FALSE)",
        "TRUE:", "FALSE:",
    ]
    
    for pattern in patterns:
        if pattern in text:
            if "TRUE" in pattern:
                return True
            elif "FALSE" in pattern:
                return False
    
    text_lower = text.lower()
    if "successfully completes" in text_lower or "trajectory is true" in text_lower:
        return True
    if "fails to complete" in text_lower or "trajectory is false" in text_lower:
        return False
        
    return None


def evaluate_trajectories(
    pairs_dir: str,
    output_dir: str,
    model: str,
    max_concurrent: int = 1,
    effort_level: Optional[str] = None,
    temperature: Optional[float] = None,
) -> Dict:
    """Evaluate trajectories and return a summary report."""
    
    prompt_py_path = os.path.join(os.path.dirname(__file__), "prompt.py")
    single_traj_prompt = load_single_traj_prompt(prompt_py_path)
    system_prompt = "You are a helpful agent that uses tools iteratively to complete the user's task, and when finished, provides the final answer or simply states \"Task completed\" without further tool calls."

    task_ids = [d for d in os.listdir(pairs_dir) if os.path.isdir(os.path.join(pairs_dir, d))]
    print(f"Processing ALL {len(task_ids)} tasks...")
    
    print(f"Using Model: {model}")
    print(f"Output Directory: {output_dir}")
    print(f"Max Concurrent: {max_concurrent}")
    print("-" * 50)

    results: List[Dict] = []
    num_correct = 0
    successful_calls = 0
    
    results_lock = threading.Lock()
    counter_lock = threading.Lock()
    
    def process_trajectory(task_id: str, traj_type: str, task_index: int, total_tasks: int) -> Optional[Dict]:
        """Process a single trajectory (true/false)."""
        nonlocal num_correct, successful_calls
        
        task_root = os.path.join(pairs_dir, task_id)
        traj_dir = os.path.join(task_root, traj_type)
        
        cfg_path = os.path.join(traj_dir, f"{task_id}.json")
        traj_path = os.path.join(traj_dir, "traj.jsonl")
        
        if not os.path.exists(cfg_path) or not os.path.exists(traj_path):
            return None
            
        try:
            cfg = read_json(cfg_path)
            instruction = cfg.get("instruction")
            if not instruction:
                return None
                
            traj = read_jsonl(traj_path)
            if not traj:
                return None
            
            # Check if a result file already exists (resume functionality)
            existing_result = None
            if os.path.exists(output_dir):
                for existing_dir in os.listdir(output_dir):
                    if existing_dir.startswith(f"{task_id}_{traj_type}_"):
                        existing_result_file = os.path.join(output_dir, existing_dir, "result.json")
                        if os.path.exists(existing_result_file):
                            try:
                                with open(existing_result_file, 'r', encoding='utf-8') as f:
                                    existing_result = json.load(f)
                                break
                            except:
                                continue
            
            if existing_result:
                print(f"[{task_index}/{total_tasks}] Skipping {task_id}_{traj_type} (already exists)")
                with counter_lock:
                    if existing_result.get('correct') is True:
                        num_correct += 1
                    if not existing_result.get('llm_output', '').startswith('Error:'):
                        successful_calls += 1
                return existing_result
            
            # Create a new output directory; include microseconds to avoid name collisions.
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            output_subdir = os.path.join(output_dir, f"{task_id}_{traj_type}_{timestamp}")
            result_file = os.path.join(output_subdir, "result.json")
            os.makedirs(output_subdir, exist_ok=True)
            
            traj_text = "\n".join([json.dumps(step, ensure_ascii=False) for step in traj])
            user_prompt = single_traj_prompt.format(instruction=instruction, trajectory=traj_text)
            
            print(f"[{task_index}/{total_tasks}] Processing {task_id}_{traj_type}")
            print(f"Instruction: {instruction[:100]}{'...' if len(instruction) > 100 else ''}")
            
            try:
                llm_output, usage_info = call_llm(
                    model,
                    system_prompt,
                    user_prompt,
                    screenshot_path=None,
                    effort_level=effort_level,
                    temperature=temperature,
                )
                verdict = parse_verdict(llm_output)
                with counter_lock:
                    successful_calls += 1
            except Exception as e:
                verdict = None
                llm_output = f"Error: {str(e)}"
                usage_info = {}

            ground_truth = (traj_type == "true")
            correct = verdict == ground_truth if verdict is not None else None
            if correct:
                with counter_lock:
                    num_correct += 1

            status = "✓" if correct else "✗" if correct is False else "?"
            # Do not use `verdict or 'N/A'` here; otherwise False would be printed as 'N/A'.
            if verdict is True:
                predict_str = "True"
            elif verdict is False:
                predict_str = "False"
            else:
                predict_str = "N/A"
            print(f"Predict: {predict_str}, Ground Truth: {ground_truth}, Correct: {status}")
            
            if llm_output:
                preview = llm_output[:200].replace('\n', ' ')
                print(f"LLM Output Preview: {preview}{'...' if len(llm_output) > 200 else ''}")
            print()

            result = {
                "task_id": f"{task_id}_{traj_type}",
                "instruction": instruction,
                "verdict": verdict,
                "ground_truth": ground_truth,
                "correct": bool(correct) if correct is not None else None,
                "llm_output": llm_output,
                "output_length": len(llm_output),
                "usage": usage_info,
                "model": model,
                "effort": effort_level,       # Record the effort level if used.
                "temperature": temperature,   # Record the temperature parameter.
                "timestamp": timestamp,
            }
            
            with open(result_file, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            
            print(f"  ✅ Saved result to {result_file}")
            return result
            
        except Exception as e:
            print(f"Error processing {task_id}_{traj_type}: {e}")
            return None
    
    all_tasks = []
    for i, task_id in enumerate(task_ids, 1):
        all_tasks.append((task_id, "true", i * 2 - 1, len(task_ids) * 2))
        all_tasks.append((task_id, "false", i * 2, len(task_ids) * 2))
    
    if max_concurrent > 1:
        with ThreadPoolExecutor(max_workers=max_concurrent) as executor:
            futures = {
                executor.submit(process_trajectory, task_id, traj_type, idx, total): (task_id, traj_type)
                for task_id, traj_type, idx, total in all_tasks
            }
            
            for future in as_completed(futures):
                result = future.result()
                if result:
                    with results_lock:
                        results.append(result)
    else:
        # Single-threaded processing
        for task_id, traj_type, idx, total in all_tasks:
            result = process_trajectory(task_id, traj_type, idx, total)
            if result:
                results.append(result)

    total = len(results)
    accuracy = (num_correct / total) if total > 0 else 0.0
    
    return {
        "total": total, 
        "correct": num_correct, 
        "accuracy": accuracy, 
        "details": results,
        "statistics": {
            "successful_calls": successful_calls,
        }
    }


def main():
    parser = argparse.ArgumentParser(description="Evaluate trajectories with LLM judge")
    parser.add_argument(
        "--model",
        type=str,
        default="deepseek-chat",
        help="Model name",
    )
    parser.add_argument(
        "--data-path",
        type=str,
        default=os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data", "GUI")),
        help="Root directory containing GUI task domains, Optional",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="./LLM-as-a-Judge_GUI",
        help="Output directory for evaluation results.",
    )
    parser.add_argument(
        "--max-concurrent",
        type=int,
        default=5,
        help="Maximum number of concurrent API requests (worker threads)",
    )
    parser.add_argument(
        "--reasoning-effort",
        type=str,
        default="medium",
        choices=["low", "medium", "high"],
        help="Reasoning effort level for models that support it",
    )
    parser.add_argument("--temperature", type=float, default=None, 
                        help="Temperature parameter")
    parser.add_argument(
        "--env-file",
        type=str,
        default=".mcp_env",
        help="Path to the environment file containing API keys (default: .mcp_env)",
    )
    
    args = parser.parse_args()

    load_dotenv(dotenv_path=args.env_file, override=False)
    
    if not verify_api_config(args.model):
        print("\nProgram terminated: API configuration validation failed, please fix and retry.")
        return

    data_root = args.data_path
    if not os.path.isdir(data_root):
        print(f"Error: data_path '{data_root}' does not exist or is not a directory.")
        return
    
    domain_dirs = [
        os.path.join(data_root, d)
        for d in os.listdir(data_root)
        if os.path.isdir(os.path.join(data_root, d))
    ]
    if not domain_dirs:
        print(f"Error: data_path '{data_root}' contains no domain subdirectories.")
        return
    
    os.makedirs(args.output, exist_ok=True)
    
    # Helper to compute metrics (precision, recall, F1, accuracy) from detailed results.
    def _compute_metrics(details: List[Dict]) -> Dict[str, float]:
        tp = fp = tn = fn = 0
        for d in details:
            gt = d.get("ground_truth")
            correct = d.get("correct")
            if gt is True:
                if correct is True:
                    tp += 1
                elif correct is False:
                    fn += 1
            elif gt is False:
                if correct is True:
                    tn += 1
                elif correct is False:
                    fp += 1
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
        accuracy = (tp + tn) / (tp + tn + fp + fn) if (tp + tn + fp + fn) > 0 else 0.0
        return {
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "accuracy": accuracy,
        }

    # Evaluate all domains and aggregate results.
    combined_details: List[Dict] = []
    total_tasks = 0
    total_correct = 0
    total_successful_calls = 0

    print("\n" + "=" * 60)
    print("Per-domain summary")
    print("=" * 60)

    for domain_dir in sorted(domain_dirs):
        domain_name = os.path.basename(domain_dir)
        report = evaluate_trajectories(
            pairs_dir=domain_dir,
            output_dir=args.output,
            model=args.model,
            max_concurrent=args.max_concurrent,
            effort_level=args.reasoning_effort,
            temperature=args.temperature,
        )

        domain_total = report.get("total", 0)
        domain_correct = report.get("correct", 0)
        domain_details = report.get("details", [])
        domain_stats = _compute_metrics(domain_details)

        total_tasks += domain_total
        total_correct += domain_correct
        combined_details.extend(domain_details)
        stats = report.get("statistics", {})
        total_successful_calls += stats.get("successful_calls", 0)

        print(
            f"{domain_name}: "
            f"F1={domain_stats['f1']*100:.2f}%, "
            f"Total={domain_total}, "
            f"Correct={domain_correct}"
        )

    overall_stats = _compute_metrics(combined_details)

    print("\n" + "=" * 60)
    print("Overall summary")
    print("=" * 60)
    print(f"Total Tasks: {total_tasks}")
    print(f"Correct Predictions: {total_correct}")
    print(f"Precision: {overall_stats['precision']*100:.2f}%")
    print(f"Recall:    {overall_stats['recall']*100:.2f}%")
    print(f"F1 Score:  {overall_stats['f1']*100:.2f}%")
    print("=" * 60)


if __name__ == "__main__":
    main()
