# Agent-as-a-Judge Task

You will verify the factual correctness of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

I'd like to get a list of the top 10 apps downloaded worldwide each year from 2020 to 2022. Provide official links to support your statement. For each app, I need to know its category (e.g., game, health app, etc.), the company that created it, the country of origin of the company, the download volume (in millions), and the official link of app.

Please organize the results in one Markdown table with the following columns names in order:
Year, Rank, App, Downloads(million), Category, Parent Company, Country, App Official Link

[The End of Query]

### Response

[The Start of Response]

# Data Table
| Year | Rank | App            | Downloads(million) | Category      | Parent Company          | Country | App Official Link              |
|------|------|----------------|---------------------|---------------|-------------------------|---------|--------------------------------|
| 2020 | 1    | TikTok         | 850                | Entertainment | ByteDance               | China   | https://www.tiktok.com/        |
| 2020 | 2    | WhatsApp       | 600                | Messaging     | Meta                    | USA     | https://www.whatsapp.com/      |
| 2020 | 3    | Facebook       | 540                | Social        | Meta                    | USA     | https://www.facebook.com/      |
| 2020 | 4    | Instagram      | 503                | Social        | Meta                    | USA     | https://www.instagram.com/     |
| 2020 | 5    | Zoom           | 477                | Productivity  | Zoom Video Communications | USA   | https://zoom.us/               |
| 2020 | 6    | Messenger      | 423                | Messaging     | Meta                    | USA     | https://www.messenger.com/     |
| 2020 | 7    | Snapchat       | 281                | Social        | Snap Inc.               | USA     | https://www.snapchat.com/      |
| 2020 | 8    | Telegram       | 256                | Messaging     | Telegram FZ-LLC         | UAE     | https://telegram.org/          |
| 2020 | 9    | Google Meet    | 254                | Productivity  | Google                  | USA     | https://meet.google.com/       |
| 2020 | 10   | Netflix        | 223                | Entertainment | Netflix                 | USA     | https://www.netflix.com/       |
| 2021 | 1    | TikTok         | 656                | Entertainment | ByteDance               | China   | https://www.tiktok.com/        |
| 2021 | 2    | Instagram      | 545                | Social        | Meta                    | USA     | https://www.instagram.com/     |
| 2021 | 3    | Facebook       | 416                | Social        | Meta                    | USA     | https://www.facebook.com/      |
| 2021 | 4    | WhatsApp       | 395                | Messaging     | Meta                    | USA     | https://www.whatsapp.com/      |
| 2021 | 5    | Telegram       | 329                | Messaging     | Telegram FZ-LLC         | UAE     | https://telegram.org/          |
| 2021 | 6    | Snapchat       | 327                | Social        | Snap Inc.               | USA     | https://www.snapchat.com/      |
| 2021 | 7    | Zoom           | 300                | Productivity  | Zoom Video Communications | USA   | https://zoom.us/               |
| 2021 | 8    | Messenger      | 291                | Messaging     | Meta                    | USA     | https://www.messenger.com/     |
| 2021 | 9    | CapCut         | 255                | Video Editing | ByteDance               | China   | https://www.capcut.com/        |
| 2021 | 10   | Spotify        | 203                | Music         | Spotify                 | Sweden  | https://www.spotify.com/       |
| 2022 | 1    | TikTok         | 672                | Entertainment | ByteDance               | China   | https://www.tiktok.com/        |
| 2022 | 2    | Instagram      | 548                | Social        | Meta                    | USA     | https://www.instagram.com/     |
| 2022 | 3    | Facebook       | 449                | Social        | Meta                    | USA     | https://www.facebook.com/      |
| 2022 | 4    | WhatsApp       | 424                | Messaging     | Meta                    | USA     | https://www.whatsapp.com/      |
| 2022 | 5    | CapCut         | 357                | Video Editing | ByteDance               | China   | https://www.capcut.com/        |
| 2022 | 6    | Snapchat       | 330                | Social        | Snap Inc.               | USA     | https://www.snapchat.com/      |
| 2022 | 7    | Telegram       | 310                | Messaging     | Telegram FZ-LLC         | UAE     | https://telegram.org/          |
| 2022 | 8    | Subway Surfers | 304                | Game          | SYBO Games              | Denmark | https://subwaysurfers.com/     |
| 2022 | 9    | Stumble Guys   | 254                | Game          | Kitka Games (acq. Scopely) | Finland | https://www.stumbleguys.com/   |
| 2022 | 10   | Messenger      | 250                | Messaging     | Meta                    | USA     | https://www.messenger.com/     |

## Sources and Methodology
The rankings and download volumes are primarily drawn from data.ai (formerly App Annie) reports and cross-verified with Sensor Tower estimates, focusing on combined iOS and Google Play downloads worldwide. Note that some sources exclude pre-installed apps or separate games, leading to minor ranking variations; the table prioritizes inclusive data for comprehensiveness. Country of origin refers to the founding company's location, even if later acquired.

---
The top downloaded apps from 2020 to 2022 reveal a dynamic mobile landscape shaped by global events, technological shifts, and user preferences. This comprehensive overview expands on the key trends, providing deeper context, year-by-year breakdowns, and supporting data from multiple sources. It incorporates all details from the direct answer while adding analytical insights, historical comparisons, and additional tables for clarity.

## Year-by-Year Breakdown and Insights
**2020: Pandemic-Driven Surge in Connectivity and Productivity**  
2020 saw unprecedented download growth due to global lockdowns, with apps facilitating remote work, social interaction, and entertainment leading the pack. Total worldwide app downloads reached approximately 218 billion, up 7% from 2019, per data.ai estimates. Video conferencing apps like Zoom and Google Meet exploded in popularity, reflecting the shift to remote lifestyles. Social platforms dominated otherwise, with TikTok's viral short videos capturing attention amid isolation. Notably, download volumes were the highest in this period, with leaders exceeding 500 million installs. Sources like Appfigures confirm TikTok's dominance but note rapid growth in Zoom (485 million) and Telegram (353 million), aligning closely with the aggregated figures used.

| Rank | App            | Downloads (million) | Key Notes |
|------|----------------|----------------------|-----------|
| 1    | TikTok         | 850                 | Surged due to viral challenges; includes regional variants like Douyin in some estimates. |
| 2    | WhatsApp       | 600                 | Essential for cross-border communication during travel restrictions. |
| 3    | Facebook       | 540                 | Maintained strong user base for news and groups. |
| 4    | Instagram      | 503                 | Photo-sharing thrived as people documented home life. |
| 5    | Zoom           | 477                 | Grew 30x from 2019 amid remote work boom. |
| 6    | Messenger      | 423                 | Paired with Facebook for private chats. |
| 7    | Snapchat       | 281                 | Popular for filters and stories among younger users. |
| 8    | Telegram       | 256                 | Gained traction for privacy features during protests. |
| 9    | Google Meet    | 254                 | Google's rebranded Hangouts benefited from integration with Gmail. |
| 10   | Netflix        | 223                 | Streaming demand spiked with more home time. |

**2021: Stabilization and Content Creation Rise**  
As restrictions eased, downloads slightly dipped to around 230 billion globally, a 5% increase from 2020. TikTok continued leading, but tools like CapCut emerged, signaling a trend toward user-generated content. Video conferencing apps like Zoom declined relatively as in-person activities resumed, while messaging and social apps held steady. Statista notes TikTok's 656 million downloads, consistent with hybrid work persisting. This year also saw Telegram's growth amid privacy concerns with competitors.

| Rank | App            | Downloads (million) | Key Notes |
|------|----------------|----------------------|-----------|
| 1    | TikTok         | 656                 | Maintained momentum with expanded features like live streaming. |
| 2    | Instagram      | 545                 | Reels feature competed directly with TikTok. |
| 3    | Facebook       | 416                 | Focused on community building post-pandemic. |
| 4    | WhatsApp       | 395                 | Added business tools for e-commerce. |
| 5    | Telegram       | 329                 | Benefited from WhatsApp privacy policy backlash. |
| 6    | Snapchat       | 327                 | Introduced Spotlight for short videos. |
| 7    | Zoom           | 300                 | Still essential but growth slowed. |
| 8    | Messenger      | 291                 | Enhanced with end-to-end encryption. |
| 9    | CapCut         | 255                 | TikTok's editing tool rode the video creation wave. |
| 10   | Spotify        | 203                 | Podcasts and playlists drove audio entertainment. |

**2022: Diversification with Gaming and Editing Tools**  
Global downloads reached about 255 billion, up 11% from 2021, per data.ai. Post-pandemic recovery brought casual games like Subway Surfers and Stumble Guys into the top 10, alongside persistent social apps. TikTok's 672 million installs reaffirmed its lead, but Instagram's close second (548 million) showed fierce competition. Video editing (CapCut) and privacy-focused messaging (Telegram) continued strong, reflecting ongoing content creation and security priorities. Some reports exclude games, placing WhatsApp Business or Spotify in lower ranks, but inclusive data highlights gaming's resurgence.

| Rank | App            | Downloads (million) | Key Notes |
|------|----------------|----------------------|-----------|
| 1    | TikTok         | 672                 | Hit peak revenue alongside downloads. |
| 2    | Instagram      | 548                 | Boosted by Threads integration experiments. |
| 3    | Facebook       | 449                 | Emphasized Marketplace for shopping. |
| 4    | WhatsApp       | 424                 | Expanded to business APIs. |
| 5    | CapCut         | 357                 | Grew with TikTok's ecosystem. |
| 6    | Snapchat       | 330                 | AR lenses drove engagement. |
| 7    | Telegram       | 310                 | Privacy features appealed amid data concerns. |
| 8    | Subway Surfers | 304                 | Endless runner game revived nostalgia. |
| 9    | Stumble Guys   | 254                 | Multiplayer battle royale hit mobile gaming. |
| 10   | Messenger      | 250                 | Integrated more with Meta's suite. |

**Key Citations:**
- [Business of Apps - Most Popular Apps (2025)](https://www.businessofapps.com/data/most-popular-apps/) 
- [data.ai State of Mobile 2021 PDF](https://static.poder360.com.br/2021/08/APP-ANNIE-State-of-mobile-2021-1.pdf) 
- [data.ai State of Mobile 2023 PDF](https://cocktailmarketing.com.mx/wp-content/uploads/2023/12/State-of-mobile-2023-data.ai_.pdf) 
- [App Annie: 230B New App Downloads in 2021](https://www.adweek.com/media/app-annie-230b-new-app-downloads-in-2021/) 
- [Visual Capitalist - The Top Downloaded Apps in 2022](https://www.visualcapitalist.com/top-downloaded-apps-2022/) 
- [Statista - Most Downloaded Mobile Apps Worldwide](https://www.statista.com/statistics/1285960/top-downloaded-mobile-apps-worldwide/) 
- [Sensor Tower - Global Consumer Spending in Mobile Apps](https://sensortower.com/blog/app-revenue-and-downloads-2021) 
- [Appfigures - The Most Downloaded Apps Worldwide in 2020](https://appfigures.com/resources/insights/most-downloaded-mobile-apps-2020)

[The End of Response]

### Single-Row (One extracted item)

[The Start of Single-Row]

| Year | Rank | App            | Downloads(million) | Category      | Parent Company          | Country | App Official Link              |
|------|------|----------------|---------------------|---------------|-------------------------|---------|--------------------------------|
| 2021 | 4    | WhatsApp       | 395                | Messaging     | Meta                    | USA     | https://www.whatsapp.com/      |

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
