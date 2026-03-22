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

# Overview of Rankings

| Year | Airport | Rank | Location | Total Passengers | Code(IATA/ICAO) |
|------|---------|------|----------|-------------|----------|
| 2020 | Guangzhou Baiyun International Airport | 1 | Airport S Rd, Baiyun District, Guangzhou, Guangdong, China | 43,767,558 | CAN/ZGGG |
| 2020 | Hartsfield-Jackson Atlanta International Airport | 2 | 6000 N Terminal Pkwy, College Park, Atlanta, Georgia, USA | 42,918,685 | ATL/KATL |
| 2020 | Chengdu Shuangliu International Airport | 3 | Airport S Rd, Shuangliu District, Chengdu, Sichuan, China | 40,741,509 | CTU/ZUUU |
| 2020 | Dallas/Fort Worth International Airport | 4 | 2400 Aviation Dr, Grapevine, Dallas/Fort Worth, Texas, USA | 39,364,990 | DFW/KDFW |
| 2020 | Shenzhen Bao'an International Airport | 5 | Hangzhan 4th Rd, Bao'an District, Shenzhen, Guangdong, China | 37,916,054 | SZX/ZGSZ |
| 2020 | Chongqing Jiangbei International Airport | 6 | Lianglu Ave, Yubei District, Chongqing, China | 34,937,789 | CKG/ZUCK |
| 2020 | Beijing Capital International Airport | 7 | Capital Airport Rd, Shunyi District, Beijing, China | 34,513,827 | PEK/ZBAA |
| 2020 | Denver International Airport | 8 | 8500 Peña Blvd, Denver, Colorado, USA | 33,741,129 | DEN/KDEN |
| 2020 | Kunming Changshui International Airport | 9 | Changshui Ave, Guandu District, Kunming, Yunnan, China | 32,990,805 | KMG/ZPPP |
| 2020 | Shanghai Hongqiao International Airport | 10 | 2550 Hongqiao Rd, Minhang District, Shanghai, China | 31,165,641 | SHA/ZSSS |
| 2021 | Hartsfield-Jackson Atlanta International Airport | 1 | 6000 N Terminal Pkwy, College Park, Atlanta, Georgia, USA | 75,704,760 | ATL/KATL |
| 2021 | Dallas/Fort Worth International Airport | 2 | 2400 Aviation Dr, Grapevine, Dallas/Fort Worth, Texas, USA | 62,465,756 | DFW/KDFW |
| 2021 | Denver International Airport | 3 | 8500 Peña Blvd, Denver, Colorado, USA | 58,828,552 | DEN/KDEN |
| 2021 | Chicago O'Hare International Airport | 4 | 10000 W Balmoral Ave, O'Hare, Chicago, Illinois, USA | 54,020,399 | ORD/KORD |
| 2021 | Los Angeles International Airport | 5 | 1 World Way, Westchester, Los Angeles, California, USA | 48,007,284 | LAX/KLAX |
| 2021 | Charlotte Douglas International Airport | 6 | 5501 Josh Birmingham Pkwy, Charlotte, North Carolina, USA | 43,302,230 | CLT/KCLT |
| 2021 | Orlando International Airport | 7 | 1 Jeff Fuqua Blvd, Orlando, Florida, USA | 40,351,068 | MCO/KMCO |
| 2021 | Guangzhou Baiyun International Airport | 8 | Airport S Rd, Baiyun District, Guangzhou, Guangdong, China | 40,259,401 | CAN/ZGGG |
| 2021 | Chengdu Shuangliu International Airport | 9 | Airport S Rd, Shuangliu District, Chengdu, Sichuan, China | 40,117,496 | CTU/ZUUU |
| 2021 | Harry Reid International Airport | 10 | 5757 Wayne Newton Blvd, Paradise, Las Vegas, Nevada, USA | 39,754,366 | LAS/KLAS |
| 2022 | Hartsfield-Jackson Atlanta International Airport | 1 | 6000 N Terminal Pkwy, College Park, Atlanta, Georgia, USA | 93,699,630 | ATL/KATL |
| 2022 | Dallas/Fort Worth International Airport | 2 | 2400 Aviation Dr, Grapevine, Dallas/Fort Worth, Texas, USA | 73,362,946 | DFW/KDFW |
| 2022 | Denver International Airport | 3 | 8500 Peña Blvd, Denver, Colorado, USA | 69,286,461 | DEN/KDEN |
| 2022 | Chicago O'Hare International Airport | 4 | 10000 W Balmoral Ave, O'Hare, Chicago, Illinois, USA | 68,340,619 | ORD/KORD |
| 2022 | Dubai International Airport | 5 | Airport Rd, Al Garhoud, Dubai, United Arab Emirates | 66,069,981 | DXB/OMDB |
| 2022 | Los Angeles International Airport | 6 | 1 World Way, Westchester, Los Angeles, California, USA | 65,924,298 | LAX/KLAX |
| 2022 | Istanbul Airport | 7 | Tayakadın, Terminal Caddesi No:1, Arnavutköy, Istanbul, Turkey | 64,289,107 | IST/LTFM |
| 2022 | Heathrow Airport | 8 | Heathrow Airport, Longford TW6, Hillingdon, London, United Kingdom | 61,599,196 | LHR/EGLL |
| 2022 | Indira Gandhi International Airport | 9 | New Delhi, Delhi 110037, India | 59,490,074 | DEL/VIDP |
| 2022 | Paris Charles de Gaulle Airport | 10 | 95700 Roissy-en-France, France | 57,474,033 | CDG/LFPG |
| 2023 | Hartsfield-Jackson Atlanta International Airport | 1 | 6000 N Terminal Pkwy, College Park, Atlanta, Georgia, USA | 104,653,451 | ATL/KATL |
| 2023 | Dubai International Airport | 2 | Airport Rd, Al Garhoud, Dubai, United Arab Emirates | 86,994,365 | DXB/OMDB |
| 2023 | Dallas/Fort Worth International Airport | 3 | 2400 Aviation Dr, Grapevine, Dallas/Fort Worth, Texas, USA | 81,755,538 | DFW/KDFW |
| 2023 | Heathrow Airport | 4 | Heathrow Airport, Longford TW6, Hillingdon, London, United Kingdom | 79,183,364 | LHR/EGLL |
| 2023 | Tokyo Haneda Airport | 5 | 3 Chome-3-2 Hanedakuko, Ota City, Tokyo, Japan | 78,719,302 | HND/RJTT |
| 2023 | Denver International Airport | 6 | 8500 Peña Blvd, Denver, Colorado, USA | 77,837,636 | DEN/KDEN |
| 2023 | Istanbul Airport | 7 | Tayakadın, Terminal Caddesi No:1, Arnavutköy, Istanbul, Turkey | 76,236,980 | IST/LTFM |
| 2023 | Los Angeles International Airport | 8 | 1 World Way, Westchester, Los Angeles, California, USA | 75,050,651 | LAX/KLAX |
| 2023 | Chicago O'Hare International Airport | 9 | 10000 W Balmoral Ave, O'Hare, Chicago, Illinois, USA | 73,894,226 | ORD/KORD |
| 2023 | Indira Gandhi International Airport | 10 | New Delhi, Delhi 110037, India | 72,214,841 | DEL/VIDP |
| 2024 | Hartsfield-Jackson Atlanta International Airport | 1 | 6000 N Terminal Pkwy, College Park, Atlanta, Georgia, USA | 108,100,000 | ATL/KATL |
| 2024 | Dubai International Airport | 2 | Airport Rd, Al Garhoud, Dubai, United Arab Emirates | 92,300,000 | DXB/OMDB |
| 2024 | Dallas/Fort Worth International Airport | 3 | 2400 Aviation Dr, Grapevine, Dallas/Fort Worth, Texas, USA | 87,800,000 | DFW/KDFW |
| 2024 | Tokyo Haneda Airport | 4 | 3 Chome-3-2 Hanedakuko, Ota City, Tokyo, Japan | 85,900,000 | HND/RJTT |
| 2024 | Heathrow Airport | 5 | Heathrow Airport, Longford TW6, Hillingdon, London, United Kingdom | 83,900,000 | LHR/EGLL |
| 2024 | Denver International Airport | 6 | 8500 Peña Blvd, Denver, Colorado, USA | 82,400,000 | DEN/KDEN |
| 2024 | Istanbul Airport | 7 | Tayakadın, Terminal Caddesi No:1, Arnavutköy, Istanbul, Turkey | 80,100,000 | IST/LTFM |
| 2024 | Chicago O'Hare International Airport | 8 | 10000 W Balmoral Ave, O'Hare, Chicago, Illinois, USA | 80,000,000 | ORD/KORD |
| 2024 | Indira Gandhi International Airport | 9 | New Delhi, Delhi 110037, India | 77,800,000 | DEL/VIDP |
| 2024 | Shanghai Pudong International Airport | 10 | S1 Yingbin Expy, Pudong District, Shanghai, China | 76,800,000 | PVG/ZSPD |

## Supporting Sources
The data is primarily sourced from Airports Council International's annual reports, which provide authoritative rankings based on verified airport submissions. For detailed methodology and full datasets, refer to ACI's official publications.

---

The world's busiest airports by passenger traffic have undergone notable shifts between 2020 and 2024, reflecting the aviation industry's response to global events, economic recovery, and changing travel patterns. In 2020, the COVID-19 pandemic drastically reduced international travel, leading to a dominance of Chinese airports in the top rankings as domestic traffic in China recovered faster than elsewhere. Guangzhou Baiyun International Airport topped the list with 43,767,558 passengers, followed closely by Hartsfield-Jackson Atlanta, which saw its numbers drop to 42,918,685 due to restrictions on U.S. domestic and international flights. Other Chinese hubs like Chengdu Shuangliu (40,741,509 passengers) and Shenzhen Bao'an (37,916,054) filled the upper ranks, highlighting how regional lockdowns and travel policies influenced global rankings. U.S. airports like Dallas/Fort Worth (39,364,990) and Denver (33,741,129) still held strong positions thanks to resilient domestic networks.

By 2021, as vaccinations rolled out and restrictions eased in the U.S., American airports reclaimed the majority of the top spots. Hartsfield-Jackson Atlanta surged back to first with 75,704,760 passengers, nearly doubling its 2020 figure, driven by Delta Air Lines' hub operations. Dallas/Fort Worth (62,465,756) and Denver (58,828,552) followed, benefiting from pent-up domestic demand. Chinese airports like Guangzhou Baiyun (40,259,401) and Chengdu Shuangliu (40,117,496) remained in the top 10, but the gap widened as U.S. traffic rebounded faster. Airports like Charlotte Douglas (43,302,230) and Orlando (40,351,068) entered the list, underscoring the role of leisure travel in the early recovery phase.

In 2022, the resumption of international travel marked a key milestone, with global passenger traffic reaching about 7 billion, or 73.8% of 2019 levels. Hartsfield-Jackson Atlanta maintained its lead with 93,699,630 passengers, approaching pre-pandemic volumes. The top four U.S. airports—Dallas/Fort Worth (73,362,946), Denver (69,286,461), and Chicago O'Hare (68,340,619)—dominated, but international hubs like Dubai (66,069,981) and Istanbul (64,289,107) re-entered the top 10, reflecting border reopenings in the Middle East and Europe. London Heathrow (61,599,196), Delhi (59,490,074), and Paris Charles de Gaulle (57,474,033) also returned, signaling a balanced recovery between domestic and international markets. This year saw the biggest jumps for European airports, such as Heathrow rising from 54th in 2021.

The year 2023 saw global passenger traffic climb to 8.5 billion, nearing 94% of 2019 levels, fueled by the full reopening of China and strong international demand. Hartsfield-Jackson Atlanta hit 104,653,451 passengers, surpassing its 2019 record. Dubai (86,994,365) leaped to second, overtaking Dallas/Fort Worth (81,755,538), as it became the leading international hub. London Heathrow (79,183,364) and Tokyo Haneda (78,719,302) followed, with Haneda jumping from 16th in 2022 due to Japan's border reopening. Denver (77,837,636), Istanbul (76,236,980), Los Angeles (75,050,651), Chicago O'Hare (73,894,226), and Delhi (72,214,841) rounded out the list, showing a mix of domestic strength in the U.S. and growing international connectivity in Asia and Europe. The rise of Dubai and Istanbul highlighted the increasing importance of Middle Eastern and transcontinental routes.

Finally, in 2024, global traffic exceeded 9.4 billion passengers, 2.7% above 2019, confirming a full recovery. Hartsfield-Jackson Atlanta led with 108,100,000 passengers, followed by Dubai (92,300,000) and Dallas/Fort Worth (87,800,000). Tokyo Haneda (85,900,000) and London Heathrow (83,900,000) maintained strong positions, while Denver (82,400,000), Istanbul (80,100,000), Chicago O'Hare (80,000,000), Delhi (77,800,000), and Shanghai Pudong (76,800,000) completed the top 10. Shanghai Pudong's rise from 21st in 2023 was notable, driven by China's visa easing and flight expansions. This year underscored Asia's accelerating recovery and the continued dominance of U.S. hubs for domestic travel.

### Key Citations
- Airports Council International (2020 Rankings): https://aci.aero/2021/04/22/aci-world-data-reveals-covid-19s-impact-on-worlds-busiest-airports/
- Airports Council International (2021 Rankings): https://aci.aero/2022/04/11/the-top-10-busiest-airports-in-the-world-revealed/
- Airports Council International (2022 Rankings): https://aci.aero/2023/04/05/international-travel-returns-top-10-busiest-airports-in-the-world-revealed/
- Airports Council International (2023 Rankings): https://aci.aero/2024/04/14/top-10-busiest-airports-in-the-world-shift-with-the-rise-of-international-air-travel-demand/
- Airports Council International (2023 Final Confirmation): https://aci.aero/2024/07/16/top-20-busiest-airports-in-the-world-confirmed-by-aci-world/
- Airports Council International (2024 Rankings): https://aci.aero/2025/07/08/worlds-busiest-airports-revealed-in-final-global-rankings/

[The End of Response]

### Single-Row (One extracted item)

[The Start of Single-Row]

| Year | Airport | Rank | Location | Total Passengers | Code(IATA/ICAO) |
|------|---------|------|----------|-------------|----------|
| 2021 | Harry Reid International Airport | 10 | 5757 Wayne Newton Blvd, Paradise, Las Vegas, Nevada, USA | 39,754,366 | LAS/KLAS |

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
