# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Find a researcher who is affiliated with UC Berkeley as of 2025 or received his PhD from UC Berkeley, and who has a paper related to vision and language models that was accepted at ICLR 2023. Provide the researcher's name,  a description of their UC Berkeley affiliation (such as current position at Berkeley or PhD obtained there), and a link to the paper's page on OpenReview.

[The End of Query]

### Response

[The Start of Response]

Trevor Darrell is a researcher who meets the criteria.

- **Name**: Trevor Darrell
- **UC Berkeley Affiliation**: Professor in the Electrical Engineering and Computer Science Department at UC Berkeley as of 2025.
- **Paper Link**: https://openreview.net/forum?id=eR2dG8yjnQ

---

The paper "Using Language to Extend to Unseen Domains" explores how language descriptions can adapt pretrained vision models to new domains without needing target data during training. This approach, termed Language Guided Adaptive Risk Minimization (LARM), leverages natural language to guide model adaptation at test time, building on vision-language pretraining methods like CLIP. It addresses challenges in domain generalization for visual tasks, where models often fail on unseen distributions despite strong performance on training data.

Key contributions include:
- A method to use language as a proxy for domain shifts, enabling zero-shot adaptation.
- Empirical results showing improvements on benchmarks like PACS, VLCS, OfficeHome, TerraIncognita, and DomainNet, with gains of up to 7.6% in accuracy.
- Analysis of how language supervision complements visual cues, reducing risks associated with domain mismatches.

The work highlights the potential of integrating language for robust vision systems, particularly in scenarios with limited data access. It also discusses limitations, such as reliance on accurate language descriptions and potential biases in pretrained models.

**Table 1: Performance Comparison on Domain Generalization Benchmarks**

| Benchmark      | Baseline (ERM) Accuracy (%) | LARM Accuracy (%) | Improvement (%) |
| -------------- | --------------------------- | ----------------- | --------------- |
| PACS           | 85.5                        | 93.1              | 7.6             |
| VLCS           | 77.3                        | 82.4              | 5.1             |
| OfficeHome     | 66.5                        | 71.2              | 4.7             |
| TerraIncognita | 46.1                        | 50.8              | 4.7             |
| DomainNet      | 40.2                        | 44.9              | 4.7             |

The results demonstrate consistent gains across diverse visual domains, validating the role of language in enhancing model robustness.

Further details include ablation studies on language prompt design, where descriptive prompts outperform simple labels, and comparisons with other adaptation techniques like test-time entropy minimization. The paper also examines the interplay between vision-language alignment and risk minimization, suggesting future directions for multimodal learning in real-world applications.

**Key Citations:**
- https://openreview.net/forum?id=eR2dG8yjnQ
- https://arxiv.org/abs/2210.09520
- https://iclr.cc/virtual/2023/poster/11059
- https://nlp.cs.berkeley.edu/pubs/Dunlap-Mohri-Raghunathan-Guillory-Zhang-Darrell-Gonzalez-Rohrbach_2023_Language_paper.pdf
- https://proceedings.iclr.cc/paper_files/paper/2023/file/12e9a3a9436c3b6b596b15b75d2c0f52-Paper-Conference.pdf

[The End of Response]

### Rubric

[The Start of Rubric]

1. Correctly identify a researcher who  is affiliated with the University of California, Berkeley as of 2025 or who received a Ph.D. from UC Berkeley, and who has a paper related to vision and language models accepted at ICLR 2023. 1 point for giving the researcher's name.
2. Correctly provide a description of this researcher's UC Berkeley affiliation (e.g., current position at UC Berkeley or Ph.D. obtained there) to earn 1 point.
3. Correctly provide the link to the paper's page on OpenReview to earn 1 point.
4. Full score: 3 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-2:
Professor in the Electrical Engineering and Computer Science Department at UC Berkeley as of 2025.

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
