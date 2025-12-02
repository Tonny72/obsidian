---
created: [[2019-07-01]]T08:28:32.0000000+02:00
tags:
  - Siemens
---
# [[2019-10-17]] 
  Offerte naar Harry gestuurd
# [[2020-01-06]] 
Task naar Outlook verhuist
  
  **-----------------------------------------------**
  
  **From:** steven.thielemans@siemens.com \<steven.thielemans@siemens.com\>
  **Sent:** Wednesday, 5 June 2019 18:58
  **To:** Tonny Lemmens \<Tonny.Lemmens@sibelco.com\>
  **Cc:** gunther.busschots@siemens.com
  **Subject:** Vragen in verband met schermen overnemen
  
  Dag Tonny,
  
  In navolging van de meeting over het overnemen van verschillende panels waren er nog enkele zaken die openstonden:
  
  Prioriteit op smart viewer:
  Qua prioriteiten enzoverder zijn de mogelijkheden niet echt uitgebreid. Men kan in de smartserver settings kiezen voor"*Disconnect existing connections" /"Automatic shared sessions" /"Refuse concurrent connections"* bij het opkomen van een nieuwe connectie. Ook kan men kiezen of local input mogelijk is indien er een smarclient connectie is. Hierdoor krijg je wat beperkingen langs de kant van de panel maar deze gelden dan voor al de connecties
  Langs de smartclient zijde kan men ook kiezen of de sessie '*Shared'*mag zijn of niet. Zo kan men vermijden dat er meerdere sessies tegelijk opstaan.Als Engineering bijvoorbeeld overneemt kan men kiezen om de sessie niet te sharen waardoor je er toch doorkomt. Indien dit van crusiaal belang is wil ik het gerust eens testen wat en hoe er mogelijk is.
  
  Operator busy signal:
  Naargelang de bovenstaande keuzes: kan local input ook worden uitgeschakeld. (fysische)
  Signaal van read only access krijg je automatisch als er iemand het paneel al aan het bedienen is.
  
  Hoeveel panels maximum in 1 Runtime Advanced.
  Ik vind hier ook niet meteen documentatie over. Volgens onderstaand topic zou 4 connecties het maximum zijn:
  [https://support.industry.siemens.com/tf/WW/en/posts/maximum-number-of-connected-clients-sm-rtclient-to-sm-rtserver/144785?page=0&pageSize=10](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fsupport.industry.siemens.com%2Ftf%2FWW%2Fen%2Fposts%2Fmaximum-number-of-connected-clients-sm-rtclient-to-sm-rtserver%2F144785%3Fpage%3D0%26pageSize%3D10&data=02%7C01%7Ctonny.lemmens%40sibelco.com%7C3b4a35df5ebe48eb0abf08d6e9d6eac2%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C636953506627558136&sdata=R4Qe%2FuvqFOa0O%2FTxhBy2U1pvpwbfTuE72XCTNE3i3ls%3D&reserved=0)
  Maar ik vermoed dat het te maken heeft met de maximaal gelijktijdige connecties want configureren kan je er meer.
  Hoeveel panels kan ik ovenemen met de WinCC Prof?
  Dit kan in de Runtime professionel zelf niet rechtstreeks doen omdat deze op een andere manier werkt.
  Wat men wel kan is met een script in RT professional de smartclient.exe openen die dan bovenop de runtime komt. Men kan dan bij het oproepen een aantal parameters meegeven zoals connection IP. (idem V7) Men kan van deze applicatie ook meerdere instanties tegelijk oproepen.
  Hier zit je dus niet met de beperking van de voorconfiguratie aangezien je slechts 1 smartclient.exe hebt die je telkens met andere parameters gaat oproepen.
  Beperking in beide situaties: (zoals reeds gemeld)
  Per panel kan men steeds maar 1 beeld zien. Wanneer men ergens (waar dan ook) een beeldwissel uitvoert wordt op alle smartclients en de panel zelf het beeld gewisseld.
  Kopieren van een beeld uit en een project en de tags opnieuw gebruiken is wel mogelijk, hou dan wel rekening met het aantal PLC connecties
  8 voor Runtime Advanced
  256 (max 128 S7-300) voor Runtime Professional
  Grootste voordeel is natuurlijk bij Runtime Professional dat alle tags indivudeel worden uitgelezen (zonder overnemen van het scherm).
  \- Operator kan gewoon doorgaan met zijn scherm
  \- Intern kunnen verschillende mensen in het labo andere schermen zien van 1 installatie.
  Als je toch graag liever eens de functionaliteiten test of een opstelling zou zien, laat het dan zeker weten.
  Dan kunnen we samen bekijken wat er mogelijk is om een werkbare oplossing te vinden.
  Met vriendelijke groeten,
  Steven Thielemans
  
  Siemens S.A./N.V.
  RC-BE DI S-AREA NORTH
  Guido Gezellestraat 123
  1654 Beersel, Belgium
  Mobile: +32 476997208
  [mailto:steven.thielemans@siemens.com](mailto:steven.thielemans@siemens.com)
  [www.siemens.be](https://eur01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.siemens.be&data=02%7C01%7Ctonny.lemmens%40sibelco.com%7C3b4a35df5ebe48eb0abf08d6e9d6eac2%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C636953506627558136&sdata=et4W%2BL01xFT5UatL2exN9vf5OF1NRokXTkSOPt3UM6w%3D&reserved=0)
  [www.siemens.com/ingenuityforlife](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fsiemens.com%2Fingenuityforlife&data=02%7C01%7Ctonny.lemmens%40sibelco.com%7C3b4a35df5ebe48eb0abf08d6e9d6eac2%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C636953506627568126&sdata=gW%2Bd0KPg3CMBvPoQdO6c8ZHNyhcFXHyA0gPfpXN2yzA%3D&reserved=0)
  ![image1](image1-12.gif)
  Maatschappelijke zetel / Siège social : Siemens NV/SA, Guido Gezellestraat 123, 1654 Beersel. RPR Brussel / RPM Bruxelles, BTW/TVA BE 0404.284.716, Erkenningsnummers/Numéros d’agrément: Beveiligingsonderneming/ Entreprise de sécurité - 20 1321 06, Onderneming voor veiligheidsadvies/ Entreprise de consultance en sécurité – 128533., BNP Paribas Fortis BE52 2100 0409 8809, BIC: GEBABEBB, Deutsche Bank BE70 8260 0046 6425, BIC: DEUTBEBE, EORI-nummer/Numéro
  [00043921-V01.pdf](assets/pdf/00043921-V01.pdf)
  
  ![image2](image2-43%201.png)![image3](image3-27%201.png)![image4](image4-16%201.png)![image5](image5-12%201.png)![image6](image6-11%201.png)![image7](image7-8%201.png)![image8](image8-5%201.png)
  ![image9](image9-5%201.png)