---
title: Programmeren SVA605_A en SVA605_B
updated: [[2015-01-09]]T14:03:34.0000000+01:00
created: [[2015-01-09]]T14:02:28.0000000+01:00
---

- # [[2015-01-09]] 14:03 
  Tonny, graag programmatie aanpassen voor de ventielen.
  De ventielen zijn geplaatst, aangesloten en getest.
  De sturing dient nog softwarematig aangepast te worden...
  Huidige situatie zit zo:
  
  SVA605_A = zorgt voor glandwater naar Zuiger Limburg
  SVA605_B = zorgt voor glandwater naar Zuiger Ina
  
  Vanuit ruststand
  SVA605_A -\> OPEN
  SVA605_B -\> GESLOTEN
  
  \- Voor glandwater naar Zuiger Limburg
  -\> SVA605_A openen
  -\> SVA605_B sluiten (is al gesloten in ruststand)
  
  \- Voor glandwater naar Zuiger INA
  -\> SVA605_A Sluiten
  -\> SVA605_B openen
  
  Wat momenteel mogelijk is en niet zou mogen is dat beide ventielen tegelijk bedient kunnen worden...dit resulteert tot het blijven staan van de ventielen in hun laatste stand
  
  Zo te programmeren dat we met een puls werken van 2 seconden.
  
  DWZ 
  puls vanuit DO12 (C1.1.10.4) zal SVA605_A Doen openen & SVA605_B Doen Sluiten
  
  puls vanuit DO16 (C1.1.10.4) zal SVA605_A Doen Sluiten & SVA605_B Doen Openen
  
  De as-built schema's volgen nog
  
  Harry, motor van de zuigbuislier is enkel getest voor te halen en te vieren, noodstop is nog niet getest en de motor zal mechanisch een kwart gedraaid worden zodat de kabelinvoer correct komt te staan