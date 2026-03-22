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

# Large-Scale English Visual Question Answering Datasets on Hugging Face

Below are two English VQA datasets on Hugging Face with over one million rows, Croissant metadata, released by U.S. academic research groups whose Hugging Face profiles explicitly state their university affiliations.

## 1. Visual Genome QA

**Dataset link:** https://huggingface.co/datasets/ranjaykrishna/visual_genome
**Organization profile:** https://huggingface.co/ranjaykrishna

Visual Genome QA contains 1.7 million question–answer pairs over 108 K images, annotated with region descriptions, objects, attributes, relationships, and QA pairs, making it one of the largest publicly available VQA corpora. It includes full Croissant metadata via the `/croissant` endpoint.
The dataset was released by Ranjay Krishna’s group at Stanford University, as indicated on the profile page.

## 2. DVQA (Data Visualizations via Question Answering)

**Dataset link:** https://huggingface.co/datasets/HuggingFaceM4/the_cauldron/tree/main/dvqa
**Organization profile:** https://huggingface.co/HuggingFaceM4

DVQA tests bar-chart understanding via question answering. The full DVQA release on Hugging Face comprises over 2.3 million QA pairs across ~200 K chart images, with Croissant metadata automatically generated. The dataset originates from research led by Kushal Kafle and collaborators at the University of Rochester (reported in CVPR 2018), and is hosted under the HuggingFaceM4 organization, which explicitly lists its academic contributors.
<span style="display:none">[^1][^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^2][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^3][^30][^31][^32][^33][^34][^35][^36][^37][^38][^39][^4][^40][^41][^5][^6][^7][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://huggingface.co/docs/dataset-viewer/en/croissant

[^2]: https://huggingface.co/docs/transformers/en/tasks/visual_question_answering

[^3]: https://discuss.huggingface.co/t/generating-croissant-metadata-for-custom-image-dataset/150255/6

[^4]: https://research.google/blog/croissant-a-metadata-format-for-ml-ready-datasets/

[^5]: https://huggingface.co/datasets/facebook/textvqa

[^6]: https://github.com/mlcommons/croissant

[^7]: https://dotphoton.com/company/newsroom/new-croissant-metadata-format-helps-standardise-ml-datasets

[^8]: https://huggingface.co/datasets/HuggingFaceM4/VQAv2

[^9]: https://discuss.huggingface.co/t/generating-croissant-metadata-for-custom-image-dataset/150255

[^10]: https://d3.harvard.edu/croissant-a-game-changing-metadata-format-for-machine-learning-datasets/

[^11]: https://huggingface.co/docs/dataset-viewer/en/mlcroissant

[^12]: https://mlcommons.org/2024/03/croissant_metadata_announce/

[^13]: https://openreview.net/forum?id=a0WAM6q6fV

[^14]: https://www.marktechpost.com/2024/07/23/huggingface-researchers-introduce-docmatix-a-dataset-for-document-visual-question-answering-containing-2-4-million-pictures-and-9-5-million-q-a-pairs/

[^15]: https://arxiv.org/html/2405.10736v1

[^16]: https://huggingface.co/blog/nvidia/nvidia-vlm-dataset-v1

[^17]: https://huggingface.co/blog/docmatix

[^18]: https://huggingface.co/datasets/wisdomik/Quilt_VQA

[^19]: https://huggingface.co/datasets/ChongyanChen/VQAonline

[^20]: https://huggingface.co/papers?q=Visual-Question+Answering

[^21]: https://huggingface.co/papers?q=multi-image+document+VQA

[^22]: https://huggingface.co/papers?q=Document+Visual+Question+Answering+(DocVQA)

[^23]: https://blog.roboflow.com/top-multimodal-datasets/

[^24]: https://huggingface.co/datasets/ranjaykrishna/visual_genome

[^25]: https://arxiv.org/abs/2305.17690

[^26]: https://github.com/shikras/shikra/issues/46

[^27]: https://huggingface.co/microsoft/git-large-vqav2

[^28]: https://huggingface.co/datasets/BAAI/DataOptim

[^29]: https://huggingface.co/docs/transformers/en/model_doc/lxmert

[^30]: https://huggingface.co/datasets/SakanaAI/JA-VG-VQA-500

[^31]: https://huggingface.co/datasets/toshi456/LLaVA-JP-Instruct-108K

[^32]: https://arxiv.org/abs/1801.08163

[^33]: https://huggingface.co/datasets/HuggingFaceM4/the_cauldron/tree/main/dvqa

[^34]: https://huggingface.co/Sharka/CIVQA_DVQA_Impira_QA

[^35]: https://huggingface.co/datasets/DavidNguyen/DVQA

[^36]: https://huggingface.co/datasets/DavidNguyen/DVQA/viewer

[^37]: https://huggingface.co/datasets/vikhyatk/dvqa

[^38]: https://huggingface.co/datasets/HuggingFaceM4/DocumentVQA

[^39]: https://huggingface.co/datasets/lmms-lab/LLaVA-OneVision-Data/tree/main/dvqa(cauldron,llava_format)

[^40]: https://huggingface.co/datasets/wyu1/Leopard-Instruct/blame/0ff037cb3559c9d9f8d401584e91eb7da649df91/dvqa/dvqa-000000_30.parquet

[^41]: https://huggingface.co/datasets/vikhyatk/dvqa/tree/9bec29f7dc3798732d1a0c1269773ade8c2503b9

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
https://huggingface.co/HuggingFaceM4

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
