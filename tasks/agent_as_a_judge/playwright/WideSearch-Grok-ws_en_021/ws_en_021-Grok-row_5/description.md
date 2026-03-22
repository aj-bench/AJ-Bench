# Agent-as-a-Judge Task

You will verify the factual correctness of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Could you provide a detailed list of Michelin three-star restaurants in Paris, France as of December 31, 2024? I especially want to know the name, main cuisine style, exact address of each restaurant and the official link.

Please organize the results in one Markdown table with the following columns:
Restaurant, Main Cuisine Style, Address, Official Link

[The End of Query]

### Response

[The Start of Response]

| Restaurant | Main Cuisine Style | Address | Official Link |
|------------|--------------------|---------|---------------|
| Plénitude - Cheval Blanc Paris | Creative | 8 quai du Louvre, Paris, 75001, France | [https://www.chevalblanc.com/en/maison/paris/restaurants-and-bars/plenitude/](https://www.chevalblanc.com/en/maison/paris/restaurants-and-bars/plenitude/) |
| L'Ambroisie | Classic Cuisine | 9 place des Vosges, Paris, 75004, France | [https://www.ambroisie-paris.com/](https://www.ambroisie-paris.com/) |
| Kei | Modern Cuisine, Creative | 5 rue Coq-Héron, Paris, 75001, France | [https://restaurant-kei.fr/en](https://restaurant-kei.fr/en) |
| Arpège | Creative | 84 rue de Varenne, Paris, 75007, France | [https://www.alain-passard.com/en/](https://www.alain-passard.com/en/) |
| Alléno Paris au Pavillon Ledoyen | Creative | 8 avenue Dutuit, Paris, 75008, France | [https://www.yannick-alleno.com/en/restaurants-reservation/restaurant-3-etoiles-paris.html](https://www.yannick-alleno.com/en/restaurants-reservation/restaurant-3-etoiles-paris.html) |
| Le Gabriel - La Réserve Paris | Modern Cuisine | 42 avenue Gabriel, Paris, 75008, France | [https://www.lareserve-paris.com/en/restaurants-bars/restaurant-le-gabriel/](https://www.lareserve-paris.com/en/restaurants-bars/restaurant-le-gabriel/) |
| Épicure | Modern Cuisine | 112 rue du Faubourg-Saint-Honoré, Paris, 75008, France | [https://www.oetkerhotels.com/hotels/le-bristol-paris/restaurants-bar/epicure/](https://www.oetkerhotels.com/hotels/le-bristol-paris/restaurants-bar/epicure/) |
| Le Cinq | Modern Cuisine | 31 avenue George-V, Paris, 75008, France | [https://www.fourseasons.com/paris/dining/restaurants/le_cinq/](https://www.fourseasons.com/paris/dining/restaurants/le_cinq/) |
| Pierre Gagnaire | Creative | 6 rue Balzac, Paris, 75008, France | [https://pierregagnaire-lerestaurant.com/en](https://pierregagnaire-lerestaurant.com/en) |
| Le Pré Catelan | Creative, Contemporary | Route de Suresnes - bois de Boulogne, Paris, 75016, France | [https://leprecatelan.paris/](https://leprecatelan.paris/) |

### Key Citations
-  Paris 3 Stars MICHELIN Restaurants - https://guide.michelin.com/us/en/ile-de-france/paris/restaurants/3-stars-michelin
-  List of Michelin 3-star restaurants - Wikipedia - https://en.wikipedia.org/wiki/List_of_Michelin_3-star_restaurants
-  Michelin 3-Star Restaurants | 2024 - Paris Insiders Guide - https://www.parisinsidersguide.com/michelin-3-star-restaurants-paris.html
-  Plénitude - Cheval Blanc Paris – Paris - a MICHELIN Guide Restaurant - https://guide.michelin.com/en/ile-de-france/paris/restaurant/plenitude-cheval-blanc-paris
-  L'Ambroisie – Paris - a MICHELIN Guide Restaurant - https://guide.michelin.com/en/ile-de-france/paris/restaurant/l-ambroisie
-  Kei – Paris - a MICHELIN Guide Restaurant - https://guide.michelin.com/en/ile-de-france/paris/restaurant/kei
-  Arpège – Paris - a MICHELIN Guide Restaurant - https://guide.michelin.com/en/ile-de-france/paris/restaurant/arpege
-  Alléno Paris au Pavillon Ledoyen – Paris - a MICHELIN Guide Restaurant - https://guide.michelin.com/en/ile-de-france/paris/restaurant/alleno-paris-au-pavillon-ledoyen
-  Épicure – Paris - a MICHELIN Guide Restaurant - https://guide.michelin.com/en/ile-de-france/paris/restaurant/epicure
-  Le Pré Catelan – Paris - a MICHELIN Guide Restaurant - https://guide.michelin.com/en/ile-de-france/paris/restaurant/le-pre-catelan
-  Restaurant Le Gabriel | 3 Michelin Star Restaurant in Paris - https://www.lareserve-paris.com/en/restaurants-bars/restaurant-le-gabriel/
-  Restaurant Pierre Gagnaire - https://pierregagnaire-lerestaurant.com/en
-  Le Cinq | Michelin-Star Restaurant Paris | Fine Dining in Paris - https://www.fourseasons.com/paris/dining/restaurants/le_cinq/

[The End of Response]

### Single-Row (One extracted item)

[The Start of Single-Row]

| Restaurant | Main Cuisine Style | Address | Official Link |
|------------|--------------------|---------|---------------|
| Alléno Paris au Pavillon Ledoyen | Creative | 8 avenue Dutuit, Paris, 75008, France | [https://www.yannick-alleno.com/en/restaurants-reservation/restaurant-3-etoiles-paris.html](https://www.yannick-alleno.com/en/restaurants-reservation/restaurant-3-etoiles-paris.html) |

[The End of Single-Row]

------------------------------------------------------------
## Core Principle

Your task is NOT to evaluate whether the Single-Row answers the entire Query. Your task IS ONLY to evaluate whether THIS Single-Row:

1. Correctly reflects the part of the Response it was extracted from;
2. Is factually correct according to verification tools.

You MUST ignore completeness. You MUST evaluate only the correctness of THIS Single-Row's own claims.

------------------------------------------------------------
## Role and High-Level Objective

Act as a neutral, impartial judge. All factual checks must be performed using Playwright MCP tools.

------------------------------------------------------------
## Step-by-Step Evaluation Procedure

### Step 1 — Initial Read
- Read the Query, Response, and Single-Row fully.

### Step 2 — Trace Source in the Response
- Locate the corresponding content in the Response.
- Confirm the Single-Row faithfully reflects the Response.

### Step 3 — Verify Each Claim Individually with Playwright MCP Tools
- Focus strictly on content relevant to the Query.
- Do not let style, language, or level of detail influence judgment.
- Treat "N/A", "NA", or "Data Unavailable" as problematic unless explicitly allowed.
- Follow explicit references in the Response: URLs, citations, or footnotes (e.g., `[^1]`, `<sup>1</sup>`).
- Open referenced pages with Playwright MCP tools and locate supporting evidence.
- Primarily rely on references in the Response; if none exist, search authoritative sources using the tools.
- If a reference is unreachable, paywalled, or does not support the claim, mark accordingly.
- Verify every field if the item contains multiple attributes (e.g., in a table row).
- Numeric values must strictly match authoritative sources—no tolerance allowed.

### Step 4 — Record Verification Results
For every claim in the Single-Row record:
- Supported / Contradicted / Not verifiable

------------------------------------------------------------
## Final Judgment Rules

A Single-Row is labeled **[1]** ONLY IF:
1. It contains at least one claim relevant to the Query; AND
2. Every claim is factually correct; AND
3. It faithfully represents the Response.

Otherwise, assign **[0]**.

### If ANY claim is:
- incorrect, OR
- missing, OR
- unverifiable
→ assign **[0]**

------------------------------------------------------------
## Strict Requirements

- You MUST use Playwright MCP tools for all factual verification.
- You MUST NOT add or infer information beyond what is provided.

------------------------------------------------------------
## Output Format (Strict)

Your final output must be exactly one line:

Response: [1]
or
Response: [0]

Nothing else.
