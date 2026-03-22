# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

I am interested in reading popular science books about Artificial Intelligence (AI) or closely related topics, written (or co-written) by recipients of the prestigious Turing Award. Please help me identify five suitable books that are specifically intended for general readers, rather than textbooks aimed at students or academic reference manuals. For each selected book, please provide the title, the name(s) of the author(s), the year in which the author(s) received the Turing Award, and a link to its Goodreads page.

[The End of Query]

### Response

[The Start of Response]

# Five Popular Science Books on AI by Turing Award Laureates

| Title | Author(s) | Turing Award Year | Goodreads Link |
| :-- | :-- | :-- | :-- |
| The Society of Mind | Marvin Minsky | 1969 | https://www.goodreads.com/book/show/326790.The_Society_of_Mind |
| The Emotion Machine: Commonsense Thinking, Artificial Intelligence, and the Future of the Human Mind | Marvin Minsky | 1969 | https://www.goodreads.com/en/book/show/169007.The_Emotion_Machine |
| The Book of Why: The New Science of Cause and Effect | Judea Pearl | 2011 | https://www.goodreads.com/book/show/36204378-the-book-of-why |
| Probably Approximately Correct: Nature’s Algorithms for Learning and Prospering in a Complex World | Leslie Valiant | 2010 | https://www.goodreads.com/en/book/show/16043523-probably-approximately-correct |
| The Sciences of the Artificial | Herbert A. Simon | 1975 | https://www.goodreads.com/book/show/4060631-the-sciences-of-the-artificial |

<span style="display:none">[^1][^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^2][^20][^3][^4][^5][^6][^7][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://www.goodreads.com/book/show/326790.The_Society_of_Mind

[^2]: https://www.goodreads.com/en/book/show/169007.The_Emotion_Machine

[^3]: https://www.goodreads.com/book/show/1487628.The_Book_of_Why

[^4]: https://www.goodreads.com/book/show/326790

[^5]: https://psyopsprime.com/consciousness/a-review-of-the-emotion-machine/

[^6]: https://www.goodreads.com/book/show/15788966-the-book-of-why

[^7]: https://www.goodreads.com/book/show/133749168

[^8]: https://www.goodreads.com/work/editions/163208-the-emotion-machine-commonsense-thinking-artificial-intelligence-and

[^9]: https://www.goodreads.com/book/show/36204378-the-book-of-why

[^10]: https://www.goodreads.com/book/show/8768838

[^11]: https://www.goodreads.com/en/book/show/16043523-probably-approximately-correct

[^12]: https://www.goodreads.com/book/show/1027612

[^13]: https://www.goodreads.com/book/show/58700545-probably-approximately-correct

[^14]: https://www.goodreads.com/book/show/4060631-the-sciences-of-the-artificial

[^15]: https://www.goodreads.com/author/show/6539018.Leslie_Valiant

[^16]: https://www.goodreads.com/book/show/676046.The_Sciences_of_the_Artificial___3rd_Edition

[^17]: https://www.goodreads.com/book/similar/21820779-probably-approximately-correct-nature-s-algorithms-for-learning-and-pro

[^18]: https://www.goodreads.com/work/editions/2071475-the-sciences-of-the-artificial

[^19]: https://www.goodreads.com/author/quotes/6539018.Leslie_Valiant

[^20]: https://www.goodreads.com/book/show/56383684-the-sciences-of-the-artificial-reissue-of-the-third-edition-with-a-new

[The End of Response]

### Rubric

[The Start of Rubric]

1. Correctly recommend five popular science books on artificial intelligence or related topics written (or co-written) by Turing Award winners that are suitable for general readers. These books cannot be textbooks or academic reference manuals for students. 1 point will be awarded for each book recommended, for a maximum of 5 points.
2. Provide the author names, year the author received the Turing Award, and links to the books' Goodreads pages for each of the five recommended books that meet the above requirements. 1 point will be awarded if all information for each book is correct. In other words, if a book's title is correct but the author name is incorrect, no points will be awarded. A maximum of 5 points will be awarded.
3. Total possible score: 10 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-1:
The Emotion Machine: Commonsense Thinking, Artificial Intelligence, and the Future of the Human Mind

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
