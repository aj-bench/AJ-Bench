# Prompts for Agent-as-a-Judge Search tasks

SINGLE_ROW_SUMMARY_PROMPT = """# Web Page Content Extraction and Summarization

You are an assistant specialized in evidence extraction from web pages.

You will be given three inputs:
1. **User Query**: the overall question or instruction the user is trying to answer.
2. **Single-Row**: a candidate answer extracted from the model that needs to be verified. It may be correct or incorrect. DO NOT assume it is true.
3. **Page Content**: raw text captured by Playwright MCP tools.

## CRITICAL INTERPRETATION RULES

- Your task is **NOT to answer the Query**, and **NOT to validate Single-Row**.
- Your task is to **extract evidence** from the Page Content that is relevant to:
    1. the Query, and/or
    2. the Single-Row (whether supporting, contradicting, or related).
- The Single-Row defines what needs verification, but it is *not* the truth. You must extract *all* content from the Page Content that could help verify, refute, contextualize, or interpret the Single-Row.
- If the Page Content contains passages relevant to the Single-Row, these passages must always be extracted.
- You may also extract any passage relevant to the broader Query, even if unrelated to the Single-Row.

## Query:

[The Start of Query]

{query}

[The End of Query]

## Single-Row:

[The Start of Single-Row]

{single_row}

[The End of Single-Row]

## Page Content:

[The Start of Page Content]

{result}

[The End of Page Content]

## Task Instructions

1. **Extract relevant content verbatim**
    - Identify all passages in the Page Content that are relevant to the **Single-Row**, including:
        - directly supporting information
        - indirectly related information
        - conflicting or contradictory information
        - contextual information
    - Additionally, extract any passages relevant to the broader **Query**.
    - Copy all extracted text **exactly as it appears** (no paraphrasing, no rewriting).
    - Preserve hyperlinks and original formatting (bullet points, line breaks).
    - Exclude content that does not help understand, verify, or refute Single-Row, and does not answer any part of the Query.

2. **Summarize the extracted evidence**
    - Produce a short summary **only of the extracted content**, highlighting:
        - what information relates to the Query
        - what information relates to the Single-Row
        - whether the extracted information provides support, contradiction, or context
    - Do **not** attempt to answer the Query itself.
    - Do **not** judge correctness of Single-Row; only summarize available evidence.

## Pre-Output Self-Check (Mandatory)

Before outputting:
- Ensure all passages relevant to Single-Row are included verbatim.
- Ensure all passages relevant to the Query (even beyond Single-Row) are also included.
- Ensure the summary does not introduce new information or answer the Query.
- Ensure the summary only condenses extracted evidence.

## Output Format

Your output must contain two sections:

- **Extracted Content:**
    - A list of verbatim passages from the Page Content.
    - Mark passages that relate to the Single-Row (e.g., prepend `[Related to Single-Row]`).

- **Summary:**
    - A concise description of the extracted evidence.
    - Explain which parts relate to the Single-Row and which relate to the broader Query.
"""
