# Agent-as-a-Judge Task

You will verify the factual correctness of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

I would like to manage my property and am interested in learning about the top 50 property managers published by the National Multifamily Housing Council for 2025, including their ranking, company name, number of units managed in 2024, and the year the company was founded. Please provide a link to the top 50 property managers published by the National Multifamily Housing Council for 2025 to support your claim.

Please output the organized data in the format of one Markdown table.
The column names in the table are as follows in sequence:
Rank, Company Name, Number of Managed Units in 2024, Company Establishment Time.

[The End of Query]

### Response

[The Start of Response]

| Rank | Company Name                          | Number of Managed Units in 2024 | Company Establishment Time |
|------|---------------------------------------|---------------------------------|----------------------------|
| 1    | Greystar                              | 946,742                        | 1993                       |
| 2    | Asset Living                          | 288,665                        | 1986                       |
| 3    | Willow Bridge Property Company        | 220,676                        | 1965                       |
| 4    | RPM Living                            | 218,661                        | 2002                       |
| 5    | Cushman & Wakefield                   | 167,000                        | 1917                       |
| 6    | FPI Management                        | 165,038                        | 1968                       |
| 7    | Apartment Management Consultants (AMC)| 152,989                        | 2000                       |
| 8    | Avenue5 Residential                   | 142,841                        | 2014                       |
| 9    | Bozzuto                               | 121,232                        | 1988                       |
| 10   | WinnCompanies                         | 116,337                        | 1971                       |
| 11   | BH Management Services                | 107,099                        | 1993                       |
| 12   | MAA                                   | 102,348                        | 1977                       |
| 13   | ZRS Management                        | 92,927                         | 1991                       |
| 14   | Bell Partners                         | 88,407                         | 1976                       |
| 15   | Equity Residential                    | 84,249                         | 1969                       |
| 16   | AvalonBay Communities                 | 83,753                         | 1978                       |
| 17   | RAM Partners                          | 81,252                         | 1989                       |
| 18   | The Michaels Organization             | 79,471                         | 1973                       |
| 19   | Cortland                              | 78,078                         | 2005                       |
| 20   | Monarch Investment & Management Group | 75,871                         | 1992                       |
| 21   | RangeWater Real Estate                | 72,117                         | 2006                       |
| 22   | Edward Rose Building Enterprise       | 71,591                         | 1921                       |
| 23   | Hunt/Envolve                          | 66,316                         | 1947                       |
| 24   | Weidner Apartment Homes               | 66,249                         | 1977                       |
| 25   | CONAM Management Corporation          | 62,818                         | 1975                       |
| 26   | Hawthorne Residential Partners        | 62,651                         | 2009                       |
| 27   | Essex Property Trust                  | 62,510                         | 1971                       |
| 28   | The Related Companies                 | 62,455                         | 1972                       |
| 29   | FPA Multifamily                       | 62,244                         | 1985                       |
| 30   | Bridge Investment Group               | 61,150                         | 2009                       |
| 31   | UDR                                   | 60,123                         | 1972                       |
| 32   | Camden Property Trust                 | 58,858                         | 1981                       |
| 33   | Harbor Group International            | 58,316                         | 1985                       |
| 34   | Cardinal Group Companies              | 54,622                         | 2007                       |
| 35   | Village Green                         | 50,455                         | 1919                       |
| 36   | GoldOller Real Estate Investments      | 48,134                         | 2009                       |
| 37   | Windsor Communities                   | 48,071                         | 1960                       |
| 38   | Balfour Beatty Communities            | 47,485                         | 1999                       |
| 39   | Pegasus Residential                   | 46,264                         | 2009                       |
| 40   | Drucker + Falk                        | 43,294                         | 1938                       |
| 41   | Dominium                              | 43,199                         | 1972                       |
| 42   | Elmington                             | 38,953                         | 2010                       |
| 43   | Fairfield Residential                 | 38,790                         | 1985                       |
| 44   | Berkshire Residential Investments     | 38,703                         | 1966                       |
| 45   | United Apartment Group                 | 37,521                         | 1995                       |
| 46   | Mission Rock Residential              | 37,236                         | 2012                       |
| 47   | Westdale Real Estate Investment & Management | 36,313                  | 1991                       |
| 48   | Valiant Residential                   | 35,724                         | 1987                       |
| 49   | Beztak                                | 34,958                         | 1964                       |
| 50   | Knightvest Capital                    | 34,697                         | 2007                       |

For the primary source, visit the NMHC's official 2025 Top Managers List at [https://www.nmhc.org/research-insight/the-nmhc-50/top-50-lists/2025-top-managers-list/](https://www.nmhc.org/research-insight/the-nmhc-50/top-50-lists/2025-top-managers-list/). Note: Founding years for some firms (e.g., Beztak) are approximate based on predecessor entities, as exact dates vary in sources.

### Key Citations
- [NMHC 2025 Top Managers List](https://www.nmhc.org/research-insight/the-nmhc-50/top-50-lists/2025-top-managers-list/)
- [Multifamily Executive: 2025 NMHC Top 50 Managers](https://www.multifamilyexecutive.com/business-finance/top-50/2025-nmhc-top-50-managers_o)
- [Yield PRO: NMHC 50 Recognizes Industry’s Top Firms](https://yieldpro.com/2025/04/nmhc-50-recognizes-industrys-top-firms-3/)
- [Asset Living Ranked No. 2 on NMHC’s 2025 Top 50 Managers List](https://www.assetliving.com/blogs/asset-living-ranked-no-2-on-nmhcs-2025-top-50-managers-list)
- [Willow Bridge Named 3rd Largest Multifamily Manager in 2025 NMHC Top 50 Rankings](https://www.willowbridgepc.com/about/news/3218-willow-bridge-named-3rd-largest-multifamily-manager-in-2025-nmhc-top-50-rankings)
- [Valiant Residential: How Valiant Grew into a Top 50 Multifamily Firm](https://www.multifamilydive.com/news/apartment-management-nmhc-top-50-valiant-residential/749034/)
- [Beztak Recognized as a US Best Managed Company](https://www.globenewswire.com/news-release/2025/05/15/3082264/0/en/Beztak-Recognized-as-a-US-Best-Managed-Company-and-National-Multifamily-Housing-Council-2025-Top-50-Managers.html)
- [Knightvest Capital Named to NMHC Top 50 Lists](https://www.prnewswire.com/news-releases/knightvest-capital-named-to-nmhc-top-50-lists-for-nations-largest-apartment-owners-and-managers-302419174.html)
- [Greystar: About Greystar](https://www.greystar.com/business/about-greystar/newsroom/greystar-named-in-2025-nmhc-top-50)
- [Asset Living: 37 Years of Growth](https://www.assetliving.com/blogs/asset-living-37-years-of-growth-and-innovation-in-property-management)

[The End of Response]

### Single-Row (One extracted item)

[The Start of Single-Row]

| Rank | Company Name                          | Number of Managed Units in 2024 | Company Establishment Time |
|------|---------------------------------------|---------------------------------|----------------------------|
| 41   | Dominium                              | 43,199                         | 1972                       |

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
