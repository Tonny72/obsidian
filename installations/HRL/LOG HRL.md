---
title: LOG HRL
updated: [[2022-09-12]]T09:12:31.0000000+02:00
created: [[2013-01-25]]T12:43:39.0000000+01:00
---

- # [[2012-12-04]] 
  Server is binnen gekomen. Nog in te plannen
- # [[2012-12-10]] 16:29 
  Mail van Tom Peeters
  
  *Beste Tonny,*
  
  **
  
  *Om de down-tijd bij uitval zo kort mogelijk te houden moet het een cold standby systeem blijven.*
  
  *Met andere woorden identieke instellingen, servernaam en ip-adres als de bestaande server.*
  
  *En dan gewoon uitgeschakeld ernaast zetten.*
  
  **
  
  *De scada cliënts maken verbinding met een map op de server en hieruit halen ze de project data.*
  
  *Als je dus de systeemnaam en het ip-adres van de backup-server wijzigt moet dat op alle clients worden aangepast op het moment dat je normale server uitvalt.*
  
  *Ook zitten er in het scada project en de ingestelde plc-connecties verwijzingen naar de computernaam en ip-adressen. Deze zouden op de backup-server dan ook allemaal opnieuw ingesteld moeten worden.*
  
  *Dit is niet iets wat iedereen zo even kan doen, dus zal er iemand van ons waarschijnlijk langs moeten komen om alles op dat moment om te stellen.*
  
  **
  
  *Vandaar dat we hadden afgesproken om een kopie van de server als cold-standby in de kast te leggen.*
  
  *Men zou dan alleen de stekkers om moeten steken, aanzetten en de hele fabriek zou weer moeten werken (op gebied van scada).*
  
  **
  
  *Denk je er donderdag aan dat er <u>Windows Server 2003</u> op moet komen? Een nieuwere OS versie wordt door iFix niet ondersteund.*
- # [[2012-12-10]] 16:44 
  | **9CBHHA6T-CBSWGMXV-TQWQAEPV-MU6B2QJD-XPH4MH34-3479BH8D-Z95JXJF7-T3QK3LYR** |
  |-----------------------------------------------------------------------------|
  
  *From \<<http://www.acronis.com/enterprise/download/thanks/?p=abr11.5sw&Email=tonny.lemmens%40sibelco.com>\>*
  
  <http://www.acronis.com/enterprise/download/backup-recovery/server-windows/>
- # [[2012-12-14]]
  Poging tot installeren de IBM x3550 server. Lukt niet wil niet booten
- # [[2012-12-17]] 8:24 
  Nog enkele ontbrekende drivers.
- # [[2012-12-28]] 8:35 
  Op X3550 M4 server kan geen Windows 2003 meer worden gezet.
- # [[journals/older/2013/2013-01-07]] 12:40 
  Gestart met x3650
  
  Procedure: [Installatie van een IBM server](onenote:#Installatie%20van%20een%20IBM%20server&section-id={C5C3A9A8-E417-4672-8106-3F8124495B5A}&page-id={19627120-0CEE-4A91-88A5-D5C92F10B932}&end&base-path=https://d.docs.live.net/648fe635197c5860/OneNote/Volledige%20documentatie/TODO's.one)
- # [[journals/older/2013/2013-01-09]] 11:19 
  Timo Rutten op de hoogte gebracht
  
  [Tonny Lemmens - Ifix server](Notes://BEDESNTS1/C12566FD00314CF5/DABA975B9FB113EB852564B5001283EA/FE9604200F826848C1257AEE0033EB59)
- # [[2013-01-25]] 10:30 
  Installatie is aan de gang
  
  [Link IFix Server](onenote:Installaties/HRL/IFix.one#section-id={A38EF1E7-BB7F-4369-9618-C5AD2FF402CF}&base-path=https://d.docs.live.net/648fe635197c5860/OneNote/Volledige documentatie)
- # [[2013-01-25]] 12:44 
  [[2013-01-28]] wordt de sailor app getest voor droogzand getest
- # [[2013-01-29]] 9:29 
  Weegbrug client geïnstalleerd.
  
  <http://nlhrlsvrwgb1:59380/custom/install.html>
  
  Check Linkworx
  
  <http://10.31.244.16:59160/?module=tagoverview>
- # [[2013-01-30]] 11:48 
  Testen zijn goed verlopen buiten een klein foutje in de PLC.
  
  Verslag maken voor uitbreiding naar Kwartsmeel.
- #
- # [[2013-02-04]] 16:41 
  Uittesten Matrikon en Kepserver voor simulatie Kwartsmeel
- # [[journals/older/2013/2013-02-08]] 10:51 
  Ik begrijp niet hoe ik in Heerlen moet configuren.
  
  Mail naar Stijn gestuurd.
- # [[journals/older/2013/2013-02-08]] 11:23 
  Mail naar T.Rutten (en Hans) gestuurd.
  
  Timo,
  
  Heb jij nog verder met de IFix server in Heerlen ivm redundantie?
  
  Ivm de laadapplicatie en kwartsmeel:
  
  Per laadplaats wil ik de volgende signalen willen voorstellen.
  
  ![image1](image1-17%201.png)
  
  Voor LB04 is dit natuurlijk overkill, want er zal voor 100% uit silo18 worden geladen. Maar dit is gelijkaardig aan droogzand en dus blijft alles universeel.
- # [[journals/older/2013/2013-02-08]] 11:40
  Mail ontvangen
  
  Wat betreft de iFIX server zijn we weer een stuk verder gekomen.
  
  Tom is nu een weekje op vakantie.
  
  Daarna zullen we het meteen oppakken zodat we het kunnen afronden.
  
  Fijn weekend en / of Carnaval.
  
  Met vriendelijke groet,
  
  Timo Rutten
- # [[2013-03-04]] 8:53 
  Mail verstuurd naar T.Rutten met de vraag hoe ver hij staat.
- # [[2013-03-21]] 9:23 
  Antwoord [[2013-03-11]] van T.Rutten
  
  Afgelopen zaterdag is de inbedrijfname van de nieuwe iFIX server goed verlopen.
  
  We hebben met alle PLC’s communicatie.
  
  Het volgende item is de clients koppelen aan de server.
  
  Antwoord [[2013-03-11]] van Hans Ophelders
  
  Aan de KM verlading zijn we nog niet toegekomen, eerste zullen we de droogzandverlading compleet afronden.
  
  De Ifix server loopt parallel aan droogzandverlading en zal nagenoeg gelijktijdig worden opgeleverd.(mits geen tegenslag)
  
  Tevens nog een aantal kleinere projecten die inmiddels al in gebruik hadden moeten zijn.( droogzandsilo 9 + input DZ naar Molen 4 + ruwzand band Silo-1)
  
  Gezien we door de weeks ook nog productie draaien + verlading moeten waarborgen lopen we al gauw achter de feiten aan.
  
  We starten binnen kort aan de KM verlading, zal je hierover tijdig berichten.
- # [[2013-09-10]] 12:43 
  Meeting kwartsmeel verlading
  
  <https://sibelco.box.com/s/oqdvp107fexrudijoiob>
  
  Timo gaat eerst programmeren en nadien komt pas Stijn in het verhaal.
- # [[2013-11-04]] 8:19 
  [Installatie van een IBM server](onenote:..\..\TODO's.one#Installatie%20van%20een%20IBM%20server&section-id={C5C3A9A8-E417-4672-8106-3F8124495B5A}&page-id={19627120-0CEE-4A91-88A5-D5C92F10B932}&end&base-path=https://d.docs.live.net/648fe635197c5860/OneNote/Volledige%20documentatie)
- # Reserve server
  Type: x3650 7979-2AG
  
  S/N: 99T2999
  
  Administrator password is *blank*
  
  Geen rechten om software te installeren. (Ook geen lokale Administrator inlog gegevens)
  
  Ingelogd met user: ifixadmin , Password: ghjkl op domein: sibelco-europe.amorg.group
  
  Domain account met local admin rechten:
  
  ~~user: SBXIFIG0~~
  
  ~~password: A2ifi12~~
  
  domain: SIBEUR
  
  Local admin account:
  
  user: administrator
  
  password: hectoll
  
  domain: NL-HRL-APS-001
  
  Ook heb ik het ifixadmin account van sibelcobe.amorg.group domain toegevoegd bij de local admins.
- # [[2014-01-13]] 11:38 
  Den boel terug in de gang gestampt.
  
  Doodle voor Stijn en Timo gemaakt
- # [[2014-02-18]] 16:10 
  Loading App is aangepast voor mailverlading.
  
  Timo Rutten moet nog aanpassingen doen in de PLC.
  
  Mail naar Hans gestuurd met de stand van zaken
- # [[2014-02-26]] 9:05 
  5 maart wordt er getest
- # [[2014-03-08]] 15:44 
  Mail naar Hans gestuurd of de testen goed verlopen zijn.
- # [[2014-03-10]] 15:06 
  Niks uitgevoerd vanwege te druk. [[2014-03-11]] opnieuw ingepland
- # [[2015-12-16]] 15:21 
  Configuratie van opcuaserver en loading app voorbereid
  
  Dialogen van loading app moeten aangepast worden.
- # [[2016-01-27]] 09:27 
  25/01 de communicatie van Loading App naar PLC in orde gebracht.
- # [[2013-01-28]] 10:52 
  Installatie van IFix op de server lukte niet.
- # [[2013-01-30]] 11:46 
  Reserve IFix server in het Domain gezet. NLHRLIFIX2
  
  Infofil werkt verder om IFix aan de praat te krijgen.
  
  Documentatie maken
- # [[2016-02-05]] 12:59 
  Het schoot weer niet op vandaag.
  
  Huidige problemen:
- Release valt niet terug op 0 na een stop
- Bunker blijft aangemeld in loading app
  OPMERKING Button Vrijgave Overbrugt van Silo 12 is de test voor de stop van bunker KMS07
- # [[2016-02-11]] 16:06 
  Ik had van Stijn een nieuwe .dll gekregen en de oude hernoemd naar old.dll
  
  Dit mag niet.
  
  De loading app laadde de oude .dll eerst voor de nieuwe .dll. Daarom werkte het niet
- # [[2016-11-09]] 11:00 
  Meeting gehad over de toekomst van IFIX. HRL heeft voorlopig een vergunning tot 2020. Dus we proberen voorlopig alles in de lucht te houden met minimum kost.
- Sibelco\ifixadmin user wordt nog altijd gebruikt, maar moet verwijderd worden. Afgesproken dat dit op [[2016-12-17]] gebeurt.
- Timo bekijkt om een paar PLC's om te zetten naar ethernet. Dan kan uiteindelijk de IFix server virtueel worden gezet.
- Timo bekijkt om voor een upgrade van IFIX zodat deze op een nieuwe server kan worden gezet. Als dit niet te duur is.
- # [[2017-07-18]] (install na de virus crash)
  Zie [IP adressen HRL](onenote:#IP%20adressen%20HRL&section-id={85C84BE7-4DD6-41DA-83CE-AC71C3B7F02D}&page-id={23184BCB-13F9-4A0D-A2DA-2C217095BAD5}&end&base-path=https://d.docs.live.net/648fe635197c5860/Docs/OneNote's/Persoonlijk%20(web)/Sibelco/Installaties/HRL/IFix.one)
  
  Er is voor gekozen om de server en client uit het domain te halen om zelf firewall en updates te kunnen beheren.
  
  We proberen IFIX zoveel mogelijk op een eiland te isoleren.
  
  Op de clients is Windows 7 geïnstalleerd. Deze dienen als host voor VMWare Player
  
  Als virtual machine is XP gekozen. (Windows7 werkt niet met IFIX)
  
  User: ifixadmin
  
  Pw: A2ifi12
- # [[2017-07-24]] 
  Op ESX een user aangemaakt
  
  User: ifixadmin
  
  Pw: A2ifi12. (inclusief punt)
  
  IP ESX server: 10.31.250.29
  
  Netwerk config
  
  ![image2](image2-13%201.png)
- # [[2017-09-29]] 
  Ifix server is klaar
  
  Tom krijgt geen backup getrokken
  
  Aan ICT gevraagd hoe dit moet
- # [[2017-10-04]] 
  Backup maken op [[2017-10-13]]
- # [[2017-10-13]] 
  Rack Heerlen op 13 okt 2017. De kast is toe.
  
  Er is een clone van de IFix op de NAS gemaakt. En een backup staat op de bedesnas1.
  
  ![image3](image3%201.jpeg)
- # [[2018-03-02]] 
  MES tags voor heerlen zijn aangemaakt op de IFIX server en de MES server
- # [[2019-04-10]] 
  Er is nog recentelijk een backup gemaakt.
  
  Ook is er een ticket lopende om de Ifix server in het beheerde Vmware systeem te steken
- # [[2019-05-02]] 
  Men heeft het ticket afgesloten
  
  [INC0053857](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fsibelco.service-now.com%2Fnav_to.do%3Furi%3Dincident.do%253Fsys_id%3D82d6892ddb20f70cbe45320a68961990%2526sysparm_stack%3Dincident_list.do%253Fsysparm_query%3Dactive%3Dtrue&data=02%7C01%7CTonny.Lemmens%40sibelco.com%7Cce0f1acc8e214ba4c96208d6c6e83057%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C636915097891192078&sdata=eVw7MEX1ESk3QFnDnC%2BFgb43tofDdlQlaRow8azcSGw%3D&reserved=0)
- # [[2019-05-14]] 
  Aan Jef gevraagd hoe dit nu verder moet
- # [[2019-05-24]]
  Jef er nog eens op gewezen
- # [[2019-05-28]] 
  IFIX server gecrasht
- # [[2019-06-04]] 
  Nieuwe server HP Proliant klaargemaakt en config terug restoren.
- # [[2019-06-07]] 
  HP Proliant server is geplaatst en getest. Nu enkel nog de licentie. Dit is (al meermals) aan Jef gevraagd.
  
  Free license
  | VMware vSphere Hypervisor 6 License | J102N-0U00H-K8R81-0V98M-14FMK |
  |-------------------------------------|-------------------------------|
  
  *Van \<<https://my.vmware.com/en/group/vmware/evalcenter?p=free-esxi6>\>*
- # [[2019-09-04]] 
  Mail naar Jef
  
  Jef,
  
  Wat moet ik doen om de IFix VMware backup van Heerlen in orde te krijgen.
  
  Deze draait nu sinds juni met de gratis licentie zonder dat er een backup van wordt genomen.
- # [[2019-09-18]] 
  Nog maar eens een mail naar Jef, met Harry in cc
  
  Volgende keer uitzoeken wie buiten jef kan mij helpen?
- # [[2019-10-03]] 
  Als tegenprestatie van de oude sms server, wil Jef de ESX in orde brengen.
- # [[2019-10-16]] 
  Er komt schot in de zaak
  
  [CHG0032714](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fsibelco.service-now.com%2Fnav_to.do%3Furi%3Dchange_request.do%253Fsys_id%3D857d2c511be00c1c252cea0f6e4bcb9f%2526sysparm_stack%3Dchange_request_list.do%253Fsysparm_query%3Dactive%3Dtrue&data=02%7C01%7Csilvia.odekerken%40sibelco.com%7Cd29c86e2ad7b476a5b6208d75213e979%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C637068117801253509&sdata=Qg19QKzroPFQm%2BC7Q22lAfeYlH0lyfXsQg%2BkYcA%2F%2B%2F0%3D&reserved=0) aangemaakt.
- # [[2019-11-07]] 
  Francis Somers is de man die verantwoordelijk is voor opvolging IT infrastructuur HRL
- # [[2020-02-06]] 
  Op 3/02 Silvia er nog eens op attend gemaakt.
  
  Dit was het antwoord:
  
  Hi Tonny,
  
  Ik was in de veronderstelling dat dit begin januari was afgehandeld en ik heb de aanvraag gecontroleerd en zie net dat de change is afgesloten vanwege deze reden:
  
  “We are unable to add the server to backups due to compatibility issues”
  
  Unable to add the server to backups as the ESX where the server is hosted seems to have compatibility for getting it added to the existing Vcenter.
  
  Only when added to Vcenter the backups are possible. Hence backup is not possible due to compatibility.
  
  Dat is redelijk kort door de bocht. Ik ga kijken welke andere mogelijkheden er bestaan voor het maken van een back up van deze server.
  
  Ticket is CHG0033190: IFIX (scada) server Heerlen
- # [[2020-03-06 1]] 
  Laatste boze mail gestuurd naar ICT
  
  Voor mij is dit afgesloten
- # [[2022-01-24]] 
  Nieuwe IFix is bijna klaar. Nog MES omzetten
- # [[2022-09-12]] 
  MES was gestopt. Geen reden kunnen vinden.