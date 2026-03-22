# Agent-as-a-Judge Task

You will verify the factual correctness of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

For a comparative politics study on descriptive representation, compile the share of women in the lower or single chamber of every OECD member’s national parliament at four benchmark dates: 31 Dec 1995, 31 Dec 2005, 31 Dec 2015, and 31 Dec 2024. Exclude upper chambers. Regarding the total seats, please provide the total number of seats in the lower parliament.  If a country joined the OECD after 1995, record 'NA' for all statistics for years before membership. Please provide official links to support your statement.

Please output one Markdown table with the columns, in this exact order:
 Country | Share of Women Seats 1995(%) | Total Seats 1995 | Share of Women Seats 2005(%) | Total Seats 2005 | Share of Women Seats 2015(%) | Total Seats 2015 |  Share of Women Seats 2024(%) | Total Seats 2024 

[The End of Query]

### Response

[The Start of Response]

| Country | Share of Women Seats 1995(%) | Total Seats 1995 | Share of Women Seats 2005(%) | Total Seats 2005 | Share of Women Seats 2015(%) | Total Seats 2015 | Share of Women Seats 2024(%) | Total Seats 2024 |
|---------| ---------------------------- | ---------------- | ---------------------------- | ---------------- | ---------------------------- | ---------------- | ---------------------------- | ---------------- |
| Australia | 9.5 | 147 | 24.7 | 150 | 26.7 | 150 | 39.1 | 150 |
| Austria | 23.5 | 183 | 33.9 | 183 | 30.6 | 183 | 36.1 | 183 |
| Belgium | 12.0 | 150 | 34.7 | 150 | 39.3 | 150 | 39.3 | 150 |
| Canada | 18.0 | 295 | 21.1 | 308 | 26.0 | 338 | 30.9 | 338 |
| Chile | NA | NA | NA | NA | 15.8 | 120 | 35.1 | 155 |
| Colombia | NA | NA | NA | NA | 19.9 | 166 | 29.4 | 188 |
| Costa Rica | NA | NA | NA | NA | 33.3 | 57 | 49.1 | 57 |
| Czech Republic | 10.0 | 200 | 17.0 | 200 | 20.0 | 200 | 25.5 | 200 |
| Denmark | 33.0 | 179 | 36.9 | 179 | 37.4 | 179 | 43.6 | 179 |
| Estonia | NA | NA | NA | NA | 23.8 | 101 | 28.7 | 101 |
| Finland | 33.5 | 200 | 37.5 | 200 | 41.5 | 200 | 45.5 | 200 |
| France | 6.4 | 577 | 12.2 | 574 | 26.2 | 577 | 36.2 | 577 |
| Germany | 26.2 | 672 | 31.8 | 614 | 36.5 | 631 | 35.7 | 736 |
| Greece | 6.0 | 300 | 13.0 | 300 | 19.7 | 300 | 23.3 | 300 |
| Hungary | NA | NA | 9.1 | 385 | 10.1 | 198 | 15.2 | 199 |
| Iceland | 25.4 | 63 | 33.3 | 63 | 41.3 | 63 | 46.0 | 63 |
| Ireland | 12.7 | 166 | 13.3 | 166 | 16.3 | 166 | 25.3 | 160 |
| Israel | NA | NA | 15.0 | 120 | 26.7 | 120 | 24.2 | 120 |
| Italy | 15.1 | 630 | 11.5 | 616 | 31.0 | 630 | 32.8 | 400 |
| Japan | 2.7 | 511 | 9.0 | 480 | 9.5 | 475 | 15.7 | 465 |
| Korea | NA | NA | 13.4 | 299 | 16.3 | 300 | 20.3 | 300 |
| Latvia | NA | NA | NA | NA | 18.0 | 100 | 31.0 | 100 |
| Lithuania | NA | NA | NA | NA | 23.4 | 141 | 28.4 | 141 |
| Luxembourg | 20.0 | 60 | 23.3 | 60 | 28.3 | 60 | 35.0 | 60 |
| Mexico | 14.2 | 500 | 24.2 | 500 | 42.4 | 498 | 50.2 | 500 |
| Netherlands | 31.3 | 150 | 36.7 | 150 | 37.3 | 150 | 39.3 | 150 |
| New Zealand | 21.2 | 99 | 32.2 | 121 | 31.4 | 121 | 45.5 | 123 |
| Norway | 39.4 | 165 | 37.9 | 169 | 39.6 | 169 | 44.4 | 169 |
| Poland | NA | NA | 20.4 | 460 | 27.4 | 460 | 31.3 | 460 |
| Portugal | 8.7 | 230 | 21.3 | 230 | 34.8 | 230 | 34.8 | 230 |
| Slovak Republic | NA | NA | 16.7 | 150 | 18.7 | 150 | 23.3 | 150 |
| Slovenia | NA | NA | NA | NA | 35.6 | 90 | 35.6 | 90 |
| Spain | 16.0 | 350 | 36.0 | 350 | 39.7 | 350 | 44.3 | 350 |
| Sweden | 40.4 | 349 | 45.3 | 349 | 43.6 | 349 | 45.0 | 349 |
| Switzerland | 17.5 | 200 | 25.0 | 200 | 32.0 | 200 | 38.5 | 200 |
| Turkey | 1.8 | 450 | 4.4 | 550 | 14.9 | 550 | 19.9 | 600 |
| United Kingdom | 9.2 | 651 | 19.7 | 646 | 29.4 | 650 | 40.5 | 650 |
| United States | 10.9 | 440 | 15.2 | 435 | 19.3 | 435 | 28.7 | 435 |

---

The table above provides the share of women in the lower or single chamber of parliament for each OECD member country at the specified benchmark dates, along with the total number of seats at those times. For countries that joined the OECD after 1995, 'NA' is recorded for years before membership, as per the query instructions. The percentages are rounded to one decimal place for consistency.

The data is sourced from the Inter-Parliamentary Union (IPU), which is the official authority for this information. Note that for 1995, the data is from the latest election before or in 1995, as exact Dec 31 data was not available, but it reflects the situation around that time.

For 2024, the total seats are updated for known changes since 2015 (e.g., Chile, Colombia, Ireland, New Zealand, Italy, Japan, Turkey), based on verified sources from web searches and Wikipedia extracts, to reflect the structure as of end 2024.

**Key Citations**:
- OECD Members and Partners: https://www.oecd.org/en/about/members-partners.html
- IPU Women in Parliaments 1945-1995: http://archive.ipu.org/PDF/publications/women45-95_en.pdf
- IPU World Classification as of 31 Dec 2005: http://archive.ipu.org/wmn-e/arc/classif311205.htm
- IPU World Classification as of 1 Jan 2016 (reflecting end 2015): http://archive.ipu.org/wmn-e/arc/classif010116.htm
- UN Women/IPU Women in Politics 2025 Map (as of 1 Jan 2025, reflecting end 2024): https://www.unwomen.org/sites/default/files/2025-03/women-in-politics-2025-en.pdf
- Additional total seats verification from Wikipedia List of Legislatures by Number of Members: https://en.wikipedia.org/wiki/List_of_legislatures_by_number_of_members

[The End of Response]

### Single-Row (One extracted item)

[The Start of Single-Row]

| Country | Share of Women Seats 1995(%) | Total Seats 1995 | Share of Women Seats 2005(%) | Total Seats 2005 | Share of Women Seats 2015(%) | Total Seats 2015 | Share of Women Seats 2024(%) | Total Seats 2024 |
|---------| ---------------------------- | ---------------- | ---------------------------- | ---------------- | ---------------------------- | ---------------- | ---------------------------- | ---------------- |
| Mexico | 14.2 | 500 | 24.2 | 500 | 42.4 | 498 | 50.2 | 500 |

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
