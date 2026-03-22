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

# Super Bowl Annual Statistics (2001–2025)

| Year | Champion | Host Stadium | Host City | Nielsen HHLD Rating | Viewership (million) | Half-time Show Sponsors |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 2001 | Baltimore Ravens | Raymond James Stadium | Tampa | 40.4[^1] | 84.3[^1] | E-Trade[^2] |
| 2002 | New England Patriots | Louisiana Superdome | New Orleans | 40.4[^1] | 86.8[^1] | E-Trade[^2] |
| 2003 | Tampa Bay Buccaneers | Qualcomm Stadium | San Diego | 40.7[^1] | 88.6[^1] | Dr Pepper[^3] |
| 2004 | New England Patriots | Reliant Stadium | Houston | 41.4[^1] | 89.8[^1] | Pepsi[^3] |
| 2005 | New England Patriots | Alltel Stadium | Jacksonville | 41.1[^1] | 86.1[^1] | Pepsi[^3] |
| 2006 | Pittsburgh Steelers | Ford Field | Detroit | 41.6[^1] | 90.7[^1] | Pepsi[^3] |
| 2007 | Indianapolis Colts | Dolphin Stadium | Miami Gardens | 42.6[^1] | 93.2[^1] | Pepsi[^3] |
| 2008 | New York Giants | University of Phoenix Stadium | Glendale | 43.1[^1] | 97.4[^1] | Pepsi[^3] |
| 2009 | Pittsburgh Steelers | Raymond James Stadium | Tampa | 42.0[^1] | 98.7[^1] | Pepsi[^3] |
| 2010 | New Orleans Saints | Sun Life Stadium | Miami Gardens | 45.0[^1] | 106.5[^1] | Pepsi[^3] |
| 2011 | Green Bay Packers | Cowboys Stadium | Arlington | 46.0[^1] | 111.0[^1] | Pepsi[^3] |
| 2012 | New York Giants | Lucas Oil Stadium | Indianapolis | 47.1[^1] | 111.3[^1] | Pepsi[^3] |
| 2013 | Baltimore Ravens | Mercedes-Benz Superdome | New Orleans | 46.4[^1] | 108.7[^1] | Pepsi[^3] |
| 2014 | Seattle Seahawks | MetLife Stadium | East Rutherford | 46.7[^1] | 112.8[^1] | Pepsi[^3] |
| 2015 | New England Patriots | University of Phoenix Stadium | Glendale | 47.5[^1] | 114.8[^1] | Pepsi[^3] |
| 2016 | Denver Broncos | Levi’s Stadium | Santa Clara | 46.6[^1] | 112.3[^1] | Pepsi[^3] |
| 2017 | New England Patriots | NRG Stadium | Houston | 45.3[^1] | 112.0[^1] | Pepsi[^3] |
| 2018 | Philadelphia Eagles | U.S. Bank Stadium | Minneapolis | 43.1[^1] | 104.0[^1] | Pepsi[^3] |
| 2019 | New England Patriots | Mercedes-Benz Stadium | Atlanta | 41.4[^1] | 98.9[^1] | Pepsi[^3] |
| 2020 | Kansas City Chiefs | Hard Rock Stadium | Miami Gardens | 42.0[^1] | 102.1[^1] | Pepsi[^3] |
| 2021 | Tampa Bay Buccaneers | Raymond James Stadium | Tampa | 38.4[^1] | 95.9[^1] | Pepsi[^3] |
| 2022 | Los Angeles Rams | SoFi Stadium | Inglewood | 37.9[^1] | 101.5[^1] | Apple Music[^4] |
| 2023 | Kansas City Chiefs | State Farm Stadium | Glendale | 40.7[^1] | 115.1[^1] | Apple Music[^2] |
| 2024 | Kansas City Chiefs | Allegiant Stadium | Las Vegas | 43.5[^1] | 123.7[^1] | Apple Music[^4] |
| 2025 | Philadelphia Eagles | Caesars Superdome | New Orleans | 41.7[^1] | 127.7[^1] | Apple Music[^4] |

Sources:

- Champions, host stadium, host city: FOX Sports[^5]
- Nielsen HHLD rating \& viewership: Nielsen[^1]
- Half-time show sponsors history: Sporting News, Reuters[^2][^4]
<span style="display:none">[^10][^6][^7][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://www.nielsen.com/news-center/2025/super-bowl-lix-makes-tv-history-with-over-127-million-viewers/

[^2]: https://www.sportingnews.com/us/nfl/news/apple-super-bowl-halftime-show-pepsi/samfwqw9lqfefztzpnbvld0v

[^3]: http://www.espn.com/nfl/superbowl/history/winners

[^4]: https://www.reuters.com/sports/nfl/super-bowl-2025-halftime-show-who-is-performing-who-is-sponsoring-how-watch-2025-02-03/

[^5]: https://www.foxsports.com/nfl-super-bowl-winners-and-results

[^6]: https://www.reuters.com/business/media-telecom/super-bowl-audience-sets-all-time-record-single-network-broadcast-2025-02-11/

[^7]: https://www.cnn.com/2022/09/23/media/nfl-super-bowl-halftime-show-sponsor-pepsi

[^8]: https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions

[^9]: https://en.wikipedia.org/wiki/Super_Bowl_television_ratings

[^10]: https://en.wikipedia.org/wiki/Super_Bowl



[The End of Response]

### Single-Row (One extracted item)

[The Start of Single-Row]

| Year | Champion | Host Stadium | Host City | Nielsen HHLD Rating | Viewership (million) | Half-time Show Sponsors |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 2018 | Philadelphia Eagles | U.S. Bank Stadium | Minneapolis | 43.1[^1] | 104.0[^1] | Pepsi[^3] |

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
