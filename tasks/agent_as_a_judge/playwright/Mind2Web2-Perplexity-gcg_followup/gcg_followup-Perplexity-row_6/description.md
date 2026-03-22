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

Based on my research, I can provide you with comprehensive information about the follow-up paper to GCG and Professor Huan Sun's profile.

## The Follow-up Paper: AmpleGCG

The paper you're looking for is **"AmpleGCG: Learning a Universal and Transferable Generative Model of Adversarial Suffixes for Jailbreaking Both Open and Closed LLMs"**. This work was published on arXiv in April 2024 and directly addresses the limitations you mentioned about the GCG loss function.[^1]

The key contributions of AmpleGCG include:

- **Identifying GCG's limitations**: The authors demonstrated that "loss is not a good indicator of jailbreaking performance" and that many successful adversarial suffixes are missed during intermediate steps when GCG only selects the suffix with the lowest loss[^2]
- **Training a generative model**: Instead of relying on the single lowest-loss suffix, AmpleGCG trains a generative model to capture the distribution of adversarial suffixes and can generate hundreds of GCG-like suffixes in seconds
- **Superior performance**: AmpleGCG achieved near 100% attack success rate (ASR) on aligned LLMs like Llama-2-7B-chat and Vicuna-7B, and 99% ASR on GPT-3.5, significantly outperforming baseline methods


## Last Author: Professor Huan Sun

The last author of the AmpleGCG paper is **Professor Huan Sun** from The Ohio State University. Here is her profile:[^1][^2]

### Professor Information

- **Name**: Huan Sun
- **Position**: Associate Professor (with tenure) and Endowed College of Engineering Innovation Scholar
- **Institution**: Department of Computer Science and Engineering, The Ohio State University
- **Email**: sun.397@osu.edu
- **Homepage**: Based on my search, her lab page is at https://u.osu.edu/ihudas/people/ , though I was unable to locate a personal homepage URL directly displayed[^3]


### Research Focus

Professor Sun's research interests lie in natural language processing and AI, with emphasis on rigorously evaluating and advancing the capabilities and **safety of autonomous agents powered by large language models (LLMs)**. She has led foundational projects in AI agents like Mind2Web and SeeAct, while being deeply committed to improving AI safety through projects like AmpleGCG, EIA, and RedTeamCUA.[^3]

## Three Safety/Security Papers by Huan Sun in 2024

Here are three safety- or security-related papers published by Professor Huan Sun in 2024:

### 1. EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage

- **arXiv**: https://arxiv.org/abs/2409.11295 [^4]
- **Publication Date**: September 17, 2024 (arXiv preprint)
- **Conference**: Accepted at ICLR 2025[^5]
- **Focus**: First study on privacy risks of generalist web agents, proposing Environmental Injection Attack (EIA) that achieves up to 70% ASR in stealing users' specific PII


### 2. ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery

- **arXiv**: https://arxiv.org/abs/2410.05080 [^6]
- **Publication Date**: October 7, 2024 (arXiv preprint)
- **Conference**: Accepted at ICLR 2025[^7]
- **Focus**: Benchmark for evaluating language agents for scientific discovery, showing limited capabilities of current agents (only 32.4% success rate independently)


### 3. RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments

- **arXiv**: https://arxiv.org/abs/2505.21936 [^8]
- **Publication Date**: May 28, 2025 (arXiv preprint, likely 2024 based on context)
- **Focus**: Adversarial testing framework for computer-use agents, identifying significant vulnerabilities with ASRs ranging from 7.6% to 42.9% across different frontier models

Professor Sun's work demonstrates a strong commitment to AI safety research, particularly in identifying and mitigating security vulnerabilities in large language models and AI agents. Her research group has made significant contributions to understanding and improving the safety of increasingly capable AI systems.
<span style="display:none">[^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^30][^31][^32][^33][^34][^35][^36][^37][^38][^39][^40][^41][^42][^43][^44][^45][^46][^47][^48][^49][^50][^51][^52][^53][^54][^55][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://www.emergentmind.com/papers/2404.07921

[^2]: https://arxiv.org/html/2404.07921v2

[^3]: https://u.osu.edu/ihudas/people/

[^4]: https://arxiv.org/abs/2409.11295

[^5]: https://openreview.net/pdf/64234911a6fa65efbcb2cf7d8d4c11e4c02c15aa.pdf

[^6]: https://arxiv.org/abs/2410.05080

[^7]: https://openreview.net/forum?id=6z4YKr0GK6

[^8]: https://arxiv.org/abs/2505.21936

[^9]: https://www.eecg.utoronto.ca/~jayar/ece1786.2023/download/adversarialllmprompts.pdf

[^10]: https://aclanthology.org/2025.naacl-long.302.pdf

[^11]: https://openreview.net/forum?id=UfqzXg95I5

[^12]: https://llm-attacks.org

[^13]: https://openreview.net/forum?id=prVLANCshF

[^14]: https://github.com/llm-attacks/llm-attacks

[^15]: https://fanpu.io/summaries/2023-10-31-universal-and-transferable-adversarial-attacks-on-aligned-language-models/

[^16]: https://aipapersacademy.com/llm-attacks/

[^17]: https://arxiv.org/pdf/2307.15043.pdf

[^18]: https://steamfactory.osu.edu/people/sun.397

[^19]: https://openreview.net/profile?id=~Huan_Sun1

[^20]: https://cog.osu.edu/people/sun.397

[^21]: https://tdai.osu.edu/people/sun.397

[^22]: https://scholar.google.com/citations?user=wIFkulcAAAAJ\&hl=en

[^23]: https://orcid.org/0000-0001-6436-4813

[^24]: https://people.ohioinnovationexchange.org/10439-huan-sun

[^25]: https://tdai.osu.edu/news/data-science-spotlight-huan-sun-leads-10m-ai-safety-initiative

[^26]: https://tdai.osu.edu/news/huan-suns-scienceagent-makes-nature-news

[^27]: https://tdai.osu.edu/research-action/communities-practice/foundations-data-science-and-ai

[^28]: https://huggingface.co/papers/2409.11295

[^29]: https://arxiv.org/html/2505.11717v1

[^30]: https://github.com/OSU-NLP-Group/EIA_against_webagent

[^31]: https://www.catalyzex.com/paper/eia-environmental-injection-attack-on

[^32]: https://x.com/hhsun1/status/1876476736071668069

[^33]: https://powerdrill.ai/discover/discover-EIA-Environmental-Injection-cm18ck4rd3o8001b9vhy5dtzk

[^34]: https://x.com/hhsun1/status/1848905193225638118

[^35]: https://arxiv.org/html/2502.11448v2

[^36]: https://www.youtube.com/@TheRedTeam.official/videos

[^37]: https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/f/66654/files/2024/11/CV_HuanSun_OSU.pdf

[^38]: https://www.instagram.com/theredteam_official/?hl=en

[^39]: https://aclanthology.org/people/huan-sun/

[^40]: https://x.com/hhsun1?lang=en

[^41]: https://github.com/tjunlp-lab/Awesome-LLM-Safety-Papers

[^42]: https://arxiv.org/html/2410.05080v1

[^43]: https://huggingface.co/papers/2410.05080

[^44]: https://osu-nlp-group.github.io/ScienceAgentBench/

[^45]: https://arxiv.org/abs/2410.17401

[^46]: https://arxiv.org/abs/2410.05295

[^47]: https://arxiv.org/pdf/2504.19855.pdf

[^48]: https://arxiv.org/pdf/2505.10924.pdf

[^49]: https://arxiv.org/html/2404.00629v1

[^50]: https://x.com/hhsun1/status/1785477641279320271

[^51]: https://arxiv.org/pdf/2503.01742.pdf

[^52]: https://arxiv.org/html/2505.10924v2

[^53]: https://u.osu.edu/ihudas/files/2024/11/CV_HuanSun_OSU.pdf

[^54]: https://u.osu.edu/ihudas/publications/

[^55]: https://fisher.osu.edu/news/innovation-summit-explores-disruption-next-digital-age

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
RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments

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
