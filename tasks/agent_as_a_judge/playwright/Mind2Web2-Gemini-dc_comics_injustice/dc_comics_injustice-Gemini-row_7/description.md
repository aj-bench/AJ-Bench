# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

I am a DC Comics fan. Could you find three comic books from different series written by the same author as Injustice: Gods Among Us Year One that feature Batman (excluding Injustice itself)? Please provide the links to the homepage of Injustice and these comic books on DC comic's official website.

[The End of Query]

### Response

[The Start of Response]

# The Batman Canon of Tom Taylor: A Comprehensive Analysis Beyond Injustice

## Introduction: The Creative Legacy of Tom Taylor
Based on a thorough review of published materials, the writer of Injustice: Gods Among Us: Year One is definitively confirmed as Tom Taylor.<sup>1</sup>

## Core Findings: Three Distinct Portrayals of Batman by Tom Taylor

### DCEASED: The Dark Knight in the Undead Apocalypse
Official DC Comics Homepage Link: https://www.dc.com/graphic-novels/dceased <sup>9</sup>

### NIGHTWING: The Mentor and the Bat-Family
While not a solo Batman title, Tom Taylor's critically acclaimed run on Nightwing is an essential entry for any fan of the Dark Knight.
Official DC Comics Homepage Link: https://www.dc.com/graphic-novels/nightwing-2016/nightwing-vol-1-leaping-into-the-light <sup>10</sup>

### BATMAN: THE DETECTIVE: A Return to First Principles
Official DC Comics Homepage Link: https://www.dc.com/graphic-novels/batman-the-detective-2021/batman-the-detective <sup>11</sup>

## Summary of Findings and Conclusion
Official DC Comics Homepage Link for Injustice: Gods Among Us: https://www.dc.com/graphic-novels/injustice-gods-among-us-2013/injustice-gods-among-us-year-one-the-complete-collection

#### Works cited
1. www.penguinrandomhouse.com, https://www.penguinrandomhouse.com/books/590014/injustice-gods-among-us-year-one-the-deluxe-edition-by-tom-taylor/  
2. Injustice: Gods Among Us Year One - The Complete Collection: Volume 1 by Tom Taylor - Books on Google Play, https://play.google.com/store/books/details/Tom_Taylor_Injustice_Gods_Among_Us_Year_One_The_Co?id=GwaLCwAAQBAJ  
3. Injustice: Gods Among Us #1 by Tom Taylor - Goodreads, https://www.goodreads.com/book/show/18058138-injustice  
4. Tom Taylor – #1 New York Times Bestselling Author, https://www.tomtaylormade.com/  
5. DCeased by Tom Taylor | Goodreads, https://www.goodreads.com/book/show/46021336-dceased  
6. I am Tom Taylor, writer of Injustice: Gods Among Us, and Earth 2. AMA : r/DCcomics - Reddit, https://www.reddit.com/r/DCcomics/comments/2hxvpc/i_am_tom_taylor_writer_of_injustice_gods_among_us/  
7. Nightwing by Tom Taylor - Full Story - YouTube, https://www.youtube.com/watch?v=F5jqOnalZrc  
8. DCeased by Tom Taylor, Paperback | Barnes & Noble®, https://www.barnesandnoble.com/w/dceased-tom-taylor/1131757988  
9. DCeased - DC Comics, https://www.dc.com/graphic-novels/dceased  
10. NIGHTWING VOL. 1: LEAPING INTO THE LIGHT | DC, https://www.dc.com/graphic-novels/nightwing-2016/nightwing-vol-1-leaping-into-the-light  
11. Tom Taylor | DC, https://www.dc.com/talent/tom-taylor  
12. Batman: Detective Comics Vol. 1: Mercy of the Father by Tom Taylor | Goodreads, https://www.goodreads.com/book/show/219850919-batman  
13. Batman: Detective Comics Vol. 1: Mercy of the Father by Tom Taylor: 9781799501800 | PenguinRandomHouse.com: Books, https://www.penguinrandomhouse.com/books/773603/batman-detective-comics-vol-1-mercy-of-the-father-by-tom-taylor/  
14. INJUSTICE: GODS AMONG US YEAR ONE – THE COMPLETE COLLECTION - DC Comics, https://www.dc.com/graphic-novels/injustice-gods-among-us-2013/injustice-gods-among-us-year-one-the-complete-collection

[The End of Response]

### Rubric

[The Start of Rubric]

1. Correctly identify the author of Injustice: Gods Among Us Year One for 1 point;
2. Identify three additional comic series by this author featuring Batman a significant character (excluding Injustice: Gods Among Us Year One series). Each correctly identified series earns 1 point, up to a maximum of 3 points;
3. Provide valid homepage links for the above three comics on the DC Comics official website. Each correctly provided link earns 1 point, with a maximum of 3 points.
4. Accurately provide the homepage link for Injustice: Gods Among Us Year One series on the DC Comics official website to earn 1 point;
5. Total points: 8 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-3:
https://www.dc.com/graphic-novels/batman-the-detective-2021/batman-the-detective

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
