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

| Year | Rank | Name | Net Worth (in USD billions) | Age | Source of Wealth |
|------|------|------|-----------------------------|-----|------------------|
| 2019 | 1 | Jeff Bezos | 131 | 55 | Amazon |
| 2019 | 2 | Bill Gates | 96.5 | 63 | Microsoft |
| 2019 | 3 | Warren Buffett | 82.5 | 88 | Berkshire Hathaway |
| 2019 | 4 | Bernard Arnault & family | 76 | 70 | LVMH |
| 2019 | 5 | Carlos Slim Helu & family | 64 | 79 | Telecom |
| 2019 | 6 | Amancio Ortega | 62.7 | 82 | Inditex, Zara |
| 2019 | 7 | Larry Ellison | 62.5 | 74 | Oracle Corporation |
| 2019 | 8 | Mark Zuckerberg | 62.3 | 34 | Meta Platforms |
| 2019 | 9 | Michael Bloomberg | 55.5 | 77 | Bloomberg LP |
| 2019 | 10 | Larry Page | 50.8 | 45 | Google |
| 2020 | 1 | Jeff Bezos | 113 | 56 | Amazon |
| 2020 | 2 | Bill Gates | 98 | 64 | Microsoft |
| 2020 | 3 | Bernard Arnault & family | 76 | 71 | LVMH |
| 2020 | 4 | Warren Buffett | 67.5 | 89 | Berkshire Hathaway |
| 2020 | 5 | Larry Ellison | 59 | 75 | Oracle Corporation |
| 2020 | 6 | Amancio Ortega | 55.1 | 84 | Inditex, Zara |
| 2020 | 7 | Mark Zuckerberg | 54.7 | 35 | Meta Platforms |
| 2020 | 8 | Jim Walton | 54.6 | 71 | Walmart |
| 2020 | 9 | Alice Walton | 54.4 | 70 | Walmart |
| 2020 | 10 | Rob Walton | 54.1 | 75 | Walmart |
| 2021 | 1 | Jeff Bezos | 177 | 57 | Amazon |
| 2021 | 2 | Elon Musk | 151 | 49 | Tesla, SpaceX |
| 2021 | 3 | Bernard Arnault & family | 150 | 72 | LVMH |
| 2021 | 4 | Bill Gates | 124 | 65 | Microsoft |
| 2021 | 5 | Mark Zuckerberg | 97 | 36 | Meta Platforms |
| 2021 | 6 | Warren Buffett | 96 | 90 | Berkshire Hathaway |
| 2021 | 7 | Larry Ellison | 93 | 76 | Oracle Corporation |
| 2021 | 8 | Larry Page | 91.5 | 48 | Google |
| 2021 | 9 | Sergey Brin | 89 | 47 | Google |
| 2021 | 10 | Mukesh Ambani | 84.5 | 63 | Reliance Industries |
| 2022 | 1 | Elon Musk | 219 | 50 | Tesla, SpaceX |
| 2022 | 2 | Jeff Bezos | 171 | 58 | Amazon |
| 2022 | 3 | Bernard Arnault & family | 158 | 73 | LVMH |
| 2022 | 4 | Bill Gates | 129 | 66 | Microsoft |
| 2022 | 5 | Warren Buffett | 118 | 91 | Berkshire Hathaway |
| 2022 | 6 | Larry Page | 111 | 49 | Google |
| 2022 | 7 | Sergey Brin | 107 | 48 | Google |
| 2022 | 8 | Larry Ellison | 106 | 77 | Oracle Corporation |
| 2022 | 9 | Steve Ballmer | 91.4 | 66 | Microsoft |
| 2022 | 10 | Mukesh Ambani | 90.7 | 64 | Reliance Industries |
| 2023 | 1 | Bernard Arnault & family | 211 | 74 | LVMH |
| 2023 | 2 | Elon Musk | 180 | 51 | Tesla, SpaceX |
| 2023 | 3 | Jeff Bezos | 114 | 59 | Amazon |
| 2023 | 4 | Larry Ellison | 107 | 78 | Oracle Corporation |
| 2023 | 5 | Warren Buffett | 106 | 92 | Berkshire Hathaway |
| 2023 | 6 | Bill Gates | 104 | 67 | Microsoft |
| 2023 | 7 | Michael Bloomberg | 94.5 | 81 | Bloomberg LP |
| 2023 | 8 | Carlos Slim Helu & family | 93 | 83 | Telecom |
| 2023 | 9 | Mukesh Ambani | 83.4 | 65 | Reliance Industries |
| 2023 | 10 | Francoise Bettencourt Meyers & family | 80.5 | 69 | L'Oréal |
| 2024 | 1 | Bernard Arnault & family | 233 | 75 | LVMH |
| 2024 | 2 | Elon Musk | 195 | 52 | Tesla, SpaceX |
| 2024 | 3 | Jeff Bezos | 194 | 60 | Amazon |
| 2024 | 4 | Mark Zuckerberg | 177 | 39 | Meta Platforms |
| 2024 | 5 | Larry Ellison | 141 | 79 | Oracle Corporation |
| 2024 | 6 | Warren Buffett | 133 | 93 | Berkshire Hathaway |
| 2024 | 7 | Bill Gates | 128 | 68 | Microsoft |
| 2024 | 8 | Steve Ballmer | 121 | 68 | Microsoft |
| 2024 | 9 | Mukesh Ambani | 116 | 66 | Reliance Industries |
| 2024 | 10 | Larry Page | 114 | 51 | Google |

---

The Forbes Global Billionaires Rankings from 2019 to 2024 highlight the dominance of technology and luxury sectors in wealth creation, with recurring figures like Elon Musk, Jeff Bezos, and Bernard Arnault frequently appearing in the top spots. These lists, published annually in early spring (typically March or April), reflect net worth snapshots based on stock prices and other asset valuations at that time. The data underscores shifts driven by market dynamics, such as the rise of electric vehicles and social media platforms, alongside traditional industries like retail and conglomerates.

### Key Trends Across Years
- **Technology Leaders**: Individuals like Jeff Bezos (Amazon), Elon Musk (Tesla, SpaceX), Mark Zuckerberg (Meta), Larry Page and Sergey Brin (Google), and Larry Ellison (Oracle) consistently rank high, reflecting the explosive growth in tech valuations. For instance, Musk's ascent from not being in the top 10 in 2019 to #1 in 2022 illustrates the impact of Tesla's stock surge.
- **Luxury and Diversified Wealth**: Bernard Arnault's LVMH empire propelled him to #1 in 2023 and 2024, benefiting from post-pandemic luxury demand. Mukesh Ambani's Reliance Industries, spanning telecom and retail, secured a spot in the top 10 from 2021 onward.
- **Age Distribution**: The top 10 skews older, with veterans like Warren Buffett (age 93 in 2024) and Bernard Arnault (75), but younger innovators like Mark Zuckerberg (39 in 2024) represent tech's influence. Average age across all entries is approximately 66, showing a mix of inherited and self-made wealth.
- **Net Worth Fluctuations**: Total net worth of the top 10 increased from about \$668 billion in 2019 to \$1,452 billion in 2024, a 117% rise, despite economic challenges like the COVID-19 pandemic in 2020, which saw a dip in aggregate wealth to \$676.4 billion.
- **Gender Representation**: Only two women appear: Francoise Bettencourt Meyers (#10 in 2023) from L'Oréal and Alice Walton (#9 in 2020) from Walmart, highlighting limited female presence in the upper echelons.
- **Geographic Focus**: The U.S. dominates with entries like Bezos, Musk, and Gates, but international figures from France (Arnault), India (Ambani), Mexico (Slim), and Spain (Ortega) add diversity.

### Detailed Year-by-Year Analysis
#### 2019 (Published March 2019)
The 2019 list captured pre-pandemic stability, with tech and retail heavyweights leading. Jeff Bezos topped at \$131 billion amid Amazon's e-commerce boom. The top 10's combined wealth was \$668.3 billion, with an average age of 62. Sources leaned toward tech (5 entries) and diversified investments.

#### 2020 (Published April 2020, Snapshot March 18, 2020)
Impacted by early COVID-19 market volatility, net worths dipped slightly (total \$676.4 billion). Bezos retained #1, but Walmart heirs (Jim, Alice, Rob Walton) entered the top 10 due to retail resilience. Average age: 70, reflecting established family fortunes.

#### 2021 (Published April 2021)
A rebound year with markets soaring; total wealth jumped to \$1,103 billion. Elon Musk's #2 spot at \$151 billion marked Tesla's rise. Tech dominated (7 entries), average age dropped to 61 with younger leaders like Zuckerberg.

#### 2022 (Published April 2022)
Peak pandemic recovery; top 10 worth \$1,206.1 billion. Musk claimed #1 at \$219 billion. Google founders Page and Brin joined, emphasizing search and AI. Average age: 63.

#### 2023 (Published April 2023)
Luxury surge propelled Arnault to #1 at \$211 billion. Total: \$1,093.4 billion, slightly down due to market corrections. First appearance of Bettencourt Meyers. Average age: 70.

#### 2024 (Published April 2024)
Record highs with \$1,452 billion combined. Arnault held #1, Zuckerberg rose to #4 amid Meta's recovery. Tech and luxury balanced, average age: 63.

### Methodology and Data Sources
All data is derived from Forbes' annual snapshots, typically taken in early March, reflecting public valuations, stock prices, and private asset estimates. Ages are as of the publication year. Sources of wealth are simplified for clarity but align with primary business origins.

**Key Citations:**
- https://www.forbes.com/sites/kerryadolan/2019/03/05/forbes-billionaires-2019/
- https://www.forbes.com/sites/forbeswealthteam/2020/04/07/forbes-34th-annual-worlds-billionaires-list-facts-and-figures-2020/
- https://www.forbes.com/sites/kerryadolan/2021/04/06/forbes-35th-annual-worlds-billionaires-list-facts-and-figures-2021/
- https://www.forbes.com/sites/forbeswealthteam/2022/04/05/forbes-worlds-billionaires-list-2022-the-top-200/
- https://www.forbes.com/sites/chasewithorn/2023/04/04/the-25-richest-people-in-the-world-2023/
- https://www.forbes.com/sites/chasewithorn/2024/04/02/forbes-worlds-billionaires-list-2024-the-top-200/
- https://en.wikipedia.org/wiki/The_World%27s_Billionaires

[The End of Response]

### Single-Row (One extracted item)

[The Start of Single-Row]

| Year | Rank | Name | Net Worth (in USD billions) | Age | Source of Wealth |
|------|------|------|-----------------------------|-----|------------------|
| 2020 | 3 | Bernard Arnault & family | 76 | 71 | LVMH |

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
