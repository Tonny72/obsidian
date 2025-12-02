---
title: Aanpassing AF11
updated: [[2018-10-08]]T14:57:19.0000000+02:00
created: [[2018-10-08]]T14:34:31.0000000+02:00
---

- # Probleem
  SC232 komt altijd vast te zitten
  
  ![image1](image1-47%201.png)
  
  Na controle in programma bleek dat SVA201 al in stap5 wordt open gestuurd, en pas in stap151 wordt SC232 gestart.
- # Aanpassing in sequentie
- ## Stap5 
  sequentie AF11_SEQ_BM101_Vuller wordt SVA201 niet meer open gestuurd.
- ## Stap151
  ![image2](assets/images/image2-29%201.png)
- ## Stap155
  ![image3](image3-18%201.png)
- ## Stap156
  ![image4](image4-10%201.png)
- ## Stap161
  ![image5](image5-8%201.png)
- ## Stap162
  ![image6](image6-8%201.png)
- ## Stap164
  ![image7](image7-5%201.png)