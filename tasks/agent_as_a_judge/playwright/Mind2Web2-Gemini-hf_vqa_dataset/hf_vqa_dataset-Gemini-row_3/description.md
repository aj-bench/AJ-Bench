# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

I'm looking into large-scale English visual question answering datasets hosted on HuggingFace, particularly those released by academic institutions in the US.

Please find two English visual question answering datasets with more than 1M rows and provided with Croissant metadata, released by a research group from US universities with their HuggingFace profile explicitly stating the university affiliation. For each dataset, show me the link to the dataset on HuggingFace and a link to the HuggingFace profile of the organization.

[The End of Query]

### Response

[The Start of Response]

# Primary Finding: A Direct Match to Query Specifications

The investigation identified one dataset, neulab/MultiUI, which fully satisfies all five criteria stipulated in the query. It is a large-scale, English-language VQA-compatible dataset from a major US university, published under a formal organization profile with an explicit affiliation, and is provisioned with Croissant metadata.

- Dataset: neulab/MultiUI
  - Link to Dataset: https://huggingface.co/datasets/neulab/MultiUI
- Publishing Organization: neulab
  - Link to Organization Profile: https://huggingface.co/neulab

## Publisher Verification: Carnegie Mellon University

The publishing entity, neulab, is a formal organization on the Hugging Face Hub. Its profile page provides a clear and direct statement of its academic affiliation: "This is Graham Neubig's lab at the Language Technologies Institute (LTI) of Carnegie Mellon University (CMU)".<sup>10</sup> This statement unequivocally fulfills the requirement for a dataset released by a research group from a US university with an explicit affiliation stated on its Hugging Face profile. Carnegie Mellon University is a globally recognized leader in computer science and artificial intelligence research, lending significant credibility to the datasets it publishes.

## Dataset Analysis: neulab/MultiUI

The neulab/MultiUI dataset was examined against the technical specifications of the query and found to be a complete match.

- Scale: The dataset is exceptionally large, containing 7.29 million rows (or samples).<sup>10</sup> This figure is substantially greater than the specified threshold of one million rows, making it a suitable resource for training large-scale, data-intensive models.
- Task and Language: MultiUI is a comprehensive multimodal dataset designed for training vision-language models across a variety of tasks. Its scope explicitly includes Visual Question Answering, and the data is in English.<sup>11</sup> This aligns directly with the core task requirement.
- Croissant Metadata: The dataset card for neulab/MultiUI is explicitly tagged with the "Croissant" library, indicating its full compatibility with the metadata standard.<sup>11</sup> This is further confirmed by the platform's automated generation of Croissant metadata for all Parquet-compatible datasets, as detailed in the previous section.

### Works cited

1. Visual Question Answering - Hugging Face, https://huggingface.co/docs/transformers/tasks/visual_question_answering  
2. What is Visual Question Answering? - Hugging Face, https://huggingface.co/tasks/visual-question-answering  
3. Salesforce/blip-vqa-base - Hugging Face, https://huggingface.co/Salesforce/blip-vqa-base  
4. Croissant: A Metadata Format for ML-Ready Datasets - arXiv, https://arxiv.org/html/2403.19546v1  
5. Croissant is a high-level format for machine learning datasets that brings together four rich layers. - GitHub, https://github.com/mlcommons/croissant  
6. Croissant: a metadata format for ML-ready datasets - Google Research, https://research.google/blog/croissant-a-metadata-format-for-ml-ready-datasets/  
7. Get Croissant metadata - Hugging Face, https://huggingface.co/docs/dataset-viewer/croissant  
8. flaviagiammarino/path-vqa · Datasets at Hugging Face, https://huggingface.co/datasets/flaviagiammarino/path-vqa  
9. HuggingFaceM4/DocumentVQA · Datasets at Hugging Face, https://huggingface.co/datasets/HuggingFaceM4/DocumentVQA  
10. NeuLab @ LTI/CMU - Hugging Face, https://huggingface.co/neulab  
11. neulab/MultiUI · Datasets at Hugging Face, https://huggingface.co/datasets/neulab/MultiUI  
12. ranjaykrishna/visual_genome · Datasets at Hugging Face, https://huggingface.co/datasets/ranjaykrishna/visual_genome  
13. MMInstruction/M3IT · Datasets at Hugging Face, https://huggingface.co/datasets/MMInstruction/M3IT

[The End of Response]

### Rubric

[The Start of Rubric]

1. Find two large-scale English visual question answering (VQA) datasets containing more than 1 million rows of data (including 1 million rows). The datasets must provide Croissant metadata and be released by research teams from U.S. universities, with the HuggingFace profile of their affiliated research team clearly indicating the university affiliation. 1 point will be awarded for each qualifying dataset, with a maximum of 2 points.
2. For the above datasets, 1 point will be awarded for each accurate HuggingFace profile link of the team corresponding to a dataset, with a maximum of 2 points.
3. For the above datasets, 1 point will be awarded for each accurate link to the dataset on HuggingFace, with a maximum of 2 points.
(The total maximum score is 6 points.)

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-2:
https://huggingface.co/neulab

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
