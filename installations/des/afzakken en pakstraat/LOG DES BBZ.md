---
title: LOG DES BBZ
updated: [[2023-02-01]]T08:29:46.0000000+01:00
created: [[2013-01-24]]T10:37:46.0000000+01:00
---

- # [[2012-12-04]] 
  Paneel geeft Fout geen leegweging. De losklep gaat nog wel maar de lift gaat niet boven.
  
  Bij het legen staat op het panel
  
  Aanvoer: 23
  
  BB vuller: 51
  
  Afvoer: 9
  
  Weeg in leeg: DI 1.2.4.13
- ### In panel software:
  Alarm tekst BB: "BB-weging = gn leegmeldig"
  
  Is gekoppeld met Signal:00514 I/O Intlk_345
  
  ![image1](image1-5%201.png)
  
  Als de sequentie in stap51 is en Weeg_in_leeg=0, dan loopt een timer. Na het aflopen van de timer wordt Intlk_345=1. Intlk_345 geeft het alarm 'gn leegmelding'
  
  Mogelijk blijft de sequentie net iets te lang in stap51 staan.
  
  Timer: T_intlk345 gewijzigd van 30s naar 35s
  
  Om van stap51 naar stap52 te gaan is volgende voorwaarde
  
  ![image2](image2-2%201.png)
  
  Mogelijk is de lezer BB_aanwezig (DI .1.2.3.8) slecht.
  
  Mogelijk komt M10 niet op 1 of Einde_Weging_stoppuls_p niet op 1
  
  Veel mogelijkheden dus.
  
  Trending (+ history log) aangemaakt onder: Control Structure - Root - Control Network - Sibelco_Dessel - Applications - Bibbag_Zand - Programs - Program2.
  
  ![image3](image3%201%201.png)
  
  Kwestie van trend op te volgen indien er nog eens een probleem is.
- #
- # [[2012-12-04]] 16:47 
  Mail naar Geert Staes gestuurd. Even afwachten.
- # [[2012-12-06]] 9:59 
  Gisteren verlof gehad.
  
  Is 3x voorgevallen.
  
  =\> Alarm geprogrammeerd op Intl_345
  
  ![image4](image4%201%201.png)
- # [[2012-12-10]] 16:20 
  Geen alarmen voorgekomen
- # [[2012-12-12]] 13:52 
  Voorgekomen op [[2012-12-12]] 7u08m47s
  
  [12-12-2012 13-52-28.jpg](12-12-2012_13-52-28.jpg)
  
  ![image5](image5%201%201.png)
- # [[journals/older/2013/2013-01-07]] 9:02 
  Joris heeft vandaag gemeld dat dit nog voorkomt.
  
  Dit is niet te zien in Trend en niet in Event List.
  
  ![image6](image6%201%201.png)
- #
- # [[journals/older/2013/2013-01-07]] 9:21 
  Peter Smeyers heeft dit zojuist ook nog eens gemeld.
- # [[journals/older/2013/2013-01-07]] 9:36 
  Mogelijk een oorzaak gevonden.
  
  BB_aanwezig eerst eens laten nakijken. Mogelijk flikkert die hard
- # [[2013-01-24]] 10:38 
  Via mail
  
  Collega's,
  
  Ben juist ter plaatse gaan kijken. Blijkt dat rollenbaan 5+6 (soms) niet draait. Dit gebeurt zowel in manuele als automatische mode.
  
  De uitgang van de plc komt niet hoog.
  
  Onze afzakkers bedienen de installatie op een correcte manier!
  
  Graag nakijken waarom uitgang niet hoog komt?
  
  Mvg
  
  Geert Staes
- # [[2013-01-24]] 10:45 
  ![image7](image7%201%201.png)
- # [[2013-01-24]] 14:03 
  Niet meer te simuleren
- # [[2013-05-22]] 14:08 
  Probleem met lift: extra logging opgezet.
  
  Extra logging
- # [[2013-05-22]] 17:04 
  Extra zakkenteller aangemaakt. En linkworx logging opgezet. Maar komt niet in database
  
  Waarom komt zakkenteller niet in linkworx database
- # [[2013-05-27]] 9:03 
  Probleem Bbzand is opgelost. Joris heeft parameters in drive aangepast.
- # [[2013-07-04]] 15:49 
  Probleem gemeld door Peter Drees
- # [[2013-07-04]] 18:47 
  Probleem opgelost: kapotte sensor
- # [[2013-07-05]] 10:20 
  Storingzoeken BB zand
  
  <https://www.box.com/s/ionf7uevhqfezt4a6piy>
- # [[2014-09-30]] 16:31 
  Extra Merkers op teller geprogrammeerd in Program2.Debug
  
  [[2016-04-18]] 14:58
  
  Programma blijft hangen in stap51
  
  Mogelijk hetzelfde probleem als december 2012. =\> Toen was het BB_aanwezig
  
  [[2016-04-20]] 16:53
  
  In programma BB_vuller – Lijn50 – Staat ‘Einde_weging_auto’ = 1
  
  Deze wordt nergens op 1 gezet, niet in plc, en niet in paneel (of ik kan het niet vinden)
  
  Dit zorgde ervoor daar het zaakje uitviel
- # [[2016-08-25]] 15:12 
  PP874 Toevoer BBZ FFS (10.32.29.151) gekoppeld
- #
- # [[2016-10-10]] 11:10 
  AF5_12 startte niet mee op bij het starten van de sequentie toevoer BBZ en FFS.
  
  Dit kwam omdat de vergrendeling (AF5_2 moet draaien) actief was op moment van starten.
  
  =\> Startvoorwaarde aangepast
  
  ![image8](image8%201%201.png)
- # [[2018-04-10]] 
  mail verstuurd
  
  Als de rollenbaan volledig vol staat en men laat de volgende bigbag vertrekken kan het zijn dat er niks vertrekt.
  
  Er komt ook een alarm op het scherm: "BB: gn pall op 1/pos1, gn op BB"
  
  Dit is signal 00541, Intlk_366
  
  Timer op Alarmen_BB, lijn0204 van 20s gewijzigd naar 50s
- # [[2018-05-07]] 
  <u>Veel voorkomende alarmen:</u>
  
  **Gn pall op1/pos1, gn op bb:** 
  
  Dit alarm wordt actief als de seq. BBvuller in stap 66 of stap stap 67 staat, en BB_pallet1 is actief en BB_pallet2 is actief en er is geen pallet op positie1.
  
  Dit heeft waarschijnlijk te maken dat Afvoer-sequentie te lang in stap 81 staat, en dit komt mogelijk doordat er iets met de label-printer afhandeling is.
  
  Ik heb de time-out van dit alarm van 50sec verhoogd naar 5 minuten. Zodat, indien er iets met de printer is, er genoeg tijd is om dit op te lossen voordat er een alarm komt.
  
  **pall detectie op 2 & nt op 1:**
  
  Dit alarm wordt actief als de seq. BBvuller in stap 53 is, en BB_pallet2 is actief en BB_pallet1 is NIET actief.
  
  Waarschijnlijk ligt de pallet niet goed onder de vuller, of moet de sensor worden bijgesteld.
  
  <u>Bigbag wordt niet gevuld.</u>
  
  Een paar keer op een paar dagen tijd bleef de sequentie hangen en werd de BB niet gevuld.
  
  Dit had te maken met de sensor ‘Kruisassen niet gedraaid’ ofwel dat de haken niet helemaal in positie staan.
  
  Wim Peeters heeft deze sensor bijgeregeld.
  
  <u>Sequentie</u>
  
  Ik heb de sequentie in een visio gegoten, zodat mee kan gevolgd worden wat er gebeurd.
  
  [Link Sequentie BBZ](https://sibelco.sharepoint.com/:u:/t/Team_PlantDessel_Dessel_MiningandProcessingOperations_ProjectandTechnicalServices/EZwCVKY009FNjKtFu8OVWcwBKVF-dqnPdUIoWw0mdH6aYg?e=1KqnWd)
  
  Mvg
- # [[2018-09-03]] 
  Rollenbaan 5-6 start soms ongewenst.
  
  Heeft te maken met afname van paletten.
  
  Timer T_M91 aangepast
  
  ![image9](image9%201%201.png)
- # [[2021-07-27]] 
  In simulatie werkt het nieuwe programma.
  
  Todo next: Wanneer men draait met BBZ het oude programma stilaan omzet naar het nieuwe programma.
  
  EERST IO controleren
- # [[2021-07-29]] 
  Bedienings panel is kapot. Een nieuw (groter) paneel gezet.
- # [[2023-02-01]] 
  Extra stappen in seq. vuller (stap S5, S200 en S107) voor controle dat MES is gestart