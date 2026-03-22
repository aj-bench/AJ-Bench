# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

I'm interested in films released after Captain America: Civil War featuring at least two credited actors from its cast. First, provide the U.S. release date for Captain America: Civil War along with a cast page link (from any credible source clearly listing the cast). Then, identify 3 films released no later than 2020 featuring at least two actors who were credited in Captain America: Civil War. For each identified film, clearly state the film's title, the names of those actors, their character names in the identified film, the film's U.S. release date, a link to its Wikipedia page, and a link to a cast page clearly listing these actors.

[The End of Query]

### Response

[The Start of Response]

# Films Featuring Multiple “Captain America: Civil War” Cast Members (2016–2020)

**Main Takeaway:** Three post-Civil War films released by 2020 that each feature at least two credited actors from *Captain America: Civil War* are *Spider-Man: Homecoming* (2017), *Avengers: Infinity War* (2018), and *Avengers: Endgame* (2019).

## 1. Captain America: Civil War

U.S. Release Date: May 6, 2016[^1]
Cast Listing: https://en.wikipedia.org/wiki/Captain_America:_Civil_War#Cast

***

## 2. Spider-Man: Homecoming (2017)

U.S. Release Date: July 7, 2017[^2]
Wikipedia: https://en.wikipedia.org/wiki/Spider-Man:_Homecoming
Cast Listing: https://en.wikipedia.org/wiki/Spider-Man:_Homecoming#Cast

Actors from *Civil War*

- Tom Holland as Peter Parker / Spider-Man
- Robert Downey Jr. as Tony Stark / Iron Man

***

## 3. Avengers: Infinity War (2018)

U.S. Release Date: April 27, 2018[^3]
Wikipedia: https://en.wikipedia.org/wiki/Avengers:_Infinity_War
Cast Listing: https://en.wikipedia.org/wiki/Avengers:_Infinity_War#Cast

Actors from *Civil War*

- Robert Downey Jr. as Tony Stark / Iron Man
- Chris Evans as Steve Rogers / Captain America

***

## 4. Avengers: Endgame (2019)

U.S. Release Date: April 26, 2019[^4]
Wikipedia: https://en.wikipedia.org/wiki/Avengers:_Endgame
Cast Listing: https://en.wikipedia.org/wiki/Avengers:_Endgame#Cast

Actors from *Civil War*

- Robert Downey Jr. as Tony Stark / Iron Man
- Chris Evans as Steve Rogers / Captain America

***

Sources[^1]
<span style="display:none">[^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^20][^21][^22][^5][^6][^7][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://en.wikipedia.org/wiki/Captain_America:_Civil_War

[^2]: https://en.wikipedia.org/wiki/Spider-Man:_Homecoming

[^3]: https://en.wikipedia.org/wiki/Avengers:_Infinity_War

[^4]: https://en.wikipedia.org/wiki/Avengers:_Endgame

[^5]: https://www.imdb.com/title/tt3498820/fullcredits/

[^6]: https://www.imdb.com/title/tt3498820/releaseinfo/

[^7]: https://www.tvguide.com/movies/captain-america-civil-war/cast/2000310023/

[^8]: https://www.movieinsider.com/m12422/captain-america-3

[^9]: https://marvelcinematicuniverse.fandom.com/wiki/Captain_America:_Civil_War

[^10]: https://www.imdb.com/title/tt3498820/

[^11]: https://www.rottentomatoes.com/m/captain_america_civil_war/cast-and-crew

[^12]: https://www.rottentomatoes.com/m/captain_america_civil_war

[^13]: https://www.youtube.com/watch?v=v6OdOJShRWQ

[^14]: https://www.boxofficemojo.com/release/rl3210970625/

[^15]: https://www.imdb.com/title/tt2250912/releaseinfo/

[^16]: https://www.imdb.com/title/tt4154756/releaseinfo/

[^17]: https://www.imdb.com/title/tt4154796/releaseinfo/

[^18]: https://www.movieinsider.com/m13170/spider-man

[^19]: https://www.movieinsider.com/m11839/the-avengers-infinity-war

[^20]: https://www.imdb.com/title/tt4154796/

[^21]: https://www.youtube.com/watch?v=rk-dF1lIbIg

[^22]: https://www.imdb.com/title/tt4154756/

[The End of Response]

### Rubric

[The Start of Rubric]

1. Correctly state the US release date for Captain America: Civil War (1 point);
2. Provide a link to the cast page for Captain America: Civil War. Any reliable source that clearly lists the cast will do (1 point);
3. Identify 3 films released no later than 2020 featuring at least two actors who were credited in Captain America: Civil War. For each identified film, clearly state the film’s title, the names of those actors, their character names in the identified film, the film’s U.S. release date, a link to its Wikipedia page, and a link to a cast page clearly listing these actors. Each identified film that meets all of the above requirements will receive 1 point, for a maximum of 3 points;
4. For each of the three films that meet the aforementioned requirements, providing a link to the Wikipedia page for each film will earn 1 point, with a maximum of 3 points;
5. For each of the three films that meet the aforementioned requirements, clearly listing the cast list page link for each film will earn 1 point, with a maximum of 3 points;
6. The maximum score is 11 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-3:
Avengers: Endgame; Robert Downey Jr. (Tony Stark / Iron Man), Chris Evans (Steve Rogers / Captain America); April 26, 2019

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
