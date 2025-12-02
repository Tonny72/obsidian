---
title: Uitval C3 oven
updated: [[2018-05-04]]T16:30:57.0000000+02:00
created: [[2018-05-04]]T13:12:11.0000000+02:00
---

- # [[2018-05-04]] 
  Zonet is de oven uitgevallen door mij.
  
  Maar wat is er gebeurd.
  Dit is het programma:
  
  ![image1](image1-202.png)
  
  Ik heb variabele IO.BE601_00_PB gekoppeld aan de hardware op onderstaande plaats
  
  ![image2](image2-114.png)
  
  Dit was nodig omdat het signaal van de toerenwachter niet binnen kwam.
  
  Hier door komt er een '1' van de PB_CONV op .DI1. Dit is het signaal van de werkschakelaar.
  Maar deze blijkbaar nog geïnverteerd worden.
  
  Zie programma van de C3_BE103_00 waar het wel goed is.
  
  ![image3](image3-66.png)
- # Conclusie 
  De werkschakelaar is nooit getest geweest.m