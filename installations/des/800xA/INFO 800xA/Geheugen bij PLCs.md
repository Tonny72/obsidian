---
title: Geheugen bij PLCs
updated: [[2013-04-11]]T09:14:42.0000000+02:00
created: [[2013-03-25]]T12:21:54.0000000+01:00
---

- # [[2013-04-11]] 9:14 
  Er is een case aangemaakt bij ABB
- # [[2013-04-03]] 9:12 
  Geen antwoord ontvangen
  Nogmaals mail gestuurd
  
  Hennie,
  
  Engelbert,
  
  Hebben jullie nog iets vinden waarom de Compiler statistics in Control Builder maar enkele van de applicaties laat zien.
  
  Ik heb de indruk dat nieuw aangemaakte applicatie wel goed getoond worden. Misschien heeft het iets met de upgrade te maken.
  
  ![image1](image1-167.png)
- # [[2013-03-25]] 14:01 
  Mail naar ABB gestuurd waarom de Compiler Statistics maar 5 apps laat zien.
- # [[2013-03-25]] 12:23 
  Naar aanleiding van het geheugen probleem bij de controller van M3, wat opzoekingen gedaan.
  
  =\> Zie [Conclusie](onenote:#Geheugen%20bij%20PLCs&section-id={3F60D0C4-1F99-4A13-B691-FF9A31D292D6}&page-id={A4DAE379-31BC-4E1E-82D6-B8CB0D7175B9}&object-id={4E897957-5A90-091A-3E46-141FB9A22776}&A2&base-path=H:\Public\Planning\Tonny%20Planning\TODO's.one)
  
  [Compiler Statistics.pdf](Compiler_Statistics.pdf)
  [Task Execution en Offset.pdf](Task_Execution_en_Offset.pdf)
  [Memory Usage per Component.pdf](Memory_Usage_per_Component.pdf)
  
  Applicatie memory gebruik:
  
  ![image2](image2-4.gif)
  
  ![image3](image3-49.png)
  
  ![image4](image4-1.gif)
  
  ![image5](image5.gif)
  
  Controller memory gebruik:
  
  ![image6](image6.gif)
  
  ![image7](image7-1.gif)
  
  ONLINE:
  
  ![image8](image8.gif)
  
  ![image9](image9.gif)
  
  Molen3 (PM861)
  ![image10](image10-1.jpg)
  Hydro (PM866)
  ![image11](image11.jpg)
  Droger3 (PM861)
  ![image12](image12.jpg)
  Silo’s (PM861)
  ![image13](image13-1.jpg)
  Molen6 7 (PM861)
  ![image14](image14-1.jpg)
  
  Molen5
  ![image15](image15-3%201.png)
- # Conclusie
  De SibMotorUni en de SibRealIn zijn objecten gebouwd op de standaard bibliotheek en deze gebruiken vrij veel geheugen.
  Standaard best PM864 controller kopen. Deze heeft 3x zoveel geheugen als een PM861.
  
  Of eventueel zelf een bibliotheek te maken die veel efficienter is. Enfin met minder alarm functie blocks. HH, H, L, LL
  Een AlarmCond FB neemt 1.9kB in beslag. En zo zitten er 6 in een SignalRealIn =\> 11.4kB
  
  Prijs PM861 = 5519€
  Prijs PM864 = 9546€