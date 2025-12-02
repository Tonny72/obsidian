---
title: Aansturing Zuiger - Boosters (Team)
updated: [[2012-07-21]]T09:59:49.0000000+02:00
created: [[2010-11-24]]T10:33:28.0000000+01:00
---

[Aansturing Zuiger - boosters (Team).docx](assets/resources/Aansturing_Zuiger_-_boosters_(Team).docx)
[Aansturing Zuiger - boosters (Team)](file://bedesfs1/sibdes/_UsrData/TL/Private/Documenten/Automation/MHZ/Aansturing%20Zuiger%20-%20boosters%20(Team).docx)

**Aansturing Lier**

![image1](image1-343.png)
1.  Normale werking tussen S+ en S-
2.  Indien men komt op punt x1,3: lier zo snel mogelijk naar boven.
3.  Indien men komt op punt x1,4: Bresklep open.
**Snelheidsregeling FS**
Snelheid wordt geregeld op 3,5 m/s
![image2](image2-184.png)
Om materiaal te kunnen verpompen, moet de pomp binnen het materiaal bereik draaien.
Alarm geven wanneer het toerental van de pomp buiten het materiaal draait.
Indien de snelheid onder een bepaald punt komt, dan de bresklep openen om de pomp te helpen.
**Booster**
![image3](image3-112.png)
De snelheid van de booster-pompen gelijk houden met de snelheid van de baggerpomp

**Vertaling van het Team-document.**
**Samenvatting**
Materiaal uit een productie-installatie naar een met een Stretch
Baggerschip zal worden gewonnen en over een afstand van ongeveer 5,8 km met de hulp van
drie pompstations naar een verwerkingsbedrijf in een andere fabriek
worden gepompt.
Het ontwerp van de pomp en de bepaling van de werkpunten en de
Ontwerp van de pomp station wordt vervoerd door het bedrijf verdediging.

**Productie parameters**
Dichtheid ruw materiaal 2,65 kg/m³
Korn 0,225 mm
Productie 400 ton/h
Flow 800 m³/h
Dichtheid 1,31 kg/l
Nominale snelheid 3,67 m/s
Kritische snelheid 3,31 m/s

****
**Structuur overzicht**
Volgende figuur toont de algemene structuur van het hydraulische circuit. De route bestaat uit een baggerboot en drie pompstations.
![image4](image4-9.jpg)
De doorlooptijd voor het materiaal ligt op 5855 m lengte van de pijp en een snelheid van 3,6 m / s in totaal 1626 seconden of ongeveer 28 minuten.
De pijpleiding heeft een totaal watervolume van ongeveer 360 kubieke meter.
Stopzetting van het materiaal moet worden vermeden, als gevolg van de
Verheffing van de pijpleiding, de zuivering is niet mogelijk.
Dit leegt de pijpleiding, die in rust is niet automatisch op de
bieden perszijde voor de eerste booster, een glijbaan.
Sinds het lozingspunt van de pijpleiding naar de Booster 3 heeft een gat op dit punt, is een glijbaan geïnstalleerd.
**Baggerschip**
Het baggerschip is al beschikbaar en zal worden omgezet voor gebruik in dit project. De exacte elektrische en hydraulische gegevens zijn momenteel niet bekend. Een raming voor het elektrisch vermogen van Baggerschip is opgenomen in Bijlage

**Het Controlesysteem**
Structuur van het controlesysteem
Er wordt verondersteld dat de bagger in de drie pompstations en het land is een PLC met visualisatie (figuur 5.1-1). We gaan ervan uit dat de communicatie wordt gerealiseerd tussen de individuele controles een licht-golf geleider track.
De installatie en inbedrijfstelling, het is zeker nuttig om in de pompstations, een compleet beeld van het gehele systeem. Ook voor de exploitatie en het onderhoud dat nuttig zou zijn. Dit is hoofdzakelijk een kwestie van operationele en zakelijke filosofie.
![image5](image5-5.jpg)
Structuur van het hydraulisch gedeelte van het baggerschip
De baggerschepen zullen worden uitgerust met een pomp van Warmerdam (10 / 8) om de watervoorziening te verzegelen. Het wordt aangedreven door een 6-polige elektrische motor met directe aandrijving en snelheidsregeling. Door middel van een flow sensor, wordt het debiet gemeten. Dit signaal wordt gebruikt om de snelheid van de baggerpomp controle. Het baggerschip is uitgerust met een dichtheid van meting. Het baggerschip is uitgerust met een vacuüm systeem. Het baggerschip heeft een bresklep.

![image6](image6-63.png)
De voordruk sensor komt overeen met de vacuüm sensor. De barrière druk is weer vastgezet te verduidelijken. Het is noodzakelijk te onderzoeken of de regel ook van toepassing wanneer deze pompen, de vergrendeling druk moet worden 0,35 tot 0,7 bar hoger is dan de persdruk!

Regelbereik van het baggerschip
**Vereisten:**
**Voor het genereren van een continue stroom van materiaal aanwezig moet zijn in de winning-proces, een vacuüm- en debiet regeling aanwezig zijn.**

**Vacuüm regeling**
**Vereisten:**
**De besturing is weer terug in "werking van de pomp. Geen niet-erkende fout met een status hoger dan zijn M 'gemeld. De twee bypass kleppen zijn gesloten, SVA111 (wisselvanne booster) en SVA113 (klep achter zuiger Mam) te openen. De lijn wordt gevuld met water.**
**Zo is het vacuüm regelaar ingeschakeld, de schakelaar "vacuüm regulator on / off" worden geëxploiteerd op de visualisatie-interface (op).**
**Het vacuüm regelaar kan altijd worden uitgeschakeld door de gebruiker wanneer de schakelaar wordt bediend vacuüm regulator on / off "op de visualisatie scherm (gehandicapten).**

**De controle van de saugrohrwinde gedaan in een fase on-off-modus.**
****
**De output van de controller (controle-waarde) wordt berekend in verhouding tot het verschil tussen het vacuüm setpoint = PA_Vakuumregelung_Vakuumsollwert en het vacuüm waarde met de proportionele factor = PA_Vakuumregelung_PID proportionele factor en beperkt in-PA_Vakuumregelung_PID Max_Output ... PA_Vakuumregelung_PID-Min_Output.**
**Er is een dode zone gelijk aan de snelheid drempel voor fijne controle van Saugrohrwinde PA_Vakuumregelung_Saugrohrwinde_Schwellwert (de lineaire snelheid van de Saugrohrkopfes in m / sec) berekend met behulp van de karakteristieke PA_Saugrohrwinde_Geschwindigkeit_zu_Drehzahl_x1 ... PA_Saugrohrwinde_Geschwindigkeit_zu_Drehzahl_xy2 in de snelheid in rpm. Hoger is dan de absolute waarde van de controller de uitgang van die drempel, dus deze uitgang wordt gebruikt als een snelheidsregeling voor het regelen van de Saugrohrwinde. Als de output waarde van de doden binnen het bereik, is de Saugrohrwinde niet bediend.**

**Als het vacuüm waarde, de ineenstorting detectiedrempel = PA_Vakuumdruck_Einsturzerkennungsschwelle hieronder (alle vacuum waarden negatief zijn), om de overgang stap "ineenstorting", waarin de aanzuigslang wordt verhoogd totdat de hysterese drempel = PA_Vakuumdruck_Einsturz hysteresis ondergrens is bereikt. Kom dan terug naar de controller in stap werking van de pomp. Het vacuümsysteem is weer actief.**

**Beneden het vacuüm waarde van de blokkade Erkennuschwelle = PA_Vakuumdruck_Verstopfung langer dan de wachttijd = PA_Vakuumdruck_Verstopfung_Wartezeit (alle vacuum waarden zijn negatief), dan is het vacuum regulator is uitgeschakeld en de controle overgaat naar stap "stop", waar het blijft tot het vacuüm feedback opnieuw normaal en de fout werd erkend. Kom dan terug naar de controller in stap werking van de pomp. Het vacuüm controller is niet automatisch ingeschakeld.**

**Automatische bresklep**
De bypass klep kan handmatig worden gecontroleerd op elk gewenst moment. De handmatige bediening van de bypass klep heeft over de automatische besturing van een hogere prioriteit.
**Vereisten:**
**De besturing is weer terug in "pompen" operatie. Geen niet-erkende fout met een status hoger dan zijn M 'gemeld. De twee bypass kleppen zijn gesloten, de twee dia's te openen. De lijn wordt gevuld met het mengsel. Het vacuüm regelaar staat op.**

**Zo heeft de Brest flap automatisch wordt bediend, om de parameters PA_Brestklappe_automatisch om de waarde TRUE worden ingesteld.**

**Als de huidige vacuüm-waarde daalt tot onder de drempel PA_Brestklappe_VAKUUM_Auf (alle vacuum waarden zijn negatief) of wanneer de stroom daalt onder de drempel PA_Brestklappe_GESCHW_Auf, de Brest deur gaat automatisch open. De overgang naar stap "instorten" wordt geactiveerd. Als de overgang naar stap "Collapse" van de automatische opening van Brest flap is gerezen, is de buis opgeheven. De diepte verschil in meters, waarrond de aanzuigslang wordt verhoogd, wordt bepaald door de parameter waarde PA_Brestklappe_Einsturz_Saugrohr_anheben. De duur van de opdracht krijgen van de Saugrohrwinde is berekend op basis van de parameterwaarde PA_Saugrohrwinde_Geschwindigkeit_Holen. Na de zuigkracht werd verhoogd door de diepte verschil, is de sluiting toestand van Brest flap gecontroleerd. Als de huidige vacuüm waarde hoger is dan de drempel PA_Brestklappe_VAKUUM_Zu (alle vacuum waarden zijn negatief) en op hetzelfde debiet hoger is dan de huidige drempel PA_Brestklappe_GESCHW_Zu, de Brest deur gesloten is. Wanneer deze meer dan de huidige waarde van het vacuüm-vacuüm Einsturzhystereseschwelle (alle vacuum waarden zijn negatief), is de verhoging van de zuigbuis gestopt. Volgende gaat allemaal volgens de gebruikelijke scenario van stap "ineenstorting" van.**

**Debietregeling**
**Vereisten:**
De besturing is weer terug in "werking van de pomp. Geen niet-erkende fout met een status hoger dan zijn M 'gemeld. De twee bypass kleppen zijn gesloten, de twee dia's te openen. De lijn wordt gevuld met water.
Zo is het debiet regelaar ingeschakeld, de schakelaar
"Flow snelheidscontrole On / Off", actief op de visualisatie-interface (op).
Het debiet regelaar kan altijd worden uitgeschakeld door de gebruiker als de schakelaar snelheid van flow control on / off "wordt gedrukt op de visualisatie scherm (uitgeschakeld).

De parameterwaarde PA_Fliessgeschwindigkeitsregelung_PID proportionele factor wordt gebruikt als de transfer factor van het evenredige deel van de PID-regelaar. De stroomsnelheid commando waarde wordt berekend als het rekenkundig gemiddelde van de parameters en PA_Fliessgeschwindigkeitsregelung_Sollwert_minimal PA_Fliessgeschwindigkeitsregelung_Sollwert_maximal. Het uitgangspunt van de controller (gemanipuleerde variabele) is evenredig met het verschil tussen de stroomsnelheid
Setpoint en de stroomsnelheid waarde met de proportionele factor wordt berekend en in-PA_Fliessgeschwindigkeitsregelung_Sandpumpe Drehzahl_Min ...
PA_Fliessgeschwindigkeitsregelung_Sandpumpe-Drehzahl_Max beperkt. Ter verbetering van de controle op de kwaliteit kan ook het integraal onderdeel van de PID regelaar zijn ingeschakeld.
Structuur van het hydraulisch gedeelte van de pompstations
De booster pomp stations zijn met het bedrijf Warman (200 SHG) met
Seal watervoorziening veilig. De drive is een 4-pins
Elektromotor met riemaandrijving en snelheid controle zijn verricht.

![image7](image7-54.png)
De initiële druksensor bevindt zich onder de pomp design bij 1 bar. In werking mag de voordruk in geen geval negatief worden.

Met betrekking tot de verzegeling waterdruk is hier dezelfde opmerking als in de baggerpomp.

Het zegel watervoorziening komt uit het land station. Met een beperkte watertoevoer pomp vers water in de seal waterleiding wordt geïntroduceerd.

De diameter van de afdichting waterleiding zijn verschillend
Zwischen Pumpe und Booster 3:
o 140 mm
o 2.230 m
o 3 x 7 m3/h
o v = 0,379 m/s
o Druckverlust pro 100m = 0,012 bar

Zwischen Booster 3 und Booster 2:
o 110 mm
o 1.615 m
o 2 x 7 m3/h
o v = 0,409 m/s
o Drukverlies pro 100m = 0,018 bar
Tussen Booster 2 en Booster 3:
o 75 mm
o 910 m
o 1 x 7 m3/h
o v = 0,440 m/s
o Drukverlies pro 100m = 0,034 bar

Totale stroom = 21m³/h

Het zoete water pomp kan ook worden gebruikt bij de bestrijding van de werkpunten van elke blokkeren waterpomp in een gestaag werkpunt.

Sequentie
![image8](image8-2.jpg)
Stap "in de pijplijn te vullen" (eerste vulling - na het legen)
**Vereisten:**
De besturing is weer terug in "Ready". Geen niet-erkende fout met een status hoger dan zijn M 'gemeld. De Saugrohrtiefe hebben 2 ... 5 m., met de Saugrohrkopf in het open water moet worden gevestigd. )
Dit vulproces is gestart, de schakelaar "pijplijn te vullen on / off" worden geëxploiteerd op de visualisatie-interface (op). Het is "vulpijp" van de overgang naar de fase (als er geen fout met de status hierboven, M opgetreden ').

- De kleppen gesloten
- De twee bypass kleppen zijn gesloten
- Het zegel waterpomp om zand pomp en waterpompen afdichting voor alle booster pompen zijn ingeschakeld.
- Het zand pomp met het toerental instelling = PA_Rohrleitung_befüllen_Sandpumpe_Drehzahl \[rpm\] aangeschakeld.
- Na het persen druk heeft bereikt de drempel PA_Rohrleitung_befüllen_Sandpumpe_Pressdruck_Schwellwert, de Schieber_Bagger geopend. De Schieber_Land is gedeeltelijk open.
- De booster pompen zijn vrijgegeven. Als het formulier is groter dan de drempel voor het vullen = PA_Rohrleitung_befüllen_Booster_X\_Vordruck_Schwellwert (waarbij X -.- Nee Booster), dan is de bijbehorende booster pomp. Target snelheid wordt berekend met behulp van de volgende formule: *Snelheid = PA_Boosterpumpe_1\_Drehzahlverhältnis_Offset + PA_Boosterpumpe_1\_Drehzahlverhältnis_Faktor \* Zand toerental van de pomp;*
- Wachttijd = PA_Rohrleitung_befüllen_Wartezeit_bis_Betriebsbereit
- De twee kleppen zijn gesloten
- De zandpomp en boosterpompen zijn uitgeschakeld
- Het zegel waterpomp de pomp zand en afdichting waterpomp naar de booster pompen zijn uitgeschakeld.
- Overgang terug naar stap "operatie" (als het niet fout met een status hoger dan S opgetreden ').
  Deze modus komt overeen met de stap "vulpijp" controle van de graafmachine en dezelfde stap elke booster station controller.
  "Vul pipe" De verhuizing kan worden geannuleerd te allen tijde door de gebruiker bij het "vulpijp on / off" schakelaar wordt gedrukt op de visualisatie-interface (de gaten).
- De twee afsluiters en bypass-kleppen zijn gesloten.
- Alle pompen zijn uitgeschakeld.
  **Reactie op Fout:**
  **Zal "vulpijp" in de stap van de glijbaan, een van de bypass klep of een pomp die betrokken zijn bij de werking van de gestoorde, om de overgang stap "off", waarbij alle uitgangen worden geschakeld meteen uit. Hetzelfde gebeurt wanneer een van de relevante druksensoren defect is of als een van de gemeten waarden gemeten druk te hoog is (zelfs als de Sperrwasserpumpe_Flowsensor niet meer reageert).**
  **Wanneer er een fout optreedt met een status lager dan N, 'de stap' pijplijn**
  **"Niet te vullen geannuleerd.**
  
  **Gebeurt in stap "in de pijplijn te vullen" een vergissing met een 'N' de status, dus de overgang naar stap "noodsituatie". Alle uitgangen zijn uitgeschakeld.**
  **Gebeurt in stap "in de pijplijn te vullen" een vergissing met de status 'F', dus de overgang in de stap "fatale fout". Alle uitgangen zijn uitgeschakeld.**
  
  **Stap "lege pijplijn"**
  **Vereisten:**
  **De besturing is weer terug in "Ready". Geen niet-erkende fout met een status hoger dan zijn M 'gemeld. De twee bypass kleppen en de twee kleppen zijn gesloten.**
  **Met het oog op de evacuatie wordt gestart, de schakelaar afvoerleiding on / off "worden geëxploiteerd op de visualisatie-interface (op). Het is "lege pijplijn" de overgang in de stap.**
  **Te bloeden de lijn, alleen die twee dia's en de bypass klep kan worden geopend achter de sleepboot, dan kan het water terug te voeren.**
- **De twee bypass kleppen open zijn.**
- **Als de twee bypass kleppen open zijn, de Schieber_Bagger geopend. De Schieber_Land blijft gesloten.**
- **Zodra de Schieber_Bagger en de bypass kleppen open zijn, wachten (wachttijd programmeerbare PA_Rohrleitung_entleeren_Wartezeit).**
- **De twee bypass kleppen en Schieber_Bagger worden gesloten.**
- **Transfer terug naar "operatie" (stap wanneer er geen fout met de status hierboven vermeld, heeft S opgetreden ').**
  
  **Deze modus komt overeen met de stap "lege pijplijn" van de graafmachine controle en dezelfde stap elke booster station controller.**
  
  **"Afvoerpijp" De verhuizing kan worden geannuleerd te allen tijde door de gebruiker bij het "lege pijp aan / uit"-schakelaar is ingedrukt op de visualisatie-interface (uit).**
- **De twee bypass kleppen en de kleppen zijn gesloten.**
  **Reactie op Fout:**
  **Als "lege pijplijn 'in de stap van Schieber_Bagger, de Schieber_Land of de bypass wordt verstoord, dan is de overgang naar de stap" off ", waarbij alle uitgangen worden geschakeld meteen uit. Wanneer er een fout optreedt met een status lager dan N '(zie ook verder) is "lege pijplijn' van de stap is niet geannuleerd.**
  **Gebeurt in stap "lege pijplijn" een vergissing met een 'N' de status, dus de overgang naar stap "noodsituatie". Alle uitgangen zijn uitgeschakeld.**
  **Gebeurt in stap "lege pijplijn" een vergissing met de status 'F', dus de overgang in de stap "fatale fout". Alle uitgangen zijn uitgeschakeld**
  
  **Stap "pump-besturingssysteem met water / zand mengsel"**
  **Vereisten:**
  De besturing is weer terug in "Ready". Geen niet-erkende fout met een status hoger dan zijn M 'gemeld. De twee bypass kleppen en twee kleppen moeten worden gesloten. De lijn is volledig gevuld met water. De Saugrohrtiefe hebben 2 ... 5 m., met de Saugrohrkopf in het open water moet worden gevestigd.
  Zo is de automatische modus wordt gestart, de schakelaar moet "pomp die on / off" worden geëxploiteerd op de visualisatie-interface (op). De overgang vindt plaats in de stap "pomp" operatie (als er geen fout met een status hoger dan M opgetreden ').
- Overgang in de stap "Pump operationele aanpak" (als er geen fout met hoger dan de staat, M 'plaatsgevonden)
- Het zegel waterpomp om zand pomp en waterpompen afdichting voor alle booster pompen zijn ingeschakeld.
- De twee glijbanen en twee terugstroomafsluiter zijn gesloten. Het Zand pomp wordt ingeschakeld met de snelheid instelling = PA_Pumpenbetrieb_anfahren_Sandpumpe_Drehzahl.
- Na het persen druk heeft bereikt de drempel A_Rohrleitung_anfahren_Sandpumpe_Pressdruck_Schwellwert, de Schieber_Bagger openen.
- De booster pompen zijn vrijgegeven. Als het formulier is groter dan de drempel voor het vullen = PA_Rohrleitung_anfahren_Booster_X\_Vordruck_Schwellwert (waarbij X -.- Nee Booster), dan is de bijbehorende booster pomp. Target snelheid wordt berekend met behulp van de volgende formule:
	- Snelheid = PA_Boosterpumpe_1\_Drehzahlverhältnis_Offset PA_Boosterpumpe_1\_Drehzahlverhältnis_Faktor \* Zand toerental van de pomp;
- Als de compressie druk van de booster pomp 3 boven de drempel PA_Rohrleitung_anfahren_Booster_3\_Pressdruck_Schwellwert, de Schieber_Land geopend.
- Zodra de Schieber_Land open is, het zand pomp snelheden (met de Versnelling = PA_Pumpenbetrieb_anfahren_Sandpumpe_Drehzahlbeschleunigung). Het zand toerental van de pomp wordt verhoogd met de waarde = PA_Sandpumpe_Drehzahlvorgabe. De booster pompen worden nog steeds bepaald door de snelheid eisen, die worden berekend door de bovenstaande formule.
- Als het zand pomp een snelheid bereikt van de waarde van het werk, wordt gewacht.
  Wachttijd = PA_Pumpenbetrieb_anfahren_Wartezeit_bis_Pumpenbetrieb.
- Na het verstrijken van de wachttijd, om de overgang stap "pompen" (als er geen fout met de status hierboven, M 'plaatsgevonden)
  Deze modus komt overeen met de stappen van "pump-operationele aanpak" en "pomp" de werking van de graafmachine controle en dezelfde stappen elke booster station controller.
  De verhuizing "pomp" operatie kan worden gestopt te allen tijde door de gebruiker wanneer de knop "Pump-operatie On / Off" wordt gedrukt op de visualisatie-interface (Uit). In dit geval, de overgang in de stap "Stop".
  **Reactie op Fout:**
  **Wanneer er een fout optreedt met een status lager dan "A" is de stap werking van de pomp is niet "afgebroken.**
  **Kick terug in de 'pump-operatie "een vergissing met de status' A ', dus de overgang in de stap" Stop. Na deze fout is erkend, de overgang in de stap "pomp" werkt weer.**
  **Als "Move werking van de pomp" in stap een van de dia, een van de bypass klep of een pomp die betrokken zijn bij de werking van de gestoorde, de overgang in de stap**
  **"Switch off" (dia-en bypass-kleppen open moet blijven staan). Alle uitgangen zijn direct uitgeschakeld. Hetzelfde gebeurt wanneer er een fout hoger met de status als 'M' optreedt (zie ook verder) als een van de relevante druksensoren defect is of als een van de bewaakte gemeten drukwaarden te hoog is (zelfs als de Sperrwasserpumpe_Flowsensor niet meer reageert).**
  
  **"Move pompen operatie" stap in stap of "pomp" operatie met een fout status, N ', dus de overgang naar stap "noodsituatie". Alle uitgangen zijn uitgeschakeld.**
  **stap "Move operatie pomp" in stap of "pomp" een vergissing met de status 'F', dus de overgang in de stap "fatale fout". Alle uitgangen zijn uitgeschakeld.**
  
  **Stap "pump-besturingssysteem met water / zand mengsel stop"**
  Pompen, die met water / zand mengsel stoppen - stoppen uit bij de gewone
  **Vereisten:**
  **De besturing is weer terug in "pompen" operatie. Geen niet-erkende fout met een status hoger dan zijn M 'gemeld. De twee bypass kleppen zijn gesloten, de twee dia's te openen. De lijn is geheel gevuld met het mengsel.**
  **Zo wordt de werking van de pomp ingesteld, de schakelaar, die pompen aan / uit "worden geëxploiteerd op de visualisatie-interface (uit). Voor de eerste stap de overgang naar de "Stop" (als er geen fout met een status hoger dan M opgetreden ').**
- **Overgang in de stap "Stop.”**
- **Er wordt nagegaan of het vacuüm is hoger dan de drempelwaarde "vacuüm-water drempel \[bar\]" is (alle vacuüm waarden zijn negatief). Dit is niet het geval, dan is het inlaatspruitstuk wordt automatisch verhoogd tot dit niveau is bereikt.**
- **Als het vacuüm-water drempel is bereikt en of er geen fout met een status hoger dan S heeft plaatsgevonden '(ook zie verder), de passage in de stap "Stop".**
- **Tijdens de purge tijd = PA_Pumpenbetrieb_einstellen_Spülzeit wordt gepompt. De purge tijd bij de aanpassing van het mengsel financiering is ongeveer 28 minuten plus wat vrije tijd (bijv. 5 minuten).**
- **De twee kleppen zijn gesloten.**
- **Als de kleppen gesloten zijn, zijn het zand pomp en alle booster pompen uitgeschakeld.**
- **Het zegel waterpomp de pomp zand en afdichting waterpomp naar de booster pompen zijn uitgeschakeld.**
- **Wachttijd = PA_Pumpenbetrieb_einstellen_Wartezeit_bis_betriebsbereit.**
- **Na het verstrijken van de wachttijd, om de overgang stap "Ready" (als er geen fout met een status hoger dan S opgetreden ').**
  
  **Deze modus komt overeen met de stappen van "Stop" en "shutdown" van de graafmachine controle en dezelfde stappen elke booster station controller, geschiedde in die de controle van de stap "pomp" werking wanneer de schakelaar "pomp die op" wordt gedrukt op de visualisatie-interface ( uit), of (misschien) een bug met de status 'S optreedt' (zie ook verder).**
  
  **Visualisatie en parameter**
  Display de operationele status van de pompen
  Indicator voor de pomp, zoals een pomp-overzicht scherm, met split-achtige vertegenwoordiging van alle pompen in parallel:
  \- Vordruck \[bar\]
  \- Pressdruck \[bar\]
  \- Differenzdruck \[bar\]
  \- Drehzahl-Pumpe \[RPM\]
  \- Leistung \[kW\]
  \- Sperrwasserdruck \[bar\]
  \- Betriebszustand - Pumpenmotor
  o AUS grau
  o Betrieb grün
  o Störung rotv
  \- Betriebszustand – Sperrwasserpumpenmotor
  o AUS grau
  o Betrieb grün
  o Störung rot
  \- Staus Not-Aus gelb/rot
  \- Störmeldungen Text
  Schieber – I/O – Variablen
  \- Schieber Auf DA
  \- Schieber Zu DE
  \- Schieber Störung DE
  \- Schieber zu DE
  \- Schieber offen DE
  
  Reacties op de controle problemen (foutmeldingen)
  De foutmeldingen kan een van de volgende status
  I - informatie (het bericht wordt alleen weergegeven)
  M - bericht (waarschuwing)
  A - pauze (de overgang in de stap "Stop" wordt verhoogd)
  S - stop (de overgang in de stap "Stop" en vervolgens in de stap "Stop" wordt verhoogd)
  N - Emergency (de overgang naar stap "noodstop wordt geactiveerd, waarbij alle uitgangen onmiddellijk worden uitgeschakeld)
  F - Fatale fout (de overgang in de stap "fatale fout" wordt geactiveerd, waarbij alle uitgangen onmiddellijk worden uitgeschakeld)