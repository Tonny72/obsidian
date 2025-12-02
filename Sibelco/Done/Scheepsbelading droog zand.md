---
title: Scheepsbelading droog zand
date created: 2017-11-16T09:37:35+01:00
date modified: 2025-09-18T21:58:57+02:00
---
[[journals/2017-11-16]]

| **Subject** | **Scheepsbelading droog zand**  |
| ----------- | ------------------------------- |
| **From**    | Oude Weegbrug Dessel            |
| **To**      | Tonny Lemmens                   |
| **Sent**    | woensdag 15 november 2017 19:27 |
	
	Tonny,
	
	Kan je de afzuiging wat langer laten draaien vooraleer de klep open gaat, komt veel stof vrij van de moment je start.
	
	Mvg
	
	Wim
	
	Oude weegbrug Dessel

[[journals/2017-11-16]] 
  SEQ LZ Stap1 = PC7.4.1.1
  PC7.4.1.1 =\> PC7.5.24.1 =\> STT_ZAF1_VAN_ZT:CALC_VAL (=DIC1593)
  
  MMS_M5_TO_LLB.ZAF1_Start := MMS_From2.AC450_Sib.DIC1593 OR
  MMS_From2.AC450_Sib.TZ_B0_DI OR
  MMS_From2.AC450_Sib.STT_ZAF_1\_vanuit_LLB5;
  
  Par.ZAF1.AutoCmd := Par.WeekWorkTime OR MMS_From.M5.ZAF1_Start OR MMS_From.D3.ZAF1_Poc;
  
  De [[installations/des/ZAF1]] draait altijd tijdens werkuren.
  
  -------------------------------------------------------------------------------
  
  Sequentie in Visio gezet
  <https://sibelco.sharepoint.com/teams/Team_PlantDessel_Dessel_MiningandProcessingOperations_ProjectandTechnicalServices/Public%20Documents/Installaties/Beladen%20vrachtwagens/LLZ/LLZ2_SEQ%20-%20Laden%20zand.vsdx?d=w4e57c7f501584ba78e2f5d9ad0e22435>
  
  -------------------------------------------------------------------------------
[[journals/2017-11-16]] 14:34 
  Volgens Wim ook veel stof bij laden aan de oude weegbrug.
  Mogelijk ZAF1 slecht.
  Gevraagd aan GS en MVP om dit eens na te kijken.