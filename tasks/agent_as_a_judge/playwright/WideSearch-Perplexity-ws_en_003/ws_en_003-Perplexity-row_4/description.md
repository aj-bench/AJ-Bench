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

|  Index  | Date       | Event_Name                                               | Event_Level            | Discipline         | Result             | Top_3_Athletes                                                        | Competition_Link                                                                                                                         | Year_Month   |
|---:|:-----------|:---------------------------------------------------------|:-----------------------|:-------------------|:-------------------|:----------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|:-------------|
|  0 | 2019-01-12 | FIS Freestyle Ski World Cup - Font Romeu                 | World Cup              | Women's Slopestyle | Silver Medal (2nd) | 1. Sarah Hoefflin (SUI), 2. Eileen Gu (USA), 3. Giulia Tanno (SUI)    | https://www.nbcolympics.com/videos/2019-font-romeu-eileen-gu-reaches-first-world-cup-podium                                              | 2019-01      |
|  1 | 2019-01-27 | FIS Freestyle Ski World Cup - Seiser Alm                 | World Cup              | Women's Slopestyle | Gold Medal (1st)   | 1. Eileen Gu (USA), 2. Julia Krass (CAN), 3. Megan Oldham (USA)       | https://www.thesportsexaminer.com/freestyle-skiing-eileen-gu-15-takes-world-cup-slopestyle-in-seiser-alm/                                | 2019-01      |
|  2 | 2019-09-07 | FIS Freestyle Ski World Cup - Cardrona                   | World Cup              | Women's Halfpipe   | Silver Medal (2nd) | 1. Zhang Kexin (CHN), 2. Eileen Gu (CHN), 3. Cassie Sharpe (CAN)      | https://en.wikipedia.org/wiki/Eileen_Gu                                                                                                  | 2019-09      |
|  3 | 2020-01-18 | Winter Youth Olympic Games Lausanne 2020                 | Youth Olympic          | Women's Slopestyle | Silver Medal (2nd) | 1. Mathilde Gremaud (SUI), 2. Eileen Gu (CHN), 3. Megan Oldham (CAN)  | https://en.wikipedia.org/wiki/China_at_the_2020_Winter_Youth_Olympics                                                                    | 2020-01      |
|  4 | 2020-01-20 | Winter Youth Olympic Games Lausanne 2020                 | Youth Olympic          | Women's Halfpipe   | Gold Medal (1st)   | 1. Eileen Gu (CHN), 2. Li Fanghui (CHN), 3. Hanna Faulhaber (USA)     | https://news.cgtn.com/news/2020-01-21/Gu-Ailing-Eileen-claims-2nd-gold-for-China-at-Winter-Youth-Olympics--NqybjcgxVe/index.html         | 2020-01      |
|  5 | 2020-01-22 | Winter Youth Olympic Games Lausanne 2020                 | Youth Olympic          | Women's Big Air    | Gold Medal (1st)   | 1. Eileen Gu (CHN), 2. Anastasia Tatalina (RUS), 3. Lara Wolf (GER)   | https://en.wikipedia.org/wiki/China_at_the_2020_Winter_Youth_Olympics                                                                    | 2020-01      |
|  6 | 2020-02-14 | FIS Freestyle Ski World Cup - Calgary Snow Rodeo         | World Cup              | Women's Halfpipe   | Gold Medal (1st)   | 1. Eileen Gu (CHN), 2. Cassie Sharpe (CAN), 3. Rachael Karker (CAN)   | https://en.wikipedia.org/wiki/Eileen_Gu                                                                                                  | 2020-02      |
|  7 | 2020-02-15 | FIS Freestyle Ski World Cup - Calgary Snow Rodeo         | World Cup              | Women's Slopestyle | Gold Medal (1st)   | 1. Eileen Gu (CHN), 2. Megan Oldham (CAN), 3. Mathilde Gremaud (SUI)  | https://en.wikipedia.org/wiki/Eileen_Gu                                                                                                  | 2020-02      |
|  8 | 2021-01-29 | Winter X Games Aspen 2021                                | Invitational (X Games) | Women's Big Air    | Bronze Medal (3rd) | 1. Mathilde Gremaud (SUI), 2. Megan Oldham (CAN), 3. Eileen Gu (CHN)  | https://www.aspentimes.com/news/new-star-eileen-gu-wins-second-gold-third-medal-in-historic-x-games-aspen-debut/                         | 2021-01      |
|  9 | 2021-01-29 | Winter X Games Aspen 2021                                | Invitational (X Games) | Women's SuperPipe  | Gold Medal (1st)   | 1. Eileen Gu (CHN), 2. Cassie Sharpe (CAN), 3. Rachael Karker (CAN)   | https://www.aspentimes.com/news/new-star-eileen-gu-wins-second-gold-third-medal-in-historic-x-games-aspen-debut/                         | 2021-01      |
| 10 | 2021-01-30 | Winter X Games Aspen 2021                                | Invitational (X Games) | Women's Slopestyle | Gold Medal (1st)   | 1. Eileen Gu (CHN), 2. Megan Oldham (CAN), 3. Mathilde Gremaud (SUI)  | https://www.aspentimes.com/news/new-star-eileen-gu-wins-second-gold-third-medal-in-historic-x-games-aspen-debut/                         | 2021-01      |
| 11 | 2021-03-11 | FIS Freestyle Ski and Snowboarding World Championships   | World Championship     | Women's Halfpipe   | Gold Medal (1st)   | 1. Eileen Gu (CHN), 2. Cassie Sharpe (CAN), 3. Rachael Karker (CAN)   | https://en.wikipedia.org/wiki/Eileen_Gu                                                                                                  | 2021-03      |
| 12 | 2021-03-13 | FIS Freestyle Ski and Snowboarding World Championships   | World Championship     | Women's Slopestyle | Gold Medal (1st)   | 1. Eileen Gu (CHN), 2. Mathilde Gremaud (SUI), 3. Megan Oldham (CAN)  | https://www.downdays.eu/events/report/2021-fis-freestyle-world-championships-slopestyle-recap-results-replay/                            | 2021-03      |
| 13 | 2021-12-04 | FIS Freestyle Ski World Cup - Steamboat Springs          | World Cup              | Women's Big Air    | Gold Medal (1st)   | 1. Eileen Gu (CHN), 2. Megan Oldham (CAN), 3. Tess Ledeux (FRA)       | https://www.fis-ski.com/freeski-park-and-pipe/news/2021-22/gu-and-svancer-on-another-level-in-steamboat-big-air                          | 2021-12      |
| 14 | 2021-12-10 | FIS Freestyle Ski World Cup - Copper Mountain            | World Cup              | Women's Halfpipe   | Gold Medal (1st)   | 1. Eileen Gu (CHN), 2. Rachael Karker (CAN), 3. Cassie Sharpe (CAN)   | https://www.downdays.eu/events/report/world-cup-halfpipe-eileen-gu-alex-ferreira-win-at-copper-mountain/                                 | 2021-12      |
| 15 | 2021-12-30 | FIS Freestyle Ski World Cup - Calgary Snow Rodeo         | World Cup              | Women's Halfpipe   | Gold Medal (1st)   | 1. Eileen Gu (CHN), 2. Rachael Karker (CAN), 3. Cassie Sharpe (CAN)   | https://en.wikipedia.org/wiki/Eileen_Gu                                                                                                  | 2021-12      |
| 16 | 2022-01-01 | FIS Freestyle Ski World Cup - Calgary Snow Rodeo         | World Cup              | Women's Halfpipe   | Gold Medal (1st)   | 1. Eileen Gu (CHN), 2. Rachael Karker (CAN), 3. Cassie Sharpe (CAN)   | https://en.wikipedia.org/wiki/Eileen_Gu                                                                                                  | 2022-01      |
| 17 | 2022-01-08 | FIS Freestyle Ski World Cup - Mammoth Mountain           | World Cup              | Women's Halfpipe   | Gold Medal (1st)   | 1. Eileen Gu (CHN), 2. Kelly Sildaru (EST), 3. Brita Sigourney (USA)  | https://www.downdays.eu/events/report/nico-porteous-eileen-gu-win-mammoth-world-cup-halfpipe/                                            | 2022-01      |
| 18 | 2022-02-08 | Winter Olympic Games Beijing 2022                        | Olympic                | Women's Big Air    | Gold Medal (1st)   | 1. Eileen Gu (CHN), 2. Tess Ledeux (FRA), 3. Mathilde Gremaud (SUI)   | https://www.skimag.com/olympics/eileen-gu-wins-olympic-big-air-gold/                                                                     | 2022-02      |
| 19 | 2022-02-15 | Winter Olympic Games Beijing 2022                        | Olympic                | Women's Slopestyle | Silver Medal (2nd) | 1. Mathilde Gremaud (SUI), 2. Eileen Gu (CHN), 3. Kelly Sildaru (EST) | https://www.espn.com/olympics/story/_/id/33292331/olympian-eileen-gu-18-finishes-second-women-ski-slopestyle-snares-second-medal-beijing | 2022-02      |
| 20 | 2022-02-18 | Winter Olympic Games Beijing 2022                        | Olympic                | Women's Halfpipe   | Gold Medal (1st)   | 1. Eileen Gu (CHN), 2. Cassie Sharpe (CAN), 3. Rachael Karker (CAN)   | https://www.olympics.com/en/news/ailing-eileen-gu-freeski-medal-beijing-2022-halfpipe                                                    | 2022-02      |
| 21 | 2023-01-19 | FIS Freestyle Ski World Cup - Calgary Snow Rodeo         | World Cup              | Women's Halfpipe   | Gold Medal (1st)   | 1. Eileen Gu (CHN), 2. Amy Fraser (CAN), 3. Rachael Karker (CAN)      | https://www.fis-ski.com/freeski-park-and-pipe/news/2022-23/calgary-snow-rodeo-halfpipe-results                                           | 2023-01      |
| 22 | 2023-01-21 | FIS Freestyle Ski World Cup - Calgary Snow Rodeo         | World Cup              | Women's Halfpipe   | Gold Medal (1st)   | 1. Eileen Gu (CHN), 2. Amy Fraser (CAN), 3. Rachael Karker (CAN)      | https://www.fis-ski.com/freeski-park-and-pipe/news/2022-23/calgary-snow-rodeo-halfpipe-results                                           | 2023-01      |
| 23 | 2024-01-21 | FIS Freestyle Ski World Cup - Laax                       | World Cup              | Women's Slopestyle | Silver Medal (2nd) | 1. Mathilde Gremaud (SUI), 2. Eileen Gu (CHN), 3. Megan Oldham (CAN)  | https://www.fis-ski.com/freeski-park-and-pipe/news/2023-24/slopestyle-season-begins-in-laax                                              | 2024-01      |
| 24 | 2024-01-27 | Winter X Games Aspen 2024                                | Invitational (X Games) | Women's SuperPipe  | Gold Medal (1st)   | 1. Eileen Gu (CHN), 2. Zoe Atkin (USA), 3. Amy Fraser (CAN)           | https://www.olympics.com/en/news/winter-x-games-aspen-2024-all-results-and-scores-complete-list                                          | 2024-01      |
| 25 | 2024-02-15 | FIS Freestyle Ski World Cup - Calgary Snow Rodeo         | World Cup              | Women's Halfpipe   | Gold Medal (1st)   | 1. Eileen Gu (CHN), 2. Amy Fraser (CAN), 3. Rachael Karker (CAN)      | https://www.fis-ski.com/freeski-park-and-pipe/news/2024-25/record-setting-night-at-the-snow-rodeo-for-gu-and-ferreira                    | 2024-02      |
| 26 | 2024-02-17 | FIS Freestyle Ski World Cup - Calgary Snow Rodeo         | World Cup              | Women's Halfpipe   | Gold Medal (1st)   | 1. Eileen Gu (CHN), 2. Amy Fraser (CAN), 3. Rachael Karker (CAN)      | https://www.fis-ski.com/freeski-park-and-pipe/news/2024-25/record-setting-night-at-the-snow-rodeo-for-gu-and-ferreira                    | 2024-02      |
| 27 | 2024-09-09 | FIS Freestyle Ski World Cup - Cardrona (Winter Games NZ) | World Cup              | Women's Halfpipe   | Gold Medal (1st)   | 1. Eileen Gu (CHN), 2. Zhang Kexin (CHN), 3. Rachael Karker (CAN)     | https://www.olympics.com/en/news/olympian-eileen-gu-wins-record-15th-freeski-world-cup                                                   | 2024-09      |
| 28 | 2024-12-07 | FIS Freestyle Ski World Cup - Secret Garden              | World Cup              | Women's Halfpipe   | Gold Medal (1st)   | 1. Eileen Gu (CHN), 2. Li Fanghui (CHN), 3. Svea Irving (USA)         | https://www.olympics.com/en/news/eileen-gu-wins-secret-garden-halfpipe-nick-goepper-results                                              | 2024-12      |
| 29 | 2024-12-21 | FIS Freestyle Ski World Cup - Copper Mountain            | World Cup              | Women's Halfpipe   | Gold Medal (1st)   | 1. Eileen Gu (CHN), 2. Zoe Atkin (GBR), 3. Cassie Sharpe (CAN)        | https://www.olympics.com/en/news/eileen-gu-continues-perfect-start-halfpipe-season-copper-results                                        | 2024-12      |
| 30 | 2025-01-17 | FIS Freestyle Ski World Cup - Laax                       | World Cup              | Women's Slopestyle | Gold Medal (1st)   | 1. Eileen Gu (CHN), 2. Megan Oldham (CAN), 3. Mathilde Gremaud (SUI)  | https://laaxopen.com/en/eileen-gu-and-birk-ruud-are-the-laax-open-2025-freeski-champions/                                                | 2025-01      |

**Note:** The dataset shows Gu's meteoric rise from her first World Cup podium in Font Romeu, France (January 12, 2019) to becoming the most successful freestyle skier in World Cup history by January 2025, with her recent slopestyle victory at Laax marking her continued dominance across multiple disciplines.[^15][^21][^22]
<span style="display:none">[^23][^24][^25][^26][^27][^28][^29][^30][^31][^32][^33][^34][^35][^36][^37][^38][^39][^40][^41][^42][^43][^44][^45][^46][^47][^48][^49][^50][^51][^52][^53][^54]</span>

<div style="text-align: center">⁂</div>

[^1]: https://www.olympics.com/en/news/ailing-eileen-gu-freeski-medal-beijing-2022-halfpipe

[^2]: https://www.nbcolympics.com/news/eileen-gu-triumphs-halfpipe-third-medal-olympics

[^3]: https://www.espn.com/olympics/story/_/id/33292331/olympian-eileen-gu-18-finishes-second-women-ski-slopestyle-snares-second-medal-beijing

[^4]: https://en.wikipedia.org/wiki/Eileen_Gu

[^5]: https://www.downdays.eu/events/report/2021-fis-freestyle-world-championships-slopestyle-recap-results-replay/

[^6]: https://www.olympics.com/en/news/olympian-eileen-gu-wins-record-15th-freeski-world-cup

[^7]: https://www.olympics.com/en/news/eileen-gu-continues-perfect-start-halfpipe-season-copper-results

[^8]: https://www.fis-ski.com/freeski-park-and-pipe/news/2024-25/eileen-gu-wins-historic-17th-world-cup-as-alex-ferreira-returns-to-top-spot

[^9]: https://www.olympics.com/en/news/eileen-gu-wins-secret-garden-halfpipe-nick-goepper-results

[^10]: https://news.cgtn.com/news/2020-01-21/Gu-Ailing-Eileen-claims-2nd-gold-for-China-at-Winter-Youth-Olympics--NqybjcgxVe/index.html

[^11]: https://en.wikipedia.org/wiki/China_at_the_2020_Winter_Youth_Olympics

[^12]: https://www.aspentimes.com/news/new-star-eileen-gu-wins-second-gold-third-medal-in-historic-x-games-aspen-debut/

[^13]: https://www.aspentimes.com/news/eileen-gus-return-to-x-games-aspen-superpipe-ends-much-like-first-with-a-gold-medal/

[^14]: https://www.olympics.com/en/news/winter-x-games-aspen-2024-all-results-and-scores-complete-list

[^15]: https://laaxopen.com/en/eileen-gu-and-birk-ruud-are-the-laax-open-2025-freeski-champions/

[^16]: https://www.chinadailyhk.com/hk/article/602726

[^17]: https://www.fis-ski.com/freeski-park-and-pipe/news/2021-22/eileen-gu-checks-off-another-world-first-with-double-cork-1440

[^18]: https://www.fis-ski.com/freeski-park-and-pipe/news/2021-22/gu-and-svancer-on-another-level-in-steamboat-big-air

[^19]: https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=fs\&competitorid=226193

[^20]: https://www.olympics.com/en/athletes/gu-ailing-eileen

[^21]: https://www.thesportsexaminer.com/freestyle-skiing-eileen-gu-15-takes-world-cup-slopestyle-in-seiser-alm/

[^22]: https://www.nbcolympics.com/videos/2019-font-romeu-eileen-gu-reaches-first-world-cup-podium

[^23]: https://www.scmp.com/sport/other-sport/article/3196813/eileen-gu-named-best-performing-female-athlete-beijing-winter-olympics-says-winning-3-medals-was

[^24]: https://asiasociety.org/southern-california/eileen-gu

[^25]: https://www.fis-ski.com/DB/general/athlete-biography.html?sectorcode=fs\&competitorid=226193\&type=result

[^26]: https://www.youtube.com/watch?v=QXFzzEEJX4Q

[^27]: https://www.youtube.com/watch?v=ODHdH1jy4HQ

[^28]: https://www.multippl.com/eileen-gu-the-half-asian-model-and-skiing-star-passionate-about-representation/

[^29]: https://www.xgames.com/events/x-games-aspen-2024/eileen-gu-athlete-profile

[^30]: https://www.olympics.com/en/video/gu-ailing-right-now-i-am-feeling-pretty-unstoppable/

[^31]: https://unofficialnetworks.com/2024/09/09/eileen-gu-wins-record-breaking-15th-world-cup-halfpipe-event/

[^32]: https://www.wintergamesnz.kiwi/post/eileen-gu-claims-all-time-lead-for-fis-freeski-world-cup-wins-on-closing-day-of-winter-games-nz

[^33]: https://www.olympics.com/en/olympic-games/lausanne-2020

[^34]: https://www.fis-ski.com/freeski-park-and-pipe/news/2024-25/precious-halfpipe-points-and-fis-world-cup-record-up-for-grabs-at-secret-garden

[^35]: https://news.cgtn.com/news/2019-08-29/Eileen-Gu-Mao-Bingqiang-win-freestyle-skiing-titles-in-New-Zealand-JykVkvjt2U/index.html

[^36]: https://www.skimag.com/olympics/eileen-gu-wins-olympic-big-air-gold/

[^37]: https://www.globaltimes.cn/content/1162331.shtml

[^38]: https://www.fis-ski.com/freeski-park-and-pipe/news/2018-19/slopestyle-world-cup-comes-back-to-seiser-alm

[^39]: https://www.downdays.eu/tag/eileen-gu/

[^40]: https://www.cbc.ca/player/play/video/9.6586160

[^41]: https://www.downdays.eu/events/report/nico-porteous-eileen-gu-win-mammoth-world-cup-halfpipe/

[^42]: https://www.fis-ski.com/freeski-park-and-pipe/news/2021-22/gu-and-ferreira-locked-in-for-globes-at-halfpipe-season-finale-in-mammoth

[^43]: https://www.scmp.com/sport/china/article/3158524/chinas-eileen-gu-and-su-yiming-take-historic-big-air-triumph-fis-world

[^44]: https://www.olympics.com/en/news/great-winter-olympic-rivalries-ailing-eileen-gu-and-kelly-sildaru-in-freestyle

[^45]: https://www.downdays.eu/events/report/world-cup-halfpipe-eileen-gu-alex-ferreira-win-at-copper-mountain/

[^46]: https://www.aspentimes.com/news/x-games-aspen-notes-day-0-gu-returns-for-second-time-progression-and-the-brands-future/

[^47]: https://www.chinadaily.com.cn/a/202112/06/WS61adbcc9a310cdd39bc799f1.html

[^48]: https://www.fis-ski.com/freeski-park-and-pipe/news/2023-24/record-setting-night-at-the-snow-rodeo-for-gu-and-ferreira

[^49]: https://snowbrains.com/eileen-gu-sets-all-time-record-for-fis-freeski-world-cup-wins/

[^50]: https://www.clickondetroit.com/sports/2022/02/18/chinas-eileen-gu-triumphs-in-halfpipe-for-second-gold-of-games/

[^51]: https://www.thesportsexaminer.com/freestyle-skiing-fifth-straight-world-cup-win-for-moguls-star-kingsbury/

[^52]: https://www.olympics.com/en/news/freesking-gu-ailing-eileen-history-calgary

[^53]: https://www.mountainwatch.com/Snow-news/eileen-gu-claims-all-time-lead-for-fis-freeski-world-cup-halfpipe-wins-on-closing-day-of-winter-games-nz

[^54]: https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/f0a35abe60db84928ff0ab552957df18/8772f1cd-5113-4c97-b46d-06b6efbd8e54/8f67babe.csv



[The End of Response]

### Single-Row (One extracted item)

[The Start of Single-Row]

|  Index  | Date       | Event_Name                                               | Event_Level            | Discipline         | Result             | Top_3_Athletes                                                        | Competition_Link                                                                                                                         | Year_Month   |
|---:|:-----------|:---------------------------------------------------------|:-----------------------|:-------------------|:-------------------|:----------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|:-------------|
|  3 | 2020-01-18 | Winter Youth Olympic Games Lausanne 2020                 | Youth Olympic          | Women's Slopestyle | Silver Medal (2nd) | 1. Mathilde Gremaud (SUI), 2. Eileen Gu (CHN), 3. Megan Oldham (CAN)  | https://en.wikipedia.org/wiki/China_at_the_2020_Winter_Youth_Olympics                                                                    | 2020-01      |

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
