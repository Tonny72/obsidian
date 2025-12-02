---
title: MES oplossen dubbele  W/C voor 1 seq.
updated: [[2015-02-06]]T09:31:45.0000000+01:00
created: [[2015-02-06]]T09:27:12.0000000+01:00
---

MES oplossen dubbele W/C voor 1 seq.
vrijdag 6 februari 2015
9:27

Welke seq. heeft een dubbele W/C

- SMDS2 en SMWS
- PML03 en PDP08
- SMCAL en SMDS1
- # SMDS2 en SMWS
  (\* SMDS2 \*)
  
  (\* ----- \*)
  
  Keuze72_74 := (ParLossen.Silo1SIB=72) OR (ParLossen.Silo1SIB=74);
  
  SMDS2_EnableProductionCounter := ParLossen.TZ_B6_Draait AND Keuze72_74;
  
  SMDS2_Run := (Poc.Lossen_SIB.Status.OnSeq OR Poc.Lossen_SIB.Status.OffSeq) AND Keuze72_74;
  
  (\* SMWS \*)
  
  (\* ---- \*)
  
  SMWS_Source2_Pecentage := 100-ParLossen.PercentageSIB;
  
  SMWS_EnableProductionCounter := ParLossen.Motoren.S_B3.StatAct AND NOT Keuze72_74;
  
  SMWS_Run := (Poc.Lossen_SIB.Status.OnSeq OR Poc.Lossen_SIB.Status.OffSeq) AND NOT Keuze72_74;
- # SMCAL en SMDS1
  (\* SMCAL \*)
  
  (\* ----- \*)
  
  SMCAL_FlowMass := 12.9;
  
  SMCAL_EnableProductionCounter := ((Par.AF5_ZS54.StatOpen AND Par.KeuzeVan=54) OR
  
  (Par.AF5_ZS55.StatOpen AND Par.KeuzeVan=55) OR
  
  (Par.AF5_ZS56.StatOpen AND Par.KeuzeVan=56) OR
  
  (Par.AF5_ZS57.StatOpen AND Par.KeuzeVan=57)) AND
  
  Par.AF5_6.StatRun;
  
  (\* SMDS1 \*)
  
  (\* ----- \*)
  
  SMDS1_FlowMass := 21;
  
  SMDS1_EnableProductionCounter := ((Par.AF5_ZS41.StatOpen AND Par.KeuzeVan=41) OR
  
  (Par.AF5_ZS42.StatOpen AND Par.KeuzeVan=42) OR
  
  (Par.AF5_ZS43.StatOpen AND Par.KeuzeVan=43) OR
  
  (Par.AF5_ZS44.StatOpen AND Par.KeuzeVan=44) OR
  
  (Par.AF5_ZS45.StatOpen AND Par.KeuzeVan=45) OR
  
  (Par.AF5_ZS46.StatOpen AND Par.KeuzeVan=46) OR
  
  (Par.AF5_ZS47.StatOpen AND Par.KeuzeVan=47)) AND
  
  Par.AF5_11.StatRun;