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

# Case Studies in AI Hallucination

## Case Study 1: The Misinformation Loop — Citing AI-Generated Spam for Factual Queries

### Perplexity's Response and Failure

In response to the query, Perplexity generated a coherent and plausible-sounding list of cultural attractions and festivals in the Japanese city. However, the platform cited only a single source for its information: an obscure blog post published on LinkedIn in November 2023.<sup>2</sup> Further analysis by GPTZero, and corroborated by a second detection tool used by *Forbes*, revealed that this source article showed telltale signs of being entirely AI-generated itself.<sup>2</sup>

## Case Study 2: Data Fabrication in Deep Research — Inventing Quantitative Evidence

### Incident Description

An illustrative example comes from a user on the official Perplexity AI subreddit who used the Deep Research mode to investigate the **"reasons for decline in the Indian stock market"**.<sup>8</sup> This is a complex financial query where the accuracy of numerical data is paramount for any meaningful analysis.

### Perplexity's Response and Failure

The Deep Research mode produced a detailed and authoritative-sounding report. It included highly specific financial metrics, stating: *"Despite the correction, Nifty 50 trades at a 12-month forward P/E of 22.3x—a 15% premium to its 10-year average. Q3 FY25 earnings disappointed, with 45% of Nifty companies missing revenue estimates and 52% undershooting EBITDA projections, particularly in IT and consumer staples."*.<sup>8</sup> The report duly cited its sources for this information.

However, when the user attempted to verify these figures by consulting the provided source links, they discovered that the specific data points were nowhere to be found. Suspecting a hallucination, the user prompted Perplexity again, asking it to provide the specific sources for the data in question. In response, the AI effectively retracted its previous statement, admitting: *"I apologize for any inaccuracies in the data provided. Upon reviewing the available sources, I could not find specific information confirming the exact figures... The statement that 45% of Nifty companies missed revenue estimates and 52% undershot EBITDA projections... does not have a direct source in the provided links."*.<sup>8</sup> The user concluded that "most of the data was just made up".<sup>8</sup>

## Case Study 3: The Phantom URL — Fabricated Links and Phishing Risks

### Suggesting Malicious URLs

A far more dangerous manifestation of this failure was identified in a report by the cybersecurity firm Netcraft and highlighted by media outlets like *LiveMint*.<sup>12</sup> This investigation uncovered a real-world instance where Perplexity's URL hallucination posed a direct security risk to its users. When a user asked for the **official URL of Wells Fargo**, a major financial institution, Perplexity AI suggested a known phishing site.<sup>12</sup>

In this scenario, the AI did not invent a non-functional link but instead provided a URL to a live, malicious domain designed to steal user credentials. This type of error is particularly insidious because it weaponizes the user's trust in the AI. A user asking for an official website is likely to believe the answer provided by a platform that markets itself as a reliable information source, making them more susceptible to the phishing attack. The Netcraft report noted that this vulnerability is especially acute for smaller brands that are less likely to be well-represented in an LLM's training data, but the Wells Fargo example shows that even major brands are not immune.<sup>12</sup>

#### Works cited

1. Perplexity AI \- Wikipedia, [https://en.wikipedia.org/wiki/Perplexity\_AI](https://en.wikipedia.org/wiki/Perplexity_AI)  
2. Perplexity Is Already "Citing" Error-Filled AI-Generated Spam \- Futurism, [https://futurism.com/the-byte/perplexity-citing-ai-generated-spam](https://futurism.com/the-byte/perplexity-citing-ai-generated-spam)  
3. Perplexity AI: Does Fact-Checking Make it the Superior Study Buddy? \- Medium, [https://medium.com/@maysarosley/perplexity-ai-does-fact-checking-make-it-the-superior-study-buddy-0f46357dd174](https://medium.com/@maysarosley/perplexity-ai-does-fact-checking-make-it-the-superior-study-buddy-0f46357dd174)  
4. Elijah Clark: A Review of Perplexity AI, Rewritten by Perplexity Itself \- Broadband Breakfast, [https://broadbandbreakfast.com/elijah-clark-a-review-of-perplexity-ai-rewritten-by-perplexity-itself/](https://broadbandbreakfast.com/elijah-clark-a-review-of-perplexity-ai-rewritten-by-perplexity-itself/)  
5. Is Your AI Chatbot Hallucinating on You? What a Tool\! \- Iowa Source, [https://www.iowasource.com/2025/07/01/ai-delusions/](https://www.iowasource.com/2025/07/01/ai-delusions/)  
6. What are AI hallucinations? \- Google Cloud, [https://cloud.google.com/discover/what-are-ai-hallucinations](https://cloud.google.com/discover/what-are-ai-hallucinations)  
7. Examples of AI Hallucinations : r/ChatGPT \- Reddit, [https://www.reddit.com/r/ChatGPT/comments/134nu96/examples\_of\_ai\_hallucinations/](https://www.reddit.com/r/ChatGPT/comments/134nu96/examples_of_ai_hallucinations/)  
8. Perplexity keeps on making up facts? : r/perplexity\_ai \- Reddit, [https://www.reddit.com/r/perplexity\_ai/comments/1j02znl/perplexity\_keeps\_on\_making\_up\_facts/](https://www.reddit.com/r/perplexity_ai/comments/1j02znl/perplexity_keeps_on_making_up_facts/)  
9. Perplexity providing fake URLs. help\! : r/perplexity\_ai \- Reddit, [https://www.reddit.com/r/perplexity\_ai/comments/1ehg6a2/perplexity\_providing\_fake\_urls\_help/](https://www.reddit.com/r/perplexity_ai/comments/1ehg6a2/perplexity_providing_fake_urls_help/)  
10. In my experience, Perplexity and OpenAI's deep research tools are so misleading \- Hacker News, [https://news.ycombinator.com/item?id=43180281](https://news.ycombinator.com/item?id=43180281)  
11. How Strong Is AI When Hallucinations Haunt? \- G2 Learning Hub, [https://learn.g2.com/tech-signals-ai-hallucinations-and-research](https://learn.g2.com/tech-signals-ai-hallucinations-and-research)  
12. AI chatbots like ChatGPT and Perplexity could send you to scam ..., [https://www.livemint.com/technology/tech-news/ai-chatbots-like-chatgpt-and-perplexity-could-send-you-to-scam-links-warns-study-11751600193362.html](https://www.livemint.com/technology/tech-news/ai-chatbots-like-chatgpt-and-perplexity-could-send-you-to-scam-links-warns-study-11751600193362.html)  
13. Anyone getting answers not found in linked sources? : r/perplexity\_ai, [https://www.reddit.com/r/perplexity\_ai/comments/1d5feoe/anyone\_getting\_answers\_not\_found\_in\_linked\_sources/](https://www.reddit.com/r/perplexity_ai/comments/1d5feoe/anyone_getting_answers_not_found_in_linked_sources/)  
14. Perplexity.ai, praktisch, aber problematisch: Erfundene Zitate ..., [https://stefanpfeiffer.blog/2025/05/01/perplexity-ai-praktisch-aber-problematisch-erfundene-zitate-falsche-autoren/](https://stefanpfeiffer.blog/2025/05/01/perplexity-ai-praktisch-aber-problematisch-erfundene-zitate-falsche-autoren/)  
15. Second-Hand Hallucinations: Investigating Perplexity's AI ... \- GPTZero, [https://gptzero.me/news/gptzero-perplexity-investigation/](https://gptzero.me/news/gptzero-perplexity-investigation/)  
16. Has anyone else noticed a decline in Perplexity AI's accuracy lately ..., [https://www.reddit.com/r/perplexity\_ai/comments/1ltk0z1/has\_anyone\_else\_noticed\_a\_decline\_in\_perplexity/](https://www.reddit.com/r/perplexity_ai/comments/1ltk0z1/has_anyone_else_noticed_a_decline_in_perplexity/)  
17. Introducing Perplexity Deep Research, [https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research)  
18. Perplexity Fabricated Data-Deep Research : r/perplexity\_ai \- Reddit, [https://www.reddit.com/r/perplexity\_ai/comments/1jjcj1s/perplexity\_fabricated\_datadeep\_research/](https://www.reddit.com/r/perplexity_ai/comments/1jjcj1s/perplexity_fabricated_datadeep_research/)  
19. Minimizing empirically incorrect responses : r/perplexity\_ai \- Reddit, [https://www.reddit.com/r/perplexity\_ai/comments/1hhvqxs/minimizing\_empirically\_incorrect\_responses/](https://www.reddit.com/r/perplexity_ai/comments/1hhvqxs/minimizing_empirically_incorrect_responses/)  
20. Always wrong answers in basic calculations : r/perplexity\_ai \- Reddit, [https://www.reddit.com/r/perplexity\_ai/comments/1ldbpt5/always\_wrong\_answers\_in\_basic\_calculations/](https://www.reddit.com/r/perplexity_ai/comments/1ldbpt5/always_wrong_answers_in_basic_calculations/)  
21. Perplexity not visiting URL \- Only halluzinating \- Features \- Make Community, [https://community.make.com/t/perplexity-not-visiting-url-only-halluzinating/45682](https://community.make.com/t/perplexity-not-visiting-url-only-halluzinating/45682)  
22. Perplexity Makes Longshot \$34.5B Offer for Chrome \- Hacker News, [https://news.ycombinator.com/item?id=44877656](https://news.ycombinator.com/item?id=44877656)  
23. Perplexity Deep Research \- Hacker News, [https://news.ycombinator.com/item?id=43061827](https://news.ycombinator.com/item?id=43061827)

[The End of Response]

### Rubric

[The Start of Rubric]

Find links that contain at least one real-world case where Perplexity AI's search products (e.g., Pro Search or Deep Research) generated hallucinatory responses to user inputs—such as fabricated URLs or made-up information. The content of the links must describe specific instances of these hallucinatory responses (e.g., the user's input and the AI's response, or a detailed description of what occurred). Each eligible link found will earn 1 point, with a maximum of 3 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-1:
https://www.reddit.com/r/perplexity_ai/comments/1j02znl/perplexity_keeps_on_making_up_facts/

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
