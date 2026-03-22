# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Could you find three brands that have each won a Hypebeast HypeAward or Hypebeast100 Award (excluding Best Sneaker and Best Collab) at least twice from 2020 to 2025? Please list the years each brand received the award and the categories they won.

[The End of Query]

### Response

[The Start of Response]

# Architects of Acclaim: An Analysis of Repeat Winners in the Hypebeast Awards (2020-2024)

## Introduction: Hypebeast as a Cultural Barometer

A meticulous analysis of the Hypebeast Awards from the 2020 through 2024 cycles reveals a compelling narrative about the nature of sustained industry leadership. Within the user-specified parameters—at least two award wins in categories other than "Best Sneaker" or "Best Collab"—two brands emerge as definitive repeat victors: Louis Vuitton and New Balance. Their consecutive wins in their respective categories for 2020 and 2021 stand as a testament to exceptionally well-executed, long-term strategic visions that captured and defined the era.

The inability to identify a third brand that meets these stringent criteria from the available documentation is, in itself, a crucial finding.

## The Reign of a Redefined Maison: Louis Vuitton's Dominance in Menswear

### Summary of Accolades

| Year | Award Category | Source Snippet(s) |
| :---- | :---- | :---- |
| 2020 | Best Menswear Brand | 3 |
| 2021 | Best Menswear Brand | 2 |

## The Quiet Champion: New Balance's Strategic Ascent in Footwear

### Summary of Accolades

| Year | Award Category | Source Snippet(s) |
| :---- | :---- | :---- |
| 2020 | Best Footwear Brand | 3 |
| 2021 | Best Footwear Brand | 2 |

## The Field of Contenders: An Examination of Single Victories and Data Gaps

### The Elusive Third Winner: A Finding on Market Volatility

A rigorous review of the provided documentation confirms that no other brand won two or more Hypebeast Awards in the specified, non-excluded categories between 2020 and 2024. One structural factor contributing to this finding is the evolution of the Hypebeast100 Awards' format. The 2023 announcement, for instance, presented a collective of honorees—Stüssy, Sandy Liang, ASICS, Carhartt x sacai, and Wales Bonner x adidas Samba—rather than assigning a distinct, named award category to each winner in its primary press release.<sup>1</sup> While a separate report did clarify that Sandy Liang won "Best Womenswear Brand," the broader format of that year makes direct year-over-year comparisons for other brands more challenging.<sup>5</sup>

#### Works cited

1. Hypebeast 100 2023: this year's list of the most accomplished creatives, https://hypebeast.com/newsroom/hypebeast100-2023-this-years-list-of-the-most-accomplished-creatives  
2. HB100 2021 - Hypebeast, https://hypebeast.com/hb100/2021/awards  
3. HB100 2020 - Hypebeast, https://hypebeast.com/hb100/2020/awards  
4. Hypebeast100 2022 | Hypebeast, https://hypebeast.com/hb100/2022/awards  
5. Sandy Liang and Yoon Star in Hypebeast 100 2023 | Hypebae, https://hypebae.com/2023/12/sandy-liang-feng-chen-wang-yoon-ahn-hypebeast-100-list  
6. Peggy Gou and Rihanna Star in Hypebeast 100 2024 | Hypebae, https://hypebae.com/2024/12/hypebeast-100-nicole-mclaughlin-rihanna-peggy-gou-the-row  
7. Jonathan Anderson Named Designer of the Year and Balenciaga Recruits Nicole Kidman in This Week's Top Fashion News - Hypebeast, https://hypebeast.com/2023/12/top-fashion-news-jonathan-anderson-designer-year-nicole-kidman-balenciaga-nigo-supreme

[The End of Response]

### Rubric

[The Start of Rubric]

1. Correctly identify three brands that have won the Hypebeast HypeAward or Hypebeast 100 Award at least twice between 2020 and 2025 (excluding Best Sneaker and Best Collab categories). Award 1 point for each correct brand identified, up to 3 points.
2. Provide the corresponding award years for the three qualifying brands. Award 1 point for each brand only if all its corresponding award years are correct. In other words, if a brand has two award years and one is incorrect, no point is awarded. Maximum 3 points.
3. Provide the corresponding award categories for the three qualifying brands. Award 1 point for each brand only if all its corresponding award categories are correct. In other words, if a brand has two award categories and one is incorrect, no point is awarded. Maximum 3 points.
4. The maximum score for content dimension is 9 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-1:
Louis Vuitton

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
