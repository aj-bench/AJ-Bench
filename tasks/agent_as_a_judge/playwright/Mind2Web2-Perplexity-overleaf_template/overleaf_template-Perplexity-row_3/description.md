# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

I want to find three Overleaf templates from Overleaf's official template list for my CV. I hope three templates can already display my photo without further customized modification, with the photo placed in the top left corner of my CV. Please return the links to these templates.

[The End of Query]

### Response

[The Start of Response]

# Recommended Overleaf CV Templates with Built-In Top-Left Photo

Below are three official Overleaf templates that include a photo slot—positioned at the top left—out of the box.

1. Recent Grad CV – with photo
https://www.overleaf.com/latex/templates/recent-grad-cv-with-photo/dqfncmgrjkyy
2. Simple Academic CV [with photo]
https://www.overleaf.com/latex/templates/simple-academic-cv-with-photo/gxkrgqfhrwfp
3. Awesome CV
https://www.overleaf.com/latex/templates/awesome-cv/dfnvtnhzhhbm
<span style="display:none">[^1][^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^2][^20][^21][^22][^23][^24][^25][^26][^27][^3][^4][^5][^6][^7][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://www.overleaf.com/latex/templates/recent-grad-cv-with-photo/dqfncmgrjkyy

[^2]: https://www.reddit.com/r/LaTeX/comments/1e1gda1/positioning_the_image/

[^3]: https://www.overleaf.com/latex/templates/deedy-cv/bjryvfsjdyxz

[^4]: https://www.overleaf.com/latex/templates/simple-academic-cv-with-photo/gxkrgqfhrwfp

[^5]: https://latex.org/forum/viewtopic.php?t=4049

[^6]: https://resumegenius.com/resume-templates/latex-resume-template

[^7]: https://www.overleaf.com/latex/templates/charless-cv-template/mnhkbhwyytfv

[^8]: https://stackoverflow.com/questions/61644225/how-to-place-the-logo-at-the-top-right-side-of-the-page-in-latex

[^9]: https://www.reddit.com/r/gatech/comments/gvy2jd/any_good_overleaf_templates_for_resume/

[^10]: https://www.overleaf.com/latex/templates

[^11]: https://www.overleaf.com/latex/templates/a-customised-curve-cv/mvmbhkwsnmwv

[^12]: https://www.reddit.com/r/LaTeX/comments/1jzd25t/any_modern_looking_cv_templates_in_latex/

[^13]: https://www.overleaf.com/latex/templates/resume-template/ysrmnrwyrhpp

[^14]: https://www.overleaf.com/learn/how-to/Including_images_on_Overleaf

[^15]: https://www.overleaf.com/latex/templates/jakes-resume/syzfjbzwjncs

[^16]: https://www.overleaf.com/gallery/tagged/cv

[^17]: https://latex.org/forum/viewtopic.php?t=25810

[^18]: https://www.overleaf.com/latex/examples/tagged/cv

[^19]: https://www.overleaf.com/learn/latex/Inserting_Images

[^20]: https://www.overleaf.com/latex/templates/tagged/cv/page/5

[^21]: https://www.overleaf.com/latex/templates/awesome-cv/dfnvtnhzhhbm

[^22]: https://www.overleaf.com/latex/templates/awesome-source-cv/wrdjtkkytqcw

[^23]: https://www.overleaf.com/latex/templates/awesome-cv-gold/tshsfmqnjpfn

[^24]: https://www.overleaf.com/latex/templates/tagged/cv/page/21

[^25]: https://github.com/posquit0/Awesome-CV

[^26]: https://github.com/posquit0/Awesome-CV/issues/420

[^27]: https://www.reddit.com/r/LaTeX/comments/14fy16h/my_new_latex_resume_based_on_awesomecv/

[The End of Response]

### Rubric

[The Start of Rubric]

Locate 3 resume templates from Overleaf’s official templates where the top-left corner of the template directly displays a personal photo.
After identifying qualifying resume templates, provide their corresponding webpage links. Each valid link provided earns 1 point, up to a maximum of 3 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-1:
https://www.overleaf.com/latex/templates/awesome-cv/dfnvtnhzhhbm

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
