# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Identify four widely-used protein visualization software tools commonly employed in structural biology. For each tool, provide the developer's name, supported operating systems (Windows, macOS, Linux/Unix), a direct link to the software's official website, and indicate whether it is free, paid, or has both free and paid versions available.

[The End of Query]

### Response

[The Start of Response]

# Widely-Used Protein Visualization Software Tools

Below is a summary of four commonly employed protein visualization tools in structural biology, including their developers, supported operating systems, official websites, and licensing models.


| Software | Developer | Supported OS | Official Website | License |
| :-- | :-- | :-- | :-- | :-- |
| PyMOL | Originally created by Warren Lyford DeLano; currently maintained and commercialized by Schrödinger, Inc. | Windows; macOS; Linux/Unix | https://pymol.org/view.html | Both free (open-source code; legacy builds, student/educator licences) and paid (current binaries/subscriptions) [^1][^2] |
| UCSF Chimera | Resource for Biocomputing, Visualization, and Informatics (RBVI) at University of California, San Francisco | Windows; macOS; Linux | https://www.cgl.ucsf.edu/chimera/ | Free for noncommercial use [^3][^4] |
| VMD | Theoretical and Computational Biophysics Group, University of Illinois at Urbana-Champaign | Windows; macOS; Unix/Linux | http://www.ks.uiuc.edu/Research/vmd/ | Free of charge (open-source) [^5][^6] |
| Jmol | Jmol development team (open-source project) | Windows; macOS; Linux/Unix | http://www.jmol.org/ | Free and open-source (LGPL) [^7] |

<span style="display:none">[^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^20][^21][^22][^23][^24][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://proteopedia.org/wiki/index.php/PyMOL

[^2]: https://en.wikipedia.org/wiki/PyMOL

[^3]: https://en.wikipedia.org/wiki/UCSF_Chimera

[^4]: https://www.rcsb.org/docs/additional-resources/molecular-graphics-software

[^5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2972669/

[^6]: https://kbbox.h-its.org/toolbox/tools/preparation-and-general-modelling-tools/vmd/

[^7]: https://en.wikipedia.org/wiki/Jmol

[^8]: https://services.anu.edu.au/information-technology/software-systems/pymol

[^9]: https://www.exxactcorp.com/Supported-Software/VMD

[^10]: https://www.exxactcorp.com/Supported-Software/ucsf-chimera

[^11]: https://www.pymol.org/view.html

[^12]: https://marpat.github.io/chimera-intro.html

[^13]: https://hpc.llnl.gov/software/visualization-software/vmd

[^14]: https://pubmed.ncbi.nlm.nih.gov/32881101/

[^15]: https://www.pymol.org/pymol.html

[^16]: https://www.youtube.com/watch?v=OHJD8tzigGo

[^17]: https://fitzkee.chemistry.msstate.edu/sites/default/files/ch8990/pymol-tutorial.pdf

[^18]: https://journals.iucr.org/services/help/jtkt/2.html

[^19]: https://proteopedia.org/wiki/index.php/Introduction_to_Jmol

[^20]: http://wiki.jmol.org/index.php/Jmol:About

[^21]: https://molview.org

[^22]: http://www.bioinformatics.org/jmol-tutorials/jtat/_docs/jmol_app.htm

[^23]: https://www.rcsb.org/docs/3d-viewers/jmol

[^24]: https://jmol.sourceforge.net

[The End of Response]

### Rubric

[The Start of Rubric]

1. List four protein visualization software tools widely used in structural biology. 1 point for each correct tool listed, maximum 4 points.
2. For each correct tool, accurately provide the developer's name. 1 point for each correct tool listed, maximum 4 points.
3. For each correct tool, accurately provide the operating system it supports (e.g., Windows, macOS, Linux/Unix). 1 point for each correct tool listed, maximum 4 points.
4. For each correct tool, provide a direct link to its official website. 1 point for each correct tool listed, maximum 4 points.
5. For each correct tool, indicate whether it is free software, paid software, or both free and paid versions. 1 point for each accurate description, maximum 4 points.
6. Total 20 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-2:
Resource for Biocomputing, Visualization, and Informatics (RBVI) at University of California, San Francisco

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
