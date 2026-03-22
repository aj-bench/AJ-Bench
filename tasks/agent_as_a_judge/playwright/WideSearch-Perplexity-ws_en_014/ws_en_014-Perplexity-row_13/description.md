# Agent-as-a-Judge Task

You will verify the factual correctness of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

What are the world's busiest airports by passenger traffic? List the top ten busiest airports between 2020-2024 (including 2020 and 2024). Please provide official links to support your statement. I want to know about their rank, specific location (including city, district, road), total passengers (with precision to the person) and code(IATA/ICAO).

Please organize the results in one Markdown table with the following column names in order: 
Year, Airport, Rank, Location, Total Passengers, Code(IATA/ICAO)

[The End of Query]

### Response

[The Start of Response]

# World’s Busiest Airports by Passenger Traffic (2020–2024)

Below is a consolidated table of the top ten busiest airports worldwide for each year from 2020 through 2024. Rankings, precise passenger counts, and official sources are provided for each year.


| Year | Airport | Rank | Location | Total Passengers | Code (IATA/ICAO) |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 2020 | Guangzhou Baiyun International Airport | 1 | 8 Gaoxin South 2nd Road, Huangpu District, Guangzhou, Guangdong, China | 43 767 558[^1] | CAN/ZGGG |
| 2020 | Hartsfield–Jackson Atlanta International Airport | 2 | 6000 N Terminal Pkwy, College Park, Georgia, USA | 42 918 685[^1] | ATL/KATL |
| 2020 | Chengdu Shuangliu International Airport | 3 | No. 12 Shuangliu Airport Road, Shuangliu District, Chengdu, Sichuan, China | 40 741 509[^1] | CTU/ZUUU |
| 2020 | Dallas/Fort Worth International Airport | 4 | 2400 Aviation Dr, DFW Airport, Texas, USA | 39 364 990[^1] | DFW/KDFW |
| 2020 | Shenzhen Bao’an International Airport | 5 | 69 Jichang 3rd Road, Bao’an District, Shenzhen, Guangdong, China | 37 916 054[^1] | SZX/ZGSZ |
| 2020 | Chongqing Jiangbei International Airport | 6 | No. 1 Airport, Yubei District, Chongqing, China | 34 937 789[^1] | CKG/ZUCK |
| 2020 | Beijing Capital International Airport | 7 | 3 Sanjing Rd, Chaoyang, Beijing, China | 34 513 827[^1] | PEK/ZBAA |
| 2020 | Denver International Airport | 8 | 8500 Peña Blvd, Denver, Colorado, USA | 33 741 129[^1] | DEN/KDEN |
| 2020 | Kunming Changshui International Airport | 9 | No. 222 Huaguan Rd, Guandu District, Kunming, Yunnan, China | 32 990 805[^1] | KMG/ZPPP |
| 2020 | Shanghai Hongqiao International Airport | 10 | 2550 North Caoxi Rd, Changning District, Shanghai, China | 31 165 641[^1] | SHA/ZSSS |
| 2021 | Hartsfield–Jackson Atlanta International Airport | 1 | 6000 N Terminal Pkwy, College Park, Georgia, USA | 75 704 760[^2] | ATL/KATL |
| 2021 | Dallas/Fort Worth International Airport | 2 | 2400 Aviation Dr, DFW Airport, Texas, USA | 62 465 756[^2] | DFW/KDFW |
| 2021 | Denver International Airport | 3 | 8500 Peña Blvd, Denver, Colorado, USA | 58 828 552[^2] | DEN/KDEN |
| 2021 | Chicago O’Hare International Airport | 4 | 10000 W O'Hare Ave, Chicago, Illinois, USA | 54 020 339[^2] | ORD/KORD |
| 2021 | Los Angeles International Airport | 5 | 1 World Way, Los Angeles, California, USA | 48 007 284[^2] | LAX/KLAX |
| 2021 | Charlotte Douglas International Airport | 6 | 5501 Josh Birmingham Pkwy, Charlotte, North Carolina, USA | 43 302 230[^2] | CLT/KCLT |
| 2021 | Orlando International Airport | 7 | 1 Jeff Fuqua Blvd, Orlando, Florida, USA | 40 351 068[^2] | MCO/KMCO |
| 2021 | Guangzhou Baiyun International Airport | 8 | 8 Gaoxin South 2nd Road, Huangpu District, Guangzhou, Guangdong, China | 40 259 401[^2] | CAN/ZGGG |
| 2021 | Chengdu Shuangliu International Airport | 9 | No. 12 Shuangliu Airport Road, Shuangliu District, Chengdu, Sichuan, China | 40 117 496[^2] | CTU/ZUUU |
| 2021 | Harry Reid International Airport | 10 | 5757 Wayne Newton Blvd, Paradise, Nevada, USA | 39 754 366[^2] | LAS/KLAS |
| 2022 | Hartsfield–Jackson Atlanta International Airport | 1 | 6000 N Terminal Pkwy, College Park, Georgia, USA | 93 699 630[^3] | ATL/KATL |
| 2022 | Dallas/Fort Worth International Airport | 2 | 2400 Aviation Dr, DFW Airport, Texas, USA | 73 362 946[^3] | DFW/KDFW |
| 2022 | Denver International Airport | 3 | 8500 Peña Blvd, Denver, Colorado, USA | 69 286 461[^3] | DEN/KDEN |
| 2022 | O’Hare International Airport | 4 | 10000 W O'Hare Ave, Chicago, Illinois, USA | 68 340 619[^3] | ORD/KORD |
| 2022 | Dubai International Airport | 5 | Dubai International Airport Road, Garhoud, Dubai, UAE | 66 069 981[^3] | DXB/OMDB |
| 2022 | Los Angeles International Airport | 6 | 1 World Way, Los Angeles, California, USA | 65 924 298[^3] | LAX/KLAX |
| 2022 | Istanbul Airport | 7 | Yeşilköy Mah., Atatürk Blv., Bakirköy, Istanbul, Turkey | 64 289 107[^3] | IST/LTBA |
| 2022 | Heathrow Airport | 8 | Greater London, Hillingdon, UK | 61 614 508[^3] | LHR/EGLL |
| 2022 | Indira Gandhi International Airport | 9 | New Delhi, Palam, Delhi, India | 59 490 074[^3] | DEL/VIDP |
| 2022 | Charles de Gaulle Airport | 10 | Roissy-en-France, Île-de-France, France | 57 474 033[^3] | CDG/LFPG |
| 2023 | Hartsfield–Jackson Atlanta International Airport | 1 | 6000 N Terminal Pkwy, College Park, Georgia, USA | 104 700 000[^4] | ATL/KATL |
| 2023 | Dubai International Airport | 2 | Dubai International Airport Road, Garhoud, Dubai, UAE | *Data not published* | DXB/OMDB |
| 2023 | Dallas/Fort Worth International Airport | 3 | 2400 Aviation Dr, DFW Airport, Texas, USA | *Data not published* | DFW/KDFW |
| 2023 | Denver International Airport | 4 | 8500 Peña Blvd, Denver, Colorado, USA | *Data not published* | DEN/KDEN |
| 2023 | O’Hare International Airport | 5 | 10000 W O'Hare Ave, Chicago, Illinois, USA | *Data not published* | ORD/KORD |
| 2023 | Los Angeles International Airport | 6 | 1 World Way, Los Angeles, California, USA | *Data not published* | LAX/KLAX |
| 2023 | Istanbul Airport | 7 | Yeşilköy Mah., Atatürk Blv., Bakirköy, Istanbul, Turkey | *Data not published* | IST/LTBA |
| 2023 | Indira Gandhi International Airport | 8 | New Delhi, Palam, Delhi, India | *Data not published* | DEL/VIDP |
| 2023 | Guangzhou Baiyun International Airport | 9 | 8 Gaoxin South 2nd Road, Huangpu District, Guangzhou, Guangdong, China | *Data not published* | CAN/ZGGG |
| 2023 | Shanghai Pudong International Airport | 10 | 1100 Pudong Airport Blvd, Pudong, Shanghai, China | *Data not published* | PVG/ZSPD |
| 2024 | Hartsfield–Jackson Atlanta International Airport | 1 | 6000 N Terminal Pkwy, College Park, Georgia, USA | 108 100 000[^5] | ATL/KATL |
| 2024 | Dubai International Airport | 2 | Dubai International Airport Road, Garhoud, Dubai, UAE | 92 300 000[^5] | DXB/OMDB |
| 2024 | Dallas/Fort Worth International Airport | 3 | 2400 Aviation Dr, DFW Airport, Texas, USA | 87 800 000[^5] | DFW/KDFW |
| 2024 | Tokyo Haneda Airport | 4 | 3-3 Hanedakuko, Ota City, Tokyo, Japan | 85 900 000[^5] | HND/RJTT |
| 2024 | London Heathrow Airport | 5 | Hillingdon, Greater London, UK | 78 900 000[^5] | LHR/EGLL |
| 2024 | Denver International Airport | 6 | 8500 Peña Blvd, Denver, Colorado, USA | 82 400 000[^5] | DEN/KDEN |
| 2024 | Istanbul Airport | 7 | Yeşilköy Mah., Atatürk Blv., Bakirköy, Istanbul, Turkey | 80 100 000[^5] | IST/LTBA |
| 2024 | O’Hare International Airport | 8 | 10000 W O'Hare Ave, Chicago, Illinois, USA | 80 000 000[^5] | ORD/KORD |
| 2024 | Indira Gandhi International Airport | 9 | New Delhi, Palam, Delhi, India | 77 800 000[^5] | DEL/VIDP |
| 2024 | Shanghai Pudong International Airport | 10 | 1100 Pudong Airport Blvd, Pudong, Shanghai, China | 76 800 000[^5] | PVG/ZSPD |

**Sources:**
2020 data: ACI World “COVID-19’s impact on world’s busiest airports” (22 Apr 2021)[^1]
2021 data: Simple Flying “The World’s 10 Busiest Airports In 2021” (10 Apr 2022)[^2]
2022 data: Wikipedia “List of busiest airports by passenger traffic” (accessed 2025)[^3]
2023 data: ACI-NA “2023 North American Airport Traffic Summary” (5 Aug 2024)[^4]
2024 data: CNN “Air ‘traffic is back’: These are the world’s 10 busiest airports” (14 Apr 2025)[^5]
<span style="display:none">[^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^30][^31][^6][^7][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://aci.aero/2021/04/22/aci-world-data-reveals-covid-19s-impact-on-worlds-busiest-airports/

[^2]: https://simpleflying.com/worlds-busiest-airports-2021/

[^3]: https://en.wikipedia.org/wiki/List_of_busiest_airports_by_passenger_traffic

[^4]: https://airportscouncil.org/press_release/airports-council-releases-2023-north-american-airport-traffic-rankings/

[^5]: https://www.cnn.com/2025/04/14/travel/worlds-busiest-airports-passengers-2024

[^6]: https://airportindustry-news.com/aci-world-reveals-top-10-busiest-airports-in-2021/

[^7]: https://airportindustry-news.com/aci-reveals-worlds-busiest-airports-in-new-dataset/

[^8]: https://www.dutyfreedynamics.com/note/us-tops-ranking-busiest-airports-2021

[^9]: https://www.ttrweekly.com/site/2025/07/aci-ranks-the-worlds-busiest-airports/

[^10]: https://money-tourism.gr/en/aci-world-these-are-the-20-busiest-airports-in-the-world/

[^11]: https://www.aviacionline.com/worlds-busiest-airports-top-20-ranking-confirmed-by-aci

[^12]: https://airport-world.com/aci-data-confirms-top-20-busiest-airports-in-world/

[^13]: https://aci.aero/2022/07/25/final-data-released-top-20-busiest-airports-confirmed/

[^14]: https://airportscouncil.org/press_release/airports-council-releases-2021-north-america-airport-traffic-rankings/

[^15]: https://www.dw.com/en/covid-pandemic-reshuffles-list-of-busiest-airports/a-57286903

[^16]: https://www.stratosjets.com/blog/busiest-us-airports/

[^17]: https://www.oag.com/busiest-airports-world

[^18]: https://aci.aero/2024/07/16/top-20-busiest-airports-in-the-world-confirmed-by-aci-world/

[^19]: https://www.cnn.com/travel/article/worlds-busiest-airports-2020-coronavirus-pandemic

[^20]: https://www.reddit.com/r/aviation/comments/knu5zy/10_busiest_airports_of_2020/

[^21]: https://www.gigasheet.com/sample-data/list-of-busiest-airports-by-passenger-traffic

[^22]: https://facilitiesmanagementadvisor.com/maintenance-and-operations/u-s-dominates-list-of-worlds-top-10-busiest-airports/

[^23]: https://www.reddit.com/r/delta/comments/u24z5l/2021_busiest_airport_report/

[^24]: https://www.cnn.com/travel/article/worlds-busiest-airports-2021

[^25]: https://www.statista.com/statistics/185679/passengers-boarded-at-the-leading-25-us-airports/

[^26]: https://www.oag.com/busiest-airports-world-2023

[^27]: https://www.cnbc.com/2025/07/08/here-are-the-top-15-busiest-airports-in-the-world.html

[^28]: https://centreforaviation.com/analysis/reports/worlds-busiest-passenger-and-cargo-airports-in-2023-a-deeper-dive-691536

[^29]: https://aci.aero/2025/07/08/worlds-busiest-airports-revealed-in-final-global-rankings/

[^30]: https://aci.aero/2025/04/14/the-busiest-airports-in-the-world-defy-global-uncertainty-and-hold-top-rankings/

[^31]: https://www.reddit.com/r/Infographics/comments/18vxssi/the_busiest_airports_in_2023/



[The End of Response]

### Single-Row (One extracted item)

[The Start of Single-Row]

| Year | Airport | Rank | Location | Total Passengers | Code (IATA/ICAO) |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 2021 | Denver International Airport | 3 | 8500 Peña Blvd, Denver, Colorado, USA | 58 828 552[^2] | DEN/KDEN |

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
