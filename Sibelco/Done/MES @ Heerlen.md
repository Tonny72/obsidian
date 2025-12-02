---
date created: 2017-07-20
date modified: 2025-08-31
---

| **Subject** | **MES @ Heerlen**                                                            |
|-------------|------------------------------------------------------------------------------|
| **From**    | [Stijn Vandenbroucke](mailto:stijn.vandenbroucke@linkworx.eu)                |
| **To**      | Timo Rutten (T.Rutten@inofil.nl); Tonny Lemmens; May Jaspers; Hans Ophelders |
| **Cc**      | Dries Deweerdt; Peter Drees                                                  |
| **Sent**    | woensdag 31 mei 2017 22:09                                                   |

Heren,

Bedankt voor de zeer constructieve dag! Hieronder een samenvatting van de todo’s en afspraken.

**<u>Afspraken:</u>**

- Voor de zandbergen is er momenteel geen goede oplossing beschikbaar om te weten welk vak gebruikt wordt.
  Om deze reden wordt ervoor gekozen om selectie van de zandbergen altijd door de operator te laten tot. Op het ogenblik dat er een technische oplossing zou komen die kan aangeven welk vak actief is, kan dit verfijnd worden.
- Prioritair zijn 4 tonnage tellers die ontbreken (detail hieronder), Timo koppelt terug op welke termijn deze kunnen voorzien worden.
- Voor de niet lot gecontroleerde artikelen onderscheiden we volgende:
	- Het feed item dat uit de groeve komt, blijft niet lot gecontroleerd. Op dit ogenblik kan dit nog niet gerapporteerd worden via MES gezien beperking in de M3 interface. Timing wanneer dit wordt aangepast zal ikzelf terugkoppelen.
	- De andere items die uit de hydro komen en niet lot gecontroleerd zijn, zullen aangepast worden en lot gecontroleerd worden. Hiervoor dient afspraak met Percy Pauwels / Jan Smolders gemaakt te worden zodat bestaande orders kunnen verwijderd worden en na aanpassing door Jan, nieuwe orders worden aangemaakt. De actie hiervoor zit bij May om dit af te stemmen met Percy en Jan.
- Inofil kan beroep doen op Dries in functie van integratie / controle & test IFIX tags
- We houden iedereen betrokken in de communicatie (Timo, kan je mail adres van je collega ook bezorgen?)
  
  **<u>Te beslissen:</u>**
- Bijsturingsfactor op tonnage meting: instellen in IFIX of instellen in MES? (1<sup>ste</sup> moet geprogrammeerd worden, 2<sup>e</sup> is beschikbaar)
  
  **<u>Timing:</u>**
- Gezien beperkte inspanning nodig is om automatisch te rapporteren, zien we dit graag binnen de maand afgerond
  
  **<u>Reeds beschikbaar in IFIX:</u>**
- **SHOVEL(PMN12):** Tonnageteller beschikbaar, te testen
- **HYDRO (PWP07):** Tonnageteller beschikbaar, te testen ; doel-/productielocaties zullen manueel worden ingegeven in MES
- **MAGNEET SEPARATIE (PWP08):** Tonnageteller beschikbaar, te testen ; doel-/productielocaties zullen manueel worden ingegeven in MES
- **DROGERS (PDP06 en PDP07):** doellocatie/productielocatie beschikbaar, te testen
- **MOLEN (PML11):** Tonnageteller beschikbaar, test testen ; doel-/productielocatie beschikbaar maar om te zetten naar integer, te testen
  
  **<u>Todo Inofiil (in volgorde van belangrijkheid):</u>**
- 2x Tonnageteller voor stockmove (toevoer naar buffer droger 1 + toevoer naar buffer droger 2)
- 2x Tonnageteller voor droger
- Bron- en doel locatie molen
- Vrijgave bit per workcenter (+ overrule mogelijkheid in M3)
  
  *<u>Programmatie Tonnageteller Stockmove naar buffer droger:</u>*
  aan de hand van de stand van de zwenktrechter (S11 of S12) en de tonnageteller na de shovel/dump hopper.
  ![image1](image1-50%201.png)
  
  *<u>Programmatie Tonnageteller droger:</u>*
  volgens integratie principe Tony
  
  Vb droger 1
  
  Gewicht silo1 wordt iedere 5s gemeten
  
  Gewicht_T1 = 25.060T
  Gewicht_T2 = 25.059T
  =\> 0.001T/5s =\> 0.72T/u
  
  Indien silo1 wordt bijgevuld met bijvb 0.43T/u (flow mass)
  ====\> outputsnelheid = 0.72T/u + 0.43T/u = 1.15T/u
  ====\> tonnage teller ook iedere 5 seconden verhogen adhv de berekende outputsnelheid
  
  *<u>Programmatie Molen:</u>*
  Bronlocaties (Silo 3, 4 of 5): bitomzetten naar integer en deze integer waarde voorzien als tag in IFIX
  
  [[2017-10-16]]
  IFix server is geïnstalleerd, en we hebben backups gemaakt.
  Volgens Timo Rutten wordt de server na de herfstvakantie in gebruik genomen.
  [[journals/2017-11-16]]
  **From:** Hans Ophelders
  **Sent:** dinsdag 14 november 2017 20:52
  **To:** Stijn Vandenbroucke \<<stijn.vandenbroucke@linkworx.eu>\>
  **Cc:** Tonny Lemmens \<<Tonny.Lemmens@sibelco.com>\>; Herwig Janssen \<<Herwig.Janssen@sibelco.com>\>; Harry Stienen \<<Harry.Stienen@sibelco.com>\>
  **Subject:** RE: MES @ Heerlen
  
  Stijn,
  
  Het enige waar we nu nog mee bezig zijn is de koppeling van de bandwegers van de droogzand, de rest is klaar.
  
  Gr. Hans
- # [[2017-11-24]] 
  Gepland voor week van [[2017-12-18]]
- # [[2018-01-09]] 
  ![image2](image2-4.jpg)
  
  ![image3](image3-2.jpeg)
- # [[2018-01-09]] 
  [[2018-01-17]] gaan Kristof en ik naar Heerlen
- # [[2018-01-17]]
  Ping van MES server Heerlen (NL-HRL-APS-002 - 10.31.250.20) naar 10.31.244.17 (ifix server) lukt niet
  
  Er dient wat op de ESX worden aangepast. Hiervoor is een reboot nodig. Dit wordt door Kristof op [[2018-02-09]] gedaan.
- # [[2018-03-02]] 
  Ik heb de tags van de MES in Heerlen toegevoegd in de underlying van de MES server.
  <http://10.31.250.20:59171/?module=tagoverview>
  
  (Hier staan de tags van ifix sever)
  <http://10.31.250.40:59160/?module=tagoverview>
- # [[2018-03-19]] 
  Mail van Hans
  
  [IFIX TAGS - Workcenters_2.xlsx](assets/resources/IFIX_TAGS_-_Workcenters_2.xlsx)
  ![image4](image4-12%201.png)
- # [[2018-04-09]] 
  Live gegaan met IFIX
  Infofil moet nog extra tags maken
  [Extra Tags voor Inofil](onenote:https://linkworx-my.sharepoint.com/personal/stijn_vandenbroucke_linkworx_eu/Documents/projects/Sibelco/sibelco%20-%20heerlen/Overzicht%20tags.one#Extra%20Tags%20voor%20Inofil&section-id={3218A2E7-29D6-4B80-B4FA-2ABF23E00B88}&page-id={DF6D03F0-FD53-413E-A62F-79C039AD4893}&end)
  
  Ook moet Linkworx nog als service kunnen starten.
  De oude draait in folder opcuaserver. De nieuw in folder linkworx.
  De Service wil niet draaien met user ifixadmin (access denied). Aan Inofil het administrator password gevraagd
  todo: de nieuwe 'in de linkworx folder' server indienst pakken. Niet vergeten de opc en http aan te passen
- # [[2018-04-27]] 
  Herinnnerings mail naar Timo gestuurd.
  [Overzicht tags](onenote:https://linkworx-my.sharepoint.com/personal/stijn_vandenbroucke_linkworx_eu/Documents/projects/Sibelco/sibelco%20-%20heerlen/Overzicht%20tags.one#section-id={3218A2E7-29D6-4B80-B4FA-2ABF23E00B88}&end)
- # [[2018-06-18]] 
  Verwerking van de Excel van Timo
  [Lijst bijgewerkt](onenote:https://linkworx-my.sharepoint.com/personal/stijn_vandenbroucke_linkworx_eu/Documents/projects/Sibelco/sibelco%20-%20heerlen/Overzicht%20tags.one#Extra%20Tags%20voor%20Inofil&section-id={3218A2E7-29D6-4B80-B4FA-2ABF23E00B88}&page-id={DF6D03F0-FD53-413E-A62F-79C039AD4893}&object-id={8B15088F-DEDA-0CB5-2DCD-5804019B6038}&11)
- # [[2018-06-20]] 
  Nieuwe tags actief gezet