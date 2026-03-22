# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Determine if actor Chris Evans can be connected to any U.S. president born prior to the year 1920 through political relationships or familial relationships, both of which should obey three degrees of separation. If such a connection exists, please specify:

1. The name and birth date of the U.S. president.
2. The exact chain of connections, clearly indicating the nature of each connection (familial relationship or political relationship, e.g., relative, colleague, successor, mentor).
3. The source(s) confirming the relationship between actor Chris Evans and the U.S. president, with preference for official or authoritative references.

[The End of Query]

### Response

[The Start of Response]

# Connection Analysis Between Chris Evans and U.S. Presidents Born Before 1920

A thorough review of available genealogical records and political affiliations reveals **no verifiable connection**—familial or political—between actor Chris Evans and any U.S. president born prior to 1920 within three degrees of separation.

**Key Findings**

1. **Familial Lines**
    - Chris Evans’s closest notable political relative is his maternal uncle, Michael “Mike” Capuano (b. 1952), former U.S. Representative for Massachusetts’s 7th District. This is a first-degree familial relationship but does not lead to any president born before 1920.
    - Extensive genealogical charts trace Evans’s lineage to Revolutionary War and Civil War soldiers, but none of his documented ancestors are directly related to U.S. presidents born before 1920.[^1]
2. **Political Associations**
    - Chris Evans founded the civic-education platform *A Starting Point* and has interviewed numerous members of Congress; however, none of these interviews or partnerships link him to presidents born before 1920 via mentor-mentee, colleague, or successor relationships.
    - His uncle Mike Capuano served alongside modern presidents and in the U.S. House from 1999 to 2019, but those presidencies (e.g., Bill Clinton, George W. Bush, Barack Obama, Donald Trump) all post-date 1920 births.
3. **Chain of Separation Attempts**
Attempts to construct chains—e.g., Chris Evans → familial tie → Congressional service → mentorship or appointment by an older president—fail to reach any president born before 1920 within three steps.

**Conclusion**
There is **no documented chain of familial or political relationships** connecting Chris Evans to any U.S. president born before 1920 within three degrees of separation.[^1]
<span style="display:none">[^10][^11][^2][^3][^4][^5][^6][^7][^8][^9]</span>

<div style="text-align: center">⁂</div>


[^1]: https://famouskin.com/ahnentafel.php?name=60127+chris+evans

[^2]: https://people.com/politics/the-personal-journey-behind-chris-evans-politics-website/

[^3]: https://people.com/all-about-chris-evans-parents-siblings-7502694

[^4]: https://www.wired.com/story/chris-evans-starting-point-politics/

[^5]: https://www.hollywoodancestry.com/post/captain-america-s-chris-evans-descended-from-long-line-of-patriot-soldiers-immigrants

[^6]: https://www.imdb.com/news/ni60889193/

[^7]: https://chris-evans.boards.net/thread/405/chriss-family-history

[^8]: https://www.reddit.com/r/marvelcirclejerk/comments/1izu8yq/captain_america_under_hydras_influence_ended_up/

[^9]: https://en.wikipedia.org/wiki/Chris_Evans_(actor)

[^10]: https://www.hollywoodreporter.com/movies/movie-features/chris-evans-talks-trump-tom-brady-anxiety-retirement-rumors-1196705/

[^11]: https://www.linkedin.com/posts/chris-evans99_chris-evans-appointed-as-finisterre-president-activity-7150529661251284992-J2gi



[The End of Response]

### Rubric

[The Start of Rubric]

1. Identify a U.S. president born before 1920, whose connection actor Chris Evans could establish through political or family relationships, adhering to the three-degree separation principle. List the president's name and date of birth. 1 point.
2. Describe the exact chain of relationships between Chris Evans and the U.S. president, specifying the nature of each level (family or political, e.g., relative, colleague, successor, mentor). 1 point. No extra points are awarded for listing multiple relationships.
3. Provide sources confirming the connection between actor Chris Evans and the U.S. president, prioritizing official or authoritative sources. 1 point.
4. Maximum 3 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-1:
No U.S. president born before 1920 can be connected to actor Chris Evans through political or familial relationships (within three degrees of separation).

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
