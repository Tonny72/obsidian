---
title: 'FPV Sibelco: reactief vermogen leveren'
updated: [[2021-06-18]]T07:55:01.0000000+02:00
created: [[2021-06-18]]T07:24:04.0000000+02:00
---

> FPV Sibelco: reactief vermogen leveren
vrijdag 18 juni 2021
7:24

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Subject</strong></th>
<th><strong>FPV Sibelco: reactief vermogen leveren</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>From</strong></td>
<td><a href="mailto:nicolas.greant@external.engie.com">nicolas.greant@external.engie.com</a></td>
</tr>
<tr class="even">
<td><strong>To</strong></td>
<td>Tonny Lemmens; Harry Stienen</td>
</tr>
<tr class="odd">
<td><strong>Cc</strong></td>
<td>olaf.rabaey@engie.com; marc.ceyssens@external.engie.com</td>
</tr>
<tr class="even">
<td><strong>Sent</strong></td>
<td>maandag 31 mei 2021 17:27</td>
</tr>
<tr class="odd">
<td><strong>Attachments</strong></td>
<td><p>&lt;&lt;Cos phi management Sibelco FPV en EDFwind _V5.docx&gt;&gt;</p>
<p>&lt;&lt;[[2021-05-20]]-NGR-calc-Ploss.xlsx&gt;&gt;</p></td>
</tr>
</tbody>
</table>

Hey Tonny, Harry,

Zie curve in bijlage p.7/15: wij hebben destijds afgesproken Smax = 4050 kVA en Qmax = 1440 kVA zodat we ons actief-vermogensverlies (P) beperken.
Uit de setpoint file van Tonny zien we dat jullie regelmatig meer dan 2000 kVA vragen.
Kan je dit nog eens nakijken aub?

Zie Excel file in bijlage ter illustratie:

- als wij meer dan 4050 kW produceren dan zouden jullie geen reactief mogen vragen
- als wij P = 4000 kW produceren dan zouden jullie niet meer dan 12.5% van 5000 kVA (ofte 625 kVAr) mogen vragen
- …
- als wij P = 3900 kW produceren dan zouden jullie niet meer dan 21.5% van 5000 kVA (ofte 1075 kVAr) mogen vragen
- …
- als wij minder dan 3800 kW produceren dan zouden jullie niet meer dan 28% van 5000 kVA (ofte 1400 kVAr) mogen vragen
  
  Mvg,
  
  **Nicolas GRÉANT**
  Project Manager
  Solar Technics
  
  [**nicolas.greant@external.engie.com**](mailto:%20nicolas.greant@external.engie.com)
  **+32 (0)474 211 428**
  
  ![image1](image1-99.png)
  
  [**engie-solutions.be**](https://eur01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fengie-solutions.be%2F&data=04%7C01%7CTonny.Lemmens%40sibelco.com%7C22af381a58724cac77df08d92448baff%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C637580717466448508%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&sdata=aUofGUnaDcej2UgY2lyE26G6NxbKLcm1eJy%2B3RFbAeo%3D&reserved=0)
  
  Gelieve rekening te houden met het milieu voordat u dit document afdrukt
  
  ![image2](image2-58.png)
  
  ENGIE Mail Disclaimer: <http://www.engie.com/disclaimer/>
  
  | **Subject** | **RE: FPV Sibelco: reactief vermogen leveren**                                                  |
  |-------------|-------------------------------------------------------------------------------------------------|
  | **From**    | <nicolas.greant@external.engie.com>                                                             |
  | **To**      | Tonny Lemmens; Harry Stienen                                                                    |
  | **Cc**      | marc.ceyssens@external.engie.com; service-solartechnics.esolbe@engie.com; olaf.rabaey@engie.com |
  | **Sent**    | donderdag 17 juni 2021 15:56                                                                    |
  
  Hey Tonny, Harry,
  
  Tenzij ik me vergis zie ik nog geen aangepaste cos phi sturing.
  
  Vandaag vroegen jullie bv Q = 25.6% toen wij P = 4443 kW aan het produceren waren.
  Daardoor boeten wij in aan actief vermogen en kunnen wij ons rendement richting LRM / Floating PV niet halen.
  
  Ik stel voor dat Olaf onze programmatie dus aanpast en de beperking bij ons inprogrammeert (tenzij tegenbericht).
  
  ![image3](image3-4.jpg)
  
  Mvg,
  
  **Nicolas GRÉANT**
  Project Manager
  Solar Technics
  
  [**nicolas.greant@external.engie.com**](mailto:%20nicolas.greant@external.engie.com)
  **+32 (0)474 211 428**
  
  ![image1](image1-99.png)
  
  [**engie-solutions.be**](https://eur01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fengie-solutions.be%2F&data=04%7C01%7CTonny.Lemmens%40sibelco.com%7C25f91f698c1f46bcaf3d08d93197c0c2%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C637595350154366221%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&sdata=NOo96LdNJJ8Y6W%2FtZITmGgUSKxorg6tSlhu%2BTGY%2F96w%3D&reserved=0)
  
  Gelieve rekening te houden met het milieu voordat u dit document afdrukt
  
  ![image2](image2-58.png)
  
  **From:** GRÉANT Nicolas (ENGIE Benelux)
  **Sent:** maandag 31 mei 2021 17:28
  **To:** Tonny Lemmens \<Tonny.Lemmens@sibelco.com\>; Harry Stienen \<harry.stienen@sibelco.com\>
  **Cc:** RABAEY Olaf (ENGIE Benelux) \<olaf.rabaey@engie.com\>; CEYSSENS Marc (ENGIE Benelux) \<marc.ceyssens@external.engie.com\>
  **Subject:** FPV Sibelco: reactief vermogen leveren
  
  Hey Tonny, Harry,
  
  Zie curve in bijlage p.7/15: wij hebben destijds afgesproken Smax = 4050 kVA en Qmax = 1440 kVA zodat we ons actief-vermogensverlies (P) beperken.
  Uit de setpoint file van Tonny zien we dat jullie regelmatig meer dan 2000 kVA vragen.
  Kan je dit nog eens nakijken aub?
  
  Zie Excel file in bijlage ter illustratie:
- als wij meer dan 4050 kW produceren dan zouden jullie geen reactief mogen vragen
- als wij P = 4000 kW produceren dan zouden jullie niet meer dan 12.5% van 5000 kVA (ofte 625 kVAr) mogen vragen
- …
- als wij P = 3900 kW produceren dan zouden jullie niet meer dan 21.5% van 5000 kVA (ofte 1075 kVAr) mogen vragen
- …
- als wij minder dan 3800 kW produceren dan zouden jullie niet meer dan 28% van 5000 kVA (ofte 1400 kVAr) mogen vragen
  
  Mvg,
  
  **Nicolas GRÉANT**
  Project Manager
  Solar Technics
  
  [**nicolas.greant@external.engie.com**](mailto:%20nicolas.greant@external.engie.com)
  **+32 (0)474 211 428**
- # [[2021-06-18]] 7:47 
  Cos Phi setpunt van 0.97 naar 0.96 gezet