---
date created: 2012-11-22
date modified: 2025-07-21
---
# LOG DES 800xA en ABB

- # [[2012-11-15]]
  Antwoord van Peter Stroop gehad. Hij gaat dit uitzoeken.
  
  Aan Remco Dercksen gevraagd om dit uit te zoeken.
  Zie ook \<[file://C:\Users\TL79FF\~1.SIB\AppData\Local\Temp\OneNoteAttachments\SQL](file:///C:/Users/TL79FF~1.SIB/AppData/Local/Temp/OneNoteAttachments/SQL) Server.msg\<[file://C:\Users\TL79FF\~1.SIB\AppData\Local\Temp\OneNoteAttachments\SQL%20Server.msg](file:///C:/Users/TL79FF~1.SIB/AppData/Local/Temp/OneNoteAttachments/SQL%20Server.msg)\>\>
- # Mail van Bart
  To: Herwig Janssen; Tonny Lemmens; Mike Van de Put
  Cc: Rocco Opdebeek; Rob Vreys; Jan Vreys; Geert Staes; Peter Drees; Jos Vanhoof; Ronny Hoeben; Wim Nuyts
  Subject: Verslag meeting molen 5 Sibelco-CMI-Digasys e.a.
  
  Hierbij mijn impressie van de vergadering deze voormiddag.
  Verslag verder te verdelen indien noodzakelijk.
  
  Te nemen acties asap uitvoeren.
  Timing van de start van de testen wordt later vastgelegd in functie van de voortgang van de voorbereidingen (tempo wordt hier bepaald door DDB/Digasys).
  
  Aanwezig:
  
  Mike Van de Put, Tonny Lemmens en Bart Van Herck (Sibelco)
  Olivier Leroy (CMI)
  Bruno Ternisier (Naude T)
  Kurt Vanderspinnen (KVDS)
  Eddy Vansevenant (Digasys)
  
  Besproken punten:
  
  A. Bepalen gewicht molen op drie manieren: 'essai de l'essai'
  
  1\. Rekstrookjes
  
  1.a. Positie van de vier rekstrookjes (twee op elk chassis) werd vastgelegd en gemarkeerd. Plaatsing = Digasys.
  (Hierbij de kwam opmerking dat Mr Vansevenant dat hij nog geen antwoord gekregen heeft op de vraag aan DDB om hiervoor 2.000 Euro provisie te krijgen. Deze 'speciale' rekstrookjes kunnen pas besteld worden na deze goedkeuring en de levertermijn is 2-4 weken !! )
  
  1.b. Sibelco voorziet op de vier posities waar de rekstrookjes geplaatst worden telkens een pt100-temperatuursensor met uitlezing. Deze moet NIET gelogd worden, maar wordt afgeschreven op geregelde tijdstippen (Rob/Mike/Bart)
  
  2\. Motorvermogen
  
  Sibelco (Elekrische dienst) zal het vermogen van de drives aan Digasys aanbieden in de vorm van een spanningssignaal. Omvormen bestaande mA-signaal uit de drive ofwel een extra uitgang hiervoor te voorzien. Plan B is het aanbieden van de data uit DCS ABB. (Rob/Bart)
  
  3\. Manuele meting + berekening
  
  3\. a. Sibelco neemt op vijf equidistante plaatsen een staal van ongeveer 10 liter. Deze stalen worden verzameld in een vat staande op een weegschaal waarin reeds voldoende water aanwezig is om door het niveauverschil een volumebepaling te doen. Tegelijk wordt het vat dus gewogen en de kan de dichtheid perfect worden bepaald. (Weegschaal labo kan tot 300kg wegen)
  
  3\. b. Sibelco doet onder controle van Digasys een meting van de vrije ruimte tussen materiaal en molenwand (op vijf equidistante plaatsen) en bepaalt met behulp van de bekomen dichtheid in 5.a. de volume-inhoud van de molentrommel. Volmumebepaling in samenspraak met Projectafdeling (Mike/Ronny/Bart)
  
  4\. Opstellen van de database
  
  Praktische haalbaarheid van het samenvoegen van de data van Digasys (min 10 Hz) en de data van DCS-Sibelco (+/- 1Hz) wordt door Digasys uitgevoerd
  
  B. Ijking van de drie meetmethodes
  
  Hierbij stelt Sibelco de vraag of de capaciteit voor deze test moet worden opgedreven tot 80-85% ipv de huidige 70-75%.
  Blijkbaar heeft dat voor deze haalbaarheidstest geen zin en brengt dit enkel 'bijkomende risico's' met zich mee... (TBD, want in verslag Digasys staat wel degelijk 80%)
  
  De drie voorgestelde meetmethodes worden simultaan geijkt als volgt:
  
  \- In- en uitgang van de molentrommel worden afgesloten
  \- De manuele gewichtsmeting (afstandsmeting) wordt uitgevoerd
  \- De molen draait 10 minuten terwijl de metingen gelogd worden
  \- De molen wordt gestopt en er wordt 20 ton uit de molen gezogen. Dit gewicht wordt gecontroleerd door passage langs de weegbrug.
  \- De molen wordt gestart om het niveau van het product overal weer gelijkmatig te verdelen
  \- De molen wordt weer gestopt en geopend om de manuele volume/gewichtsmeting weer te herhalen
  
  Deze cyclus wordt hehaald tot de molen volledig leeg is.
  
  C. Meten rekken op de trommel
  
  (vooraf: bedoeling van deze opstelling is het testen van de haalbaarheid met n rekstrookje. Het bestellen van het volledige meetsysteem van 12 kanalen zal minstens 12 weken duren en zal blijkbaar pas gebeuren na evaluatie van deze haalbaarheidsstudie...)
  
  1\. Digasys installeert als proef n rekstrookje op de molenwand ter hoogte van de uitloop
  2\. Sibelco legt de kabel (levering Digasys) tussen dit rekstrookje en de zender (dient ge soleerd te worden van de trommelwand vermits de kabel slechts hittebestendig is tot 80 C). Zender wordt ter hoogte van de tandkroon geplaast (Mike)
  3\. Sibelco bevestigt de rondantennekabel ge soleerd op de molen (Mike)
  4\. Sibelco plaatst de naderingsschakelaar voor de positiebepaling van de trommel (Mike)
  5\. Alle elektrische aansluitingen voor dit deel gebeuren door Digasys !!
  
  D. Analyse van de meetresultaten
  
  Digasys zal de bekomen metingen analyseren om daarna te bepalen met welke methode(s) zal worden verder gewerkt.
  
  Dit wou ik jullie mededelen
  Bart
  
  Veiligheid: respecteer verkeersregels - overal !
  Safety: respect traffic rules - everywhere !
- # [[2012-11-27]]
  Mail van Peter ontvangen
  *Ik ben nog druk met de aantal opties die we hebben in kaart te brengen om te bepalen wat haalbaar is ...*
  
  *het makkelijkste is om de exel verzie te veranderen zodat we gewoon een groter werkveld krijgen. maar dat betekent wel dat we*
  
  *dat voor alle systemen moeten doen.*
  
  *we zijn ook nog aan het kijken naar een cristal reports mogelijkheden.*
  
  *Helaas ben ik de komende dagen even niet beschikbaar.*
  
  *Ik zal proberen maandag uitsluitsel te geven wat de beste methode gaat worden..*
- # [[2012-12-06]] 
  Dit duurt te lang. Besloten om Excel te gebruiken (in afwachting van cpm)
- # [[2012-11-09]]
  Remco Dercksen gevraagd om hier werk van te maken
- # [[2012-11-15]]
  Een mail naar Peter Stroop gestuurd met vraag naar de status
- # [[2012-11-20]]
  OPC client van Dessel naar Peter gestuurd
- # [[2012-11-22 1]] 10:07 
  Een mail naar Peter en Remco gestuurd met vraag naar status
- # [[2012-11-27]]
  Beste Tonny,
  
  Ik ben nog druk met de aantal opties die we hebben in kaart te brengen om te bepalen wat haalbaar is ...
  het makkelijkste is om de exel verzie te veranderen zodat we gewoon een groter werkveld krijgen. maar dat betekent wel dat we
  dat voor alle systemen moeten doen.
  
  we zijn ook nog aan het kijken naar een cristal reports mogelijkheden.
  
  Helaas ben ik de komende dagen even niet beschikbaar.
  Ik zal proberen maandag uitsluitsel te geven wat de beste methode gaat worden..
  
  En de OPC client is goed aan gekomen werkte perfect via de skydrive...
- # [[2012-12-06]] 
  Mail naar Peter gestuurd met vraag naar vorderingen
- # [[2012-12-28]] 8:37 
  Er moet een extra CPU worden bijgezet.
- # [[journals/older/2013/2013-01-09]] 13:48 
  Performantie probleem opgelost
- # [[2013-06-06]] 9:55 
  Licentie probleem i.v.m. tags opgelost. Veel ongebruikte objecten verwijderd.
- # [[2013-08-07]] 10:54 
  SibMotorBi aangepast.
  ![image1](image1-3%201.png)
- # [[2013-09-23]] 12:43 
  Vandaag problemen gehad met servers. 800CS en AS servers herstart.
  PLC [[LLB]] was vast gelopen. Gereset. *Het is me het dagje wel.*
- # [[2013-09-23]] 14:59 
  D-schijven van de 800CS waren vol gelopen. Software DVD naar C verhuisd.
- # [[2014-02-05]] 11:20 
  Ticket bij ICT ingelegd voor het SMS probleem
  [SMSsen vanuit 800xA](onenote:800xA%20Todo.one#SMSsen%20vanuit%20800xA&section-id={3B13E359-B650-42EF-A219-D0939C605E6B}&page-id={67A4D7CE-62D0-4CA8-B826-EEC2F04B2EF1}&end&base-path=https://d.docs.live.net/648fe635197c5860/Documenten/OneNote's/Persoonlijk%20(web)/Installaties/DES/800xA)
- # [[2014-02-06]] 11:58 
  [SMSsen vanuit 800xA](onenote:800xA%20Todo.one#SMSsen%20vanuit%20800xA&section-id={3B13E359-B650-42EF-A219-D0939C605E6B}&page-id={67A4D7CE-62D0-4CA8-B826-EEC2F04B2EF1}&end&base-path=https://d.docs.live.net/648fe635197c5860/Documenten/OneNote's/Persoonlijk%20(web)/Installaties/DES/800xA)
  Samen met Kristof een extra config op de SMS server aangemaakt
- # [[2014-02-07]] 14:59 
  Alarmen LLB uit de alarmlijst gehaald
- # [[2014-02-07]] 13:32 
  [SMS voor HHH niveau's B53, B62, B67, B86](onenote:800xA%20Todo.one#SMS%20voor%20HHH%20niveau's%20B53,%20B62,%20B67,%20B86&section-id={3B13E359-B650-42EF-A219-D0939C605E6B}&page-id={2F385CC9-7928-4093-B464-BAF4E845F298}&end&base-path=https://d.docs.live.net/648fe635197c5860/Documenten/OneNote's/Persoonlijk%20(web)/Installaties/DES/800xA) Done
- # [[2014-02-11]] 12:44 
  SMS sen kwamen dubbel binnen. Opgelost
- # [[2014-02-13]] 15:05 
  PAC VB15.2 via Profinet.
  Het werkt tot op de switch.
  Volledig afgewerkt inclusief Faceplate
  Ticket bij ICT gemaakt voor enabelen van Profinet op de switchen
- # [[2014-02-18]] 14:52 
  Profinet werkt via switch.
  Kristof moet andere switchen van nieuwe software voorzien. Mogelijk moet de hele stack worden geupgrade.
- # [[2014-10-09]] 11:42 
  Full Backups van AS2 verplaatst naar BEDESNAS1
  [\\\10.32.16.25\Production_Software\Backups\ABB\Backups 800xA](file://10.32.16.25/Production_Software/Backups/ABB/Backups%2520800xA)
- # [[2014-10-13]] 9:15 
  Services van CS1 herstart omdat er geen history in de trending stond.
- # [[2014-10-13]] 19:17 
  AS2 herstart. Geen ping naar 10.32.29.254
- # [[2014-11-19]] 14:25 
  Interlock graphic gemaakt. Te vinden onder Graphics Structure - Graphics Tools - Sibelco
- # [[2015-02-23]] 15:24 
  Geëxperimenteerd met versioning (versie beheer) van libraries. Om met een schone lei te beginnen zouden de meeste bibliotheken op released gezet moeten worden.
  Als ik de sibProcessObj lib willen releasen komen er fouten te voorschijn. Mogelijk kan hier wel worden doorgeklikt, maar ik vertrouw het niet.
  =\> Proberen via een vmdk export van AS1 een test-systeem op te zetten.
- # [[2017-05-22]] 
  Dit weekend 800xA geupgrade naar v6
- # [[2018-05-29]] 
  Skype meeting gehad met Peter Stroop voor analyseren van OPC communicatie
  Applog Viewer gebruiken en Refresh Rate verlagen
- # [[2018-09-17]] 
  800CS2 volledig herstart vanwege opc problemen in faceplate. Enkel de 800xA services herstarten helpt niet.
- # [[2021-07-27]] 
  DES - ALG - Signalen nakijken
  De signalen op scherm moeten grijs of rood zijn, geen groen
  
  =\> Alle signalen op ROOD gezet