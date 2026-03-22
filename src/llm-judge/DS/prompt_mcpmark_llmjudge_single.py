DEFAULT_AGENT_JUDGE_WIDESEARCH_PROMPT = """
You are an impartial evaluator. Your job is to determine whether the given Agent Trajectory successfully completes the Task Description.

You must follow these rules strictly:
(1) Base your judgment only on the information provided in the Task Description and the Agent Trajectory.
(2) Evaluate whether every requirement in the Task Description is fully satisfied.
(3) Your answer must be binary: 'PASS' or 'FAIL'.
(4) Before giving the binary result, you may provide chain-of-thought or step-by-step internal reasoning.
(5) Do not propose improvements, fixes, or technical solutions—simply judge.

Input Format:
[TASK DESCRIPTION]
{task}

[AGENT TRAJECTORY]
{trajectory}

Judging Criteria:
Mark the trajectory as PASS only if all required steps are present, all computations or file operations are correct, the output format exactly matches the specification, no required content is missing, and no extra or disallowed content is added. If any requirement is unmet, the result must be FAIL.

Output Format (Strict):
RESULT: PASS or FAIL

"""


DEFAULT_AGENT_JUDGE_WIDESEARCH_PROMPT_2 = """
You are an impartial evaluator. Your task is to assess whether the given
Agent Trajectory completes the Task Description.

Rules:
1. Base your judgment only on the information explicitly provided in the Task Description and the Agent Trajectory.
2. Verify that all requirements, both explicit and reasonably implied, appear to be satisfied.
3. If any step seems incomplete, ambiguous, or weakly supported by evidence, consider it as potentially not fully satisfied.
4. The Agent Trajectory must demonstrate clear and complete task fulfillment. Partial or uncertain completion may lead to a negative judgment.
5. Your final decision must be binary: PASS or FAIL.
6. You may briefly justify your decision before the final result.
7. Do not propose improvements or alternative solutions.

Input Format:
[TASK DESCRIPTION]
{task}

[AGENT TRAJECTORY]
{trajectory}


Output Format (Strict):
RESULT: PASS
or
RESULT: FAIL
"""
