# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Find 3 ICLR 2024 accepted conference papers on OpenReview whose 'Related Work' sections do not appear anywhere in the main body of the paper (the main body is defined as all sections appearing before the references and appendix). Provide direct OpenReview PDF links and forum links for each paper.

[The End of Query]

### Response

[The Start of Response]

# Unconventional 'Related Work' Placement at ICLR 2024

| Paper Title | OpenReview Forum Link | OpenReview PDF Link | Location of 'Related Work' | Formatting Strategy |
| :---- | :---- | :---- | :---- | :---- |
| What Happens During the Loss Plateau? Understanding Abrupt Learning in Transformers | https://openreview.net/forum?id=493ee3e943f013fbc23f2bcf9f674560ddd2d174 | https://openreview.net/pdf?id=493ee3e943f013fbc23f2bcf9f674560ddd2d174 | Appendix H | Displacement to Appendix |
| The mechanistic basis of data dependence and abrupt learning in an in-context classification task | https://openreview.net/forum?id=aN4Jf6Cx69 | https://openreview.net/pdf?id=aN4Jf6Cx69 | Appendix H | Displacement to Appendix |
| Improved Techniques for Training Consistency Models | https://openreview.net/forum?id=WNzy9bRDvG | https://openreview.net/pdf?id=WNzy9bRDvG | Integrated into Introduction | Full Integration |

A direct examination of both papers' PDFs confirms that their respective "Related Work" sections are located in Appendix H, entirely outside the main nine-page body.

Structurally, the paper has no section titled "Related Work." Instead, the literature review is seamlessly integrated into the first few paragraphs of the Introduction.

## Works cited

1. ICLR 2024 Conference - OpenReview, https://openreview.net/group?id=ICLR.cc/2024/Conference  
2. What Happens During the Loss Plateau ... - OpenReview, https://openreview.net/pdf/493ee3e943f013fbc23f2bcf9f674560ddd2d174.pdf  
3. The mechanistic basis of data dependence and abrupt learning in ..., https://openreview.net/forum?id=aN4Jf6Cx69  
4. ICLR 2024 Awards, https://iclr.cc/virtual/2024/awards_detail  
5. Improved Techniques for Training Consistency Models - OpenReview, https://openreview.net/forum?id=WNzy9bRDvG  
6. IMPROVED TECHNIQUES FOR TRAINING ... - ICLR Proceedings, https://proceedings.iclr.cc/paper_files/paper/2024/file/41bd71e7bf7f9fe68f1c936940fd06bd-Paper-Conference.pdf

[The End of Response]

### Rubric

[The Start of Rubric]

1. Identify accepted conference papers of ICLR 2024 on OpenReview, with the requirement that the "Related Work" section does not appear in the main body of the offer(the main body is defined as all parts before the references and appendices). Award 1 point for each eligible paper provided, with a maximum of 3 points.
2. Provide the OpenReview PDF link for each paper meeting the above requirement. Award 1 point for each correct PDF link provided, up to a maximum of 3 points.
3. Provide the OpenReview forum link for each paper meeting the above requirement. Award 1 point for each correct forum link provided, up to a maximum of 3 points.
4. The total possible score is 9 points.


[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-2:
https://openreview.net/pdf?id=aN4Jf6Cx69

[The End of Single-Row]

------------------------------------------------------------
## Core Principle

**Your task is NOT to evaluate whether the Single-Row answers the entire Query. Your task IS ONLY to evaluate whether THIS extracted Single-Row:**

1. **Directly corresponds to exactly ONE scoring unit in the Rubric;**
2. **Correctly reflects the part of the Response it was extracted from;**
3. **Is factually correct according to verification tools;**
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
→ You MAY search authoritative sources using Playwright MCP tools.

### B. A URL, page link, or reference link
→ You MUST evaluate ONLY the correctness of the link provided.
→ You MUST NOT:
- generate a new link,
- search for the correct link,
- fix the link,
- replace anything missing.

If the Rubric requires a link and the Single-Row does not provide one → label [0].

------------------------------------------------------------
## Verification Procedure

### Step 1 — Identify the Target Rubric Unit
- Locate the scoring unit whose index matches "Extracted From Rubric" in the Single-Row.
- All evaluation must be restricted to the requirements of that scoring unit.

### Step 2 — Trace Source in the Response
- Identify where in the Response the Single-Row was extracted from.
- Confirm the Single-Row content faithfully reflects the Response.

### Step 3 — Evidence Verification (Using Tools)
You MUST:

- Follow all explicit references in the Response that are relevant to the Single-Row, including URLs, footnotes (e.g., `[^1]`, `<sup>1</sup>`), or entries in "Work Cited" / "Key Citations".
- Open referenced pages using Playwright MCP tools.
- Validate every claim in the Single-Row that attempts to satisfy the Rubric.

If Response references are insufficient:
- Only if the Rubric requires *factual content*, you may perform searches.
- If the Rubric requires *a link*, you MUST NOT search for any missing link.

### Step 4 — Handling "Unverifiable"
If a claim remains unverifiable after:
- reviewing all Response references, and
- performing allowed searches,

then mark the claim as **Not verifiable** and assign label [0].

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
