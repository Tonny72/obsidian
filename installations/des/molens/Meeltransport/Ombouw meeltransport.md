---
title: Ombouw meeltransport
updated: [[2016-10-14]]T08:20:50.0000000+02:00
created: [[2016-09-12]]T08:36:09.0000000+02:00
---

MT_6 en de andere advant symbolen zitten al in Molen3

Eigenlijk had KR dit al moeten omprogrammeren

![image1](image1-227.png)

- ## DAT Communicatie nakijken
  (\*-----------------------------------------------\*)
  (\* Conversie van DAT_From_S\_M4M5_1 \*)
  (\* ----------------------------------------------\*)
  DintToBool32( Int := DAT_From_S\_M4M5_1.B1,
  BoolStruct := BS2,
  Status := Status );
  
  MMS_M5_TO_ST02.STT_MT_F2_VAN_M4 := BS2.bit0 or debug_1;
  MMS_M5_TO_ST02.STT_MT_F2_VAN_M5 := BS2.bit1 or debug_2;
  MMS_From2.AC450_Sib.MT_F1V_M5_Tpt_Poc := BS2.bit2;
  MMS_From2.AC450_Sib.MT_1R_M5_Tpt_Poc := BS2.bit3; (# VALUE4 \#)
  MMS_From2.AC450_Sib.MT_1L_M5_Tpt_Poc := BS2.bit4; (# VALUE5 \#)
  MMS_From2.AC450_Sib.MT_2\_M5_Tpt_Poc := BS2.bit5; (# VALUE6 \#)
  
  MMS_M5_TO_M4.M4_SEQ_TRANSPORT_Stap34 := BS2.bit19 AND DAT_CommValid; (# value20 \#)
  
  (\*-----------------------------------------------\*)
  (\* Conversie van DAT_From_S\_M4M5_3\_B2 \*)
  (\* Ontvangen van AC450 Sibelco \*)
  (\* ----------------------------------------------\*)
  DintToBool32( Int := DAT_From_S\_M4M5_3.B2,
  BoolStruct := BS_S\_M4M5_3\_B2,
  Status := Status );
  
  MMS_M5_TO_M4.MT_2\_DI := BS_S\_M4M5_3\_B2.value;
  DAT_From_S\_M4M5.MT_2\_DI := BS_S\_M4M5_3\_B2.value;
  
  MMS_M5_TO_M4.M4_WK1_1\_O_DI := BS_S\_M4M5_3\_B2.value3;
  MMS_M5_TO_M4.M4_WK1_2\_O_DI := BS_S\_M4M5_3\_B2.value4;
  MMS_M5_TO_M4.M5_3\_1_O := BS_S\_M4M5_3\_B2.value5;
  MMS_M5_TO_M4.M5_3\_2_O := BS_S\_M4M5_3\_B2.value6;
  
  MMS_M5_TO_D4.D4_SEQ_DZ_Run := BS_S\_M4M5_3\_B2.value10;
  MMS_M5_TO_D4.D4_SEQ_DZ_GSO := BS_S\_M4M5_3\_B2.value11;
  MMS_M5_TO_D4.D4_SEQ_DZ_ProdStap := BS_S\_M4M5_3\_B2.value12;
  MMS_MBS_TO_D3.ZT_5\_DI := BS_S\_M4M5_3\_B2.value13;
  MMS_MBS_TO_D3.ZT_6\_DI := BS_S\_M4M5_3\_B2.value14;
  MMS_M5_TO_D4.D4_KD4 := BS_S\_M4M5_3\_B2.value15;
  MMS_M5_TO_D4.D4_KBU := BS_S\_M4M5_3\_B2.value16;
  MMS_From2.AC450_Sib.STT_ZAF_1\_vanuit_LLB5 := BS_S\_M4M5_3\_B2.value17;
  
  MMS_From2.AC450_Sib.M5_3\_1_M5_Poc := BS_S\_M4M5_3\_B2.value18;
  
  -------------------------------------------
  MMS_From2.AC450_Sib.M5_3\_1_M5_Poc := BS_S\_M4M5_3\_B2.value18;
  MMS_From2.AC450_Sib.M5_3\_1_M5_Poc := BS_S\_M4M5_3\_B8.value3;
  MMS_From2.AC450_Sib.M5_3\_2_M5_Poc := BS_S\_M4M5_3\_B8.value4;
  
  (\*-----------------------------------------------\*)
  (\* Conversie van DAT_From_S\_M4M5_4\_B3 \*)
  (\* Ontvangen van AC450 Sibelco \*)
  (\* ----------------------------------------------\*)
  DintToBool32( Int := DAT_From_S\_M4M5_4.B3,
  BoolStruct := BS_S\_M4M5_4\_B3,
  Status := Status );
  
  MMS_From2.AC450_Sib.M4_MT_F1V_Poc := BS_S\_M4M5_4\_B3.value;
  MMS_From2.AC450_Sib.M4_MT_F1M_Poc := BS_S\_M4M5_4\_B3.value2;
  MMS_From2.AC450_Sib.M4_MT_2\_Poc := BS_S\_M4M5_4\_B3.value3;
  MMS_From2.AC450_Sib.M4_MT_1L_Poc := BS_S\_M4M5_4\_B3.value4;
  MMS_From2.AC450_Sib.M4_MT_1R_Poc := BS_S\_M4M5_4\_B3.value5;
  
  ----------------------------------
  
  MMS_From2.AC450_Sib.SEQ4_M5_Draait := BS_S\_M4M5_3\_B10.value15; (#Seq. Meeltransport draait \#)