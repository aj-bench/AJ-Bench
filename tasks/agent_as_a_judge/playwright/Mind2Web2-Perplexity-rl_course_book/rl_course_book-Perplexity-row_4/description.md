# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Search for reinforcement learning (RL) courses offered by Stanford, CMU, and UC Berkeley as of 2025. For each university, identify one RL course and provide the instructor name(s) and a link to the course page. From each course’s page, select one textbook or reference book that is used or recommended in the course. Ensure that the selected book is different for each university (i.e., no duplicates across the three courses), and that it is available in either paperback or hardcover format from a bookseller. For each selected book, include its title and author(s).

[The End of Query]

### Response

[The Start of Response]

# Reinforcement Learning Courses at Stanford, CMU, and UC Berkeley (2025)

**Main Recommendation:**
To gain a broad yet rigorous grounding in reinforcement learning (RL), enroll in one of the three flagship RL courses below. Each features a distinct textbook offering complementary perspectives—from foundational theory to modern deep RL—ensuring a well-rounded education without overlap.

***

## Stanford University

**Course**: CS 234: Reinforcement Learning
**Instructor**: Emma Brunskill
**Course Page**: http://web.stanford.edu/class/cs234/

**Selected Textbook**
Title: Reinforcement Learning: An Introduction
Authors: Richard S. Sutton and Andrew G. Barto

***

## Carnegie Mellon University

**Course**: 10-703: Deep Reinforcement Learning and Control
**Instructor**: Katerina Fragkiadaki
**Course Page**: https://cmudeeprl.github.io/703website_f24/

**Selected Textbook**
Title: Deep Learning
Authors: Ian Goodfellow, Yoshua Bengio, and Aaron Courville

***

## University of California, Berkeley

**Course**: CS 285: Deep Reinforcement Learning
**Instructor**: Sergey Levine
**Course Page**: https://rail.eecs.berkeley.edu/deeprlcourse/

**Selected Textbook**
Title: Algorithms for Reinforcement Learning
Author: Csaba Szepesvári

***

Each of these books is readily available in paperback or hardcover from major booksellers.
<span style="display:none">[^1][^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^2][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^3][^4][^5][^6][^7][^8][^9]</span>

<div style="text-align: center">⁂</div>

[^1]: https://github.com/tallamjr/stanford-cs234

[^2]: https://cmudeeprl.github.io/403website_s22/

[^3]: https://csdiy.wiki/en/深度学习/CS285/

[^4]: https://github.com/charlesyou999648/CS234_RL

[^5]: https://cmudeeprl.github.io/703website_f24/

[^6]: https://rail.eecs.berkeley.edu/deeprlcourse/

[^7]: https://www.reddit.com/r/reinforcementlearning/comments/1gghbth/now_available_on_youtube_stream_all_the_lectures/

[^8]: https://www.reddit.com/r/reinforcementlearning/comments/t30od4/courses_needed_to_become_proficient_in/

[^9]: https://rail.eecs.berkeley.edu/deeprlcourse-fa20/

[^10]: https://www.youtube.com/watch?v=WsvFL-LjA6U

[^11]: https://www.andrew.cmu.edu/course/10-703/

[^12]: https://github.com/mohammadasghari/UC-Berkeley-CS-294-Deep-RL

[^13]: https://www.youtube.com/watch?v=FgzM3zpZ55o

[^14]: https://campusai.github.io/theory/

[^15]: https://web.stanford.edu/class/cs234/slides/lecture1pre.pdf

[^16]: https://bulletin.stanford.edu/courses/2190451

[^17]: https://web.stanford.edu/class/cs234/modules.html

[^18]: http://web.stanford.edu/class/cs234/

[^19]: https://web.stanford.edu/class/cs234/assignments.html

[^20]: https://web.stanford.edu/class/cs234/project.html

[^21]: https://explorecourses.stanford.edu/search?view=catalog\&filter-coursestatus-Active=on\&q=CS+234%3A+Reinforcement+Learning\&academicYear=20242025

[^22]: https://explorecourses.stanford.edu/search?q=CS234

[^23]: https://github.com/harryzhangOG/Deep-RL-Notes

[^24]: https://mandi-zhao.gitbook.io/deeprl-notes

[^25]: https://www.reddit.com/r/MachineLearning/comments/db8c4u/n_uc_berkeleys_cs_285_deep_reinforcement_learning/

[^26]: https://ivlabs.github.io/resources/reinforcement-learning/

[^27]: http://rail.eecs.berkeley.edu/deeprlcourse/resources/

[^28]: https://www.cs.ubc.ca/~van/cpsc533/rl.html

[^29]: https://towardsdatascience.com/best-free-courses-and-resources-to-learn-reinforcement-learning-ed6633608cb2/

[The End of Response]

### Rubric

[The Start of Rubric]

1. Provide the reinforcement learning (RL) courses offered by Stanford University, Carnegie Mellon University, and UC Berkeley until 2025. For each university, identify 1 RL course and provide the instructor name(s) and a link to the course page. 1 point for a piece of correct information, for a maximum of 3 points;
2. From each pprovided course's page, select one textbook or reference book that is used or recommended in the corresponding course. Ensure that the selected book is different for each university (i.e., no duplicates across the three courses), and that it is available in either paperback or hardcover format from a bookseller. For each selected book, include its title and author(s). 1 point for correctly providing all required information for a book, for a maximum of 3 points.
3. Total score: 6 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-2:
Reinforcement Learning: An Introduction by Richard S. Sutton and Andrew G. Barto

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
