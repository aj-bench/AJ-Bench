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

Based on Spotify's official 2024 Wrapped data, here are the top 10 most-streamed songs globally and in the U.S. Research suggests these rankings reflect a mix of pop, hip-hop, and alternative influences, with some overlap between lists. It seems likely that viral trends on platforms like TikTok contributed to their success, though streaming data leans toward consistent listener engagement over time.

## Global Top 10
- **1. Espresso** by Sabrina Carpenter: A catchy pop hit that dominated summer playlists.
- **2. Beautiful Things** by Benson Boone: Emotional ballad blending pop and alternative elements.
- **3. BIRDS OF A FEATHER** by Billie Eilish: Melancholic track from her album *Hit Me Hard and Soft*.
- **4. Gata Only** by FloyyMenor, Cris Mj: Reggaeton vibe with Spanish lyrics.
- **5. Lose Control** by Teddy Swims: Soulful R&B-infused pop.
- **6. End of Beginning** by Djo: Nostalgic indie-pop reflecting on change.
- **7. Too Sweet** by Hozier: Folk-pop with a modern twist.
- **8. One Of The Girls** by The Weeknd, JENNIE, Lily Rose Depp: Moody R&B collaboration.
- **9. Cruel Summer** by Taylor Swift: Resurgent 2019 track that gained massive traction.
- **10. Die With A Smile** by Lady Gaga, Bruno Mars: Romantic duet with retro influences.

## U.S. Top 10
- **1. Espresso** by Sabrina Carpenter: Shared top spot with global, highlighting its broad appeal.
- **2. Not Like Us** by Kendrick Lamar: Hip-hop diss track with cultural impact.
- **3. A Bar Song (Tipsy)** by Shaboozey: Country-rap crossover hit.
- **4. I Had Some Help** by Post Malone feat. Morgan Wallen: Collaborative country-pop.
- **5. MILLION DOLLAR BABY** by Tommy Richman: Funky R&B viral sensation.
- **6. Good Luck, Babe!** by Chappell Roan: Queer anthem with 1980s pop flair.
- **7. Beautiful Things** by Benson Boone: Consistent performer across regions.
- **8. BIRDS OF A FEATHER** by Billie Eilish: Strong showing in both lists.
- **9. I Remember Everything** by Zach Bryan feat. Kacey Musgraves: Folk-country duet.
- **10. Stick Season** by Noah Kahan: Reflective folk track.

These lists show a blend of established artists and rising stars, with no major controversies noted beyond typical debates on genre blending. For full details, see the official Spotify source: [Spotify Newsroom](https://newsroom.spotify.com/2024-12-04/top-songs-artists-podcasts-audiobooks-albums-trends-2024/).

| Category | Rank | Title | Link in Spotify | Singer | Language | Songwriter(s) | Producer(s) | Release Date |
|----------|------|-------|-----------------|--------|----------|---------------|-------------|--------------|
| Global | 1 | Espresso | https://open.spotify.com/track/2qSkIjg1o9h3YT9RAgYN75 | Sabrina Carpenter | English | Sabrina Carpenter, Amy Allen, Steph Jones, Julian Bunetta | Julian Bunetta | 2024/04/11 |
| Global | 2 | Beautiful Things | https://open.spotify.com/track/6tNQ70jh4OwmPGpYy6R2o9 | Benson Boone | English | Benson Boone, Jack LaFrantz, Evan Blair | Evan Blair | 2024/01/19 |
| Global | 3 | BIRDS OF A FEATHER | https://open.spotify.com/track/6dOtVTDdiauQNBQEDOtlAB | Billie Eilish | English | Billie Eilish, Finneas O'Connell | Finneas O'Connell | 2024/07/02 |
| Global | 4 | Gata Only | https://open.spotify.com/track/6XjDF6nds4DE2BBbagZol6 | FloyyMenor, Cris Mj | Spanish | FloyyMenor | Big Cvyu | 2024/02/02 |
| Global | 5 | Lose Control | https://open.spotify.com/track/6usohdchdzW9oML7VC4Uhk | Teddy Swims | English | Teddy Swims, Joshua Coleman, Marco Rodriguez, Mikky Ekko, Julian Bunetta | Julian Bunetta | 2023/06/23 |
| Global | 6 | End of Beginning | https://open.spotify.com/track/3qhlB30KknSejmIvZZLjOD | Djo | English | Joe Keery | Joe Keery, Adam Thein | 2024/03/01 |
| Global | 7 | Too Sweet | https://open.spotify.com/track/4IadxL6BUymXlh8RCJJu7T | Hozier | English | Hozier | Hozier, Bekon, Chakra, Sergiu Gherman, Peter Gonzales | 2024/03/22 |
| Global | 8 | One Of The Girls | https://open.spotify.com/track/7CyPwkp0oE8Ro9Dd5CUDjW | The Weeknd, JENNIE, Lily Rose Depp | English | Mike Dean, Abel Tesfaye, Lily-Rose Depp, Ramsey, Sam Levinson | Mike Dean | 2023/12/08 |
| Global | 9 | Cruel Summer | https://open.spotify.com/track/1BxfuPKGuaTgP7aM0Bbdwr | Taylor Swift | English | Taylor Swift, Jack Antonoff, St. Vincent | Taylor Swift, Jack Antonoff | 2019/08/23 |
| Global | 10 | Die With A Smile | https://open.spotify.com/track/2plbrEY59IikOBgBGLjaoe | Lady Gaga, Bruno Mars | English | Lady Gaga, Bruno Mars, Dernst "D'Mile" Emile II, Andrew Watt, James Fauntleroy | Bruno Mars, D'Mile, Lady Gaga, Andrew Watt | 2024/08/16 |
| U.S. | 1 | Espresso | https://open.spotify.com/track/2qSkIjg1o9h3YT9RAgYN75 | Sabrina Carpenter | English | Sabrina Carpenter, Amy Allen, Steph Jones, Julian Bunetta | Julian Bunetta | 2024/04/11 |
| U.S. | 2 | Not Like Us | https://open.spotify.com/track/6AI3ezQ4o3HUoP6Dhudph3 | Kendrick Lamar | English | Kendrick Lamar, Dijon McFarlane, Sean Momberger, Sounwave | Mustard, Sounwave, Sean Momberger | 2024/05/04 |
| U.S. | 3 | A Bar Song (Tipsy) | https://open.spotify.com/track/2FQrifJ1N335Ljm3TjTVVf | Shaboozey | English | Shaboozey, Sean Cook, Nevin Sastry, Joe Kent, Mark Williams, J-Kwon | Sean Cook, Nevin Sastry | 2024/04/12 |
| U.S. | 4 | I Had Some Help | https://open.spotify.com/track/7221xIgOnuakPdLqT0F3nP | Post Malone feat. Morgan Wallen | English | Post Malone, Morgan Wallen, Louis Bell, Charlie Handsome, Jonathan Hoskins, Ernest, Ashley Gorley, Chandler Paul Walters | Louis Bell, Charlie Handsome, Jonathan Hoskins | 2024/05/10 |
| U.S. | 5 | MILLION DOLLAR BABY | https://open.spotify.com/track/5AJ9hqTS2wcFQCELCFRO7A | Tommy Richman | English | Tommy Richman | Max Vossberg, Jonah Roy, Mannyvelli, Sparkheem, Kavi, Gidi | 2024/04/26 |
| U.S. | 6 | Good Luck, Babe! | https://open.spotify.com/track/0WbMK4wrZ1wFSty9F7FCgu | Chappell Roan | English | Chappell Roan, Justin Tranter, Dan Nigro | Dan Nigro | 2024/04/05 |
| U.S. | 7 | Beautiful Things | https://open.spotify.com/track/6tNQ70jh4OwmPGpYy6R2o9 | Benson Boone | English | Benson Boone, Jack LaFrantz, Evan Blair | Evan Blair | 2024/01/19 |
| U.S. | 8 | BIRDS OF A FEATHER | https://open.spotify.com/track/6dOtVTDdiauQNBQEDOtlAB | Billie Eilish | English | Billie Eilish, Finneas O'Connell | Finneas O'Connell | 2024/07/02 |
| U.S. | 9 | I Remember Everything | https://open.spotify.com/track/4KULAymBBJcPRpk1yO4dOG | Zach Bryan feat. Kacey Musgraves | English | Zach Bryan, Kacey Musgraves | Zach Bryan | 2023/09/08 |
| U.S. | 10 | Stick Season | https://open.spotify.com/track/0GNVXNz7Jkicfk2mp5OyG5 | Noah Kahan | English | Noah Kahan | Noah Kahan, Gabe Simon | 2022/07/08 |

**Key Citations:**
- [Spotify Newsroom: Top Artists, Songs, Albums, Podcasts, and Audiobooks of 2024](https://newsroom.spotify.com/2024-12-04/top-songs-artists-podcasts-audiobooks-albums-trends-2024/)
- [2024 Spotify Wrapped - Top Lists](https://routenote.com/blog/2024-spotify-wrapped-top-lists/)
- [Espresso (song) - Wikipedia](https://en.wikipedia.org/wiki/Espresso_(song))
- [Beautiful Things (Benson Boone song) - Wikipedia](https://en.wikipedia.org/wiki/Beautiful_Things_(Benson_Boone_song))
- [Birds of a Feather (Billie Eilish song) - Wikipedia](https://en.wikipedia.org/wiki/Birds_of_a_Feather_(Billie_Eilish_song))
- [Gata Only - Wikipedia](https://en.wikipedia.org/wiki/Gata_Only)
- [Lose Control (Teddy Swims song) - Wikipedia](https://en.wikipedia.org/wiki/Lose_Control_(Teddy_Swims_song))
- [End of Beginning - Wikipedia](https://en.wikipedia.org/wiki/End_of_Beginning)
- [Too Sweet - Wikipedia](https://en.wikipedia.org/wiki/Too_Sweet)
- [One of the Girls - Wikipedia](https://en.wikipedia.org/wiki/One_of_the_Girls)
- [Cruel Summer (Taylor Swift song) - Wikipedia](https://en.wikipedia.org/wiki/Cruel_Summer_(Taylor_Swift_song))
- [Die with a Smile - Wikipedia](https://en.wikipedia.org/wiki/Die_with_a_Smile)
- [Not Like Us - Wikipedia](https://en.wikipedia.org/wiki/Not_Like_Us)
- [A Bar Song (Tipsy) - Wikipedia](https://en.wikipedia.org/wiki/A_Bar_Song_(Tipsy))
- [I Had Some Help - Wikipedia](https://en.wikipedia.org/wiki/I_Had_Some_Help)
- [Million Dollar Baby (Tommy Richman song) - Wikipedia](https://en.wikipedia.org/wiki/Million_Dollar_Baby_(Tommy_Richman_song))
- [Good Luck, Babe! - Wikipedia](https://en.wikipedia.org/wiki/Good_Luck,_Babe!)
- [I Remember Everything - Wikipedia](https://en.wikipedia.org/wiki/I_Remember_Everything_(song))
- [Stick Season (song) - Wikipedia](https://en.wikipedia.org/wiki/Stick_Season_(song))

[The End of Response]

### Single-Row (One extracted item)

[The Start of Single-Row]

| Category | Rank | Title | Link in Spotify | Singer | Language | Songwriter(s) | Producer(s) | Release Date |
|----------|------|-------|-----------------|--------|----------|---------------|-------------|--------------|
| Global | 6 | End of Beginning | https://open.spotify.com/track/3qhlB30KknSejmIvZZLjOD | Djo | English | Joe Keery | Joe Keery, Adam Thein | 2024/03/01 |

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
