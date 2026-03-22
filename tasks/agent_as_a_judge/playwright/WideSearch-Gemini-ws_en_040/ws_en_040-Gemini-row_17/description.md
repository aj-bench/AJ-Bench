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

# **The Global Top 10: A Consolidated Ranking of Most Downloaded Apps (2020-2022)**

The following table presents a consolidated ranking of the top 10 most downloaded mobile applications globally for the years 2020, 2021, and 2022\. The data has been synthesized from multiple leading market intelligence firms, including Appfigures, Sensor Tower, and App Annie, to provide a single, authoritative view of the market landscape. This process resolves minor discrepancies in individual reports, offering a consensus on the rank and download volumes for each application. The inclusion of parent company and country of origin data transforms this list from a simple ranking into a strategic map, immediately illustrating the geopolitical and corporate dynamics at play, most notably the competitive landscape dominated by American and Chinese technology conglomerates.

| Year | Rank | App | Downloads(million) | Category | Parent Company | Country | App Official Link |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **2022** | 1 | TikTok | 672 | Social Media / Entertainment | ByteDance | China | [https://www.tiktok.com](https://www.tiktok.com) |
| **2022** | 2 | Instagram | 548 | Social Media / Photo & Video | Meta Platforms, Inc. | USA | [https://www.instagram.com](https://www.instagram.com) |
| **2022** | 3 | Facebook | 449 | Social Media | Meta Platforms, Inc. | USA | [https://www.facebook.com](https://www.facebook.com) |
| **2022** | 4 | WhatsApp | 424 | Communication / Messaging | Meta Platforms, Inc. | USA | [https://www.whatsapp.com](https://www.whatsapp.com) |
| **2022** | 5 | CapCut | 357 | Video Editor / Utilities | ByteDance | China | [https://www.capcut.com](https://www.capcut.com) |
| **2022** | 6 | Snapchat | 330 | Social Media / Messaging | Snap Inc. | USA | [https://www.snapchat.com](https://www.snapchat.com) |
| **2022** | 7 | Telegram | 310 | Communication / Messaging | Telegram Group Inc. | UAE / British Virgin Islands | [https://telegram.org](https://telegram.org) |
| **2022** | 8 | Subway Surfers | 304 | Game | SYBO Games | Denmark | [https://www.subwaysurfers.com](https://www.subwaysurfers.com) |
| **2022** | 9 | Stumble Guys | 254 | Game | Kitka Games / Scopely | Finland / USA | [https://www.stumbleguys.com](https://www.stumbleguys.com) |
| **2022** | 10 | Spotify | 238 | Music / Audio Streaming | Spotify AB | Sweden | [https://www.spotify.com](https://www.spotify.com) |
| **2021** | 1 | TikTok | 586 | Social Media / Entertainment | ByteDance | China | [https://www.tiktok.com](https://www.tiktok.com) |
| **2021** | 2 | Instagram | 566 | Social Media / Photo & Video | Meta Platforms, Inc. | USA | [https://www.instagram.com](https://www.instagram.com) |
| **2021** | 3 | Facebook | 416 | Social Media | Meta Platforms, Inc. | USA | [https://www.facebook.com](https://www.facebook.com) |
| **2021** | 4 | WhatsApp | 395 | Communication / Messaging | Meta Platforms, Inc. | USA | [https://www.whatsapp.com](https://www.whatsapp.com) |
| **2021** | 5 | Telegram | 365 | Communication / Messaging | Telegram Group Inc. | UAE / British Virgin Islands | [https://telegram.org](https://telegram.org) |
| **2021** | 6 | Snapchat | 327 | Social Media / Messaging | Snap Inc. | USA | [https://www.snapchat.com](https://www.snapchat.com) |
| **2021** | 7 | Zoom | 300 | Business / Communication | Zoom Video Communications, Inc. | USA | [https://www.zoom.com](https://www.zoom.com) |
| **2021** | 8 | Messenger | 268¹ | Communication / Messaging | Meta Platforms, Inc. | USA | [https://www.messenger.com](https://www.messenger.com) |
| **2021** | 9 | CapCut | 255¹ | Video Editor / Utilities | ByteDance | China | [https://www.capcut.com](https://www.capcut.com) |
| **2021** | 10 | Spotify | 203¹ | Music / Audio Streaming | Spotify AB | Sweden | [https://www.spotify.com](https://www.spotify.com) |
| **2020** | 1 | TikTok | 850 | Social Media / Entertainment | ByteDance | China | [https://www.tiktok.com](https://www.tiktok.com) |
| **2020** | 2 | WhatsApp | 600 | Communication / Messaging | Meta Platforms, Inc. | USA | [https://www.whatsapp.com](https://www.whatsapp.com) |
| **2020** | 3 | Facebook | 540 | Social Media | Meta Platforms, Inc. | USA | [https://www.facebook.com](https://www.facebook.com) |
| **2020** | 4 | Instagram | 503 | Social Media / Photo & Video | Meta Platforms, Inc. | USA | [https://www.instagram.com](https://www.instagram.com) |
| **2020** | 5 | Zoom | 477 | Business / Communication | Zoom Video Communications, Inc. | USA | [https://www.zoom.com](https://www.zoom.com) |
| **2020** | 6 | Messenger | 404¹ | Communication / Messaging | Meta Platforms, Inc. | USA | [https://www.messenger.com](https://www.messenger.com) |
| **2020** | 7 | Snapchat | 281¹ | Social Media / Messaging | Snap Inc. | USA | [https://www.snapchat.com](https://www.snapchat.com) |
| **2020** | 8 | Telegram | 256¹ | Communication / Messaging | Telegram Group Inc. | UAE / British Virgin Islands | [https://telegram.org](https://telegram.org) |
| **2020** | 9 | Google Meet | 254 | Business / Communication | Google (Alphabet Inc.) | USA | [https://workspace.google.com/products/meet/](https://workspace.google.com/products/meet/) |
| **2020** | 10 | Netflix | 223¹ | Entertainment / Video Streaming | Netflix, Inc. | USA | [https://www.netflix.com](https://www.netflix.com) |

*¹ Download figures for some apps in the lower ranks of 2020 and 2021 are consensus estimates derived from market analysis, as precise, universally agreed-upon numbers were not available across all primary sources.*

# **Annual Deep Dive: A Year-by-Year Market Analysis**

## **The 2020 Landscape: Connection in Crisis**

The year 2020 was an anomaly in the history of mobile applications, defined almost entirely by the global response to the COVID-19 pandemic. The rankings for this year reflect a world grappling with sudden and widespread lockdowns, which transformed mobile apps from conveniences into essential utilities for maintaining professional, educational, and social continuity. The central theme was a global pivot to remote everything, a trend that propelled business and communication apps to unprecedented heights on consumer download charts.<sup>1</sup>

The most dramatic story of the year was the meteoric rise of **Zoom**. Previously a well-regarded enterprise tool, it exploded into the public consciousness, becoming a household name and a verb. The platform recorded over 477 million downloads, a figure that represents a near 30-fold increase from its 16 million downloads in 2019\.<sup>5</sup> It became the de facto platform for everything from government sessions and corporate board meetings to virtual family gatherings and online schooling.4 This surge was mirrored by the rapid growth of **Google Meet**, which Google strategically unbundled from its paid enterprise suite and made free for all users, earning it over 254 million downloads.<sup>4</sup> These platforms were no longer just software; they were critical infrastructure facilitating a global response to a crisis.

This sudden shift revealed a fundamental blurring of the lines between applications designed for personal use and those built for professional environments. The mass consumer adoption of an enterprise-grade tool like Zoom created a new "prosumer" communication category. Users who experienced its relatively seamless and reliable video conferencing for work began to expect the same level of quality from their personal messaging apps. This phenomenon put immense pressure on incumbents like Meta to enhance the video capabilities across their portfolio. Conversely, the intuitive, consumer-friendly user interface of Zoom set a new benchmark for enterprise software, compelling competitors to prioritize ease of use over complex feature sets.

Despite the rise of these utility apps, the established social media giants remained formidable. Meta's suite of **WhatsApp** (600 million), **Facebook** (540 million), and **Instagram** (503 million) held three of the top four spots, demonstrating the enduring power of their massive, interconnected user bases.<sup>9</sup> At the same time, **TikTok** continued its unstoppable ascent, securing the number one position with over 850 million downloads. Its success was particularly notable as it came in the face of significant geopolitical headwinds, including a ban in the key market of India and regulatory threats in the United States, proving the immense global appeal of its algorithm-driven content model.<sup>1</sup>

## **The 2021 Landscape: The Great Habit-Formation**

If 2020 was the year of forced adoption, 2021 was the year of habit-formation, where the digital behaviors necessitated by the pandemic became deeply entrenched in daily life. The download charts for 2021 reflect a market solidifying around these new norms, with entertainment and communication platforms cementing their dominance. The theme of the year was less about disruption and more about the solidification of the new status quo.

**TikTok** firmly established itself as the most downloaded app in the world, securing its \#1 position with an estimated 586 million new downloads.<sup>10</sup> This confirmed that its 2020 success was not a fleeting trend but the mark of a new market leader. Meta's platforms proved their incredible resilience, with **Instagram** (566 million), **Facebook** (416 million), and **WhatsApp** (395 million) occupying the next three positions, showcasing the formidable strength of their combined social graph.<sup>8</sup>

However, 2021 also revealed the first significant vulnerability in a major platform's armor, centered on the issue of user privacy. In early 2021, a poorly communicated update to WhatsApp's privacy policy triggered a widespread user backlash and a subsequent migration to alternative messaging platforms. The primary beneficiary of this was **Telegram**, which surged into the top five globally with 365 million new downloads.<sup>10</sup> In January 2021 alone, Telegram saw over 63 million installs as users sought out a platform perceived to be more secure and respectful of their data.<sup>11</sup> This event served as a large-scale, real-world experiment on the balance between network effects and user trust. It demonstrated that while the friction of switching communication apps is high, it is not insurmountable when a platform is perceived to have violated the trust of its user base. This mass migration has likely forced all major platforms to recalibrate their approach to communicating policy changes and to invest more heavily in privacy-centric marketing, such as the frequent promotion of end-to-end encryption.

The rest of the top 10 underscored the enduring impact of the trends that began in 2020\. The continued strong showing of **Zoom** highlighted the permanence of hybrid and remote work models.<sup>9</sup> Meanwhile, the rapid ascent of **CapCut**, TikTok's companion video-editing app, into the top 10 was a clear signal of the booming creator economy.<sup>10</sup> Users were no longer just consuming content; they were actively participating in its creation, and they sought out tools that made this process seamless and accessible.

## **The 2022 Landscape: Entertainment and Ecosystems**

The 2022 app market was defined by two primary themes: the maturation of powerful, vertically integrated platform ecosystems and the notable diversification of at-scale entertainment. The battle at the very top of the charts remained a two-horse race between the flagships of ByteDance and Meta. **TikTok** once again claimed the top spot with 672 million downloads, while **Instagram** followed closely with 548 million, continuing its strategic pivot toward short-form video to compete.<sup>8</sup>

The most telling strategic development of the year was the symbiotic relationship between a platform and its tools, exemplified by ByteDance. **CapCut**, its free video editing software, surged to the \#4 position with an astonishing 357 million downloads.<sup>8</sup> This was not an accident but a masterclass in ecosystem strategy. By providing a powerful, user-friendly tool tailored for creating content for its primary platform, ByteDance effectively built a pipeline that fueled the TikTok content engine, making it easier for creators to produce the high-quality videos that keep users engaged. This vertical integration created a powerful competitive moat that is difficult for rivals to replicate.

The second major story of 2022 was the breakthrough of non-social and non-communication apps into the highest echelon of the download charts, indicating a broadening of consumer attention. For the first time in this three-year period, two mobile games secured spots in the top 10\. **Subway Surfers**, a title originally released in 2012, demonstrated incredible longevity by capturing the \#8 spot with 304 million downloads, its popularity likely amplified by viral trends on platforms like TikTok.<sup>8</sup> It was joined by **Stumble Guys**, a newer viral hit that garnered 254 million downloads, proving that the "party game" format could achieve massive scale.<sup>8</sup> The appearance of both a decade-old classic and a new viral sensation underscores the immense and evergreen power of mobile gaming as a cultural force, capable of generating download velocities that rival the largest social media platforms.

This diversification extended beyond gaming. **Spotify** broke into the top 10 with 238 million downloads, a significant achievement for a subscription-based service in a landscape dominated by free, ad-supported apps.8 This signals the maturity of the audio streaming market and the willingness of a global user base to pay for premium content experiences. The overall diversity of the 2022 list suggests that while a few giants control the main social channels, there is significant opportunity for specialized apps in verticals like gaming and music to achieve global scale.

### **Work cited**

1. Top 10 most-downloaded apps in 2020, [https://bccci.net/blog/top-10-most-downloaded-apps-in-2020/](https://bccci.net/blog/top-10-most-downloaded-apps-in-2020/)  
2. Ranked: The World's Most Popular Apps by Downloads, [https://www.visualcapitalist.com/cp/most-popular-apps-by-downloads/](https://www.visualcapitalist.com/cp/most-popular-apps-by-downloads/)  
3. App Annie: 3.8 trillion hours spent on mobiles in 2021 | Technology Magazine, [https://technologymagazine.com/digital-transformation/app-annie-38-trillion-hours-spent-mobiles-2021](https://technologymagazine.com/digital-transformation/app-annie-38-trillion-hours-spent-mobiles-2021)  
4. The Most Downloaded Apps Worldwide in 2020 \- Appfigures, [https://appfigures.com/resources/insights/most-downloaded-mobile-apps-2020/amp](https://appfigures.com/resources/insights/most-downloaded-mobile-apps-2020/amp)  
5. The Most Downloaded Apps Worldwide in 2020 \- Appfigures, [https://appfigures.com/resources/insights/most-downloaded-mobile-apps-2020](https://appfigures.com/resources/insights/most-downloaded-mobile-apps-2020)  
6. The Top Downloaded Apps in 2022 \- Visual Capitalist, [https://www.visualcapitalist.com/top-downloaded-apps-2022/](https://www.visualcapitalist.com/top-downloaded-apps-2022/)  
7. Sensor Tower's Q1 2022 Data Digest: Worldwide App Downloads Reached 37 Billion Last Quarter, [https://sensortower.com/blog/q1-2022-data-digest](https://sensortower.com/blog/q1-2022-data-digest)  
8. Top 10 most downloaded mobile apps of 2022 | Telco Magazine, [https://telcomagazine.com/articles/top-10-most-downloaded-mobile-apps-of-2022](https://telcomagazine.com/articles/top-10-most-downloaded-mobile-apps-of-2022)  
9. Most Popular Apps 2025: Global Stats & Rankings \- Backlinko, [https://backlinko.com/most-popular-apps](https://backlinko.com/most-popular-apps)  
10. The Most Downloaded App in 2021 · ASO Tools and App Analytics ..., [https://appfigures.com/resources/insights/20211224?f=1](https://appfigures.com/resources/insights/20211224?f=1)  
11. Top Apps Worldwide for January 2021 by Downloads \- Sensor Tower, [https://sensortower.com/blog/top-apps-worldwide-january-2021-by-downloads](https://sensortower.com/blog/top-apps-worldwide-january-2021-by-downloads)  
12. Top 10 Globally Most Downloaded Apps Of 2021 \- YourDigiLab, [https://yourdigilab.com/blog/most-downloaded-apps-2021](https://yourdigilab.com/blog/most-downloaded-apps-2021)  
13. Introducing the most downloaded apps of 2021 \- Mashable, [https://mashable.com/article/most-downloaded-apps-2021](https://mashable.com/article/most-downloaded-apps-2021)  
14. Subway Surfers \- Wikipedia, [https://en.wikipedia.org/wiki/Subway\_Surfers](https://en.wikipedia.org/wiki/Subway_Surfers)  
15. Meta Platforms \- Wikipedia, [https://en.wikipedia.org/wiki/Meta\_Platforms](https://en.wikipedia.org/wiki/Meta_Platforms)  
16. The Big Winners of 2021 in Apps: TikTok, Meta, Tinder, Free Fire, ROBLOX and More, [https://dfdnews.com/2022/02/09/the-big-winners-of-2021-in-apps-tiktok-meta-tinder-free-fire-roblox-and-more/](https://dfdnews.com/2022/02/09/the-big-winners-of-2021-in-apps-tiktok-meta-tinder-free-fire-roblox-and-more/)  
17. What Happened to CapCut? \- The Visla Blog, [https://www.visla.us/blog/news/what-happened-to-capcut/](https://www.visla.us/blog/news/what-happened-to-capcut/)  
18. Most Popular Apps (2025) \- Business of Apps, [https://www.businessofapps.com/data/most-popular-apps/](https://www.businessofapps.com/data/most-popular-apps/)

[The End of Response]

### Single-Row (One extracted item)

[The Start of Single-Row]

| Year | Rank | App | Downloads(million) | Category | Parent Company | Country | App Official Link |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **2021** | 7 | Zoom | 300 | Business / Communication | Zoom Video Communications, Inc. | USA | [https://www.zoom.com](https://www.zoom.com) |

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
