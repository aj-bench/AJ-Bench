# Agent-as-a-Judge Task

You will verify the factual correctness of ONE Single-Row extracted from a Response.
You MUST follow all instructions precisely and avoid any interpretation that goes beyond what is explicitly required.

------------------------------------------------------------
## Provided Inputs

### Query

[The Start of Query]

What are the world's busiest airports by passenger traffic? List the top ten busiest airports between 2020-2024 (including 2020 and 2024). Please provide official links to support your statement. I want to know about their rank, specific location (including city, district, road), total passengers (with precision to the person) and code(IATA/ICAO).

Please organize the results in one Markdown table with the following column names in order: 
Year, Airport, Rank, Location, Total Passengers, Code(IATA/ICAO)

[The End of Query]

### Response

[The Start of Response]

# **Global Airport Passenger Traffic Rankings (2020-2024)**

| Year | Airport | Rank | Location | Total Passengers | Code(IATA/ICAO) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 2020 | Guangzhou Baiyun International Airport | 1 | Guangzhou, Guangdong, China | 43,767,558 | CAN/ZGGG |
| 2020 | Hartsfield-Jackson Atlanta International Airport | 2 | Atlanta, Georgia, USA | 42,918,685 | ATL/KATL |
| 2020 | Chengdu Shuangliu International Airport | 3 | Chengdu, Sichuan, China | 40,741,509 | CTU/ZUUU |
| 2020 | Dallas/Fort Worth International Airport | 4 | Dallas-Fort Worth, Texas, USA | 39,364,990 | DFW/KDFW |
| 2020 | Shenzhen Bao'an International Airport | 5 | Shenzhen, Guangdong, China | 37,916,054 | SZX/ZGSZ |
| 2020 | Chongqing Jiangbei International Airport | 6 | Chongqing, China | 34,937,789 | CKG/ZUCK |
| 2020 | Beijing Capital International Airport | 7 | Beijing, China | 34,513,827 | PEK/ZBAA |
| 2020 | Denver International Airport | 8 | Denver, Colorado, USA | 33,741,129 | DEN/KDEN |
| 2020 | Kunming Changshui International Airport | 9 | Kunming, Yunnan, China | 32,990,805 | KMG/ZPPP |
| 2020 | Shanghai Hongqiao International Airport | 10 | Shanghai, China | 31,165,641 | SHA/ZSSS |
| 2021 | Hartsfield-Jackson Atlanta International Airport | 1 | Atlanta, Georgia, USA | 75,704,760 | ATL/KATL |
| 2021 | Dallas/Fort Worth International Airport | 2 | Dallas-Fort Worth, Texas, USA | 62,465,756 | DFW/KDFW |
| 2021 | Denver International Airport | 3 | Denver, Colorado, USA | 58,828,552 | DEN/KDEN |
| 2021 | Chicago O’Hare International Airport | 4 | Chicago, Illinois, USA | 54,020,399 | ORD/KORD |
| 2021 | Los Angeles International Airport | 5 | Los Angeles, California, USA | 48,007,284 | LAX/KLAX |
| 2021 | Charlotte Douglas International Airport | 6 | Charlotte, North Carolina, USA | 43,302,230 | CLT/KCLT |
| 2021 | Orlando International Airport | 7 | Orlando, Florida, USA | 40,351,068 | MCO/KMCO |
| 2021 | Guangzhou Baiyun International Airport | 8 | Guangzhou, Guangdong, China | 40,259,401 | CAN/ZGGG |
| 2021 | Chengdu Shuangliu International Airport | 9 | Chengdu, Sichuan, China | 40,117,496 | CTU/ZUUU |
| 2021 | Harry Reid International Airport | 10 | Las Vegas, Nevada, USA | 39,754,366 | LAS/KLAS |
| 2022 | Hartsfield-Jackson Atlanta International Airport | 1 | Atlanta, Georgia, USA | 93,699,630 | ATL/KATL |
| 2022 | Dallas/Fort Worth International Airport | 2 | Dallas-Fort Worth, Texas, USA | 73,362,946 | DFW/KDFW |
| 2022 | Denver International Airport | 3 | Denver, Colorado, USA | 69,286,461 | DEN/KDEN |
| 2022 | Chicago O’Hare International Airport | 4 | Chicago, Illinois, USA | 68,340,619 | ORD/KORD |
| 2022 | Dubai International Airport | 5 | Garhoud, Dubai, UAE | 66,069,981 | DXB/OMDB |
| 2022 | Los Angeles International Airport | 6 | Los Angeles, California, USA | 65,924,298 | LAX/KLAX |
| 2022 | Istanbul Airport | 7 | Arnavutköy, Istanbul, Turkey | 64,289,107 | IST/LTFM |
| 2022 | Heathrow Airport | 8 | Hillingdon, London, UK | 61,599,196 | LHR/EGLL |
| 2022 | Indira Gandhi International Airport | 9 | Palam, Delhi, India | 59,490,074 | DEL/VIDP |
| 2022 | Paris Charles de Gaulle Airport | 10 | Roissy-en-France, Île-de-France, France | 57,474,033 | CDG/LFPG |
| 2023 | Hartsfield-Jackson Atlanta International Airport | 1 | Atlanta, Georgia, USA | 104,653,451 | ATL/KATL |
| 2023 | Dubai International Airport | 2 | Garhoud, Dubai, UAE | 86,994,365 | DXB/OMDB |
| 2023 | Dallas/Fort Worth International Airport | 3 | Dallas-Fort Worth, Texas, USA | 81,755,538 | DFW/KDFW |
| 2023 | Heathrow Airport | 4 | Hillingdon, London, UK | 79,151,902 | LHR/EGLL |
| 2023 | Tokyo Haneda Airport | 5 | Ōta, Tokyo, Japan | 78,719,814 | HND/RJTT |
| 2023 | Denver International Airport | 6 | Denver, Colorado, USA | 77,837,917 | DEN/KDEN |
| 2023 | Istanbul Airport | 7 | Arnavutköy, Istanbul, Turkey | 76,027,321 | IST/LTFM |
| 2023 | Los Angeles International Airport | 8 | Los Angeles, California, USA | 75,050,872 | LAX/KLAX |
| 2023 | Chicago O’Hare International Airport | 9 | Chicago, Illinois, USA | 73,894,226 | ORD/KORD |
| 2023 | Indira Gandhi International Airport | 10 | Palam, Delhi, India | 72,214,841 | DEL/VIDP |
| 2024 | Hartsfield-Jackson Atlanta International Airport | 1 | Atlanta, Georgia, USA | 108,067,766 | ATL/KATL |
| 2024 | Dubai International Airport | 2 | Garhoud, Dubai, UAE | 92,300,000 | DXB/OMDB |
| 2024 | Dallas/Fort Worth International Airport | 3 | Dallas-Fort Worth, Texas, USA | 87,817,864 | DFW/KDFW |
| 2024 | Tokyo Haneda Airport | 4 | Ōta, Tokyo, Japan | 85,000,000 | HND/RJTT |
| 2024 | Heathrow Airport | 5 | Hillingdon, London, UK | 83,882,140 | LHR/EGLL |
| 2024 | Denver International Airport | 6 | Denver, Colorado, USA | 82,358,744 | DEN/KDEN |
| 2024 | O'Hare International Airport | 7 | Chicago, Illinois, USA | 80,043,050 | ORD/KORD |
| 2024 | Istanbul Airport | 8 | Arnavutköy, Istanbul, Turkey | 79,988,272 | IST/LTFM |
| 2024 | Indira Gandhi International Airport | 9 | Palam, Delhi, India | 77,820,834 | DEL/VIDP |
| 2024 | Shanghai Pudong International Airport | 10 | Pudong, Shanghai, China | 76,787,039 | PVG/ZSPD |

Sources: 1

## **Analysis of a Turbulent Era: A Year-by-Year Breakdown**

The period between 2020 and 2024 was marked by unprecedented volatility in the aviation sector. The rankings of the world's busiest airports fluctuated dramatically, reflecting the phased impacts of the pandemic, the uneven nature of regional recoveries, and the underlying strategic strengths of different air hubs.

### **2020: The Great Disruption and the Rise of Domestic Hubs**

The year 2020 witnessed the most severe contraction in aviation history. Global passenger traffic plummeted by 64.6% compared to 2019 levels, as nations sealed their borders and international travel ground to a halt.<sup>1</sup> This environment created a unique set of conditions that completely upended the traditional airport hierarchy. With international passenger traffic demand dropping by 75.6%, only airports within countries possessing massive, self-contained domestic markets could sustain significant operations.<sup>3</sup>

This led to a historic shift in the global rankings. For the first time since 1998, Hartsfield-Jackson Atlanta International Airport was unseated from the top position.<sup>2</sup> The new leader was Guangzhou Baiyun International Airport (CAN) in China, which handled 43.8 million passengers.<sup>1</sup> This was not an isolated event but part of a broader trend: seven of the world's top ten busiest airports in 2020 were located in China, with six of them being new to the list.<sup>1</sup> Meanwhile, perennial top-tier hubs heavily reliant on international traffic, such as Beijing Capital International Airport (PEK) and Tokyo Haneda Airport (HND), which were ranked first and second respectively in 2019, fell out of the top ten entirely.<sup>2</sup>

The 2020 rankings were a direct reflection of national pandemic responses and aviation strategies. China's ability to contain the initial outbreak internally and subsequently stimulate its vast domestic economy and travel market translated directly into aviation dominance. While the rest of the world contended with widespread lockdowns and cross-border restrictions, China's domestic passenger market began a rapid recovery.<sup>1</sup> Consequently, the 2020 list serves as a clear indicator of which major economic power first achieved a level of internal stability, making the airport rankings a proxy for national pandemic response effectiveness in that specific year.

### **2021: The American Rebound**

In 2021, the global aviation landscape shifted again, this time driven by the robust recovery of the U.S. domestic market. Hartsfield-Jackson Atlanta International Airport (ATL) reclaimed its number one ranking, handling 75.7 million passengers—a staggering 76.4% increase over its 2020 traffic.<sup>4</sup> The dominance of the U.S. market was undeniable, with American airports occupying eight of the top ten positions globally.<sup>4</sup> Dallas/Fort Worth (DFW) and Denver (DEN) secured the second and third spots, respectively.<sup>4</sup>

This reversal was fueled by a recovery in domestic travel that outpaced all other global regions. While international travel remained largely depressed, the sheer scale of the American market, combined with an earlier easing of internal travel restrictions compared to Europe and Asia, created a powerful engine for traffic growth.<sup>3</sup> The biggest mover within the top ten was Orlando International Airport (MCO), which leaped from 27th position in 2020 to seventh in 2021, underscoring the strength of the rebounding leisure travel sector.<sup>4</sup> In contrast, Guangzhou (CAN), the leader in 2020, slid to eighth place as its growth stagnated relative to the explosive recovery in the U.S..<sup>4</sup>

The 2021 rankings highlight a key structural advantage: a mature, liberalized, and highly competitive domestic aviation market is exceptionally resilient during a recovery phase. The dynamic competition among multiple large carriers in the U.S., including legacy airlines and low-cost carriers, for a resurgence of domestic travelers provided a momentum that more centrally controlled or internationally-dependent aviation markets could not replicate at that time.

### **2022: The Dawn of International Recovery**

The year 2022 marked a critical turning point as the widespread lifting of international travel restrictions began to normalize the global rankings. Overall global passenger traffic recovered to approximately 73% of 2019 levels, a significant improvement driven by the resurgence of cross-border travel.<sup>21</sup> This trend was most visible in the composition of the top ten list, which saw the return of major international hubs.

While U.S. airports continued to hold the top four spots, led by Atlanta with 93.7 million passengers, the most significant story was the re-entry of key global connectors.<sup>7</sup> Dubai International Airport (DXB) reappeared in the top ten at number five, Istanbul Airport (IST) at number seven, London's Heathrow Airport (LHR) at number eight, and Paris Charles de Gaulle Airport (CDG) at number ten.<sup>7</sup> The most dramatic comeback was that of Heathrow, which soared from 54th place in 2021 to eighth in 2022, a clear testament to the powerful latent demand for long-haul travel in the European market.<sup>7</sup>

This rapid re-emergence demonstrates the inherent stability and "stickiness" of the global hub-and-spoke system. Despite two years of profound disruption, both airlines and passengers quickly reverted to established, pre-pandemic patterns of using geographically strategic hubs for intercontinental connections as soon as they were permitted to do so. The system's underlying value proposition—efficiently connecting vast and disparate parts of the world—was not destroyed by the pandemic, merely suppressed. The swift snap-back of these hubs proves the enduring value of their network infrastructure and geographic advantages, which are difficult to displace without a fundamental and permanent shift in airline network strategies.

### **2023: A New Equilibrium**

By 2023, the global aviation industry had reached a new equilibrium, with passenger traffic recovering to 93.8% of pre-pandemic levels and totaling nearly 8.5 billion passengers.<sup>9</sup> The top of the rankings reflected a blend of the most resilient American hubs and the most powerful international connectors, creating a stable, post-recovery hierarchy.

Hartsfield-Jackson Atlanta (ATL) solidified its leadership position, becoming the first airport to exceed 100 million passengers since the pandemic began, with a total of 104.7 million.<sup>17</sup> The most significant shift at the top was the ascent of Dubai International Airport (DXB) to the number two spot for the first time, surpassing Dallas/Fort Worth (DFW), which ranked third.<sup>9</sup> This confirmed Dubai's status as the world's premier hub for international passengers.

The year was also marked by the strong recovery of the Asia-Pacific region, which had lagged in previous years due to prolonged travel restrictions. The most remarkable evidence of this was Tokyo Haneda Airport (HND), which witnessed a remarkable ascent from 16th position in 2022 to fifth in 2023\.<sup>9</sup> The continued strength of hubs like Istanbul and Delhi, which maintained their top-ten rankings, further underscored the growing influence of non-traditional hubs in the global network.<sup>9</sup> The 2023 rankings thus represent the establishment of a "new normal," where the world's busiest airports list is a composite of hubs excelling in different but complementary models: domestic mega-hubs, intercontinental super-connectors, and rapidly growing hubs in emerging economic regions.

### **2024: Surpassing Pre-Pandemic Peaks**

The year 2024 marked the culmination of the industry's recovery narrative, with preliminary figures indicating that global passenger traffic surpassed pre-pandemic levels for the first time, reaching an estimated 9.5 billion passengers.<sup>8</sup> This represented a full recovery to 104% of 2019 traffic levels.<sup>21</sup>

The top of the rankings demonstrated stability and continued growth. Hartsfield-Jackson Atlanta (ATL) retained its title with 108.1 million passengers, followed by Dubai (DXB) with 92.3 million and Dallas/Fort Worth (DFW) with 87.8 million.<sup>14</sup> The top ten list also signaled a full-circle moment with the strong return of a key Chinese international hub. Shanghai Pudong International Airport (PVG) made a significant leap from 21st position in 2023 to the tenth spot in 2024, a comeback fueled by the easing of visa policies and the restoration of international flight services in the Asia-Pacific region.<sup>8</sup>

The sustained high rankings of airports like Istanbul and Delhi further confirmed their enhanced strategic importance in the post-pandemic aviation landscape.<sup>8</sup> The 2024 data solidifies a new world order in aviation, where leadership is defined not only by sheer volume but by a combination of strategic geographic positioning, strong national carrier support, and continuous infrastructure investment to capture both recovering and new sources of passenger demand.

## **Appendix: Data Sources and Airport Details**

### **Official Sources and References**

The data and analysis presented in this report are primarily derived from press releases, traffic summaries, and datasets published by Airports Council International (ACI) World and ACI-North America.

* ACI World Press Release (April 11, 2022): "The top 10 busiest airports in the world revealed"  
  * URL: https://aci.aero/2022/04/11/the-top-10-busiest-airports-in-the-world-revealed/  
* ACI World Press Release (April 5, 2023): "ACI World releases top 10 busiest airports worldwide for 2022"  
  * URL: https://www.aci.aero/news/2023/04/05/aci-world-releases-top-10-busiest-airports-worldwide-for-2022/ (Note: Link was inaccessible during research, data sourced from secondary reports citing this release)  
* ACI World Press Release (April 15, 2024): "ACI World shares top 10 busiest airports worldwide for 2023"  
  * URL: https://airportindustry-news.com/aci-world-reveals-top-10-busiest-airports-in-2023/ (Secondary source citing ACI)  
* ACI World Press Release (April 14, 2025): "The busiest airports in the world defy global uncertainty and hold top rankings" (Preliminary 2024 data)  
  * URL: https://aci.aero/2025/04/14/the-busiest-airports-in-the-world-defy-global-uncertainty-and-hold-top-rankings/  
* ACI-North America 2020 Airport Traffic Summary  
  * URL: https://airportscouncil.org/wp-content/uploads/2021/07/NAM2020-Top50.xlsx  
* ACI-North America Press Release (July 20, 2023): "Airports Council Releases 2022 North America Airport Traffic Rankings"  
  * URL: https://airportscouncil.org/press\_release/airports-council-releases-2022-north-america-airport-traffic-rankings/

### **Airport Physical Location Details**

| Airport | Location Details |
| :---- | :---- |
| Hartsfield-Jackson Atlanta International Airport | 6000 North Terminal Parkway, Atlanta, Georgia, USA |
| Guangzhou Baiyun International Airport | Baiyun-Huadu Districts, Guangzhou, Guangdong, China |
| Chengdu Shuangliu International Airport | Shuangliu District, Chengdu, Sichuan, China |
| Dallas/Fort Worth International Airport | 3200 E Airfield Drive, DFW Airport, Texas, USA |
| Shenzhen Bao'an International Airport | Bao'an District, Shenzhen, Guangdong, China |
| Chongqing Jiangbei International Airport | Yubei District, Chongqing, China |
| Beijing Capital International Airport | Shunyi District, Beijing, China |
| Denver International Airport | 8500 Peña Boulevard, Denver, Colorado, USA |
| Kunming Changshui International Airport | Guandu District, Kunming, Yunnan, China |
| Shanghai Hongqiao International Airport | Changning and Minhang Districts, Shanghai, China |
| Chicago O’Hare International Airport | 10000 West O'Hare Avenue, Chicago, Illinois, USA |
| Los Angeles International Airport | 1 World Way, Los Angeles, California, USA |
| Charlotte Douglas International Airport | 5501 Josh Birmingham Parkway, Charlotte, North Carolina, USA |
| Orlando International Airport | One Jeff Fuqua Boulevard, Orlando, Florida, USA |
| Harry Reid International Airport | 5757 Wayne Newton Boulevard, Las Vegas, Nevada, USA |
| Dubai International Airport | Al Garhoud District, Dubai, United Arab Emirates |
| Istanbul Airport | Tayakadın, Arnavutköy District, Istanbul, Turkey |
| Heathrow Airport | Hillingdon, London, United Kingdom |
| Indira Gandhi International Airport | Palam, New Delhi, Delhi, India |
| Paris Charles de Gaulle Airport | Roissy-en-France, Île-de-France, France |
| Tokyo Haneda Airport | Ōta, Tokyo, Japan |
| Shanghai Pudong International Airport | Pudong, Shanghai, China |

Sources: 14

#### **Work cited**

1. ACI's 2020 world airport traffic rankings show dramatic impact of ..., [https://www.internationalairportreview.com/news/157758/aci-2020-world-airport-traffic-rankings-covid-19/](https://www.internationalairportreview.com/news/157758/aci-2020-world-airport-traffic-rankings-covid-19/)  
2. The top 10 busiest airports in 2020 may surprise you \- Globalair.com, [https://www.globalair.com/articles/the-top-10-busiest-airports-in-2020-may-surprise-you?id=3585](https://www.globalair.com/articles/the-top-10-busiest-airports-in-2020-may-surprise-you?id=3585)  
3. ACI's World Airport Traffic Report reveals domestic traffic leading recovery, [https://aci.aero/2021/11/09/acis-world-airport-traffic-report-reveals-domestic-traffic-leading-recovery/](https://aci.aero/2021/11/09/acis-world-airport-traffic-report-reveals-domestic-traffic-leading-recovery/)  
4. The top 10 busiest airports in the world revealed, [https://aci.aero/2022/04/11/the-top-10-busiest-airports-in-the-world-revealed/](https://aci.aero/2022/04/11/the-top-10-busiest-airports-in-the-world-revealed/)  
5. Airports Council Releases 2021 North America Airport Traffic Rankings, [https://airportscouncil.org/press\_release/airports-council-releases-2021-north-america-airport-traffic-rankings/](https://airportscouncil.org/press_release/airports-council-releases-2021-north-america-airport-traffic-rankings/)  
6. ACI reveals top 10 busiest airports, [https://www.gtrmag.com/blog/aci-reveals-top-10-busiest-airports](https://www.gtrmag.com/blog/aci-reveals-top-10-busiest-airports)  
7. The World's Ten Busiest Airports In 2022 \- Simple Flying, [https://simpleflying.com/worlds-ten-busiest-airports-2022/](https://simpleflying.com/worlds-ten-busiest-airports-2022/)  
8. The busiest airports in the world defy global uncertainty and hold top rankings, [https://aci.aero/2025/04/14/the-busiest-airports-in-the-world-defy-global-uncertainty-and-hold-top-rankings/](https://aci.aero/2025/04/14/the-busiest-airports-in-the-world-defy-global-uncertainty-and-hold-top-rankings/)  
9. ACI World Reveals Top 10 Busiest Airports in 2023, [https://airportindustry-news.com/aci-world-reveals-top-10-busiest-airports-in-2023/](https://airportindustry-news.com/aci-world-reveals-top-10-busiest-airports-in-2023/)  
10. World's Busiest Airports Revealed in Final Global Rankings \- ACI World, [https://aci.aero/2025/07/08/worlds-busiest-airports-revealed-in-final-global-rankings/](https://aci.aero/2025/07/08/worlds-busiest-airports-revealed-in-final-global-rankings/)  
11. ACI Reveals World's Busiest Airports in 2024, [https://airportindustry-news.com/aci-reveals-worlds-busiest-airports-in-2024/](https://airportindustry-news.com/aci-reveals-worlds-busiest-airports-in-2024/)  
12. The top 10 busiest airports and the new post-pandemic world map \- InfraJournal, [https://www.infrajournal.com/en/w/top-10-busiest-airports-and-new-post-pandemic-world-map](https://www.infrajournal.com/en/w/top-10-busiest-airports-and-new-post-pandemic-world-map)  
13. Passenger \- Airports Council International \- North America, [https://airportscouncil.org/wp-content/uploads/2021/07/NAM2020-Top50.xlsx](https://airportscouncil.org/wp-content/uploads/2021/07/NAM2020-Top50.xlsx)  
14. List of busiest airports by passenger traffic \- Wikipedia, [https://en.wikipedia.org/wiki/List\_of\_busiest\_airports\_by\_passenger\_traffic](https://en.wikipedia.org/wiki/List_of_busiest_airports_by_passenger_traffic)  
15. Airports Council Releases 2022 North America Airport Traffic Rankings, [https://airportscouncil.org/press\_release/airports-council-releases-2022-north-america-airport-traffic-rankings/](https://airportscouncil.org/press_release/airports-council-releases-2022-north-america-airport-traffic-rankings/)  
16. Airports Council Releases 2024 North American Airport Traffic Rankings, [https://airportscouncil.org/press\_release/airports-council-releases-2024-north-american-airport-traffic-rankings/](https://airportscouncil.org/press_release/airports-council-releases-2024-north-american-airport-traffic-rankings/)  
17. Airports Council Releases 2023 North American Airport Traffic Rankings, [https://airportscouncil.org/press\_release/airports-council-releases-2023-north-american-airport-traffic-rankings/](https://airportscouncil.org/press_release/airports-council-releases-2023-north-american-airport-traffic-rankings/)  
18. Top 10 busiest airports in the world by passenger number, [https://www.internationalairportreview.com/article/32311/top-10-busiest-airports-world-passenger-number/](https://www.internationalairportreview.com/article/32311/top-10-busiest-airports-world-passenger-number/)  
19. COVID-19 pandemic and air transportation: Summary of Recent Research, Policy Consideration and Future Research Directions \- PubMed Central, [https://pmc.ncbi.nlm.nih.gov/articles/PMC9640395/](https://pmc.ncbi.nlm.nih.gov/articles/PMC9640395/)  
20. Hartsfield–Jackson Atlanta International Airport \- Wikipedia, [https://en.wikipedia.org/wiki/Hartsfield%E2%80%93Jackson\_Atlanta\_International\_Airport](https://en.wikipedia.org/wiki/Hartsfield%E2%80%93Jackson_Atlanta_International_Airport)  
21. Joint ACI World-ICAO Passenger Traffic Report, Trends, and Outlook, [https://aci.aero/2025/01/28/joint-aci-world-icao-passenger-traffic-report-trends-and-outlook/](https://aci.aero/2025/01/28/joint-aci-world-icao-passenger-traffic-report-trends-and-outlook/)  
22. ACI World Announces 2023's Busiest Airports, [https://www.airportxnews.com/aci-world-announces-2023s-busiest-airports/](https://www.airportxnews.com/aci-world-announces-2023s-busiest-airports/)  
23. A Hub Like No Other: 5 Reasons Why Atlanta Is The Busiest Airport On The Planet, [https://simpleflying.com/atlanta-airport-busy-reasons-list/](https://simpleflying.com/atlanta-airport-busy-reasons-list/)  
24. Why Atlanta? \- Real World Aviation \- Infinite Flight Community, [https://community.infiniteflight.com/t/why-atlanta/879090](https://community.infiniteflight.com/t/why-atlanta/879090)  
25. Hartsfield–Jackson Atlanta International Airport | ATL \- Alternative Airlines, [https://www.alternativeairlines.com/hartsfield-jackson-atlanta-international-airport](https://www.alternativeairlines.com/hartsfield-jackson-atlanta-international-airport)  
26. Hartsfield-Jackson Atlanta International Airport | The Good Traveler, [https://thegoodtraveler.org/aviation-partners/hartsfield-jackson-atlanta/](https://thegoodtraveler.org/aviation-partners/hartsfield-jackson-atlanta/)  
27. Hartsfield-Jackson Atlanta International Airport | Invest Clayton, [https://www.investclayton.com/atlanta-international-airport.php](https://www.investclayton.com/atlanta-international-airport.php)  
28. Record breaker: Hartsfield-Jackson Atlanta International Airport, [https://airport-world.com/record-breaker-hartsfield-jackson-atlanta-international-airport/](https://airport-world.com/record-breaker-hartsfield-jackson-atlanta-international-airport/)  
29. Hartsfield-Jackson Atlanta International ATLNext Program \- WSP, [https://www.wsp.com/en-us/projects/hartsfield-jackson-atlanta-international-airport](https://www.wsp.com/en-us/projects/hartsfield-jackson-atlanta-international-airport)  
30. How Dubai International Airport Grew To Become The 2nd Busiest In The World, [https://simpleflying.com/dubai-airport-growth/](https://simpleflying.com/dubai-airport-growth/)  
31. iGA Istanbul Airport takes lead in global hub air connectivity | Times Aerospace, [https://www.timesaerospace.aero/news/airports/iga-istanbul-airport-takes-lead-in-global-hub-air-connectivity](https://www.timesaerospace.aero/news/airports/iga-istanbul-airport-takes-lead-in-global-hub-air-connectivity)  
32. Dubai Airport Beats Heathrow, Incheon, Changi, Amsterdam, Istanbul, Paris, and Frankfurt as the Busiest International Airport Last Year: New Report You Need to Know \- Travel And Tour World, [https://www.travelandtourworld.com/news/article/dubai-airport-beats-heathrow-incheon-changi-amsterdam-istanbul-paris-and-frankfurt-as-the-busiest-international-airport-last-year-new-report-you-need-to-know/](https://www.travelandtourworld.com/news/article/dubai-airport-beats-heathrow-incheon-changi-amsterdam-istanbul-paris-and-frankfurt-as-the-busiest-international-airport-last-year-new-report-you-need-to-know/)  
33. How Dubai International Airport Is Dominating Global Air Travel With 87 Million Passengers In 2023, Becoming A Powerhouse Of The Travel Industry And Outpacing Istanbul And Hamad With Astonishing Growth \- Travel And Tour World, [https://www.travelandtourworld.com/news/article/how-dubai-international-airport-is-dominating-global-air-travel-with-87-million-passengers-in-2023-becoming-a-powerhouse-of-the-travel-industry-and-outpacing-istanbul-and-hamad-with-astonishing-growt/](https://www.travelandtourworld.com/news/article/how-dubai-international-airport-is-dominating-global-air-travel-with-87-million-passengers-in-2023-becoming-a-powerhouse-of-the-travel-industry-and-outpacing-istanbul-and-hamad-with-astonishing-growt/)  
34. Aviation | İGA Istanbul Airport, [https://www.igairport.aero/en/aviation/](https://www.igairport.aero/en/aviation/)  
35. İstanbul Airport | Turkish Airlines ®, [https://www.turkishairlines.com/en-int/istanbul-airport/](https://www.turkishairlines.com/en-int/istanbul-airport/)  
36. Ten Times\! Dubai Airport Announced as the World's Busiest for a Decade\!, [https://www.damacproperties.com/en/blog/ten-times-dubai-airport-announced-the-worlds-busiest-decade-0239/](https://www.damacproperties.com/en/blog/ten-times-dubai-airport-announced-the-worlds-busiest-decade-0239/)  
37. Aviation's substantial contribution to Dubai's economy revealed in latest report, [https://media.dubaiairports.ae/aviations-substantial-contribution-to-dubais-economy-revealed-in-latest-report/](https://media.dubaiairports.ae/aviations-substantial-contribution-to-dubais-economy-revealed-in-latest-report/)  
38. Aviation's substantial contribution to Dubai's economy revealed in latest report \- Dnata, [https://www.dnata.com/media-centre/aviations-substantial-contribution-to-dubais-economy-revealed-in-latest-report/](https://www.dnata.com/media-centre/aviations-substantial-contribution-to-dubais-economy-revealed-in-latest-report/)  
39. en.wikipedia.org, [https://en.wikipedia.org/wiki/Dubai\_International\_Airport\#:\~:text=In%202014%2C%20the%20airport%20indirectly,(DWC)%20is%20fully%20operational.](https://en.wikipedia.org/wiki/Dubai_International_Airport#:~:text=In%202014%2C%20the%20airport%20indirectly,\(DWC\)%20is%20fully%20operational.)  
40. DXB records highest annual traffic in 2024, celebrating a decade as the world's busiest international airport \- Dubai Airports News, [https://media.dubaiairports.ae/dxb-records-highest-annual-traffic-in-2024-celebrating-a-decade-as-the-worlds-busiest-international-airport/](https://media.dubaiairports.ae/dxb-records-highest-annual-traffic-in-2024-celebrating-a-decade-as-the-worlds-busiest-international-airport/)  
41. Who we are \- Dubai Airports, [https://dubaiairports.ae/corporate/our-story/who-we-are](https://dubaiairports.ae/corporate/our-story/who-we-are)  
42. DFW Airport Map and Terminal Guide: Where to Eat, Park, and Stay, [https://www.travelandleisure.com/airlines-airports/dfw-airport/dallas-fort-worth-airport-guide](https://www.travelandleisure.com/airlines-airports/dfw-airport/dallas-fort-worth-airport-guide)  
43. Airlines \- DFW International Airport, [https://www.dfwairport.com/explore/plan/airlines/](https://www.dfwairport.com/explore/plan/airlines/)  
44. Dallas Fort Worth International Airport \- Wikipedia, [https://en.wikipedia.org/wiki/Dallas\_Fort\_Worth\_International\_Airport](https://en.wikipedia.org/wiki/Dallas_Fort_Worth_International_Airport)  
45. Denver International Airport \- Wikipedia, [https://en.wikipedia.org/wiki/Denver\_International\_Airport](https://en.wikipedia.org/wiki/Denver_International_Airport)  
46. Airlines serving DEN | Denver airport, [https://airportden.com/airlines](https://airportden.com/airlines)  
47. About DFW & Fast Facts \- DFW International Airport | Official Website, [https://www.dfwairport.com/business/about/facts/](https://www.dfwairport.com/business/about/facts/)  
48. airports and regions: \- International Economic Development Council, [https://www.iedconline.org/clientuploads/Economic%20Development%20Journal/EDJ\_14\_Spring\_Ensign.pdf](https://www.iedconline.org/clientuploads/Economic%20Development%20Journal/EDJ_14_Spring_Ensign.pdf)  
49. DEN Generates \$36B Annually in Economic Impact for Colorado, [https://www.flydenver.com/press-release/den-generates-36b-annually-in-economic-impact/](https://www.flydenver.com/press-release/den-generates-36b-annually-in-economic-impact/)  
50. Study Shows DEN Generated \$47.2 Billion Annually in Economic Impact for Colorado, [https://www.flydenver.com/press-release/study-shows-den-generated-47-2-billion-annually-in-economic-impact-for-colorado/](https://www.flydenver.com/press-release/study-shows-den-generated-47-2-billion-annually-in-economic-impact-for-colorado/)  
51. DFW Airport Announces Start of Transformational Work on \$9 Billion Capital Plan with Reimagining of Terminal C, [https://www.dfwairport.com/dfwnewsroom/dfw-airport-announces-start-of-work-on-9b-capital-plan-with-terminal-c/](https://www.dfwairport.com/dfwnewsroom/dfw-airport-announces-start-of-work-on-9b-capital-plan-with-terminal-c/)  
52. Global traffic to reach 22.3 billion passengers by 2053 – ACI World \- Airport World, [https://airport-world.com/global-traffic-to-reach-22-3-billion-passengers-by-2053-aci-world/](https://airport-world.com/global-traffic-to-reach-22-3-billion-passengers-by-2053-aci-world/)  
53. ACI World projects 22.3 billion passengers by 2053, [https://aci.aero/2025/02/26/aci-world-projects-22-3-billion-passengers-by-2053/](https://aci.aero/2025/02/26/aci-world-projects-22-3-billion-passengers-by-2053/)  
54. ACI World Releases 2024-2053 Global Airport Traffic Forecasts, [https://www.airportxnews.com/aci-world-releases-2024-2053-global-airport-traffic-forecasts/](https://www.airportxnews.com/aci-world-releases-2024-2053-global-airport-traffic-forecasts/)  
55. Global air passenger numbers expected to reach 22.3 billion by 2053 \- Business Traveller, [https://www.businesstraveller.com/business-travel/2025/02/28/global-air-passengers-numbers-expected-to-reach-22-3-billion-by-2053/](https://www.businesstraveller.com/business-travel/2025/02/28/global-air-passengers-numbers-expected-to-reach-22-3-billion-by-2053/)  
56. Joint ACI World-ICAO Passenger Traffic Report, Trends, and Outlook \- Airport Suppliers, [https://www.airport-suppliers.com/joint-aci-world-icao-passenger-traffic-report-trends-and-outlook/](https://www.airport-suppliers.com/joint-aci-world-icao-passenger-traffic-report-trends-and-outlook/)  
57. Guangzhou Baiyun International Airport \- Wikipedia, [https://en.wikipedia.org/wiki/Guangzhou\_Baiyun\_International\_Airport](https://en.wikipedia.org/wiki/Guangzhou_Baiyun_International_Airport)  
58. Aviation | Atlanta, GA \- AtlantaGA.gov, [https://www.atlantaga.gov/government/departments/aviation](https://www.atlantaga.gov/government/departments/aviation)  
59. Chengdu Shuangliu International Airport \- Wikipedia, [https://en.wikipedia.org/wiki/Chengdu\_Shuangliu\_International\_Airport](https://en.wikipedia.org/wiki/Chengdu_Shuangliu_International_Airport)  
60. Dallas \- Fort Worth, TX (DFW) \- American Airlines, [https://www.aa.com/i18n/travelInformation/destinationInformation/dfw-airport.jsp](https://www.aa.com/i18n/travelInformation/destinationInformation/dfw-airport.jsp)  
61. Chongqing Jiangbei International Airport \- Wikipedia, [https://en.wikipedia.org/wiki/Chongqing\_Jiangbei\_International\_Airport](https://en.wikipedia.org/wiki/Chongqing_Jiangbei_International_Airport)  
62. Beijing Capital International Airport \- 北京市人民政府, [https://english.beijing.gov.cn/travellinginbeijing/transportation/airport/202005/t20200516\_1899219.html?v%3Djt](https://english.beijing.gov.cn/travellinginbeijing/transportation/airport/202005/t20200516_1899219.html?v%3Djt)  
63. Denver International Airport | DEN, [https://www.flydenver.com/](https://www.flydenver.com/)  
64. About Kunming Changshui International Airport \- World Travel Guide, [https://www.worldtravelguide.net/guides/asia/china/kunming-changshui-international-airport/](https://www.worldtravelguide.net/guides/asia/china/kunming-changshui-international-airport/)  
65. Shanghai Hongqiao International Airport \- Wikipedia, [https://en.wikipedia.org/wiki/Shanghai\_Hongqiao\_International\_Airport](https://en.wikipedia.org/wiki/Shanghai_Hongqiao_International_Airport)  
66. O'Hare International Airport \- Flychicago, [https://www.flychicago.com/ohare/home/pages/default.aspx](https://www.flychicago.com/ohare/home/pages/default.aspx)  
67. LAX Official Site | Welcome to Los Angeles International Airport, [https://www.flylax.com/](https://www.flylax.com/)  
68. Charlotte, NC (CLT) \- Airport information \- American Airlines, [https://www.aa.com/i18n/travelInformation/destinationInformation/clt-airport.jsp](https://www.aa.com/i18n/travelInformation/destinationInformation/clt-airport.jsp)  
69. Orlando International Airport \- City of Orlando, [https://www.orlando.gov/Parking-Transportation/Public-Transit/Orlando-International-Airport](https://www.orlando.gov/Parking-Transportation/Public-Transit/Orlando-International-Airport)  
70. Harry Reid International Airport | Las Vegas, NV, [https://www.vegasmeansbusiness.com/listing/harry-reid-international-airport/30559/](https://www.vegasmeansbusiness.com/listing/harry-reid-international-airport/30559/)  
71. İGA Istanbul Airport | Istanbul Grand Airport, [https://www.igairport.aero/en/](https://www.igairport.aero/en/)  
72. Heathrow: Welcome to Heathrow Airport | Heathrow, [https://www.heathrow.com/](https://www.heathrow.com/)  
73. Delhi Airport (DEL) \- Arrival, Departure, Transit & Travel Guide, [https://www.newdelhiairport.in/](https://www.newdelhiairport.in/)  
74. Welcome to Paris-Charles de Gaulle airport (CDG), [https://www.parisaeroport.fr/en/passengers/charles-de-gaulle-airport](https://www.parisaeroport.fr/en/passengers/charles-de-gaulle-airport)  
75. [TOKYO (HANEDA)] TOKYO INTERNATIONAL AIRPORT ... \- JAL, [https://www.jal.co.jp/jp/en/inter/airport/hnd/info/](https://www.jal.co.jp/jp/en/inter/airport/hnd/info/)  
76. en.wikipedia.org, [https://en.wikipedia.org/wiki/Shenzhen\_Bao%27an\_International\_Airport\#:\~:text=Shenzhen%20Bao'an%20International%20Airport%20(IATA%3A%20SZX%2C%20ICAO,northwest%20of%20the%20city%20centre.](https://en.wikipedia.org/wiki/Shenzhen_Bao%27an_International_Airport#:~:text=Shenzhen%20Bao'an%20International%20Airport%20\(IATA%3A%20SZX%2C%20ICAO,northwest%20of%20the%20city%20centre.)  
77. Harry Reid International Airport, [https://www.airport-suppliers.com/airport/harry-reid-international-airport/](https://www.airport-suppliers.com/airport/harry-reid-international-airport/)  
78. Istanbul Airport (IST) (International airport) \- Mapy.com, [https://mapy.com/en/?source=osm\&id=1069762460](https://mapy.com/en/?source=osm&id=1069762460)  
79. Indira Gandhi International Airport \- Wikipedia, [https://en.wikipedia.org/wiki/Indira\_Gandhi\_International\_Airport](https://en.wikipedia.org/wiki/Indira_Gandhi_International_Airport)  
80. Paris-Charles de Gaulle Airport (CDG) \- Mapy.com, [https://mapy.com/en/?source=osm\&id=11300608](https://mapy.com/en/?source=osm&id=11300608)  
81. RJTT/Tokyo International Haneda General Airport Information, [https://acukwik.com/Airport-Info/RJTT](https://acukwik.com/Airport-Info/RJTT)  
82. Shanghai International Airport: Address, Images, and Notes | Vietjet Air, [https://www.vietjetair.com/en/pages/travel-guides-1665635013747/shanghai-international-airport-address-images-and-notes-1703581258666](https://www.vietjetair.com/en/pages/travel-guides-1665635013747/shanghai-international-airport-address-images-and-notes-1703581258666)

[The End of Response]

### Single-Row (One extracted item)

[The Start of Single-Row]

| Year | Airport | Rank | Location | Total Passengers | Code(IATA/ICAO) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 2021 | Harry Reid International Airport | 10 | Las Vegas, Nevada, USA | 39,754,366 | LAS/KLAS |

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
