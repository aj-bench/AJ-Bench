# NOTE: LLM-as-a-Judge
system_prompt = """You are a helpful llm that completes the user's task, and when finished, provides the final answer or simply states "Task completed"."""

user_prompt = """# LLM-as-a-Judge Task

Verify and evaluate the following two responses to a given query.

## Query:
{query}

## Response A:
{response_a}

## Response B:
{response_b}

## Evaluation Guidelines:
1. Act as a **neutral and impartial judge**.
2. Compare the content of each response and analyze whether there are factual errors or inaccuracies. Use this analysis to determine which response is better.
3. Carefully assess which response more effectively addresses the user's query and provides a more accurate answer.
4. Support your judgment with a clear explanation that compares both responses.
5. Do **not** let response order, length, or assistant identity influence your evaluation.
6. Your evaluation must include fact-checking and verification.

## Expected Output:
- First, provide your explanation of the comparison, This explanation must cover all parts of both responses that address the query.
- Then, output your final verdict in this exact format:
    - If you determine that **Response A** is better, output: `[[A]]`
    - If you determine that **Response B** is better, output: `[[B]]`"""

# NOTE: Agent-as-a-Judge
system_prompt = (
    "You are a helpful agent that uses tools iteratively to complete the user's task, "
    'and when finished, provides the final answer or simply states "Task completed" without further tool calls.'
)

agent_judge_prompt = """# Agent-as-a-Judge Task

## Query:
{query}

## Response A:
{response_a}

## Response B:
{response_b}

## Evaluation Guidelines:
1. Act as a **neutral and impartial judge**.
2. Compare the content of each response and analyze whether there are factual errors or inaccuracies. Use this analysis to determine which response is better.
3. Carefully assess which response more effectively addresses the user's query and provides a more accurate answer.
4. Support your judgment with a clear explanation that compares both responses.
5. Do **not** let response order, length, or assistant identity influence your evaluation.

## Expected Output:
- First, provide your explanation of the comparison, This explanation must cover all parts of both responses that address the query.
- Then, output your final verdict in this exact format:
    - If you determine that **Response A** is better, output: `[[A]]`
    - If you determine that **Response B** is better, output: `[[B]]`"""

# NOTE: Single Trajectory Evaluation
single_traj_prompt = """# Single Trajectory Evaluation Task

## Instruction:
{instruction}

## Trajectory:
{trajectory}

## Evaluation Guidelines:
1. Act as a **neutral and impartial judge**.
2. Analyze the trajectory to determine if it successfully completes the given instruction.
3. Consider whether the trajectory follows logical steps and achieves the intended goal.
4. Look for any errors, inconsistencies, or failures in the execution.
5. Provide a clear explanation of your reasoning.

## Expected Output:
- First, provide your detailed analysis of the trajectory, explaining why it succeeds or fails.
- Then, output your final verdict in this exact format:
    - If the trajectory **successfully completes** the instruction, output: `[[TRUE]]`
    - If the trajectory **fails to complete** the instruction, output: `[[FALSE]]`
- You must output your final verdict in your final message, using exactly one of the above formats and nothing else after it."""
