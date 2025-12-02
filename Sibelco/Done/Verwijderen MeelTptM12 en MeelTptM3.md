---
title: Verwijderen MeelTptM12 en MeelTptM3
updated: [[2018-12-07]]T09:17:29.0000000+01:00
created: [[2018-11-13]]T08:01:39.0000000+01:00
---

> Verwijderen MeelTptM12 en MeelTptM3
dinsdag 13 november 2018
8:01

In MeelTptM12 en MeelTptM3 zit geen nuttige code =\> Verwijderen

- ##
- ## In Molen1_2.MeelTptM12
  
  Bevat 1 control Module Communicatie van SibMeelTptM12
  
  Variabelen:
  
  | MMS_From | MMS_TO_MeelTptM12 | retain |
  |------------------|---------------------------|--------|
  | Par      | Par_MeelTptM12            | retain |
  
  In MMS_TO_MeelTptM12 zit
  | M5        | MMS_M5_TO_MeelTptM12         | retain |
  |-------------------|--------------------------------------|--------|
  | MeelTptM3 | MMS_MeelTptM3_TO_MeellTptM12 | retain |
  | MT        | MMS_MT_TO_MeellTptM12        | retain |
- ## Uit Molen5 communicatie MMS_M5_TO_MeelTptM12 verwijderd
  
  (\* deleted [[2018-11-12]] tl
  MMS_M5_TO_MeelTptM12.MT_MS1_O\_DI := BS_S\_M4M5_3\_B3.value20; (# Klep MS1 is open \#)
  MMS_M5_TO_MeelTptM12.MT_MS2_O\_DI := BS_S\_M4M5_3\_B3.value21; (# Klep MS2 is open \#)
  MMS_M5_TO_MeelTptM12.MT_MS3_O\_DI := BS_S\_M4M5_3\_B3.value22; (# Klep MS3 is open \#)
  MMS_M5_TO_MeelTptM12.MT_MS4_O\_DI := BS_S\_M4M5_3\_B3.value23; (# Klep MS4 is open \#)
  MMS_M5_TO_MeelTptM12.MT_MS5_O\_DI := BS_S\_M4M5_3\_B3.value24; (# Klep MS5 is open \#)
  MMS_M5_TO_MeelTptM12.MT_MS6_O\_DI := BS_S\_M4M5_3\_B3.value25; (# Klep MS6 is open \#)
  MMS_M5_TO_MeelTptM12.MT_MS7_O\_DI := BS_S\_M4M5_3\_B3.value26; (# Klep MS7 is open \#)
  MMS_M5_TO_MeelTptM12.MT_MS8_O\_DI := BS_S\_M4M5_3\_B3.value27; (# Klep MS8 is open \#)
  MMS_M5_TO_MeelTptM12.MT_MS9_O\_DI := BS_S\_M4M5_3\_B3.value28; (# Klep MS9 is open \#)
  MMS_M5_TO_MeelTptM12.MT_MS10_O\_DI := BS_S\_M4M5_3\_B3.value29; (# Klep MS10 is open \#)
  MMS_M5_TO_MeelTptM12.MT_MS11_O\_DI := BS_S\_M4M5_3\_B3.value30; (# Klep MS11 is open \#)
  MMS_M5_TO_MeelTptM12.MT_MS12_O\_DI := BS_S\_M4M5_3\_B3.value31; (# Klep MS12 is open \#)
  MMS_M5_TO_MeelTptM12.MT_MS1_KL_AS := BS_S\_M4M5_3\_B3.value32; (# Aansturing MT_MS1_KL vanuit Advant \#)
  \*)
  
  ----------------------------------------------------------------------------------------------------------------------------
  
  MMS_M5_TO_MeelTptM12.MT_MS2_KL_AS := BS_S\_M4M5_3\_B4.value; (# Aansturing MT_MS2_KL vanuit Advant \#)
  MMS_M5_TO_MeelTptM12.MT_MS3_KL_AS := BS_S\_M4M5_3\_B4.value2; (# Aansturing MT_MS3_KL vanuit Advant \#)
  MMS_M5_TO_MeelTptM12.MT_MS4_KL_AS := BS_S\_M4M5_3\_B4.value3; (# Aansturing MT_MS4_KL vanuit Advant \#)
  MMS_M5_TO_MeelTptM12.MT_MS5_KL_AS := BS_S\_M4M5_3\_B4.value4; (# Aansturing MT_MS5_KL vanuit Advant \#)
  MMS_M5_TO_MeelTptM12.MT_MS6_KL_AS := BS_S\_M4M5_3\_B4.value5; (# Aansturing MT_MS6_KL vanuit Advant \#)
  MMS_M5_TO_MeelTptM12.MT_MS7_KL_AS := BS_S\_M4M5_3\_B4.value6; (# Aansturing MT_MS7_KL vanuit Advant \#)
  MMS_M5_TO_MeelTptM12.MT_MS8_KL_AS := BS_S\_M4M5_3\_B4.value7; (# Aansturing MT_MS8_KL vanuit Advant \#)
  MMS_M5_TO_MeelTptM12.MT_MS9_KL_AS := BS_S\_M4M5_3\_B4.value8; (# Aansturing MT_MS9_KL vanuit Advant \#)
  MMS_M5_TO_MeelTptM12.MT_MS10_KL_AS := BS_S\_M4M5_3\_B4.value9; (# Aansturing MT_MS10_KL vanuit Advant \#)
  MMS_M5_TO_MeelTptM12.MT_MS11_KL_AS := BS_S\_M4M5_3\_B4.value10; (# Aansturing MT_MS11_KL vanuit Advant \#)
  MMS_M5_TO_MeelTptM12.MT_MS12_KL_AS := BS_S\_M4M5_3\_B4.value11; (# Aansturing MT_MS12_KL vanuit Advant \#)
  
  MMS_M5_TO_MeelTptM12.MT_MS60_O\_DI := BS_S\_M4M5_3\_B4.value12; (# Klep MS60 is open \#)
  MMS_M5_TO_MeelTptM12.MT_MS60_T\_DI := BS_S\_M4M5_3\_B4.value13; (# Klep MS60 is toe \#)
  MMS_M5_TO_MeelTptM12.MT_MS61_O\_DI := BS_S\_M4M5_3\_B4.value14; (# Klep MS61 is open \#)
  MMS_M5_TO_MeelTptM12.MT_MS61_T\_DI := BS_S\_M4M5_3\_B4.value15; (# Klep MS61 is toe \#)
  MMS_M5_TO_MeelTptM12.MT_MS62_1\_O_DI := BS_S\_M4M5_3\_B4.value16; (# Klep MS62_1 is open \#)
  MMS_M5_TO_MeelTptM12.MT_MS62_1\_T_DI := BS_S\_M4M5_3\_B4.value17; (# Klep MS62_1 is toe \#)
  MMS_M5_TO_MeelTptM12.MT_MS62_2\_O_DI := BS_S\_M4M5_3\_B4.value18; (# Klep MS62_2 is open \#)
  MMS_M5_TO_MeelTptM12.MT_MS62_2\_T_DI := BS_S\_M4M5_3\_B4.value19; (# Klep MS62_2 is toe \#)
  MMS_M5_TO_MeelTptM12.MT_MS63_1\_O_DI := BS_S\_M4M5_3\_B4.value20; (# Klep MS63_1 is open \#)
  MMS_M5_TO_MeelTptM12.MT_MS63_1\_T_DI := BS_S\_M4M5_3\_B4.value21; (# Klep MS63_1 is toe \#)
  MMS_M5_TO_MeelTptM12.MT_MS63_2\_O_DI := BS_S\_M4M5_3\_B4.value22; (# Klep MS63_2 is open \#)
  MMS_M5_TO_MeelTptM12.MT_MS63_2\_T_DI := BS_S\_M4M5_3\_B4.value23; (# Klep MS63_2 is toe \#)
  MMS_M5_TO_MeelTptM12.MT_MS64_1\_O_DI := BS_S\_M4M5_3\_B4.value24; (# Klep MS64_1 is open \#)
  MMS_M5_TO_MeelTptM12.MT_MS64_1\_T_DI := BS_S\_M4M5_3\_B4.value25; (# Klep MS64_1 is toe \#)
  MMS_M5_TO_MeelTptM12.MT_MS64_2\_O_DI := BS_S\_M4M5_3\_B4.value26; (# Klep MS64_2 is open \#)
  MMS_M5_TO_MeelTptM12.MT_MS64_2\_T_DI := BS_S\_M4M5_3\_B4.value27; (# Klep MS64_2 is toe \#)
  MMS_M5_TO_MeelTptM12.MT_MS66_O\_DI := BS_S\_M4M5_3\_B4.value28; (# Klep MS66 is open \#)
  MMS_M5_TO_MeelTptM12.MT_MS66_T\_DI := BS_S\_M4M5_3\_B4.value29; (# Klep MS66 is toe \#)
  
  MMS_M5_TO_MeelTptM12.MT_MS60_KL_AS := BS_S\_M4M5_3\_B4.value30; (# Aansturing MT_MS60_KL vanuit Advant \#)
  MMS_M5_TO_MeelTptM12.MT_MS61_KL_AS := BS_S\_M4M5_3\_B4.value31; (# Aansturing MT_MS61_KL vanuit Advant \#)
  MMS_M5_TO_MeelTptM12.MT_MS62_1\_KL_AS := BS_S\_M4M5_3\_B4.value32; (# Aansturing MT_MS62_1\_KL vanuit Advant \#)
  
  ---------------------------------------------------------------------------------------------------------------------------------
  
  MMS_M5_TO_MeelTptM12.MT_MS62_2\_KL_AS := BS_S\_M4M5_3\_B5.value; (# Aansturing MT_MS62_2\_KL vanuit Advant \#)
  MMS_M5_TO_MeelTptM12.MT_MS63_1\_KL_AS := BS_S\_M4M5_3\_B5.value2; (# Aansturing MT_MS63_1\_KL vanuit Advant \#)
  
  MMS_M5_TO_MeelTptM12.MT_MS63_2\_KL_AS := BS_S\_M4M5_3\_B5.value3; (# Aansturing MT_MS63_2\_KL vanuit Advant \#)
  MMS_M5_TO_MeelTptM12.MT_MS64_1\_KL_AS := BS_S\_M4M5_3\_B5.value4; (# Aansturing MT_MS64_1\_KL vanuit Advant \#)
  MMS_M5_TO_MeelTptM12.MT_MS64_2\_KL_AS := BS_S\_M4M5_3\_B5.value5; (# Aansturing MT_MS64_2\_KL vanuit Advant \#)
  MMS_M5_TO_MeelTptM12.MT_MS66_KL_AS := BS_S\_M4M5_3\_B5.value6; (# Aansturing MT_MS66_KL vanuit Advant \#)
  
  -------------------------------------------------------------------------------------------------------------------------------------------
- ## In MeelTpt_M3 zit
  ![image1](image1-65%201.png)
  
  Variabelen in MeelTpt_M3
  | MMS_From | MMS_TO_MeelTptM3 | retain |
  |------------------|--------------------------|--------|
  | Par      | Par_MeelTptM3    | retain |
  | IO               | IO_MeelTptM3             | retain |
  
  In MMS_TO_MeelTptM3 zit
  | M3      | MMS_M3_TO_MeelTptM3      | retain |
  |-----------------|----------------------------------|--------|
  | MeelTpt | MMS_MeelTpt_TO_MeelTptM3 | retain |