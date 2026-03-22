# Agent-as-a-Judge Task

You will verify the factual correctness of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Please research the following information about Super Bowl: date, champions, host stadium, host city, Nielsen HHLD rating, average viewership across all platforms (million, round to one decimal place), and the half-time show sponsors.  I need annual statistics from 2001 to 2025 (including 2001 and 2025). Provide official links to support your statement.

Please give me the organized data in the format of one Markdown table, with the column names as: 
Year, Champion, Host Stadium, Host City,  Nielsen HHLD Rating, Viewership (million), Half-time Show Sponsors.
For host city, give the full name of the city, like Houston.

[The End of Query]

### Response

[The Start of Response]

# Super Bowl Statistics (2001–2025)

## Data Compilation
The following table compiles the requested statistics based on official sources. Viewership is rounded to one decimal place and represents average across all platforms where available (primarily TV for earlier years, inclusive of streaming for recent ones). For 2025, all details are post-event.

| Year | Champion              | Host Stadium             | Host City       | Nielsen HHLD Rating | Viewership (million) | Half-time Show Sponsors     |
|------|-----------------------|--------------------------|-----------------|---------------------|----------------------|-----------------------------|
| 2001 | Baltimore Ravens     | Raymond James Stadium   | Tampa          | 40.4               | 84.3                | None                       |
| 2002 | New England Patriots | Louisiana Superdome     | New Orleans    | 40.4               | 86.8                | Clear Channel Entertainment|
| 2003 | Tampa Bay Buccaneers | Qualcomm Stadium        | San Diego      | 40.7               | 88.6                | AT&T Wireless              |
| 2004 | New England Patriots | Reliant Stadium         | Houston        | 41.4               | 89.8                | AOL TopSpeed               |
| 2005 | New England Patriots | Alltel Stadium          | Jacksonville   | 41.1               | 86.1                | Ameriquest Mortgage        |
| 2006 | Pittsburgh Steelers  | Ford Field              | Detroit        | 41.6               | 90.9                | Sprint Nextel              |
| 2007 | Indianapolis Colts   | Dolphin Stadium         | Miami Gardens  | 42.6               | 93.2                | Pepsi                      |
| 2008 | New York Giants      | University of Phoenix Stadium | Glendale | 43.1               | 97.5                | Bridgestone                |
| 2009 | Pittsburgh Steelers  | Raymond James Stadium   | Tampa          | 42.0               | 98.7                | None                       |
| 2010 | New Orleans Saints   | Sun Life Stadium        | Miami Gardens  | 45.0               | 106.5               | Bridgestone                |
| 2011 | Green Bay Packers    | Cowboys Stadium         | Arlington      | 46.0               | 111.0               | None                       |
| 2012 | New York Giants      | Lucas Oil Stadium       | Indianapolis   | 47.0               | 111.4               | None                       |
| 2013 | Baltimore Ravens     | Mercedes-Benz Superdome | New Orleans    | 46.4               | 108.7               | Pepsi                      |
| 2014 | Seattle Seahawks     | MetLife Stadium         | East Rutherford| 46.7               | 112.2               | Pepsi                      |
| 2015 | New England Patriots | University of Phoenix Stadium | Glendale | 47.5               | 114.4               | Pepsi                      |
| 2016 | Denver Broncos       | Levi's Stadium          | Santa Clara    | 46.6               | 111.9               | Pepsi                      |
| 2017 | New England Patriots | NRG Stadium             | Houston        | 45.3               | 111.3               | Pepsi                      |
| 2018 | Philadelphia Eagles  | U.S. Bank Stadium       | Minneapolis    | 43.1               | 103.5               | Pepsi                      |
| 2019 | New England Patriots | Mercedes-Benz Stadium   | Atlanta        | 41.1               | 98.5                | Pepsi                      |
| 2020 | Kansas City Chiefs   | Hard Rock Stadium       | Miami Gardens  | 41.6               | 101.3               | Pepsi                      |
| 2021 | Tampa Bay Buccaneers | Raymond James Stadium   | Tampa          | 38.2               | 96.4                | Pepsi                      |
| 2022 | Los Angeles Rams     | SoFi Stadium            | Inglewood      | 36.9               | 112.3               | Pepsi                      |
| 2023 | Kansas City Chiefs   | State Farm Stadium      | Glendale       | 40.4               | 114.2               | Apple Music                |
| 2024 | Kansas City Chiefs   | Allegiant Stadium       | Las Vegas      | 43.5               | 123.7               | Apple Music                |
| 2025 | Philadelphia Eagles  | Caesars Superdome       | New Orleans    | 41.7               | 127.7               | Apple Music                |

This table addresses the core query by organizing annual data from reliable sources. Note that early viewership primarily captures TV audiences, while recent figures (e.g., 2021 onward) include streaming and out-of-home viewing for a more comprehensive total.

**Key Citations:**
- [List of Super Bowl champions - Wikipedia](https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions)
- [Super Bowl television ratings - Wikipedia](https://en.wikipedia.org/wiki/Super_Bowl_television_ratings)
- [List of Super Bowl halftime shows - Wikipedia](https://en.wikipedia.org/wiki/List_of_Super_Bowl_halftime_shows)
- [Super Bowl LIX - Wikipedia](https://en.wikipedia.org/wiki/Super_Bowl_LIX)
- [Super Bowl LIX halftime show - Wikipedia](https://en.wikipedia.org/wiki/Super_Bowl_LIX_halftime_show)
- [Super Bowl LIX averages record audience of 127.7 million viewers](https://www.nfl.com/news/super-bowl-lix-averages-record-audience-of-127-7-million-viewers)
- [Super Bowl LIX Makes TV History With Over 127 Million Viewers | Nielsen](https://www.nielsen.com/news-center/2025/super-bowl-lix-makes-tv-history-with-over-127-million-viewers/)
- [Apple Music Replaces Pepsi as Sponsor of Super Bowl Halftime Show](https://variety.com/2022/music/news/apple-music-super-bowl-halftime-show-pepsi-1235381368/)
- [Super Bowl LVIII Draws 123.7 Million Average Viewers, Largest TV Audience on Record | Nielsen](https://www.nielsen.com/news-center/2024/super-bowl-lviii-draws-123-7-million-average-viewers-largest-tv-audience-on-record/)
- [Nielsen recount: Super Bowl LVII adds 2 million viewers to become most-watched show ever](https://www.latimes.com/entertainment-arts/business/story/2023-05-02/nielsen-does-a-recount-and-finds-super-bowl-lvii-is-the-most-watched-show-of-all-time)

[The End of Response]

### Single-Row (One extracted item)

[The Start of Single-Row]

| Year | Champion              | Host Stadium             | Host City       | Nielsen HHLD Rating | Viewership (million) | Half-time Show Sponsors     |
|------|-----------------------|--------------------------|-----------------|---------------------|----------------------|-----------------------------|
| 2013 | Baltimore Ravens     | Mercedes-Benz Superdome | New Orleans    | 46.4               | 108.7               | Pepsi                      |

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
