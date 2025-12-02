---
date created: Invalid date
modified: 2025-09-12 09:59
tags:
  - 800xA
  - dev
---
# 800xA TLib

- # [Link Nog te doen voor ontwerp](onenote:#Nog%20te%20doen%20voor%20ontwerp&section-id={CFC7F9A5-4F11-4063-BECD-A548B673DB61}&page-id={E35BE22D-1DA9-4D25-B1A5-5294C33D0B0B}&end&base-path=https://d.docs.live.net/648fe635197c5860/OneNote's/Persoonlijk%20(web)/Personal/Computer/Develop/Ontwikkeling.one)
  
  [Link Word document TLib](https://sibelco-my.sharepoint.com/personal/tonny_lemmens_sibelco_com/_layouts/15/guestaccess.aspx?guestaccesstoken=b1RwUVgC6tLyxGd0JWWtK240BuaVS2FRTyf%2b%2bteFfe0%3d&docid=2_1b09f964baf26437c826c86c9be3b9161&rev=1)
  ~~GEEN ENKEL OBJECT IN TLIB_BASIC IS ALARM-OWNER. !!!!~~ Deprecated zie [Ervaring ivm TLib K287]

## [[2013-09-08]] 8:26 
  Verder gedaan aan ontwerp.
- ### TAansturing_v2
  Afhandeling van Modes, verschillende PriorityCmds, Start stop, AutoCmd
  Kan worden gebruikt voor TValve
  Commands graphic element gemaakt (nog omzetten naar faceplate element)
  **Bezig met Priority faceplate element**
- ### TPriority
  In welke mode (man, auto, panel) is een Priority active
- ### TMotorBasic
  Motor eerst gemaakt met diagram editor :-) met compact versie.
  Omgezet naar 800xA
  Zowel een AutoCmd als (startstop)Cmds geïmplementeerd
  
  Testversie gemaakt in TTest_MotorUni_v2
## [[2018-01-09]] 
  Bovenstaand is niet meer van toepassing.
  :-)
  TLib.TValve is in productie bij LLB BU85.
  Nog een Operator Note icoon voorzien in de faceplate.
## [[2018-01-25]] 
  TSequenceInterface toegevoegd.
## [[2018-06-25]] 
  ObjectMode - functie toegevoegd. Deze zit in test in TValveBasic
  
  Ervaring ivm TLib K287
  Geëxperimenteerd met alarmen op een PP en alarmen in 800xA.
  Conclusie: Het is niet te doen om bepaalde geen alarm-owner te maken. In K287 heb ik een TValve en een TMotor zoals deze standaard in 800xA zijn voorzien. TValve en TMotor zijn beiden alarm owner. Als ik nu TValve of TMotor wil embedden in een ander object (bijvoorbeeld TValve_HMI of TMotor_HMI), dan worden alamen altijd gerefereerd aan de originele TValve of TMotor.
  Als er een Alarm-Owner embedded is in een ander Object, dan mag de alarm-owner geen aspect object zijn. Gevolg alle grafische koppelingen gaan verloren. Dus moet er op het bovenste niveau telkens grafische koppeling zijn
  Totdat er andere inzichten zijn: Beter om een THMI bibliotheek te voorzien.
## [[2018-07-04]] 
  THMI bibliotheek afgevoerd.
  Het is te complex om deze te scheiden omdat alle signalen moeten worden doorgesluist
  
  In TValve en TMotor zit nu geen code en zijn beiden alarm owner. En mogen dus niet worden embed in een ander object.
## [[2018-07-10]] 
  zie [TLibGraphics](onenote:#TLibGraphics&section-id={CFC7F9A5-4F11-4063-BECD-A548B673DB61}&page-id={E5A50DBC-B042-4F5E-835B-1C4ADDC1BA47}&end&base-path=https://d.docs.live.net/648fe635197c5860/Docs/OneNote's/Persoonlijk%20(web)/Personal/Computer/Develop/Ontwikkeling.one)
## [[2018-07-11]] 
  Probleem met MotorBi. Bij een start of stop werd IO.Out1 pas de volgende cyclus geüpdate
  
  Daarom Out1 en Out2 op nosort gezet. 
  Dit gaf een code-sort-loop op werkschakelaar.
  
  In Basic wordt Out1 en Out2 geschreven en Werkschakelaar gelezen.
  In IO wordt Out1 en Out2 gelezen en Werkschakelaar geschreven.
  
  =\> Oplossing: een extra CM (Werkschakelaar_IO) die voor Basic en IO wordt uitgevoerd.
  
  Er moet voor werkschakelaar een extra beveiliging worden ingebouwd omdat bij een cold-restart, werkschakelaar = 0.
  Dit resulteert in een OOS bij Basic
## [[2018-11-17]] 
  [TDrive](onenote:#TDrive&section-id={CFC7F9A5-4F11-4063-BECD-A548B673DB61}&page-id={BB8FA2D7-DC0C-4AF8-9A6D-FDB32F57A36A}&end&base-path=https://d.docs.live.net/648fe635197c5860/Docs/OneNote's/Persoonlijk%20(web)/Personal/Computer/Develop/Ontwikkeling.one)
## [[2022-02-04]] 
  Test Procedure
  1\. Zet FB1 = 0 (Out1=0)
  2\. Zet FB1 terug op 1
  3\. =\> Out1 zal terug op 1 komen. DIT MAG NIET
  
  Er is al voorbereiding gebeurd om dit op te lossen
  
  Er is een extra “Start_Stop_FB” toegevoegd
  
  TODO:
  • Verwijder bij StartStop_FB bij Set: de StartStop.Q1
  • Verwijder StartStop_FB1_Q := StartStop.Q1
  
  TEST WAT ER GEBEURD BIJ EEN DRAAIENDE MOTOR ALVORENS TE DOWNLOADEN NAAR EEN INSTALLATIE
  Dit is aangepast in versie 4 van T-Bibliotheken