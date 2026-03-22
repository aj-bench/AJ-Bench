# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Identify five ancient Chinese objects from the Cleveland Museum of Art's collection that dated entirely to 2000 BCE or earlier, as listed on the museum's official website. For each object, provide its name, period, estimated date range, and overall dimensions. If an object is not on display, please indicate that as well.

[The End of Query]

### Response

[The Start of Response]

# Five Ancient Chinese Objects at CMA Dated to 2000 BCE or Earlier

**Main Takeaway:**
These five Neolithic-period objects, all dating entirely to 2000 BCE or earlier, highlight the technical mastery and ritual significance of early Chinese artisans. Three are on display in gallery 241A, while two are not currently on view.

***

## Jar with Spiral Designs

- Period: Neolithic period, Majiayao culture, Majiayao phase (Northwest China)
- Date: 3300 – 2650 BCE[^1]
- Dimensions: Diameter 39.1 cm; Overall height 45.2 cm[^1]
- Display: Gallery 241A, Arts of Ancient China[^1]

***

## Jar with Curvilinear Designs

- Period: Neolithic period, Majiayao culture, Banshan phase (Northwest China)
- Date: 2650 – 2350 BCE[^2]
- Dimensions: Diameter 36.8 × 30.5 cm; Overall height 36.2 cm[^2]
- Display: Gallery 241A, Arts of Ancient China[^2]

***

## Bird-shaped Urn

- Period: Neolithic period, Majiayao culture, Banshan phase (Northwest China)
- Date: 2650 – 2350 BCE[^3]
- Dimensions: Overall 26.7 × 31.1 × 27.9 cm[^3]
- Display: Gallery 241A, Arts of Ancient China[^3]

***

## Ceremonial Disc (Bi)

- Period: Neolithic period, Liangzhu culture (East China)
- Date: 3300 – 2200 BCE[^4]
- Dimensions: Diameter 32 cm; Thickness 1 cm; Inner diameter 5.4 cm[^4]
- Display: Not on view[^4]

***

## Perforated Disc (Pi)

- Period: Neolithic period (China)
- Date: 3000 – 2000 BCE[^5]
- Dimensions: Diameter 23.5 cm; Inner diameter 7 cm[^5]
- Display: Not on view[^5]
<span style="display:none">[^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^20][^21][^22][^23][^24][^6][^7][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://www.clevelandart.org/print/art/2004.64

[^2]: https://www.clevelandart.org/art/1930.332

[^3]: https://www.clevelandart.org/art/2007.276

[^4]: https://www.clevelandart.org/art/1917.974

[^5]: https://www.clevelandart.org/print/art/1915.627

[^6]: http://epaper.chinadaily.com.cn/a/202403/05/WS65e6546ea310df4030f4fd8e.html

[^7]: https://www.clevelandart.org/art/2020.86

[^8]: https://www.clevelandart.org/print/art/1952.567

[^9]: https://hypebeast.com/2023/9/cleveland-museum-of-art-china-southern-paradist-exhibition

[^10]: https://www.clevelandart.org/art/1962.44

[^11]: https://www.clevelandart.org/art/1991.78.2

[^12]: https://www.clevelandart.org/about-collection/collection-areas/chinese-art

[^13]: https://www.clevelandart.org/art/1962.281

[^14]: https://diluo.digital.conncoll.edu/Asianart/uncategorized/jades-translucency-through-time/

[^15]: https://www.clevelandart.org/art/1960.288

[^16]: https://asia-archive.si.edu/learn/for-educators/teaching-china-with-the-smithsonian/explore-by-object/pendant-in-the-form-of-a-mask/

[^17]: https://www.clevelandart.org/print/art/1938.9

[^18]: https://www.clevelandart.org/art/1915.673

[^19]: https://www.clevelandart.org/print/art/2009.83

[^20]: https://www.clevelandart.org/art/1915.628

[^21]: https://www.clevelandart.org/print/art/1953.628

[^22]: https://www.clevelandart.org/print/art/1915.628

[^23]: https://www.clevelandart.org/art/2004.64

[^24]: https://www.clevelandart.org/art/2009.83

[The End of Response]

### Rubric

[The Start of Rubric]

1. Locate and list the names of five ancient Chinese objects from the Cleveland Museum of Art's official website that date entirely from 2000 BCE or earlier. 1 point for each object listed, maximum 5 points.
2. For each of the five objects listed above:
   - Accurately state its specific period: 1 point
   - Provide its approximate date range: 1 point
   - State its overall dimensions: 1 point
   - If the artifact is not currently on display, clearly indicate this: 1 point
   Maximum score: 20 points
3. Total possible points are 25 points

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-2:
3000 – 2000 BCE

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
