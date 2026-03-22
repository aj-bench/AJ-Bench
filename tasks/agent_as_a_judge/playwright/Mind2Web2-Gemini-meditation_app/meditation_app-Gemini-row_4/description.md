# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Identify two meditation apps from the U.S. Google Play Store that have more than 300,000 user ratings as of 2025 and job listings for software engineering-related positions online. For each app, provide a direct link to its Play Store page, the app's official website, and a direct link to a software engineering-related job listing.

[The End of Query]

### Response

[The Start of Response]

# Identification of Qualifying Applications

The analysis confirms that Calm and Headspace are the sole applications that satisfy the specified criteria, positioning them as the definitive market leaders for this investigation.

- Calm
  - Google Play Store: https://play.google.com/store/apps/details?id=com.calm.android
  - Official website: https://www.calm.com/
  - Software engineering job listing: https://job-boards.greenhouse.io/calm/jobs/7983107002

- Headspace
  - Google Play Store: https://play.google.com/store/apps/details?id=com.getsomeheadspace.android
  - Official website: https://www.headspace.com/
  - Software engineering job listing: https://job-boards.greenhouse.io/hs/jobs/6786108

## Works cited

1. Insight Timer - Meditation App - Apps on Google Play, https://play.google.com/store/apps/details?id=com.spotlightsix.zentimerlite2  
2. Happier meditation - Apps on Google Play, https://play.google.com/store/apps/details?id=com.changecollective.tenpercenthappier  
3. Calm - Sleep, Meditate, Relax - Apps on Google Play, https://play.google.com/store/apps/details?id=com.calm.android  
4. Headspace: Meditation & Health - Apps on Google Play, https://play.google.com/store/apps/details?id=com.getsomeheadspace.android  
5. Headspace: Meditation & Health on the App Store, https://apps.apple.com/us/app/headspace-meditation-health/id493145008  
6. Calm - The #1 App for Meditation and Sleep, https://www.calm.com/  
7. Sleep more and stress less with 40% off of Calm Premium, https://www.calm.com/livemore  
8. Android Apps by Calm.com, Inc. on Google Play, https://play.google.com/store/apps/developer?id=Calm.com,+Inc.  
9. Calm on the App Store, https://apps.apple.com/us/app/calm/id571800810  
10. Daily Calm - Calm - The #1 App for Meditation and Sleep, https://www.calm.com/app  
11. Support your team with the #1 app for meditation and sleep - Calm Health, https://health.calm.com/calm-for-organizations/  
12. Calm Health: Mental Health Solutions App for Organizations, https://health.calm.com/  
13. Job Application for Full Stack Software Engineer at Calm - Greenhouse, https://job-boards.greenhouse.io/calm/jobs/7983107002  
14. Software Engineers - Backend - Calm | Built In NYC, https://www.builtinnyc.com/job/software-engineers-backend/6291075  
15. Mental Wellness App: Meditation & Sleep - Headspace, https://www.headspace.com/app  
16. Headspace: Mental Health App for Meditation & Sleep, https://www.headspace.com/  
17. Android Apps by Headspace for Meditation, Mindfulness and Sleep on Google Play, https://play.google.com/store/apps/developer?id=Headspace+for+Meditation,+Mindfulness+and+Sleep  
18. Subscribe to Headspace, https://www.headspace.com/subscriptions  
19. Job Application for Software Engineer, API at Headspace - Greenhouse, https://job-boards.greenhouse.io/hs/jobs/6786108  
20. 12+ Software Jobs Hiring at Headspace 1-Click Apply Now, https://www.ziprecruiter.com/co/headspace/Jobs/Software  
21. HEADSPACE Jobs in California (Now Hiring) Aug 2025, https://www.ziprecruiter.com/co/headspace/Jobs/--in-California  
22. Staff Software Engineer, Full Stack - Headspace | Built In NYC, https://www.builtinnyc.com/job/staff-software-engineer-full-stack/4738344  
23. Headspace Jobs - Wellfound, https://wellfound.com/company/headspace/jobs  
24. Headspace jobs in Remote - Indeed, https://www.indeed.com/m/jobs?q=Headspace&l=Remote

[The End of Response]

### Rubric

[The Start of Rubric]

1. Identify Identify two meditation apps from the U.S. Google Play Store that have more than 300,000 user ratings as of 2025 and job listings for software engineering-related positions online. Award 1 point for each qualifying app identified, up to 2 points.
2. For apps meeting the above criteria, provide their corresponding Google Play Store page links. Award 1 point for each valid link provided, up to 2 points.
3. Provide the official website for each identified app. Award 1 point for each correct website provided, up to 2 points.
4. Provide the direct link to software engineering-related job listings for each identified app. Award 1 point for each valid job listing link provided, up to 2 points.
5. The total possible score is 8 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-2:
https://play.google.com/store/apps/details?id=com.getsomeheadspace.android

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
