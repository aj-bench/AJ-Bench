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

# Seattle Overview and Key Rankings

**Population and U.S. Rank (2024)**
Seattle is the most populous city in Washington State, with an estimated population of **780,995** in 2024. It ranks as the **18th-most populous city** in the United States.[^1]

**2024 Rental Price Ranking**
According to ApartmentAdvisor’s 2024 National Rent Report, Seattle’s median monthly rent for a one-bedroom apartment is **\$1,840**. Among the 100 major U.S. cities tracked, this places Seattle at **18th** highest in rental cost.[^2]

## Three Significant Seattle Landmarks

Below are Wikipedia links to three of Seattle’s most iconic landmarks:

- Space Needle
https://en.wikipedia.org/wiki/Space_Needle
- Pike Place Market
https://en.wikipedia.org/wiki/Pike_Place_Market
- Seattle Center
https://en.wikipedia.org/wiki/Seattle_Center


## Three Notable Historical Events in Seattle

Here are Wikipedia pages for three major events that have shaped Seattle’s history:

- Great Seattle Fire (1889)
https://en.wikipedia.org/wiki/Great_Seattle_Fire
- Alaska–Yukon–Pacific Exposition (1909)
https://en.wikipedia.org/wiki/Alaska–Yukon–Pacific_Exposition
- Century 21 Exposition (1962 World’s Fair)
https://en.wikipedia.org/wiki/Century_21_Exposition

***
1. Seattle population and U.S. city rank in 2024[^1]
2. Seattle’s median rent and 2024 rental ranking among 100 U.S. cities[^2]
<span style="display:none">[^10][^3][^4][^5][^6][^7][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://www.apartmentadvisor.com/national-rent-report

[^2]: https://listwithclever.com/research/price-to-rent-ratio-2024/

[^3]: https://www.visualcapitalist.com/ranked-u-s-cities-with-the-highest-rent-in-2024/

[^4]: https://constructioncoverage.com/research/cities-with-the-largest-rent-increases-decreases

[^5]: https://rentalrealestate.com/data/rent/expensive/

[^6]: https://constructioncoverage.com/research/cities-with-the-most-expensive-rents

[^7]: https://www.stessa.com/blog/cities-highest-rent-to-price

[^8]: https://realestate.usnews.com/places/rankings/most-expensive-places-to-live

[^9]: https://www.reddit.com/r/EconomyCharts/comments/1ddf9qc/ranked_us_cities_with_the_highest_rent_in_2024/

[^10]: https://smartasset.com/data-studies/rent-increases-2025

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
