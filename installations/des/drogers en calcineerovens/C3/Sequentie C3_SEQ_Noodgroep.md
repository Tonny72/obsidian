---
date created: 2025-08-20T08:01:29+02:00
date modified: 2025-09-18T19:29:08+02:00
---
# Sequentie C3_Burner

## Start
ON-Sequentie start automatisch als: Gen_Power_on=1 EN Gen_Off=1 EN Net_Power_on=1

## Stop 
OFF-Sequentie start als: NET_Power_On=0 EN NET_Off=0

## ON-Sequentie
```mermaid
---
config:
  layout: elk
---

flowchart TB

%% bepaal classes
  classDef step fill: #2dcfff, stroke: #000000, color: #000000
    
S1("S1: Geen actie"):::step
S1 -- "Wacht 20 seconden" --> S2

S2("S2: Poc.Reset_VSD_EM := True;"):::step
S2 -- "Wacht 2 seconden" --> S3

S3("S3: Poc.Reset_VSD_EM := False;"):::step
S3 -- "Wacht 20 seconden" --> S4

S4("S4: Start C3_PU422"):::step
S4 -- "C3_PU422 draait en wacht 5 seconden" --> S15
S4 -- C3_PU422 draait niet wacht 10 seconden --> S10

S10("S10: Start C3_PU423"):::step
S10 -- "S10.T > Wacht_20s Or Not IaPar.Water_cooling.PU422_00_RUN" --> S15

S15("S15: Start C312"):::step
S15 -- "S15.T > Wacht_5s Or Not IaPar.Killn.C312_00_StatRun" --> S16

S16("S16: Poc.FA311_Start := Start;"):::step
S16 -- "S16.T > Wacht_5s Or Not IaPar.Burner.FA311_00_RUN" --> S17

S17("S17")
```

## OFF-Sequentie
```mermaid
---
config:
  layout: elk
---

flowchart TB

%% bepaal classes
  classDef step fill: #2dcfff, stroke: #000000, color: #000000
    
S500("S500: Stop C3_PU422, Stop C3_PU423, Stop C312, Stop C3_FA311"):::step
S500 -- "S500.T > Wacht_5s and Not Net_Power_On" --> S501

S501("S501: geen actie"):::step
S501 -- "Wacht 20 seconden" --> S502

S502("S502: Poc.Reset_VSD_EM := True;"):::step
S502 -- "Wacht 2 seconden" --> S503

S503("S503: Poc.Reset_VSD_EM := False;"):::step
S503 -- "Wacht 20 seconden" --> S504

S504("S504: geen actie"):::step
S504 -- "Geen voorwaarde" --> S505

S505("S505: Start C3_PU422"):::step
S505 -- "S505.T > Wacht_5s And IaPar.Water_cooling.PU422_00_RUN" --> S520
S505 -- "S505.T > Wacht_10s And Not IaPar.Water_cooling.PU422_00_RUN" --> S510

S510("S510: Start C3_PU423"):::step
S510 -- "S510.T > Wacht_10s Or Not IaPar.Water_cooling.PU422_00_RUN" --> S520

S520("S520: Poc.C312_Start := Start;"):::step
S520 -- "S520.T > Wacht_5s Or Not IaPar.Killn.C312_00_StatRun" --> S521

S521("Poc.FA311_Start := Start;"):::step
S521 -- "S521.T > Wacht_5s Or Not IaPar.Burner.FA311_00_RUN" --> S522

S522("S522: geen actie"):::step
S522 -- "HMI_Stop_SEQ" --> S523

S523("S523: Stop C3_PU422, stop C3_PU423, stop C312, stop FA311"):::step
S523 -- "geen voorwaarde" --> S524

S524("Einde OFF-sequentie"):::step
```