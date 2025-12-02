---
title: Ombouw LLZ2
updated: [[2022-01-20]]T09:12:31.0000000+01:00
created: [[2018-10-10]]T08:48:43.0000000+02:00
---

Ombouw LLZ2
woensdag 10 oktober 2018
8:48

- # [[2018-10-10]] 
  6 di kaarten besteld
  ![image1](image1-48%201.png)
  
  ![image2](image2-30%201.png)
- # TODO
- ~~In seq. ILock1 aanpassen zodat de sequentie niet kan worden gestart als er wordt overgetapt.~~
- ~~In LLZ start van ZAF1 koppelen aan IAC_LLZ_TO_LLZ.ZAF1_Start~~
- ~~In laadterminal de tags aanpassen om te laden~~
- ~~AF5_LSH5 mag weg~~
- Indien geen OPC verbinding, rode kruisen tonen adv DataQuality
- ~~In LLZ Units zijn LLZ2 en OVT zijn geen aspects objects meer. Deze nog volledig verwijderen~~
- ~~In LLZ Sequenties LLZ2_SEQ is geen aspect object meer. Deze nog verwijderen~~
- Force IO nog op alarmbar van motorBI
- ~~Vergrendeling op ZS58 door vrijgave loadingApp~~
- TValve Tag : CfgStatusBoxVisible standaard op false zetten
- ~~Verwijderen uit Advant LZ2_ZS41 - \> LZ2_ZS51~~
- ~~reset tijd verlengen voor remote start stop cmds~~
- # DONE tijdens ombouw
- ~~In de seq D4_SEQ hernoem de .par van de kleppen en motoren en vervang de transities in de sequentie~~
- ~~In Droger_4 - Communicatie_IAC - IAC_LL2 Poc koppelen. (deze is nog niet ingevuld om communicatie te kunnen testen)~~
- # Oude IO
  ![image3](image3-19%201.png)
  
  ![image4](image4-11%201.png)
  
  ![image5](image5-9%201.png)