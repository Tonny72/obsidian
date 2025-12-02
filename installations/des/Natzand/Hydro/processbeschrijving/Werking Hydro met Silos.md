---
aliases:
tags:
  - Hydro
  - silos
date created: 2025-08-01
date modified: 2025-09-09
---
 ## Sequentie S_Seq_Lijn_1_2
- Stap 19, Stap29, Stap39, ...
	- Productiestap voor de verschillende silo keuzes
	- S_Lijn_1_2_Herstart = 1
	- Tr19, Tr29, Tr39, ...
		- Hoogniveau of doorstappen
	- Stap 548
		- Indien er gewisseld wordt van type bunker
			- S_Lijn_1_2_Herstart = 0
			- S_Lijn_1_2_Doorstart_HY = 1
			- S_L12_M32_Productiestap = 0
	- Tr 548
		- Wacht 2 seconden
	- Stap 549
		- S_Lijn_1_2_Doorstart_HY = 0
[[installations/des/Natzand/Hydro/processbeschrijving/Sequentie SEQ_Hydro_Lijn_1_2]]

```mermaid
		  %%{init: {'theme': 'base', 
		          'themeVariables': { 'primaryColor': '#BB2528', 
		          'primaryTextColor': '#fff', 
		          'primaryBorderColor': '#7C0000', 
		          'lineColor': '#F8B229', 
		          'secondaryColor': '#006100', 
		          'tertiaryColor': '#fff', 
		          'fontSize': 7px', 
		          'fontFamily': 'Inter'}}}%%
		  stateDiagram-v2
		  
		  S100 : <b>S100</b>#colon;Productiestap
		  S101 : S101#colon; HY_voeding = 0
		  S102 : S102 - HY_DIC3_Track = 1, HY_DIC4_track = 1
		  S103 : S103#colon; Stop HY_ZP32,Stop HY_ZP34, Doorstap_kleppen_Lijn1_2 = 1
		  S104 : S104#colon; Open HY_KL30
		  S105 : S105#colon; Sluit HY_ZP32_BW,\nStop HY_BP1,\nSluit HY_KL31
		  S106 : S106#colon; Start HY_ZP34, Doorstap_kleppen_Lijn1_2 = 0
		  S113 : S113#colon; Start HY_BP1,\nOpen HY_KL31,Doorstap_kleppen_Lijn1_2 = 1
		  S114 : S114#colon; Stop HY_ZP34,\nStart HY_BP1, Sluit HY_KL30,\nOpen HY_KL31
		  S115 : S115#colon; Open HY_KL_ZP32_BW,\nStart HY_ZP34
		  Tr100 : <b>Tr100#colon; S_Lijn_1_2_Doorstart_HY</b>
		  
		  [*] --> S100
		  S100 --> Tr100
		  Tr100 --> S101
		  S101 --> S102: Tr101#colon; Wacht 10 seconden
		  S102 --> S103: Tr102#colon; Silokeuze = beton of metaal\nWacht 20 minuten
		  S102 --> S113: Tr62#colon; Silokeuze = Maat\nWacht 5 minuten
		  S103 --> S104: Tr103#colon; Wacht 5 seconden
		  S104 --> S105: HY_KL30is open
		  S105 --> S106: Wacht 30 seconden\nen Seq. S_L12_M32 is in productiestap\nen HY_KL31 is toe.
		  S113 --> S114: HY_KL31 is open\nen HY_BP1 draait
		  S114 --> S115: HY_BP1 draait\nenSeq. S_L12_M32 is in productiestap\nen HY_KL30 is toe
```

	  
- Stap 100: Productiestap
- Tr100: S_Lijn_1_2_Doorstart_HY
- Stap 101: HY_voeding = 0
- Tr101: Wacht 10 seconden
- Stap 102:
	- HY_DIC3_Track = 1
	- HY_DIC4_Track = 1
- Tr102: Wacht 20 minuten, Tr62: Wacht 5 minuten
- Stap103
	- Stop [[installations/des/Natzand/Hydro/processbeschrijving/HY_ZP32]]
	- Stop [[installations/des/Natzand/Hydro/processbeschrijving/HY_ZP34]]
	- Doorstap_kleppen_Lijn1_2 = 1
- Stap104 ... Stap105, Stap114 ... Stap115
	- Start, Stop pompen
	- Open, Sluit kleppen

- Stap106, Stap116
	- Doorstap_kleppen_Lijn1_2 = 0
	- <img src="https://www.plantuml.com/plantuml/png/ZLDBJzmm4BxdLymP0OhZP0-Hg2ZbG5KGAsKb1DtASfDPS3UnJJAf2hyUFsAndEWfclaUyqqc0JYVI8uq3tqsxPMsSfG3TBYJSqyR_4TVU_Me1zG4FUueUr8T0WwMNXnfQaTbIHcTPGtBETGG7WqP2rVtuc7DY-EjFgnBLryQCxgPLknxj1Qrk5P_D1C5d07pFcNqAU7MWLxtuvhd7gWYK47JpuhI175nvqpJZ8iryrKYE6dmN4NfocLno_vV63-JnQKOVnV62GVPs6SxRKQMvyucD8NhYeK-ahYwptuU_OAJaoy-NrWp3rKGHMb2MKHhM8-ccrjIw4Vw9akKeWv2LiETR9y8M0uJjaPtg2Elzg7_6koKVbnsp8kavb5TGADwiyVv5HtbDvBHO7Om84dPHq6mkVp-ZOlDADkzN_COjZesIq6fUMZFWltge_kDb1G_dYL36JFmPO7gG_uoiQewVHXg0cCZMYNKNJkg-VlwM-qErk3pgRy3AyGDBy1fbGPx-3O3RRchnydWQNQEklC_o1i0" />

```plantuml 
		  @startuml
		  skinparam defaultTextAlignment left
		  hide empty description
		  
		  S103 : S103 Stop HY_ZP32,\n Stop HY_ZP34,\nDoorstap_kleppen_Lijn1_2 = 1
		  S104 : S104 Open HY_KL30
		  S105 : S105 Sluit HY_ZP32_BW,\nStop HY_BP1,\nSluit HY_KL31
		  S106 : S106 Start HY_ZP34,\nDoorstap_kleppen_Lijn1_2 = 0
		  S113 : S113 Start HY_BP1,\nOpen HY_KL31,\nDoorstap_kleppen_Lijn1_2 = 1
		  Tr100: S_Lijn_1_2_Doorstart_HY
		  [*] --> S100
		  S100 --> Tr100
		  Tr100 --> S101
		  S100 : Productiestap
		  S101 --> S102: Tr101: Wacht 10 seconden
		  S101 : HY_voeding = 0
		  S102 --> S103: Tr102 Silokeuze = beton of metaal
		  S102 : HY_DIC3_Track = 1, \nHY_DIC4_track = 1
		  S102 --> S113: Tr62 Silokeuze = Maat
		  S103 --> S104: Tr103 Wacht 5 seconden
		  S104 --> S105: HY_KL30is open
		  S105 --> S106 :Wacht 30 seconden\nen Seq. S_L12_M32 is in productiestap\nen HY_KL31 is toe.
		  @enduml
```


## HY_RS_Lijn_L1_2_Reset
- Is 0 tijdens stilstand
- Is 1 tijdens werking
  
```
  HY_RS_Lijn_L1_2_Reset:= (IaPar.HY_Z2.StatRun Or IaPar_Zeef_1.HY_Z1.StatRun) 
   					     And IaPar_ZP38.HY_ZP38.StatRun 
  				 And IaPar_Indikker_M34.HY_ZP33.StatRun 
  				 And IaPar_Silo.S_Lijn_1_2_Herstart 
  				 And Poc_L1_L2.HY_Voeding 
  				 And (
  						 (
  						   (IaPar_Silo.Keuze_Silo_Beton_L12 Or IaPar_Silo.Keuze_Silo_Metaal_L12) 
  						   And not IaPar_Pomptank_ZP34.SI_ST3.LTLLL.Act
  						 ) 
  						 Or (IaPar_Silo.Keuze_Silo_Maat_L12 
  						     And Not IaPar_Pomptank_ZP34.HY_ST25.LTLLL.Act)
  					  );
  ```
- ### Tijdens werking
  
HERNOEMEN NAAR L1_2_Voeding ?
	- 1 = Normale werking
	- 0 = zand / voeding af
		- HY_SS2.Select = 2, Ketel1: Regelkleppen onder sizer dicht
		- HY_SS3.Select = 2, Ketel1: Regelkleppen onder sizer dicht
		- HY_DIC4_Track
		- HY_DIC2_Track
		- HY_SS8.Select = 2, Ketel3 (voedingsklep dicht?)
		- HY_SS6.Select = 2, Ketel2 (voedingsklep dicht?)
## HY_DIC2_Track
```
HY_DIC2_Track := Poc_L1_L2.HY_DIC2_Track And IaPar_Pomptank_ZP38.HY_L1_L2_Auto Or               VoteOut.SI_ST3.Forward.LTLLL.Act And IaPar_Pomptank_ZP34.HY_KL30.StatOpen Or               IaPar_Pomptank_ZP34.HY_ZP34.StatStop Or Not IaPar_Zeef_2.HY_Herstart_L1_2_RS;
```
## HY_DIC4_Track
```
HY_DIC4_Track := Poc_L1_L2.HY_DIC4_Track And IaPar_Pomptank_ZP38.HY_L1_L2_Auto Or 
                     VoteOut.SI_ST3.Forward.LTLLL.Act And IaPar_Pomptank_ZP34.HY_KL30.StatOpen Or 
                     IaPar_Pomptank_ZP34.HY_ZP34.StatStop Or
                     Not IaPar_Zeef_2.HY_Herstart_L1_2_RS;
```
    

## Sequentie S_Seq_Lijn_3_4
- Stap 548
		- Indien er gewisseld wordt van type bunker
			- S_Lijn_3_4_Herstart = 0
			- S_Lijn_3_4_Doorstart_HY = 1
			- S_L34_M32_Productiestap = 0
## HY_Z2 - Zeef2
![image.png](assets/images/image_1717183048521_0\.jpg)
## HY_ZP38 - Zandpomp 38
![image.png](assets/images/image_1717183123281_0\.jpg)
- ## HY_ZP33 - Zandpomp 33
![image.png](assets/images/image_1717183393000_0\.jpg)