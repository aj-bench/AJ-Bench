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

### Key Points on Perplexity AI Hallucinations
- Research suggests that Perplexity AI, like other generative models, can produce hallucinated responses, including fabricated facts, sources, or summaries, even in its search products like Pro Search and Deep Research. This seems likely due to underlying model limitations rather than intentional design flaws.
- Evidence leans toward these issues being more pronounced in complex queries, where the AI may invent details to fill gaps, such as non-existent events, future dates, or inaccurate attributions, potentially misleading users.
- While not all responses are affected, documented cases highlight the importance of verification, as hallucinations can confuse real information with made-up content, raising concerns for reliability in research or decision-making.

### Overview of Specific Failures
Perplexity AI's hallucinations often manifest as confidently presented but incorrect information, such as inventing sources, events, or details not supported by real data. Below are three sourced examples, each detailing a concrete instance with user input, AI response, and the fabricated elements.

1. **Fabricated Financial Details in Hospital Commissioning Query**  
   A user queried Perplexity about revenue changes after a hospital's oncology wing commissioning. The AI fabricated an entire scenario, claiming a 300 basis point increase in oncology revenue share (from 3% to 6%) in the first full quarter post-commissioning, highlighting advanced procedures like chemotherapy and bone marrow transplants. When pressed on the commissioning date (Q4 2025), Perplexity admitted no evidence existed, contradicting its initial detailed response. This illustrates "gaslighting"-like behavior where invented facts are later denied. Source: X post with screenshots of the interaction.

2. **Invented Sources with Future Dates in Economic Research**  
   In a Deep Research query on China's state ownership of land, banking, and enterprises, Perplexity provided data citing sources dated "July 2025"—an impossible future date at the time of the query (February 2025). The user could not locate these sources, and Perplexity failed to provide direct links, confirming the citations were fabricated. This case shows how the AI can hallucinate non-existent references to bolster responses.

3. **Falsely Attributed and Added Content in News Summaries**  
   Perplexity Pro summarized a New York Post article on a dispute between US Senator Jim Jordan and an EU commissioner, copying two real paragraphs but adding five fabricated ones on free speech and online regulation, attributing them to the Post. Another instance involved falsely claiming WIRED reported a police officer committed a crime he did not. These hallucinations mix real and made-up content, potentially diluting trademarks and confusing readers, as noted in a lawsuit.

### Implications for Users
It appears that while Perplexity aims to ground answers in sources, hallucinations persist, especially in interpretive or data-scarce topics. Users should cross-verify outputs, particularly in professional contexts like finance or journalism, where fabricated details could lead to errors. Ongoing lawsuits and investigations suggest broader industry challenges, but improvements like better retrieval mechanisms may mitigate risks over time.

---

Perplexity AI, as an AI-powered search engine, has been praised for its ability to provide cited responses, but it is not immune to the common issue of hallucinations—where generative AI produces false, misleading, or entirely fabricated information presented as fact. This phenomenon arises from the model's probabilistic nature, training data gaps, or over-reliance on pattern matching rather than true understanding. In the context of Perplexity's products like Pro Search (which emphasizes real-time web sourcing) and Deep Research (for in-depth analysis), hallucinations can manifest as invented URLs, non-existent sources, made-up events, or inaccurate summaries. Below, we delve into documented real-world failures, drawing from user reports, investigations, and lawsuits. These cases are specific, including user queries, AI responses, and verification of errors, to illustrate the problem's scope.

#### Understanding Hallucinations in Perplexity AI
Hallucinations in Perplexity often involve "second-hand" errors, where the AI cites or summarizes sources incorrectly, sometimes laundering fabrications from other AI-generated content. For instance, a GPTZero investigation revealed Perplexity relying on AI-generated sources, leading to passed-down inaccuracies. This is distinct from general AI issues, as Perplexity's design (retrieval-augmented generation) aims to reduce them but doesn't eliminate risks entirely. Common triggers include ambiguous queries, outdated data, or topics with sparse reliable information. While not controversial per se, these failures spark debates on AI reliability, ethics in sourcing, and potential legal liabilities, as seen in lawsuits accusing Perplexity of trademark dilution through mixed real and fabricated content.

#### Detailed Case Studies
Here are three primary examples, each from a distinct source, showcasing concrete hallucinations in Perplexity's search products. These include the user input, AI's response, fabricated elements, and how the error was identified. Additional related instances are noted for completeness.

1. **Fabricated Hospital Commissioning and Revenue Details (Financial Query Hallucination)**  
   - **User Query**: "In the first full quarter after KIMS Hospitals commissioned its Secunderabad oncology wing, by how many basis points did oncology revenue share increase, and what specific service mix change did management highlight?"  
   - **AI Response (from Perplexity)**: The AI claimed that in the first full quarter post-commissioning (prior to Q1 FY26), oncology revenue share increased by 300 basis points (from 3% to 6% of group revenue). It highlighted a shift toward advanced procedures like chemotherapy, radiation oncology, and bone marrow transplants, crediting this for higher average revenue per occupied bed (ARPOB) in the Telangana region. Sources cited included Scribd documents and hospital investor presentations.  
   - **Fabricated Elements**: The entire commissioning event and revenue details were invented; no such oncology wing was commissioned in Q4 2025. The AI manufactured specifics like the 300 basis point increase and service mix changes, presenting them as factual.  
   - **Verification and Follow-Up**: When the user queried, "Are you sure that Sukhendraabad Oncology was commissioned in Q4 2025? And what are the sources of the information?", Perplexity reviewed earnings transcripts and admitted no evidence of commissioning existed, referencing other locations instead (e.g., Anantapur, Ongole). This self-contradiction exemplifies "peak AI gaslighting," where fabricated narratives are later denied. The example was shared via screenshots on X, highlighting the risk in financial research.

2. **Invented Sources with Impossible Dates (Deep Research on Economic Ownership)**  
   - **User Query**: Research on the level of the People's Republic of China's (PRC) state and collective ownership of land, banking, enterprises, etc. (Using Deep Research feature).  
   - **AI Response**: Perplexity provided detailed information on ownership levels, citing multiple sources including one dated "July 2025."  
   - **Fabricated Elements**: The sources were non-existent or unverifiable, with impossible future dates (the query occurred in February 2025, making July 2025 citations fabricated). This created an illusion of up-to-date, authoritative data.  
   - **Verification**: The user attempted to locate the sources independently but failed. When asked for direct links, Perplexity admitted it couldn't find them. This case underscores hallucinations in Deep Research, where the AI invents citations to support responses, potentially misleading users on geopolitical or economic topics. Reported on Reddit as a warning to verify AI outputs independently.

3. **Falsely Attributed News Summaries and Added Content (Pro Search in Journalism)**  
   - **User Query/Context**: Summarization of news articles, such as a New York Post story on US Senator Jim Jordan's dispute with EU Commissioner Thierry Breton over Elon Musk and X (via Perplexity Pro).  
   - **AI Response**: Perplexity copied two paragraphs verbatim from the Post article but appended five generated paragraphs on free speech and online regulation, attributing the entire summary to the Post. In another instance, it falsely claimed WIRED reported a California police officer committed a theft involving a volunteer's bike and wireless headset—a story WIRED did not publish.  
   - **Fabricated Elements**: The added paragraphs were entirely made-up, not present in the original article, creating a hybrid of real and hallucinated content. The WIRED attribution was invented, misrepresenting the outlet's reporting.  
   - **Verification**: A WIRED investigation and subsequent lawsuit by Dow Jones and the New York Post confirmed these as hallucinations, noting they dilute trademarks by injecting "uncertainty and distrust." The lawsuit cites these as examples of Perplexity presenting fabricated material as fact, verified against original articles.

#### Additional Related Instances
For a broader view, consider these supporting cases:
- **Cultural and Travel Queries (Second-Hand Hallucinations)**: In queries like "Cultural festivals in Kyoto, Japan" or "Vietnam's famous floating markets," Perplexity relied on AI-generated sources (e.g., LinkedIn articles), leading to inaccuracies such as describing the permanently closed Cai Be market as operational. Verified via GPTZero's AI detection tools, showing how hallucinations propagate from synthetic content.
- **Physics Problem Blundering**: Physicist David Deutsch queried Perplexity on a relativity scenario ("An object is approaching with relativistic speed..."), and it provided wrong answers akin to bluffing, using phrases from similar but unrelated problems. This highlights factual errors in technical queries.
- **General Substack Critique**: Reports note Perplexity citing non-existent sources or fabricating quotes, creating deceptive authority, though without query-specific details.

#### Comparative Table of Hallucination Types in Perplexity Cases
To organize the patterns, here's a table summarizing the examples by type, impact, and mitigation suggestions:

| Case                          | Hallucination Type       | Fabricated Element                                           | Query Context                  | Impact                                                     | Suggested Mitigation                                         |
| ----------------------------- | ------------------------ | ------------------------------------------------------------ | ------------------------------ | ---------------------------------------------------------- | ------------------------------------------------------------ |
| Hospital Revenue (Financial)  | Invented Event & Data    | Non-existent commissioning, 300 bps increase, service mix details | Pro Search on business metrics | Could mislead investors; financial decisions at risk       | Cross-check with official transcripts or databases           |
| China Ownership (Economic)    | Fake Sources             | Impossible dates (e.g., July 2025), unverifiable links       | Deep Research on geopolitics   | Spreads misinformation on policy; erodes trust in research | Request direct source links; use traditional search engines  |
| News Summaries (Journalistic) | Added/Attributed Content | Made-up paragraphs, false story claims                       | Pro Search summarization       | Trademark dilution; confuses readers on facts vs. fiction  | Compare AI output to original articles; flag for legal review |
| Floating Markets (Travel)     | Passed-Down Errors       | Describing closed sites as active                            | General search                 | Inaccurate planning; user frustration                      | Verify with real-time sources like official tourism sites    |
| Physics Query (Technical)     | Factual Blunders         | Incorrect reasoning/phrases                                  | Standard query                 | Hinders education/scientific use                           | Consult domain experts or multiple AI models                 |

This table illustrates recurring themes: source fabrication (most common), event invention, and content mixing. Impacts range from personal (e.g., wrong travel info) to systemic (e.g., legal disputes), with mitigations emphasizing human oversight.

#### Broader Context and Counterarguments
While these failures are documented, Perplexity has implemented features like real-time citations to combat hallucinations, and not all users encounter them—some reports praise its accuracy over competitors. Counterarguments suggest hallucinations are industry-wide, not unique to Perplexity, stemming from LLM limitations like next-token prediction. However, critics argue Perplexity's search veneer makes errors more insidious, as users assume cited responses are verified. Lawsuits emphasize ethical scraping and hallucination risks, balancing views from stakeholders like publishers (concerned about IP) and AI advocates (focusing on innovation). Ongoing research, such as benchmarks for hallucination detection, suggests stacking tools (e.g., retrieval augmentation, confidence scoring) can reduce occurrences by 20-50%, though complete elimination may be impossible for computable LLMs.

In summary, these examples demonstrate Perplexity's vulnerabilities in producing hallucinated answers, underscoring the need for vigilance. For users, combining AI with manual checks remains key, while developers continue refining models to address these pitfalls.

### Key Citations
- [A Lawsuit Against Perplexity Calls Out Fake News AI Hallucinations](https://www.wired.com/story/dow-jones-new-york-post-sue-perplexity/)
- [Warning about Perplexity AI "Deep Research", it hallucinated...](https://www.reddit.com/r/singularity/comments/1iqjmng/warning_about_perplexity_ai_deep_research_it/)
- [Second-Hand Hallucinations: Investigating Perplexity's AI-Generated Sources](https://gptzero.me/news/gptzero-perplexity-investigation/)
- [X Post on Fabricated Hospital Details](https://x.com/compoundingaiin/status/1956338482307039258)
- [Your AI is Making Shit Up: The Brutal Truth About Hallucinations...](https://readwojtech.substack.com/p/your-ai-is-making-shit-up-the-brutal)
- [X Post on Physics Query Blunder](https://x.com/DavidDeutschOxf/status/1868556239292293222)
- [X Post Criticizing Perplexity for Hallucinations](https://x.com/uwukko/status/1879383678809411995)

[The End of Response]

### Rubric

[The Start of Rubric]

Find links that contain at least one real-world case where Perplexity AI's search products (e.g., Pro Search or Deep Research) generated hallucinatory responses to user inputs—such as fabricated URLs or made-up information. The content of the links must describe specific instances of these hallucinatory responses (e.g., the user's input and the AI's response, or a detailed description of what occurred). Each eligible link found will earn 1 point, with a maximum of 3 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-1:
https://x.com/compoundingaiin/status/1956338482307039258

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
