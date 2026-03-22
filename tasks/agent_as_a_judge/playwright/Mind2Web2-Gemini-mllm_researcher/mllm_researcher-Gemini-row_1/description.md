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

# **Identification of a UC Berkeley Researcher with a Vision and Language Publication at ICLR 2023**

## **Executive Summary: Verified Researcher and Publication**

An exhaustive analysis of the provided materials has successfully identified a researcher who meets the specified criteria: an affiliation with the University of California, Berkeley (UC Berkeley), an accepted paper at the International Conference on Learning Representations (ICLR) 2023, and a research focus directly related to vision and language models. The identified individual is Lisa Dunlap, a PhD student at UC Berkeley. The qualifying publication is titled "Using Language to Extend to Unseen Domains." This paper directly addresses the intersection of computer vision and natural language processing by leveraging language descriptions to improve the generalization capabilities of vision models. The core findings of this investigation are summarized in the table below for immediate reference.

**Table 1: Summary of Findings**

| Category | Details |
| :---- | :---- |
| **Researcher Name** | Lisa Dunlap |
| **UC Berkeley Affiliation** | PhD Student, Department of Electrical Engineering and Computer Sciences (EECS). Advised by Professor Joseph E. Gonzalez and Professor Trevor Darrell within the Berkeley Artificial Intelligence Research (BAIR) lab and the Sky Computing Lab.<sup>1</sup> |
| **ICLR 2023 Paper Title** | Using Language to Extend to Unseen Domains.<sup>3</sup> |
| **OpenReview Link** | https://openreview.net/forum?id=15xQhXQ4rK |

### **Works cited**

1. Lisa Ballard Dunlap, https://www.lisabdunlap.com/  
2. Lisa Dunlap - OpenReview, https://openreview.net/profile?id=~Lisa_Dunlap1  
3. Using Language to Extend to Unseen Domains - OpenReview, https://openreview.net/forum?id=15xQhXQ4rK  
4. Anna Rohrbach – Vision and Language, https://anna-rohrbach.net/  
5. Search | OpenReview, https://openreview.net/search?term=~Aditi_Raghunathan1&content=authors&group=all&source=forum&sort=cdate:desc  
6. ICLR Poster Using Language to Extend to Unseen Domains, https://iclr.cc/virtual/2023/poster/11059  
7. Using Language to Extend to Unseen Domains - OpenReview, https://openreview.net/forum?id=eR2dG8yjnQ  
8. Contact — Lisa Ballard Dunlap, https://www.lisabdunlap.com/contact  
9. Trevor Darrell | Research UC Berkeley, https://vcresearch.berkeley.edu/faculty/trevor-darrell  
10. Prof. Trevor Darrell - People @EECS, https://people.eecs.berkeley.edu/~trevor/  
11. Joseph Gonzalez | Research UC Berkeley, https://vcresearch.berkeley.edu/faculty/joseph-gonzalez  
12. Joseph E. Gonzalez: About - People @EECS, https://people.eecs.berkeley.edu/~jegonzal/  
13. Anna Rohrbach - OpenReview, https://openreview.net/profile?id=~Anna_Rohrbach1  
14. Lisa DUNLAP | University of California, Berkeley, Berkeley | UCB | Department of Electrical Engineering and Computer Sciences | Research profile - ResearchGate, https://www.researchgate.net/profile/Lisa-Dunlap-2  
15. CROSS-MODALITY DEBIASING: USING LANGUAGE TO MITIGATE SUB-POPULATION SHIFTS IN IMAGING - OpenReview, https://openreview.net/pdf?id=o1TKGCrSL7  
16. ICLR Poster Modeling content creator incentives on algorithm-curated platforms, https://iclr.cc/virtual/2023/poster/10716  
17. Modeling content creator incentives on algorithm-curated platforms - OpenReview, https://openreview.net/forum?id=7yV7fb2aBh  
18. Michael Jordan | Research UC Berkeley, https://vcresearch.berkeley.edu/faculty/michael-jordan  
19. Karl Krauth - The Branco Weiss Fellowship, https://brancoweissfellowship.org/fellow/krauth/  
20. CV - Sarah Dean, https://sdean.website/cv.pdf  
21. MODELING CONTENT CREATOR INCENTIVES ON ALGORITHM-CURATED PLATFORMS - OpenReview, https://openreview.net/pdf?id=l6CpxixmUg  
22. Modeling content creator incentives on algorithm-curated platforms ..., https://openreview.net/forum?id=l6CpxixmUg  
23. Joey Hejna, https://joeyhejna.com/  
24. XuDong Frank Wang's Home Page - People @EECS, http://people.eecs.berkeley.edu/~xdwang/  
25. Publications of Professor Yi Ma - People @EECS, https://people.eecs.berkeley.edu/~yima/Publication.html

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
Lisa Dunlap

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
