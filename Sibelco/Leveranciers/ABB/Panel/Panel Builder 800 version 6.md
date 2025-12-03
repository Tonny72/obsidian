---
tags: [panel_builder]
date created: 2025-12-03T07:26:03+01:00
  - - 2014-11-27
date modified: 2025-12-03T10:35:06+01:00
---

- # Openen Project
- # Aanmaken van Tags
  Er is aan de Rotoseal een PP874 Process Panel in dienst.
  
  Om een tags aan te maken klik bij Functions op Tags
  ![image1](image1-510.png)
- #
- # Verbinding met met Kepware OPC UA server
  Voeg een controller toe
  ![image2](image2-200.png)
  
  Voeg een tag toe
  ![image3](image3-120.png)
  
  The Tag ID, in the example above, corresponds with BrowseName in the OPC UA server.
  Dus enkel de **BrowsName gebruiken**
- # Alarm Afhandeling
  Zoektocht om zowel 800xA alarmen als Panelbuilder Alarmserver te gebruiken
  Koppel 2 signalen: AlState en AEAck
  ![image4](image4-86.png)