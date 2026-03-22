# Agent-as-a-Judge Task

You will verify the factual correctness of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

Could you provide an updated list of all officially recognized Areas of Outstanding Natural Beauty (AONBs) and National Scenic Area (NSA) in the UK as of 2024? Please supply supporting links, and include the following details: name of each scenic area, designation category (AONB or NSA), regions (select from England, Scotland, Wales, and Northern Ireland), designation time (the year it was designated as an AONB/NSA for the first time), responsible public body (select from Natural England, Natural Resources Wales, Northern Ireland Environment Agency, or NatureScot), counties (list all administrative counties it covers, separated by commas), and the official website.

Please organize the results in one Markdown table with the following columns:
Designation Category, Area Name, Regions, Designation Time, Responsible Public Body, Counties, Website

[The End of Query]

### Response

[The Start of Response]

| Designation Category | Area Name | Regions | Designation Time | Responsible Public Body | Counties | Website |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| AONB | Anglesey | Wales | 1967 | Natural Resources Wales | Anglesey | https://www.anglesey.gov.uk/en/Residents/Countryside-and-Coast/Anglesey-AONB/Anglesey-AONB.aspx |
| AONB | Antrim Coast and Glens | Northern Ireland | 1988 | Northern Ireland Environment Agency | Causeway Coast and Glens, Mid and East Antrim | https://ccght.org/ |
| AONB | Arnside and Silverdale | England | 1972 | Natural England | Lancashire, Westmorland and Furness | https://www.arnsidesilverdaleaonb.org.uk/ |
| AONB | Binevenagh | Northern Ireland | 1966 | Northern Ireland Environment Agency | Causeway Coast and Glens | https://www.daera-ni.gov.uk/topics/areas-outstanding-natural-beauty |
| AONB | Blackdown Hills | England | 1991 | Natural England | Devon, Somerset | https://www.blackdownhillsaonb.org.uk/ |
| AONB | Cannock Chase | England | 1958 | Natural England | Staffordshire | https://www.cannockchaseaonb.co.uk/ |
| AONB | Causeway Coast | Northern Ireland | 1989 | Northern Ireland Environment Agency | Causeway Coast and Glens | https://ccght.org/ |
| AONB | Chichester Harbour | England | 1964 | Natural England | Hampshire, West Sussex | https://www.conservancy.co.uk/ |
| AONB | Chilterns | England | 1965 | Natural England | Buckinghamshire, Central Bedfordshire, Hertfordshire, Luton, Oxfordshire | https://www.chilternsaonb.org/ |
| AONB | Clwydian Range and Dee Valley | Wales | 1985 | Natural Resources Wales | Denbighshire, Flintshire, Wrexham | https://www.clwydianrangeanddeevalley.org.uk/ |
| AONB | Cornwall | England | 1959 | Natural England | Cornwall | https://www.cornwall-aonb.gov.uk/ |
| AONB | Cotswolds | England | 1966 | Natural England | Bath and North East Somerset, Gloucestershire, Oxfordshire, South Gloucestershire, Warwickshire, Wiltshire, Worcestershire | https://www.cotswoldsaonb.org.uk/ |
| AONB | Cranborne Chase and West Wiltshire Downs | England | 1981 | Natural England | Dorset, Hampshire, Somerset, Wiltshire | https://www.cranbornechase.org.uk/ |
| AONB | Dedham Vale | England | 1970 | Natural England | Essex, Suffolk | https://www.dedhamvalestourvalley.org/ |
| AONB | Dorset | England | 1959 | Natural England | Dorset | https://www.dorsetaonb.org.uk/ |
| AONB | East Devon | England | 1963 | Natural England | Devon | https://www.eastdevonaonb.org.uk/ |
| AONB | Forest of Bowland | England | 1964 | Natural England | Lancashire, North Yorkshire | https://www.forestofbowland.com/ |
| AONB | Gower | Wales | 1956 | Natural Resources Wales | Swansea | https://www.gower-aonb.co.uk/ |
| AONB | High Weald | England | 1983 | Natural England | East Sussex, Kent, Surrey, West Sussex | https://www.highweald.org/ |
| AONB | Howardian Hills | England | 1987 | Natural England | North Yorkshire | https://www.howardianhills.org.uk/ |
| AONB | Isle of Wight | England | 1963 | Natural England | Isle of Wight | https://www.isleofwight-nl.org.uk/ |
| AONB | Isles of Scilly | England | 1975 | Natural England | Isles of Scilly | https://www.ios-aonb.info/ |
| AONB | Kent Downs | England | 1968 | Natural England | Greater London, Kent, Medway | https://www.kentdowns.org.uk/ |
| AONB | Lagan Valley | Northern Ireland | 1965 | Northern Ireland Environment Agency | Belfast, Lisburn and Castlereagh | https://www.laganvalleyregionalpark.org/ |
| AONB | Lincolnshire Wolds | England | 1973 | Natural England | Lincolnshire, North East Lincolnshire | https://www.lincswolds.org.uk/ |
| AONB | Llŷn | Wales | 1957 | Natural Resources Wales | Gwynedd | https://www.ahne-llyn-aonb.org/ |
| AONB | Malvern Hills | England | 1959 | Natural England | Gloucestershire, Herefordshire, Worcestershire | https://www.malvernhillsaonb.org.uk/ |
| AONB | Mendip Hills | England | 1972 | Natural England | Bath and North East Somerset, North Somerset, Somerset | https://www.mendiphillsaonb.org.uk/ |
| AONB | Mourne | Northern Ireland | 1986 | Northern Ireland Environment Agency | Armagh City, Banbridge and Craigavon, Newry, Mourne and Down | https://www.mourneaonb.org/ |
| AONB | Nidderdale | England | 1994 | Natural England | North Yorkshire | https://www.nidderdaleaonb.org.uk/ |
| AONB | Norfolk Coast | England | 1968 | Natural England | Norfolk | https://www.norfolkcoastaonb.org.uk/ |
| AONB | North Devon Coast | England | 1959 | Natural England | Devon | https://www.northdevonbiosphere.org.uk/ |
| AONB | North Pennines | England | 1988 | Natural England | County Durham, Cumberland, Northumberland, North Yorkshire, Westmorland and Furness | https://www.northpennines.org.uk/ |
| AONB | Northumberland Coast | England | 1958 | Natural England | Northumberland | https://www.northumberlandcoast.org.uk/ |
| AONB | North Wessex Downs | England | 1972 | Natural England | Hampshire, Oxfordshire, Swindon, West Berkshire, Wiltshire | https://www.northwessexdowns.org.uk/ |
| AONB | Quantock Hills | England | 1956 | Natural England | Somerset | https://www.quantockhills.com/ |
| AONB | Ring of Gullion | Northern Ireland | 1991 | Northern Ireland Environment Agency | Armagh City, Banbridge and Craigavon, Newry, Mourne and Down | https://ringofgullionaonb.co.uk/ |
| AONB | Shropshire Hills | England | 1958 | Natural England | Shropshire, Telford and Wrekin | https://www.shropshirehillsaonb.co.uk/ |
| AONB | Solway Coast | England | 1964 | Natural England | Cumberland | https://www.solwaycoastaonb.org.uk/ |
| AONB | South Devon | England | 1960 | Natural England | Devon, Plymouth, Torbay | https://www.southdevon-nl.org.uk/ |
| AONB | Sperrins | Northern Ireland | 1968 | Northern Ireland Environment Agency | Causeway Coast and Glens, Derry and Strabane, Fermanagh and Omagh, Mid Ulster | https://www.sperrinsaonb.com/ |
| AONB | Strangford and Lecale | Northern Ireland | 1967 | Northern Ireland Environment Agency | Ards and North Down, Newry, Mourne and Down | https://www.strangfordlough.org/ |
| AONB | Suffolk Coast and Heaths | England | 1970 | Natural England | Suffolk, Essex | https://www.suffolkcoastandheaths.org/ |
| AONB | Surrey Hills | England | 1958 | Natural England | Surrey | https://www.surreyhills.org/ |
| AONB | Tamar Valley | England | 1995 | Natural England | Cornwall, Devon | https://www.tamarvalley.org.uk/ |
| AONB | Wye Valley | England, Wales | 1971 | Natural England, Natural Resources Wales | Gloucestershire, Herefordshire, Monmouthshire | https://www.wyevalleyaonb.org.uk/ |
| NSA | Assynt-Coigach | Scotland | 1980 | NatureScot | Highland | https://www.nature.scot/ |
| NSA | Ben Nevis and Glen Coe | Scotland | 1980 | NatureScot | Highland, Argyll and Bute | https://www.nature.scot/ |
| NSA | Cairngorm Mountains | Scotland | 1980 | NatureScot | Highland, Aberdeenshire | https://www.nature.scot/ |
| NSA | Deeside and Lochnagar | Scotland | 1980 | NatureScot | Aberdeenshire, Angus | https://www.nature.scot/ |
| NSA | Dornoch Firth | Scotland | 1980 | NatureScot | Highland | https://www.nature.scot/ |
| NSA | East Stewartry Coast | Scotland | 1980 | NatureScot | Dumfries and Galloway | https://www.nature.scot/ |
| NSA | Eildon and Leaderfoot | Scotland | 1980 | NatureScot | Scottish Borders | https://www.nature.scot/ |
| NSA | Fleet Valley | Scotland | 1980 | NatureScot | Dumfries and Galloway | https://www.nature.scot/ |
| NSA | Glen Affric | Scotland | 1980 | NatureScot | Highland | https://www.nature.scot/ |
| NSA | Glen Strathfarrar | Scotland | 1980 | NatureScot | Highland | https://www.nature.scot/ |
| NSA | Hoy and West Mainland | Scotland | 1980 | NatureScot | Orkney Islands | https://www.nature.scot/ |
| NSA | Jura | Scotland | 1980 | NatureScot | Argyll and Bute | https://www.nature.scot/ |
| NSA | Kintail | Scotland | 1980 | NatureScot | Highland | https://www.nature.scot/ |
| NSA | Knapdale | Scotland | 1980 | NatureScot | Argyll and Bute | https://www.nature.scot/ |
| NSA | Knoydart | Scotland | 1980 | NatureScot | Highland | https://www.nature.scot/ |
| NSA | Kyle of Tongue | Scotland | 1980 | NatureScot | Highland | https://www.nature.scot/ |
| NSA | Kyles of Bute | Scotland | 1980 | NatureScot | Argyll and Bute | https://www.nature.scot/ |
| NSA | Loch Lomond | Scotland | 1980 | NatureScot | Argyll and Bute, Stirling | https://www.nature.scot/ |
| NSA | Loch na Keal, Isle of Mull | Scotland | 1980 | NatureScot | Argyll and Bute | https://www.nature.scot/ |
| NSA | Loch Rannoch and Glen Lyon | Scotland | 1980 | NatureScot | Perth and Kinross, Stirling | https://www.nature.scot/ |
| NSA | Loch Shiel | Scotland | 1980 | NatureScot | Highland | https://www.nature.scot/ |
| NSA | Loch Tummel | Scotland | 1980 | NatureScot | Perth and Kinross | https://www.nature.scot/ |
| NSA | Lynn of Lorn | Scotland | 1980 | NatureScot | Argyll and Bute | https://www.nature.scot/ |
| NSA | Morar, Moidart and Ardnamurchan | Scotland | 1980 | NatureScot | Highland | https://www.nature.scot/ |
| NSA | Nith Estuary | Scotland | 1980 | NatureScot | Dumfries and Galloway | https://www.nature.scot/ |
| NSA | North Arran | Scotland | 1980 | NatureScot | North Ayrshire | https://www.nature.scot/ |
| NSA | North-West Sutherland | Scotland | 1980 | NatureScot | Highland | https://www.nature.scot/ |
| NSA | River Earn (Comrie to St. Fillans) | Scotland | 1980 | NatureScot | Perth and Kinross | https://www.nature.scot/ |
| NSA | River Tay (Dunkeld) | Scotland | 1980 | NatureScot | Perth and Kinross | https://www.nature.scot/ |
| NSA | Scarba, Lunga and the Garvellachs | Scotland | 1980 | NatureScot | Argyll and Bute | https://www.nature.scot/ |
| NSA | Shetland | Scotland | 1980 | NatureScot | Shetland Islands | https://www.nature.scot/ |
| NSA | Small Isles | Scotland | 1980 | NatureScot | Highland | https://www.nature.scot/ |
| NSA | South Lewis, Harris and North Uist | Scotland | 1980 | NatureScot | Western Isles | https://www.nature.scot/ |
| NSA | South Uist Machair | Scotland | 1980 | NatureScot | Western Isles | https://www.nature.scot/ |
| NSA | St. Kilda | Scotland | 1980 | NatureScot | Western Isles | https://www.nature.scot/ |
| NSA | The Cuillin Hills | Scotland | 1980 | NatureScot | Highland | https://www.nature.scot/ |
| NSA | The Trossachs | Scotland | 1980 | NatureScot | Stirling | https://www.nature.scot/ |
| NSA | Trotternish | Scotland | 1980 | NatureScot | Highland | https://www.nature.scot/ |
| NSA | Upper Tweeddale | Scotland | 1980 | NatureScot | Scottish Borders | https://www.nature.scot/ |
| NSA | Wester Ross | Scotland | 1980 | NatureScot | Highland | https://www.nature.scot/ |

## Key Designation Milestones

**Gower** was the first AONB designated in the UK in 1956, while **Quantock Hills** became the first AONB in England the same year. Scotland's 40 National Scenic Areas were originally identified in 1978 by the Countryside Commission for Scotland and formally designated in 1980. The most recent AONB designation was **Tamar Valley** in 1995.[^1][^16][^4][^6][^15]

## Contact Information for Responsible Bodies

**Natural England**: Tel: 0300 060 3900, Website: https://www.gov.uk/government/organisations/natural-england [^17][^14]

**Natural Resources Wales**: Tel: 0300 065 3000, Email: enquiries@naturalresourceswales.gov.uk [^18][^19]

**Northern Ireland Environment Agency (DAERA)**: Tel: 0300 200 7840, Email: daera.helpline@daera-ni.gov.uk [^20][^21][^22]

**NatureScot**: Website: https://www.nature.scot/ [^3][^6]
<span style="display:none">[^23][^24][^25][^26][^27][^28][^29][^30][^31][^32][^33][^34][^35][^36][^37][^38][^39][^40][^41][^42][^43][^44][^45][^46][^47][^48][^49][^50][^51][^52][^53][^54]</span>

<div style="text-align: center">⁂</div>

[^1]: https://en.wikipedia.org/wiki/Area_of_Outstanding_Natural_Beauty

[^2]: https://en.wikipedia.org/wiki/National_scenic_area_(Scotland)

[^3]: https://www.nature.scot/professional-advice/protected-areas-and-species/protected-areas/national-designations/national-scenic-areas

[^4]: https://en.wikipedia.org/wiki/Areas_of_Outstanding_Natural_Beauty_in_Wales

[^5]: https://www.daera-ni.gov.uk/topics/areas-outstanding-natural-beauty

[^6]: https://en.wikipedia.org/wiki/NatureScot

[^7]: https://www.gov.uk/guidance/areas-of-outstanding-natural-beauty-aonbs-designation-and-management

[^8]: https://www.planning.data.gov.uk/dataset/area-of-outstanding-natural-beauty

[^9]: https://ccght.org/wp-content/uploads/2021/03/ACG-AONB-Management-Plan-2020-2030-DRAFT.pdf

[^10]: https://www.gov.scot/publications/national-scenic-areas-of-scotland-maps/

[^11]: https://national-landscapes.org.uk/national-landscapes

[^12]: https://bedandbreakfastnationwide.com/areas-of-outstanding-natural-beauty/

[^13]: https://en.wikipedia.org/wiki/Natural_Resources_Wales

[^14]: https://en.wikipedia.org/wiki/Natural_England

[^15]: https://www.gov.scot/policies/landscape-and-outdoor-access/natural-heritage-designations/

[^16]: https://www.nature.scot/professional-advice/protected-areas-and-species/protected-areas/national-designations/national-scenic-areas/national-scenic-areas-background-guidance

[^17]: https://www.gov.uk/government/organisations/natural-england

[^18]: https://www.ukata.org.uk/support/natural-resources-wales/

[^19]: https://naturalresources.wales/about-us/contact-us/general-enquiries/?lang=en

[^20]: https://www.regulated-professions.service.gov.uk/regulatory-authorities/department-of-agriculture-environment-and-rural-affairs

[^21]: https://www.daera-ni.gov.uk/contact

[^22]: https://www.daera-ni.gov.uk/contacts/daera-helpline-numbers

[^23]: https://publications.naturalengland.org.uk/file/2635576

[^24]: https://www.tripadvisor.co.uk/ShowTopic-g186535-i625-k6957823-Scotland_s_Finest_Landscapes_The_Official_Top_40_List-Scottish_Highlands_Scotland.html

[^25]: https://wiki.openstreetmap.org/wiki/Areas_of_Outstanding_Natural_Beauty_(UK)

[^26]: https://nl.wikipedia.org/wiki/National_Scenic_Area

[^27]: https://ymgynghori.cyfoethnaturiol.cymru/north-east-gogledd-ddwyrain/waless-national-park-proposal-public-consultation/user_uploads/area-of-search-report---final.pdf

[^28]: https://www.whatdotheyknow.com/body/list/aonbcb

[^29]: https://www.gov.scot/publications/report-proposal-national-park-southwest-scotland/pages/10/

[^30]: https://www.ruralpayments.org/topics/all-schemes/agri-environment-climate-scheme/agri-environment-climate-scheme-full-guidance-menu/agri-environment-designations/

[^31]: https://www.scotlink.org/wp-content/uploads/2024/03/30-by-30-March-Digital.pdf

[^32]: https://directory.shropshire.gov.uk/service/241826f5-d540-496e-b8f2-7652571e1e42/natural-england/

[^33]: https://coastandheaths-nl.org.uk/managing/about/boundary-review/

[^34]: https://datamap.gov.wales/layers/inspire-nrw:NRW_AONB

[^35]: https://ccght.org/wp-content/uploads/2012/07/Antrim-CG-AONB-Introductory-Leaflet.pdf

[^36]: https://www.yorkshire-wolds-designation-project.org/support/faqs

[^37]: https://national-landscapes.org.uk

[^38]: https://kids.kiddle.co/National_scenic_area_(Scotland)

[^39]: https://en.wikipedia.org/wiki/Category:National_scenic_areas_of_Scotland

[^40]: https://www.nature.scot/sites/default/files/2017-07/Publication%202010%20-%20SNH%20Commissioned%20Report%20374%20-%20The%20Special%20Qualities%20of%20the%20National%20Scenic%20Areas.pdf

[^41]: https://www.nature.scot/doc/naturescot-commissioned-report-374-special-qualities-national-scenic-areas

[^42]: https://www.highland.gov.uk/download/downloads/id/2450/wester_ross_national_scenic_area_revised_draft_management_strategy_november_2002.pdf

[^43]: https://www.nature.scot/professional-advice/protected-areas-and-species/protected-areas/national-designations

[^44]: https://www.herefordshire.gov.uk/conservation-1/national-landscapes-areas-outstanding-natural-beauty-aonb

[^45]: https://www.ahne-llyn-aonb.org/Contact

[^46]: https://www.nidirect.gov.uk/contacts/angling-northern-ireland-daera-inland-fisheries-group

[^47]: https://isleofwight-nl.org.uk

[^48]: https://www.first-nature.com/waleswildlife/~conservation.php

[^49]: https://historicengland.org.uk/advice/caring-for-heritage/rural-heritage/protected-rural-landscapes/

[^50]: https://www.northernireland.gov.uk/news/closing-date-extended-competition-recruit-non-executive-board-members-daera

[^51]: https://www2.dardni.gov.uk/GatewayWeb/Internet/Level0/Help.aspx

[^52]: https://www.gov.uk/government/organisations/natural-resources-wales/about

[^53]: https://www.southdevon-nl.org.uk

[^54]: https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/d40a22052258817272eecb2d1d66a747/348ce2f8-ccc3-40f9-8b3c-ad6f45dce410/32ae8a6e.csv



[The End of Response]

### Single-Row (One extracted item)

[The Start of Single-Row]

| Designation Category | Area Name | Regions | Designation Time | Responsible Public Body | Counties | Website |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| AONB | Surrey Hills | England | 1958 | Natural England | Surrey | https://www.surreyhills.org/ |

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
