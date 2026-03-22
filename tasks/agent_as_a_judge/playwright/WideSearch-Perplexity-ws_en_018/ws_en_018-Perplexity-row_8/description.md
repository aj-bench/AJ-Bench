# Agent-as-a-Judge Task

You will verify the factual correctness of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Analyze the trend of the U.S. federal government spending and deficit before and after the pandemic. Please provide me with the following data through fiscal years 2015-2024: the federal Budget (trillion), the federal spending (trillion), the federal deficit (trillion), the national debt (trillion), the net interest cost on the gross federal debt (trillion), and the official links supporting your statements.

Please organize the results in one Markdown table with the following column names in order: 
Fiscal Year, Federal Budget, Federal Spending, Federal Deficit, National Debt, Net Interest Cost, Official Link.
 
Under the Fiscal Year, state the statistics like FY2015, FY2016.

[The End of Query]

### Response

[The Start of Response]

# Trends in U.S. Federal Budget, Outlays, Deficit, Debt, and Net Interest (FY2015–FY2024)

**Key takeaway:** Federal outlays and deficits jumped sharply with the onset of COVID-19, driving national debt and net interest costs to historic highs by FY2024.


| Fiscal Year | Federal Budget (Request, \$ trillions) | Federal Spending (Outlays, \$ trillions) | Federal Deficit (\$ trillions) | National Debt (Total Public Debt Outstanding, \$ trillions) | Net Interest Cost (\$ trillions) | Official Link |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| FY2015 | 3.9 [^1] | 3.5 [^1] | 0.5 [^1] | 18.1 [^2] | 0.223 [^3] | https://www.whitehouse.gov/omb/historical-tables/ |
| FY2016 | 4.0 [^1] | 3.9 [^1] | 0.6 [^1] | 19.6 [^2] | 0.240 [^3] | https://www.whitehouse.gov/omb/historical-tables/ |
| FY2017 | 4.2 [^1] | 4.1 [^1] | 0.7 [^1] | 20.2 [^2] | 0.285 [^3] | https://www.whitehouse.gov/omb/historical-tables/ |
| FY2018 | 4.1 [^1] | 4.1 [^1] | 0.8 [^1] | 21.5 [^2] | 0.331 [^3] | https://www.whitehouse.gov/omb/historical-tables/ |
| FY2019 | 4.4 [^1] | 4.4 [^1] | 0.9 [^1] | 22.7 [^2] | 0.345 [^3] | https://www.whitehouse.gov/omb/historical-tables/ |
| FY2020 | 6.5 [^1] | 6.6 [^1] | 3.1 [^1] | 26.9 [^2] | 0.345 [^3] | https://www.whitehouse.gov/omb/historical-tables/ |
| FY2021 | 6.8 [^1] | 6.8 [^1] | 2.8 [^1] | 28.4 [^2] | 0.569 [^3] | https://www.whitehouse.gov/omb/historical-tables/ |
| FY2022 | 6.3 [^1] | 6.3 [^1] | 1.1 [^1] | 30.9 [^2] | 0.666 [^3] | https://www.whitehouse.gov/omb/historical-tables/ |
| FY2023 | 6.1 [^1] | 6.3 [^1] | 1.5 [^1] | 32.6 [^2] | 0.658 [^4] | https://www.whitehouse.gov/omb/historical-tables/ |
| FY2024 | 6.8 [^1] | 6.7 [^1] | 2.7 [^1] | 34.4 [^2] | 0.881 [^4] | https://www.whitehouse.gov/omb/historical-tables/ |

- Federal Budget (President’s Budget Request) and Federal Spending (Outlays) are from OMB Historical Table 1.1.[^1]
- National Debt (Total Public Debt Outstanding) is from Treasury’s Monthly Treasury Statement series.[^2]
- Net Interest Cost on gross federal debt:
    - FY2015–FY2022 from CBO’s historical interest reports.[^3]
    - FY2023–FY2024 from the Peterson Foundation and CBO.[^4]
<span style="display:none">[^10][^11][^12][^5][^6][^7][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://en.wikipedia.org/wiki/United_States_federal_budget

[^2]: https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/

[^3]: https://www.crfb.org/blogs/interest-debt-grow-past-1-trillion-next-year

[^4]: https://trumpwhitehouse.archives.gov/wp-content/uploads/2020/02/hist_fy21.pdf

[^5]: https://en.wikipedia.org/wiki/2015_United_States_federal_budget

[^6]: https://www.pgpf.org/article/any-way-you-look-at-it-interest-costs-on-the-national-debt-will-soon-be-at-an-all-time-high/

[^7]: https://obamawhitehouse.archives.gov/omb/budget/Historicals

[^8]: https://www.cbo.gov/publication/most-recent/graphics

[^9]: https://www.cbpp.org/research/federal-budget/deficits-debt-and-interest

[^10]: https://www.whitehouse.gov/omb/information-resources/budget/historical-tables/

[^11]: https://www.pgpf.org/article/what-are-interest-costs-on-the-national-debt/

[^12]: https://en.wikipedia.org/wiki/National_debt_of_the_United_States



[The End of Response]

### Single-Row (One extracted item)

[The Start of Single-Row]

| Fiscal Year | Federal Budget (Request, \$ trillions) | Federal Spending (Outlays, \$ trillions) | Federal Deficit (\$ trillions) | National Debt (Total Public Debt Outstanding, \$ trillions) | Net Interest Cost (\$ trillions) | Official Link |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| FY2022 | 6.3 [^1] | 6.3 [^1] | 1.1 [^1] | 30.9 [^2] | 0.666 [^3] | https://www.whitehouse.gov/omb/historical-tables/ |

[The End of Single-Row]

------------------------------------------------------------
## Core Principle

Your task is NOT to evaluate whether the Single-Row answers the entire Query. Your task IS ONLY to evaluate whether THIS Single-Row:

1. Correctly reflects the part of the Response it was extracted from;
2. Is factually correct according to verification tools.

You MUST ignore completeness. You MUST evaluate only the correctness of THIS Single-Row's own claims.

------------------------------------------------------------
## Role and High-Level Objective

Act as a neutral, impartial judge. All factual checks must be performed using Playwright MCP tools.

------------------------------------------------------------
## Step-by-Step Evaluation Procedure

### Step 1 — Initial Read
- Read the Query, Response, and Single-Row fully.

### Step 2 — Trace Source in the Response
- Locate the corresponding content in the Response.
- Confirm the Single-Row faithfully reflects the Response.

### Step 3 — Verify Each Claim Individually with Playwright MCP Tools
- Focus strictly on content relevant to the Query.
- Do not let style, language, or level of detail influence judgment.
- Treat "N/A", "NA", or "Data Unavailable" as problematic unless explicitly allowed.
- Follow explicit references in the Response: URLs, citations, or footnotes (e.g., `[^1]`, `<sup>1</sup>`).
- Open referenced pages with Playwright MCP tools and locate supporting evidence.
- Primarily rely on references in the Response; if none exist, search authoritative sources using the tools.
- If a reference is unreachable, paywalled, or does not support the claim, mark accordingly.
- Verify every field if the item contains multiple attributes (e.g., in a table row).
- Numeric values must strictly match authoritative sources—no tolerance allowed.

### Step 4 — Record Verification Results
For every claim in the Single-Row record:
- Supported / Contradicted / Not verifiable

------------------------------------------------------------
## Final Judgment Rules

A Single-Row is labeled **[1]** ONLY IF:
1. It contains at least one claim relevant to the Query; AND
2. Every claim is factually correct; AND
3. It faithfully represents the Response.

Otherwise, assign **[0]**.

### If ANY claim is:
- incorrect, OR
- missing, OR
- unverifiable
→ assign **[0]**

------------------------------------------------------------
## Strict Requirements

- You MUST use Playwright MCP tools for all factual verification.
- You MUST NOT add or infer information beyond what is provided.

------------------------------------------------------------
## Output Format (Strict)

Your final output must be exactly one line:

Response: [1]
or
Response: [0]

Nothing else.
