# Agent-as-a-Judge Task

You will verify the factual correctness of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Please list the top 10 individuals from the Forbes Global Billionaires Ranking for each year from 2019 to 2024 (including 2024). For each person, include their name, ranking, net worth, source of wealth, and age of that year end. Present the information in a table format. All your data should come from Forbes, which means the ages and net worth are calculated based on the publication date. Please provide corresponding links to support your statement.

Please present the organized data in one Markdown table format.
The column headers, in order, should be:
Year, Rank, Name, Net Worth (in USD billions), Age, Source of Wealth.

[The End of Query]

### Response

[The Start of Response]

# Top 10 Forbes Global Billionaires (2019–2024)

Below is the annual ranking of the world’s top 10 billionaires for each year from 2019 through 2024, including their rank, name, net worth (USD billions), age at year-end, and primary source of wealth. All figures are based on Forbes’ year-end publications for each list.


| Year | Rank | Name | Net Worth (USD B) | Age | Source of Wealth |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 2019 | 1 | Jeff Bezos \& family | 131.0 | 55 | Amazon |
| 2019 | 2 | Bill Gates | 96.5 | 64 | Microsoft |
| 2019 | 3 | Warren Buffett | 82.5 | 89 | Berkshire Hathaway |
| 2019 | 4 | Bernard Arnault \& family | 76.0 | 70 | LVMH |
| 2019 | 5 | Carlos Slim Helú \& family | 64.0 | 79 | Telecom |
| 2019 | 6 | Amancio Ortega | 62.7 | 83 | Inditex (Zara) |
| 2019 | 7 | Larry Ellison | 62.5 | 75 | Oracle |
| 2019 | 8 | Mark Zuckerberg | 62.3 | 35 | Facebook (Meta) |
| 2019 | 9 | Michael Bloomberg | 55.5 | 77 | Bloomberg LP |
| 2019 | 10 | Larry Page | 50.8 | 46 | Google |
| 2020 | 1 | Jeff Bezos | 145.0 | 56 | Amazon |
| 2020 | 2 | Bill Gates | 104.0 | 65 | Microsoft |
| 2020 | 3 | Bernard Arnault \& family | 92.0 | 71 | LVMH |
| 2020 | 4 | Warren Buffett | 73.0 | 90 | Berkshire Hathaway |
| 2020 | 5 | Mark Zuckerberg | 69.0 | 36 | Facebook (Meta) |
| 2020 | 6 | Larry Ellison | 66.0 | 76 | Oracle |
| 2020 | 7 | Steve Ballmer | 63.0 | 64 | Microsoft |
| 2020 | 8 | Amancio Ortega | 61.0 | 84 | Inditex (Zara) |
| 2020 | 9 | Larry Page | 58.0 | 47 | Google |
| 2020 | 10 | Jim Walton | 57.0 | 72 | Walmart |
| 2021 | 1 | Elon Musk | 301.0 | 50 | Tesla, SpaceX |
| 2021 | 2 | Jeff Bezos | 202.0 | 57 | Amazon |
| 2021 | 3 | Bernard Arnault \& family | 197.0 | 72 | LVMH |
| 2021 | 4 | Bill Gates | 139.0 | 66 | Microsoft |
| 2021 | 5 | Larry Ellison | 130.0 | 77 | Oracle |
| 2021 | 6 | Larry Page | 127.0 | 48 | Google |
| 2021 | 7 | Sergey Brin | 122.0 | 48 | Google |
| 2021 | 8 | Mark Zuckerberg | 121.0 | 37 | Facebook (Meta) |
| 2021 | 9 | Steve Ballmer | 106.0 | 65 | Microsoft |
| 2021 | 10 | Warren Buffett | 105.0 | 91 | Berkshire Hathaway |
| 2022 | 1 | Elon Musk | 219.0 | 51 | Tesla, SpaceX |
| 2022 | 2 | Bernard Arnault \& family | 158.0 | 73 | LVMH |
| 2022 | 3 | Jeff Bezos | 171.0 | 58 | Amazon |
| 2022 | 4 | Gautam Adani \& family | 125.0 | 60 | Infrastructure, commodities |
| 2022 | 5 | Bill Gates | 129.0 | 67 | Microsoft |
| 2022 | 6 | Warren Buffett | 118.0 | 92 | Berkshire Hathaway |
| 2022 | 7 | Larry Ellison | 117.0 | 78 | Oracle |
| 2022 | 8 | Mukesh Ambani | 107.0 | 65 | Diversified (Reliance) |
| 2022 | 9 | Steve Ballmer | 106.0 | 66 | Microsoft |
| 2022 | 10 | Carlos Slim Helú \& family | 93.0 | 80 | Telecom |
| 2023 | 1 | Bernard Arnault \& family | 211.0 | 74 | LVMH |
| 2023 | 2 | Elon Musk | 180.0 | 52 | Tesla, SpaceX |
| 2023 | 3 | Jeff Bezos | 141.0 | 59 | Amazon |
| 2023 | 4 | Gautam Adani \& family | 132.0 | 61 | Infrastructure, commodities |
| 2023 | 5 | Warren Buffett | 118.0 | 93 | Berkshire Hathaway |
| 2023 | 6 | Bill Gates | 114.0 | 68 | Microsoft |
| 2023 | 7 | Larry Ellison | 112.0 | 79 | Oracle |
| 2023 | 8 | Larry Page | 111.0 | 49 | Google |
| 2023 | 9 | Sergey Brin | 109.0 | 49 | Google |
| 2023 | 10 | Mukesh Ambani | 108.0 | 66 | Diversified (Reliance) |
| 2024 | 1 | Bernard Arnault \& family | 255.0 | 75 | LVMH |
| 2024 | 2 | Elon Musk | 185.0 | 53 | Tesla, SpaceX |
| 2024 | 3 | Gautam Adani \& family | 143.0 | 62 | Infrastructure, commodities |
| 2024 | 4 | Jeff Bezos | 140.0 | 60 | Amazon |
| 2024 | 5 | Bill Gates | 113.0 | 69 | Microsoft |
| 2024 | 6 | Warren Buffett | 109.0 | 94 | Berkshire Hathaway |
| 2024 | 7 | Larry Ellison | 108.0 | 80 | Oracle |
| 2024 | 8 | Steve Ballmer | 103.0 | 67 | Microsoft |
| 2024 | 9 | Mukesh Ambani | 100.0 | 67 | Diversified (Reliance) |
| 2024 | 10 | Mark Zuckerberg | 100.0 | 38 | Facebook (Meta) |

*All data are drawn from Forbes’ annual “Global Billionaires” rankings for each respective year.*
<span style="display:none">[^1][^10][^11][^2][^3][^4][^5][^6][^7][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://www.beckershospitalreview.com/hospital-management-administration/forbes-2019-world-s-billionaires-the-10-richest-people/

[^2]: https://www.visualcapitalist.com/richest-people-in-the-world/

[^3]: https://www.visualcapitalist.com/richest-people-in-the-world-2021/

[^4]: https://www.forbes.com/sites/denizcam/2019/12/20/the-biggest-billionaire-winners-and-losers-of-2019/

[^5]: https://www.forbes.com/sites/forbespr/2020/04/07/forbes-publishes-34th-annual-list-of-global-billionaires/

[^6]: https://www.forbes.com/sites/kerryadolan/2021/04/06/forbes-35th-annual-worlds-billionaires-list-facts-and-figures-2021/

[^7]: https://www.usatoday.com/story/money/2019/10/03/forbes-400-amazon-ceo-remains-richest-person-us-despite-divorce/3849962002/

[^8]: https://www.foxbusiness.com/money/richest-billionaires-world-2020-forbes

[^9]: https://www.youtube.com/watch?v=F7XIRDsvMeA

[^10]: https://www.investopedia.com/articles/investing/012715/5-richest-people-world.asp

[^11]: https://www.youtube.com/watch?v=mvOF76T_8i4



[The End of Response]

### Single-Row (One extracted item)

[The Start of Single-Row]

| Year | Rank | Name | Net Worth (USD B) | Age | Source of Wealth |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 2024 | 9 | Mukesh Ambani | 100.0 | 67 | Diversified (Reliance) |

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
