# Agent-as-a-Judge Task

You will verify the factual correctness of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Could you please give me a demographic brief analyzing the shifting racial composition of new U.S. citizens since 2002? This requires a year-by-year breakdown of their original birthplace composition from 2002 to 2022. Using U.S. Department of Homeland Security Yearbook of Immigration Statistics, the Annual Flow Reports, and archived USCIS Factsheets, compile the following metrics for each fiscal year from 2002 through 2022 (including 2022) and provide corresponding official links to support your statement.

Please output the results in one Markdown table with columns, in this exact order:
Year | Total Naturalized | Born in Africa | Born in Asia | Born in Europe | Born in Caribbean | Born in Central America| Born in other North America | Born in Oceania | Born in South America

[The End of Query]

### Response

[The Start of Response]

# **The Evolving Profile of New American Citizens: A Statistical Compendium (2002-2022)**

The empirical foundation for understanding the changing composition of new U.S. citizens is the year-by-year statistical data on their region of birth. The following table presents a comprehensive 21-year dataset compiled from official DHS and U.S. Citizenship and Immigration Services (USCIS) sources. The data tracks the total number of persons naturalized each fiscal year and disaggregates that total by the six major geographic regions of birth as defined by DHS. For enhanced analytical clarity, the "North America" category, as reported in source documents, has been further broken down into its three constituent sub-regions: the Caribbean, Central America, and Other North America (primarily comprising Mexico and Canada).

This detailed breakdown allows for a nuanced examination of the distinct migration and naturalization patterns that exist within the Western Hemisphere. The data reveals both long-term secular trends and sharp annual fluctuations, which are analyzed in subsequent sections of this report.

| Year | Total Naturalized | Born in Africa | Born in Asia | Born in Europe | Born in Caribbean | Born in Central America | Born in other North America | Born in Oceania | Born in South America |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 2022 | 969,380 | 106,094 | 361,176 | 92,240 | 129,484 | 43,483 | 151,443 | 5,260 | 79,980 |
| 2021 | 813,861 | 76,009 | 295,224 | 77,090 | 115,220 | 41,310 | 131,900 | 4,300 | 72,700 |
| 2020 | 628,254 | 66,436 | 246,099 | 57,403 | 80,879 | 30,703 | 92,668 | 3,392 | 50,441 |
| 2019 | 843,593 | 84,990 | 327,273 | 81,040 | 101,312 | 42,077 | 133,521 | 4,308 | 68,678 |
| 2018 | 761,901 | 64,934 | 275,621 | 71,436 | 95,298 | 40,815 | 141,479 | 3,792 | 67,892 |
| 2017 | 707,265 | 61,851 | 255,306 | 65,141 | 92,540 | 39,359 | 126,472 | 3,327 | 63,063 |
| 2016 | 753,060 | 72,338 | 271,733 | 74,344 | 105,204 | 41,649 | 112,992 | 3,953 | 70,821 |
| 2015 | 730,259 | 71,492 | 261,374 | 78,074 | 92,807 | 39,160 | 115,525 | 3,811 | 67,927 |
| 2014 | 653,416 | 62,175 | 233,163 | 71,325 | 83,376 | 35,866 | 103,305 | 3,399 | 60,665 |
| 2013 | 779,929 | 71,872 | 275,700 | 80,333 | 120,995 | 42,682 | 108,130 | 3,849 | 76,167 |
| 2012 | 757,434 | 74,775 | 257,035 | 82,714 | 109,762 | 40,592 | 111,319 | 3,886 | 76,992 |
| 2011 | 694,193 | 69,738 | 249,940 | 82,209 | 79,820 | 33,784 | 104,146 | 3,734 | 70,485 |
| 2010 | 619,913 | 64,022 | 251,598 | 78,011 | 62,483 | 25,706 | 75,647 | 3,646 | 58,474 |
| 2009 | 743,715 | 60,383 | 276,375 | 90,214 | 84,860 | 43,914 | 121,435 | 3,928 | 61,666 |
| 2008 | 1,046,539 | 80,080 | 260,044 | 99,513 | 131,935 | 86,168 | 244,269 | 4,314 | 71,753 |
| 2007 | 660,477 | 41,652 | 238,797 | 104,272 | 68,577 | 41,814 | 130,772 | 5,629 | 62,334 |
| 2006 | 702,589 | 50,397 | 242,674 | 112,553 | 90,979 | 38,463 | 93,644 | 4,683 | 68,117 |
| 2005 | 604,280 | 38,830 | 237,724 | 97,482 | 55,472 | 35,011 | 90,089 | 3,898 | 44,504 |
| 2004 | 537,151 | 34,531 | 199,650 | 101,343 | 58,181 | 31,080 | 63,840 | 3,080 | 44,176 |
| 2003 | 463,204 | 41,780 | 191,772 | 49,244 | 56,351 | 12,838 | 71,957 | 2,822 | 41,780 |
| 2002 | 573,708 | 32,878 | 216,081 | 104,834 | 72,559 | 28,155 | 65,441 | 3,463 | 49,918 |

Sources: U.S. Department of Homeland Security, Yearbook of Immigration Statistics (2002-2022 editions) and U.S. Naturalizations Annual Flow Reports (2002-2022 editions). Data for each year is compiled from the "Persons Naturalized by Region and Country of Birth" tables contained within these publications.<sup>11</sup> The breakdown of North America into its constituent sub-regions is derived from tables that provide this level of detail.<sup>7</sup>

## **In-Depth Analysis of Regional Origin Trends**

A granular examination of the data reveals four determinative trends that have reshaped the demographic landscape of new U.S. citizens over the past two decades: the consolidation of Asia as a primary source region; the persistent and multifaceted strength of the Americas; the relative decline of Europe from its historical position; and the significant emergence of Africa as a growing source of new Americans.

### **The Ascendancy of Asia: The New Center of Gravity**

Throughout the 2002-2022 period, Asia has cemented its role as the leading region of birth for new U.S. citizens. In nearly every year, individuals born in Asian countries have constituted the largest or second-largest regional bloc, consistently representing over one-third of all persons naturalized.<sup>5</sup> This trend is not a recent phenomenon but rather the continuation of a shift that began in the 1970s, when Asia first surpassed Europe as the primary source region, driven by changes in immigration law and the arrival of Indochinese refugees.<sup>2</sup>

The strength and stability of this trend are rooted in the diversity of immigration pathways that lead to citizenship for Asian-born individuals. The top source countries—consistently including India, the Philippines, the People's Republic of China, and Vietnam—represent a wide spectrum of U.S. immigration categories.<sup>3</sup> Many immigrants from India and China, for example, initially arrive on employment-based visas, reflecting the high demand for skilled labor in the U.S. economy. Immigrants from the Philippines often utilize both employment and family-sponsored preference categories. Meanwhile, the significant number of naturalizations from Vietnam is, in part, a generational echo of the large-scale refugee resettlement that followed the Vietnam War, which established a substantial population of lawful permanent residents (LPRs) who would become eligible for citizenship in subsequent decades.<sup>2</sup>

This diversification of pathways provides a resilient foundation for the flow of new citizens from Asia. Unlike regions that may be more heavily dependent on a single class of admission, the multi-channeled nature of Asian immigration means that changes to one specific visa category are less likely to dramatically alter the overall trend. This suggests that Asia will remain a, if not the, principal source of new American citizens for the foreseeable future.

### **The Enduring Significance of the Americas**

While Asia as a continent is a leading source, the combined nations of the Americas—encompassing Mexico, the Caribbean, and Central America—represent an equally powerful and defining force in U.S. naturalization trends. When analyzed collectively, this bloc consistently accounts for over a third of all new citizens each year, rivaling Asia for the top position.<sup>7</sup> A key to understanding this region's impact is to disaggregate the broad "North America" category used in many official reports into its distinct sub-regions.

**Mexico**, categorized under "Other North America," stands in a class of its own. Year after year, it is the single largest country of birth for new citizens, frequently comprising 13 to 17 percent of the total annual cohort.<sup>6</sup> This reflects Mexico's deep and long-standing demographic, economic, and social ties to the United States.

The **Caribbean** is another major contributor, consistently sending a large number of new citizens. The Dominican Republic, Cuba, and Jamaica are perennially among the top 10 or 15 source countries globally, underscoring the region's significant role in American immigration patterns.<sup>3</sup>

**Central America**, while contributing smaller absolute numbers, is also a noteworthy source, with El Salvador consistently ranking as a significant country of origin for naturalizing citizens.<sup>3</sup>

A distinguishing characteristic of this regional cohort, particularly those from Mexico and Central America, is the longer median time they spend in LPR status before naturalizing. While immigrants from Africa and Asia typically naturalize within a median of 6 to 7 years of receiving LPR status, the median for those from North America is often 10 years or longer.<sup>9</sup> Several factors may contribute to this extended timeline. Geographic proximity may reduce the perceived urgency of formalizing citizenship, as ties to the home country are easier to maintain.<sup>23</sup> Furthermore, a substantial portion of this population became eligible for LPR status through the Immigration Reform and Control Act (IRCA) of 1986, a pathway that involved different timelines and socioeconomic profiles than other immigration streams.<sup>2</sup> This longer "incubation period" suggests the existence of a large, latent pool of LPRs from the Americas who are eligible to naturalize. This population can be activated by specific triggers, such as political campaigns or proposed changes to immigration law, making them a critical and somewhat unpredictable variable in future naturalization statistics.

### **The Recalibration of European Origins**

The data from 2002 to 2022 illustrates a fundamental recalibration of Europe's role as a source of new American citizens. While historically the dominant wellspring of immigration to the United States, Europe's contribution to the naturalizing class has settled into a new, more modest phase. Throughout the period, the proportion of new citizens born in Europe has consistently hovered around 10 percent of the annual total, a sharp departure from the majorities seen in earlier eras.<sup>5</sup>

This trend should not be interpreted as a cessation of European immigration but rather as a shift in its composition and a reflection of historical migration cycles. The decline in the share of naturalizations from traditional Western and Southern European countries is a long-term consequence of post-World War II economic prosperity and demographic stabilization in those nations, which led to lower rates of emigration.<sup>25</sup>

The sustained flow of new citizens from Europe during this period is now primarily driven by individuals from Eastern European nations. This reflects migration patterns that emerged following the end of the Cold War and the conflicts in the Balkans during the 1990s. Many individuals from countries such as Ukraine, Poland, and Bosnia-Herzegovina arrived in the United States as refugees, asylees, or through family-based migration in the 1990s and early 2000s, becoming eligible for citizenship during the timeframe of this report.<sup>14</sup> Therefore, the story of European naturalization in the 21st century is one of an internal demographic shift from west to east. This implies that future trends in naturalization from Europe will be closely linked to the ongoing geopolitical and economic stability of the former Soviet bloc and Balkan states.

### **The Emergence of Africa as a Key Source Region**

One of the most significant demographic stories of the past two decades is the steady and accelerating emergence of Africa as a key source of new U.S. citizens. While starting from a smaller numerical base than other regions, the number of naturalizations of African-born individuals has demonstrated consistent and robust growth. By the latter half of the 2002-2022 period, Africa regularly accounted for approximately 10 percent of all new citizens annually, establishing itself as a major and growing component of the naturalizing population.<sup>1</sup>

Beyond the growing numbers, a notable characteristic of this group is its high propensity to naturalize relatively quickly after becoming eligible. The median time spent in LPR status for African-born immigrants before becoming citizens is among the shortest of any regional group, typically around six years.<sup>9</sup> This rapid rate of civic integration points to a strong desire to establish permanent roots in the United States.

This trend is likely connected to the specific immigration pathways through which many Africans arrive. A significant number enter through the Diversity Visa program, which by design draws immigrants from countries with historically low rates of immigration to the U.S. Others arrive as refugees or are granted asylum.<sup>26</sup> For these individuals, the prospect of returning to their country of origin may be limited or nonexistent, fostering a greater incentive to seek the stability, rights, and protections afforded by U.S. citizenship. As long as these immigration pathways remain viable, Africa is poised to become an increasingly influential source of new Americans, contributing to the nation's growing diversity.

#### **Work cited**

1. Fiscal Year 2020 US Naturalizations Annual Flow Report, [https://cis.org/sites/default/files/2022-01/21\_1004\_plcy\_naturalizations\_fy2020.pdf](https://cis.org/sites/default/files/2022-01/21_1004_plcy_naturalizations_fy2020.pdf)  
2. Naturalizations in the United States: 2008 \- Office of Homeland ..., [https://ohss.dhs.gov/sites/default/files/2023-12/Naturalizations\_2008.pdf](https://ohss.dhs.gov/sites/default/files/2023-12/Naturalizations_2008.pdf)  
3. U.S. Naturalizations: 2020\. Annual Flow Report. \- Office of ..., [https://ohss.dhs.gov/sites/default/files/2023-12/2021\_1004\_plcy\_naturalizations\_fy2020v2.pdf](https://ohss.dhs.gov/sites/default/files/2023-12/2021_1004_plcy_naturalizations_fy2020v2.pdf)  
4. Spotlight on Naturalization Trends in 2008 | migrationpolicy.org, [https://www.migrationpolicy.org/article/spotlight-naturalization-trends-2008](https://www.migrationpolicy.org/article/spotlight-naturalization-trends-2008)  
5. Table 21\. Persons Naturalized by Region and Country of Birth: Fiscal Years 2011 to 2020, [https://ohss.dhs.gov/topics/immigration/yearbook/2020/table21](https://ohss.dhs.gov/topics/immigration/yearbook/2020/table21)  
6. U.S. Naturalizations: 2016\. Annual Flow Report. \- Office of ..., [https://ohss.dhs.gov/sites/default/files/2023-12/Naturalizations\_2016.pdf](https://ohss.dhs.gov/sites/default/files/2023-12/Naturalizations_2016.pdf)  
7. U.S. Naturalizations: 2019 \- Annual Flow Report August 2020, [https://ohss.dhs.gov/sites/default/files/2023-12/21\_0824\_plcy\_naturalizations\_fy2019.pdf](https://ohss.dhs.gov/sites/default/files/2023-12/21_0824_plcy_naturalizations_fy2019.pdf)  
8. Article: Naturalization Trends in the United States | migrationpolicy.org, [https://www.migrationpolicy.org/article/naturalization-trends-united-states-2017](https://www.migrationpolicy.org/article/naturalization-trends-united-states-2017)  
9. Characteristics of People Who Naturalized Between FY 2015 and FY 2019 \- USCIS, [https://www.uscis.gov/sites/default/files/document/reports/Characteristics\_of\_People\_Who\_Natzd\_Between\_FY15andFY19.pdf](https://www.uscis.gov/sites/default/files/document/reports/Characteristics_of_People_Who_Natzd_Between_FY15andFY19.pdf)  
10. U.S. Naturalizations: 2022 Annual Flow Report \- Office of Homeland ..., [https://ohss.dhs.gov/sites/default/files/2024-03/2023\_0818\_plcy\_naturalizations\_fy2022.pdf](https://ohss.dhs.gov/sites/default/files/2024-03/2023_0818_plcy_naturalizations_fy2022.pdf)  
11. Yearbook of Immigration Statistics | OHSS, [https://ohss.dhs.gov/topics/immigration/yearbook](https://ohss.dhs.gov/topics/immigration/yearbook)  
12. Naturalizations Annual Flow Report | OHSS \- Office of Homeland Security Statistics, [https://ohss.dhs.gov/topics/immigration/naturalizations/annual-flow-report](https://ohss.dhs.gov/topics/immigration/naturalizations/annual-flow-report)  
13. Historical Naturalizations Annual Flow Report \- Office of Homeland Security Statistics, [https://ohss.dhs.gov/topics/immigration/naturalizations/naturalizations-annual-flow-report/historical-naturalizations](https://ohss.dhs.gov/topics/immigration/naturalizations/naturalizations-annual-flow-report/historical-naturalizations)  
14. U.S. Naturalizations: 2012 \- Office of Homeland Security Statistics, [https://ohss.dhs.gov/sites/default/files/2023-12/Naturalizations\_2012.pdf](https://ohss.dhs.gov/sites/default/files/2023-12/Naturalizations_2012.pdf)  
15. U S Naturalizations: 2014\. Annual Flow Report. April 2016., [https://ohss.dhs.gov/sites/default/files/2023-12/Naturalizations\_2014.pdf](https://ohss.dhs.gov/sites/default/files/2023-12/Naturalizations_2014.pdf)  
16. U.S. Naturalizations: 2011 \- Office of Homeland Security Statistics, [https://ohss.dhs.gov/sites/default/files/2023-12/Naturalizations\_2011.pdf](https://ohss.dhs.gov/sites/default/files/2023-12/Naturalizations_2011.pdf)  
17. Naturalizations in the United States: 2005 \- Office of Homeland ..., [https://ohss.dhs.gov/sites/default/files/2023-12/Naturalizations\_2005.pdf](https://ohss.dhs.gov/sites/default/files/2023-12/Naturalizations_2005.pdf)  
18. DHS Annual Flow Report 8/18 of U.S. Naturalizations: 2017, [https://ohss.dhs.gov/sites/default/files/2023-12/Naturalizations\_2017.pdf](https://ohss.dhs.gov/sites/default/files/2023-12/Naturalizations_2017.pdf)  
19. DHS U.S. Naturalizations: 2018 \- Annual Flow Report August 2019, [https://ohss.dhs.gov/sites/default/files/2023-12/21\_0824\_plcy\_naturalizations\_fy2018.pdf](https://ohss.dhs.gov/sites/default/files/2023-12/21_0824_plcy_naturalizations_fy2018.pdf)  
20. Naturalization Trends in the United States \- Migration Policy Institute, [https://www.migrationpolicy.org/article/naturalization-trends-united-states-2012](https://www.migrationpolicy.org/article/naturalization-trends-united-states-2012)  
21. Article: Naturalized Citizens in the United States | migrationpolicy.org, [https://www.migrationpolicy.org/article/naturalization-trends-united-states](https://www.migrationpolicy.org/article/naturalization-trends-united-states)  
22. DHS Annual Flow Report on Naturalization Statistics for FY-2015 \- MyAttorney USA, [https://myattorneyusa.com/immigration-news/dhs-annual-flow-report-on-naturalization-statistics-for-fy-2015/](https://myattorneyusa.com/immigration-news/dhs-annual-flow-report-on-naturalization-statistics-for-fy-2015/)  
23. Naturalized Population: Trends and Characteristics \- Bipartisan Policy Center, [https://bipartisanpolicy.org/wp-content/uploads/2019/03/BPC-Immigration-Task-Force-Naturalized-Population-Characteristics-and-Trends-Issue-Brief-May-2014\_0.pdf](https://bipartisanpolicy.org/wp-content/uploads/2019/03/BPC-Immigration-Task-Force-Naturalized-Population-Characteristics-and-Trends-Issue-Brief-May-2014_0.pdf)  
24. Table 21\. Persons Naturalized by Region and Country of Birth: Fiscal Years 2017 to 2019, [https://ohss.dhs.gov/topics/immigration/yearbook/2019/table21](https://ohss.dhs.gov/topics/immigration/yearbook/2019/table21)  
25. What the data says about immigrants in the U.S. \- Pew Research Center, [https://www.pewresearch.org/short-reads/2025/08/21/key-findings-about-us-immigrants/](https://www.pewresearch.org/short-reads/2025/08/21/key-findings-about-us-immigrants/)  
26. Trends in Naturalization Rates: FY 2014 Update | USCIS, [https://www.uscis.gov/sites/default/files/document/data/Trends-in-Naturalization-Rates-FY14-Update.pdf](https://www.uscis.gov/sites/default/files/document/data/Trends-in-Naturalization-Rates-FY14-Update.pdf)  
27. Spotlight on Legal Immigration to the United States \- Migration Policy Institute, [https://www.migrationpolicy.org/article/spotlight-legal-immigration-united-states-2006](https://www.migrationpolicy.org/article/spotlight-legal-immigration-united-states-2006)  
28. FY 2021 USCIS Annual Statistical Report, [https://www.uscis.gov/sites/default/files/document/reports/2021%20USCIS%20Statistical%20Annual%20Report.pdf](https://www.uscis.gov/sites/default/files/document/reports/2021%20USCIS%20Statistical%20Annual%20Report.pdf)  
29. U.S. Naturalizations: 2021\. Annual Flow Report. \- Office of ..., [https://ohss.dhs.gov/sites/default/files/2023-12/2022\_0624\_plcy\_naturalizations\_fy2021.pdf](https://ohss.dhs.gov/sites/default/files/2023-12/2022_0624_plcy_naturalizations_fy2021.pdf)  
30. www.congress.gov, [https://www.congress.gov/crs\_external\_products/IF/HTML/IF12322.web.html](https://www.congress.gov/crs_external_products/IF/HTML/IF12322.web.html)  
31. Article: Naturalized Citizens in the United States | migrationpolicy.org, [https://www.migrationpolicy.org/article/naturalization-trends-united-states-2021](https://www.migrationpolicy.org/article/naturalization-trends-united-states-2021)

[The End of Response]

### Single-Row (One extracted item)

[The Start of Single-Row]

| Year | Total Naturalized | Born in Africa | Born in Asia | Born in Europe | Born in Caribbean | Born in Central America | Born in other North America | Born in Oceania | Born in South America |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 2019 | 843,593 | 84,990 | 327,273 | 81,040 | 101,312 | 42,077 | 133,521 | 4,308 | 68,678 |

[The End of Single-Row]

------------------------------------------------------------
## Core Principle

Your task is NOT to evaluate whether the Single-Row answers the entire Query. Your task IS ONLY to evaluate whether THIS Single-Row:

1. Correctly reflects the part of the Response it was extracted from;
2. Is factually correct according to verification tools.

You MUST ignore completeness. You MUST evaluate only the correctness of THIS Single-Row's own claims.

------------------------------------------------------------
## Role and High-Level Objective

Act as a neutral, impartial judge. All factual checks must be performed using Playwright MCP tools.

------------------------------------------------------------
## Step-by-Step Evaluation Procedure

### Step 1 — Initial Read
- Read the Query, Response, and Single-Row fully.

### Step 2 — Trace Source in the Response
- Locate the corresponding content in the Response.
- Confirm the Single-Row faithfully reflects the Response.

### Step 3 — Verify Each Claim Individually with Playwright MCP Tools
- Focus strictly on content relevant to the Query.
- Do not let style, language, or level of detail influence judgment.
- Treat "N/A", "NA", or "Data Unavailable" as problematic unless explicitly allowed.
- Follow explicit references in the Response: URLs, citations, or footnotes (e.g., `[^1]`, `<sup>1</sup>`).
- Open referenced pages with Playwright MCP tools and locate supporting evidence.
- Primarily rely on references in the Response; if none exist, search authoritative sources using the tools.
- If a reference is unreachable, paywalled, or does not support the claim, mark accordingly.
- Verify every field if the item contains multiple attributes (e.g., in a table row).
- Numeric values must strictly match authoritative sources—no tolerance allowed.

### Step 4 — Record Verification Results
For every claim in the Single-Row record:
- Supported / Contradicted / Not verifiable

------------------------------------------------------------
## Final Judgment Rules

A Single-Row is labeled **[1]** ONLY IF:
1. It contains at least one claim relevant to the Query; AND
2. Every claim is factually correct; AND
3. It faithfully represents the Response.

Otherwise, assign **[0]**.

### If ANY claim is:
- incorrect, OR
- missing, OR
- unverifiable
→ assign **[0]**

------------------------------------------------------------
## Strict Requirements

- You MUST use Playwright MCP tools for all factual verification.
- You MUST NOT add or infer information beyond what is provided.

------------------------------------------------------------
## Output Format (Strict)

Your final output must be exactly one line:

Response: [1]
or
Response: [0]

Nothing else.
