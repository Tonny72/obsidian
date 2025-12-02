---
title: Property transfer aspect  (CounterWatchdog)
updated: [[2016-03-18]]T07:53:06.0000000+01:00
created: [[2014-04-30]]T15:41:28.0000000+02:00
---

Om in de controller connectie met 800xA te verifieren wordt het Property Transfer aspect gebruikt.

*Control Module Type SibelcoCommonLib2.800xAConnectionWatchog gemaakt.*
NIET VERGETEN Property Transfer Definition Disable en Enable Transfer te doen

![image1](image1-173.png)

- # Property Transfer Service
  In de service structure voeg bij Property Transfer, Service een Service Group toe.
  
  ![image2](image2-97.png)
  
  Selecteer het Service Group Definition Aspect en klik op **Add**
  
  ![image3](image3-53.png)
  
  Voeg twee Service Providers toe.
  
  Selecteer een Service Provider en klik View.
  Koppel de Service provider aan een Server (800 connectivity server)
  ![image4](image4-30.png)
- # Property transfer
  Om waarden van 800xA naar de AC800M te sturen, moet het property transfer aspect worden toegevoegd.
- ## Voorbeeld CounterWatchdog
  Maak een variable 'CounterWatchdog' aan in Counter Builder.
  Voeg op dezelde plaats in de Control Structure een 'Property Transfer Definition' aspect toe.
  
  ![image5](image5-25.png)
  
  Er wordt van de Expression naar de Aspect/Property geschreven.