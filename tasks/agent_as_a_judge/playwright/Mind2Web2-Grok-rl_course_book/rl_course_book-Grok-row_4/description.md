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

- **Stanford University**: CS234: Reinforcement Learning, taught by Emma Brunskill. Course page: [http://web.stanford.edu/class/cs234/](http://web.stanford.edu/class/cs234/). Recommended book: *Artificial Intelligence: A Modern Approach* by Stuart J. Russell and Peter Norvig.
- **Carnegie Mellon University (CMU)**: 10-703: Deep Reinforcement Learning, taught by Katerina Fragkiadaki. Course page: [https://cmudeeprl.github.io/703website_f24/](https://cmudeeprl.github.io/703website_f24/). Recommended book: *Reinforcement Learning: An Introduction* by Richard S. Sutton and Andrew G. Barto.
- **UC Berkeley**: CS285: Deep Reinforcement Learning, taught by Sergey Levine. Course page: [https://rail.eecs.berkeley.edu/deeprlcourse/](https://rail.eecs.berkeley.edu/deeprlcourse/). Recommended book: *Algorithms for Reinforcement Learning* by Csaba Szepesvari.

These courses represent current offerings in reinforcement learning as of 2025, focusing on foundational and advanced concepts. The selected books are distinct, widely recommended in their respective courses, and available in physical formats such as paperback or hardcover from major booksellers.

### Course Overviews
Each course provides a comprehensive introduction to reinforcement learning (RL), with variations in emphasis. Stanford's CS234 covers core RL challenges and approaches, suitable for students new to the field. CMU's 10-703 integrates deep learning with RL for control applications, drawing on multiple AI disciplines. UC Berkeley's CS285 emphasizes deep RL methods, particularly for decision-making and robotics.

### Book Availability
All selected books are established references in AI and RL:
- *Artificial Intelligence: A Modern Approach* is available in hardcover and explores broad AI topics, including RL.
- *Reinforcement Learning: An Introduction* comes in paperback and serves as a foundational text for RL algorithms.
- *Algorithms for Reinforcement Learning* is offered in both paperback and hardcover, focusing on theoretical RL algorithms.

---
Reinforcement learning (RL) courses at top universities like Stanford, Carnegie Mellon University (CMU), and UC Berkeley continue to evolve, incorporating the latest advancements in AI as of 2025. These programs typically build on prerequisites in machine learning, probability, and programming, preparing students for research and applications in areas such as robotics, gaming, and autonomous systems. Below is a detailed examination of one selected RL course per university, including instructors, course links, and a unique recommended reference book drawn from the course materials. The books were chosen to avoid duplication and confirmed for availability in physical formats (paperback or hardcover) through major retailers.

### Stanford University: CS234 - Reinforcement Learning
Offered in Winter 2025, this course provides a solid introduction to RL, covering Markov decision processes, value functions, policy gradients, and practical algorithms. It addresses core challenges like exploration-exploitation trade-offs and scalability. The course is designed for graduate students but accessible to advanced undergraduates with machine learning backgrounds.

- **Instructor**: Emma Brunskill, Associate Professor of Computer Science, whose research focuses on RL for decision-making in education and healthcare.
- **Course Page**: [http://web.stanford.edu/class/cs234/](http://web.stanford.edu/class/cs234/)
- **Selected Reference Book**: *Artificial Intelligence: A Modern Approach* by Stuart J. Russell and Peter Norvig. This comprehensive AI textbook includes sections on RL within a broader context of intelligent agents and search algorithms. It is available in hardcover from publishers like Pearson.

The course references multiple resources, but this book stands out for its holistic view of AI, complementing RL-specific topics.

### Carnegie Mellon University (CMU): 10-703 - Deep Reinforcement Learning
This Fall 2024 offering (expected to continue similarly in 2025) combines deep learning with RL for control tasks, covering topics like Q-learning, actor-critic methods, and applications in robotics. It emphasizes interdisciplinary approaches from AI, including neural networks and optimization.

- **Instructor**: Katerina Fragkiadaki, whose work spans computer vision and RL for embodied agents.
- **Course Page**: [https://cmudeeprl.github.io/703website_f24/](https://cmudeeprl.github.io/703website_f24/)
- **Selected Reference Book**: *Reinforcement Learning: An Introduction* by Richard S. Sutton and Andrew G. Barto. This seminal text introduces RL fundamentals, including temporal-difference learning and multi-armed bandits. It is widely available in paperback from MIT Press.

Historical iterations of the course (e.g., Fall 2018) also involved Tom Mitchell, but recent sections highlight Fragkiadaki's leadership. The book is a core recommendation across CMU's RL curriculum.

### UC Berkeley: CS285 - Deep Reinforcement Learning
Focused on deep RL for real-world applications, this course covers model-free and model-based methods, imitation learning, and offline RL. Lectures emphasize practical implementations in robotics and control, with assignments involving coding in frameworks like PyTorch.

- **Instructor**: Sergey Levine, a leading researcher in RL and robotics, known for contributions to algorithms like soft actor-critic.
- **Course Page**: [https://rail.eecs.berkeley.edu/deeprlcourse/](https://rail.eecs.berkeley.edu/deeprlcourse/)
- **Selected Reference Book**: *Algorithms for Reinforcement Learning* by Csaba Szepesvari. This book delves into theoretical foundations, including convergence proofs and sample complexity in MDPs. It is available in both paperback and hardcover from Morgan & Claypool Publishers.

The course resources list several texts, but this one provides a rigorous algorithmic perspective, distinguishing it from more introductory materials.

### Comparative Table of Courses and Books

| University    | Course Code & Title                  | Instructor(s)              | Key Topics Covered                          | Recommended Book Title & Author(s)                  | Physical Format Availability |
|---------------|--------------------------------------|----------------------------|---------------------------------------------|-----------------------------------------------------|-------------------------------|
| Stanford     | CS234: Reinforcement Learning       | Emma Brunskill            | MDPs, value iteration, policy gradients, deep RL basics | *Artificial Intelligence: A Modern Approach* by Stuart J. Russell and Peter Norvig | Hardcover                    |
| CMU          | 10-703: Deep Reinforcement Learning | Katerina Fragkiadaki      | Q-learning, actor-critic, control applications, neural networks | *Reinforcement Learning: An Introduction* by Richard S. Sutton and Andrew G. Barto | Paperback                    |
| UC Berkeley  | CS285: Deep Reinforcement Learning  | Sergey Levine             | Model-based RL, imitation learning, offline RL, robotics | *Algorithms for Reinforcement Learning* by Csaba Szepesvari | Paperback/Hardcover          |

This table highlights differences in focus: Stanford leans introductory, CMU integrates control, and Berkeley emphasizes applications. All courses assume familiarity with machine learning; prerequisites include courses like CS229 (Stanford), 10-701 (CMU), or CS189 (Berkeley).

### Additional Context on Book Selections
The books were selected directly from course pages or associated resources to ensure relevance:
- Stanford's CS234 lists Russell and Norvig's book as a key reference for AI foundations.
- CMU's 10-703 historically recommends Sutton and Barto for core RL concepts.
- Berkeley's CS285 resources explicitly include Szepesvari's text for algorithmic depth.

Availability was verified through online booksellers: *Artificial Intelligence: A Modern Approach* (4th edition) in hardcover; *Reinforcement Learning: An Introduction* (2nd edition) in paperback; *Algorithms for Reinforcement Learning* in both formats. These texts are non-overlapping, providing diverse perspectives—from broad AI integration to theoretical algorithms.

These courses reflect the growing importance of RL in AI, with ongoing updates to incorporate 2025 trends like scalable RL and multi-agent systems. Students interested in enrollment should check university catalogs for 2025 schedules, as offerings may vary slightly.

**Key Citations:**
-  CS234: Reinforcement Learning Winter 2025 - Stanford University - http://web.stanford.edu/class/cs234/
-  CS 234: Reinforcement Learning - Explore Courses - https://explorecourses.stanford.edu/search?view=catalog&filter-coursestatus-Active=on&q=CS%2520234:%2520Reinforcement%2520Learning&academicYear=20242025
-  10-703 Deep RL - https://cmudeeprl.github.io/703website_f24/
-  Deep Reinforcement Learning and Control Fall 2018, CMU 10703 - https://www.andrew.cmu.edu/course/10-703/
-  Deep Reinforcement Learning - Berkeley RAIL Lab - https://rail.eecs.berkeley.edu/deeprlcourse/
-  Deep Reinforcement Learning - Berkeley RAIL Lab - https://rail.eecs.berkeley.edu/deeprlcourse/
-  CS 285 Resources - Berkeley RAIL Lab - http://rail.eecs.berkeley.edu/deeprlcourse/resources/
-  Artificial Intelligence: A Modern Approach (Pearson Series in Artifical ... - https://www.amazon.com/Artificial-Intelligence-A-Modern-Approach/dp/0134610997
-  Sutton Reinforcement Learning - Amazon.com - https://www.amazon.com/sutton-reinforcement-learning/s?k=sutton%2Breinforcement%2Blearning
-  Algorithms for Reinforcement Learning (Synthesis Lectures on ... - https://www.amazon.com/Algorithms-Reinforcement-Synthesis-Artificial-Intelligence/dp/303100423X

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
Artificial Intelligence: A Modern Approach by Stuart J. Russell and Peter Norvig

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
