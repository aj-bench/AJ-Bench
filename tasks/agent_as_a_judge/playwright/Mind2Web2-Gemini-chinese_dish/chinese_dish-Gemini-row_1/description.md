# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

I want to cook two delicious Chinese dishes using what I have in my fridge: potatoes, chicken thighs, cilantro, scallions, and cucumbers. Please help me find two recipes that, together, make full use of all these ingredients. It’s okay if the recipes share some ingredients, but they should not be exactly the same.

For each recipe, please:

- List all the required ingredients.
- Specify any additional ingredients and seasonings I need to buy.

Note: The only seasonings I currently have are oil, salt, MSG, soy sauce, and vinegar. And of course, I have water 😊

[The End of Query]

### Response

[The Start of Response]

## The Main Course: Classic Braised Chicken with Potatoes (马铃薯焖鸡, Mǎlíngshǔ Mèn Jī)

### Ingredient Breakdown

The following table provides a clear breakdown of the required components, separating the ingredients available in the kitchen from those that require a trip to the store. This separation simplifies the logistical planning for the home chef.

Table 1: Braised Chicken with Potatoes: Ingredient List

| Ingredients from Your Fridge | Additional Ingredients to Purchase |
| :---- | :---- |
| Chicken Thighs | Ginger |
| Potatoes | Garlic |
| Scallions | Cornstarch |
| Oil | Dark Soy Sauce (optional) |
| Salt | Sugar |
| MSG | Water |
| Soy Sauce |  |

Data compiled from source 1, 3, 4, 5.

## The Side Dish: Aromatic Smashed Cucumber Salad (拍黄瓜, Pāi Huángguā)

### Ingredient Breakdown

The following table confirms that this recipe completes the utilization of all five core ingredients, while also specifying the additional items needed.

Table 2: Smashed Cucumber Salad: Ingredient List

| Ingredients from Your Fridge | Additional Ingredients to Purchase |
| :---- | :---- |
| Cucumbers | Garlic |
| Cilantro | Sugar |
| Scallions | Sesame Oil |
| Salt | Sesame Seeds (optional) |
| Oil | Chili Oil (optional) |
| Soy Sauce |  |
| Vinegar |  |
| MSG (optional) |  |

Data compiled from source 6, 8, 9.

#### Works cited

1. Xinjiang Cuisine - Big Plate Chicken Recipe (Dapanji) - Reddit, https://www.reddit.com/r/recipes/comments/i7vv1b/xinjiang_cuisine_big_plate_chicken_recipe_dapanji/  
2. Xinjiang Da Pan Ji 大盘鸡 (Big Plate Chicken Recipe) - YouTube, https://www.youtube.com/watch?v=1MXNP1710AM  
3. Braised chicken and potatoes 薯仔焖鸡 (Cantonese style) - YouTube, https://www.youtube.com/watch?v=ol4DM-BYNrI&pp=0gcJCfwAo7VqN5tD  
4. Braised Chicken with Potatoes - Singapore - Eat What Tonight, https://eatwhattonight.com/2021/02/braised-chicken-with-potatoes/  
5. Chinese Style Potato Chicken. (Hor Lan Shu ... - Table for 2.... or more, https://wendyinkk.blogspot.com/2008/02/chinese-style-potato-chicken-hor-lan.html  
6. Asian Cucumber Salad Recipe: Fresh + Spicy | Unpeeled Journal, https://unpeeledjournal.com/spicy-asian-cucumber-salad-recipe/  
7. Asian Cucumber Salad {So Cool} - Two Peas & Their Pod, https://www.twopeasandtheirpod.com/asian-cucumber-salad/  
8. I made some Smashed Cucumber Salad - 拍黄瓜 : r/chinesefood - Reddit, https://www.reddit.com/r/chinesefood/comments/vknnxj/i_made_some_smashed_cucumber_salad_%E6%8B%8D%E9%BB%84%E7%93%9C/  
9. Smashed Cucumber Salad Recipe - Allrecipes, https://www.allrecipes.com/recipe/258377/smashed-cucumber-salad/

[The End of Response]

### Rubric

[The Start of Rubric]

1. Provide two Chinese cuisine recipes. The combined ingredients of the two recipes must cover potatoes, chicken thighs, cilantro, scallions, and cucumbers. The ingredients required for each recipe can partially overlap but must not be identical. Each valid recipe is worth 1 point, for a total of up to 2 points.
2. Award 1 point for listing all the essential ingredients for each provided recipe, with a maximum of 2 points.
3. Award 1 point for listing other ingredients (excluding potatoes, chicken thighs, cilantro, scallions, and cucumbers) and seasonings (excluding oil, salt, monosodium glutamate (MSG), soy sauce, vinegar, and water) that need to be purchased for each provided recipe, with a maximum of 2 points.
4. Total score: 6 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-1:
Classic Braised Chicken with Potatoes (马铃薯焖鸡, Mǎlíngshǔ Mèn Jī)

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
