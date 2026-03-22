# Agent-as-a-Judge Task

You will verify the factual correctness of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

I am doing research on public transportation in Sydney. I wanna know each Sydney train's line number, line name, total number of stations, and termini. Pay attention: each Sydney railway line, that has been put into use by May 31, 2025, is included. The total number of stations should reflect the status quo in Sydney as of May 2025. Please provide official links to support your statement.

Please organize the results in one Markdown table with the following columns:
Line Number, Line Name, Total Stations, Termini
Note: When compiling the total number of stations, variations in station count resulting from peak-hour additions or reductions are excluded.

[The End of Query]

### Response

[The Start of Response]

# Train Line Table

| Line Number | Line Name | Total Stations | Termini |
|-------------|-----------|---------------|---------|
| T1 | North Shore & Western Line | 36 | Berowra and Emu Plains or Richmond |
| T2 | Leppington & Inner West Line | 37 | City Circle and Parramatta or Leppington via Granville |
| T3 | Liverpool & Inner West Line | 25 | City Circle and Liverpool via Lidcombe and Regents Park |
| T4 | Eastern Suburbs & Illawarra Line | 33 | Bondi Junction and Waterfall or Cronulla via Central |
| T5 | Cumberland Line | 30 | Schofields and Leppington (limited services to Richmond) |
| T6 | Lidcombe & Bankstown Line | 6 | Bankstown and Lidcombe |
| T7 | Olympic Park Line | 2 | Lidcombe and Olympic Park (some services to Central) |
| T8 | Airport & South Line | 26 | City Circle and Macarthur via Revesby and Sydenham or Airport |
| T9 | Northern Line | 37 | Hornsby and Gordon via Strathfield and City |
| M1 | Metro North West & Bankstown Line | 21 | Tallawong and Sydenham |

## Line Details and History
- **T1 North Shore & Western Line**: This line combines the North Shore and Western routes, serving northern and western suburbs. It has 36 stations on its main path, but with branches, it serves more unique locations. The line's history dates back to the 1880s, with electrification in the 1920s. Termini include Berowra (north) and Emu Plains/Richmond (west), with services crossing the Harbour Bridge. Official map for counting stations: https://transportnsw.info/sydney-trains-network-map.

- **T2 Leppington & Inner West Line**: With 37 stations, this line serves the inner west and south-west, branching at Granville. It was formed in 2013 by merging previous services and extended to Leppington in 2015. The line uses the City Circle for CBD access. Termini are the City Circle and Leppington or Parramatta. The number of stations is confirmed from simplified educational sources.

- **T3 Liverpool & Inner West Line**: Adjusted in October 2024 to 25 stations after the Bankstown closure, this line runs via Lidcombe and Regents Park to Liverpool. It was previously the Bankstown Line but was reconfigured to maintain service to Liverpool. Termini are the City Circle and Liverpool. The count is based on post-2024 timetable changes described in Transport for NSW updates.

- **T4 Eastern Suburbs & Illawarra Line**: This 33-station line serves the eastern suburbs and Illawarra region, with branches to Waterfall and Cronulla. It was the first to be electrified in 1926 and includes the Eastern Suburbs underground section opened in 1979. Termini are Bondi Junction and Waterfall or Cronulla. Station count is derived from line descriptions and maps.

- **T5 Cumberland Line**: The 30-station line is a cross-suburban service linking western suburbs without going through the CBD. It was introduced in 1996 and extended in 2013. Termini are Schofields and Leppington, with limited services to Richmond. The number is from Wikipedia extraction.

- **T6 Lidcombe & Bankstown Line**: Following the 2024 closure, this became a 6-station shuttle on the remaining Bankstown branch. It was in operation as of May 2025, providing local connectivity during the metro conversion. Termini are Lidcombe and Bankstown. The line's status and count are confirmed from post-closure updates.

- **T7 Olympic Park Line**: A 2-station shuttle serving the Olympic Park precinct, with some services extending to Central. It was created for the 2000 Olympics. Termini are Lidcombe and Olympic Park. The count is from Wikipedia.

- **T8 Airport & South Line**: This 26-station line connects the CBD to the airport and south-western suburbs, using the Airport Link tunnel opened in 2000. It was split from T2 in 2017. Termini are the City Circle and Macarthur. Station count is based on route descriptions.

- **T9 Northern Line**: With 37 stations, this line serves the northern suburbs via the Main Suburban and North Shore lines. It was separated from T1 in 2019, restoring a pre-2009 route. Termini are Hornsby and Gordon. The count is from the station table on Wikipedia.

- **M1 Metro North West & Bankstown Line**: The 21-station metro line is driverless and underground in parts, extending from the 2019 Northwest section to Sydenham in 2024. The Bankstown extension was not complete by May 2025 (scheduled for 2026). Termini are Tallawong and Sydenham. Official interactive map for confirmation: https://www.sydneymetro.info/map/sydney-metro-interactive-train-map.

### Key Citations
- Transport for NSW Sydney Trains Network Map: https://transportnsw.info/sydney-trains-network-map
- Sydney Metro Interactive Train Map: https://www.sydneymetro.info/map/sydney-metro-interactive-train-map
- Sydney Trains Wikipedia: https://en.wikipedia.org/wiki/Sydney_Trains
- Sydney Metro Wikipedia: https://en.wikipedia.org/wiki/Sydney_Metro
- Bankstown Line Closure Update: https://www.sydneymetro.info/article/update-metro-conversion-t3-bankstown-line
- Rail Service Improvement Program: https://www.transport.nsw.gov.au/projects/programs/rail-service-improvement-program
- Sydney Metro City Opening: https://www.nsw.gov.au/media-releases/sydney-metro-city-to-open-on-monday-19-august
- Network Patronage Data: https://en.wikipedia.org/wiki/Sydney_Trains (2024-25 figures)
- Sydney Metro Map and Stations: https://www.timeout.com/sydney/news/sydney-metro-map-where-does-sydneys-new-super-fast-train-line-go-081924
- Sydney Metro Information: https://themetrorailguy.com/metro-rail-systems/sydney-metro-information-route-map-fare-prices-pass-hours-timings/

[The End of Response]

### Single-Row (One extracted item)

[The Start of Single-Row]

| Line Number | Line Name | Total Stations | Termini |
|-------------|-----------|---------------|---------|
| T3 | Liverpool & Inner West Line | 25 | City Circle and Liverpool via Lidcombe and Regents Park |

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
