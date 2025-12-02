---
created: [[2013-01-09]]T15:06:59.0000000+01:00
tags: #LLB 
---

- # [[2012-12-04]] 16:50
	- Vandaag te horen gekregen dat laden schip altijd in noodwerking moet gebeuren.
- # [[2012-12-07]] 11:28
	- Laden schip zit in plc LLB
	  Pc1.20.1 Keuze hand / badge
	  Pc1.20.2 is Keuze MS60, MS61, MS63, MS66, MS67 schip
	  
	  | Bunker | Vrijgave | Noodwerking | Manueel weegbrug |
	  |--------|----------|-------------|------------------|
	  | B60S   | ok       | ok          | ok               |
	  | B61S   | ok       | ok          | ok               |
	  | B63S   | ok       | ok          | ok               |
	  | B66S   | ok       | ok          | ok               |
	  | B67S   | ok       | ok          | ok               |
	  Getest met badge: ok
- # [[journals/older/2013/2013-01-09]] 15:07 
  Project opnieuw aangevat.
  
  Storingenboek: 2012/DES/1042
  
  dinsdag 4 december 2012
  
  15:33
  
  Veel stof dat vrijkomt bij belading bunkers 69 en 61.
  
  Abnormaal veel !!!!
  
  Geert Staes is gaan kijken. Alles werkt
- # [[2013-01-10]] 13:57
	- Verder gewerkt aan project
	  AFZUIGING EN BLOWER VOOR ELKE SEQUENTIE VAN LLB5 AANSLUITEN
- # [[2013-01-11]] 16:12
	- Verder gewerkt aan project.
- # [[2013-01-28]] 10:58 
  Tekenen beeld LLB3 (B1-B8)
- # [[2013-01-28]] 11:09 
  Het was te lang geleden.
  
  Begin terug vanaf LLB0 en afwerken van begin tot einde.
- # [[2013-02-12]] 9:58 
  [Overzicht filters, loskleppen en blowers van LLB](file:///H:/Private/Documenten/Projecten/Ombouw%20PLC%20LLB/Overzicht%20filters,%20loskleppen%20en%20blowers%20van%20LLB.xlsx)
  
  LLB0 gechecked
- # [[2013-02-12]] 16:44 
  Vrij goed kunnen verder werken vandaag
  
  Vervolg excel [Overzicht filters, loskleppen en blowers van LLB](file:///H:/Private/Documenten/Projecten/Ombouw%20PLC%20LLB/Overzicht%20filters,%20loskleppen%20en%20blowers%20van%20LLB.xlsx) voor MS61
- # [[2013-02-13]] 12:15
	- Extra noodstop
	  | DI800_4.8 | LLB6_NS | LLB6 Noodstop scheepsbelading |
	  |-----------|---------|-------------------------------|
- ## PLC LLB
  ![image1](image1-217.png)
  
  Ook LLB5_NST (DI800_2.5) gekoppeld
- ## PLC LLB5
  ![image2](image2-123.png)
- ##
- # [[2013-02-13]] 12:58
	- Excel sheet afgewerkt
- # [[2013-02-13]] 13:24
	- Sequentie [[LLB0]] in Visio tekenen
- # [[2013-02-13]] 14:56 
  Beslist om alle sequenties universeel te maken.
  
  Zie [Overzicht filters, loskleppen en blowers van LLB](file:///H:/Private/Documenten/Projecten/Ombouw%20PLC%20LLB/Overzicht%20filters,%20loskleppen%20en%20blowers%20van%20LLB.xlsx)
- # [[2013-02-13]] 16:35 
  Anomalieën in Excel sheet (laten) uitzoeken
- # [[2013-02-14]] 11:22 
  LLB0 beschreven
- # [[2013-02-14]] 13:11 
  LLB1 t.e.m. LLB4 beschreven
  
  LLB5 en LLB6 nog doen
- # [[2013-02-14]] 16:58 
  LLB0 beeldgetekend
  
  Vervolg met koppelen objecten met sequentie
- # [[2013-02-15]] 12:01 
  Sequentie LLB0 start-stop-noodstop = OK
- # [[2013-02-15]] 16:22 
  Beeld LLB1 getekend (nog niet helemaal af)
  
  =\> Vervolg Sequentie LLB1, blijft al hangen in stap1
- # [[2013-02-18]] 9:36 
  LLB1 OK
- # [[2013-02-19]] 11:21 
  LLB2 -\> LLB4 OK
  
  LLB5 detail nog verder tekenen / uitzoeken
- # [[2013-02-19]] 15:43 
  PLC in labo gezet.
  
  IO beginnen invullen
- # [[2013-02-19]] 16:53 
  IO t.e.m. DO.107 ingevuld
- # [[2013-02-28]] 16:38 
  IO nog wat verder ingevuld
  
  SibBoolIO element gemaakt
- # [[2013-03-04]] 10:56 
  Overlopen oud programma
  
  Aanduiden met groene fluo indien ok
- # [[2013-03-07]] 12:22 
  LLB6 is zo goed mogelijk getest
- # [[2013-03-07]] 14:06 
  LLB5 Lamp knipperen tijdens opstart
  
  Volbranden indien op STT2 mag worden gedrukt
- # [[2013-03-08]] 16:01 
  LLB2 level van B23-\>B26 nog invullen
- # [[2013-03-11]] 13:58 
  Is momenteel zo goed mogelijk in orde. Een paar dagen voor ombouw dossier terug oprakelen.
- # [[2013-05-21]] 13:15 
  Storingenboek B69: Er zou geen afzuiging zijn.
  
  Het volgende getest:
  
  B69 vrijgegeven, afzuiging met de knop aan het kanaal gestart
- # [[2013-06-05]] 13:27 
  Gisteren en vandaag zelfde probleem met B69.
  
  Logging opgezet
  
  ![image3](image3-71.png)
- # [[2013-06-05]] 17:04 
  PLC gepatcht
  
  Voorbereiding ombouw LLB XML bestanden OPC server voorbereid
- # [[2013-06-11]] 7:26 
  Ombouw is goed verlopen.
- # [[2013-06-12]] 10:00 
  Probleem met LLB6_4 (FB tijd stond te kort)
  
  Max. vrijgave tijd voor schepen op 4h gezet.
- # [[2013-07-02]] 11:41 
  De niveaumetingen van de bunkers komen niet juist in het weegbrugprogramma
  
  Klep van B62 gaat traag toe.
- # [[2013-07-02]] 11:51 
  [Klep van B62 gaat traag toe.](onenote:#LLB&section-id={9E0E157C-9179-4382-8032-06FCB36C8B5C}&page-id={D7A5EE5D-E55A-4099-A702-1F8DCA3A7200}&object-id={B4E068B9-C4E5-0DCC-3D26-DDE771925D7C}&13&base-path=H:\Public\Planning%20Tonny\LOGS\DES\Lossen\LLB.one)
  
  Sequentie aangepast en nadraaitijd kleiner gezet
- # [[2013-07-03]] 11:35 
  Blower M500 start niet op bij overtappen 65-\>101, 102
  
  Dit zit in PLC zakscheur
  
  ![image4](image4-44.png)
- # [[2013-07-04]] 14:11 
  Probleem blower M500 LLB_B1 bij overtappen 65-\>101,102 opgeslost
- # [[2013-07-04]] 15:39 
  [De niveaumetingen van de bunkers komen niet juist in het](onenote:#LLB&section-id={9E0E157C-9179-4382-8032-06FCB36C8B5C}&page-id={D7A5EE5D-E55A-4099-A702-1F8DCA3A7200}&object-id={B4E068B9-C4E5-0DCC-3D26-DDE771925D7C}&E&base-path=H:\Public\Planning%20Tonny\LOGS\DES\Lossen\LLB.one) weegbrugprogamma: .xml bestand van Objective tagserver aangepast
- # [[2013-07-11]] 15:16 
  Met Dirk Tubbeckx gebeld. Is moeilijk te testen. Lader los gaat bellen wanneer er een vrachtwagen is.
- # [[2014-01-28]] 11:22 
  Probleem gehad met MAF1. =\> Met had een brug op de MAF1 liggen
- # [[2014-02-11]] 8:35 
  LLB5_MS64LB geblokkeerd op vraag van zjeeke
- # [[2014-02-05]] 10:27 
  Nieuwe klep LLB5_SVA910
  
  <https://www.box.com/shared/p42d6u4rsqkpem56qs33>
- # [[2014-02-25]] 10:38 
  Mail naar mechanische dienst gestuurd om dit na de kijken.
- # [[2014-03-18]] 9:11 
  Mail van Mike
  
  Beste.
  
  Deze laadbalg heeft geen sluitconus .
  
  Geert Staes is met de leverancier bezig om de laadbalg aan te passen
  
  vriendelijke groeten
- # [[2014-03-06]] 16:47 
  Mail naar Mike en Rocco gestuurd
- # [[2014-10-21]] 10:00 
  Op vraag van Luc Gijbels laden uit MS21 aangepast.
  
  De vijs grijpt rechtstreek in de Silo, achter de vijs staat er nog een klep.
- # [[2015-02-02]] 11:48 
  Met testbadge voor schip getest.
  
  Geen probleem
- # [[2015-04-07]] 11:09 
  Voor sequentie CMT_LossenMeelsilo (BU52/BU53) is geprogrammeerd dat eerst de losklep open gaat en vervolgens de beluchting.
  
  Voor LLB6 schip zou lamp blijven knipperen. =\> Getest het nadraaien van de afzuiging duurt 1,5 minuut
  
  Tijdens het verhalen moet de afzuigklep open blijven. Getest: dit is zo.
- # [[2016-02-09]] 09:25 
  LLB5_MS65 in de sequentie LLB_MS65.Seq_lossen parameter Afzuigverlengtijd van 30s naar 5s gezet.
- # [[2017-03-30]] 
  Problemen met LLB6_4
  
  Zie [Aanpassing Laden Schip](https://sibelco.sharepoint.com/teams/Team_PlantDessel_Dessel_MiningandProcessingOperations_ProjectandTechnicalServices/_layouts/15/guestaccess.aspx?guestaccesstoken=4g7USmAk1JIopTA9fs7tlkgqw3IzMkaOmkAErnCRSoc%3d&docid=2_19683eeedac434aad8570f7700da2a484&rev=1)
  
  Parameter Drive parameter 2101 scalair fly start heeft het opgelost
- # [[2022-11-07]] 
  LLB6 aangepast de HN-detectie bediend nu ook de Off-sequentie
  
  Stap 6 en 7 omgewisseld in sequentie