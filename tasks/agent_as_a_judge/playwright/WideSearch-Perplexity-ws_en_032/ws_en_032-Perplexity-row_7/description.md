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

# Sydney Train Lines Overview as of May 31, 2025

The Sydney Trains network comprises **nine** suburban lines, each identified by a number (T1–T9). Below is a summary of each line’s number, official name, total number of stations in regular service (excluding peak-hour variations), and its termini.


| Line Number | Line Name | Total Stations | Termini |
| :-- | :-- | --: | :-- |
| T1 | North Shore \& Western | 49 | Berowra ↔ Emu Plains / Richmond |
| T2 | Leppington \& Inner West | 43 | City Circle ↔ Leppington / Parramatta |
| T3 | Liverpool \& Inner West | 30 | City Circle ↔ Liverpool |
| T4 | Eastern Suburbs \& Illawarra | 34 | Bondi Junction ↔ Waterfall / Cronulla |
| T5 | Cumberland | 18 | Schofields ↔ Leppington (limited services to Richmond) |
| T6 | Lidcombe \& Bankstown | 22 | Lidcombe ↔ Bankstown |
| T7 | Olympic Park | 4 | Lidcombe ↔ Olympic Park |
| T8 | Airport \& South | 27 | City Circle ↔ Macarthur / Central (peak via Sydenham or Airport) |
| T9 | Northern | 21 | Hornsby ↔ Gordon (via Strathfield \& City) |

**Sources:**

- Sydney Trains official route details for T1–T9 lines
    - T1: transportnsw.info/routes/details/sydney-trains-network/t1/020t1
    - T2: transportnsw.info/routes/details/sydney-trains-network/t2/020t2
    - T3: transportnsw.info/routes/details/sydney-trains-network/t3/020t3
    - T4–T9: Sydney Trains network map and line list, Wikipedia[^1]
<span style="display:none">[^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^2][^20][^21][^22][^23][^24][^25][^3][^4][^5][^6][^7][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://en.wikipedia.org/wiki/Sydney_Trains

[^2]: https://en.wikipedia.org/wiki/List_of_Sydney_Trains_railway_stations

[^3]: https://en.wikipedia.org/wiki/Main_Western_railway_line,_New_South_Wales

[^4]: https://www.youtube.com/watch?v=MFNWkWJGBUA

[^5]: https://en.wikipedia.org/wiki/North_Shore_railway_line

[^6]: https://www.reddit.com/r/TransitDiagrams/comments/1gckpk3/oc_map_of_sydneys_train_metro_and_light_rail/

[^7]: https://www.barbershop.org.au/files/sydney-trains-network-map.pdf

[^8]: https://www.nswrail.net/lines/show.php?name=NSW%3Anorth_shore

[^9]: https://nswtrains.fandom.com/wiki/List_of_Sydney_railway_stations

[^10]: https://nswtrains.fandom.com/wiki/List_of_Sydney_suburban_railway_lines

[^11]: https://forums.dovetailgames.com/threads/dovetail-we-need-this-t1-north-shore-western-line.87436/

[^12]: https://forums.dovetailgames.com/threads/inner-west-leppington-line-t2-2018.75428/

[^13]: https://en.wikipedia.org/wiki/Liverpool_\&_Inner_West_Line

[^14]: https://en.wikipedia.org/wiki/North_Shore_\&_Western_Line

[^15]: https://en.wikipedia.org/wiki/Leppington_\&_Inner_West_Line

[^16]: https://moovitapp.com/index/en-gb/public_transportation-line-t3-Sydney-442-858486-511500-6

[^17]: https://kids.kiddle.co/North_Shore_\&_Western_Line

[^18]: https://moovitapp.com/index/en-gb/public_transportation-line-t2-Sydney-442-858486-667609-11

[^19]: https://moovitapp.com/index/en-gb/public_transportation-line-t3-Sydney-442-858486-227305306-8

[^20]: https://transportnsw.info/routes/details/sydney-trains-network/t1/020t1

[^21]: https://www.transsee.ca/stoplist?a=sydneytrains\&r=T2

[^22]: https://www.savet3.org/post/nsw-government-refuses-to-run-trains-to-central-and-liverpool-from-bankstown

[^23]: https://transportnsw.info/routes/details/sydney-trains-network/t2/020t2

[^24]: https://transportnsw.info/routes/details/sydney-trains-network/t3/020t3

[^25]: https://restoreinnerwestline.org.au/restoreinnerwestline/



[The End of Response]

### Single-Row (One extracted item)

[The Start of Single-Row]

| Line Number | Line Name | Total Stations | Termini |
| :-- | :-- | --: | :-- |
| T7 | Olympic Park | 4 | Lidcombe ↔ Olympic Park |

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
