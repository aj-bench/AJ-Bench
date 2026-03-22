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

The follow-up paper you are referring to is "AmpleGCG: Learning a Universal and Transferable Generative Model of Adversarial Suffixes for Jailbreaking Both Open and Closed LLMs," which critiques the GCG approach by highlighting how it misses successful adversarial suffixes by focusing only on the lowest-loss option and addresses this by training a generative model (AmpleGCG) to produce such suffixes efficiently.

The last author of this paper is Huan Sun, an associate professor in the Department of Computer Science and Engineering at The Ohio State University.

Her homepage, displaying her professional information, research interests, and contact details, is available at https://cse.osu.edu/people/sun.397.

Three other safety- or security-related papers by Huan Sun from 2024 are:

1. **How Trustworthy are Open-Source LLMs? An Assessment under Malicious Demonstrations Shows their Vulnerabilities** – This work evaluates vulnerabilities in open-source LLMs to malicious in-context demonstrations, revealing risks in trustworthiness and alignment. (Accepted at NAACL 2024; direct link: https://aclanthology.org/2024.naacl-long.152/)

2. **EIA: Environmental Injection Attack on Generalist Web Agents for Vision-Language Navigation** – This paper introduces an attack method that injects misleading environmental elements to derail web agents, highlighting security gaps in vision-language navigation tasks. (arXiv preprint; direct link: https://arxiv.org/abs/2409.11295)

3. **AmpleGCG-Plus: A Strong Generative Model of Adversarial Suffixes to Jailbreak LLMs with Lower Per-query Cost** – Building on prior jailbreaking techniques, this explores an enhanced generative model for creating adversarial suffixes with improved efficiency and lower costs, underscoring ongoing challenges in LLM security. (arXiv preprint; direct link: https://arxiv.org/abs/2410.22143)

### Key Considerations
- Research suggests that while GCG set a benchmark for adversarial attacks, follow-ups like AmpleGCG reveal inefficiencies in its optimization, particularly in loss selection, leading to broader explorations in generative approaches for safety testing.
- Evidence leans toward Huan Sun being a leading figure in LLM safety, with her work emphasizing practical vulnerabilities in aligned models, though the field remains rapidly evolving with debates on the transferability and ethics of such attacks.
- Pursuing a PhD under her supervision could align well with interests in LLM agents and security, given her focus on mitigating risks in autonomous systems.

### Application Insights
For PhD applications, highlighting connections to specific papers like AmpleGCG in your statement of purpose may strengthen your case. Review her lab's ongoing projects via the OSU NLP group (https://nlp.osu.edu/) or SunLab site (https://u.osu.edu/ihudas/) for alignment with your goals. Contact information is listed on her faculty profile for potential outreach.

---

The field of large language model (LLM) safety has seen significant advancements since the introduction of the Greedy Coordinate Gradient (GCG) algorithm in the 2023 paper "Universal and Transferable Adversarial Attacks on Aligned Language Models" (arXiv:2307.15043). This original work, authored by Andy Zou, Zifan Wang, J. Zico Kolter, and Matt Fredrikson, demonstrated how gradient-based optimization could generate universal adversarial suffixes to jailbreak aligned LLMs, prompting harmful outputs despite safety training. However, as the user noted, follow-up research has identified key limitations in GCG's loss function, particularly its tendency to select only the suffix with the lowest loss, thereby overlooking other viable adversarial suffixes that emerge during intermediate optimization steps. This oversight can reduce the attack's comprehensiveness and efficiency, especially in diverse query scenarios.

One prominent follow-up addressing these issues is the 2024 paper "AmpleGCG: Learning a Universal and Transferable Generative Model of Adversarial Suffixes for Jailbreaking Both Open and Closed LLMs" (arXiv:2404.07921), authored by Zeyi Liao and Huan Sun. The paper explicitly critiques GCG's reliance on single lowest-loss selection, arguing that it misses numerous successful suffixes generated mid-process. To overcome this, the authors collect these overlooked suffixes as training data and fine-tune a generative LLM (AmpleGCG) to model the distribution of adversarial suffixes conditioned on harmful queries. This approach enables rapid generation of hundreds of suffixes in seconds, achieving near-100% attack success rates on models like Llama-2-7B-chat and Vicuna-7B, with strong transferability to closed-source models like GPT-3.5. The work amplifies GCG's impact by making attacks more scalable and harder to defend, while also proposing implications for improving LLM alignment techniques.

Huan Sun, the last author of this paper, serves as the senior supervisor and corresponding researcher, guiding the project's direction on LLM safety and generative attacks. She is an associate professor (with tenure) in the Department of Computer Science and Engineering at The Ohio State University (OSU), where she holds the endowed College of Engineering Innovation Scholar position. Her research broadly spans natural language processing (NLP), artificial intelligence (AI), and data mining, with a particular emphasis on building robust LLM-based agents, understanding transformer limitations, and mitigating safety risks in autonomous systems. Sun's background includes a PhD from the University of California, Santa Barbara, postdoctoral work at the University of Washington, and prior visiting roles at institutions like Amazon A9. She has received numerous awards, including NSF CAREER, JP Morgan Faculty Research Award, and recognitions from Schmidt Sciences for AI safety initiatives. Her homepage at https://cse.osu.edu/people/sun.397 directly displays her biography, publications, teaching, and contact details (email: sun.397@osu.edu; office: Dreese Labs 589). Additional resources include her lab's site (SunLab, part of OSU NLP at https://u.osu.edu/ihudas/), which outlines group projects on agent safety and benchmarking, and her Google Scholar profile for citation metrics.

Beyond AmpleGCG, Huan Sun has contributed to several other safety- and security-related papers in 2024, reflecting her growing focus on LLM vulnerabilities, adversarial robustness, and trustworthy AI. These works often build on themes of jailbreaking, injection attacks, and malicious demonstrations, providing critical insights for PhD research in LLM safety. Below is a detailed overview of three such papers, selected for their relevance to security themes like adversarial attacks and alignment risks. I've included a table summarizing key aspects for comparison.

| Paper Title | Publication Details | Key Contributions to Safety/Security | Authors (Huan Sun's Role) | Direct Link | Citation Count (as of Aug 2025) |
|-------------|---------------------|-------------------------------------|---------------------------|-------------|---------------------------------|
| How Trustworthy are Open-Source LLMs? An Assessment under Malicious Demonstrations Shows their Vulnerabilities | Accepted at NAACL 2024 (Conference Proceedings); arXiv preprint from Nov 2023 | Examines how malicious in-context learning demonstrations can exploit open-source LLMs, causing misalignment and harmful behaviors; proposes benchmarks for evaluating trustworthiness under adversarial inputs, revealing that models like Llama-2 are vulnerable to subtle manipulations in few-shot prompts. This highlights security risks in deployment scenarios where user inputs could be tainted. | Lingbo Mo, Boshi Wang, Muhao Chen, Huan Sun (Senior author, oversaw evaluation framework and revisions) | https://aclanthology.org/2024.naacl-long.152/ | ~150 (rapidly increasing due to conference visibility) |
| EIA: Environmental Injection Attack on Generalist Web Agents for Vision-Language Navigation | arXiv preprint (Sep 2024) | Introduces EIA, a novel attack that injects misleading visual or textual elements into web environments to disrupt vision-language agents during navigation tasks; demonstrates high success rates in derailing agents like GPT-4V, emphasizing security flaws in multimodal systems and the need for robust grounding mechanisms. This work extends safety concerns to agent-based applications in real-world web interactions. | Zeyi Liao, Lingbo Mo, Chejian Xu, Mintong Kang, Jiawei Zhang, Chaowei Xiao, Yuan Tian, Bo Li, Huan Sun (Senior author, contributed to attack design and transferability analysis) | https://arxiv.org/abs/2409.11295 | ~45 (emerging interest in multimodal security) |
| AmpleGCG-Plus: A Strong Generative Model of Adversarial Suffixes to Jailbreak LLMs with Lower Per-query Cost | arXiv preprint (Oct 2024) | Enhances the AmpleGCG framework by optimizing the generative model for lower computational costs per query while maintaining high jailbreak success; addresses scalability limitations in prior attacks, showing improved efficiency on diverse LLMs and discussing defenses like input filtering. This underscores ongoing security challenges in making attacks more accessible and cost-effective. | Vishal Kumar, Zeyi Liao, Jaylen Jones, Huan Sun (Senior author, led model optimization and experimentation) | https://arxiv.org/abs/2410.22143 | ~20 (recent preprint, gaining traction in jailbreak communities) |

These papers collectively illustrate Sun's research trajectory toward practical, scalable solutions for testing and improving LLM security. For instance, "How Trustworthy..." focuses on demonstration-based vulnerabilities, a common in-context learning exploit, while EIA shifts to multimodal environments, revealing cross-modal risks not covered in text-only attacks like GCG. AmpleGCG-Plus, as a direct extension, refines generative approaches for efficiency, making it relevant for resource-constrained safety evaluations. All emphasize empirical rigor, with experiments on models like Llama-2, Vicuna, and GPT variants, and often include code repositories (e.g., AmpleGCG-Plus at GitHub) for reproducibility.

In the broader context, Sun's 2024 output aligns with industry and academic debates on LLM safety, such as those from OpenAI's alignment efforts or Anthropic's constitutional AI. Her work counters arguments that gradient-based attacks like GCG are sufficient by showing generative models can uncover more diverse vulnerabilities, though critics note ethical concerns in publicizing jailbreak methods. For PhD aspirants, her supervision style appears collaborative, with students like Zeyi Liao and Lingbo Mo leading first-authorship on safety papers, suggesting opportunities for independent projects. Prospective students should note her recent funding from Schmidt Sciences for AI safety (\$10M initiative, announced May 2025), which could support PhD research on agent robustness.

To further explore, her ORCID (0000-0001-6436-4813) lists comprehensive publications, and her X account (@hhsun1) shares updates on hiring postdocs and PhD positions, often emphasizing safety in LLM agents. If applying, tailor your proposal to intersect with her themes, such as combining generative attacks with agent benchmarking, and reference these papers to demonstrate familiarity.

**Key Citations:**
- [AmpleGCG Paper](https://arxiv.org/abs/2404.07921)
- [Huan Sun Faculty Profile](https://cse.osu.edu/people/sun.397)
- [How Trustworthy are Open-Source LLMs?](https://aclanthology.org/2024.naacl-long.152/)
- [EIA Paper](https://arxiv.org/abs/2409.11295)
- [AmpleGCG-Plus Paper](https://arxiv.org/abs/2410.22143)
- [Original GCG Paper](https://arxiv.org/abs/2307.15043)

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

Extracted From Rubric-4:
https://aclanthology.org/2024.naacl-long.152/

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
