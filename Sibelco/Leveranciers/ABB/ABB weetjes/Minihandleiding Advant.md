---
title: Minihandleiding Advant
date created: 0000-11-19T09:22:12+00:17
date modified: 2025-10-20T13:37:56+02:00
---

- # ABB minihandleiding Advant
	- Commando's
	  LTREE -\> list tree
	  ANPER -\> Analyse performer
	  CRDB -\> Create database element
	  DDB -\> Delete database element
	  MDB -\> modify database (aanpassen in de database)
	  m =\> modify
	  
	  ! =\> quit modify
	  
	  end =\> terug naar hoogste niveau
	  GVD -\> get variable dynamic (bekijken van een signaal)
	  C PC -\> connect to programm
	  GEPCD -\> get pc dynamic gepcd d,pc10.1.1.1
	  LV -\> list variable (vb LV =M5_20 -\> toon variabele M5_20)
	  SLTARG -\> select target (kiezen van path in Online Builder)
	  SLLEV -\> select level pc (\* ipv \#)
	  DIMDB -\> dimensioneren / bekijken van de database.
	  DIMPC -\> dimensioneren van programma's.
	  DIM -\> dimdb en dimpc bevestigen met dim commando
	  RECONFIG -\> herconfigureren van de PLC (alles wordt gewist)
	  ECONFIG -\> enable configuration (aanpassen van de configuratie, DIT STOPT HET SYSTEEM)
	  DICONFIG -\> disable configuratie (uit de configuratie modus gaan)
	  CRDB -\> Create database (maak element bij in de database)
	  DDB -\> Delete database (verwijder database element)
	  IS -\> insert statement
	  PCPGM(10,) -\> 10 staat voor doorlooptijd van 10ms
	  GEPD PC1 -\> Generate page division. Voorbereidend werk voor afdrukken.
	  MPD pc1.2.3.4=321.5 -\> Zet bepaald pc op bepaalde bladzijde.
	  SEOM C,P -\> set output medium console, printer (voorbereidng voor printen)
	  LPCD pc1,4\>5 -\> print van pagina 4 tot 5 van pc1
	  LPN -\> list page nummering
	  LDBD -\> list database LDBD SEL=DIC
	  TSESS -\> terminate session
	  EBM PCx-\> enable build mode
	  DIBM -\> disable build mode DIBM PC2 check of alle inputs aangesloten zijn. Na een DIBM altijd een DBL uitvoeren
	  DBL -\> deblock het programma
	  DUAP APPLIK -\> Dump applikatie (geeft een volledige image)
	  (Message: Dump applicatie
	  Van MAM wasserij
	  
	  09 mei 2007
	  
	  Tonny)
	  
	  DUTDB -\> naam db -\> dump total database
	  DUTPT -\> naam pt -\> dump total program
	  Maken van source code voor bewerking in FCB
	  Maak een backup van de productie PLC
	  DUAP APPLIk
	  En op de labo PLC
	  Zie dat de juiste versie in de flash kaart zit en dat de communicatiekaart hetzelfde adres heeft.
	  LOAP APPLIK
	  DUTDB DB (doet een binaire dump van de database.) (plc moet in config mode staan)
	  DUTPT PT (doet een binaire dump van de program tables)
	  Deze commando’s maken een extra backup. Het is mogelijk dat een LOAP APPLIK niet lukt.
	  
	  Maken van de source code
	  DUDBS (dump database source)
	  Generate printer linsting only: No
	  
	  Destination SCDB
	  
	  Selection: ALL
	  
	  (eventueel any options selecteren)
	  .BA bestand wordt aangemaakt
	  
	  DUPCS pc1 /SRCE (dump pc source) dupcs pc1 /srce
	  Ook voor andere pc’s
	  
	  PLC herconfigureren met RECONFIG
	  
	  *LOTDB DB*
	  
	  *Compress database dump: Y*
	  
	  *Redimension: Y*
	  
	  *Vul alle waarden in voor de database*
	  
	  *DIM*
	  
	  *Spare area: 200kb*
	  
	  **
	  
	  *LOTPT PT*
	  
	  *Redimension: Y*
	  
	  *Vul alle waarden in voor de program tables*
	  
	  *DIM*
	  **
	  **
	  **
	  **
	  **
	  In Application builder: File – Convert
	  Converteer de .AA en .BA bestanden naar .AAX en .BAX in vb M:\OnderHd\Electr\Private\proj\DESSEL\NODES\SILOS\SRCE
	  Start FCB
	  Kies File - Backtranslate source
	  In de omzetting van de database kan een fout komen op de LAN’s. Deze moeten verwijderd worden.
	  
	  Pas DB en PC’s aan
	  Maken van binaire code upload in plc
	  Kies: File – Generate Source (SCPT en BUSILO)
	  Sluit FCB
	  In Application Builder: File – Convert
	  Converteer .AAX en .BAX naar .AA en .BA
	  
	  In online builder
	  PLC herconfigureren met RECONFIG
	  
	  DIMDB om de database te dimensioneren
	  DIM om te bevestigen
	  Spare area: 200kB
	  
	  DIMPC
	  Dim
	  
	  TRDBS
	  Segment: SCDB01
	  Translation mode: S(hort)
	  Maak een backup van de database met DUTDB DBx.
	  
	  Alvorens de pc’s in te laden moet voor elke pc het volgende uitgevoerd worden
	  IS PC1
	  
	  PCPGM(20,)
	  
	  !
	  
	  DS PC1
	  **TRPCS**
	  **Of**
	  **TRPCS SRCE:PC121201 voor PC12 -\> Zie SRCE directory**
	  Programmeren
	  SEQ
	  Een sequentie moet onder de root van een programma staan. Niet onder een controle module.
	  vb IS PC3
	  SEQ(250,,0,0,0)
	  Onder een SEQ moet een STEP geplaatst worden.
	  AC110
	  Deze kan je niet programmeren met online builder, enkel met FCB
	  Maak connectie met COM2.
	  \- Target Connect.
	  \- File - Online Mode
	  \- File - OpenSection - PC of DB (of kies de linkse icoontjes).
	  \- Klik op het meter-icoon. =display value.
	  \- Test - Cyclic Display
	  \- Target Disconnect
	  FATAL ERROR
	  Eerste keer opgetreden in kaai na de Advantfieldbus (AF100_1) IMPL op 0 en terug op 1 te zetten.
	  1\. Dump van programma en database: duap applik
	  2\. Plc op stand CLEAR zetten en op INIT drukken.
	  3\. Laden van het programma en de database: loap applik
	  4\. Reset de plc (INIT)
	  Mogelijk helpt dit niet en moeten de programma’s en de database appart gedumpt en geladen worden.
	  1\. Dump programma: dutpt pt
	  2\. Dump database: dutdb db (enkel in configuration mode)
	  ****
	  GEPCD
	  ******
	  lopcs