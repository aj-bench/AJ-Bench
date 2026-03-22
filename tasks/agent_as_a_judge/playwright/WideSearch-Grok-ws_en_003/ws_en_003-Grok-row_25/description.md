# Agent-as-a-Judge Task

You will verify the factual correctness of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Could you help compile a detailed dataset of Eileen Gu's competitive achievements in freestyle skiing from Jan, 2015 to Jan 31st 2025, including the following information: event dates (year and month), specific event names (e.g., Winter Olympic Games, FIS Freestyle Ski World Championships, FIS Freestyle Ski World Cup stops, Winter Youth Olympic Games, X Games), event levels (e.g., Olympic, World Championship, World Cup, Youth Olympic, invitational, etc.), disciplines (women's big air, women's slopestyle, women's halfpipe, etc.), and results (e.g., gold medal, the 4th, etc.), and the top 3 players? By the way, as for competitions, only official matches should be counted, preliminary qualifiers should not be included. Please also provide a link corresponding to each competition result as evidence for your statement.

[The End of Query]

### Response

[The Start of Response]

| Date (Year-Month) | Event Name | Level | Discipline | Result | Top 3 Players | Link |
|-------------------|------------|-------|------------|--------|---------------|------|
| 2019-01 | FIS Freestyle Ski World Cup - Seiser Alm | World Cup | Women's Slopestyle | 1st (Gold) | 1. Eileen Gu (USA), 2. Sarah Hoefflin (SUI), 3. Jennie-Lee Burmansson (SWE) | https://www.fis-ski.com/DB/general/results.html?sectorcode=FS&raceid=10960  |
| 2019-03 | FIS Freestyle Ski World Cup - Mammoth Mountain | World Cup | Women's Slopestyle | 3rd (Bronze) | Top 3 unavailable | https://www.fis-ski.com/DB/general/results.html?sectorcode=FS&raceid=11002 |
| 2019-09 | FIS Freestyle Ski World Cup - Cardrona | World Cup | Women's Slopestyle | 1st (Gold) | Top 3 unavailable | https://www.redbull.com/us-en/athlete/eileen-gu  |
| 2020-01 | Winter Youth Olympic Games - Lausanne | Youth Olympic | Women's Halfpipe | 1st (Gold) | 1. Gu Ailing (CHN) - 93.00, 2. Li Fanghui (CHN) - 85.66, 3. Hanna Faulhaber (USA) - 77.33 | https://en.wikipedia.org/wiki/Freestyle_skiing_at_the_2020_Winter_Youth_Olympics_%E2%80%93_Girls%27_halfpipe  |
| 2020-01 | Winter Youth Olympic Games - Lausanne | Youth Olympic | Women's Slopestyle | 2nd (Silver) | 1. Kelly Sildaru (EST) - 93.75, 2. Gu Ailing (CHN) - 93.25, 3. Jennie-Lee Burmansson (SWE) - 90.00 | https://en.wikipedia.org/wiki/Freestyle_skiing_at_the_2020_Winter_Youth_Olympics_%E2%80%93_Girls%27_slopestyle  |
| 2020-01 | Winter Youth Olympic Games - Lausanne | Youth Olympic | Women's Big Air | 1st (Gold) | 1. Gu Ailing (CHN) - 171.25, 2. Kirsty Muir (GBR) - 170.00, 3. Jennie-Lee Burmansson (SWE) - 151.75 | https://en.wikipedia.org/wiki/Freestyle_skiing_at_the_2020_Winter_Youth_Olympics_%E2%80%93_Girls%27_big_air  |
| 2021-01 | X Games Aspen | Invitational | Women's Superpipe (Halfpipe) | 1st (Gold) | 1. Eileen Gu (CHN), 2. Rachael Karker (CAN), 3. Zoe Atkin (GBR) | https://www.xgames.com/events/x-games-aspen-2021/competitions/womens-ski-superpipe  |
| 2021-01 | X Games Aspen | Invitational | Women's Slopestyle | 1st (Gold) | 1. Eileen Gu (CHN), 2. Isabel Atkin (GBR), 3. Megan Oldham (CAN) | https://www.downdays.eu/events/report/x-games-2021-womens-ski-slopestyle-results-recap/  |
| 2021-01 | X Games Aspen | Invitational | Women's Big Air | 3rd (Bronze) | 1. Mathilde Gremaud (SUI) - 91, 2. Megan Oldham (CAN) - 77, 3. Eileen Gu (CHN) - 73 | https://espnpressroom.com/us/press-releases/2021/01/x-games-aspen-2021-day-one-news-and-results/  |
| 2021-03 | FIS Freestyle Ski World Championships - Aspen | World Championship | Women's Halfpipe | 1st (Gold) | 1. Gu Ailing (CHN) - 93.00, 2. Rachael Karker (CAN) - 91.75, 3. Zoe Atkin (GBR) - 90.50 | https://en.wikipedia.org/wiki/FIS_Freestyle_Ski_and_Snowboarding_World_Championships_2021_%E2%80%93_Women%27s_ski_halfpipe  |
| 2021-03 | FIS Freestyle Ski World Championships - Aspen | World Championship | Women's Slopestyle | 1st (Gold) | 1. Gu Ailing (CHN) - 84.23, 2. Mathilde Gremaud (SUI) - 77.15, 3. Megan Oldham (CAN) - 76.18 | https://en.wikipedia.org/wiki/FIS_Freestyle_Ski_and_Snowboarding_World_Championships_2021_%E2%80%93_Women%27s_ski_slopestyle  |
| 2021-03 | FIS Freestyle Ski World Championships - Aspen | World Championship | Women's Big Air | 3rd (Bronze) | 1. Anastasia Tatalina (RUS) - 184.50, 2. Lana Prusakova (RUS) - 165.50, 3. Gu Ailing (CHN) - 161.50 | https://en.wikipedia.org/wiki/FIS_Freestyle_Ski_and_Snowboarding_World_Championships_2021_%E2%80%93_Women%27s_ski_big_air  |
| 2021-03 | FIS Freestyle Ski World Cup - Aspen | World Cup | Women's Halfpipe | 7th | Top 3 unavailable | https://www.fis-ski.com/DB/general/results.html?sectorcode=FS&raceid=12206 |
| 2021-03 | FIS Freestyle Ski World Cup - Aspen | World Cup | Women's Slopestyle | 4th | Top 3 unavailable | https://www.fis-ski.com/DB/general/results.html?sectorcode=FS&raceid=12205 |
| 2021-12 | FIS Freestyle Ski World Cup - Copper Mountain | World Cup | Women's Halfpipe | 1st (Gold) | 1. Eileen Gu (CHN), 2. Zoe Atkin (GBR), 3. Rachael Karker (CAN) | https://www.redbull.com/us-en/fis-world-cup-copper-mountain-report-eileen-gu-wins  |
| 2021-12 | FIS Freestyle Ski World Cup - Steamboat | World Cup | Women's Big Air | 1st (Gold) | Top 3 unavailable | https://www.fis-ski.com/DB/general/results.html?sectorcode=FS&raceid=12468 |
| 2021-12 | FIS Freestyle Ski World Cup - Calgary | World Cup | Women's Halfpipe | 1st (Gold) | Top 3 unavailable | https://www.fis-ski.com/DB/general/results.html?sectorcode=FS&raceid=12471 |
| 2022-01 | FIS Freestyle Ski World Cup - Calgary | World Cup | Women's Halfpipe | 1st (Gold) | Top 3 unavailable | https://www.fis-ski.com/DB/general/results.html?sectorcode=FS&raceid=12472 |
| 2022-01 | FIS Freestyle Ski World Cup - Mammoth Mountain | World Cup | Women's Halfpipe | 1st (Gold) | Top 3 unavailable | https://www.fis-ski.com/DB/general/results.html?sectorcode=FS&raceid=12474 |
| 2022-01 | FIS Freestyle Ski World Cup - Mammoth Mountain | World Cup | Women's Slopestyle | 2nd (Silver) | Top 3 unavailable | https://www.fis-ski.com/DB/general/results.html?sectorcode=FS&raceid=12473 |
| 2022-02 | Winter Olympic Games - Beijing | Olympic | Women's Big Air | 1st (Gold) | 1. Eileen Gu (CHN) - 188.25, 2. Tess Ledeux (FRA) - 187.50, 3. Mathilde Gremaud (SUI) - 182.50 | https://en.wikipedia.org/wiki/Freestyle_skiing_at_the_2022_Winter_Olympics_%E2%80%93_Women%27s_big_air  |
| 2022-02 | Winter Olympic Games - Beijing | Olympic | Women's Slopestyle | 2nd (Silver) | 1. Mathilde Gremaud (SUI) - 86.56, 2. Eileen Gu (CHN) - 86.23, 3. Kelly Sildaru (EST) - 82.06 | https://en.wikipedia.org/wiki/Freestyle_skiing_at_the_2022_Winter_Olympics_%E2%80%93_Women%27s_slopestyle  |
| 2022-02 | Winter Olympic Games - Beijing | Olympic | Women's Halfpipe | 1st (Gold) | 1. Eileen Gu (CHN) - 95.25, 2. Cassie Sharpe (CAN) - 90.75, 3. Rachael Karker (CAN) - 87.75 | https://en.wikipedia.org/wiki/Freestyle_skiing_at_the_2022_Winter_Olympics_%E2%80%93_Women%27s_halfpipe  |
| 2023-01 | FIS Freestyle Ski World Cup - Calgary | World Cup | Women's Halfpipe | 1st (Gold) | Top 3 unavailable | https://www.fis-ski.com/DB/general/results.html?sectorcode=FS&raceid=13036 |
| 2023-01 | FIS Freestyle Ski World Cup - Calgary | World Cup | Women's Halfpipe | 1st (Gold) | Top 3 unavailable | https://www.fis-ski.com/DB/general/results.html?sectorcode=FS&raceid=13037 |
| 2023-12 | FIS Freestyle Ski World Cup - Secret Garden | World Cup | Women's Halfpipe | 1st (Gold) | 1. Eileen Gu (CHN), 2. Amy Fraser (CAN), 3. Zoe Atkin (GBR) | https://www.olympics.com/en/news/eileen-gu-wins-secret-garden-halfpipe-nick-goepper-results  |
| 2023-12 | FIS Freestyle Ski World Cup - Copper Mountain | World Cup | Women's Halfpipe | 1st (Gold) | 1. Eileen Gu (CHN), 2. Zoe Atkin (GBR), 3. Svea Irving (USA) | https://www.olympics.com/en/news/eileen-gu-continues-perfect-start-halfpipe-season-copper-results  |
| 2024-01 | FIS Freestyle Ski World Cup - Laax | World Cup | Women's Slopestyle | 2nd (Silver) | 1. Mathilde Gremaud (SUI), 2. Eileen Gu (CHN), 3. Tess Ledeux (FRA) | https://www.fis-ski.com/DB/general/results.html?sectorcode=FS&raceid=13400 |
| 2024-01 | X Games Aspen | Invitational | Women's Superpipe (Halfpipe) | 1st (Gold) | 1. Eileen Gu (CHN) - 95.66, 2. Zoe Atkin (USA) - 90.66, 3. Amy Fraser (CAN) - 90.00 | https://www.xgames.com/events/x-games-aspen-2024/competitions/womens-ski-superpipe  |
| 2024-02 | FIS Freestyle Ski World Cup - Mammoth Mountain | World Cup | Women's Halfpipe | 2nd (Silver) | Top 3 unavailable | https://www.fis-ski.com/DB/general/results.html?sectorcode=FS&raceid=13402 |
| 2024-02 | FIS Freestyle Ski World Cup - Calgary | World Cup | Women's Halfpipe | 1st (Gold) | Top 3 unavailable | https://www.fis-ski.com/DB/general/results.html?sectorcode=FS&raceid=13404 |
| 2024-02 | FIS Freestyle Ski World Cup - Calgary | World Cup | Women's Halfpipe | 1st (Gold) | Top 3 unavailable | https://www.fis-ski.com/DB/general/results.html?sectorcode=FS&raceid=13405 |
| 2024-09 | FIS Freestyle Ski World Cup - Cardrona | World Cup | Women's Halfpipe | 1st (Gold) | 1. Eileen Gu (CHN) - 96.00, 2. Zoe Atkin (GBR), 3. Svea Irving (USA) | https://www.olympics.com/en/news/olympian-eileen-gu-wins-record-15th-freeski-world-cup  |
| 2024-12 | FIS Freestyle Ski World Cup - Secret Garden | World Cup | Women's Halfpipe | 1st (Gold) | 1. Eileen Gu (CHN), 2. Zoe Atkin (GBR), 3. Amy Fraser (CAN) | https://snowbrains.com/eileen-gu-snags-remarkable-halfpipe-victory-at-fis-freeski-world-cup-in-secret-garden-china/  |
| 2024-12 | FIS Freestyle Ski World Cup - Copper Mountain | World Cup | Women's Halfpipe | 1st (Gold) | 1. Eileen Gu (CHN) - 90.50, 2. Zoe Atkin (GBR), 3. Amy Fraser (CAN) | https://www.globaltimes.cn/page/202412/1325574.shtml  |
| 2025-01 | FIS Freestyle Ski World Cup - Laax | World Cup | Women's Slopestyle | 1st (Gold) | 1. Eileen Gu (CHN) - 81.22, 2. Tess Ledeux (FRA), 3. Mathilde Gremaud (SUI) | https://www.olympics.com/en/news/dnp-freeski-slopestyle-world-cup-eileen-gu-wins-laax  |

**Key Citations:**
- [FIS Athlete Biography - Eileen Gu](https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=fs&competitorid=226193&type=result) 
- [Eileen Gu - Wikipedia](https://en.wikipedia.org/wiki/Eileen_Gu) 
- [Olympics.com - Eileen Gu News](https://www.olympics.com/en/athletes/gu-ailing-eileen) 
- [Red Bull Athlete Profile - Eileen Gu](https://www.redbull.com/us-en/athlete/eileen-gu) 
- [X Games Past Results](https://www.xgames.com/past-results) 
- [FIS Freeski World Cup Wins Record](https://www.freeskier.com/eileen-gu-take-halfpipe-gold-sets-record-for-most-fis-freeski-world-cup-wins-at-winter-games-new-zealand) 
- [Global Times - Gu Ailing Wins](https://www.globaltimes.cn/page/202412/1325574.shtml) 
- [Downdays - X Games 2021 Recap](https://www.downdays.eu/events/report/x-games-2021-womens-ski-slopestyle-results-recap/) 
- [ESPN Press Room - X Games 2021 Day One](https://espnpressroom.com/us/press-releases/2021/01/x-games-aspen-2021-day-one-news-and-results/) 
- [X Games Aspen 2024 Results](https://www.olympics.com/en/news/winter-x-games-aspen-2024-all-results-and-scores-complete-list)

[The End of Response]

### Single-Row (One extracted item)

[The Start of Single-Row]

| Date (Year-Month) | Event Name | Level | Discipline | Result | Top 3 Players | Link |
|-------------------|------------|-------|------------|--------|---------------|------|
| 2023-01 | FIS Freestyle Ski World Cup - Calgary | World Cup | Women's Halfpipe | 1st (Gold) | Top 3 unavailable | https://www.fis-ski.com/DB/general/results.html?sectorcode=FS&raceid=13037 |

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
