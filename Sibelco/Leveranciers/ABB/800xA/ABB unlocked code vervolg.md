---
created: [[2017-02-10]]T15:17:48.0000000+01:00
---

- # Parameters
  
  | **Status**          | **dint** | **by_ref** | **in** | ****  | **Main status word (Connect to Drive data)**    |
  | ------------------------- | -------------- | ---------------- | ------------ | ----- | ----------------------------------------------------- |
  | **RawPv1**          | dint           | by_ref           | in           |       | Raw process value speed (Connect to Drive data)       |
  | **DriveMaxMin1**    | real           | retain           | in           | 20000 | Drive signal 1 range (value, -value)                  |
  | **RawPv2**          | dint           | by_ref           | in           |       | Raw process value arbitrary (Connect to Drive data)   |
  | **DriveMaxMin2**    | real           | retain           | in           | 20000 | Drive signal 2 range (value, -value)                  |
  | **ReadyToSwitchOn** | bool           | by_ref           | out          |       | Drive is ready to be switched on                      |
  | **Ready**           | bool           | by_ref           | out          |       | Ready to operate (SW bit1)                            |
  | **Run**             | bool           | by_ref           | out          |       | Operation enabled (SW bit 2)                          |
  | **AtSetpoint**      | bool           | by_ref           | out          |       | Operating within reference value tolerance (SW bit 8) |
  | **Remote**          | bool           | by_ref           | out          |       | Remote Control location (SW bit 9)                    |
  | **Overrideped**     | bool           | by_ref           | out          |       | Overrideped , Fault (SW bit 3)                        |
  | **Alarm**           | bool           | by_ref           | out          |       | Drive Warning/Alarm (SW bit 7)                        |
  | **Limit**           | bool           | by_ref           | out          |       | Above_limit (SW bit 10)                               |
  | **SP2Used**         | bool           | by_ref           | out          |       | Setpoint 2 used in drive (SW bit 11)                  |
  | **Pv1**             | real           | by_ref           | out          |       | Process value 1 (ex Speed)                            |
  | **Pv1MaxMin**       | real           | by_ref           | in           | 100   | Pv1 range (value, -value)                             |
  | **Pv2**             | real           | by_ref           | out          |       | Process value 2                                       |
  | **Pv2MaxMin**       | real           | by_ref           | in           | 100   | Pv2 range (value, -value)                             |
  | **StatusW**         | dword          | by_ref           | out          |       | Main status word                                      |
  | **ObjectTest**      | bool           | by_ref           | in           |       | Indicates ObjectTest                                  |
  | **SwitchedOn**      | bool           | by_ref           | in           |       | Indicates simulated SwitchedOn                        |
  | **Started**         | bool           | by_ref           | in           |       | Indicates simulated Started                           |
  | **SpdSP**           | real           | by_ref           | in           |       | Indicates speed reference                             |
- # Variables
  
  | **RawPv1Int**                | **dint** | **retain** | **** | **** |
  | ---------------------------------- | -------------- | ---------------- | ---- | ---- |
  | **RawPv2Int**                | dint           | retain           |      |      |
  | **RawPv1Loc**                | real           | retain           |      |      |
  | **RawPv2Loc**                | real           | retain           |      |      |
  | **Ts**                       | real           | retain           |      |      |
  | **FirstScan**                | bool           | retain           | TRUE |      |
  | **Starting**                 | bool           | retain           |      |      |
  | **SwitchedOnAndStartedOld**  | bool           | retain           |      |      |
  | **SwitchedOnAndStartedOld1** | bool           | retain           |      |      |
- hallo
  
  ```python-repl
  
  SampleTime( Ts =\> Ts,
  FirstScan := FirstScan );
  FirstScan := false;
  if ObjectTest then
   StatusW := 16#301; (\* Indicate 'Remote', 'ReadyToSwitchOn' and 'AtSetpoint' \*)
  if SwitchedOn and Started then
   if not SwitchedOnAndStartedOld1 then
  Starting := true;
  end_if;
  if SpdSP \> RawPv1Loc then
  RawPv1Loc:= RawPv1Loc + SpdSP/10.0 \* Ts;
  IF RawPv1Loc \>= SpdSP THEN
  RawPv1Loc:= SpdSP;
  Starting := false;
  END_IF;
  else
  RawPv1Loc:= RawPv1Loc - SpdSP/10.0 \* Ts;
  IF RawPv1Loc \<= SpdSP THEN
  RawPv1Loc:= SpdSP;
  Starting := false;
  END_IF;
  end_if;
  if Starting then
  RawPv2Loc:= RawPv2Loc + DriveMaxMin2/20.0 \* Ts;
  IF RawPv2Loc \> DriveMaxMin2 THEN
  RawPv2Loc:= DriveMaxMin2;
  END_IF;
  end_if;
  StatusW := StatusW or 16#6; (\* Indicate 'Ready' and 'Run' \*)
  else
  if SwitchedOn then
  StatusW := StatusW or 16#2; (\* Indicate 'Ready' \*)
  end_if;
  RawPv1Loc:= RawPv1Loc - DriveMaxMin1/10.0 \* Ts;
  IF RawPv1Loc \< 0.0 THEN
  RawPv1Loc:= 0.0;
  END_IF;
  RawPv2Loc:= 0.0;
  Starting := false;
  end_if;
  RawPv1Int := real_to_dint(RawPv1Loc);
  RawPv2Int := real_to_dint(RawPv2Loc);
  SwitchedOnAndStartedOld1 := SwitchedOnAndStartedOld;
  SwitchedOnAndStartedOld := SwitchedOn and Started;
  else
  (\* Get data from main status word 1 \*)
  StatusW := dint_to_dword(Status);
  RawPv1Int := RawPv1;
  RawPv2Int := RawPv2;
  end_if;
  (\* Translate status word \*)
  ReadyToSwitchOn := (StatusW and 1) = 1;
  Ready := (StatusW and 2) = 2;
  Run := (StatusW and 4) = 4;
  Overrideped := (StatusW and 8) = 8;
  AtSetpoint := (StatusW and 16#100) = 16#100;
  Alarm := (StatusW and 16#80) = 16#80;
  Remote := (StatusW and 16#200) = 16#200;
  Limit := (StatusW and 16#400) = 16#400;
  SP2Used := (StatusW and 16#800) = 16#800;
  (\* Get raw process values 1 & 2 and convert them with its ranges \*)
  Pv1 := dint_to_real(RawPv1Int)/DriveMaxMin1\*Pv1MaxMin;
  Pv2 := dint_to_real(RawPv2Int)/DriveMaxMin2\*Pv2MaxMin;
  ```
  
  *From \<[https://sibelco-my.sharepoint.com/personal/tonny_lemmens_sibelco_com/Documents/DEV/ABB/Document1.docx](https://sibelco-my.sharepoint.com/personal/tonny_lemmens_sibelco_com/Documents/DEV/ABB/Document1.docx)\>*