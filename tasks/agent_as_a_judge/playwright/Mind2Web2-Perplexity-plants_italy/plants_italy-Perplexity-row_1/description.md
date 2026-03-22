# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Please identify two plant species with distinct genera that are originally native to regions in Africa, Asia, or the Americas, and have later been introduced to Italy. What are their scientific names? Then for each species, provide a link to its distribution information on Plants of the World Online. Please also provide links to Wikipedia articles about the genera of the two plant species.

[The End of Query]

### Response

[The Start of Response]

# Plant Species Introduced to Italy

**Lantana camara**
Scientific name: *Lantana camara*
– Distribution on Plants of the World Online: https://powo.science.kew.org/taxon/325686-2
– Genus (Wikipedia): https://en.wikipedia.org/wiki/Lantana

**Ailanthus altissima**
Scientific name: *Ailanthus altissima*
– Distribution on Plants of the World Online: https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:120045-2
– Genus (Wikipedia): https://en.wikipedia.org/wiki/Ailanthus
<span style="display:none">[^1][^10][^11][^12][^13][^14][^15][^16][^17][^18][^2][^3][^4][^5][^6][^7][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11767948/

[^2]: https://www.cabidigitallibrary.org/doi/full/10.1079/cabicompendium.3889

[^3]: https://portal.wiktrop.org/species/show/186

[^4]: https://en.wikipedia.org/wiki/Ailanthus_altissima

[^5]: https://www.inaturalist.org/guide_taxa/495182

[^6]: https://www.nature.com/articles/s41598-023-41607-2

[^7]: https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0035565

[^8]: https://iforest.sisef.org/contents/?id=ifor0693-006

[^9]: https://powo.science.kew.org/taxon/325686-2

[^10]: https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:813521-1

[^11]: https://www.maltawildplants.com/SIMR/Ailanthus_altissima.php

[^12]: https://www.youtube.com/watch?v=59ntNUCUCLk

[^13]: https://pfaf.org/user/Plant.aspx?LatinName=Ailanthus+altissima

[^14]: https://www.missouribotanicalgarden.org/PlantFinder/PlantFinderDetails.aspx?kempercode=a847

[^15]: https://www.nature.org/en-us/about-us/where-we-work/united-states/indiana/stories-in-indiana/journey-with-nature--tree-of-heaven/

[^16]: https://www.michigan.gov/invasives/id-report/plants/trees/tree-of-heaven

[^17]: http://powo.science.kew.org/results?q=Ailanthus

[^18]: https://www.fs.usda.gov/database/feis/plants/tree/ailalt/all.html

[The End of Response]

### Rubric

[The Start of Rubric]

1. Identify plants that are native to Africa, Asia, or the Americas and were later introduced to Italy. Award 1 point for each scientific name of a plant belonging to a different genus, with a maximum of 2 points.
2. Award 1 point for each link to the distribution information of the identified plant species on Plants of the World Online, with a maximum of 2 points.
3. Award 1 point for each link to the Wikipedia article of the genus of the identified plant species, with a maximum of 2 points.
4. Total score: 6 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-1:
Lantana camara

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
