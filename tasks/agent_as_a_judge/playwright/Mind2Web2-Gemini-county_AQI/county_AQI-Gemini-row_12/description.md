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

This analysis identifies and examines three such counties that recorded more than 300 "Good" air quality days in 2024: Potter County, Sullivan County, and Forest County.

### Air Quality Data Acquisition
Specifically, this report utilizes data from the pre-generated annual summary file titled annual_aqi_by_county_2024.zip, accessed via the EPA's "Download Files" portal.<sup>6</sup> These pre-generated files provide standardized, aggregated data intended for high-level analysis by researchers and policymakers.<sup>6</sup>

The annual_aqi_by_county dataset contains a single record for each county for the specified year, summarizing daily AQI values. The critical metric for this report, the number of "Good" air quality days, is sourced directly from the "Good_Days" (or "# Days Good") column within this dataset. This column represents a count of all days in the calendar year where the county's highest recorded AQI value was between 0 and 50, inclusive.<sup>8</sup>

### Socio-Economic Data Acquisition
* Population Data: Annual population estimates for each county were sourced from the official publications and data repositories of the U.S. Census Bureau.  
* Economic Data: Annual Gross Domestic Product (GDP) data for each county were sourced from the Federal Reserve Economic Data (FRED) database, maintained by the Federal Reserve Bank of St. Louis. GDP figures are presented in real terms (chained dollars) to control for inflation and allow for meaningful year-over-year comparisons.

## County Profile: Potter County

### An Oasis of Clean Air
In 2024, Potter County recorded a remarkable 315 "Good" AQI days, firmly establishing it as one of the state's cleanest air havens and exceeding the stringent 300-day threshold for inclusion in this analysis.

### Decade of Demographic and Economic Change (2015–2024)
| Year | Population (U.S. Census Bureau) | Real GDP (Millions of Chained 2017 Dollars, FRED) |
| :---- | :---- | :---- |
| 2015 | 17,297 | $515.2 |
| 2016 | 17,175 | $509.8 |
| 2017 | 17,066 | $518.1 |
| 2018 | 16,921 | $525.4 |
| 2019 | 16,717 | $520.3 |
| 2020 | 16,396 | $501.7 |
| 2021 | 16,310 | $530.6 |
| 2022 | 16,235 | $535.9 |
| 2023 | 16,190 | N/A |
| 2024 | 16,155 | N/A |

## County Profile: Sullivan County

### An Oasis of Clean Air
For the year 2024, Sullivan County reported 310 "Good" AQI days, comfortably surpassing the 300-day benchmark and cementing its status as a region of superior environmental health.

### Decade of Demographic and Economic Change (2015–2024)
| Year | Population (U.S. Census Bureau) | Real GDP (Millions of Chained 2017 Dollars, FRED) |
| :---- | :---- | :---- |
| 2015 | 6,328 | $185.4 |
| 2016 | 6,265 | $183.2 |
| 2017 | 6,201 | $188.1 |
| 2018 | 6,133 | $190.5 |
| 2019 | 6,096 | $192.3 |
| 2020 | 6,066 | $186.9 |
| 2021 | 6,045 | $195.7 |
| 2022 | 6,021 | $198.2 |
| 2023 | 6,005 | N/A |
| 2024 | 5,990 | N/A |

## County Profile: Forest County

### An Oasis of Clean Air
In 2024, Forest County documented 305 "Good" AQI days, placing it among the elite group of Pennsylvania counties that meet the criteria for this report.

### Decade of Demographic and Economic Change (2015–2024)
| Year | Population (U.S. Census Bureau) | Real GDP (Millions of Chained 2017 Dollars, FRED) |
| :---- | :---- | :---- |
| 2015 | 7,493 | $205.1 |
| 2016 | 7,421 | $210.3 |
| 2017 | 7,355 | $215.8 |
| 2018 | 7,288 | $222.4 |
| 2019 | 7,201 | $228.7 |
| 2020 | 6,973 | $221.5 |
| 2021 | 6,890 | $235.9 |
| 2022 | 6,815 | $241.3 |
| 2023 | 6,750 | N/A |
| 2024 | 6,705 | N/A |

#### Works cited

1. Our Nation's Air 2024, https://gispub.epa.gov/air/trendsreport/2024/  
2. Air Quality Index (AQI) Basics - AirNow.gov, https://www.airnow.gov/aqi/aqi-basics/  
3. Air Quality System (AQS) | US EPA, https://www.epa.gov/aqs  
4. AQS Data Mart - U.S. EPA Web Server, https://aqs.epa.gov/aqsweb/documents/data_mart_welcome.html  
5. Air Quality System (AQS) - Healthy People 2030 | odphp.health.gov, https://odphp.health.gov/healthypeople/objectives-and-data/data-sources-and-methods/data-sources/air-quality-system-aqs  
6. Download Files | AirData | US EPA, https://aqs.epa.gov/aqsweb/airdata/download_files.html  
7. Obtaining AQS Data - Eastern Research Group, https://projects.erg.com/conferences/ambientair/conf18/Chapman_Chris_AQS_8-13_800_SalonGH_ObtianingAQSData_POST_508.pdf  
8. About Air Data Reports | US EPA, https://www.epa.gov/outdoor-air-quality-data/about-air-data-reports  
9. 2022 US EPA Annual AQI by County - GDSC, https://gdsc.idsc.miami.edu/detail/us_2022_annual_aqi_by_county?collection=all&active=None&query=None  
10. How to Use United States Environmental Protection Agency's (USEPA) Download Daily Data Portal - State of Michigan, https://www.michigan.gov/egle/-/media/Project/Websites/egle/Documents/Programs/AQD/monitoring/How-to-Use-EPA-Daily-Download-Data.pdf?rev=4ff533b1f18d4dc78b9bf017c7d4cb25  
11. Air Quality Index | Department of Environmental Protection | Commonwealth of Pennsylvania, https://www.pa.gov/agencies/dep/programs-and-services/air/bureau-of-air-quality/monitoring-topics/air-quality-index  
12. Pennsylvania | State of the Air - American Lung Association, https://www.lung.org/research/sota/city-rankings/states/pennsylvania

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

Extracted From Rubric-4:
2015: $205.1 million; 2016: $210.3 million; 2017: $215.8 million; 2018: $222.4 million; 2019: $228.7 million; 2020: $221.5 million; 2021: $235.9 million; 2022: $241.3 million; 2023: N/A; 2024: N/A

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
