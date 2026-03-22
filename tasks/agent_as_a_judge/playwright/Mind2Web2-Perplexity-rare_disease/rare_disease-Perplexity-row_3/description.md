# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

I’ve heard of a rare genetic disorder involving abnormal skull fusion generally caused by a genetic mutation in the FGFR2 gene, leading to abnormal shape of head and face, with no abnormalities of the hands or feet. Please identify this condition, and provide a webpage link that outlines both the common issues if left untreated and the common treatment options. Then, locate a doctor whose profile explicitly states that they specialize in this specific disease - not just a general term like Craniosynostosis -  and provide a direct link to their profile.

[The End of Query]

### Response

[The Start of Response]

# Crouzon Syndrome

**Crouzon syndrome** is a rare autosomal dominant genetic disorder caused by mutations in the FGFR2 gene, characterized by the premature fusion of cranial sutures leading to abnormal head and facial shape without abnormalities of the hands or feet.[^1]

## Untreated Complications and Treatment Options

A comprehensive overview of common complications if left untreated—such as increased intracranial pressure, airway compromise, sleep apnea, hydrocephalus, and vision problems—and multidisciplinary treatment approaches (including skull reshaping, frontal-orbital advancement, and midface advancement) is available on the Children’s Hospital of Philadelphia website:
https://www.chop.edu/conditions-diseases/crouzon-syndrome [^2]

## Specialist Profile

Dr. Jordan W. Swanson, MD, MSc
Plastic Surgeon, Children’s Hospital of Philadelphia
Top areas of expertise include Craniosynostosis, **Crouzon syndrome**, Metopic Ridge, Osteotomy, and Bone Graft.
Profile and booking information:
https://www.medifind.com/doctors/jordan-w-swanson/10080721 [^3]
<span style="display:none">[^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^20][^21][^22][^23][^4][^5][^6][^7][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://en.wikipedia.org/wiki/Crouzon_syndrome

[^2]: https://www.chop.edu/conditions-diseases/crouzon-syndrome

[^3]: https://www.medifind.com/doctors/jordan-w-swanson/10080721

[^4]: https://www.urmc.rochester.edu/childrens-hospital/craniofacial/treatment-crouzon.aspx

[^5]: https://www.medifind.com/conditions/crouzon-syndrome/1385/doctors

[^6]: https://cleftandcraniofacialinstituteofutah.com/crouzon-syndrome/

[^7]: https://www.myface.org/craniofacial-conditions/crouzonsyndrome/treatments/

[^8]: https://www.childrenshospital.org/conditions/crouzon-syndrome

[^9]: https://www.nationwidechildrens.org/conditions/crouzon-syndrome

[^10]: https://www.healthline.com/health/crouzon-syndrome

[^11]: https://www.gosh.nhs.uk/conditions-and-treatments/conditions-we-treat/crouzon-syndrome/

[^12]: https://www.medicalnewstoday.com/articles/321605

[^13]: https://www.chp.edu/our-services/plastic-surgery/conditions/crouzon-syndrome

[^14]: https://www.ccakids.org/assets/nl2017-01.pdf

[^15]: https://www.medifind.com/conditions/Pfeiffer Syndrome/4206/doctors

[^16]: https://www.instagram.com/p/CRzT4J9LCR3/?hl=en

[^17]: https://www.med.upenn.edu/globalhealth/jordan-w-swanson-md.html

[^18]: https://www.med.upenn.edu/apps/faculty/index.php/g275/p8763512

[^19]: https://www.lakesideschool.org/alumni/alumni-lives/jordan-swanson-98-surgery-for-the-people

[^20]: https://www.chop.edu/doctors/swanson-jordan-w/book-appointment

[^21]: https://www.instagram.com/reel/CN-xdFtjp2X/

[^22]: https://www.instagram.com/dr.jordanswanson/?hl=en

[^23]: https://www.instagram.com/p/C2Bb-6wLwEj/

[The End of Response]

### Rubric

[The Start of Rubric]

1. Correctly identifying this rare genetic disease earns 1 point.
2. Correctly providing a link that include an overview of the genetic disease, common issues prior to treatment, and typical treatment protocols earns 1 point.
3. Providing a doctor whose profile clearly states that they specialize in the disease and attaching a link to their profile earns 1 point.
4. Full score: 3 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-3:
https://www.medifind.com/doctors/jordan-w-swanson/10080721

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
