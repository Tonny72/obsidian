---
created: [[2011-03-25]]T13:22:31.0000000+01:00
---

Code voor een drive met koelventilator

1.  Start de drive pas als de koelventilator draait.
2.  Laat de koelventilator even nadraaien

(\* BL401 en BL401V \*)
(\* --------------- \*)
BL401_AutoCmdIn := poc.Flotatie.BL401_AutoCmd OR BL401_Man_Out;

BL401_TOf( In := BL401_AutoCmdIn,
PT := dint_to_time(1000) );

Par.BL401.AutoCmd := BL401_AutoCmdIn AND BL401V_Par.StatRun;
BL401V_Par.AutoCmd := BL401_AutoCmdIn or BL401_TOf.Q;

**(\* WPU201 en WPU201V \*)**
**(\* ----------------- \*)**
**WPU201_AutoCmdIn := poc.Lijn1.WPU201_AutoCmd OR poc.Lijn2.WPU201_AutoCmd OR poc.Lijn3.WPU201_AutoCmd;**
**WPU201_TOf( In := WPU201_AutoCmdIn,**
**PT := dint_to_time(1000) );**
**Par.WPU201.AutoCmd := WPU201_AutoCmdIn and Par.WPU201V.StatRun;**
**Par.WPU201V.AutoCmd := WPU201_AutoCmdIn or WPU201_TOf.Q;**

| **Name**                                  | **Data Type** | **Initial Value** | **Parameter**                    |
|-------------------------------------------|---------------|-------------------|----------------------------------|
| PriorityCmd_1                             | Bool          | False             | **Par.WPU201V.StatStop** |
| PriorityCmd_1Conf | dint          | 1                 | **3**                            |
| PriorityCmd_1Text                         | string\[30\]  | 'Prio01'  | **'Koelventilator'**     |
