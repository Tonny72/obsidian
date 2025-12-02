---
title: 'Opvolging MES - ABB Communicatie '
updated: [[2022-01-21]]T13:42:32.0000000+01:00
created: [[2019-05-14]]T14:00:27.0000000+02:00
---

- # [[2019-04-23]] 
  ------------
  
  **Van:** Stijn Vandenbroucke \<<stijn.vandenbroucke@linkworx.eu>\>
  
  **Verzonden:** dinsdag 23 april 2019 21:56
  
  **Aan:** Jurgen Smolders; Nico Gerinckx; Tonny Lemmens; Harry Stienen
  
  **CC:** Mike Van de Put; Geert Staes; Jochem Janssen; Stef Valkiers
  
  **Onderwerp:** 21/04 ABB-MES communicatie
  
  **Opvolgingsvlag:** Flag for follow up
  
  **Vlagstatus:** Met vlag
  
  Allen,
  
  Zondagavond is de communicatie tussen MES en ABB uitgevallen.
  
  Oorzaak is niet echt bekend, ik heb gevraagd aan Tonny om uit te zoeken aan ABB kant wat er kan gebeurd zijn.
  
  Het feit is dat dit 1x om de zoveel maand blijft voorvallen.
  
  Wat jammer blijft, is dat de operatoren dit niet vaststellen.
  
  Eigenlijk zijn er twee manieren waarop dit vrij makkelijk vast te stellen is:
- Er komt geen enkele ton meer bij op géén enkel workcenter (dus ton/h volgens MES zal sterk dalen na enkele uren)
- Maar vooral: er komen onterechte stilstanden! Deze zouden een belletje moeten doen rinkelen…
  
  <u>Volgende acties:</u>
- [@Tonny Lemmens](mailto:Tonny.Lemmens@sibelco.com): eventueel simuleren met test omgeving?
- [@Tonny Lemmens](mailto:Tonny.Lemmens@sibelco.com): watchdog staat al tijdje als apart proces op de server
- [@Jurgen Smolders](mailto:Jurgen.Smolders@sibelco.com)/[@Nico Gerinckx](mailto:Nico.Gerinckx@sibelco.com): instructie operatoren zodat ze asap melding maken van dergelijk voorval
- [@Jurgen Smolders](mailto:Jurgen.Smolders@sibelco.com)/[@Nico Gerinckx](mailto:Nico.Gerinckx@sibelco.com): stilstanden corrigeren ifv rapporten
- [@Harry Stienen](mailto:Harry.Stienen@sibelco.com): het heeft enkele uren geduurd vooraleer Emde terug operationeel was, om 2 redenen:
- Gebrek aan kennis van de installatie (en Murphy heeft ervoor gezorgd dat Jochem er niet was)
- Het feit dat de communicatie van de weegsilo over ABB loopt
  
  ð Alle communicatie met Siemens PLC’s is stabiel gebleven in deze periode, ook Rosa (waar een pak meer communicatie is) is perfect haar ding blijven doen
  
  ð De zoektocht naar de diepere oorzaak binnen ABB wordt iedere keer aangezwengeld na een incident, maar komt steeds weer op een dood spoor…
  
  *Vandaar:*
  
  1) Is er zicht op kostprijs Emde om de communicatie over te nemen ifv pallet opvolging vanaf weegsilo?
  
  2) Wie kan er iemand binnen ABB contacteren zodat dit (terugkerend) issue te gronde kan bekeken worden?
- # [[2020-01-06]] 
  Task in Outlook gezet