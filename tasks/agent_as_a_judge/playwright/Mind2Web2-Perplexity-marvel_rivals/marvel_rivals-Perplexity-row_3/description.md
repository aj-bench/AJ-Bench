# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Marvel Rivals is a video game featuring iconic Marvel characters, each with a unique set of abilities.

Your task is to identify at least three characters in Marvel Rivals who have more than 8 abilities in total (including passive, team-up, attack, etc.). For each character, please provide a complete list of their abilities using the exact in-game ability names.

[The End of Query]

### Response

[The Start of Response]

# Marvel Rivals Characters with More Than Eight Abilities

Below are three Marvel Rivals heroes whose kits exceed eight total abilities, including passives and team-up skills. All ability names are taken verbatim from the in-game listings.

## Hawkeye

- Piercing Arrow
- Blast Arrow
- Hunter’s Sight
- Crescent Slash
- Hypersonic Arrow
- Ronin Slash
- Skyward Leap
- Archer’s Focus
- Supersensory Vision (Team Up)[^1]


## Iron Fist

- Iron Fist
- Yat Jee Chung Kuen
- Living Chi
- K’un-Lun Kick
- Harmony Recovery
- Crane Leap
- Dragon’s Defense
- Wall Runner
- Chi Absorption
- Dragon’s Chill (Team Up)[^1]


## Spider-Man

- Spider-Power
- Web-Cluster
- Spectacular Spin
- Web-Swing
- Get Over Here!
- Amazing Combo
- Thwip and Flip
- Spider-Sense
- Suit Expulsion (Team Up)
- Extra Web-Fluid (Team Up)[^1]
<span style="display:none">[^10][^2][^3][^4][^5][^6][^7][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://marvelrivals.wiki.fextralife.com/Hero+Abilities

[^2]: https://www.youtube.com/watch?v=-123nVXXTQ8

[^3]: https://esports.gg/news/marvel-rivals/all-marvel-rivals-characters-and-their-abilities/

[^4]: https://www.reddit.com/r/GamingLeaksAndRumours/comments/1cnpjdw/full_abilities_of_the_marvel_rivals_characters/

[^5]: https://www.rockpapershotgun.com/marvel-rivals-characters-roster

[^6]: https://www.marvelrivals.com/heroes/

[^7]: https://marvelrivals.fandom.com/wiki/Heroes

[^8]: https://www.reddit.com/r/marvelrivals/comments/1hsdlfl/i_made_full_detailed_character_guides_for_marvel/

[^9]: https://www.youtube.com/watch?v=bbc3rUZxz1c

[^10]: https://www.polygon.com/marvel-rivals-guide/491013/team-up-abilities-list-all/

[The End of Response]

### Rubric

[The Start of Rubric]

1. Identify characters in Marvel Rivals with more than 8 skills (including passive, party, and attack skills). 1 point is awarded for identifying 3 or more characters, up to a maximum of 3 points.
2. Provided that point 1 is met, 1 point is awarded for providing a complete skill list for each character (using in-game skill names), up to a maximum of 3 points.
3. Total: 6 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-1:
Spider-Man

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
