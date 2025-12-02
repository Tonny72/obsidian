---
title: LOG ALG ENERGY
updated: 2017-02-27T10:25:22
date created: 2012-11-21T11:15:01+02:00
date modified: 2025-10-20T20:21:48+02:00
---

- # maandag 22 oktober 2012
  Tags werken
- # [[2012-11-22 1]] 11:01 
  Product ingeven bij start
- # donderdag 15 november 2012
  Verder gewerkt aan tabel. Iets nieuw ontdekt <Http://10.32.83.140:80/Reports>
  
  Afwerken excel tabel van Bart (zie printout)
  
  Geprobeerd van extra tags toe te voegen… niet gelukt ☹
- # [[2012-12-06]] 11:04 
  Deling van de wasserij klopt niet
- # [[2012-12-06]] 13:29 
  Rapport MHZ_Aanvoerzand_Day
- # [[2012-12-11]] 13:28 
  Product bij start ingeven wordt niet gedaan door operators.
  
  Sequentie aanpassen [Sequentie aanpassen voor kwaliteit en locatie](onenote:#Sequentie%20aanpassen%20voor%20kwaliteit%20en%20locatie&section-id={ADFBBDB8-912C-4765-8B59-7E623A7FC499}&page-id={C31CA99D-AF97-451E-A3B4-C41ACA48BAFC}&end&base-path=https://d.docs.live.net/648fe635197c5860/D%20DATA%20NOTEBOOK/TODO's.one)
- # [[2012-12-11]] 16:50 
  MHZ_Wasserij_Detail_Day
  
  MHZ_Wasserij_Overzicht_Day
  
  MHZ_PACs en kWh pulsen \_Day
- # [[2013-01-08]] 16:11 
  Gevraagd aan Kristof wat de coordinaten van de server zijn.
- # [[2013-01-17]] 16:16 
  Nogmaals mail naar Kristof gestuurd.
  
  [Tonny Lemmens - Fw: SQL Server](Notes://BEDESNTS1/C12566FD00314CF5/DABA975B9FB113EB852564B5001283EA/90E4FC980512E372C1257AF60053CAC7)
- # [[2013-02-01]] 16:04 
  Gestart met installatie Windows op DES Esx3 (10.32.19.47)
  
  SP1 is bezig.
- # [[2013-01-08]] 16:27 
  Mail naar Stijn gestuurd
  
  *Even de draad terug opnemen ...*
  
  *1. Replicatie Maasmechelen - Dessel.*
  
  *In Dessel staat een server klaar waar SQL server op geïnstalleerd kan worden.*
  
  *Ik vermoed dat poorten 1433 en 1434 van en naar beide servers moeten open staan. Of zijn er extra nodig?*
  
  *Ik heb nog wel nooit een replicatie opgezet. Mogelijk heb ik assistentie nodig.*
  
  *2. Ivm HDA*
  
  *Heb je nog iets gedaan met vorige mail die ik heb gestuurd.*
  
  *Wat is volgens u de beste manier?*
  
  *3. Er komen geen rapporten meer binnen via email. Ik weet niet waarom.*
- # [[2013-01-08]]
  Mail ontvangen
  
  *1) Voor SqlServer: 1433 en 1434 zijn inderdaad de basic poorten. Ik vermoed dat er voor de nieuwe tools binnen SQL 2012 mogelijks nog andere poorten zullen nodig zijn ook.*
  
  *Zorg dat je je werkwijze goed documenteert met screenshots, zodat je ook nog kunt terugzoeken welke instelling waar actief was. Met de mirroring heb ik ook nog in de ‘master’ tabellen met querien om zaken opnieuw in orde te krijgen...*
  
  *2) Voor HDA: nu werkt HDA op twee manieren:*
    *a. als ‘restore’ voor ‘DA’ (nl bij herstart)*
  *b. ofwel periodiek overhalen van data mbv een aggregatie type*
  
  *Ik denk dat het afhankelijk is van het proces welke methodiek toepasbaar is. Persoonlijk heb ik een lichte voorkeur om in normaal regime ‘da’ te gebruiken zodat de gelogde waarde onafhankelijk is van een mogelijke aggregatie die door de HDA Server wordt uitgevoerd. Uit een snel testje is gebleken dat je toch al snel weer met kleine afwijkingen moet rekening houden.*
  
  *Het lijkt me dat we best samen eens alles op een rijtje zetten en pro- en contra’s afwegen.*
  
  *3) Op 22/12 is er om 3u ’s nachts een herstart geweest van de ua machine. Ik vermoed dat er nog een delay in het opstarten van de rapporterings service moet komen =\> als de service al start en de SQLServer Report Service is nog niet actief, dan start het mogelijks niet correct (dat is geen zekerheid, maar een indruk). Ik heb nu een testje gedaan en het lijkt terug ok. Ik hou het mee in de gaten.*

[[2013-01-30]] 12:08 
Meeting met [[Stijn Vandenbroucke]] en Pieter Sijmons van Control & Protection
[[Archive/applications/Kepware/Kepware]] Connectivity Suite in MHZ installeren.

[[2013-01-30]] 16:13 
Kepware installatie bestanden gedownload.
# [[2013-01-30]] 16:27 
  Installatie gestart op MHZEngClient
  
  Selecteer bij drivers OPC Connectivity suite
- # [[2013-01-31]] 10:22 
  Eindelijk kunnen starten met installatie Kepware op CS1
- # [[2013-01-31]] 15:31 
  Kepware server op AS1 en LinkWorx server geïnstalleerd. Krijg dit niet werkend. Quality van de tags is good, maar er worden geen waarden getoond.
  
  Redundancy master geeft wel het gewenste resultaat.
  
  Mail naar Stijn gestuurd voor een offerte.
- # [[2013-02-01]] 8:54 
  Gestart met LinkWorx pc in Dessel te installeren.
  
  Via mail aan Stijn gevraagd of SQL Server Express voldoende is.
- # [[2013-02-04]] 14:13 
  SQL Server install gestart
- # [[2013-02-05]] 15:26 
  LinkWorx in Dessel geïnstalleerd en Database aangemaakt.
- # [[2013-02-06]] 11:13 
  Tag aangemaakt, maar Linkworx krijgt geen verbinding met AS1. Kepware Redundancy master heeft ook problemen.
- # [[2013-02-06]] 14:19 
  Vandaag een aantal mails gedaan m.b.t. de stabiliteit in MHZ
  
  Monitoring server van de aspect gehaald en terug op de Linkworx pc gezet.
- # [[2013-02-07]]
  90 dagen trial ontvangen en geïnstalleerd in MHZ
- # [[journals/older/2013/2013-02-08]] 10:34 
  Geprobeerd Redundancy master in Dessel te installeren. Maar krijg het niet geconfigureerd. Mail naar Kepware gestuurd.
- # [[2013-02-13]] 12:06 
  Reducancy master draait
  
  DCOM problemen naar remote abb opc server. Peter Stroop gecontacteerd.
- # [[2013-02-15]] 8:31 
  Update naar Stijn gestuurd.
  
  Een mail naar Wilfired Pauwels gestuurd ivm OPC connectie Dessel
- # [[2013-02-18]] 8:49 
  MHZ gecontrolleerd. Loopt stabiel
- # [[2013-02-18]] 15:49 
  Meeting EMIS gehad
  
  Gestart met installatie W7 voor Linkworx in MHL
  
  W7 SP1 kopieren en installeren
  
  Underlying tags aanmaken voor PACs
  
  ![image1](image1-1%201.png)
- # Voorbeeld Bbzand
  VB_15_9\_Alg
  
  VB_15_9\_PV
- # [[2013-02-18]] 8:49 
  DES - Energy bij onder de kap van ENERGY gestoken
- # [[2013-02-21]] 16:47 
  In Des en Mhl draait linkworx in console mode op de AS1 server.
- # [[2013-02-22]] 12:31 
  MHL still online
  
  MHZ still online
  
  DES still online :)
[[2013-02-25]] 8:42 

| MHZ | Online |
|-----|--------|
| MHL | Online |
| DES | Fout   |
Zeer eigenaardig DES was uitgevallen, maar is zomaar vanzelf in gang geschoten. Ik vermoed ip probleem. 2de netwerkkaart uitgeschakeld.

- # [[2013-02-25]] 11:30 
  Install van EMCO Ping monitor op laptop .
- # [[2013-02-25]] 13:40 
  Power config van DES aangepast. De pc zette zich na een half uur in sleep
[[2013-02-26]] 11:06 
MHZ deze morgen offline gekomen en niet meer in de gang gekregen
Linkworx maar op AS1 gestart.
Klein rapport in Crystal Reports gemaakt.


[[2013-02-26]] 16:45 
TAGS voor Dessel in [[Linkworx]] gezet
  
  PAC van Booster Donk nog doen
- # [[2013-02-27]] 8:13 
  Alle verstingingen Linkworx online
- # [[2013-02-28]] 11:41 
  Dagrapport MHZ is klaar in Crystal Reports
- # [[2013-03-04]] 8:57 
  Alle drie vestigingen Linkworx OK
- # [[2013-03-08]] 8:42 
  Alle drie vestigingen Linkworx OK
- # [[2013-03-11]] 13:58 
  Crystal reports registratie
- # [[2013-03-11]] 16:51 
  D3_PM1 erbij gestoken
- # [[2013-03-19]] 13:05 
  Meeting in MHZ
- # [[2013-03-25]]
  D3 extra logging opgezet
- # [[2013-03-26]] 8:42 
  Fout ivm query Bart opgelost
- # [[2013-03-26]] 12:29 
  kWh tellers Dessel 15.1
- # [[2013-04-03]] 10:06 
  Mails Stijn
- # [[2013-04-08]] 11:26 
  Query voor Bart aangepast
  
  <https://sibelco.box.com/s/n99qyrlh05fwtbbzrhpm>
- # [[2013-04-08]] 15:03 
  Test met een nieuwe linkworx versie gedaan.
  
  =\> Versie met 'Manuele Invoer'
- # [[2013-04-19]] 11:52 
  4 tags bijgeconfigueerd. Maar dit wil niet werken.
  
  Gemeld aan Stijn
- # [[2013-04-23]] 11:34 
  Extra tags gelogd voor Bart (MHL)
  
  S_MT2 (vocht) en S_TT2 (temp) compressorkamer op scherm gezet + gelogd
- # [[2013-04-26]] 10:35 
  Aanpassingen voor Bart en MHZ (zie mail)
- # [[2013-05-27]] 9:17 
  Gert Carpentier heeft gevraagd om te wachten tot na installatie nieuwe firewall (2 weken)
- # [[2013-05-27]] 14:44 
  Extra tag in Dessel: BBM_Zakkenteller. Komt goed in webpage, maar komt niet in database.
  
  Mail naar Stijn gestuurd.
- # [[2013-05-27]] 15:47 
  Logging liep niet meer goed sinds 22/05: aangepast.
- # [[2013-05-27]] 16:28 
  Tag BBM_Zakkenteller in orde brengen
  
  Logging loopt
- # [[2013-05-27]] 17:01 
  SELECT DATETIMEFROMPARTS(
  
  Datepart(Year, timestamp),
  
  Datepart(MONTH, timestamp),
  
  Datepart(DAY, timestamp),
  
  Datepart(HOUR, timestamp),
  
  (Datepart(MINUTE, timestamp) % 5)\*5, 0, 0),
  
  Sum(\[BBM_ZakkenTeller_Val\])
  
  FROM \[linkworx\].\[dbo\].\[LNKWRX_DATALOG_TM_0D0H1M0S_DIFFERENCES\]
  
  Where BBM_Zakkenteller_Val is not null
  
  Group by Datepart(Year, timestamp),
  
  Datepart(MONTH, timestamp),
  
  Datepart(DAY, timestamp),
  
  Datepart(HOUR, timestamp),
  
  Datepart(MINUTE, timestamp) % 5
- # [[2013-05-28]] 8:29 
  Rapport aantalzakken bbzand
  
  <https://www.box.com/s/hf9jqobl9sv8c1cro1ox>
- # [[2013-05-29]] 16:14 
  Analyse van de kWh Excel file
  
  [1955_001.pdf](assets/pdf/1955_001.pdf)
- # [[2013-05-30]]
  Testen nieuwe versie Linkworx
- # [[2013-05-31]]
  Voorbereiden manuele ingave Dessel.
- # [[2013-06-03]]
  Export Enprove
  
  Programmatie PACs HSK15.9
- # [[2013-06-04]] 9:11 
  Logging in Linkworx
  
  ![image2](image2%201%201.png)
- # [[2013-06-13]] 10:12 
  Rapport van aantal zakken BB_meel in SQL Server reporting services (SSRS) gemaakt.
- #
- # [[2013-06-21]] 9:39 
  Intranet site opgezet <http://be-des-sql-001/reports>
- # [[2013-06-24]]
  Manuele invoer
- # [[2013-06-25]]
  Manuele invoer
- # [[2013-07-05]] 15:35 
  Export opgezet met Linkworx. Gevraagd aan Enprove of dit OK is
- # [[2013-07-05]] 16:05 
  Backup van Linkworx configs naar BEDESNAS1
- # [[2013-07-08]] 12:26 
  Infrax data naar tabel
  
  <http://be-des-sql-001/Reports/Pages/Report.aspx?ItemPath=%2fMHZ%2fMHZ+Verbruik+Infrax>
- # [[2013-07-12]] 16:51 
  Aanvoer MHZ in Linkworx gezet.
- # [[2013-08-08]] 11:16 
  File export van Linkworx werkt niet (meer). Aan Stijn mail gestuurd
- # [[2013-09-09]] 11:29 
  Mail van Enprove.
  
  Oude gegevens zijn mogelijk slecht.
- # [[2013-09-10]] 13:20 
  Regional settings aangepast voor user LinkworxService. Export lijkt nu wel in orde
- # [[2013-09-13]] 12:31 
  Mail van Enprove ontvangen. Gegevens komen goed binnen.
  
  Aan Mike gevraagd wat er nu moet gebeuren
- # [[2013-09-18]] 15:15 
  Opbouw query Dessel maandrapport
  
  <https://sibelco.box.com/s/ooeqmch0zj83yd04qq46>
- # [[2013-09-25]] 16:36 
  Extra sequentie gegevens voor Mike gelogd
  
  \[M1_SEQ_ALG_Val\]
  
  ,\[M4_SEQ_HOOFD_Val\]
  
  ,\[M6_SEQ_HOOFD_Val\]
  
  ,\[M7_SEQ_HOOFD_Val\]
  
  ,\[M3_SEQ_HOOFD_Val\]
  
  ,\[M2_SEQ_ALG_Val\]
  
  ,\[M5_SEQ_HOOFD_Val\]
  
  ,\[D4_SEQ_ALG_Val\]
  
  ,\[D3_SEQ_ALG_Val\]
  
  ,\[CAL_SEQ_HOOFD_Val\]
- # [[2013-09-30]] 12:15 
  Extra loggings voor zakken installaties
- # [[2013-10-02]] 10:20 
  Extra tags in query klaar gezet en naar Enprove gestuurd.
- # [[2013-10-07]] 16:55 
  Extra tags in productie gezet.
- # [[2013-10-08]] 15:12 
  Extra Pacs geprogrammeerd en in linkworx gezet
- # [[2013-10-11]] 16:48 
  De resultaten van de Queries uit de DIFFERENCE tabellen kloppen niet.
  
  Beslist om zelf regelmatig de SIB_DIFF tabel op te vullen.
  
  Zie query <https://sibelco.box.com/s/pcgbe4ftmwzl8fsdum60>
  
  Dus in de SIB_DIFF tabel een kolom voor ELKE meting maken.
  
  Zowel voor T1M als T5M als Manual_log
  
  Via stored procedure SIB_FILL DIFF_TABLE
- # [[2013-10-16]] 10:03 
  Hoe omgaan met meetfouten?
  
  Dit kan in Linkworx, maar is minder flexibel dan SQL server.
  
  Bij wijziging moet Linkworx altijd worden herstart, met mogelijkheid tot fouten
  
  =\> MEETFOUTEN wegwerken in SQL server, Linkworx alleen gebruiken voor logging.
- # [[2013-10-16]] 10:23 
  Begonnen met een lege tabel. Het inserten van alle (330383) timestamps duurde 1:35u
- # [[2013-10-16]] 15:12 
  Het opvullen van een lege SIB_DIFF met stored procedure SIB_FILL_DIFF_TABLE duurt 5 minuten
- # [[2013-10-17]] 15:50 
  De hele dag gezocht naar hoe een insert trigger altijd uitvoeren.
  
  =\>
  
  ALTER TRIGGER \[dbo\].\[reminder1\]
  
  ON \[linkworx\].\[dbo\].\[LNKWRX_DATALOG_TM_0D0H1M0S\]
  
  AFTER INSERT, UPDATE
  
  AS
  
  SET XACT_ABORT OFF;
  
  EXEC SIB_FILL_DIFF_TABLE
- # [[2014-11-04]] 13:54 
  Extra logging tags toegevoegd van Lus SCR
  
  Ook verder gewerkt aan
  
  <https://sibelco.box.com/s/7jbfj2hlhlsyljnjnilb>
- # [[2014-12-08]] 10:51 
  Het is weer te lang geleden. Waar was ik alweer gebleven?
- # [[2014-03-11]] 16:45 
  Rapport <http://be-des-sql-001/Reports/Pages/Report.aspx?ItemPath=%2fDES%2fMolens%2fDES-M1M2-Herwig>
- # [[2014-12-30]] 7:50 
  Gisteren teller HSE_C1 gereset
  
  Tellerstand actief 20792316 kWh
  
  Tellerstand Reactief 4546325 kVarh
- # [[2015-09-09]] 16:22 
  In de Linkworx_DES_Log DB een SP gemaakt om een goed tijdsinterval te bekomen
  
  Voorbeeld
  
  [Oproepen van een stored procedure](onenote:..\..\..\Personal\Computer\SQL.one#Oproepen%20van%20een%20stored%20procedure&section-id={B72AADD9-3250-4C6D-B6C3-C26901E7E051}&page-id={9638A290-24D8-4340-A203-C9D579640C91}&end&base-path=https://d.docs.live.net/648fe635197c5860/Docs/OneNote's/Persoonlijk%20(web))
- # [[2015-01-08]] 13:36 
  In MHZ geëxperimenteerd met het door linkworx laten opvangen van een teller reset. Maar werkt voorlopig niet
  
  \<instancecode="SibkWh_Test"model="power.measurement.model"\>  
  \<variablecode="totalEnergyConsumption"tag="SIBKWH_TEST"datalog.interval.column="SibkWh_Test"datalog.interval.timespan="\*.\*:1:0"datalog.change.min.absolute.deviation="0.01"\>  
  \<isvalidconditionsource="{new.value}\>{old.value}"/\>  
  \</variable\>  
  \</instance\>
  
  [[2016-05-11]] 16:38
  
  Peter en Stijn hebben gevraag om mijn visie op papier te zetten
  
  Dit zit er al in be-des-sql-001 in de DESSEL_LOG DB
- SELECT TOP 1000 \[timestamp\]
- ```sql
  SELECT timestamp
   ,[M2_1\_PM_Energy\]
   ,[PML02_ItemNo\]
  
  ,\[PML02_Started\]
  
  ,\[PML02_Production_Counter\]
  
  ,\[M1_2\_PM1_Energy\]
  
  ,\[NachtTarief\]
  
  ,\[M1_1\_PM_Energy\]
  
  ,\[PML01_Started\]
  
  ,\[PML01_Production_Counter\]
  
  ,\[HSK15_3\_K2_6\_PM_Energy\]
  
  ,\[PML01_ItemNo\]
  
  FROM \[Linkworx_DES_LOG\].\[dbo\].\[ABB_Datalog_PML01_PML02\]
  
  -- QUERY
  
  ;WITH T1 as
  
  (
  
  SELECT -- Algemeen
  
  \[timestamp\]
  
  ,LAG(timestamp) OVER (ORDER BY timestamp) AS timestamp_prev
  
  ,\[NachtTarief\]
  
  -- Energiemetingen
  
  ,\[M2_1\_PM_Energy\] - LAG(M2_1\_PM_Energy) OVER (ORDER BY timestamp) AS M2_1\_PM_Energy
  
  ,\[M1_2\_PM1_Energy\] - LAG(M1_2\_PM1_Energy) OVER (ORDER BY timestamp) AS M1_2\_PM1_Energy
  
  ,\[M1_1\_PM_Energy\] - LAG(M1_1\_PM_Energy) OVER (ORDER BY timestamp) AS M1_1\_PM_Energy
  
  ,\[HSK15_3\_K2_6\_PM_Energy\] - LAG(HSK15_3\_K2_6\_PM_Energy) OVER (ORDER BY timestamp) AS HSK15_3\_K2_6\_PM_Energy
  
  -- PML01
  
  ,CONVERT(INT, \[PML01_Started\]) AS PML01_Started
  
  ,\[PML01_ItemNo\]
  
  ,\[PML01_Production_Counter\] - LAG(PML01_Production_Counter) OVER (ORDER BY timestamp) AS PML01_Production_Counter
  
  -- PML02
  
  ,CONVERT(INT, \[PML02_Started\]) AS PML02_Started
  
  ,\[PML02_ItemNo\]
  
  ,\[PML02_Production_Counter\] - LAG(PML02_Production_Counter) OVER (ORDER BY timestamp) AS PML02_Production_Counter
  
  FROM \[Linkworx_DES_LOG\].\[dbo\].\[ABB_Datalog_PML01_PML02\]
  
  )
  
  SELECT \*
  
  ,IIF(PML01_Started = 0 AND PML02_Started = 0,
  
  M1_1\_PM_Energy + M1_2\_PM1_Energy / 2,
  
  M1_1\_PM_Energy + (M1_2\_PM1_Energy+HSK15_3\_K2_6\_PM_Energy) \* (PML01_Started / (PML01_Started + PML02_Started))
  
  ) AS PML01_Energy
  
  ,IIF(PML01_Started = 0 AND PML02_Started = 0,
  
  M2_1\_PM_Energy + M1_2\_PM1_Energy / 2,
  
  M2_1\_PM_Energy + (M1_2\_PM1_Energy+HSK15_3\_K2_6\_PM_Energy) \* (PML02_Started / (PML01_Started + PML02_Started))
  
  ) AS PML02_Energy
  
  FROM T1
  ```
- ,\[M2_1\_PM_Energy\]
  
  ,\[PML02_ItemNo\]
  
  ,\[PML02_Started\]
  
  ,\[PML02_Production_Counter\]
  
  ,\[M1_2\_PM1_Energy\]
  
  ,\[NachtTarief\]
  
  ,\[M1_1\_PM_Energy\]
  
  ,\[PML01_Started\]
  
  ,\[PML01_Production_Counter\]
  
  ,\[HSK15_3\_K2_6\_PM_Energy\]
  
  ,\[PML01_ItemNo\]
  
  FROM \[Linkworx_DES_LOG\].\[dbo\].\[ABB_Datalog_PML01_PML02\]
  
  -- QUERY
  
  ;WITH T1 as
  
  (
  
  SELECT -- Algemeen
  
  \[timestamp\]
  
  ,LAG(timestamp) OVER (ORDER BY timestamp) AS timestamp_prev
  
  ,\[NachtTarief\]
  
  -- Energiemetingen
  
  ,\[M2_1\_PM_Energy\] - LAG(M2_1\_PM_Energy) OVER (ORDER BY timestamp) AS M2_1\_PM_Energy
  
  ,\[M1_2\_PM1_Energy\] - LAG(M1_2\_PM1_Energy) OVER (ORDER BY timestamp) AS M1_2\_PM1_Energy
  
  ,\[M1_1\_PM_Energy\] - LAG(M1_1\_PM_Energy) OVER (ORDER BY timestamp) AS M1_1\_PM_Energy
  
  ,\[HSK15_3\_K2_6\_PM_Energy\] - LAG(HSK15_3\_K2_6\_PM_Energy) OVER (ORDER BY timestamp) AS HSK15_3\_K2_6\_PM_Energy
  
  -- PML01
  
  ,CONVERT(INT, \[PML01_Started\]) AS PML01_Started
  
  ,\[PML01_ItemNo\]
  
  ,\[PML01_Production_Counter\] - LAG(PML01_Production_Counter) OVER (ORDER BY timestamp) AS PML01_Production_Counter
  
  -- PML02
  
  ,CONVERT(INT, \[PML02_Started\]) AS PML02_Started
  
  ,\[PML02_ItemNo\]
  
  ,\[PML02_Production_Counter\] - LAG(PML02_Production_Counter) OVER (ORDER BY timestamp) AS PML02_Production_Counter
  
  FROM \[Linkworx_DES_LOG\].\[dbo\].\[ABB_Datalog_PML01_PML02\]
  
  )
  
  SELECT \*
  
  ,IIF(PML01_Started = 0 AND PML02_Started = 0,
  
  M1_1\_PM_Energy + M1_2\_PM1_Energy / 2,
  
  M1_1\_PM_Energy + (M1_2\_PM1_Energy+HSK15_3\_K2_6\_PM_Energy) \* (PML01_Started / (PML01_Started + PML02_Started))
  
  ) AS PML01_Energy
  
  ,IIF(PML01_Started = 0 AND PML02_Started = 0,
  
  M2_1\_PM_Energy + M1_2\_PM1_Energy / 2,
  
  M2_1\_PM_Energy + (M1_2\_PM1_Energy+HSK15_3\_K2_6\_PM_Energy) \* (PML02_Started / (PML01_Started + PML02_Started))
  
  ) AS PML02_Energy
  
  FROM T1
  
  [[2016-05-18]] 11:40
  
  Document gemaakt en met Stijn gedeeld
- # [[2016-07-01]] 09:12 
  Logging van D3 voor KU Leuven opgezet
  
  Te vinden onder [\\\10.32.29.100\c\$\linkworx\linkworx_hist\server_hist - KUL](file://10.32.29.100/c$/linkworx/linkworx_hist/server_hist%20-%20KUL)
  
  Query
  SELECT TOP 200 \*
  FROM \[Linkworx\].\[dbo\].\[LOG_D3_KUL\]
  order by dts desc

- # [[2016-09-12]] 14:04 
  Export van de logging via mail verstuurd.
  
  <https://sibelco-my.sharepoint.com/personal/tonny_lemmens_sibelco_com/Documents/Energy/DES/Drogers>
- # [[2016-12-20]] 8:46 
  Gisteren meeting gehad. NU moet er een energie logging komen.
- # [[2017-02-27]]