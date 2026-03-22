# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

I'm looking for real-world examples of failures involving Perplexity AI in the context of AI-powered search. Specifically, I am interested in cases where Perplexity AI's search products (for example, their Pro Search, or Deep Research) produced hallucinated answers—such as fabricated URLs or made-up information. Please find three links, each of which should include at least one concrete example of such a failure (for example, the user input and the AI’s response, or at least a concrete description of what happened). The sources should not merely mention general problems with Perplexity AI, but must describe specific instances where it provided hallucinated responses.

[The End of Query]

### Response

[The Start of Response]

# Examples of Perplexity AI Hallucinations in AI-Powered Search

Below are three documented instances where Perplexity AI’s search products produced fabricated or hallucinated information rather than accurate, verifiable results.

## 1. Fabricated Statistics in Deep Research Summaries

In a detailed “Experimenting with Perplexity’s Deep Research: Real Sources, Fake Facts” post, the author asked Deep Research to summarize HR-related analytics benchmarks. Despite citing real URLs, every single hard number in the AI’s response was unsupported by the linked sources. For example, Deep Research claimed:

- “Current generative AI systems demonstrate 55–70% proficiency in core people analytics functions according to industry benchmarks.”
- “AI systems now process 92% of exit interview analysis and 78% of promotion pipeline forecasting at Meta, according to leaked 2024 implementation reports.”
- “A 2024 Stanford study found that human-AI teams outperformed pure AI systems by 41% in predicting leadership succession conflicts within tech firms.”

None of these statistics appear in the cited articles—the AI clearly fabricated every percentage and study attribution.
Source: Experimenting with Perplexity’s Deep Research: Real Sources, Fake Facts[^1]

## 2. Hallucinated Source Links in “Deep Research”

On Reddit’s r/singularity, a user tested Deep Research by requesting an analysis of PRC state and collective ownership. The AI returned numerous “July 2025” sources that did not exist. When the user clicked through—or even asked Perplexity for the direct URLs—the AI could not locate any of them. The user’s exact prompt (“analysis of the People's Republic of China's state and collective ownership regarding land, banking, and enterprises”) and Deep Research’s inability to verify or fetch the cited sources illustrate a clear case of hallucinated references.
Source: Warning about Perplexity AI “Deep Research”, it hallucinated multiple sources[^2]

## 3. AI-Generated “Source” for Cultural Festivals Prompt

A GPTZero investigation highlighted how even Perplexity’s retrieval-augmented approach can pass along hallucinations when its underlying sources are AI-generated. In one example, a user queried “Cultural festivals in Kyoto, Japan,” and Perplexity’s only cited source was a completely AI-generated LinkedIn article that never existed. Similarly, a search for Vietnam’s floating markets returned the now-closed Cai Be market as an active destination—another fabricated detail. Although Perplexity displayed links, those links led to nonexistent or irrelevant content, demonstrating how hallucinated source fabrications can propagate into user answers.
Source: Second-Hand Hallucinations: Investigating Perplexity’s AI Sources[^3]
<span style="display:none">[^10][^11][^12][^4][^5][^6][^7][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://substack.com/home/post/p-158859631

[^2]: https://www.reddit.com/r/singularity/comments/1iqjmng/warning_about_perplexity_ai_deep_research_it/

[^3]: https://gptzero.me/news/gptzero-perplexity-investigation/

[^4]: https://geekycuriosity.substack.com/p/how-to-fact-check-and-eliminate-hallucination

[^5]: https://www.linkedin.com/posts/geniuslabgear_introducing-perplexity-deep-research-activity-7311401703629561856-5f4N

[^6]: https://www.nngroup.com/articles/ai-hallucinations/

[^7]: https://www.perplexity.ai/page/openais-o3-and-o4-mini-models-rVlXQo9jQ9KiH7TUHYvVAQ

[^8]: https://www.perplexity.ai/help-center/en/articles/10354919-what-advanced-ai-models-are-included-in-a-perplexity-pro-subscription

[^9]: https://www.reddit.com/r/perplexity_ai/comments/1jjcj1s/perplexity_fabricated_datadeep_research/

[^10]: https://library.ycp.edu/c.php?g=1387233\&p=10262462

[^11]: https://www.youreverydayai.com/perplexity-deep-research-what-it-is-and-if-you-should-use-it/

[^12]: https://www.ignorance.ai/p/hallucinations-are-fine-actually

[The End of Response]

### Rubric

[The Start of Rubric]

Find links that contain at least one real-world case where Perplexity AI's search products (e.g., Pro Search or Deep Research) generated hallucinatory responses to user inputs—such as fabricated URLs or made-up information. The content of the links must describe specific instances of these hallucinatory responses (e.g., the user's input and the AI's response, or a detailed description of what occurred). Each eligible link found will earn 1 point, with a maximum of 3 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-1:
https://substack.com/home/post/p-158859631

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
