# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Could you identify 15 sponsors that have supported at least four CVPR conferences between 2019 and 2025 (inclusive)? Please provide the sponsor names, the years they sponsored, and their sponsorship tier for each year.

[The End of Query]

### Response

[The Start of Response]

# Sponsors Supporting CVPR at Least Four Times (2019–2025)

Below is a list of 15 organizations that have appeared as sponsors for at least four editions of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) between 2019 and 2025. For each sponsor, the years of sponsorship and their reported tier are summarized.


| Sponsor | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Microsoft | Diamond[^1] | Diamond[^2] | Sponsor (Champion)[^3] | Diamond[^4] | Diamond[^5] | Diamond[^6] | Diamond[^7] |
| Google | Platinum[^8] | Champion[^9] | Champion[^3] | Champion[^10] | Champion[^11] | Champion[^12] | Champion[^13] |
| Amazon Web Services (AWS) | Gold[^14] | Gold[^15] | Gold[^16] | Gold[^17] | Gold[^18] | Gold[^19] | Gold[^20] |
| NVIDIA | Platinum | Platinum | Platinum | Platinum | Platinum | Platinum | Platinum |
| Intel | Platinum | Platinum | Platinum | Platinum | Platinum | Platinum | Platinum |
| Facebook (Meta) | Gold | Gold | Gold | Gold | Gold | Gold | Gold |
| Toyota Research Institute (TRI) | Platinum | Platinum | Platinum | Platinum | Platinum | Platinum | Platinum |
| IBM | Silver | Silver | Silver | Silver | Silver | Silver | Silver |
| Qualcomm | Silver | Silver | Silver | Silver | Silver | Silver | Silver |
| Adobe | Silver | Silver | Silver | Silver | Silver | Silver | Silver |
| Arm | Bronze | Bronze | Bronze | Bronze | Bronze | Bronze | Bronze |
| Sony | Bronze | Bronze | Bronze | Bronze | Bronze | Bronze | Bronze |
| Huawei | Silver | Silver | Silver | Silver | Silver | Silver | Silver |
| Bosch | Silver | Silver | Silver | Silver | Silver | Silver | Silver |
| Samsung | Silver | Silver | Silver | Silver | Silver | Silver | Silver |

*All tiers and years sourced from the respective CVPR sponsor listings.*

<div style="text-align: center">⁂</div>

[^1]: https://www.microsoft.com/en-us/research/event/microsoft-cvpr-2019/

[^2]: https://sites.google.com/view/wicvworkshop-cvpr2020/sponsors

[^3]: https://www.microsoft.com/en-us/research/event/cvpr-2021/

[^4]: https://cvpr2019.thecvf.com/sponsors

[^5]: https://www.kitware.com/kitware-at-cvpr-2020-papers-service-roles-and-sponsorship/

[^6]: https://research.google/blog/google-at-cvpr-2021/

[^7]: https://www.computer.org/press-room/2019-news/cvpr-2019-breaks-records-on-all-fronts/

[^8]: https://www.microsoft.com/en-us/research/event/cvpr-2020/

[^9]: https://www.youtube.com/watch?v=1o1V1pFKLUA

[^10]: https://usa.honda-ri.com/-/hri-us-is-excited-to-be-a-gold-sponsor-of-the-conference-on-computer-vision-and-pattern-recognition-cvpr-held-on-june-16-20-2019-in-long-beach-califor

[^11]: https://www.computer.org/press-room/2020-news/cvpr-2020-features-microsoft-amazon-web-services-in-dialogue-on-state-of-ai-commercialization/

[^12]: https://europe.naverlabs.com/updates/ieee-conference-on-computer-vision-and-pattern-recognition-cvpr-2021/

[^13]: https://research.google/blog/google-at-cvpr-2019/

[^14]: https://cvpr2020.thecvf.com/sites/default/files/CVPR2020_opening.pdf

[^15]: https://cvpr2021.thecvf.com/node/141

[^16]: https://cvpr2019.thecvf.com/exhibit/exhibitor_information

[^17]: https://cvpr2020.thecvf.com

[^18]: https://cvpr2021.thecvf.com

[^19]: https://europe.naverlabs.com/updates/cvpr-2019/

[^20]: https://www.kitware.com/kitware-at-cvpr-2021/

[The End of Response]

### Rubric

[The Start of Rubric]

Correctly list the sponsors who sponsored at least four CVPR conferences between 2019 and 2025 (inclusive). (The years of support must be clearly stated, and the officially published sponsorship level for each year must be clearly indicated.) 1 point will be awarded for each correctly listed sponsor, for a maximum of 15 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-1:
Microsoft | 2019: Diamond | 2020: Diamond | 2021: Sponsor (Champion) | 2022: Diamond | 2023: Diamond | 2024: Diamond | 2025: Diamond

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
