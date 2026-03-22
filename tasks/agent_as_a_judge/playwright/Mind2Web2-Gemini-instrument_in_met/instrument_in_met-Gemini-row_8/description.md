# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

I am currently researching string instruments from East Asia dating from the 19th century or earlier. Can you find five examples that are on display at the Met in New York City, and provide the link to each instrument’s page on the Met Collection website?

[The End of Query]

### Response

[The Start of Response]

# Curated Instrument Data and Collection Links

The following table provides a summary of the five East Asian string instruments analyzed in this report, including their culture of origin, date, current gallery location, museum object number, and a direct link to their respective pages on The Metropolitan Museum of Art's collection website.

| Instrument Name | Culture of Origin | Date of Creation | Met Gallery Location | Met Object Number | Direct Collection URL |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **Guqin (古琴)** | Chinese | 1634 | The Met Fifth Avenue in Gallery 684 | 1999.93a-b | [https://www.metmuseum.org/art/collection/search/503523](https://www.metmuseum.org/art/collection/search/503523) |
| **Sanxian (三弦)** | Chinese | 19th century | The Met Fifth Avenue in Gallery 681 | 89.4.38 | [https://www.metmuseum.org/art/collection/search/500615](https://www.metmuseum.org/art/collection/search/500615) |
| **Shamisen** | Japanese | 19th century | The Met Fifth Avenue in Gallery 681 | 1990.129.5 | [https://www.metmuseum.org/art/collection/search/503799](https://www.metmuseum.org/art/collection/search/503799) |
| **Pipa (琵琶)** | Chinese | late 16th–early 17th century | The Met Fifth Avenue in Gallery 684 | 50.145.74 | [https://www.metmuseum.org/art/collection/search/503651](https://www.metmuseum.org/art/collection/search/503651) |
| **Pipa (琵琶)** | Chinese | 19th century | The Met Fifth Avenue in Gallery 681 | 89.4.52 | [https://www.metmuseum.org/art/collection/search/500625](https://www.metmuseum.org/art/collection/search/500625) |

## Works cited

1. Musical Instruments - The Metropolitan Museum of Art, https://www.metmuseum.org/departments/musical-instruments  
2. Geomungo | Korean | Joseon dynasty (1392-1910) | The ..., https://www.metmuseum.org/art/collection/search/500725  
3. Meet Musical Instruments at The Met! - The Metropolitan Museum of Art, https://www.metmuseum.org/perspectives/meet-musical-instruments-galleries-families  
4. Prince Lu - Guqin (古琴 ) - Chinese - Ming Dynasty - The ..., https://www.metmuseum.org/art/collection/search/503523  
5. Guqin (古琴 ) | Chinese - The Metropolitan Museum of Art, https://www.metmuseum.org/art/collection/search/506800  
6. Sanxian (三弦 ) | Chinese | Qing dynasty (1644-1911) | The ..., https://www.metmuseum.org/art/collection/search/500615  
7. Shamisen - Japanese - The Metropolitan Museum of Art, https://www.metmuseum.org/art/collection/search/503799  
8. Pipa (琵琶 ) - Chinese - Ming dynasty (1368-1644) - The Metropolitan Museum of Art, https://www.metmuseum.org/art/collection/search/503651  
9. The Pipa - The Metropolitan Museum of Art, https://www.metmuseum.org/essays/the-pipa  
10. Jiu-cheng | Pipa (琵琶 ) | Chinese | The Metropolitan Museum of Art, https://www.metmuseum.org/art/collection/search/500625

[The End of Response]

### Rubric

[The Start of Rubric]

1. Correctly identify East Asian stringed instruments from the 19th century or earlier on display at The Metropolitan Museum of Art (New York). You will receive 1 point for each eligible instrument found, with a maximum of 5 points.
2. You will receive 1 point for each valid link corresponding to the aforementioned eligible instruments, with a maximum of 5 points. All links must be page links from the Met Collection website.
3. The full score is 10 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-2:
https://www.metmuseum.org/art/collection/search/503799

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
