---
title: Koppeling Wind – PV - Sibelco
updated: [[2020-06-16]]T09:02:08.0000000+02:00
created: [[2019-10-25]]T08:54:50.0000000+02:00
---

> Koppeling Wind – PV - Sibelco
vrijdag 25 oktober 2019
8:54

- # [[2019-09-05]]
- # 
  [Studie Sibelco versie 5092019.pdf](https://sibelco-my.sharepoint.com/:b:/p/tonny_lemmens/EXWdeGc27CFLofbHN-mOTDABaAMmkdbZBCu3GIhiF3_OzQ)
  
  [Verdeelsleutel P en Q - versie 5092019.xlsx](https://sibelco-my.sharepoint.com/:x:/p/tonny_lemmens/EaaV7K86PmdHvsI6yD7btHMBuQl61hh8f_a16Vj6ElMSzA)
  
  ![image1](image1-94.png)
- # [[2019-10-25]] 
  Eind 2020 moet de koppeling floating in werking zijn.
  
  Gisteren meeting gehad
  
  [[[2019-10-24]] Verslag Teams meeting.doc](https://sibelco-my.sharepoint.com/:w:/p/tonny_lemmens/EbmVoiehG81BjuQXV5kfEI0BQMJuyHfiRkEViTiNwQXlDw)
  
  ![image2](image2-55.png)
  
  Sibelco doet de metingen cos phi en moet de regeling uitsturen richting windmolen en PV
  Setpoint voor reactief/spannings niveau.
- # Berekeningen / formules
  ![image3](image3-32.png)
  
  ![image4](image4-19%201.png)
- # Metingen Sentron PAC
  Met de Sentron PAC 3200 kan geen Cos Phi worden gemeten.
  
  ![image5](image5-14%201.png)
- # [[2019-10-27]]
  Mail van Harry
  **From:** Harry Stienen \<Harry.Stienen@sibelco.com\>
  **Sent:** zondag 27 oktober 2019 21:56
  **To:** Tonny Lemmens \<Tonny.Lemmens@sibelco.com\>
  **Subject:** Aan de data..man....
  
  Tonny,
  
  Onderstaande passage…
  
  **Meting** :
  
  Het opleggen van reactief vermogen kan impact hebben op de globale productie van het PV project. Floating PV wenst hiervan inschatting te krijgen. Zowel EDF als Sibelco hebben historische data waar actief – reactief vermogen is gelogd alsook de set-points. Op basis van de combinatie van beide data, zou een simulatie kunnen gemaakt worden van wat de eventuele impact op PV-productje kan betekenen. De al dan niet gelijktijdigheid van producties van WT en PV zijn ook variabelen zullen voor onzekerheden in de schatting zorgen.
  
  ENGIE Fabricom verzamelt informatie van EDF en Sibelco en maakt eerste opzet van analyse.
  
  Wetende dat:
- Onze Kvar is gekend in de tijd voor 23 december2017 toen de windmolens nog niet actief waren.
- Je hebt een absorptie profiel gemaakt voor het FPV op basis van het bestaande pv park. Alleen dit moet ook gekompenseerd worden
- We weten de huidige levering van de windmolens 2018.
  **
  Zou je eens een poging willen wagen om het Kvar te bepalen van het FPV.?
  Zie ook de uitleg die we eens gehad hebben van ATS.
  Kunnen we na mijn verlof eens zien waar we tegen aan lopen.
  
  [[[2019-10-24]] Verslag Teams meeting.doc](https://sibelco-my.sharepoint.com/:w:/p/tonny_lemmens/ESDfz-VEOnRPvaDJ56O83BUBVfjoBIoHARkXFd9P-mVfpg)
  
  ![image2](image2-55.png)
- # [[2019-11-04]] 
  Cos phi wordt nu in plc berekend adv actief en reactief vermogen
  
  Aan Peter Drees gevraagd wat eventueel het standaard energie beheer systeem is.
  
  Siemens Energy manager Pro verder getest
  Tags moeten worden ingegeven als : ns=2;s=….
- # [[2019-11-07]] 
  Peter Drees gaat Energy Manager Pro voorleggen aan Jan Janssen. Maar kan enkele maanden duren.
- # [[2019-11-13]] 
  [Studiedocument.pdf](https://sibelco-my.sharepoint.com/:b:/p/tonny_lemmens/EdVDjwYfiZxHjFTwf-CmAF0BZoHeo2pRZr-rN6lOSgDVTg)
- # [[2019-12-11]]
  Van Roel Vloebergs
  [Sibelco Regelschema Cos phi regeling.pdf](Sibelco_Regelschema_Cos_phi_regeling.pdf)
  
  [20191008 WindProject Dessel Sibelco_reactif power.pptx](assets/resources/20191008_WindProject_Dessel_Sibelco_reactif_power.pptx)
- # [[2020-03-30]]
  [Cos phi management Sibelco FPV en EDFwind.docx](assets/resources/Cos_phi_management_Sibelco_FPV_en_EDFwind.docx)
- #
- # [[2020-04-03]]
  **From:** olaf.rabaey@engie.com \<olaf.rabaey@engie.com\>
  **Sent:** vrijdag 3 april 2020 14:44
  **To:** Tonny Lemmens \<Tonny.Lemmens@sibelco.com\>
  **Cc:** nicolas.greant@external.engie.com; Harry Stienen \<Harry.Stienen@sibelco.com\>
  **Subject:** RE: FPV Sibelco Dessel: Q-regeling?
  
  Hallo Tonny,
  
  Volgende afspraken hebben we telefonisch gemaakt omtrent de communicatie voor het zonnepark.
  
  1.  Modbus TCP/IP
  2.  PLC (zonnepark) is de master. (dwz dat deze PLC het initiatief neemt op de communicatie)
  3.  Volgende registers worden uitgelezen bij Sibelco
    1.  Register 1000: UINT16: Setpoint P in procent tov maximaal vermogen
    1.  1000 = 100% van max kWp
    2.  975 = 97.5% van max kWp 
    3.  0 = 0% = uitgeschakeld
        1.  Register 1002: INT16: Setpoint Q in procent tov maximaal reactief vermogen
    1.  0 = 0% =\> zuiver actief vermogen (cos phi = 1)
    2.  50 = 5% van max Reactief vermogen (inductief)
    3.  -50 = -5% van max Reactief vermogen (capacitief)
  1.  Volgende registers worden weggeschreven bij Sibelco
    1.  Register 2000: INT16: Actueel P (kW)
    2.  Register 2002: INT16: Actueel Q (kVAR)
    3.  Register 2004: INT16: Stroom Fase 1 (A)
    4.  Register 2006: INT16: Stroom Fase 2 (A)
    5.  Register 2008: INT16: Stroom Fase 3 (A)
    6.  Register 2010: INT16: Spanning Fase 1 (A)
    7.  Register 2012: INT16: Spanning Fase 2 (A)
    8.  Register 2014: INT16: Spanning Fase 3 (A)
    9.  Register 2016: INT32: Energie geproduceert (kWh)
  1.  Bij onderbreking van de communicatie werkt de installatie autonoom.
  Hierbij wordt een vaste cos phi gehanteerd (door de klant vast te leggen)
  
  Laat maar weten of er opmerkingen zijn.
  
  Mvg,
  **Olaf RABAEY**
  Master Project Engineer - Controls
  Industry North
  Process Solutions
  [olaf.rabaey@engie.com](mailto:%20olaf.rabaey@engie.com)
  P +32 51 25 92 18
  M +32 476 96 76 10
- # [[2020-05-11]]
  **From:** Harry Stienen \<<Harry.Stienen@sibelco.com>\>
  **Sent:** maandag 11 mei 2020 18:10
  **To:** GRÉANT Nicolas (ENGIE Benelux) \<<nicolas.greant@external.engie.com>\>
  **Cc:** Vloebergs, Roel \<<Roel.Vloebergs@luminus.be>\>; Tonny Lemmens \<<Tonny.Lemmens@sibelco.com>\>; Jan Vreys \<<Jan.Vreys@sibelco.com>\>
  **Subject:** Cos-phi bepaling Sibelco i.c.m. FPV en WM
  
  Nicolas,
  
  De mogelijkheid van Q-by night vereenvoudigd de zaken wat.
  Ik dien alleen nog wat feedback te krijgen van Roel Vloebergs over de mogelijkheden van de Siemens software.
  Er is nu wel een parameter bijgekomen zijnde Q <sub>pos_FPW</sub> en Q <sub>pos_WM</sub> hiermee dienen jullie aan te geven wat er aan Q vermogen beschikbaar is. Enfin bekijk de nieuwe draft maar eens en de excel daar heb ik wat simulaties in gedaan om mijn berekening te controleren.
  
  Groet,
  
  Harry Stienen
- # [[2020-05-28]]
  [Werkblad cos-phi.xlsx](assets/resources/Werkblad_cos-phi.xlsx)
  
  \<\<Cos phi management Sibelco FPV en EDFwind \_V3.docx\>\>
  
  **From:** nicolas.greant@external.engie.com \<nicolas.greant@external.engie.com\>
  **Sent:** donderdag 28 mei 2020 11:32
  **To:** Harry Stienen \<Harry.Stienen@sibelco.com\>
  **Cc:** Korneel.Vermeyen@luminus.be; Roel.Vloebergs@luminus.be; Tonny Lemmens \<Tonny.Lemmens@sibelco.com\>; Jan Vreys \<Jan.Vreys@sibelco.com\>; l.driesen@lrm.be
  **Subject:** RE: Cos-phi bepaling Sibelco i.c.m. FPV en WM
  
  Hey Harry,
  
  Korneel zegt me dat je alle info ontvangen zou hebben van Roel.
  Klopt dat ook voor deze puntjes:
- Q <sub>pos_WM</sub> = Max waarden nog te verkrijgen van EDF-Luminus Roel Vloebergs
- P<sub>act_WM</sub> \> ? Nog te bepalen door Roel Vloebergs
  
  Ik zou bij “V3” op p.2 nog toevoegen: er wordt beslist om in het standaard scenario de nodige Q_FPV en/of Q_Wind te regelen om de huidige cos phi = 0.97 aan injectiepunt te respecteren cf. “Bepaling setpunt cos-ⱷ van Snet” op p8/13.
  P. 4/13 en p.8/13 : conclusie van de laatste meeting was om de huidige cos phi regeling aan te houden; vandaag wordt er geregeld op cos phi = 0.97 ipv 0,995. Dus er wordt alleen Q_wind of Q_FPV geleverd indien die cos phi = 0.97 verslechtert toch?
  
  Mvg,
  
  **Nicolas GRÉANT**
- # [[2020-06-02]]
  **From:** Harry Stienen \<Harry.Stienen@sibelco.com\>
  **Sent:** dinsdag 2 juni 2020 13:20
  **To:** nicolas.greant@external.engie.com
  **Cc:** Korneel.Vermeyen@luminus.be; Roel.Vloebergs@luminus.be; Tonny Lemmens \<Tonny.Lemmens@sibelco.com\>; Jan Vreys \<Jan.Vreys@sibelco.com\>; l.driesen@lrm.be
  **Subject:** RE: Cos-phi bepaling Sibelco i.c.m. FPV en WM
  
  Beste,
  
  Eerste deel van de mail is al door Roel Vloebergs beantwoord..
  
  Voor wat betreft:
  P. 4/13 en p.8/13 : conclusie van de laatste meeting was om de huidige cos phi regeling aan te houden; vandaag wordt er geregeld op cos phi = 0.97 ipv 0,995. Dus er wordt alleen Q_wind of Q_FPV geleverd indien die cos phi = 0.97 verslechtert toch?
  Vandaag is er inderdaad geregeld op 0,97 dat is echter niet zoals gesteld in de netstudie, we krijgen er echter geen opmerkingen dus laten we het zo staan.
  Dezelfde strategie gaan we aanhouden vermits we geen opmerkingen krijgen anders gaan we alsnog moeten finetunen.
  
  Sibelco zelf stelt een bewaking in op haar eigen reactief vermogen deel, om onnodige compensatie door derden te voorkomen.
  Mocht dus niemand injecteren hoeft er ook niks gecompenseerd te worden.
  Ik zal versie 3 nog een beetje verfijnen aan de hand van je mail.
  
  Groet,
  
  Harry Stienen