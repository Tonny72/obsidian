---
title: Probleem Bigbag zand, Sequentie blijft hangen in s...
updated: [[2017-10-10]]T12:53:22.0000000+02:00
created: [[2016-10-10]]T09:14:29.0000000+02:00
---

Probleem Bigbag zand, Sequentie blijft hangen in stap1  
Toevoer BBZ (AF8)
maandag 10 oktober 2016
09:14
Het paneel van BB zand wordt aangestuurd door de plc boven.

Het Control Builder project staat onder:
M:\OnderHd\Elektrische dienst\Private\ABB\ABB Control IT Projects\Afzakinstallatie_Alg

In Program2 staat een Tab met AF8_Seq_Toev_BB. Dit is de sequentie zie Figuur 1.

In stap1 (AF8_Filter) wordt de filter gestart. =\> AF8_FGST_DO (.1.2.2.2).

Deze DO stuurt DI800_16.10 (AF5_FGST_BB) van Advant PLC Sibelco aan.

![image1](image1-186.png)

**

- #