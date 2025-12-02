---
date created: 2025-08-20T08:01:29+02:00
date modified: 2025-09-18T10:32:47+02:00
tags:
  - C3
  - sequentie
---


```mermaid
---
config:
  layout: elk
---

flowchart TB

%% bepaal classes
  classDef step fill: #2dcfff, stroke: #000000, color: #000000
    
S1("S1: Verberg knop Doorstap <br>(hmi_doorstap_visible = 0)"):::step
S1 -- "(geen voorwaarde)" --> S2

S2("S2: BU320_Int_release = 1"):::step
S2 -- "BU320 in remote" --> S3

S3("S3: Start FA310_00"):::step
S3 -- "FA310_00 draait en wacht 10 sec." --> S4

S4("S4: Diesel_Remote_Cmd=0 <br>Gas_Natural_Remote_Cmd=0 <br>HMI_Restart_Burner_Visible=1"):::step
S4 -- "FA310_00 draait en wacht 60 seconden" --> S7

S7("S7: Zet HMI_Doorstap_Visible=1 <br> BU320_Int_Release=0"):::step
S7 -- "FA310_00 draait en wacht 60 seconden" --> S8

S8("S8: Zet BU320_Reset=1"):::step
S8 -- "Wacht 10 seconden" --> S9

S9("S9: BU320_Reset=0"):::step
S9 -- "BU320_00_Igniter_On=1 of BU320_00_Igniter_Ready=1" --> S10 

S10("S10: Start BU320_00"):::step
S10 -- "BU320_00_FLAME_IGNITION=1 en Wacht 10 seconden" --> S11

S11("S11: Zet HMI_Doorstap=0"):::step
S11 -- "HMI_GAS_OR_DIESEL=1 (keuze diesel)" --> S20
S11 -- "HMI_GAS_OR_DIESEL=0 (keuze gas)" --> S100

S20("S20: Tussenstap"):::step
S20 -- "HMI_GAS_OR_DIESEL=1" --> S30
S20 -- "HMI_GAS_OR_DIESEL=0, en HMI_GAS_OR_GAS_AND_DIESEL=1" --> S40

S30("S30: Zet Gas_Natural_Remote_Cmd=0 <br>en Start PU316_00"):::step
S30 -- "PU316_00 draait" --> S50

S40("S40: Start PU317_00"):::step
S40 -- "PU317_00 draait" --> S50

S50("S50: keuzestap"):::step
S50 -- "Start_PU318_or_PU319=0 <br>(PU318)" --> S60
S50 -- "Start_PU318_or_PU319=1 <br>(PU318)" --> S70

S60("S60: Sluit AV329_02"):::step
S60 -- "AV329_02 is toe" --> S61

S61("S61: Stop PU319_00"):::step
S61 -- "PU319_00 draait niet" --> S62

S62("S62: Open AV329_01 <br>Start PU318_00"):::step
S62 -- "AV329_01 is open en PU318_00 draait" --> S80

S70("S70: Sluit AV329_01"):::step
S70 -- "AV329_01 is toe" --> S71

S71("S71: Stop PU318_00"):::step
S71 -- "PU318_00 draait niet" --> S72

S72("S72: Open AV329_02 <br> Start PU319_00"):::step
S72 -- "AV329_02 is open en PU319_00 draait" --> S80

S80("S80: BU320_Reset=1"):::step
S80 -- Wacht 2 seconden --> S81

S81("S81: BU320_Reset=0"):::step
S81 -- "BU320_00_DIESEL_READY=1 of HMI_Doorstap=1" --> S82

S82("S82: Diesel_Remote_Cmd=1 en HMI_Doorstap=0"):::step
S82 -- "(geen voorwaarde)" --> S200

S100("S100: Diesel_Remote_Cmd=0"):::step
S100 -- "ONLY GAS: (Not HMI_GAS_OR_GAS_AND_DIESEL and BU320_00_GN_READY ) <br>or (NOT HMI_GAS_OR_GAS_AND_DIESEL and BU320_00_FLAME_ON)" --> S110
S100 -- "GAS and DIESEL: HMI_GAS_OR_GAS_AND_DIESEL and BU320_00_FLAME_ON" --> S150

S110("S110: Diesel_Remote_Cmd=0 <br>Sluit AV329_01 <br>Sluit AV329_02 <br>Stop PU318_00 <br>Stop PU319_00 <br>Stop PU316_00 <br>Stop PU317_00"):::step
S110 -- "AV329_02 is toe en PU319_00 is gestopt en AV329_01 is toe en PU318_00 is gestopt en PU316_00 is gestopt en PU317_00 is gestopt of (BU320_00_GN_READY=1 of BU320_00_FLAME_ON=1)" --> S111

S111

```

# Buttons and variables

![alt text](images/image-3.png)

| Tag                       | Value                           | Comment                                                |
| ------------------------- | ------------------------------- | ------------------------------------------------------ |
| BU320_Reset               |                                 |                                                        |
| BU320_00_DIESEL_READY     |                                 |                                                        |
| Diesel_Remote_Cmd         |                                 |                                                        |
| HMI_BURNER_VISIBLE        | /                               | Not used code                                          |
| HMI_GAS_OR_DIESEL         | 0 => Gas <br> 1 => Diesel       | Button GAS of DIESEL <br>![alt text](images/image.png) |
| HMI_GAS_OR_GAS_AND_DIESEL | 0 => Gas <br> 1 => Gas + Diesel | ![alt text](images/image-1.png)                        |
| HMI_Doorstap              |                                 | ![alt text](images/image-2.png)                        |
| Gas_Natural_Remote_Cmd    |                                 | ![alt text](images/image-5.png)                        |
| Start_PU318_or_PU319      |                                 | ![alt text](images/image-6.png)                        |
