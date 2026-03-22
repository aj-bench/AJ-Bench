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

# Vision and Language Models at ICLR 2023: A Berkeley Affiliation

**Key Finding:**
Among the vision–language papers accepted to ICLR 2023, Yossi Gandelsman is affiliated with UC Berkeley and co‐authored an OpenReview‐hosted paper on diagnosing and mitigating hallucinations in vision–language representations.

***

## Researcher Profile

**Name:** Yossi Gandelsman
**Affiliation:** University of California, Berkeley (PhD student, Computer Science, 2020 – 2025)

***

## ICLR 2023 Paper

**Title:** Interpreting and Editing Vision–Language Representations to Mitigate Hallucinations
**Authors:** Nick Jiang, Anish Kachinthaya, Suzie Petryk, **Yossi Gandelsman**
**Conference:** ICLR 2023
**Description:**
This work investigates hallucinations—incorrect or spurious object references—produced by vision–language models. The authors introduce a method that (1) projects internal image features to the language vocabulary to detect overconfident “hallucinated” tokens, (2) uses these projections to spatially localize true objects, and (3) applies a “knowledge erasure” algorithm that orthogonalizes out hallucinated object features, reducing spurious detections by up to 25.7% on COCO2014 while preserving model performance.[^1]

**OpenReview Link:**
https://openreview.net/forum?id=6zfgR2b4gF
<span style="display:none">[^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^2][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^3][^30][^31][^4][^5][^6][^7][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://arxiv.org/html/2410.02762v1

[^2]: https://openreview.net/group?id=ICLR.cc%2F2023%2FConference

[^3]: https://arxiv.org/html/2505.04769v1

[^4]: https://openreview.net/forum?id=D-zfUK7BR6c

[^5]: https://nlp.cs.berkeley.edu/pubs/Zhai-Bai-Lin-Pan-Tong-Zhou-Suhr-Xie-LeCun-Ma-Levine_2024_Finetuning_paper.pdf

[^6]: https://openreview.net/forum?id=jlAjNL8z5cs

[^7]: https://openreview.net/forum?id=3UDAU2unja

[^8]: https://www2.eecs.berkeley.edu/Pubs/TechRpts/2023/EECS-2023-202.pdf

[^9]: https://openreview.net/forum?id=1tZbq88f27

[^10]: https://www2.eecs.berkeley.edu/Pubs/TechRpts/2024/EECS-2024-96.pdf

[^11]: https://openreview.net/forum?id=9yE2xEj0BH7

[^12]: https://openreview.net/forum?id=HgQR0mXQ1_a

[^13]: https://openreview.net/pdf/695c912cb41743419d359d3224d1ec5f605d986c.pdf

[^14]: https://openreview.net/pdf?id=3UDAU2unja

[^15]: https://openreview.net/profile?id=~Shijia_Yang1

[^16]: https://openreview.net/profile?id=~Huang_Huang1

[^17]: https://openreview.net/profile?id=~Lisa_Dunlap1

[^18]: https://openreview.net/profile?id=~Letian_Fu1

[^19]: https://openreview.net/profile?id=~Jiayi_Pan1

[^20]: https://openreview.net/profile?id=~William_Chen1

[^21]: https://openreview.net/profile?id=~Zhewei_Yao1

[^22]: https://openreview.net/profile?id=~Wenzhao_Zheng1

[^23]: https://openreview.net/pdf?id=9Ebi1euQZQ

[^24]: https://arxiv.org/abs/2310.01779

[^25]: https://openreview.net/forum?id=9Ebi1euQZQ

[^26]: https://openreview.net/attachment?id=9Ebi1euQZQ\&name=supplementary_material

[^27]: https://openreview.net/pdf/84f41b244ad79b4885a1ec05842cb174d9198b36.pdf

[^28]: https://openreview.net/pdf/a72eba39d90097399a5395a98f283c594227a7cc.pdf

[^29]: https://openreview.net/pdf?id=B0buEm1XNH

[^30]: https://openreview.net/profile?id=~Xiangchen_Zhao1

[^31]: https://openreview.net/search?term=~Sheng_Shen2\&content=authors\&group=all\&sort=cdate%3Adesc

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

Extracted From Rubric-1:
Yossi Gandelsman

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
