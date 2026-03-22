# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

I am conducting research on Seattle, Washington, and would like your help gathering some key information. Please start by providing the Wikipedia page for Seattle and, tell me the city’s population and its rank among U.S. cities by population by the information there as of 2024. Additionally, find a webpage that ranks U.S. cities by rental prices in 2024 and identify Seattle's position on that list. Lastly, I’d like to know more about the city’s character—provide links to Wikipedia pages for three significant landmarks in Seattle as well as three notable historical events associated with the city.

[The End of Query]

### Response

[The Start of Response]

# 1. Seattle Wikipedia page
For a detailed general overview, the primary resource on the city is the Seattle Wikipedia page: https://en.wikipedia.org/wiki/Seattle .<sup>1</sup>

# 2. Population and rank (as of 2024, per Wikipedia)
According to data from 2024, Seattle's population is estimated at 780,995 residents.<sup>1</sup> This population size ranks Seattle as the 18th most populous city in the United States.<sup>1</sup>

# 3. Rental prices ranking (2024) and Seattle’s position
According to a 2024 analysis of rental prices, the Seattle-Tacoma-Bellevue metropolitan area ranks as the 6th most expensive large metro area for renters in the United States.<sup>5</sup> The median monthly rent for the region is reported at $2,733.<sup>5</sup>

Table 1: 2024 West Coast Metropolitan Area Rental Prices

| City/Metro Area | Monthly Rent | Rank |
| :---- | :---- | :---- |
| San Jose-Sunnyvale-Santa Clara, CA | $3,811 | 1 |
| San Diego-Chula Vista-Carlsbad, CA | $3,228 | 2 |
| San Francisco-Oakland-Fremont, CA | $3,183 | 3 |
| Los Angeles-Long Beach-Anaheim, CA | $2,848 | 4 |
| Seattle-Tacoma-Bellevue, WA | $2,733 | 6 |
| Portland-Vancouver-Hillsboro, OR-WA | $2,254 | 15 |

# 4. Significant landmarks (Wikipedia links)
1. The Space Needle  
   - Wikipedia Link: https://en.wikipedia.org/wiki/Space_Needle

2. Pike Place Market  
   - Wikipedia Link: https://en.wikipedia.org/wiki/Pike_Place_Market

3. Pioneer Square Historic District  
   - Wikipedia Link: https://en.wikipedia.org/wiki/Pioneer_Square_historic_district

# 5. Notable historical events (Wikipedia links)
1. The Great Seattle Fire of 1889  
   - Wikipedia Link: https://en.wikipedia.org/wiki/Great_Seattle_Fire

2. The Klondike Gold Rush (1897-1898)  
   - Wikipedia Link: https://en.wikipedia.org/wiki/Klondike_Gold_Rush

3. The Seattle General Strike of 1919  
   - Wikipedia Link: https://en.wikipedia.org/wiki/Seattle_General_Strike_of_1919

## Works cited
1. Seattle - Wikipedia, https://en.wikipedia.org/wiki/Seattle  
2. Seattle - Simple English Wikipedia, the free encyclopedia, https://simple.wikipedia.org/wiki/Seattle  
3. Timeline of Seattle - Wikipedia, https://en.wikipedia.org/wiki/Timeline_of_Seattle  
4. History of Seattle 1900–1940 - Wikipedia, https://en.wikipedia.org/wiki/History_of_Seattle_1900%E2%80%931940  
5. U.S. Cities With the Highest Rent Prices [2024 Edition ..., https://constructioncoverage.com/research/cities-with-the-most-expensive-rents  
6. Most and Least Expensive Cities for Renters in 2024 - Bay Property Management Group, https://www.baymgmtgroup.com/blog/cities-for-renters-in-2024/  
7. Seattle Center - Wikipedia, https://en.wikipedia.org/wiki/Seattle_Center  
8. Architecture of Seattle - Wikipedia, https://en.wikipedia.org/wiki/Architecture_of_Seattle

[The End of Response]

### Rubric

[The Start of Rubric]

1. Correctly provide the Wikipedia page for Seattle, earn 1 point.
2. Correctly state the population of Seattle, earn 1 point.
3. Correctly state Seattle's population ranking among U.S. cities as of 2024, earn 1 point.
4. Provide a webpage ranking U.S. city rents in 2024 and indicate Seattle's position on that page: 1 point.
5. Correctly list three major Seattle landmarks: 1 point per correct landmark, maximum 3 points.
6. Correctly provide Wikipedia page links for three significant historical events related to Seattle: 1 point per correct link, maximum 3 points.
7. Total points: 10 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-1:
https://en.wikipedia.org/wiki/Seattle

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
