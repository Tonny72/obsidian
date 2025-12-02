---
title: Play knop - Lab dispatcher
updated: [[2020-06-04]]T09:29:51.0000000+02:00
created: [[2020-05-29]]T11:25:00.0000000+02:00
---

| **Subject** | **ABB Tags**             |
|-------------|--------------------------|
| **From**    | Jochem Janssen           |
| **To**      | Tonny Lemmens            |
| **Cc**      | Stijn Vandenbroucke      |
| **Sent**    | maandag 25 mei 2020 9:52 |

Hey Tonny,

Wanneer past het voor u om eens te kijken naar die ABB Tags voor manuele staalaanvraag Rosa?
Je weet wel, die groene ‘Play’ knopjes bij de Lab Dispatcher die de staalaanvraag triggeren.
Dit heeft gewerkt, maar om 1 of andere reden nu niet meer.

Heb je verder nog iets gehoord van de contactpersoon van ABB i.v.m. de connectie issues op de Tags / redundantie server?
Wat zijn de volgende stappen? Hoe kunnen we dit voor eens en voor altijd oplossen?

Met vriendelijke groeten,
****

- # [[2020-06-03]]
- # <http://be-des-aps-020:59160/?module=tagoverview>
  
  | DISPATCHER_SA802_SAMPLE_STATUS | opc.tcp://10.32.29.60:59151 | NS2\|String\|800xA.Dispatcher.C3_Lab.SA802.DIS_Staal_Status | 0   |    |
  |--------------------------------|-----------------------------|-------------------------------------------------------------|-----|-----|
  | DISPATCHER_SA803_SAMPLE_STATUS | opc.tcp://10.32.29.60:59151 | NS2\|String\|800xA.Dispatcher.C3_Lab.SA803.DIS_Staal_Status | 0   |    |
  | DISPATCHER_SA804_SAMPLE_STATUS | opc.tcp://10.32.29.60:59151 | NS2\|String\|800xA.Dispatcher.C3_Lab.SA804.DIS_Staal_Status | 35  |    |
  
  *SA 802, 803, 804*
  
  Mail verstuurd
  Dag Stijn,
  
  Ik ben aan het nakijken waarom het play-knopje op het scherm van de labdispatcher niet werkt.
  
  Ik vermoed dat er verkeerde tags zijn gekoppeld.
  
  Wordt ‘Take Sample’ eigenlijk gebruikt? Of is het enkel ‘Sample Status’ = 40 voor het nemen van een staal.
  
  ![image1](image1-85%201.png)
  
  Mvg
  
  Tonny
- # [[2020-06-04]] 
  Dit is aangepast.
  Jochem gaat dit testen