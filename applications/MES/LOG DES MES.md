---
date created: 2013-07-11T14:17:00+02:00
tags: [MES]
date modified: 2025-09-18T22:16:09+02:00
---
## Log

### [[2013-07-11]] 14:17 
Meeting met [[Stijn Vandenbroucke]] en Peter Drees

### [[2013-09-09]] 10:26 
Peter Drees gaat nog maar eens een document opstellen.
### [[2013-09-13]] 11:28 
Due date op 27/09 gezet. Indien dit niet wordt gehaald. Zelf afspraak met Stijn regelen of mail naar Herwig sturen.


[[2013-09-23]] 16:37 
Peter heeft verlof tot ergens 10 okt

[[2013-11-04]] 
  Rondgang gemaakt over welke signalen er gelogd moeten worden.
- # [[2014-01-16]] 14:24 
  Aanvraag ingediend voor openen poort FW 10.32.27.2 (Siemens OPC)
- # [[2014-01-24]] 14:39 
  Meeting gehad met Stijn
- # [[2014-02-11]] 13:00 
  Meeting met Peter gehad.
  
  Actielijst overlopen
- # [[2014-02-12]] 10:10 
  Twee rapporten bij gemaakt
  
  [DES-Looptijden](http://be-des-sql-001/Reports/Pages/Report.aspx?ItemPath=%2fDES%2fZakken+Installaties%2fDES-Looptijden)
  
  [DES-Aantal+per+shift-dag-week](http://be-des-sql-001/Reports/Pages/Report.aspx?ItemPath=%2fDES%2fZakken+Installaties%2fDES-Aantal+per+shift-dag-week)
- # [[2014-02-25]] 14:11 
  OPC is in orde gebracht
  
  ![image1](image1-8%201.png)
- #
- # [[2014-02-18]] 12:15 
  Met Pieter Bussche van EIV gebeld
  
  Pieter met Teamviewer het scherm van de OPC server laten overnemen.
  
  Fout niet gevonden.
  
  Pieter gaat Log nogmaals naar Siemens sturen. Ondertussen wordt de werkende config naar Dessel opgestuurd.
- # [[2014-02-28]] 15:54 
  de 2 sensoren gebruikt
  
  42-B511 (kant villa) = DI5.11
  
  49-B702 (kant sociaal geboux) = DI7.2
- # [[2014-04-01]] 14:12 
  Project loopt goed.
  
  [[2014-05-06]] 9:25
  
  Task naar achter verschoven, maar toch laten open staan als herinnering van de Actielijst
- # [[2014-05-22]] 15:48 
  Gisteren meeting met Andrew Page omdat Alexander van het interfacing project is gehaald
- # [[2014-10-20]] 12:08 
  SMFL gecontrolleerd
  
  [SMFL](onenote:DONE%20MES.one#SMFL&section-id={24FA2610-F368-461F-BF59-9038FAB38345}&page-id={2D59AB62-F311-4509-B293-A09767693498}&end&base-path=https://d.docs.live.net/648fe635197c5860/Documenten/OneNote's/Persoonlijk%20(web)/Sibelco/Projecten/MES)
- # [[2014-10-20]] 14:07 
  Op CS1 twee linkworx draaien. De ene werkt goed, de andere geeft connection uncertain.
- # [[2014-11-05]] 8:45 
  Extra logging gelegd op de W/Cs
- # [[2014-12-19]] 8:15 
  Droger4 (PDP03) gekoppeld
  
  [MES Tonnage D4](onenote:..\..\..\TODO's.one#MES%20Tonnage%20D4&section-id={7D21311A-5A29-4D4A-9AF9-A46A0666E433}&page-id={4EF3BBA9-2C4F-4AD9-8357-16CB812A650F}&end&base-path=https://d.docs.live.net/648fe635197c5860/Documenten/OneNote's/Persoonlijk%20(web))
- # [[2014-12-31]] 11:29 
  PML01 en PML02 gekoppeld
- # [[2015-01-09]] 13:59
  Rapport met Peter besproken

[[2017-10-10]] 
Probleempje met de labelprinters gehad. Er bleven labels in de cue zitten. Print Spooler herstart.

[[2021-08-30]]
Delta tonnage voor BU55 en BU124 wordt bijgehouden bij openen (BU124) of vrijgave (BU55) bunker
  
[[2021-08-25]]: Voor elke bunker voorzien.

[[2021-08-27]]:
De differentiatie functie reageert te snel.
Voor bunkers BU121 – BU125 de filtertijd op 3600 gezet.
  
[[2021-08-30]]:
Voor bunker BU124 beide filtertijden op 3600s gezet.
  
[[2021-09-01]]:

  ![image2](image2-4%201.png)
  
  ![image3](image3-2%201.png)
- # [[2021-09-13]] 
  Zanddetectie: parameters van AF5_6 zijn fout
  
  ![image4](image4-1%201.png)
- # [[2021-09-14]] 
  Joris gaat dit nakijken
- # [[2021-09-21]] 
  herinnering gestuurd
- # [[2021-09-29]] 
  Afgelopen 7 dagen geen stroommeting. Getest. en dan wel stroom. dus heeft AF5_6 al een tijd niet gedraaid
- # [[2022-01-21]]
- # Voor Molen 4 een test opgezet.
- # Open todo's
- ###### *DES - MES - Zand op band detectie*
  Zand detectie voorzien voor stockmoves waar geen tonnagemeter is.
  
  Bijvoorbeeld van BU57 naar BU105 zijn er veel correcties
- SMWS
  Hier is een tonnagemeter
- SMD4
  De tonnageteller wordt enabled door sequentie.
  
  ![image5](image5-1%201.png)
- SMDS1
  SMDS1_EnableProductionCounter := ((Poc.SMDS1.AF5_ZS41.Rev.FB1 AND Par.MES.SMDS1_source1_location_id =41) OR
  (Poc.SMDS1.AF5_ZS42.Rev.FB1 AND Par.MES.SMDS1_source1_location_id =42) OR
  (Poc.SMDS1.AF5_ZS43.Rev.FB1 AND Par.MES.SMDS1_source1_location_id =43) OR
  (Poc.SMDS1.AF5_ZS44.Rev.FB1 AND Par.MES.SMDS1_source1_location_id =44) OR
  (Poc.SMDS1.AF5_ZS45.Rev.FB1 AND Par.MES.SMDS1_source1_location_id =45) OR
  (Poc.SMDS1.AF5_ZS46.Rev.FB1 AND Par.MES.SMDS1_source1_location_id =46) OR
  (Poc.SMDS1.AF5_ZS47.Rev.FB1 AND Par.MES.SMDS1_source1_location_id =47)) AND Poc.SMDS1.AF5_11.Rev.FB1
- SMDS2
  SMDS2_EnableProductionCounter := Poc.Lossen_SIB.TZ_B6.Rev.FB1 AND Keuze72_74;
- SMCAL
  SMCAL_EnableProductionCounter := ((Par.Kleppen.AF5_ZS54.StatOpen AND Par.MES.SMCAL_source1_location_id = 54) OR
  (Par.Kleppen.AF5_ZS55.StatOpen AND Par.MES.SMCAL_source1_location_id = 55) OR
  (Par.Kleppen.AF5_ZS56.StatOpen AND Par.MES.SMCAL_source1_location_id = 56) OR
  (Par.Kleppen.AF5_ZS57.StatOpen AND Par.MES.SMCAL_source1_location_id = 57)) AND
  
  Par.Motoren.AF5_6\_StatRun;
- SMOB2
  Gebeurt via tonnageberekening
- #### *DES - MES - Stock move mes koppeling versimpelen*
  [[2022-01-25]] : Meeting opgezet over workflow

[[journals/2022-05-03]] 
  Molen5 overgezet. Even afwachten op de de fouten.

#### [[2022-05-30]] 
Molen3 gaat niet goed.
### Afwachten op Stijn  [[2022-06-27]] 
  In de test-omgeving starten van een MO op M5
  
  ![image6](image6-1%201.png)
  
  ![image7](image7-1%201.png)
  
  ![image8](image8-1%201.png)
  
  ![image9](image9-1%201.png)
  
  ![image10](image10%201.png)
  
  ![image11](image11%201.png)
  
  IN PRODUCTIE OMGEVING
  
  ![image12](image12%201.png)
  
  ![image13](image13%201.png)
  
  ![image14](image14%201.png)
  
  ![image15](image15%201.png)
  
  ![image16](image16%201.png)
- # [[2023-02-02]] 
  Twee tags aan MES toegevoegd:
  
  In Underlying
  
  ![image17](image17.jpg)
  
  En in de administrator
  
  ![image18](image18.jpg)
  
  NIET VERGETEN OM opc\genericmodel\steeringingsamples.xml aan te passen
- # [[2023-02-07]] 
  de twee tags zijn bij in de database gekomen. SIBELCO_LABO_STEERING_SAMPLE
  
  SELECT \[TT201_02\]
  
  ,\[Killn_rpm\]
  
  FROM \[Linkworx\].\[dbo\].\[SIBELCO_LABO_STEERING_SAMPLE\]
  
  Ook moet een alter View van de view.bi_steering_sample_data worden gedaan.
  
  De extra velden komen er dan bij
  
  DIT WERKT PAS ALS ER EEN NIEUW STAAL WORDT GEMAAKT
  
  ![image19](image19%201.png)
- # [[2023-02-14]] 
Eindelijk nog een doorbraak :-)
De test omgeving is in orde.
  
**AFSPRAKEN:**
MES is baas. Ook voor overgang van kwaliteit. Overgang van kwaliteit enkel mogelijk maken indien MES geforceerd wordt
  
**Flow:**
Bij een volle bunker, schrijf naar location_id. MES schrijft naar location_id_request. Indien de location_id_request niet volgt, dan moet een alarm komen.  
Test van het starten MO

| Operation | Materiaal | Dest1 | Dest2 | ABB item1 | ABB dest1 | ABB item2 | ABB dest2 |
| --------- | --------- | ----- | ----- | --------- | --------- | --------- | --------- |
| 1545      | M300/M500 | 52    | 64    | 1628      | 52        | 1631      | 64        |
| 1595      | M500/M300 | 64    | 54    | 1631      | 64        | 1628      | 52        |
| 1548      | M300/M500 | 53    | 23    | 1631      | 23        | 1631      | 53        |
| 1548      | M300/M500 | 53    | 23    | 1631      | 23        | 1628      | 53        |
| 1548      | M300/M500 | 52    | 64    | 1631      | 64        | 1628      | 52        |
| 1553      | M30/M500  | 52    | 24    | 1631      | 24        | 1628      | 52        |
| 1545      | M300/M500 | 52    | 64    | 1628      | 52        | 1631      | 64        |
| 1544      | M300/M500 | 52    | 65    | 1628      | 52        | 1631      | 65        |
| 1535      | M400      | 26    |       | 10897     | 26        |           |           |
| 1537      | M400      | 24    |       | 10897     | 24        |           |           |
| 1536      | M300BL    | 60    |       | 1640      | 60        |           |           |
|           |           |       |       |           |           |           |           |
| 1568      | M300BL    | 66    |       | 1640      | 64        |           |           |
| 1537      | M400      | 26    |       | 10897     | 26        |           |           |
| 1568      | M300BL    | 66    |       | 1640      | 66        |           |           |
|           |           |       |       |           |           |           |           |
| 1568      | M30BL     | 66    |       | 1640      | 66        |           |           |
| 1580      | M10       | 24    |       | 1648      | 24        |           |           |

### [[2023-02-16]] 
Fouten in MES zijn opgelost.
Wacht op mogelijke stilstand van M5
### [[2023-03-02]] 
M5 is aangepast. Maar mogelijk zit er nog een fout in want gisteren viel de molen uit.