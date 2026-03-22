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

### Key Templates
Research suggests that several popular LaTeX CV templates on Overleaf feature a personal photo positioned in the top left corner by default, typically within a left sidebar. This placement is common in modern designs inspired by templates like Friggeri CV, and no code modifications are needed beyond replacing the placeholder image with your own photo. Note that while these templates are widely used and customizable, photo inclusion on CVs can vary by region or industry (e.g., less common in the US for non-academic roles due to potential bias concerns).

- **Friggeri CV Template**: A visually striking template with a narrow left sidebar where the photo sits at the top left, followed by contact details. Ideal for creative or academic fields.
- **Twenty Seconds Curriculum Vitae**: Designed for quick readability, this template places the photo in the top left of a colored sidebar, emphasizing skills and experience in a compact format.
- **Forty Seconds CV**: An extension of the Twenty Seconds style, offering more customization options while keeping the photo in the top left sidebar position for a professional, multi-page layout if needed.

#### Usage Tips
To use these, open the links on Overleaf, create a copy of the project, and upload your photo to replace the placeholder (usually named something like "profile.jpg" or "example-image"). Compile the document to see the PDF output. These templates support easy edits for sections like education, experience, and skills without altering the photo position.

#### Considerations
It seems likely that these templates meet your criteria, as their default designs include the photo in the specified location based on standard LaTeX CV layouts. If your field discourages photos, you can comment out the image command easily. For best results, use a high-quality, professional headshot cropped to a square or circle as per the template's style.

---

### Detailed Survey of Overleaf CV Templates with Top Left Photo Placement
This section provides a comprehensive overview of suitable Overleaf templates for CVs that incorporate a personal photo in the top left corner by default. The selection focuses on official gallery templates, drawing from popular designs that prioritize modern aesthetics, readability, and minimal setup. These templates are part of Overleaf's extensive library, which includes hundreds of user-submitted and staff-curated options for resumes and CVs. The emphasis here is on those where the photo is pre-configured in a left sidebar or header, requiring no structural code changes—only image replacement and content filling.

The templates were identified through searches on Overleaf's gallery and related descriptions, prioritizing ones inspired by influential designs like Friggeri CV, which pioneered the left-sidebar photo layout. While many CV templates (e.g., Awesome CV or AltaCV) place photos on the right by default, the ones below align with your requirements. Note that LaTeX templates often use commands like `\includegraphics` for photos, and the position is fixed in the class file (e.g., via minipages or paracol environments).

#### Overview of Template Features
All selected templates:
- Are free and accessible via Overleaf's gallery.
- Compile with standard LaTeX engines (some require XeLaTeX for fonts).
- Include sections for education, experience, skills, publications, and more.
- Allow photo upload without code edits; placeholders are typically in the header or sidebar.
- Support multi-page expansion if your CV grows longer.

Potential drawbacks include regional preferences (e.g., photos may not be ideal for ATS-optimized resumes in tech jobs), but these can be removed by commenting out the relevant line.

#### Selected Templates and Details
Here are the three templates that best match your query, with links and key attributes:

1. **Friggeri CV Template**  
   Link: https://www.overleaf.com/latex/templates/friggeri-cv-template/hmnchbfmjgqh  
   This template, originally created by Adrien Friggeri and available on Overleaf, features a distinctive asymmetric layout with a thin left sidebar. The personal photo is placed at the very top of this sidebar, making it the top left element of the entire document. The design uses geometric shapes and bold colors for a modern, artistic feel, suitable for designers, academics, or tech professionals. By default, it includes a placeholder image that you replace via the `\includegraphics` command in the main.tex file—no repositioning needed. Modifications like color changes are optional but straightforward. This template has been adapted in various forks (e.g., Modified Friggeri CV), but the original maintains the clean top-left photo setup.

2. **Twenty Seconds Curriculum Vitae**  
   Link: https://www.overleaf.com/latex/templates/twenty-seconds-curriculum-vitae/kfgsngtymkfj  
   Optimized for "20-second scans" by recruiters, this template positions the photo in the top left corner within a prominent left sidebar. The sidebar also houses contact info, skills (often visualized with bars or icons), and languages, while the right column focuses on chronological experience and education. It's compact, one-page by default, but expandable. The photo is included out-of-the-box with a simple placeholder; upload your image and recompile. Variants like Twenty One Seconds or Swedish adaptations exist, but the core template keeps the left placement. This design draws from hipster-inspired aesthetics, ensuring visual appeal without overcomplication.

3. **Forty Seconds CV**  
   Link: https://www.overleaf.com/latex/templates/forty-seconds-cv/pztcktmyngsk  
   Building on the Twenty Seconds CV class, this highly customizable template retains the top left photo in the sidebar while adding options for multi-page support and layout tweaks (e.g., color themes, icon styles). The photo is default in the left position, with an "About Me" section below it, making it ideal for mid-career professionals needing more space. No modifications are required for the photo; it's handled via fontawesome icons and graphicx packages. User feedback highlights its flexibility, such as adjusting sidebar width or removing elements, but the base setup matches your needs perfectly. It's a rewrite of earlier classes, improving on readability and ATS compatibility.

#### Comparison Table
To aid selection, here's a table comparing the templates based on key aspects:

| Template Name     | Link                                                         | Default Photo Position | Key Strengths                                                | Potential Limitations                                 | Best For                      |
| ----------------- | ------------------------------------------------------------ | ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------- | ----------------------------- |
| Friggeri CV       | https://www.overleaf.com/latex/templates/friggeri-cv-template/hmnchbfmjgqh | Top left (sidebar)     | Artistic design, bold visuals, easy bib integration for publications | Requires XeLaTeX; more "flashy" than minimalist       | Creative/academic roles       |
| Twenty Seconds CV | https://www.overleaf.com/latex/templates/twenty-seconds-curriculum-vitae/kfgsngtymkfj | Top left (sidebar)     | Quick-scan optimized, skill visualizations, compact one-page focus | Limited to shorter CVs without extension              | Entry-level or tech positions |
| Forty Seconds CV  | https://www.overleaf.com/latex/templates/forty-seconds-cv/pztcktmyngsk | Top left (sidebar)     | Multi-page support, high customizability, icon-based skills  | Slightly more complex options may overwhelm beginners | Mid-career professionals      |

#### Additional Insights and Alternatives
If these don't fully suit, related templates like Hipster CV (https://www.overleaf.com/latex/templates/hipster-cv/tbkbkphqrtyz) or Simple Hipster CV (https://www.overleaf.com/latex/templates/simple-hipster-cv/cnpkkjdkyhhw) also feature top-left photos in sidebars, inspired by Friggeri and Twenty designs. They offer color themes and progress circles for skills, with no need for photo repositioning.

Overleaf's gallery (tagged/cv) hosts over 100 CV templates, many with photos, but left placement is less common than right due to traditional layouts. Searches revealed that templates like AltaCV or Deedy CV often default to top right but can be switched with minor code changes—however, these were excluded to adhere to your no-modification preference.

For photo best practices: Use a square aspect ratio (e.g., 100x100 pixels), professional attire, and neutral background to ensure compatibility. If compiling issues arise, Overleaf's real-time collaboration and version control make troubleshooting easy.

This survey confirms the availability of matching templates through direct gallery links and descriptions, ensuring you can start building your CV immediately.

### Key Citations
- [Overleaf CV Templates Gallery](https://www.overleaf.com/latex/templates/tagged/cv)
- [Friggeri CV Template on Overleaf](https://www.overleaf.com/latex/templates/friggeri-cv-template/hmnchbfmjgqh)
- [Twenty Seconds CV Template on Overleaf](https://www.overleaf.com/latex/templates/twenty-seconds-curriculum-vitae/kfgsngtymkfj)
- [Forty Seconds CV Template on Overleaf](https://www.overleaf.com/latex/templates/forty-seconds-cv/pztcktmyngsk)
- [Hipster CV Variants on Overleaf](https://www.overleaf.com/latex/templates/simple-hipster-cv/cnpkkjdkyhhw)
- [LaTeX Templates for CVs (External Reference)](https://www.latextemplates.com/cat/curricula-vitae)

[The End of Response]

### Rubric

[The Start of Rubric]

Locate 3 resume templates from Overleaf’s official templates where the top-left corner of the template directly displays a personal photo.
After identifying qualifying resume templates, provide their corresponding webpage links. Each valid link provided earns 1 point, up to a maximum of 3 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-1:
https://www.overleaf.com/latex/templates/twenty-seconds-curriculum-vitae/kfgsngtymkfj

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
