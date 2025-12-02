---
title: K287 - Openstaande punten K287
updated: [[2021-06-17]]T13:58:06.0000000+02:00
created: [[2020-02-26]]T09:40:29.0000000+01:00
---

- # ONTWERP
  IP PLC 10.32.8.80
  
  IEI touch screen : be-287-plt-001 (resolutie 1920x1080)
  
  Eng pc: be-287-plt-002
- #
- # AFZUIGING
  | DO3.19 | AFZ_FREQ_DO  | Aansturing contactor K4 (freq stur) | NODIG (AFZ_FREK_K4_DO)  |
  |--------|--------------|-------------------------------------|-------------------------|
  | DO3.20 | STT_AFZ_DO   | Start freq. sturing                 | NODIG (AFZ_FREK_STT)    |
  | DO3.21 | STT_AFZV1_DO | Start freq. Sturing v1              | Niet gebruikt bij laden |
  | DO3.22 | STT_AFZV2_DO | Start freq. Sturing v2              | NODIG (AFZ_SNELH2)      |
  | DO3.23 |             | Afzuiging filter                    | NODIG (AFZ_FILT_DO)     |
  | DO3.24 | AFZ_KL3_DO   | Hoofdafzuigkl KL3                   | NODIG (AFZ_KL3_DO)      |
  | DO3.25 | AFZ_KL2_DO   | Aanst afz silo2 KL2                 | Niet gebruikt bij laden |
  | DO3.26 | AFZ_KL4      | Aanst raco zandkl S1-2 KL4          | Niet gebruikt bij laden |
  | DO3.27 | AFZ_KL1_DO   | Aanst afz silo2 KL1                 | Niet gebruikt bij laden |
- # TODO's
- ## Hydroliekpomp blijft te lang draaien / Hydroliekpomp komt soms niet op.
  In Unit_Silos debug code toegevoegd.  
  Getest met Silo3. In Silo blijft Losklep_IO_Internal.Out1.Value hoog tijdens het laden.
- ## LA_KL22 blijft open
  Mogelijk met hydroliekpomp te maken? Dit moet getest worden als men laadt uit deze silo.
- ## Volgwagen 3x claxon
  Dit is aangepast. Testen!
- ## LO_KL4 gaat niet open
  Bij het lossen naar Silo2 gaat deze klep niet open
- ## BE-287-DSK-001
  Runtime installeren
  
  [[2021-06-17]] : Dit lukt niet
- # Controle draadloze module
  Wat gebeurt er als de draadloze module uitvalt =\> Volgwagen blokkeren
- ## Perslucht werkt niet
  Controlleer werking perslucht-klep.
  
  DO800_6.5 PDZ_KL =\> Zie Laden_Algemeen
  
  Manuele knoppen Silo12_4 werken niet
  
  Knoppen voor manuele bediening werken niet.
- # Lamp lossen via B2A (DO3.15)
  Wordt deze nog gebruikt?