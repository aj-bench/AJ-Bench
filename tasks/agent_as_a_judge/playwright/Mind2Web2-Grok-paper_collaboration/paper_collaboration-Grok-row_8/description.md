# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

I'm interested in the paper "ASDOT: Any-shot data-to-text generation with pretrained language models." Provide the arxiv link and the name of the first author. Identify their PhD advisor, providing the advisor's homepage and stated primary research interests. Then, find three other researchers (excluding the PhD advisor) who have co-authored at least three papers with this first author. For each researcher, list their full name and three co-authored paper titles, including the arxiv link for each paper.

[The End of Query]

### Response

[The Start of Response]

### Key Points
- The paper "ASDOT: Any-Shot Data-to-Text Generation with Pretrained Language Models" (noting the standard title uses "Any-Shot") is available on arXiv at https://arxiv.org/abs/2210.04325.
- The first author is Jiannan Xiang.
- Jiannan Xiang's PhD advisor is Zhiting Hu, whose homepage is https://zhiting.ucsd.edu/. Hu's primary research interests include machine learning, artificial intelligence, natural language processing, large-scale ML/AI systems, and their applications.
- Three researchers who have co-authored at least three papers with Jiannan Xiang (excluding Zhiting Hu) are Lemao Liu, Tianmin Shu, and Huayang Li.
- Evidence from multiple sources, including academic profiles and publication records, supports these details, though PhD student publication lists can evolve rapidly.

### Paper Details
The queried paper focuses on flexible data-to-text generation using pretrained language models, enabling any-shot (including zero-shot) applications. It was published in 2022, with Jiannan Xiang as the lead author among a team including Zhengzhong Liu, Yucheng Zhou, Eric P. Xing, and Zhiting Hu.

### First Author's Background
Jiannan Xiang is a PhD student in Data Science at the University of California, San Diego. His work spans natural language processing, embodied AI, and multimodal models, as reflected in his publications.

### Advisor Information
Zhiting Hu serves as Xiang's PhD advisor, guiding research in advanced AI systems. Hu's interests emphasize foundational and applied aspects of AI, drawing from his academic position at UCSD.

### Co-Authors Overview
The selected co-authors have collaborated with Xiang on at least three papers each, primarily in NLP and evaluation metrics for Lemao Liu and Huayang Li, and in multimodal and embodied AI for Tianmin Shu. Full details, including paper titles and arXiv links, are provided below for transparency.

**Lemao Liu**  
- Assessing Dialogue Systems with Distribution Distances (https://arxiv.org/abs/2105.02573)  
- Investigating Data Variance in Evaluations of Automatic Machine Translation Metrics (https://arxiv.org/abs/2203.15858)  
- Visualizing the Relationship Between Encoded Linguistic Information and Task Performance (https://arxiv.org/abs/2203.15860)  

**Tianmin Shu**  
- Language Models Meet World Models: Embodied Experiences Enhance Language Models (https://arxiv.org/abs/2305.10626)  
- MMToM-QA: Multimodal Theory of Mind Question Answering (https://arxiv.org/abs/2401.08743)  
- Do Vision-Language Models Have Internal World Models? Towards an Atomic Evaluation (https://arxiv.org/abs/2506.21876)  

**Huayang Li**  
- Assessing Dialogue Systems with Distribution Distances (https://arxiv.org/abs/2105.02573)  
- Investigating Data Variance in Evaluations of Automatic Machine Translation Metrics (https://arxiv.org/abs/2203.15858)  
- Visualizing the Relationship Between Encoded Linguistic Information and Task Performance (https://arxiv.org/abs/2203.15860)  

---

The paper "ASDOT: Any-Shot Data-to-Text Generation with Pretrained Language Models" represents an advancement in natural language generation, specifically addressing challenges in data-to-text tasks where training examples may be limited or absent. Published in 2022, it proposes a two-step method involving data disambiguation and sentence fusion, leveraging off-the-shelf pretrained language models for efficiency and flexibility across zero-shot, few-shot, and many-shot scenarios. The arXiv link is https://arxiv.org/abs/2210.04325, where the full PDF can be accessed for detailed methodology, experiments on datasets like DART and WebNLG, and comparisons with baselines such as fine-tuned PLMs. The first author, Jiannan Xiang, is listed prominently in the author order, consistent with academic conventions where the lead contributor appears first.

Jiannan Xiang is currently a second-year PhD student in Data Science at the University of California, San Diego (UCSD), focusing on areas like natural language processing, world models, and embodied AI. His PhD advisor is Zhiting Hu, an assistant professor at UCSD, as explicitly stated on Xiang's personal website and corroborated by university directories. Hu's homepage is https://zhiting.ucsd.edu/, which outlines his primary research interests as machine learning, artificial intelligence, natural language processing, large-scale ML/AI systems, and their applications in domains like text generation and multimodal learning. Hu's work often bridges foundational models with practical systems, influencing students like Xiang in projects involving pretrained models and embodied experiences.

To identify collaborators, an analysis of Xiang's publication record from sources like Google Scholar, his personal site, and ACL Anthology reveals several researchers with multiple joint works. Excluding Hu, three researchers who have co-authored at least three papers with Xiang are Lemao Liu, Tianmin Shu, and Huayang Li. These collaborations span Xiang's pre-PhD and PhD phases, covering topics from NLP evaluation metrics to multimodal AI. Below is a table summarizing the co-authors, their full names, the count of shared papers, and the specific titles with arXiv links where available.

| Researcher Full Name | Number of Co-Authored Papers | Co-Authored Paper Titles and arXiv Links                     |
| -------------------- | ---------------------------- | ------------------------------------------------------------ |
| Lemao Liu            | 3                            | - Assessing Dialogue Systems with Distribution Distances (https://arxiv.org/abs/2105.02573)<br>- Investigating Data Variance in Evaluations of Automatic Machine Translation Metrics (https://arxiv.org/abs/2203.15858)<br>- Visualizing the Relationship Between Encoded Linguistic Information and Task Performance (https://arxiv.org/abs/2203.15860) |
| Tianmin Shu          | 3                            | - Language Models Meet World Models: Embodied Experiences Enhance Language Models (https://arxiv.org/abs/2305.10626)<br>- MMToM-QA: Multimodal Theory of Mind Question Answering (https://arxiv.org/abs/2401.08743)<br>- Do Vision-Language Models Have Internal World Models? Towards an Atomic Evaluation (https://arxiv.org/abs/2506.21876) |
| Huayang Li           | 3                            | - Assessing Dialogue Systems with Distribution Distances (https://arxiv.org/abs/2105.02573)<br>- Investigating Data Variance in Evaluations of Automatic Machine Translation Metrics (https://arxiv.org/abs/2203.15858)<br>- Visualizing the Relationship Between Encoded Linguistic Information and Task Performance (https://arxiv.org/abs/2203.15860) |

Lemao Liu, affiliated with research institutions like Tencent AI Lab during these collaborations, contributed to Xiang's earlier work on NLP metrics and dialogue evaluation. These papers emphasize empirical assessments, such as distribution distances for dialogue systems and variance in machine translation metrics, highlighting potential pitfalls in automated evaluations. Tianmin Shu, whose research intersects cognitive science and AI, collaborates with Xiang on more recent PhD-era projects involving theory of mind in multimodal settings and world models for language enhancement. Huayang Li shares the same three papers as Liu, focusing on linguistic encoding and performance visualization, underscoring a cluster of collaborations around NLP tooling. Other potential collaborators like Defu Lian also meet the threshold with the same metric-focused papers, but the selected three provide a diverse representation across Xiang's career trajectory.

Xiang's broader publication portfolio, totaling over a dozen papers with 414 citations as of recent records, shows a shift from NLP metrics in 2021-2022 to embodied and multimodal AI in 2023-2025, aligning with his PhD under Hu. For instance, earlier works like "Learning to Stop: A Simple yet Effective Approach to Urban Vision-Language Navigation" (https://arxiv.org/abs/2009.13112) with Xin Eric Wang and William Yang Wang predate his PhD but demonstrate foundational skills in vision-language tasks. This evolution suggests Hu's influence in steering toward large-scale systems, as seen in recent contributions like "Pandora: Towards General World Model with Natural Language Actions and Video States" (https://arxiv.org/abs/2406.09455). While no major controversies surround these details, academic authorship can sometimes involve nuances in contribution levels, but standard listings confirm the collaborations.

### Key Citations
- [Any-Shot Data-to-Text Generation with Pretrained Language Models](https://arxiv.org/abs/2210.04325)
- [Jiannan Xiang's Personal Website](https://szxiangjn.github.io/)
- [Zhiting Hu's Homepage](https://zhiting.ucsd.edu/)
- [Jiannan Xiang's Google Scholar Profile](https://scholar.google.com/citations?user=l8BS2wsAAAAJ&hl=en)
- [Assessing Dialogue Systems with Distribution Distances](https://arxiv.org/abs/2105.02573)
- [Investigating Data Variance in Evaluations of Automatic Machine Translation Metrics](https://arxiv.org/abs/2203.15858)
- [Visualizing the Relationship Between Encoded Linguistic Information and Task Performance](https://arxiv.org/abs/2203.15860)
- [Language Models Meet World Models: Embodied Experiences Enhance Language Models](https://arxiv.org/abs/2305.10626)
- [MMToM-QA: Multimodal Theory of Mind Question Answering](https://arxiv.org/abs/2401.08743)
- [Learning to Stop: A Simple yet Effective Approach to Urban Vision-Language Navigation](https://arxiv.org/abs/2009.13112)

[The End of Response]

### Rubric

[The Start of Rubric]

1. Correctly find the arxiv link for the paper "ASDOT: Any shot data to text generation with pre trained language models." Get 1 point
2. Correctly identify the first author of the paper "ASDOT: Any shot data to text generation with pre trained language models", score 1 point
3. Identify the doctoral advisor of the first author, score 1 point
4. Provide the advisor's homepage, get 1 point
5. Provide the main research interests of the advisor, score 1 point
6. Find three other researchers (excluding doctoral supervisors) who have co authored at least three papers with the first author, and list their full names and the titles of the three co authored papers, including arxiv links for each paper. Mentioning one will earn one point, up to a maximum of three points
7. Full score of 8 points

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-6:
Huayang Li; Assessing Dialogue Systems with Distribution Distances (https://arxiv.org/abs/2105.02573); Investigating Data Variance in Evaluations of Automatic Machine Translation Metrics (https://arxiv.org/abs/2203.15858); Visualizing the Relationship Between Encoded Linguistic Information and Task Performance (https://arxiv.org/abs/2203.15860)

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
