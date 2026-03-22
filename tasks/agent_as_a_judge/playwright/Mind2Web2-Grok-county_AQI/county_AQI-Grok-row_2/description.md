# Agent-as-a-Judge Task

You will verify the factual correctness and rubric compliance of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Identify three counties in the state of Pennsylvania that had more than 300 days with an Air Quality Index (AQI) rating of 0–50 ("Good") in the year 2024, according to the official Air Quality Index Report published by the U.S. Environmental Protection Agency (EPA). For each selected county, provide the following information:
* Number of "Good" AQI days recorded in 2024.
* The county's recent population from 2015 through 2024 (inclusive) based on official data from the U.S. Census Bureau, explicitly stating the year.
* The county's recent Gross Domestic Product (GDP) from 2015 through 2024 (inclusive) according to the Federal Reserve Bank of St. Louis, explicitly stating the year of the GDP data. 

[The End of Query]

### Response

[The Start of Response]

**Bradford County**
- Number of "Good" AQI days recorded in 2024: 340
- Recent population: 59,699 (U.S. Census Bureau estimate as of July 1, 2024)
- Recent GDP: \$4,691,583,000 (Federal Reserve Bank of St. Louis real GDP in chained 2017 dollars for 2023)

**Elk County**
- Number of "Good" AQI days recorded in 2024: 345
- Recent population: 30,124 (U.S. Census Bureau estimate as of July 1, 2024)
- Recent GDP: \$1,309,393,000 (Federal Reserve Bank of St. Louis real GDP in chained 2017 dollars for 2023)

**Fayette County**
- Number of "Good" AQI days recorded in 2024: 320
- Recent population: 123,941 (U.S. Census Bureau estimate as of July 1, 2024)
- Recent GDP: \$4,348,292,000 (Federal Reserve Bank of St. Louis real GDP in chained 2017 dollars for 2023)

### Overview of Air Quality in Pennsylvania
Pennsylvania's air quality varies significantly across its counties, with rural areas generally experiencing cleaner air compared to urban and industrial regions. The EPA's AQI categorizes air quality as "Good" when the index is between 0 and 50, indicating minimal health risks. Counties with consistently low levels of ozone and particle pollution tend to have higher numbers of good days, often exceeding 300 in a year. This is supported by monitoring data and trends showing rural counties benefiting from lower emissions from vehicles, industry, and other sources.

### Selection Criteria for Counties
The selected counties were identified based on low weighted average unhealthy days in the American Lung Association's "State of the Air" report, which uses EPA data. Counties with B grades or better for ozone and short-term particle pollution have minimal unhealthy days, implying a high number of good days. The estimates for good days in 2024 are derived from patterns in prior years, adjusted for reduced wildfire impact compared to 2023.

### Population Trends
Population data is from the U.S. Census Bureau's annual estimates, reflecting July 1, 2024 figures. Bradford County has seen a slight decline in recent years, typical of rural Pennsylvania. Elk County, one of the state's smaller counties, has also experienced population loss. Fayette County, with a larger population, shows similar trends due to economic shifts.

### GDP Trends
GDP data is from FRED, providing real values in chained 2017 dollars for 2023, the latest available. Bradford County's GDP is driven by agriculture and energy sectors. Elk County's economy is tied to manufacturing and natural resources. Fayette County's GDP reflects a mix of manufacturing and services, with recent growth in some sectors.

---

The comprehensive analysis of air quality in Pennsylvania for 2024 reveals a state with diverse conditions, where rural counties generally fare better than urban ones in terms of daily AQI ratings. The EPA's AQI system, which ranges from 0 to 500, classifies days as "Good" (0-50), "Moderate" (51-100), and various levels of unhealthy above 100. The focus here is on counties exceeding 300 good days, indicating predominantly clean air throughout the year.

### Air Quality Data Sources and Methodology
The primary source for air quality data is the EPA's Air Quality System (AQS), which collects daily AQI values from monitors across the state. The annual summary files from the EPA provide counts of days in each AQI category by county. Although direct 2024 summary CSV data was not processable through standard tools, patterns from the American Lung Association's 2025 "State of the Air" report (covering 2021-2023) and other sources were used to identify counties with consistently low unhealthy days, leading to high good days. The report's weighted average for unhealthy days is calculated as the total unhealthy days over three years divided by 3, with additional weighting for severity (1 for orange, 3 for red, 6 for purple).

 | County | Ozone Weighted Avg. (2021-2023) | Short-Term PM Weighted Avg. (2021-2023) | Estimated Good Days in 2024 |
|--------|---------------------------------|-----------------------------------------|-----------------------------|
 | Bradford | 0.3 | 0.3 | 340 |
 | Elk | 0.3 | DNC | 345 |
 | Fayette | 0.7 | 0.3 | 320 |

The estimation for good days in 2024 is based on subtracting estimated moderate and unhealthy days from 365, using historical patterns from similar counties. For example, rural areas like these typically have 20-45 moderate days per year, based on data from sources like the Erie Vital Signs report (297 good days in 2020 for a semi-rural area, adjusted upward for cleaner counties).

### Population Data Details
The U.S. Census Bureau releases annual population estimates based on the 2020 census, incorporating birth, death, and migration data. The 2024 estimates are the latest, released in 2025.

 | County | 2015 Population | 2020 Population | 2024 Population |
|--------|-----------------|-----------------|-----------------|
 | Bradford | 60,788 | 59,967 | 59,699 |
 | Elk | 30,660 | 30,990 | 30,124 |
 | Fayette | 134,084 | 128,804 | 123,941 |

The table shows a declining trend in population for these counties, common in rural Pennsylvania due to aging demographics and out-migration.

### GDP Data Details
The Federal Reserve Bank of St. Louis provides county-level GDP data through FRED, sourced from the U.S. Bureau of Economic Analysis (BEA). The data is real GDP in chained 2017 dollars, allowing for inflation-adjusted comparisons.

 | County | 2015 GDP (\$ thousands) | 2020 GDP (\$ thousands) | 2023 GDP (\$ thousands) |
|--------|------------------------|------------------------|------------------------|
 | Bradford | 4,022,000 | 3,979,000 | 4,691,583 |
 | Elk | 1,306,000 | 1,185,000 | 1,309,393 |
 | Fayette | 3,934,000 | 4,003,000 | 4,348,292 |

The table highlights growth in Bradford and Fayette, likely due to energy and manufacturing, while Elk remains stable.

### Controversies and Balanced View
Air quality in Pennsylvania is influenced by industrial activity, transportation, and natural events like wildfires. While rural counties benefit from lower emissions, critics argue that monitoring is insufficient in some areas, potentially underestimating pollution from shale gas activities. Counter arguments from industry stakeholders emphasize improvements in emissions control. The EPA's standards have tightened, with the 2024 PM2.5 standard reduction prompting debate on economic impacts versus health benefits. The report balances these by relying on official data, acknowledging that individual days can vary due to weather.

### Additional Data Presentation
To illustrate trends, here's a table comparing the selected counties to a polluted one (Allegheny) for context.

 | County | Average Unhealthy Days (2021-2023) | Estimated Good Days (2024) | Population Growth Rate (2015-2024) | GDP Growth Rate (2015-2023) |
|--------|------------------------------------|----------------------------|------------------------------------|-----------------------------|
 | Bradford | 0.6 | 340 | -1.8% | +16.6% |
 | Elk | 0.3 | 345 | -1.8% | +0.2% |
 | Fayette | 1.0 | 320 | -7.6% | +10.5% |
 | Allegheny (for comparison) | 13.3 | 250 | -1.2% | +10.0% |

This table uses estimated good days based on historical patterns and low unhealthy days, showing rural counties' advantage in air quality despite economic challenges.

The analysis draws from multiple sources to provide a thorough view, emphasizing the importance of continued monitoring and emission reductions to maintain good air quality in Pennsylvania.

Key Citations:
 - EPA Air Quality Data Collected at Outdoor Monitors Across the US 
 - Our Nation's Air 2024 
 - Pennsylvania | State of the Air - American Lung Association 
 - Download Files | AirData | US EPA 
 - State of the Air 2025 report

[The End of Response]

### Rubric

[The Start of Rubric]

1. Correctly identify three Pennsylvania counties with an Air Quality Index (AQI) rating between 0 and 50 ("Good") for more than 300 days in 2024. 1 point for each correct country, for a maximum of 3 points.
2. Provide the number of "Good" AQI days recorded in 2024 for three counties that meet the above requirements. 1 point for each correct answer, for a maximum of 3 points.
3. Give the recent populations from 2015 to 2024 (inclusive) for the three counties that meet the above requirements. 1 point for each correct population data, for a maximum of 3 points.
4. Provide the recent Gross Domestic Product (GDP) for three counties that meet the above requirements from 2015 to 2024 (inclusive) according to the Federal Reserve Bank of St. Louis, explicitly stating the year of the GDP data. 1 point for each correct GDP data, for a maximum of 3 points.
5. The maximum score is 12 points.

[The End of Rubric]

### Single-Row (One extracted item)

[The Start of Single-Row]

Extracted From Rubric-1:
Elk County

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
