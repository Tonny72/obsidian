---
created: [[2020-01-06]]T11:06:34.0000000+01:00
tags:
  - FFS
---

| **Onderwerp** | **FFS - Pallet labelaar**                                     |
|---------------|---------------------------------------------------------------|
| **Van**       | [Stijn Vandenbroucke](mailto:stijn.vandenbroucke@linkworx.eu) |
| **Aan**       | Kurt Regout; Tonny Lemmens                                    |
| **Cc**        | Harry Stienen; Mike Van de Put; Jochem Janssen                |
| **Verzonden** | vrijdag 6 december 2019 15:16                                 |
| **Bijlagen**  | [IMG_7014.jpg](IMG_7014.jpg)                                          |

Kurt, Tonny,

Zonet bij de pallet labelaar van [[network/des/Siemens Devices/from_word/FFS]] geroepen: de arm van de labelaar staat uit zonder dat er een pallet in de buurt is (zie bijlage).
Dit zou een scenario zijn dat zich regelmatig voordoet bij kwaliteitswissel.

Scenario:

- Labelaar wordt in bypass gezet
- Niet afgewerkte pallet van vorige kwaliteit wordt afgevoerd
- Labelaar wordt terug in run gezet
- De eerste pallet van de volgende kwaliteit lijkt pas een label aanvraag te doen wanneer de pallet voorbij de labelaar is of gaat
  Gevolg: de arm van de labelaar gaat naar buiten zonder dat er een pallet in de buurt is. De arm blijft buiten staan tot iemand ingrijpt.
  In het laatste geval mag er geen beweging zijn van de rolbaan, gezien de labelaar geen vrijgave signaal geeft.
  
  De programmatie zou zo moeten zijn, dat een niet volledig pallet sowieso niet gelabeld wordt. De labelaar in bypass zetten zou sowieso al niet nodig moeten zijn.
  Daarnaast zou de pallet nooit mogen doorgaan zonder label, wanneer er een label aanvraag werd gedaan.
  
  Mogelijks is het niet zinvol om dit nu nog te bekijken, maar dit dient meengenomen te worden op het ogenblik dat de labelaars aangepast worden.
  Zou het kunnen dat de hoogtedetectie op de verkeerde pallet werkt? En vandaar dat de eerste van de volgende kwaliteit doorgaat zonder op een label te wachten?
  
  Gr, [[Stijn Vandenbroucke]].