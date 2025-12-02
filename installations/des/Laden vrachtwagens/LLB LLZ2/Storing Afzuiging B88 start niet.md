---
title: 'Storing: Afzuiging B88 start niet'
updated: [[2012-12-04]]T15:26:52.0000000+01:00
created: [[2012-12-04]]T14:51:47.0000000+01:00
---

Laadsequentie LLB5:PC1.18 stap1
Start Afzuiging MS88 pc1.18.1.1:20 -\> pc1.19.1.1:3 -\> pc1.19.1.1:23 -\> DAT LLB5 S_SIB5.B2:value2 -\> DAT Sibelco R_LLB5.B1:value2 -\> pc14.7.8.2:8 -\> pc14.7.8.2:28 -\> DAT Sibelco S_M3_2.B1:value2 -\> Molen3 -\> M3_101a (Filter MS88) en M3_101b (Filter mek. MS88)

Via Forces value in LLB5 gesimuleerd of afzuiging start -\> Geen probleem.

Indien probleem zich nog eens voordoet:
1.  Is er een vrijgave bij lossen bunkers
2.  Connect met LLB5 pc1.3.5.1 en zie of de vrijgave daar binnen komt.
3.  Zie in pc1.18:pos in welke stap de sequentie staat
4.  Start in 800xA de M3_101a en M3_101b manueel
5.  Zie wat er verder gebeurt.
