---
title: Heranalyse trigger vanuit ABB
updated: [[2019-06-13]]T08:53:42.0000000+02:00
created: [[2019-06-11]]T14:44:22.0000000+02:00
---

Aanvullend.

Iedere staalnemer heeft een status, die status wordt geschreven door Dispatcher.
De mogelijke codes zijn:

 public const int STATUS_SAMPLE_OK = 35; -\> wordt geschreven wanneer een pot van het staalstation binnenkomt en de pot is ok
 public const int STATUS_SAMPLE_NOK = 40; -\> wordt geschreven wanneer een pot van het staalstation binnenkomt en het staal wordt geannuleerd
 public const int STATUS_RESAMPLE = 45; -\> manuele knop op het Dispatcher scherm om staalname te triggeren

De status wordt op 0 gezet wanneer de robot op zijn entry positie komt (met name: net voor hij de pot opneemt).

In geval van NOK zou er dus een herstaal moeten genomen worden.

Let wel: wanneer er X stalen na elkaar worden afgekeurd, dan moet de staalname voor die staalnemer stoppen (+ zichtbaar op de staalnemer in ABB op het Rosa overzicht).
Anders komt de staalnemer in een eindeloze lus.

Gr, Stijn.

**Van:** Jochem Janssen \<<Jochem.Janssen@sibelco.com>\>
**Verzonden:** donderdag 6 juni 2019 12:20
**Aan:** Tonny Lemmens \<<Tonny.Lemmens@sibelco.com>\>
**CC:** Stijn Vandenbroucke \<<stijn.vandenbroucke@linkworx.eu>\>
**Onderwerp:** Heranalyse trigger vanuit ABB

Tonny,

EMDE: Zak 5 (1e staal = 20190606-0166), hoogtedetectie NOK -\> Parameter Groepen die niet kunnen geanalyseerd worden, die worden gecancelled.
De overgeërfde resultaten van Bulk blijven wel behouden (o.a. chemie).

![image1](image1-15.jpg)

Stel: 2e staal (zak 15) is <u>ook</u> NOK o.w.v. hoogtedetectie. Dan hebben we vandaag dus een groot probleem.
Namelijk dat Unilab zal zeggen (nadat lot end date ontvangen wordt): Voila, ik ben klaar, reken lot maar uit.
D.w.z. dat lot Approved zal worden, MAAR dat de klant geen Kleur, Darkspots, Trilzeef analyses op z’n CoA zal krijgen te zien en dus een klacht zal sturen.
Als die BB’s verladen zijn, dan nog een herstaal gaan pakken wanneer ze intussen bij de klant zijn, is helemaal miserie…

Kunnen we, in geval van EMDE (SA801), én hoogtedetectie NOK, onmiddellijk een herstaal aanvragen van eerstvolgende BB van datzelfde lot?
Hetzelde in geval staal kwam van SA802-SA803-SA804.

Mvg,

**Jochem Janssen**
Reliability Engineer

- # [[2019-06-11]] 
  Staalname voor SA801, SA802, SA803, SA804 wordt herbekeken.
  
  Een deel van Diagram-Code voorbereid naar ST-code. Pas terug oprakelen als C3 terug draait