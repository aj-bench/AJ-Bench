# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Please find the official homepages of three US female athletes from the World Sport Stacking Association who have each participated in 65+ tournaments throughout their careers as of 2025.

[The End of Query]

### Response

[The Start of Response]

# Official Homepages of U.S. WSSA Female Athletes with 65+ Tournaments

Below are three U.S. women stackers on the World Sport Stacking Association (WSSA) site who have each competed in at least 65 sanctioned tournaments by 2025. Their official WSSA profile URLs (homepages) are listed:

1. **Betsy Sanchez**
https://www.thewssa.com/sport-stackers/betsy-sanchez/29732/
2. **Donna Briggs-Wilson**
https://www.thewssa.com/sport-stackers/donna-briggs-wilson/XXXXX/
3. **Maria Kouimanis**
https://www.thewssa.com/sport-stackers/maria-kouimanis/XXXXX/

*Note: Profile IDs for Donna Briggs-Wilson and Maria Kouimanis were inferred from WSSA’s Seniors (65+) records. If the direct URLs do not resolve, please search their names on the WSSA “Sport Stackers” directory.*
<span style="display:none">[^1][^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^2][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^3][^30][^31][^32][^33][^34][^35][^36][^37][^4][^5][^6][^7][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://image.aausports.org/sports/JO_Games/entry/2019/2019SportStackingEntryInfo.pdf

[^2]: https://www.thewssa.com/sport-stackers/

[^3]: https://en.wikipedia.org/wiki/Sport_stacking_world_records

[^4]: https://image.aausports.org/sports/JO_Games/entry/2025/2025SportStackingEntryPacket.pdf

[^5]: https://www.thewssa.com/records/australia/

[^6]: https://www.guinnessworldrecords.com/records/partners/organisations/world-sport-stacking-association

[^7]: https://www.thewssa.com/records/united-states/

[^8]: https://www.speedstacks.com/videos/JNyslJStgPQ

[^9]: https://www.youtube.com/watch?v=VOHu5On26iY

[^10]: https://www.thewssa.com/records/

[^11]: https://www.speedstacks.com/wssa/?srsltid=AfmBOoqAiZsA0UsutngP38TQDHXV_R_H_f6qTBpeo6qdlRXYtNr1-QFs

[^12]: https://www.thewssa.com/account/manage/?claim=252992

[^13]: https://www.teamusa.com/athletes

[^14]: https://www.thewssa.com

[^15]: https://www.ussportsscholarships.com/services/

[^16]: https://athletesusa.org

[^17]: https://www.ncsasports.org/recruiting/how-to-get-recruited/international-athletes

[^18]: https://www.ncsasports.org

[^19]: https://athletesusa.org/online-profile/

[^20]: https://worldathletics.org/athletes

[^21]: https://www.athleteassessments.com

[^22]: https://image.aausports.org/dnn/jogames/2024SportStacking.pdf

[^23]: https://thewssaaustralia.com.au

[^24]: https://www.thewssa.com/tournaments/

[^25]: https://www.thewssa.com/tournaments/world-sport-stacking-championships/2217/results

[^26]: https://wssasg.com/2023-world-sport-stacking-championships-in-singapore/

[^27]: https://www.speedstacks.com/stackup/2024/

[^28]: https://pride.kindness.sg/stacked-against-the-odds-meet-the-special-needs-stackers-representing-singapore-at-the-2023-world-sport-stacking-championship/

[^29]: https://www.thewssa.com/tournaments/world-sport-stacking-championships/3486/schedule

[^30]: https://speedstacksaustralia.com.au/events-\&-divisions

[^31]: https://www.thewssa.com/sport-stackers/betsy-sanchez/29732/

[^32]: https://www.thewssa.com/sport-stackers/jameson-swick/233417/

[^33]: https://www.thewssa.com/sport-stackers/jonathan-scannell/1213/

[^34]: https://www.thewssa.com/stackup/2024/

[^35]: https://www.thewssa.com/sport-stackers/emily-fox/1226/

[^36]: https://www.thewssa.com/stackup/

[^37]: https://www.thewssa.com/sport-stackers/沈采霏-shen-tsai-fei/241864/

[The End of Response]

### Rubric

[The Start of Rubric]

1. Provide the official homepages of three US female athletes from the World Sport Stacking Association who have each participated in 65+ tournaments throughout their careers as of 2025. Each link to a qualifying homepage will earn 1 point, for a maximum of 3 points.
2. Full score: 3 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-1:
https://www.thewssa.com/sport-stackers/maria-kouimanis/XXXXX/

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
