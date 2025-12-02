---
title: SibToevoerAfzak.Unit_Motoren
updated: [[2016-09-27]]T12:01:57.0000000+02:00
created: [[2016-09-27]]T12:01:22.0000000+02:00
---

(\* AF5_1 \*)
Par.AF5_1.AutoCmd := MMS_From.Calcineeroven.AF5_FGST_BB_DI OR
MMS_From.Calcineeroven.AF5_FGST_FFS_DI;

(\* AF5_2 \*)
Par.AF5_2.AutoCmd := MMS_From.Calcineeroven.AF5_FGST_BB_DI OR
MMS_From.Calcineeroven.AF5_FGST_FFS_DI;

(\* AF5_3 \*)
Par.AF5_3.AutoCmd := MMS_From.Calcineeroven.AF5_FGST_BB_DI OR
MMS_From.Calcineeroven.AF5_FGST_FFS_DI;

(\* AF5_4 \*)
AF5_4\_Prio1_TOn( In := (Par.Seq_AF5_SMCAL_KeuzeNaar=105) AND Par.AF5_LSH105.OutDiff AND Par.AF5_WK3.StatOpen AND Par.AF5_3.StatRun,
PT := dint_to_time( 10000) );
AF5_4\_PrioCmd1 := AF5_4\_Prio1_TOn.Q;
AF5_4\_Prio2_TOn( In := (Par.Seq_AF5_SMCAL_KeuzeNaar=106) AND Par.AF5_LSH106.OutDiff AND Par.AF5_WK3.StatClosed AND Par.AF5_3.StatRun,
PT := dint_to_time( 10000) );
AF5_4\_PrioCmd2 := AF5_4\_Prio2_TOn.Q;
AF5_4\_PrioCmd3 := Par.AF5_3.StatStop;

(\* AF5_5 \*)
AF5_5\_PrioCmd1 := Par.AF5_4.StatStop AND Par.AF5_15.StatStop;

(\* AF5_6 \*)
AF5_6\_PrioCmd1 := Par.AF5_5.StatStop;
AF5_6\_PrioCmd2 := Par.AF5_LSH4.OutDiff;

(\* AF5_7 \*)
AF5_7\_PrioCmd1 := Par.AF5_6.StatStop;
AF5_7\_PrioCmd2 := Par.AF5_LSH6.OutDiff;

(\* AF5_8 \*)
AF5_8\_PrioCmd1 := Par.AF5_7.StatStop;

(\* AF5_10 \*)
AF5_10_PrioCmd1 := NOT Par.AF5_15.StatRun1;
AF5_10_PrioCmd2 := Par.AF5_LSH3.OutDiff;

(\* AF5_11 \*)
AF5_11_PrioCmd1 := Par.AF5_10.StatStop;
AF5_11_PrioCmd2 := Par.AF5_LSH5.OutDiff;

(\* AF5_12 \*)
Par.AF5_12.AutoCmd := MMS_From.Calcineeroven.AF5_FGST_BB_DI OR
MMS_From.Calcineeroven.AF5_FGST_FFS_DI;
AF5_12_PrioCmd1 := Par.AF5_2.StatStop;

(\* AF5_13 \*)
AF5_13_PrioCmd1 := Par.AF5_8.StatStop;

(\* AF5_15 \*)
AF5_15_AutoCmd2 := MMS_From.CalcineerTPT.AF5_15L_AutoCmd;
Par.AF5_15.AutoCmd2 := MMS_From.CalcineerTPT.AF5_15L_AutoCmd;

AF5_15_PrioCmd11_TOn( In := Par.AF5_16.StatStop,
PT := AF5_15_PrioCmd11_TOn_PT );
AF5_15_PrioCmd11 := AF5_15_PrioCmd11_TOn.Q;
AF5_15_PrioCmd21 := (NOT MMS_From.CalcineerTPT.CT_51_KL_StatOpen AND NOT MMS_From.CalcineerTPT.CT_25_StatRun) AND Par.AF5_15.AutoCmd2;
AF5_15_PrioCmd22 := Par.AF5_15_LSH.OutDiff;

(\* AF5_16 \*)
AF5_16_PrioCmd1 := Par.AF5_17.StatStop;

(\* AF5_17 \*)
AF5_17_PrioCmd1 := Par.AF5_18.StatStop;
