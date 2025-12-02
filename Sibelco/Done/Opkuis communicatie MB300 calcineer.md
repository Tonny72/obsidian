---
title: Opkuis communicatie MB300 calcineer
updated: [[2019-04-01]]T08:00:22.0000000+02:00
created: [[2019-03-29]]T10:28:55.0000000+01:00
---

- # Van Advant
  ![image1](image1-63%201.png)
- ## IO.C_SV30_DO.Value := NOT Par.C_NOODWERKING AND DAT_From_S\_CAL_1\_B2.value6;
  IO.C_SV30_DO \<= S_CAL_1\_B2.value6 \<= PC12.15.3.2:39 \<= PC12.8.43.5:60 \<= Advant object C_SV30 \<= **Wordt niet aangestuurd**
- ## IO.C_KL23_DO.Value := NOT Par.C_NOODWERKING AND DAT_From_S\_CAL_1\_B2.value20;
  IO.C_KL23_DO \<= S_CAL_1\_B2.value20 \<= PC12.15.3.3:34
- # Naar Advant
  ![image2](image2-39%201.png)
- ## C_7\_Run - R_CAL_1.B1:value6
  ![image3](image3-25%201.png)
  
  ![image4](image4-14%201.png)
- PC12.11.8.3 =\> Wordt gebruikt bij C_TOIC21 =\> Niet meer nodig
- PC12.4.14.2 =\> Wordt gebruikt als stap vw bij C_SEQ_ALG =\> C_SEQ_ALG wordt niet meer gebruikt
- PC12.5.5.4 =\> Wordt gebruikt als stap vw bij C_SEQ_NZ =\> Sequentie wordt niet meer gebruikt.
- PC12.8.7.x =\> Wordt gebruikt bij Advant C_7 =\> Niet meer nodig
  
  =\> Conclusie: verwijderen
- # R_CAL_1\_B2.value4 := IO.C_33.FB1.Value
  ![image5](image5-11%201.png)
- PC12.5.5.2 =\> Wordt gebruikt als stap vw in C_SEQ_NZ (PC12.5) = \> verwijderen
- PC12.8.15 =\> Advant object C_33 =\> verwijderen
- PC12.8.7 =\> Wordt gebruikt als vergrendeling bij Advant C_7 =\> Verwijderen
  
  =\> Conclusie verwijderen
- # C_TZ_B5: DAT_To_R\_CAL_1\_B6.value6 := IO.C_TZ_B5.FB1.Value
  ![image6](image6-10%201.png)
- PC8.1.2.3 =\> R_CAL_1.B6:VALUE6 =\> S2106.B1:VALUE21 =\> Silos R2103.B1:value21 =\> PC1.11.2.2:2 =\> Voorwaarde bij S_B2L =\> Verwijderen
- PC8.2.8.5 =\> Start VW van TZ_B3 (DX102.23) =\> Verwijderen.
- PC8.2.8.8 =\> Start VW van C_TZ_B5 (DX112.30) en S_CAL_1.B3:VALUE30  
  IO.C_TZ_B5.Out1.Value := NOT Par.C_NOODWERKING AND DAT_From_S\_CAL_1\_B3.value30;
  ![image7](image7-7%201.png)
  
  =\> Verwijderd
- ##
- ## GMP ZS72 ZS74
- DAT_To_R\_CAL_1\_B6.value7 := IaPar.GMP.C_GMP_LT_ZS72.Vergrendeling;  
  =\> Wordt niet gebruikt in Advant plc
- DAT_To_R\_CAL_1\_B6.value8 := IaPar.GMP.C_GMP_LT_ZS74.Vergrendeling;  
  =\> Wordt niet gebruikt in Advant plc
- ## C_18_AutoCmd
  DAT_To_R\_CAL_1\_B6.value10 := MMS_CT_TO_CAL.C_18_AutoCmd;
  =\> PC12.15.1.9:13 =\> Niks
- ## C_PT32
  DAT_To_R\_CAL_3.C_PT32 := C_IO.S200.C_PT32_1.Value
  =\> R_CAL_3.R6 =\> PC12.15.2.2:11 (move) =\> PC12.15.2.2:31
- PC12.6.2.1:I1 =\> Extra stap VW in PC12.6 (C_SEQ_BR) =\> Verwijderen
- PC12.8.1.12:2 =\> Berekening verschildruk =\> AIC409:66 =\> Verwijderen
- Pc12.8.35.2:I1 =\> VW voor vrijgave brander DX108.22 en =\> S_CAL_1.B2:value14 =\> Niks
  Conclusie: verwijderen
- ## IO.C_O2_AI
  DAT_To_R\_CAL_3.C_O2 := IO.Schouw.C_AIT90_1\_O2_AI.Value (\*IO.C_O2_AI.Value\*);
  IO.Schouw.C_AIT90_1\_O2_AI wordt nergens geschreven =\> Verwijderen
- # [[2019-04-01]] 
  Laatste stap disabled
  IO.C_SV30_DO.Value := NOT Par.C_NOODWERKING AND DAT_From_S\_CAL_1\_B2.value6;