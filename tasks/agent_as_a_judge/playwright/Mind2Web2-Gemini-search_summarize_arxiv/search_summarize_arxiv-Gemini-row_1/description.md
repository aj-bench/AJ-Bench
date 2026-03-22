# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Find 10 papers related to web agents published on arXiv between January 2023 and September 2024 (based on the submission time of the first version). For each paper, provide the paper name, a link to the pdf, the name and the affiliation of the first author and submission time of the first version on arXiv.

[The End of Query]

### Response

[The Start of Response]

# Annotated Analysis of Key Publications in Web Agent Research

Table 1: Summary of Selected arXiv Publications on Web Agents (Jan 2023 - Sep 2024)

| Paper Title | arXiv ID & PDF Link | First Author & Affiliation | v1 Submission Date | Core Contribution |
| :---- | :---- | :---- | :---- | :---- |
| WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models | 2401.13919([https://arxiv.org/pdf/2401.13919](https://arxiv.org/pdf/2401.13919)) | Wenhao Yu (Tencent AI Lab) | 25 Jan 2024 | Introduces a Large Multimodal Model (LMM)-powered agent that leverages both visual (screenshots) and textual information for robust end-to-end navigation on real-world websites.<sup>1</sup> |
| AutoWebGLM: A Large Language Model-based Web Navigating Agent | 2404.03648([https://arxiv.org/pdf/2404.03648](https://arxiv.org/pdf/2404.03648)) | Hanyu Lai (Tsinghua University) | 04 Apr 2024 | Develops an open-source web agent based on a 6B parameter model, using novel data strategies, curriculum learning, and HTML simplification to achieve performance comparable to proprietary models.<sup>3</sup> |
| Tree Search for Language Model Agents | 2407.01476([https://arxiv.org/pdf/2407.01476](https://arxiv.org/pdf/2407.01476)) | Jing Yu Koh (Carnegie Mellon University) | July 2024 (est.) | Proposes a novel inference-time, best-first tree search algorithm that allows LM agents to perform explicit multi-step planning and exploration, significantly improving success rates on complex web tasks.<sup>7</sup> |
| Agent-E: A State-of-the-Art Web Agent for Complex Task Automation | 2407.13032([https://arxiv.org/pdf/2407.13032](https://arxiv.org/pdf/2407.13032)) | Shishir G. Patil (Emergence AI) | July 2024 (est.) | Presents a hierarchical agent architecture that separates high-level task planning (Planner Agent) from low-level browser interaction (Browser Navigation Agent) to manage complexity and environmental noise.<sup>5</sup> |
| WebPilot: A Versatile and Autonomous Multi-Agent System for Web Task Execution with Strategic Exploration | 2408.15978([https://arxiv.org/pdf/2408.15978](https://arxiv.org/pdf/2408.15978)) | Yao Zhang (Various) | August 2024 (est.) | Implements a multi-agent system that uses a dual optimization strategy, combining global task decomposition with a localized Monte Carlo Tree Search (MCTS) for sub-task execution, emulating human-like adaptability.<sup>9</sup> |

## WebVoyager: The Dawn of Multimodal Web Navigation

- Bibliographic Data:
  - Paper Name: WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models
  - PDF Link: [https://arxiv.org/pdf/2401.13919](https://arxiv.org/pdf/2401.13919)
  - First Author: Wenhao Yu
  - Affiliation: Tencent AI Lab
  - v1 Submission Time: Thu, 25 Jan 2024 03:33:18 UTC <sup>1</sup>

## AutoWebGLM: Democratizing High-Performance Web Agents

- Bibliographic Data:
  - Paper Name: AutoWebGLM: A Large Language Model-based Web Navigating Agent
  - PDF Link: [https://arxiv.org/pdf/2404.03648](https://arxiv.org/pdf/2404.03648)
  - First Author: Hanyu Lai
  - Affiliation: Tsinghua University <sup>3</sup>
  - v1 Submission Time: Thu, 4 Apr 2024 <sup>3</sup>

## Tree Search for Language Model Agents: Introducing Deliberate Planning

- Bibliographic Data:
  - Paper Name: Tree Search for Language Model Agents
  - PDF Link: [https://arxiv.org/pdf/2407.01476](https://arxiv.org/pdf/2407.01476)
  - First Author: Jing Yu Koh
  - Affiliation: Carnegie Mellon University <sup>7</sup>
  - v1 Submission Time: July 2024 (estimated from arXiv ID 2407.01476)

## Agent-E: A Hierarchical Approach to Taming Complexity

- Bibliographic Data:
  - Paper Name: Agent-E: A State-of-the-Art Web Agent for Complex Task Automation
  - PDF Link: [https://arxiv.org/pdf/2407.13032](https://arxiv.org/pdf/2407.13032)
  - First Author: Shishir G. Patil
  - Affiliation: Emergence AI <sup>8</sup>
  - v1 Submission Time: July 2024 (estimated from arXiv ID 2407.13032)

## WebPilot: Achieving Adaptability through Multi-Agent Exploration

- Bibliographic Data:
  - Paper Name: WebPilot: A Versatile and Autonomous Multi-Agent System for Web Task Execution with Strategic Exploration
  - PDF Link: [https://arxiv.org/pdf/2408.15978](https://arxiv.org/pdf/2408.15978)
  - First Author: Yao Zhang
  - Affiliation: Various
  - v1 Submission Time: August 2024 (estimated from arXiv ID 2408.15978)

### Works cited

1. arxiv.org, [https://arxiv.org/abs/2401.13919](https://arxiv.org/abs/2401.13919)  
2. Tree Search for Language Model Agents | Request PDF - ResearchGate, [https://www.researchgate.net/publication/381911069_Tree_Search_for_Language_Model_Agents](https://www.researchgate.net/publication/381911069_Tree_Search_for_Language_Model_Agents)  
3. [2404.03648] AutoWebGLM: A Large Language Model-based Web Navigating Agent - arXiv, [https://arxiv.org/abs/2404.03648](https://arxiv.org/abs/2404.03648)  
4. [2503.23350] A Survey of WebAgents: Towards Next-Generation AI Agents for Web Automation with Large Foundation Models - arXiv, [https://arxiv.org/abs/2503.23350](https://arxiv.org/abs/2503.23350)  
5. Agent-E: From Autonomous Web Navigation to Foundational Design Principles in Agentic Systems - arXiv, [https://arxiv.org/html/2407.13032v1](https://arxiv.org/html/2407.13032v1)  
6. AutoWebGLM: A Large Language Model-based Web Navigating Agent - arXiv, [https://arxiv.org/html/2404.03648v2](https://arxiv.org/html/2404.03648v2)  
7. Tree Search for Language Model Agents, [https://arxiv.org/abs/2407.01476](https://arxiv.org/abs/2407.01476)  
8. Emergence AI Proposes Agent-E: A Web Agent Achieving 73.2% Success Rate with a 20% Improvement in Autonomous Web Navigation : r/machinelearningnews - Reddit, [https://www.reddit.com/r/machinelearningnews/comments/1edl4qj/emergence_ai_proposes_agente_a_web_agent/](https://www.reddit.com/r/machinelearningnews/comments/1edl4qj/emergence_ai_proposes_agente_a_web_agent/)  
9. arxiv.org, [https://arxiv.org/abs/2408.15978](https://arxiv.org/abs/2408.15978)  
10. WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models - GitHub, [https://github.com/MinorJerry/WebVoyager](https://github.com/MinorJerry/WebVoyager)  
11. Tree Search for Language Model Agents - Jing Yu Koh, [https://jykoh.com/search-agents](https://jykoh.com/search-agents)  
12. Beyond Reflex: A Deep Dive into Language Agent Tree Search (LATS) for Deliberate AI Problem-Solving | by Vi Q. Ha | Jul, 2025 | Medium, [https://medium.com/@vi.ha.engr/beyond-reflex-a-deep-dive-into-language-agent-tree-search-lats-for-deliberate-ai-problem-solving-343157e6111f](https://medium.com/@vi.ha.engr/beyond-reflex-a-deep-dive-into-language-agent-tree-search-lats-for-deliberate-ai-problem-solving-343157e6111f)  
13. [Literature Review] WebPilot: A Versatile and Autonomous Multi-Agent System for Web Task Execution with Strategic Exploration - Moonlight, [https://www.themoonlight.io/en/review/webpilot-a-versatile-and-autonomous-multi-agent-system-for-web-task-execution-with-strategic-exploration](https://www.themoonlight.io/en/review/webpilot-a-versatile-and-autonomous-multi-agent-system-for-web-task-execution-with-strategic-exploration)  
14. WebPilot: A Versatile and Autonomous Multi-Agent System for Web Task Execution with Strategic Exploration - Paper Without Code, [https://paperwithoutcode.com/webpilot-a-versatile-and-autonomous-multi-agent-system-for-web-task-execution-with-strategic-exploration/](https://paperwithoutcode.com/webpilot-a-versatile-and-autonomous-multi-agent-system-for-web-task-execution-with-strategic-exploration/)  
15. WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models - Hugging Face, [https://huggingface.co/papers/2401.13919](https://huggingface.co/papers/2401.13919)  
16. [2507.21206] Agentic Web: Weaving the Next Web with AI Agents - arXiv, [https://arxiv.org/abs/2507.21206](https://arxiv.org/abs/2507.21206)  
17. [2506.18959] From Web Search towards Agentic Deep Research: Incentivizing Search with Reasoning Agents - arXiv, [https://arxiv.org/abs/2506.18959](https://arxiv.org/abs/2506.18959)  
18. From Web Search towards Agentic Deep Research: Incentivizing Search with Reasoning Agents - arXiv, [https://arxiv.org/html/2506.18959](https://arxiv.org/html/2506.18959)  
19. The Agentic Web: The Next Wave to Disrupt the Internet - 36氪, [https://eu.36kr.com/en/p/3412637779922567](https://eu.36kr.com/en/p/3412637779922567)  
20. August | 2025 - viztales, [https://viztales.com/2025/08/](https://viztales.com/2025/08/)  
21. [2410.13232] Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation - arXiv, [https://arxiv.org/abs/2410.13232](https://arxiv.org/abs/2410.13232)

[The End of Response]

### Rubric

[The Start of Rubric]

1. Provide 10 papers related to Web agents published on arXiv. The submission time of the first version must be between January 2023 and September 2024. 1 point will be awarded for each correctly identified paper that meets the requirements along with its title, with a maximum of 10 points.
2. Provide the PDF link of the papers meeting the above requirements, the name and affiliation of the first author, and the submission time of the first version on arXiv. 1 point will be awarded for each complete set of correct information of a paper that meets the requirements, with a maximum of 10 points.
3. Full score: 20 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-1:
WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models

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
