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

# Recommended Chinese Recipes

**Main Takeaway:**
To make full use of your potatoes, chicken thighs, cilantro, scallions, and cucumbers in two distinct dishes, prepare (1) a refreshing Sichuan–style smashed cucumber salad and (2) a savory braised chicken–potato stew. Both recipes draw on your existing seasonings—oil, salt, MSG, soy sauce, and vinegar—and call for a handful of additional ingredients.

***

## 1. Sichuan-Style Smashed Cucumber Salad

### Ingredients

- Cucumbers (2 medium)
- Scallions (2, white and light-green parts only)
- Cilantro (a small handful)


### Seasonings \& Pantry Items (you already have)

- Oil
- Salt
- MSG
- Soy sauce
- Vinegar
- Water (for rinsing and light dressing dilution)


### Additional Ingredients to Buy

- Garlic (2 cloves)
- Chili oil (1½ tbsp)
- Sugar (1 tsp)


### Preparation Steps

1. **Prep the vegetables:**
    - Rinse cucumbers, scallions, and cilantro.
    - Smash cucumbers with the side of a knife, then cut into 2–3 inch pieces.
    - Slice scallions thinly. Chop cilantro coarsely.
2. **Make the dressing:**
In a small bowl, mix 1½ tbsp chili oil, 1 tsp sugar, 1 tbsp soy sauce, 1 tbsp vinegar, a pinch of salt, and a pinch of MSG. Add 1 tbsp water if it seems too intense.
3. **Assemble:**
Toss cucumbers, scallions, and cilantro with the dressing. Serve chilled or at room temperature.

***

## 2. Chinese-Style Braised Chicken Thighs with Potatoes

### Ingredients

- Chicken thighs (4 pieces, bone-in or boneless)
- Potatoes (2 large, peeled and cut into chunks)
- Scallions (2, white and light-green parts, cut into 2-inch lengths)
- Cilantro (to garnish)


### Seasonings \& Pantry Items (you already have)

- Oil
- Salt
- MSG
- Soy sauce
- Vinegar
- Water (for braising liquid)


### Additional Ingredients to Buy

- Garlic (3 cloves)
- Ginger (1 inch piece)
- Shaoxing cooking wine (2 tbsp)
- Sugar (1 tbsp)
- Star anise (1–2 pieces)


### Preparation Steps

1. **Brown the chicken:**
    - Heat 1 tbsp oil in a wok or deep skillet over medium heat.
    - Lightly season chicken with salt and MSG. Sear both sides until golden; remove and set aside.
2. **Aromatics:**
    - In the same pan, add 1 tbsp oil. Sauté sliced garlic and julienned ginger until fragrant (about 30 sec).
3. **Deglaze \& braise:**
    - Return chicken to the pan. Add 2 tbsp soy sauce, 2 tbsp Shaoxing wine, 1 tbsp sugar, and 1–2 star anise.
    - Pour in enough water to come halfway up the chicken; bring to a simmer.
4. **Add potatoes:**
    - After 10 min of simmering, add potato chunks.
    - Continue to braise until potatoes are tender and sauce has thickened, about 15–20 min.
5. **Finish \& garnish:**
    - Stir in scallion segments, cook 1 min more.
    - Transfer to a serving dish and sprinkle with chopped cilantro.

***

**Shopping List for Both Recipes**

- Garlic (5 cloves)
- Sugar (1 tbsp + 1 tsp)
- Chili oil (1½ tbsp)
- Ginger (1 inch)
- Shaoxing cooking wine (2 tbsp)
- Star anise (1–2 pieces)

Enjoy your meal!

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

Extracted From Rubric-3:
Garlic (2 cloves)\nChili oil (1½ tbsp)\nSugar (1 tsp)

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
