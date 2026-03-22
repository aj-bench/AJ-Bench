# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Find 3 movies that premiered in 2024 and had matching theatrical release dates in both mainland China and the United States. For each movie, clearly provide the title, the shared theatrical release date, and credible source links (such as IMDb or official news articles) explicitly confirming these theatrical release dates. Consider only official theatrical release dates—exclude film festival premieres, limited screenings, digital releases, special events, or any other non-standard releases.

[The End of Query]

### Response

[The Start of Response]

# Definitive Findings: Verified Movies with Identical US-China Theatrical Release Dates in 2024

Based on a meticulous review of the available sources, three films from 2024 had matching theatrical release dates in both the United States and mainland China. This section presents a definitive list of these films, complete with their shared release date and the corresponding source verification.

## Movie 1: The Beekeeper

- Shared Theatrical Release Date: January 12, 2024
- Source Verification: The action thriller The Beekeeper opened in the United States on January 12, 2024, as confirmed by a Box Office Mojo entry for the film's domestic release.<sup>1</sup> This date is further corroborated by its Wikipedia page.<sup>2</sup> The film also had its theatrical release in mainland China on the very same day, January 12, 2024.<sup>3</sup>

## Movie 2: Godzilla x Kong: The New Empire

- Shared Theatrical Release Date: March 29, 2024
- Source Verification: This MonsterVerse film had its wide theatrical release in the United States on March 29, 2024, a date confirmed by multiple sources, including its Wikipedia entry <sup>5</sup> and a report from The Numbers.<sup>6</sup> The film also premiered in mainland China on the exact same date. This is explicitly verified by Box Office Mojo's data for the Chinese market <sup>4</sup> and a dedicated page on The Numbers for its China release.<sup>6</sup>

## Movie 3: Deadpool & Wolverine

- Shared Theatrical Release Date: July 26, 2024
- Source Verification: The superhero film Deadpool & Wolverine was theatrically released in the United States on July 26, 2024, as documented in its Wikipedia page.<sup>7</sup> The film's premiere in mainland China also took place on this shared date, a fact confirmed by a YouTube video covering the film's press tour in Shanghai <sup>8</sup> and a fan community post on Reddit that cites news reports about the film's Chinese regulatory approval.<sup>9</sup> The successful day-and-date release of an R-rated film is particularly noteworthy, despite the requirement for "some cuts" to secure its approval in China.<sup>9</sup>

---

## Table 1: 2024 Synchronized US-China Theatrical Releases

| Movie Title | Shared Release Date | U.S. Source | China Source |
| :---- | :---- | :---- | :---- |
| The Beekeeper | January 12, 2024 | 1 | 3 |
| Godzilla x Kong: The New Empire | March 29, 2024 | 5 | 4 |
| Deadpool & Wolverine | July 26, 2024 | 7 | 8 |

### Works cited

1. The Beekeeper - Box Office Mojo, https://www.boxofficemojo.com/release/rl1465155585/  
2. en.wikipedia.org, https://en.wikipedia.org/wiki/The_Beekeeper_(2024_film)  
3. The Beekeeper - Box Office Mojo, https://www.boxofficemojo.com/releasegroup/gr4020130309/  
4. Chinese Box Office For 2024 - Box Office Mojo, https://www.boxofficemojo.com/year/2024/?area=CN  
5. Godzilla x Kong: The New Empire - Wikipedia, https://en.wikipedia.org/wiki/Godzilla_x_Kong:_The_New_Empire  
6. China Box Office for Godzilla x Kong: The New Empire (哥斯拉大战 ..., https://www.the-numbers.com/movie/Godzilla-x-Kong-The-New-Empire-(2024)/China  
7. en.wikipedia.org, https://en.wikipedia.org/wiki/Deadpool_%26_Wolverine  
8. Deadpool & Wolverine (2024) China Press Tour 'Fan Event' - YouTube, https://www.youtube.com/watch?v=zqYru1LZ_4Q  
9. Deadpool & Wolverine got the Chinese regulators blessing and and will debut in China's box office on July 26 : r/MarvelStudios_Rumours - Reddit, https://www.reddit.com/r/MarvelStudios_Rumours/comments/1dhnzlr/deadpool_wolverine_got_the_chinese_regulators/

[The End of Response]

### Rubric

[The Start of Rubric]

1. Identify films that premiered in 2024 and had consistent theatrical release dates in both mainland China and the United States. Award 1 point for each qualifying film identified, up to a maximum of 3 points.
2. For each identified film, provide the corresponding title, its official theatrical release date in both mainland China and the United States(considering only the official release date), and a reliable source link (e.g., IMDb or official news report) that clearly confirms these theatrical release dates. Award 1 point for each complete and correct set of information provided per film, up to a maximum of 3 points.
3. The maximum total score is 6 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-1:
The Beekeeper

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
