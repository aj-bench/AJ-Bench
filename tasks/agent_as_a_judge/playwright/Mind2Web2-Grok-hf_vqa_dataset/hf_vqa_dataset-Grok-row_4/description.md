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

### Key Points
- Research suggests that the Visual Genome dataset meets the criteria, released by a research group affiliated with Stanford University (a US university), with the HuggingFace profile and dataset description explicitly referencing the university affiliation through the paper authors and DOI.
- The GQA dataset also aligns with the requirements, released by a Stanford University research group, with the HuggingFace dataset page linking to Stanford-hosted resources, confirming the affiliation.
- Both datasets are English visual question answering (VQA) collections with more than 1 million rows (QA pairs or questions), and at least one (GQA) is confirmed to have Croissant metadata available.
- It seems likely that these are suitable examples, though some aspects like Croissant availability for Visual Genome could not be confirmed, highlighting the complexity in metadata standards across uploads.
- There is no major controversy around these datasets, but debates in the VQA community often center on bias mitigation and reasoning capabilities, which both datasets address to varying degrees.

### Dataset 1: Visual Genome
The Visual Genome dataset features 1.7 million QA pairs, focusing on detailed visual reasoning tasks like object recognition, attribute identification, and relationship understanding. It is released by a research group from Stanford University, as stated in the associated paper and author affiliations on the HuggingFace page. 
- Link to the dataset on HuggingFace: https://huggingface.co/datasets/ranjaykrishna/visual_genome
- Link to the HuggingFace profile of the organization: https://huggingface.co/ranjaykrishna (uploader profile, with dataset description linking to Stanford affiliation)

### Dataset 2: GQA
The GQA dataset includes over 22 million questions (with the balanced version exceeding 1.4 million), emphasizing compositional reasoning and bias reduction in real-world visual scenes. It is released by researchers from Stanford University, with the HuggingFace page referencing Stanford-hosted image data.
- Link to the dataset on HuggingFace: https://huggingface.co/datasets/echarlaix/gqa
- Link to the HuggingFace profile of the organization: https://huggingface.co/echarlaix (uploader profile, with dataset linking to Stanford resources)

---

The Visual Genome and GQA datasets represent cornerstone contributions to the field of visual question answering (VQA), particularly for large-scale English-language tasks. Both originate from research efforts at Stanford University, a leading US academic institution, and are hosted on HuggingFace with references to their university roots. Visual Genome, developed by Ranjay Krishna and colleagues including Yuke Zhu, Oliver Groth, Justin Johnson, Kenji Hata, Joshua Kravitz, Stephanie Chen, Yannis Kalantidis, Li-Jia Li, David A. Shamma, Michael S. Bernstein, and Li Fei-Fei, provides a rich foundation for connecting language and vision through crowdsourced dense image annotations. With over 108,000 images and 1,773,258 QA pairs, it exceeds the 1 million row threshold, covering a spectrum of visual tasks from basic recognition to high-level reasoning. The dataset is entirely in English, with all annotations using English as the primary language, and includes additional components like 3.8 million object instances, 2.8 million attributes, and 2.3 million relationships, making it ideal for multifaceted VQA research.

The dataset's creation involved over 33,000 unique workers via Amazon Mechanical Turk, resulting in high-quality, diverse annotations collected over 6 months. Rows in this context refer to QA pairs, which are structured as open-ended questions and answers tied to image regions, objects, and relationships. Although Croissant metadata was not retrievable via the API endpoint during analysis, the dataset supports standard HF metadata formats, including YAML warnings for repo cards, and can be loaded with configurations like "question_answer_v1.2.0" for specific QA subsets. The HuggingFace uploader, ranjaykrishna, is directly associated with the original research team, and the profile implicitly ties to Stanford through the dataset description and paper citation (DOI: 10.1007/s11263-016-0981-7), explicitly listing Stanford affiliations for the authors. This fulfills the requirement for explicit university mention, as the description highlights the academic origins.

In comparison, the GQA dataset, authored by Drew A. Hudson and Christopher D. Manning from Stanford, addresses shortcomings in prior VQA benchmarks by emphasizing real-world visual reasoning and compositional question answering. It boasts 22 million questions across 140,000 images in its full version, with the balanced subset providing 1.4 million questions (943,000 train, 132,000 val, 398,000 test), surpassing the 1 million row mark. Questions are generated using scene graphs from Visual Genome, ensuring diversity and reducing language biases through tunable smoothing techniques. The dataset is English-based, with structured semantic representations (functional programs) for each question to enable multi-step inference, spatial understanding, and logical operations.

Croissant metadata is confirmed available for GQA via the HF API, providing ML-ready field descriptions conforming to http://mlcommons.org/croissant/1.0 standards. The HuggingFace upload by echarlaix includes direct links to Stanford's NLP data server for images (https://downloads.cs.stanford.edu/nlp/data/gqa/images.zip), explicitly tying the release to Stanford University. This affiliation is further supported by the paper citation (@article{hudson2018gqa}), which credits Stanford researchers. GQA's design includes a suite of metrics beyond accuracy, such as consistency, validity, and plausibility, making it a robust tool for diagnosing model performance on different question types.

To organize the comparison, the following table summarizes key features of the two datasets:

| Feature                  | Visual Genome                                                                 | GQA                                                                                  |
|--------------------------|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Number of Rows (QA/Questions) | 1,773,258 QA pairs                                                            | 22M questions (full); 1.4M in balanced subset                                       |
| Number of Images         | 108,077                                                                       | 113,018                                                                              |
| Primary Focus            | Dense annotations for objects, attributes, relationships, and QA              | Compositional reasoning, bias mitigation, scene graph-based questions                |
| Language                 | English                                                                       | English                                                                              |
| Croissant Metadata       | Not confirmed via API                                                         | Confirmed available                                                                  |
| University Affiliation   | Stanford University (explicit in paper authors and DOI on HF page)            | Stanford University (explicit via data links and paper authors on HF page)           |
| Release Year             | 2017                                                                          | 2019                                                                                 |
| Citation Example         | Krishna et al., IJCV 2017                                                     | Hudson & Manning, CVPR 2019                                                          |

This table highlights how Visual Genome serves as a foundational dataset for broad visual understanding, while GQA builds on it for more targeted reasoning tasks. Both datasets have been widely adopted in the VQA community, with Visual Genome often used for pretraining models on dense visual concepts, and GQA for evaluating advanced reasoning capabilities. For instance, Visual Genome's QA pairs cover six question types (What, Where, When, Who, Why, How), providing a balanced distribution compared to earlier datasets. GQA, meanwhile, leverages a question engine to generate diverse questions from scene graphs, resulting in questions requiring multiple reasoning steps, with human performance at 89.3% versus model baselines around 54%.

In terms of data structure, Visual Genome's QA is stored in JSON format with fields like "qa_id", "image_id", "question", "answer", and object references, allowing easy loading via HF's datasets library with version-specific suffixes (e.g., "question_answer_v1.2.0"). GQA's structure includes questions with functional programs for semantics, enabling fine-grained analysis by question length, type, and topology. Both datasets use COCO and Flickr images, ensuring real-world variety, and Visual Genome's canonicalization to WordNet synsets enhances semantic consistency. Challenges in these datasets include potential biases, which GQA mitigates through answer distribution control and smoothing, while Visual Genome's crowdsourcing approach ensures diversity but requires careful canonicalization.

Overall, these datasets exemplify high-quality contributions from US academic institutions, facilitating progress in VQA research. Their availability on HuggingFace democratizes access, though users should note potential metadata gaps, such as unconfirmed Croissant for Visual Genome. Future extensions could include more explicit metadata integration to align with emerging standards like Croissant for better ML interoperability. Researchers interested in controversial aspects might explore counterarguments on dataset biases, as some studies suggest even balanced datasets like GQA retain subtle language priors, necessitating ongoing refinements.

### Key Citations
- [Visual Question Answering v2.0 Dataset | Papers With Code](https://paperswithcode.com/dataset/visual-question-answering-v2-0)
- [GQA: Visual Reasoning in the Real World](https://cs.stanford.edu/people/dorarad/gqa/about.html)
- [GQA: Visual Reasoning in the Real World](https://cs.stanford.edu/people/dorarad/gqa/)
- [[1902.09506] GQA: A New Dataset for Real-World Visual Reasoning and Compositional Question Answering](https://arxiv.org/abs/1902.09506)
- [Example QA pairs in the Visual Genome dataset. Our QA pairs cover a... | Download Scientific Diagram](https://www.researchgate.net/figure/Example-QA-pairs-in-the-Visual-Genome-dataset-Our-QA-pairs-cover-a-spectrum-of-visual_fig22_301844872)
- [Visual Genome Dataset | Papers With Code](https://paperswithcode.com/dataset/visual-genome)
- [ranjaykrishna/visual_genome · Datasets at Hugging Face](https://huggingface.co/datasets/ranjaykrishna/visual_genome)
- [Get Croissant metadata - Hugging Face](https://huggingface.co/docs/dataset-viewer/en/croissant)

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
https://huggingface.co/echarlaix

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
