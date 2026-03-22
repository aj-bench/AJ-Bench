# Agent-as-a-Judge Task

You will verify the factual correctness of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Please compile a table listing the “CNN Hero of the Year” for every year the award was actually presented, from its first introduction through 2024 (including 2024), along with relevant details for each honoree. Please provide the official link of each year's "CNN Hero of the Year" to support your statement.

Organize the results in one Markdown table with the following columns:
Year of Award, Full Name, Gender, Date of Birth, Country of Birth,  University, Devoted Country, Background/Occupation, Major Contributions

Notes:
- Skip the year when no single CNN Hero of the Year is honored.
- If the honoree did not attend college, write “NA” in the University column.
- In the “Background/Occupation” column, specify the primary profession or social role, such as a nurse, teacher, or social entrepreneur.
- In the “Major Contribution” column, briefly describe their main contributions to public welfare or society, for example providing education for children, aiding the homeless, or promoting environmental protection.
- If you know the country where the individual engaged, you may note this in the “Devoted Country” column, for instance “China,” “United States,” or “India.”

[The End of Query]

### Response

[The Start of Response]

| Year of Award | Full Name            | Gender | Date of Birth     | Country of Birth | University                          | Devoted Country | Background/Occupation | Major Contributions                                                                 | Official CNN Link |
|---------------|----------------------|--------|-------------------|------------------|-------------------------------------|-----------------|-----------------------|-------------------------------------------------------------------------------------|-------------------|
| 2008         | Liz McCartney       | Female | Unknown          | United States   | Boston College; George Washington University (Master's) | United States  | Social entrepreneur   | Rebuilding homes for disaster victims, aiding recovery after Hurricane Katrina     | https://edition.cnn.com/2008/LIVING/11/22/heroes.show/  |
| 2009         | Efren Peñaflorida   | Male   | March 5, 1981    | Philippines     | Cavite State University             | Philippines    | Teacher               | Providing mobile education via pushcart classrooms to prevent youth gang involvement | https://edition.cnn.com/2009/LIVING/11/16/cnnheroes.peaflorida/  |
| 2010         | Anuradha Koirala    | Female | April 14, 1949   | Nepal           | NA                                  | Nepal           | Social activist       | Rescuing and rehabilitating victims of sex trafficking                              | https://www.cnn.com/2010/LIVING/11/21/cnnheroes.hero.of.year/index.html  |
| 2011         | Robin Lim           | Female | November 24, 1956| United States   | NA                                  | Indonesia       | Midwife               | Offering free maternity care and birthing services to low-income women              | https://edition.cnn.com/2011/12/11/living/cnn-heroes  |
| 2012         | Pushpa Basnet       | Female | 1984             | Nepal           | NA                                  | Nepal           | Social worker         | Supporting children of incarcerated parents with education and housing              | https://www.cnn.com/2012/12/02/world/cnnheroes-show  |
| 2013         | Chad Pregracke      | Male   | December 4, 1974 | United States   | Black Hawk College                  | United States  | Environmentalist      | Cleaning U.S. rivers and waterways, removing millions of pounds of trash            | https://www.cnn.com/2013/12/01/world/cnnheroes-pregracke/index.html  |
| 2014         | Pen Farthing        | Male   | May 1969         | United Kingdom  | NA                                  | Afghanistan     | Former military commando | Rescuing stray animals in war zones and reuniting them with soldiers                | https://www.cnn.com/2014/08/14/world/asia/cnnheroes-farthing  |
| 2015         | Maggie Doyne        | Female | November 7, 1986 | United States   | NA                                  | Nepal           | Humanitarian          | Building orphanages, schools, and women's centers for vulnerable children           | https://www.cnn.com/2015/11/29/us/cnn-heroes-doyne/index.html  |
| 2016         | Jeison Aristizábal  | Male   | Unknown          | Colombia        | Universidad Libre                   | Colombia        | Social worker         | Offering education, therapy, and support for disabled youth                         | https://www.cnn.com/2016/06/23/health/cnn-heroes-jeison-aristizabal  |
| 2017         | Amy Wright          | Female | September 21, 1975 | United States | University of Cincinnati College-Conservatory of Music | United States | Social entrepreneur   | Creating employment opportunities for people with disabilities through coffee shops | https://www.cnn.com/2017/06/22/health/cnnheroes-amy-wright-bitty-and-beaus-coffee  |
| 2018         | Ricardo Pun-Chong  | Male   | Unknown          | Peru            | NA                                  | Peru            | Physician             | Providing free shelter and support for families of sick children seeking treatment | https://www.cnn.com/2018/05/31/health/cnnheroes-ricardo-pun-chong-inspira  |
| 2019         | Freweini Mebrahtu   | Female | 1965             | Ethiopia        | Prairie View A&M University         | Ethiopia        | Chemical engineer     | Developing reusable menstrual pads to enable girls to stay in school                | https://www.cnn.com/2019/12/08/world/freweini-mebrahtu-2019-cnn-hero-of-the-year  |
| 2021         | Shirley Raines      | Female | December 29 (approx. 1967) | United States | NA                                  | United States  | Beautician            | Delivering beauty services, food, and essentials to homeless communities           | https://www.cnn.com/2021/12/12/us/shirley-raines-2021-cnn-hero-of-the-year/index.html  |
| 2022         | Nelly Cheboi        | Female | November 26, 1992| Kenya           | Augustana College                   | Kenya           | Software engineer     | Establishing computer labs and tech education in rural schools                      | https://www.cnn.com/2022/12/11/us/nelly-cheboi-2022-cnn-hero-of-the-year/index.html  |
| 2023         | Dr. Kwane Stewart   | Male   | October 4, 1974 | United States   | Colorado State University           | United States  | Veterinarian          | Offering free veterinary care for pets of homeless individuals                     | https://www.cnn.com/2023/12/10/us/kwane-stewart-2023-cnn-hero-of-the-year/index.html  |
| 2024         | Stephen Knight      | Male   | Unknown (approx. 1960) | United States | NA                                  | United States  | Non-profit founder    | Fostering dogs for owners in addiction recovery to support family reunification     | https://www.cnn.com/2024/12/08/world/cnn-hero-of-the-year-stephen-knight-dogs-matter-foster-addiction-cnnheroes  |

### Key Citations
- https://en.wikipedia.org/wiki/CNN_Heroes
- https://edition.cnn.com/world/heroes
- https://www.cnn.com/2010/LIVING/11/21/cnnheroes.hero.of.year/index.html
- https://edition.cnn.com/2011/12/11/living/cnn-heroes
- https://www.cnn.com/2012/12/02/world/cnnheroes-show
- https://www.cnn.com/2013/12/01/world/cnnheroes-pregracke/index.html
- https://www.cnn.com/2014/08/14/world/asia/cnnheroes-farthing
- https://www.cnn.com/2015/11/29/us/cnn-heroes-doyne/index.html
- https://www.cnn.com/2016/06/23/health/cnn-heroes-jeison-aristizabal
- https://www.cnn.com/2017/06/22/health/cnnheroes-amy-wright-bitty-and-beaus-coffee
- https://www.cnn.com/2018/05/31/health/cnnheroes-ricardo-pun-chong-inspira
- https://www.cnn.com/2019/12/08/world/freweini-mebrahtu-2019-cnn-hero-of-the-year
- https://www.cnn.com/2021/12/12/us/shirley-raines-2021-cnn-hero-of-the-year/index.html
- https://www.cnn.com/2022/12/11/us/nelly-cheboi-2022-cnn-hero-of-the-year/index.html
- https://www.cnn.com/2023/12/10/us/kwane-stewart-2023-cnn-hero-of-the-year/index.html
- https://www.cnn.com/2024/12/08/world/cnn-hero-of-the-year-stephen-knight-dogs-matter-foster-addiction-cnnheroes

[The End of Response]

### Single-Row (One extracted item)

[The Start of Single-Row]

| Year of Award | Full Name            | Gender | Date of Birth     | Country of Birth | University                          | Devoted Country | Background/Occupation | Major Contributions                                                                 | Official CNN Link |
|---------------|----------------------|--------|-------------------|------------------|-------------------------------------|-----------------|-----------------------|-------------------------------------------------------------------------------------|-------------------|
| 2010         | Anuradha Koirala    | Female | April 14, 1949   | Nepal           | NA                                  | Nepal           | Social activist       | Rescuing and rehabilitating victims of sex trafficking                              | https://www.cnn.com/2010/LIVING/11/21/cnnheroes.hero.of.year/index.html  |

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
