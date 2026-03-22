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

### Key Protein Visualization Tools in Structural Biology

Four widely used tools for protein visualization in structural biology are PyMOL, VMD (Visual Molecular Dynamics), UCSF Chimera, and UCSF ChimeraX. These tools are essential for analyzing molecular structures, trajectories, and related data, and are commonly employed by researchers for tasks like viewing 3D models, rendering images, and performing basic analyses.

#### PyMOL
- **Developer**: Schrödinger
- **Supported Operating Systems**: Windows, macOS, Linux/Unix
- **Official Website**: [https://pymol.org/](https://pymol.org/)
- **Availability**: Both free (open-source version) and paid (commercial licenses with additional features)

#### VMD
- **Developer**: Theoretical and Computational Biophysics Group at the University of Illinois at Urbana-Champaign
- **Supported Operating Systems**: Windows, macOS, Linux/Unix
- **Official Website**: [https://www.ks.uiuc.edu/Research/vmd/](https://www.ks.uiuc.edu/Research/vmd/)
- **Availability**: Free

#### UCSF Chimera
- **Developer**: Resource for Biocomputing, Visualization, and Informatics (RBVI) at the University of California, San Francisco (UCSF)
- **Supported Operating Systems**: Windows, macOS, Linux/Unix
- **Official Website**: [https://www.cgl.ucsf.edu/chimera/](https://www.cgl.ucsf.edu/chimera/)
- **Availability**: Both free (for noncommercial use) and paid (commercial licensing)

#### UCSF ChimeraX
- **Developer**: Resource for Biocomputing, Visualization, and Informatics (RBVI) at the University of California, San Francisco (UCSF)
- **Supported Operating Systems**: Windows, macOS, Linux/Unix
- **Official Website**: [https://www.rbvi.ucsf.edu/chimerax/](https://www.rbvi.ucsf.edu/chimerax/)
- **Availability**: Both free (for academic, government, nonprofit, and personal use) and paid (commercial licensing)

These tools are selected based on their frequent mentions in scientific literature and community discussions as staples in the field. For installation and updates, always refer to the official websites, as system requirements may evolve.

---

In structural biology, protein visualization software plays a critical role in enabling researchers to explore, analyze, and interpret complex molecular structures derived from techniques like X-ray crystallography, cryo-electron microscopy (cryo-EM), and NMR spectroscopy. These tools facilitate the rendering of 3D models, manipulation of atomic coordinates, simulation of dynamics, and generation of publication-quality images. Among the most widely adopted are PyMOL, VMD, UCSF Chimera, and UCSF ChimeraX, which have been highlighted in numerous reviews, tutorials, and databases for their versatility and user-friendly interfaces. While other tools like Swiss-PdbViewer, NGL Viewer, and MolScript exist, the selected four stand out for their broad adoption in academic and research settings, as evidenced by their integration with resources like the Protein Data Bank (PDB) and frequent citations in bioinformatics forums.

PyMOL, originally developed on open-source foundations, is renowned for its high-quality rendering capabilities and scripting features using Python, making it ideal for creating detailed molecular illustrations. It supports advanced features like ray-tracing for photorealistic images and is commonly used in drug design and protein engineering. VMD excels in handling large biomolecular systems, including molecular dynamics simulations, and offers built-in scripting for analysis. It is particularly favored for visualizing trajectories from simulations and integrating with tools like NAMD. UCSF Chimera, though now considered legacy software, remains popular for its interactive features, such as density map analysis and sequence alignment integration, and is free for noncommercial users. Its successor, UCSF ChimeraX, builds on this foundation with enhanced performance for modern datasets, including support for virtual reality and larger structures from cryo-EM, and is actively developed with new features like AI integration for structure prediction visualization.

The selection of these tools is informed by their prominence in educational resources, such as tutorials on YouTube and academic courses, as well as their compatibility with emerging technologies like AlphaFold for structure prediction. For instance, PyMOL and ChimeraX are often recommended for beginners due to their intuitive interfaces, while VMD is preferred for computational biophysicists handling simulation data. Community feedback on platforms like Reddit and ResearchGate underscores their reliability, with users noting Chimera's ease for Mac users and VMD's robustness for large-scale visualizations.

To provide a structured overview, the following table summarizes the key attributes of each tool based on official sources and verified specifications:

| Tool              | Developer                                      | Supported Operating Systems          | Official Website                          | Availability                  |
|-------------------|------------------------------------------------|--------------------------------------|-------------------------------------------|-------------------------------|
| PyMOL            | Schrödinger                                   | Windows (64-bit, e.g., Windows 11), macOS (13.0+ including Apple Silicon), Linux/Unix (64-bit, e.g., Rocky/RedHat Enterprise Linux 8+) | [https://pymol.org/](https://pymol.org/) | Both free (open-source) and paid (commercial) |
| VMD              | Theoretical and Computational Biophysics Group at the University of Illinois at Urbana-Champaign | Windows, macOS (MacOS X), Linux/Unix | [https://www.ks.uiuc.edu/Research/vmd/](https://www.ks.uiuc.edu/Research/vmd/) | Free (includes source code)  |
| UCSF Chimera     | Resource for Biocomputing, Visualization, and Informatics (RBVI) at UCSF (Regents of the University of California) | Windows (e.g., Vista and later), macOS (10.6+ Intel), Linux/Unix (64-bit, including SGI IRIX) | [https://www.cgl.ucsf.edu/chimera/](https://www.cgl.ucsf.edu/chimera/) | Both free (noncommercial) and paid (commercial) |
| UCSF ChimeraX    | Resource for Biocomputing, Visualization, and Informatics (RBVI) at UCSF | Windows (current versions), macOS (current versions), Linux/Unix (e.g., Ubuntu 24.04 and other distributions) | [https://www.rbvi.ucsf.edu/chimerax/](https://www.rbvi.ucsf.edu/chimerax/) | Both free (academic/government/nonprofit/personal) and paid (commercial) |

This table highlights the cross-platform compatibility of all tools, ensuring accessibility for diverse research environments. Note that while UCSF Chimera is still functional, its developers recommend transitioning to ChimeraX for better performance and ongoing support. Pricing models reflect a focus on accessibility for academia, with commercial options providing enhanced support or features.

In practice, these tools often complement each other; for example, VMD might be used for initial trajectory analysis, followed by PyMOL for refined visualizations. Recent advancements, such as integration with AI-driven structure prediction like AlphaFold, have further expanded their utility, allowing seamless import and visualization of predicted models. For specialized needs, such as web-based visualization, alternatives like BioViz Studio or Protter may be considered, but the core four remain the go-to options for most structural biologists. Researchers should verify the latest versions on official sites, as updates may include support for new file formats or hardware accelerations like GPU rendering.

### Key Citations
- [Molecular Graphics Software - RCSB PDB](https://www.rcsb.org/docs/additional-resources/molecular-graphics-software)
- [UCSF Chimera Home Page](https://www.cgl.ucsf.edu/chimera/)
- [A Concise Review of Biomolecule Visualization - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10887528/)
- [What are the best softwares for protein structure visualisation - Reddit](https://www.reddit.com/r/bioinformatics/comments/khflfg/what_are_the_best_softwares_for_protein_structure/)
- [Appendix D: Protein Structure Visualization Tools - SWISS-MODEL](https://swissmodel.expasy.org/coursetext/appendix_D.htm)
- [Applications of visualization technology in the structural sciences](https://pmc.ncbi.nlm.nih.gov/articles/PMC12119125/)
- [Visualizing protein structures — tools and trends - Portland Press](https://portlandpress.com/biochemsoctrans/article/48/2/499/222432/Visualizing-protein-structures-tools-and-trends)
- [AlphaFold Protein Structure Database](https://alphafold.ebi.ac.uk/)
- [Cutting-edge tools for structural biology: bringing AlphaFold to the ...](https://www.sciencedirect.com/science/article/pii/S0966842X25001106)
- [Protter - interactive protein feature visualization](http://wlab.ethz.ch/protter)
- [Protein Structure Software Recommendations ? : r/bioinformatics](https://www.reddit.com/r/bioinformatics/comments/ayi2cs/protein_structure_software_recommendations/)
- [Protein Visualization Tool | PyMOL Tutorial for Beginners - YouTube](https://www.youtube.com/watch?v=7cX5bVENWAE)
- [VMD - Visual Molecular Dynamics](https://www.ks.uiuc.edu/Research/vmd/)
- [What molecular graphics program do you recommend to your ...](https://www.researchgate.net/post/What_molecular_graphics_program_do_you_recommend_to_your_students_when_teaching_structural_biology)
- [Bioinformatics Tools Every Lab Should Use - AZoLifeSciences](https://www.azolifesciences.com/article/Bioinformatics-Tools-Every-Lab-Should-Use.aspx)
- [UCSF ChimeraX Home Page](https://www.rbvi.ucsf.edu/chimerax/)
- [Download UCSF Chimera](https://www.cgl.ucsf.edu/chimera/download.html)
- [Support | pymol.org](https://www.pymol.org/support.html)
- [installation [PyMOL Documentation]](https://pymol.org/dokuwiki/doku.php?id=installation)
- [VMD: Visual Molecular Dynamics Software](https://otm.illinois.edu/technologies/vmd-visual-molecular-dynamics-software)
- [VMD Installation Guide](https://www.ks.uiuc.edu/Research/vmd/current/ig.pdf)
- [System Requirements for Chimera and ChimeraX](https://www.cgl.ucsf.edu/chimerax/system_requirements.html)
- [Download UCSF Chimera](https://www.cgl.ucsf.edu/chimera/olddownload.html)
- [UCSF Chimera - Wikipedia](https://en.wikipedia.org/wiki/UCSF_Chimera)
- [UCSF Chimera Home Page](https://www.cgl.ucsf.edu/chimera/)
- [UCSF Chimera—A Visualization System for Exploratory Research ...](https://www.cgl.ucsf.edu/home/tef/pubs/chimera.pdf)
- [System Requirements for Chimera and ChimeraX](https://www.cgl.ucsf.edu/chimerax/system_requirements.html)
- [Download UCSF ChimeraX](https://www.cgl.ucsf.edu/chimerax/download.html)
- [Source code for molecular graphics program UCSF ChimeraX](https://github.com/RBVI/ChimeraX)

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

Extracted From Rubric-4:
https://pymol.org/

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
