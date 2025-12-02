---
created: [[2012-11-22]]T09:58:50.0000000+01:00
modified:  2025-07-21
---
# HDA uit 800xA trekken


| **Attachments** | [SQL Server.msg](SQL_Server.msg) |
|-----------------|------------------------|

![image1](image1-31.png)

| **Subject** | **SQL Server**                                    |
|-------------|---------------------------------------------------|
| **From**    | [Tonny Lemmens](mailto:tonny.lemmens@sibelco.com) |
| **To**      | 'jef.mertens@sibelco.com'                         |
| **Cc**      | Kristof Loos (kristof.loos@sibelco.com)           |
| **Sent**    | vrijdag 9 november 2012 13:07                     |

Jef,

Ik heb nog voor 2 zaken jullie assistentie nodig:

1.  Installeren van een Windows 2012 server waar SQL server 2012 op moet komen.
2.  Configureren van de netwerkwerk instellingen van de Siemens PC (vlan’s netwerkkaarten, etc..)

Wanneer kan dit gebeuren? Gaat dit volgende week woensdag (14/11) of donderdag (15/11)?

Mvg

Tonny Lemmens

Elektrische Dienst




HDA uit 800xA trekken
donderdag 22 november 2012
9:58

- # [[2012-12-06]] 
  Dit duurt te lang. Besloten om Excel te gebruiken (in afwachting van cpm)
- # [[2012-11-27]]
  Mail van Peter ontvangen
  *Ik ben nog druk met de aantal opties die we hebben in kaart te brengen om te bepalen wat haalbaar is ...*
  
  *het makkelijkste is om de exel verzie te veranderen zodat we gewoon een groter werkveld krijgen. maar dat betekent wel dat we*
  
  *dat voor alle systemen moeten doen.*
  
  *we zijn ook nog aan het kijken naar een cristal reports mogelijkheden.*
  
  *Helaas ben ik de komende dagen even niet beschikbaar.*
  
  *Ik zal proberen maandag uitsluitsel te geven wat de beste methode gaat worden..*
- # [[2012-11-22 1]] 
  Mail naar Peter en Remco gestuurd met vraag naar de Status
- # 15/11 /2012
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