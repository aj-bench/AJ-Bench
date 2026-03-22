# Agent-as-a-Judge Task

You will verify the factual correctness of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

I need a list of the top 10 most-streamed songs globally and top 10 most-streamed songs in the U.S. on Spotify in 2024. Please provide an official link to support your statement. The header names should include Category, Song Rank, Song Title, Song Link in Spotify, Singer, Language, Songwriter(s), Producer(s), and Release Date.

Please organize the results in one Markdown table with the following columns:
Category,Rank,Title,Link in Spotify,Singer,Language,Songwriter(s),Producer(s),Release Date.
Note:
1.The song rankings need to be sorted in descending order.
2. Most-streamed songs globally and U.S. most-streamed songs need to be distinguished in the "Category" column.
3. Release date should be written as YYYY/MM/DD
4. If there is more than one songwriter or producer, separate them by comma.

[The End of Query]

### Response

[The Start of Response]

# Top 10 Most-Streamed Songs on Spotify in 2024

| Category | Rank | Title | Link in Spotify | Singer | Language | Songwriter(s) | Producer(s) | Release Date |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Global Most-Streamed | 1 | Espresso | https://open.spotify.com/track/3RU0w6oEUtPdEGgcQkHqkW | Sabrina Carpenter | English | Sabrina Carpenter, Jon Bellion, Amy Allen | Jon Bellion | 2024/04/11 |
| Global Most-Streamed | 2 | Beautiful Things | https://open.spotify.com/track/2A9D3q2cv3JImf0jWS9BqP | Benson Boone | English | Benson Boone, Ashley Gorley, Jackson Morgan | Jonas Jeberg | 2024/02/02 |
| Global Most-Streamed | 3 | BIRDS OF A FEATHER | https://open.spotify.com/track/6YU9wFICWCgW8VohFXRX6t | Billie Eilish | English | Billie Eilish, Finneas O’Connell | Finneas O’Connell | 2024/05/02 |
| Global Most-Streamed | 4 | Gata Only | https://open.spotify.com/track/1yqzQK2IapL1eEyrGwv3HQ | FloyyMenor, Cris Mj | Spanish | FloyyMenor, Cris MJ | FloyyMenor | 2024/03/15 |
| Global Most-Streamed | 5 | Lose Control | https://open.spotify.com/track/1bFqJQW8unK1RxK1FUIv7H | Teddy Swims | English | Kevin Jiménez, William Harrington | Kevin Jiménez, Ricky Reed | 2024/07/01 |
| Global Most-Streamed | 6 | End of Beginning | https://open.spotify.com/track/5XwTHAq7zHZi4sLkMPzqH1 | Djo | English | Joe Keery, Justin Tranter | Djo, Sam Homaee | 2024/08/20 |
| Global Most-Streamed | 7 | Too Sweet | https://open.spotify.com/track/0cBD8AUh25Dw79B2SuV7r0 | Hozier | English | Andrew Hozier-Byrne | Rob Kirwan | 2024/06/21 |
| Global Most-Streamed | 8 | One Of The Girls (with JENNIE, Lily Rose Depp) | https://open.spotify.com/track/4kM0uRsCLYOlyrW04qGVlM | The Weeknd, JENNIE, Lily-Rose Depp | English | Abel Tesfaye, Jennie Kim, Lana Del Rey | Max Martin, Oscar Holter | 2024/03/10 |
| Global Most-Streamed | 9 | Cruel Summer | https://open.spotify.com/track/2uU1VBgwc5k5w2A2bB5h2d | Taylor Swift | English | Taylor Swift, Jack Antonoff | Jack Antonoff | 2019/08/19 |
| Global Most-Streamed | 10 | Die With A Smile | https://open.spotify.com/track/7GVFoWGpoovqCOonqs7qEj | Lady Gaga, Bruno Mars | English | Stefani Germanotta, Peter Svensson, Bruno Mars | BloodPop®, Burns, Gaga | 2024/08/16 |
| U.S. Most-Streamed | 1 | Espresso | https://open.spotify.com/track/3RU0w6oEUtPdEGgcQkHqkW | Sabrina Carpenter | English | Sabrina Carpenter, Jon Bellion, Amy Allen | Jon Bellion | 2024/04/11 |
| U.S. Most-Streamed | 2 | Not Like Us | https://open.spotify.com/track/5GzXjwxhsB1n9HTYhvSpC2 | Kendrick Lamar | English | Kendrick Lamar, Dave Free, Bijan Amir | Sounwave, DJ Dahi | 2024/09/01 |
| U.S. Most-Streamed | 3 | A Bar Song (Tipsy) | https://open.spotify.com/track/6qXqdvu93GJ9VxG5fEYnbR | Shaboozey | English | Shaboozey | Shaboozey, Mike Crossey | 2024/02/10 |
| U.S. Most-Streamed | 4 | I Had Some Help (feat. Morgan Wallen) | https://open.spotify.com/track/4X0l2CjDEiOxYeR1eBG7aX | Post Malone, Morgan Wallen | English | Austin Post, Morgan Wallen, Louis Bell | Post Malone | 2024/05/05 |
| U.S. Most-Streamed | 5 | MILLION DOLLAR BABY | https://open.spotify.com/track/3PL1WE04rXL6uz4an7f0Wb | Tommy Richman | English | Tommy Richman | Tommy Richman | 2024/07/12 |
| U.S. Most-Streamed | 6 | Good Luck, Babe! | https://open.spotify.com/track/5fT7B4n5fYtWQ6o6h6TLGh | Chappell Roan | English | Chappell Roan, Dan Wilson | Dan Wilson | 2024/03/22 |
| U.S. Most-Streamed | 7 | Beautiful Things | https://open.spotify.com/track/2A9D3q2cv3JImf0jWS9BqP | Benson Boone | English | Benson Boone, Ashley Gorley, Jackson Morgan | Jonas Jeberg | 2024/02/02 |
| U.S. Most-Streamed | 8 | BIRDS OF A FEATHER | https://open.spotify.com/track/6YU9wFICWCgW8VohFXRX6t | Billie Eilish | English | Billie Eilish, Finneas O’Connell | Finneas O’Connell | 2024/05/02 |
| U.S. Most-Streamed | 9 | I Remember Everything (feat. Kacey Musgraves) | https://open.spotify.com/track/2KCRtR9HfCQeJHte1RZkLe | Zach Bryan, Kacey Musgraves | English | Zach Bryan, Kacey Musgraves, William Tyler | Sadler Vaden | 2023/06/27 |
| U.S. Most-Streamed | 10 | Stick Season | https://open.spotify.com/track/6e1VWn7xOudF3bFXUG6vT5 | Noah Kahan | English | Noah Kahan | Gabe Simon | 2023/10/20 |

Official Spotify announcement: https://newsroom.spotify.com/2024-12-04/top-songs-artists-podcasts-audiobooks-albums-trends-2024/
<span style="display:none">[^1][^10][^2][^3][^4][^5][^6][^7][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://en.wikipedia.org/wiki/List_of_Spotify_streaming_records

[^2]: https://chartmasters.org/spotify-most-streamed-artists-2024/

[^3]: https://www.reddit.com/r/popheads/comments/1hsba3g/birds_of_a_feather_is_officially_the_most/

[^4]: https://kworb.net/spotify/songs_2024.html

[^5]: https://newsroom.spotify.com/2024-12-04/top-songs-artists-podcasts-audiobooks-albums-trends-2024/

[^6]: https://open.spotify.com/playlist/37i9dQZF1DX18jTM2l2fJY

[^7]: https://charts.spotify.com/charts/overview/global

[^8]: https://www.reddit.com/r/TaylorSwift/comments/1h6fhp3/taylor_swift_is_spotifys_2024_global_top_artist/

[^9]: https://newsroom.spotify.com/2024-wrapped/

[^10]: https://www.kaggle.com/datasets/nelgiriyewithana/most-streamed-spotify-songs-2024



[The End of Response]

### Single-Row (One extracted item)

[The Start of Single-Row]

| Category | Rank | Title | Link in Spotify | Singer | Language | Songwriter(s) | Producer(s) | Release Date |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| U.S. Most-Streamed | 5 | MILLION DOLLAR BABY | https://open.spotify.com/track/3PL1WE04rXL6uz4an7f0Wb | Tommy Richman | English | Tommy Richman | Tommy Richman | 2024/07/12 |

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
