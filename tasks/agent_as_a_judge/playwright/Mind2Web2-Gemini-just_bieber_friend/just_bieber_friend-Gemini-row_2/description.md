# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Could you remind me of the name of the YouTube influencer who is a friend of Justin Bieber and plays a supporting role in a DC superhero movie? Please provide his name, the title of the movie along with its information page listing the cast, a link to his YouTube channel, and a link to an article or webpage that mentions his relationship with Justin Bieber.

[The End of Query]

### Response

[The Start of Response]

# Identification and Key Verifications

The public figure who meets the specific criteria of being a YouTube influencer, a documented friend and collaborator of musician Justin Bieber, and a supporting actor in a DC superhero film is the multi-talented creator Rudy Mancuso.

Mancuso's role in the DC cinematic landscape was in the 2023 Warner Bros. Pictures film The Flash, where he portrayed the character of Albert Desmond.<sup>1</sup>

To directly address the informational request, the following key resources are provided:

1. Name of the Influencer: Rudy Mancuso  
2. DC Superhero Movie Information: The Flash (2023). The official information page for the film, which includes details on its production and themes, can be found on DC's website:  
   - https://www.dc.com/movies/the-flash-2023  
   - The Flash (2023) Full Cast & Crew - Moviefone: https://www.moviefone.com/movie/the-flash/GqvjtiR1Skzdp96PgxYKv5/credits/  
3. YouTube Channel Link: Mancuso's primary YouTube channel, which serves as the hub for his musical and comedic content, is accessible via the following link:  
   - (https://www.youtube.com/@RudyMancuso)  
4. Article Substantiating Friendship with Justin Bieber: A comprehensive article from People magazine details the origins and nature of their relationship, featuring direct quotes from Mancuso. This article confirms their personal and professional connection:  
   - https://people.com/music/justin-bieber-rudy-mancuso-purpose-tour-brazil-opener-friendship/

## Works cited

1. Rudy Mancuso - Wikipedia, https://en.wikipedia.org/wiki/Rudy_Mancuso  
2. The Flash (2023) Full Cast & Crew - Moviefone, https://www.moviefone.com/movie/the-flash/GqvjtiR1Skzdp96PgxYKv5/credits/  
3. Rudy Mancuso to Open for Justin Bieber Tour in Brazil - People.com, https://people.com/music/justin-bieber-rudy-mancuso-purpose-tour-brazil-opener-friendship/  
4. Justin Bieber Makes Cameo in 'Racist Superman' Video - People.com, https://people.com/music/justin-bieber-racist-superman-video-cameo-canadian-superman/  
5. Rudy Mancuso - YouTube, https://www.youtube.com/user/rudymancuso/about  
6. Amazon's Musica Cast & Character Guide, https://screenrant.com/musica-2024-cast-characters/  
7. Rudy Mancuso - YouTube, https://www.youtube.com/user/rudymancuso  
8. Música (2024 film) - Wikipedia, https://en.wikipedia.org/wiki/M%C3%BAsica_(2024_film)  
9. Guess The Object with Rudy Mancuso and Camila Mendes | Música | Prime Video, https://www.youtube.com/watch?v=2AO4-oY6vmE  
10. The Flash (2023) - DC Comics, https://www.dc.com/movies/the-flash-2023  
11. The Flash (film) - Wikipedia, https://en.wikipedia.org/wiki/The_Flash_(film)  
12. My guess of who Rudy Mancuso and Saorsie Jackson are playing in The Flash : r/DCFilm, https://www.reddit.com/r/DCFilm/comments/ocn23v/my_guess_of_who_rudy_mancuso_and_saorsie_jackson/  
13. Rudy Mancuso is Going on Tour With Justin Bieber, https://staging1.justjaredjr.com/2017/02/14/rudy-mancuso-is-going-on-tour-with-justin-bieber/  
14. Rudy Mancuso is Going on Tour With Justin Bieber - Just Jared Jr, https://www.justjaredjr.com/2017/02/14/rudy-mancuso-is-going-on-tour-with-justin-bieber/  
15. Justin Bieber Guest Stars In Rudy Mancuso's 'Racist Superman' Comedy Sketch - Tubefilter, https://www.tubefilter.com/2018/04/04/justin-bieber-rudy-mancuso-comedy-sketch/  
16. Rudy Mancuso and Justin Bieber Jam - YouTube, https://www.youtube.com/watch?v=8zdA47strL0  
17. Rudy Mancuso - Circle Of Love - YouTube, https://www.youtube.com/watch?v=z8eFzkfto2w

[The End of Response]

### Rubric

[The Start of Rubric]

1. Award 1 point for correctly identifying a person who is both a YouTube influencer and a friend of Justin Bieber, and who played a supporting role in a DC superhero movie.
2. Award 1 point for correctly mentioning the name of the DC superhero movie in which the person appeared.
3. Award 1 point for correctly providing a link (URL) to the movie’s cast information page.
4. Award 1 point for providing the link to the person’s YouTube channel.
5. Award 1 point for providing a link to an article or webpage that proves the relationship between the YouTube influencer and Justin Bieber.
6. Total score: 5 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-2:
Mancuso's role in the DC cinematic landscape was in the 2023 Warner Bros. Pictures film The Flash, where he portrayed the character of Albert Desmond.

[The End of Single-Row]

------------------------------------------------------------
## Core Principle

**Your task is NOT to evaluate whether the Single-Row answers the entire Query. Your task IS ONLY to evaluate whether THIS extracted Single-Row:**

1. **Directly corresponds to exactly ONE scoring unit in the Rubric;**
2. **Correctly reflects the part of the Response it was extracted from;**
3. **Is factually correct according to verification tools;**
4. **Meets ALL requirements of the corresponding Rubric scoring unit;**
5. **Contains at least one claim relevant to the Query.**

You MUST ignore completeness.
You MUST evaluate only the correctness of THIS Single-Row's own claims.

------------------------------------------------------------
## Structural Constraints (Very Important)

1. **Single-Row = One scoring unit**
    - The "Extracted From Rubric" ID in the Single-Row must match exactly one scoring unit in the overall Rubric.

2. **No mixing**
    - The Single-Row must not combine multiple rubric units into one claim.

3. **Strict multi-condition requirement**
    - If the matched Rubric scoring unit contains multiple requirements, **the Single-Row must satisfy ALL of them. Partial fulfillment = label [0].**

4. **"N/A" rule (mandatory)**
    - If the Single-Row contains "N/A", **you must immediately label it as [0], regardless of any other information.**

------------------------------------------------------------
## Distinguishing Requirement Types (CRITICAL)

You MUST determine whether the matched Rubric scoring unit requires:

### A. Factual content
(e.g., a person's name, a date, a fact, an explanation)
→ You MAY search authoritative sources using Playwright MCP tools.

### B. A URL, page link, or reference link
→ You MUST evaluate ONLY the correctness of the link provided.
→ You MUST NOT:
- generate a new link,
- search for the correct link,
- fix the link,
- replace anything missing.

If the Rubric requires a link and the Single-Row does not provide one → label [0].

------------------------------------------------------------
## Verification Procedure

### Step 1 — Identify the Target Rubric Unit
- Locate the scoring unit whose index matches "Extracted From Rubric" in the Single-Row.
- All evaluation must be restricted to the requirements of that scoring unit.

### Step 2 — Trace Source in the Response
- Identify where in the Response the Single-Row was extracted from.
- Confirm the Single-Row content faithfully reflects the Response.

### Step 3 — Evidence Verification (Using Tools)
You MUST:

- Follow all explicit references in the Response that are relevant to the Single-Row, including URLs, footnotes (e.g., `[^1]`, `<sup>1</sup>`), or entries in "Work Cited" / "Key Citations".
- Open referenced pages using Playwright MCP tools.
- Validate every claim in the Single-Row that attempts to satisfy the Rubric.

If Response references are insufficient:
- Only if the Rubric requires *factual content*, you may perform searches.
- If the Rubric requires *a link*, you MUST NOT search for any missing link.

### Step 4 — Handling "Unverifiable"
If a claim remains unverifiable after:
- reviewing all Response references, and
- performing allowed searches,

then mark the claim as **Not verifiable** and assign label [0].

------------------------------------------------------------
## Final Judgment Rules

Label the Single-Row as **[1]** only if:

1. It makes at least one claim relevant to the Query AND
2. Every claim is factually correct AND
3. It satisfies ALL requirements of the matched Rubric scoring unit AND
4. It faithfully represents its source in the Response AND
5. No part of the claim is "N/A".

Otherwise, assign **[0]**.

------------------------------------------------------------
## Output Format (Strict)

You MUST output only:

- Response: [1]

or

- Response: [0]

Nothing else.
