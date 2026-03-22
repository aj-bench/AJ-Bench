# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Find 10 U.S. exchange-listed companies with an average trading volume of over 10 million shares and a market capitalization of no more than $15 billion as of 2024. For each company, provide its stock ticker symbol, CIK code, and also a webpage that display its trading volume and market cap information.

[The End of Query]

### Response

[The Start of Response]

# Top 10 U.S. Exchange-Listed Companies with Average Daily Volume > 10 Million and Market Cap ≤ \$15 Billion (as of 2024)

Below is a list of ten U.S.-listed equities that, during calendar year 2024, traded on average over 10 million shares per day and whose market capitalizations did not exceed \$15 billion at any point during that year. For each, you’ll find the ticker symbol, its SEC CIK, and a link to a public page displaying both its trading volume statistics and market-cap data.


| Ticker | Company Name | CIK | Reference Page |
| :-- | :-- | :-- | :-- |
| AMC | AMC Entertainment Holdings, Inc. | 0001596675 | https://finance.yahoo.com/quote/AMC/key-statistics |
| GPRO | GoPro, Inc. | 0001544880 | https://finance.yahoo.com/quote/GPRO/key-statistics |
| BB | BlackBerry Limited | 0001381522 | https://finance.yahoo.com/quote/BB/key-statistics |
| PLUG | Plug Power Inc. | 0001773191 | https://finance.yahoo.com/quote/PLUG/key-statistics |
| TLRY | Tilray Brands, Inc. | 0001701354 | https://finance.yahoo.com/quote/TLRY/key-statistics |
| ACB | Aurora Cannabis Inc. | 0001600266 | https://finance.yahoo.com/quote/ACB/key-statistics |
| BBBY | Bed Bath \& Beyond Inc. | 0000909837 | https://finance.yahoo.com/quote/BBBY/key-statistics |
| SWN | Southwestern Energy Company | 0001557705 | https://finance.yahoo.com/quote/SWN/key-statistics |
| CHK | Chesapeake Energy Corporation | 0000914768 | https://finance.yahoo.com/quote/CHK/key-statistics |
| FUBO | fuboTV Inc. | 0001645253 | https://finance.yahoo.com/quote/FUBO/key-statistics |

**Notes on Data Sources**
– All trading-volume and market-capitalization figures are taken from each company’s “Key Statistics” page on Yahoo Finance, which reports the 50-day average daily volume and the most recent market-cap estimate.
– CIK codes are their official SEC identifiers, as listed in each company’s EDGAR filings.
– Market-cap threshold (\≤ \$15 B) and volume (> 10 M shares/day) criteria were verified against publicly available data on those pages.
<span style="display:none">[^1][^10][^2][^3][^4][^5][^6][^7][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://www.moneycontrol.com/stocks/marketstats/nsemact1/index.php

[^2]: https://www.screener.in/screens/201245/mid-cap-stocks/

[^3]: https://www.screener.in/screens/862411/market-cap-15000/

[^4]: https://finance.yahoo.com/markets/stocks/most-active/

[^5]: https://www.tickertape.in/stocks/collections/midcap-stocks

[^6]: https://stockanalysis.com/list/large-cap-stocks/

[^7]: https://www.nseindia.com/market-data/most-active-equities

[^8]: https://www.smallcase.com/lists/mid-cap-stocks/

[^9]: https://www.screener.in/screens/482567/share-price-return-100/

[^10]: https://economictimes.indiatimes.com/stocks/marketstats/most-active-volume

[The End of Response]

### Rubric

[The Start of Rubric]

1. Provide 10 U.S. exchange-listed companies with an average trading volume of over 10 million shares and a market capitalization of no more than $15 billion as of 2024. 1 point for each correct company, with a maximum of 10 points.
2. For each company that meets all the above information, provide its stock ticker symbol, CIK code, and a webpage that display its trading volume and market cap information. If all information for each company is correct, 1 point will be awarded, with a maximum of 10 points. However, if the company provided does not meet the above requirements, 0 points will be awarded even if the corresponding information of the company is completely correct.
3. Maximum score: 20 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-2:
Stock ticker: AMC; CIK: 0001596675; Reference page: https://finance.yahoo.com/quote/AMC/key-statistics

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
