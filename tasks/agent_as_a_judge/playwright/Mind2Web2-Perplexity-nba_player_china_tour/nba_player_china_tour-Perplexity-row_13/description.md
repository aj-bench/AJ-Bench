# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Identify 3 current NBA players who are actively playing in the NBA as of 2025, have participated in at least 5 NBA All-Star Games, are not Chinese citizens, and have never professionally played for a Chinese basketball team or held an official coaching or managerial role in China. However, each player should have conducted at least one basketball-related tour in China from 2015 to 2025 (inclusive). For each player, clearly provide the following: list any 5 NBA All-Star Games in which they participated, a link to their Wikipedia page, the year their China tour occurred, and a direct link to an article or news source confirming the China tour.

[The End of Query]

### Response

[The Start of Response]

# Key Takeaways

Three active NBA players meet all criteria: LeBron James, Stephen Curry, and Kevin Durant. Each has appeared in at least five All-Star Games, is not a Chinese citizen, never professionally played or coached in China, and conducted a basketball-related tour in China between 2015 and 2025.

***

## 1. LeBron James

- NBA All-Star Appearances (select five): 2005, 2006, 2007, 2008, 2009
- Wikipedia: https://en.wikipedia.org/wiki/LeBron_James
- China Tour: 2015 (Nike RISE Tour made stops in Greater China)[^1]
- Tour Confirmation:
    - “The 2015 Nike RISE tour will follow NBA All-Stars … making stops throughout Greater China …”[^1]

***

## 2. Stephen Curry

- NBA All-Star Appearances (select five): 2014, 2015, 2016, 2017, 2018
- Wikipedia: https://en.wikipedia.org/wiki/Stephen_Curry
- China Tour: 2017 (Under Armour Curry Asia Tour: Beijing, Chengdu, Hangzhou)[^2]
- Tour Confirmation:
    - “Stephen and Seth travelled from Beijing to Chengdu … for the 2017 Curry Asia Tour.”[^2]

***

## 3. Kevin Durant

- NBA All-Star Appearances (select five): 2010, 2011, 2012, 2013, 2014
- Wikipedia: https://en.wikipedia.org/wiki/Kevin_Durant
- China Tour: 2016 (Nike promotional tour in China)[^3]
- Tour Confirmation:
    - “Durant went to China for a Nike promotional tour shortly after signing with the team.”[^3]

***

References
<span style="display:none">[^10][^11][^12][^13][^14][^15][^4][^5][^6][^7][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://www.slamonline.com/news/nba/paul-george-kicks-off-2015-nike-rise-tour-in-asia-photos/

[^2]: https://weartesters.com/recap-stephen-currys-2017-curry-asia-tour/

[^3]: https://www.gettyimages.com/photos/kevin-durant-visits-china

[^4]: https://www.youtube.com/watch?v=ScjRX8GTZVE

[^5]: https://www.ichongqing.info/2025/08/14/stephen-currys-china-tour-cranks-up-chinese-sneaker-market/

[^6]: https://andscape.com/features/kevin-durants-debut-in-oracle-arena-was-a-slam-dunk/

[^7]: https://kingjamesgospel.com/2015/08/26/lebron-james-wows-fans-touches-hearts-manila-nike-rise-event/

[^8]: https://trangdam.com/steph-asia-tour

[^9]: https://www.slamonline.com/news/nba/photos-kevin-durants-china-tour/

[^10]: https://nikelebron.net/lebron_james_nike_world_tour_us_china_europe_air_max_lebron_vii/

[^11]: https://www.youtube.com/watch?v=_ZsMf4PoeV4

[^12]: https://nikelebron.net/tag/rise-tour/

[^13]: https://www.youtube.com/watch?v=FShb2xDHiEI

[^14]: https://www.gettyimages.com/photos/lebron-james-shanghai-tour

[^15]: https://www.youtube.com/watch?v=P0cUgtLOsaM

[The End of Response]

### Rubric

[The Start of Rubric]

1. Search for 3 active non-Chinese NBA players who will still be playing in the NBA by 2025, have participated in at least 5 NBA All-Star Games, have never played for the Chinese national basketball team, and have never held an official coaching or management position in China. Each player must have participated in at least one basketball-related tour in China from 2015 to 2025(inclusive). 1 point will be rewarded per player found, up to a maximum of 3 points.

Provided that Scoring Point 1 is satisfied:

2. List any 5 NBA All-Star Games that each of the three players participated in. For each correct list provided for a player, 1 point is awarded (an incorrect list results in no points), up to a maximum of 3 points.
3. Provide a link to the Wikipedia page for each player. For each correct link provided, 1 point is awarded, up to a maximum of 3 points.
4. Provide the year(s) in which their China tour(s) occurred. For providing any one correct tour year for a player (if multiple years are listed and any are incorrect, no point is awarded for that player), 1 point is awarded per player, up to a maximum of 3 points.
5. Provide a direct link to an article or news source confirming the player's China tour. For each correct news link provided for a player, 1 point is awarded, up to a maximum of 3 points.
6. The maximum total score is 15 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-5:
https://www.slamonline.com/news/nba/paul-george-kicks-off-2015-nike-rise-tour-in-asia-photos/

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
