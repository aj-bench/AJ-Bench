# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

I am applying for a PhD program with a focus on large language model (LLM) safety. A notable paper in this field is *"Universal and Transferable Adversarial Attacks on Aligned Language Models,"* which introduced the GCG algorithm and has inspired numerous follow-up studies. I recall that one of these follow-up works identified certain limitations in the GCG loss function and trained an LLM to generate GCG-like suffixes. Could you help me find that paper?

I am particularly interested in pursuing a PhD under the supervision of the last author of that follow-up paper. Could you identify who the last author is, find his/her homepage where their information is directly displayed, and list three other safety- or security-related papers published by this professor in 2024 (including both arXiv preprints and papers accepted at conferences in 2024), and provide direct links to each.

[The End of Query]

### Response

[The Start of Response]

# The Successor Paper: "AmpleGCG" and its Methodological Contributions

The research paper that directly matches the query's description—one that critiques the GCG algorithm's reliance on its loss function and trains a separate LLM to generate adversarial suffixes—is "AmpleGCG: Learning a Universal and Transferable Generative Model of Adversarial Suffixes for Jailbreaking Both Open and Closed LLMs" by Zeyi Liao and Huan Sun.<sup>8</sup> This work, accepted at the inaugural Conference on Language Modeling (COLM) in 2024, represents a significant evolution of the GCG concept, moving from a pure optimization framework to a hybrid optimization-and-generation approach.<sup>10</sup>

# Principal Investigator Profile: Professor Huan Sun, The Ohio State University

The last author of the "AmpleGCG" paper, and the principal investigator leading this line of research, is Professor Huan Sun.<sup>8</sup>

Professor Sun's official university and lab homepage, which provides the most comprehensive overview of her research group, students, and publications, can be accessed directly at the following URL:

- Homepage: https://u.osu.edu/ihudas/people/ <sup>17</sup>

# A Curated Overview of Professor Sun's 2024 Research in AI Safety and Security

Table 1: Professor Huan Sun: Selected 2024 Publications on LLM Safety & Security

| Title | Venue / Year | Core Contribution | Direct Link to PDF |
| :---- | :---- | :---- | :---- |
| 1. A Trembling House of Cards? Mapping Adversarial Attacks against Language Agents | arXiv Preprint (Feb. 2024) | Proposes the first systematic conceptual framework for understanding and categorizing adversarial attacks against LLM-powered agents, breaking down vulnerabilities across Perception, Brain, and Action components. | https://arxiv.org/pdf/2402.10196 |
| 2. How Trustworthy are Open-Source LLMs? An Assessment under Malicious Demonstrations Shows their Vulnerabilities | NAACL (2024) | Conducts a large-scale empirical assessment of open-source LLMs across eight trustworthiness dimensions, demonstrating their vulnerability to attack via malicious in-context demonstrations (a different vector than adversarial suffixes). | https://aclanthology.org/2024.naacl-long.152.pdf |
| 3. EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage | ICLR (2025 Submission) / arXiv (2024) | Introduces a novel and stealthy attack vector, Environmental Injection Attack (EIA), where an adversary manipulates a web environment (e.g., a webpage's HTML) to trick a web agent into leaking private user data. | https://lzy37ld.github.io/files/eia.pdf |

## Works cited

1. Universal and Transferable Adversarial Attacks on Aligned Language Models, https://www.semanticscholar.org/paper/Universal-and-Transferable-Adversarial-Attacks-on-Zou-Wang/47030369e97cc44d4b2e3cf1be85da0fd134904a  
2. (PDF) Universal and Transferable Adversarial Attacks on Aligned Language Models, https://www.researchgate.net/publication/372684204_Universal_and_Transferable_Adversarial_Attacks_on_Aligned_Language_Models  
3. Universal and Transferable Adversarial Attacks on Aligned Language Models - arXiv, https://arxiv.org/html/2307.15043v2  
4. Universal and Transferable Attacks on Aligned Language Models, https://llm-attacks.org/  
5. Greedy Coordinate Gradient (GCG): The Essential Guide | Nightfall AI Security 101, https://www.nightfall.ai/ai-security-101/greedy-coordinate-gradient-gcg  
6. Exploiting the Index Gradients for Optimization-Based Jailbreaking on Large Language Models - ACL Anthology, https://aclanthology.org/2025.coling-main.305.pdf  
7. Universal and Transferable Adversarial Attacks on Aligned Language Models, https://tuananhbui89.github.io/blog/2024/paper-llm-attacks/  
8. [2404.07921] AmpleGCG: Learning a Universal and Transferable Generative Model of Adversarial Suffixes for Jailbreaking Both Open and Closed LLMs - arXiv, https://arxiv.org/abs/2404.07921  
9. AmpleGCG: Learning a Universal and Transferable Generative Model of Adversarial Suffixes for Jailbreaking Both Open and Closed LLMs - Semantic Scholar, https://www.semanticscholar.org/paper/AmpleGCG%3A-Learning-a-Universal-and-Transferable-of-Liao-Sun/4ad33969188555b8303b375e18f5c117a68387c6  
10. [Literature Review] AmpleGCG: Learning a Universal and Transferable Generative Model of Adversarial Suffixes for Jailbreaking Both Open and Closed LLMs - Moonlight, https://www.themoonlight.io/en/review/amplegcg-learning-a-universal-and-transferable-generative-model-of-adversarial-suffixes-for-jailbreaking-both-open-and-closed-llms  
11. Zeyi Liao, https://lzy37ld.github.io/  
12. GCG: Adversarial Attacks on Large Language Models | by Brian Pulfer | Medium, https://medium.com/@brianpulfer/gcg-adversarial-attacks-on-large-language-models-61f8b51734e9  
13. AmpleGCG: Learning a Universal and Transferable Generative Model of Adversarial Suffixes for Jailbreaking Both Open and Closed LLMs - arXiv, https://arxiv.org/html/2404.07921v2  
14. AmpleGCG: Learning a Universal and Transferable Generative Model of Adversarial Suffixes for Jailbreaking Both Open and Closed LLMs | OpenReview, https://openreview.net/forum?id=UfqzXg95I5  
15. AmpleGCG: Learning a Universal and Transferable Generative ..., https://arxiv.org/pdf/2404.07921  
16. Huan Sun - Translational Data Analytics Institute - The Ohio State University, https://tdai.osu.edu/people/sun.397  
17. People | SunLab, part of OSU NLP - U.OSU - The Ohio State University, https://u.osu.edu/ihudas/people/  
18. Huan Sun, https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/f/66654/files/2024/11/CV_HuanSun_OSU.pdf  
19. A Trembling House of Cards? Mapping Adversarial Attacks against Language Agents - arXiv, https://arxiv.org/abs/2402.10196  
20. A Trembling House of Cards? Mapping Adversarial Attacks against Language Agents - GitHub, https://github.com/OSU-NLP-Group/AgentAttack  
21. [Literature Review] A Trembling House of Cards? Mapping Adversarial Attacks against Language Agents - Moonlight, https://www.themoonlight.io/en/review/a-trembling-house-of-cards-mapping-adversarial-attacks-against-language-agents  
22. OSU-NLP-Group/Eval-LLM-Trust - GitHub, https://github.com/OSU-NLP-Group/Eval-LLM-Trust  
23. How Trustworthy are Open-Source LLMs? An Assessment under Malicious Demonstrations Shows their Vulnerabilities - ACL Anthology, https://aclanthology.org/2024.naacl-long.152.pdf  
24. How Trustworthy are Open-Source LLMs? An Assessment under Malicious Demonstrations Shows their Vulnerabilities Content Warning: This paper contains potentially offensive and harmful text. - arXiv, https://arxiv.org/html/2311.09447v2  
25. About Me - Mo, Lingbo (莫凌波), https://molingbo.github.io/

[The End of Response]

### Rubric

[The Start of Rubric]

1. Correctly identify a research paper in the field of Large Language Models (LLMs) requested in the query. Award 1 point for successful identification.
2. Correctly identify the corresponding author of this paper, award 1 point; provide a direct link to a relevant webpage presenting their information, award 1 point. Maximum 2 points.
3. Correctly identify other safety- or security-related papers published by the corresponding author in 2024 related to LLM security (including arXiv preprints and papers accepted by academic conferences in 2024). Award 1 point for each correctly identified paper, up to 3 points.
4. Based on fulfilling requirement 3, provide direct links to these three papers. Award 1 point for each valid link provided, up to 3 points.
5. The total possible score is 9 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-3:
A Trembling House of Cards? Mapping Adversarial Attacks against Language Agents

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
