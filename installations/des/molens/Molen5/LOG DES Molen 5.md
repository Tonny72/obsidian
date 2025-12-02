---
date created: 0000-01-09T13:21:30+00:17
tags:
  - M5
links:
  - "[[installations/des/molens/Molen5/Molen 5|M5]]"
date modified: 2025-09-19T14:44:16+02:00
---

- # [[2013-01-17]]
  Mail van Bart
  [Tonny Lemmens - Fw: Voorstel lijst meetpunten Molen 5 - versie 11012012](Notes://BEDESNTS1/C12566FD00314CF5/38D46BF5E8F08834852564B500129B2C/0FE903E649BBA05CC1257AF6004B4D57)
- # [[2013-01-18]] 8:50 
  Vanaf 28 jan worden de metingen van [[installations/des/molens/Molen5/Molen 5]] uitgevoerd. Volgens de planning van [[persons/Mike Van de Put 1]] moet ik 4 feb. in actie schieten
- # [[2013-01-23]] 9:34 
  File afgewerkt 
  \<[file://M:\OnderHd\Elektrische dienst\Public\Automation\Dessel\Molen 5\Meetpunten Molen5.xlsx](file:///M:/OnderHd/Elektrische%20dienst/Public/Automation/Dessel/Molen%205/Meetpunten%20Molen5.xlsx)\>
- # [[2013-01-30]] 12:13 
  Meeting met Disgasys.
  Alle metingen om de seconde loggen.
- # [[2013-01-30]] 16:14 
  Nieuwe Excel-sheet afgerond
  
  (staat op desktop van EngClient1)
- # [[2013-01-31]] 10:28 
  Aanpassen van M5_ST30_L en M5_ST30_R
  
  |          | **Oud**      | **Nieuw** |
  |-----------|--------------|-----------|
  | M5_ST30_L | 0-1000tr/min | 0-500kW   |
  | M5_ST30_R | 0-1000tr/min | 0-500kW   |
  Niet vergeten metingen terug omzetten naar originele waarden.
  
  =\> Dit moet niet volgens Geert Staes
- # [[2013-02-01]] 13:43 
  Gestart om 13.00u. Metingen komen goed binnen in excel
- # [[2013-02-01]] 16:03 
  Metingen goed verlopen. Excel op usb stick van digasys gezet
- # [[journals/older/2013/2013-02-08]]
  Gisteren aan Mike gevraagd.
  
  Digasys heeft alle metingen die ze moeten hebben.
- # [[journals/older/2013/2013-02-08]] 9:41 
  Todo afgesloten
- # [[2013-03-12]] 15:00 
  Objecten aangemaakt
- # [[2013-03-12]] 16:49 
  Beelden tekenen
- # [[2013-03-13]]
  Beelden tekenen
- # [[2013-03-14]] 14:12 
  Beelden tekenen
- # [[2013-03-15]] 16:18 
  Communicatie tussen advant en AC800M
- # [[2013-03-20]] 14:48 
  Beslist om volledig nieuw programma in AC800M te steken
- # [[2013-03-21]] 16:52 
  [Nieuwe objecten M5 ASP-800](onenote:#Nieuwe%20objecten%20M5%20ASP-800&section-id={3F60D0C4-1F99-4A13-B691-FF9A31D292D6}&page-id={84C12A6D-44C2-41F6-908D-03A06D83D820}&end&base-path=H:\Public\Planning\Tonny%20Planning\TODO's.one) verder aangevuld
  
  IO, Par en Lege secties aangemaakt
- # [[2013-03-26]] 12:36 
  Vanwege geheugen problemen niet volledig opnieuw programmeren
- # [[2013-03-26]] 15:12 
  Crash van PLC
  
  Niet gebruikte units eruit gooien
  
  ![image1](image1-9%201.png)
- ## Dit uit M5_IO_DT verwijderd
  S100M5_S100_IOretain
  
  S200M5_S200_IOretain
  
  S300M5_S300_IOretain
  
  S500M5_S500_IOretain
  
  S600M5_S600_IOretain
  
  S900M5_S900_IOretain
- ## Dit uit Par_M5 (datatype) verwijderd
  S100M5_S100_Parretain
  
  S200M5_S200_Parretain
  
  S300M5_S300_Parretain
  
  S500M5_S500_Parretain
  
  S600M5_S600_Parretain
  
  S900M5_S900_Parretain
- # [[2013-03-27]] 16:38 
  Advant programma aangepast tot pc11.6.9
- # [[2013-03-28]]
  Advant programma verder aangepast. (nog nakijken)
- # [[2013-03-29]] 15:57 
  Geprogrammeerd tot de samplers
- # [[2013-04-04]] 14:57 
  Sequentie verder met Ronny Hoeben besproken
- # [[2013-04-04]] 16:47 
  Visio aangepast
  
  [M:\OnderHd\Elektrische dienst\Public\Automation\Dessel\Molen 5\Sequenties\Sequentie M5 Hoofdsequentie TEST.vsdx](file:///M:/OnderHd/Elektrische%20dienst/Public/Automation/Dessel/Molen%205/Sequenties/Sequentie%20M5%20Hoofdsequentie%20TEST.vsdx)
- # [[2013-04-08]] 16:33 
  Visio een beetje verder gewerkt
- # [[2013-04-10]] 17:01 
  Visio een beetje verder gewerkt
- # [[2013-04-11]] 14:04 
  In de hoop dat de sequentie (bijna) correct is, toch al deels geprogrammeerd.
- # [[2013-04-18]] 16:46 
  Programmatie Sequentie
- # [[2013-04-19]] 11:51 
  Programmatie sequentie
- # [[2013-04-22]] 14:42 
  Vergrendelingen geprogrammeerd.
- # [[2013-04-30]] 12:13 
  IO testen uitgevoerd
- # [[2013-05-21]] 13:12 
  SFC knop bijgemaakt
  
  Keuze geldig bij hoofsequentie bijgemaakt
  
  Spoel, sample en cyclustijd op scherm gezet
- # [[2013-05-27]] 8:59 
  MS503 bij op het scherm M5 boven geplaatst
- # [[2013-06-25]] 11:59 
  Opzetten logging Disgasys (had deze per ongeluk verwijderd)
- # [[2013-06-26]]
  Herprogrammatie sequentie.
- # [[2013-07-02]] 16:32 
  Bespreking sequentie M5
- # [[2013-07-04]] 10:23 
  Sequentie bijgewerkt
  
  <https://www.box.com/s/zo2b99h77iwuahn9nilt>
- # [[2013-07-08]] 13:35 
  M5_60 hernoemen naar M5_50
  
  Deze is nog fout in Advant.
  
  Op scherm al OK
  
  =\> Ga dit niet meer doen. Uitgesteld tot ombouw Molen5
- # [[2013-07-08]] 17:14 
  Opkuisen oude Advant code die nodig was voor LLB.
  
  (nog veel werk)
  
  Gebleven bij R_LLB5.B1:value
- # [[2013-07-11]] 14:28 
  Storingenboek: Extra vergrendeling op M5_33
  
  M5_30 als vergrendeling op M5_33 geprogrammeerd
- # [[2013-07-12]] 14:15 
  Opkuis oude avant code tbv LLB
- # [[2013-08-06]] 16:14 
  Testen seq. Molen 5 =\> Moeten stoppen vanwege elektrisch probleem.
  
  Test blad gemaakt voor operatoren en dit aan Geert Smeyers uitgelegd.
- # [[2013-08-07]] 10:53 
  Spanning weggeweest M4 M5
- # [[2013-09-23]] 12:47 
  Extra klep M5SVA433
  
  <https://sibelco.box.com/s/esw121ozxr7udih67q0y>
- # [[2014-01-17]] 16:26 
  Begonnen met M5 in nieuwe PLC.
- # [[2014-02-05]] 16:48 
  Documentatie en programma verder aangepast
- # [[2014-02-07]] 15:03 
  Temperatuur metingen Motor getest met Joris
- # [[2014-02-12]] 10:54 
  M5_MI101BR_WS (werkschakelaar rem) toegevoegd
- # [[2014-02-12]] 13:01 
  Tijdsvertraging op vergrendelingen van M5_4 geprogrammeerd
- # [[2014-02-13]] 16:49 
  Blower airlift begonen aan documentatie data sheets
  
  <https://sibelco.box.com/s/wrk5tpuwwapydo0h30ee>
- # [[2014-02-18]] 12:11 
  Alles afgewerkt van M5_29 en M5_29FA1
  
  [Data sheet Instumentatie](https://sibelco.box.com/s/wrk5tpuwwapydo0h30ee)
  
  [Data sheet motoren](https://sibelco.box.com/s/urz9thfkidyrz4jwob52)
  
  [Doc aanpassing M5_29](https://sibelco.box.com/s/nxk1uhzm1a80e64tuftf)
- # [[2014-03-11]] 9:04 
  Storing Seq. En M5_15 vergrendelingen.
  
  Dump pc11 gestart
- # [[2014-03-11]] 13:03 
  M5_15 in AC800m geprogrammeerd
- # [[journals/2014-03-28]] 15:41 
  Hoofdsequentie aangepast (MAF_2 start niet bij ASP)
  
  M5_5 en M5_6 van Advant naar AC800M gezet
- # [[2015-01-08]] 10:47 
  Drukregeling op filter M5 geprogrammeerd
  
  PT503 -\> M5_PIC901 -\> Snelheid v. M5_1
  
  <https://sibelco.box.com/s/o52f7jbjduxewp0qxs3f>
	- # [[2015-01-29]] 9:19
		- Klep [[installations/des/molens/Molen5/M5_SVA603]] voorbereid in programmatie
		  
		  DO = 0.11.204.16
		  
		  EKO = 0.11.106.1
		  
		  EKT = 0.11.106.2
- # [[2015-02-04]] 9:53 
  Wim Peeters heeft deze klep M5_SVA603 getest en is OK
- # [[2016-05-17]] 15:44 
  Nieuwe test met M5_56 (keienband) geprogrammeerd.
- # [[2016-06-09]] 15:25 
  M5_29 H2 limiet op 105A gezet
- # [[2016-06-14]] 08:27 
  Drive keienband M5_56 er terug af gehaald. Test niet gelukt. Band slipte.
- # [[2016-06-14]] 09:34 
  HoofdSequentie M5 aangepast ivm Probleem wisselklep BU64 BU65 BU101 BU102
- # [[2016-06-14]] 09:36 
  Alarmen verwijderd van Advant DI's M5_56_R\_DI, M5_56_R\_DI, M5_57_DI
- # [[2016-06-20]] 16:09 
  Vergrendeling M5_29 aanpast. Grenswaarde M5_PT162 van 450 naar 460mbar gezet
  
  ![image2](image2-5%201.png)
- # [[2016-10-10]] 15:37
  Testen van werkschakelaars
  
  M5_20
  
  M5_04
  
  M5_28
- # [[2017-02-16]] 
  [Aanpassing Hoofdsequentie M5](https://sibelco.sharepoint.com/teams/Team_PlantDessel_Dessel_MiningandProcessingOperations_ProjectandTechnicalServices/_layouts/15/guestaccess.aspx?guestaccesstoken=uM4qpNZNDhQ1AhOBfWjNxTExkvvLoodhtpPMi2jSTPk=&docid=2_06cd67e903b944093a955fcbfd7b6ccb2&rev=1)
- # [[2017-04-27]] 
  M5_PT162 van 455 naar 460 aangepast. 455 was de waarde in het Advant programma. Dit zal niet mee overnomen zijn naar AC800M
- # [[2017-08-31]] 
  Extra signalen op scherm noodstoppen gezet
  
  ![image3](image3-3%201.png)
- # [[2017-10-10]] 
  In de hoofdsequentie Stap199 toegevoegd. M5SVA431 of M5SVA432 moet open zijn.
- # [[2018-09-06]] 
  Drive M5_MI101 (hoofdmotor): max. toerental gewijzigd van 1000 naar 1100 rpm.
- #