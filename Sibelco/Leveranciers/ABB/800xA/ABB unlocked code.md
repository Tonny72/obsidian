- created: [[2017-02-10]]
  tags:: 800xA
- # DriveStatusReceive
- ## Parameters
  | **Status**          | **dint** | **by_ref** | **in** | **** | **Main status word (Connect to Drive data)**          |
  |---------------------|----------|------------|--------|-------|-------------------------------------------------------|
  | **RawPv1**          | dint     | by_ref     | in     |      | Raw process value speed (Connect to Drive data)       |
  | **DriveMaxMin1**    | real     | retain     | in     | 20000 | Drive signal 1 range (value, -value)                  |
  | **RawPv2**          | dint     | by_ref     | in     |      | Raw process value arbitrary (Connect to Drive data)   |
  | **DriveMaxMin2**    | real     | retain     | in     | 20000 | Drive signal 2 range (value, -value)                  |
  | **ReadyToSwitchOn** | bool     | by_ref     | out    |      | Drive is ready to be switched on                      |
  | **Ready**           | bool     | by_ref     | out    |      | Ready to operate (SW bit1)                            |
  | **Run**             | bool     | by_ref     | out    |      | Operation enabled (SW bit 2)                          |
  | **AtSetpoint**      | bool     | by_ref     | out    |      | Operating within reference value tolerance (SW bit 8) |
  | **Remote**          | bool     | by_ref     | out    |      | Remote Control location (SW bit 9)                    |
  | **Overrideped**     | bool     | by_ref     | out    |      | Overrideped , Fault (SW bit 3)                        |
  | **Alarm**           | bool     | by_ref     | out    |      | Drive Warning/Alarm (SW bit 7)                        |
  | **Limit**           | bool     | by_ref     | out    |      | Above_limit (SW bit 10)                               |
  | **SP2Used**         | bool     | by_ref     | out    |      | Setpoint 2 used in drive (SW bit 11)                  |
  | **Pv1**             | real     | by_ref     | out    |      | Process value 1 (ex Speed)                            |
  | **Pv1MaxMin**       | real     | by_ref     | in     | 100   | Pv1 range (value, -value)                             |
  | **Pv2**             | real     | by_ref     | out    |      | Process value 2                                       |
  | **Pv2MaxMin**       | real     | by_ref     | in     | 100   | Pv2 range (value, -value)                             |
  | **StatusW**         | dword    | by_ref     | out    |      | Main status word                                      |
  | **ObjectTest**      | bool     | by_ref     | in     |      | Indicates ObjectTest                                  |
  | **SwitchedOn**      | bool     | by_ref     | in     |      | Indicates simulated SwitchedOn                        |
  | **Started**         | bool     | by_ref     | in     |      | Indicates simulated Started                           |
  | **SpdSP**           | real     | by_ref     | in     |      | Indicates speed reference                             |
  
  Variables
  | **RawPv1Int**                | **dint** | **retain** | **** | **** |
  |------------------------------|----------|------------|-------|-------|
  | **RawPv2Int**                | dint     | retain     |      |      |
  | **RawPv1Loc**                | real     | retain     |      |      |
  | **RawPv2Loc**                | real     | retain     |      |      |
  | **Ts**                       | real     | retain     |      |      |
  | **FirstScan**                | bool     | retain     | TRUE  |      |
  | **Starting**                 | bool     | retain     |      |      |
  | **SwitchedOnAndStartedOld**  | bool     | retain     |      |      |
  | **SwitchedOnAndStartedOld1** | bool     | retain     |      |      |
  
  ```
  Code
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
- # DriveSendCommand
- ## Parameters
  
  | **Command**      | **dint** | **by_ref** | **out** | **** | **Main control word (Connect to Drive data)**                        |
  |------------------|----------|------------|---------|-------|----------------------------------------------------------------------|
  | **RawSP1**       | dint     | by_ref     | out     |      | Raw setpoint 1 (Connect to Drive data)                               |
  | **DriveMaxMin1** | real     | retain     | in      | 20000 | Drive signal 1 range (value, -value)                                 |
  | **RawSP2**       | dint     | by_ref     | out     |      | Raw setpoint 2 (Connect to Drive data)                               |
  | **DriveMaxMin2** | real     | retain     | in      | 20000 | Drive signal 2 range (value, -value)                                 |
  | **SwitchOn**     | bool     | retain     | in      |      | Swich on order (level signal with hold function)                     |
  | **SwitchOff**    | bool     | retain     | in      |      | Swich off order (Higher priority than switch on order)               |
  | **Start**        | bool     | retain     | in      |      | Start order (level signal with hold function)                        |
  | **Stop**         | bool     | retain     | in      |      | Stop order (Higher priority than start order)                        |
  | **Reset**        | bool     | retain     | in      |      | Reset order drive                                                    |
  | **Off2**         | bool     | retain     | in      |      | Emergency stop                                                       |
  | **Off3**         | bool     | retain     | in      |      | Emergency stop (Ramping down according to settings locally in drive) |
  | **RampOutZero**  | bool     | by_ref     | in      | TRUE  | If false: Ramp function generator is set to zero                     |
  | **RampHold**     | bool     | by_ref     | in      | TRUE  | Enables ramp function generator                                      |
  | **Inching1**     | bool     | by_ref     | in      | TRUE  | Drive accelerates as fast as possible to inching setpoint1           |
  | **Inching2**     | bool     | by_ref     | in      | TRUE  | Drive accelerates as fast as possible to inching setpoint2           |
  | **RemoteCmd**    | bool     | by_ref     | in      | TRUE  | Overriding computer is requesting to control the drive               |
  | **UseSP2**       | bool     | by_ref     | in      | TRUE  | Used setpoint                                                        |
  | **SP1**          | real     | by_ref     | in      | 0     | Setpoint 1                                                           |
  | **SP1MaxMin**    | real     | by_ref     | in      | 100   | SP1 range (value, -value)                                            |
  | **SP2**          | real     | by_ref     | in      | 0     | Setpoint 2                                                           |
  | **SP2MaxMin**    | real     | by_ref     | in      | 100   | SP2 range (value, -value)                                            |
  | **Pv1**          | real     | retain     | in      | 0     | Process value 1 (ex Speed)                                           |
  | **ZeroWinPv1**   | real     | by_ref     | in      | 0.04  | Window were the ramping function treats Pv1 as Zero                  |
  | **StatusW**      | dword    | by_ref     | in      |      | Main status word                                                     |
- ## Varariables
  | **FaultResetPeriod**   | **time** | **constant hidden** | **2s** | **** |
  |------------------------|----------|---------------------|--------|-------|
  | **Reseting**           | bool     | hidden              | 0      |      |
  | **StopOrderGiven**     | bool     | retain hidden       |       |      |
  | **StartOrderGiven**    | bool     | retain hidden       |       |      |
  | **SwitchOnOrderGiven** | word     | retain hidden       | 1      |      |
  | **CommandW**           | word     |                    |       |      |
- ## Function Blocks
  | **FaultReset** | **TP** | **** | **Used by reseting functionality** |
  |----------------|--------|-------|------------------------------------|
  
  ```
  Code – Control
  IF FirstScanAfterPowerUp() THEN
  StopOrderGiven := false;
  StartOrderGiven := false;
  END_IF;
  (\* Fault Reset logic \*)
  FaultReset( In := Reset,
  PT := FaultResetPeriod,
  Q =\> Reseting );
  IF Reseting THEN
  (\* Set reset bit = 7 \*)
  CommandW := CommandW OR 16#80;
  (\* Prevent that a emergency stopped drive don't starts direct after resetnig
  if not the drive is orderd to it. Clear start bit = 3 \*)
  CommandW := CommandW AND NOT 16#8;
  (\* Make sure that Off1 bit = 0 in cw-word is toggeld when the drive
  is not ready_to Switch On (bit = 0) or is Inibited to start bit = 6.
  Do this when the Reset is commanded. \*)
  IF not((StatusW and 16#41) = 1) THEN
  CommandW := CommandW AND 16#FFFE;
  END_IF;
  StartOrderGiven := False;
  ELSE
  if SwitchOn then
  SwitchOnOrderGiven := 1;
  else
  SwitchOnOrderGiven := 0;
  end_if;
  if (StatusW and 1) = 0 then
  SwitchOnOrderGiven := 0;
  end_if;
  CommandW:= CommandW AND 16#FF7E OR SwitchOnOrderGiven; (\* no reset order any more \*)
  END_IF;
  (\* If the drive is stopped in not remote (local) mode the drive should not start
  again if there is not a start order. The drive should also contuine to run if
  the drive is started in local mode and then becomes remote if the drive is allowed
  to this according to the below conditions \*)
  IF (StatusW AND 16#204) = 16#0 THEN (\*not remote and not run \*)
  CommandW := CommandW AND 16#FFF7;
  ELSIF NOT Stop AND (StatusW AND 16#4) = 16#4 THEN (\*not stop and run \*)
  CommandW:= CommandW OR 8;
  END_IF;
  (\* Start and stop of drive ramping functionality included
  Check if drive should be stopped \*)
  IF Stop OR (StopOrderGiven AND NOT Start) THEN
  StartOrderGiven := False;
  StopOrderGiven := true;
  CommandW := CommandW AND 16#FFF7 OR 16#40;
  (\* Check if drive is allowed to be started \*)
  ELSIF (Start OR StartOrderGiven) and (StatusW AND 16#23B) = 16#233 THEN
  StartOrderGiven := True;
  StopOrderGiven := false;
  CommandW:= CommandW OR 16#48;
  END_IF;
  ```
  
  Code – Out
  ```
  (\* calculate and scale setpoints into drive range\*)
  if SP1 \>= SP1MaxMin then
  RawSP1 := real_to_dint(DriveMaxMin1);
  elsif SP1 \<= -SP1MaxMin then
  RawSP1 := real_to_dint(-DriveMaxMin1);
  else
  RawSP1 := real_to_dint(SP1 / SP1MaxMin \* DriveMaxMin1);
  end_if;
  if SP2 \>= SP2MaxMin then
  RawSP2 := real_to_dint(DriveMaxMin2);
  elsif SP2 \<= -SP2MaxMin then
  RawSP2 := real_to_dint(-DriveMaxMin2);
  else
  RawSP2 := real_to_dint(SP2 / SP2MaxMin \* DriveMaxMin2);
  end_if;
  
  (\* Assign data to Command Word 1 \*)
  IF Off2 THEN
  CommandW:= CommandW or 2;
  ELSE
  CommandW := CommandW and 16#FFFD;
  END_IF;
  IF Off3 THEN
  CommandW:= CommandW or 4;
  ELSE
  CommandW := CommandW and 16#FFFB;
  END_IF;
  IF RampOutZero THEN
  CommandW:= CommandW or 16#10;
  ELSE
  CommandW := CommandW and 16#FFEF;
  END_IF;
  IF RampHold THEN
  CommandW:= CommandW or 16#20;
  ELSE
  CommandW := CommandW and 16#FFDF;
  END_IF;
  IF Inching1 THEN
  CommandW:= CommandW or 16#100;
  ELSE
  CommandW := CommandW and 16#FEFF;
  END_IF;
  IF Inching2 THEN
  CommandW:= CommandW or 16#200;
  ELSE
  CommandW := CommandW and 16#FDFF;
  END_IF;
  IF RemoteCmd THEN
  CommandW:= CommandW or 16#400;
  ELSE
  CommandW := CommandW and 16#FBFF;
  END_IF;
  IF UseSP2 THEN
  CommandW:= CommandW or 16#800;
  ELSE
  CommandW := CommandW and 16#F7FF;
  END_IF;
  (\* Set the output \*)
  Command := dword_to_dint(CommandW);
  ```
- # UniCore
- ## Variables
  | **RunInit**                  | **bool** | **retain hidden** | **TRUE** |                                                         |
  |------------------------------|----------|-------------------|----------|----------------------------------------------------------|
  | **PanModeOld**               | bool     | retain hidden     |         | Edge on the parameter PanMode                            |
  | **Helpmem1**                 | bool     | retain hidden     |         |                                                         |
  | **PulseTime**                | time     | retain hidden     |         |                                                         |
  | **PulsMem1**                 | bool     | retain hidden     |         |                                                         |
  | **PulsMem0**                 | bool     | retain hidden     |         |                                                         |
  | **PulseTimer**               | Timer    | retain hidden     |         |                                                         |
  | **Ilock0Loc**                | bool     | retain hidden     |         |                                                         |
  | **Ilock1Loc**                | bool     | retain hidden     |         |                                                         |
  | **GroupStartILockLoc**       | bool     | retain hidden     |         |                                                         |
  | **GroupStartObjectStartOld** | bool     | retain hidden     |         |                                                         |
  | **PriorityModeLoc**          | bool     | retain hidden     |         |                                                         |
  | **PriorityCmd0Loc**          | bool     | retain hidden     |         |                                                         |
  | **PriorityCmd1Loc**          | bool     | retain hidden     |         |                                                         |
  | **PriorityCmdMan1Loc**       | bool     | retain hidden     |         |                                                         |
  | **PriorityCmdMan0Loc**       | bool     | retain hidden     |         |                                                         |
  | **OutLoc0**                  | bool     | retain hidden     |         |                                                         |
  | **ChangeTimeElapsed**        | bool     | retain hidden     |         | ChangeOverTime has Elapsed                               |
  | **ModeBeforeObjectTest**     | dint     | retain hidden     |         | True if Auto Mode before ObjectTest                      |
  | **ObjectTestOld**            | bool     | retain hidden     |         |                                                         |
  | **ModeLoc**                  | dint     | retain hidden     |         | Local storage of mode to return to after pan or loc mode |
  | **Status1**                  | dword    | retain hidden     |         |                                                         |
  | **FBTimeLoc**                | time     | retain hidden     |         |                                                         |
  | **AlarmAckedOld**            | bool     | retain hidden     |         |                                                         |
  | **EnableObjectAlarmOld**     | bool     | retain hidden     |         |                                                         |
  | **Out1xLevel**               | bool     | retain hidden     |         |                                                         |
  | **SetAutoPOld**              | bool     | retain hidden     |         |                                                         |
  | **StatusOld**                | dword    | retain hidden     | `16#C0`    |                                                         |
  | **EnableOld**                | bool     | retain hidden     |         |                                                         |
  | **GroupStartModeCnt**        | dint     | retain hidden     |         |                                                         |
  | **T0**                       | time     | retain hidden     | `TIME#0s`  |                                                         |
  | **FBConfigInt**              | dint     | retain hidden     |         |                                                         |
  | **FBTimeInt**                | time     | retain hidden     |         |                                                         |
  | **AEConfigInt**              | dint     | retain hidden     |         |                                                         |
  | **AlStateInt**               | dint     | retain hidden     |         |                                                         |
- ## Function blocks
  | ACOFUnit    | ACOFUnit   |
  |-------------|------------|
  | FBPulseOut1 | FBPulseOut |
- ## Code
  ```
  ParError := false;
  if EnableParError then
  (\* Parameter range test \*)
  if AlState \< 0 or AlState \> 6 then
  AlStateInt := 6;
  ParError := true;
  else
  AlStateInt := AlState;
  end_if;
  if FBTime \< T0 then
  FBTimeInt := T0;
  ParError := true;
  else
  FBTimeInt := FBTime;
  end_if;
  if AEConfig \< 0 or AEConfig \> 4 then
  AEConfigInt := 1;
  ParError := true;
  else
  AEConfigInt := AEConfig;
  end_if;
  if FBConfig \< 0 or FBConfig \> 6 then
  FBConfigInt := 0;
  ParError := true;
  else
  FBConfigInt := FBConfig;
  end_if;
  else
  AlStateInt := AlState;
  FBTimeInt := FBTime;
  AEConfigInt := AEConfig;
  FBConfigInt := FBConfig;
  end_if;
  
  If RunInit then
  RunInit := false;
  If ManModeInit then
  ModeLoc := 3;
  Else
  ModeLoc := 4;
  End_if;
  End_if;
  
  If Enable and not FirstScanAfterPowerUp() then
  
  (\*\*\*\*\*\*\*\*\*\*\* Toggles panMode from the operator interface \*\*\*\*\*\*\*\*\*\*\*);
  
  if LocMode or PriorityMode or not PanExists then
  PanModeAct := false;
  else
  
  if not PanMode and PanModeOld and not LocMode then
  OpPanelMode := false;
  end_if;
  
  PanModeOld := PanMode;
  PanModeAct := PanMode or OpPanelMode;
  end_if;
  
  Forced := FB0.Forced or FB1.Forced or Out0.Forced or Out1.Forced;
  Status := (FB0.Status or FB1.Status or Out0.Status or Out1.Status or ExtStatus) and 16#FFFFFF00;
  
  if (FB0.Status and 16#FF) \> (FB1.Status and 16#FF) then
  Status1 := (FB1.Status and 16#FF);
  else
  Status1 := (FB0.Status and 16#FF);
  end_if;
  
  if Status1 \> (Out0.Status and 16#FF) then
  Status1 := (Out0.Status and 16#FF);
  end_if;
  
  if Status1 \> (Out1.Status and 16#FF) then
  Status1 := (Out1.Status and 16#FF);
  end_if;
  
  if Status1 \> (ExtStatus and 16#FF) then
  Status1 := (ExtStatus and 16#FF);
  end_if;
  
  Status := Status or Status1;
  ```
  
  ```
  
  (\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Inhibit signal \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)
  
  Ilock0Loc := Ilock0;
  Ilock1Loc := Ilock1;
  GroupStartILockLoc := GroupStartILock;
  PriorityCmd0Loc := PriorityCmd0;
  PriorityCmd1Loc := PriorityCmd1;
  PriorityCmdMan0Loc := PriorityCmdMan0;
  PriorityCmdMan1Loc := PriorityCmdMan1;
  PriorityModeLoc := PriorityMode;
  
  If Inhibit then
  Ilock0Loc := false;
  Ilock1Loc := false;
  GroupStartILockLoc := false;
  PriorityCmd0Loc := false;
  PriorityCmd1Loc := false;
  PriorityCmdMan0Loc := false;
  PriorityCmdMan1Loc := false;
  PriorityModeLoc := false;
  End_if;
  
  (\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Interlock signal \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*)
  
  Out1xLevel := Out1IOLevel and Out1.Forced or Out1Level and not Out1.Forced;
  
  Interlock := (PriorityModeLoc or
  (((Ilock0 and Out1xLevel) or
  (not Out1xLevel and Ilock1)))) and not LocMode and not Inhibit;
  
  (\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Mode Selection \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*);
  
  If SetMan then
  ModeLoc := 3;
  elsif PanMode or PriorityModeLoc then
  (\* Do nothing \*)
  elsif (SetAutoP and not SetAutoPOld or SetAuto) and not LocMode and not PanMode then
  ModeLoc := 4;
  elsif (SetGroupStart or GroupStartObject.Forward.SelectGroupStart) and not GroupStartILockLoc then
  ModeLoc := 5;
  elsif SetOutOfService and Out0Indication then
  ModeLoc := 6;
  OpPanelMode := false;
  End_if;
  
  If LocMode then
  ObjMode := 0;
  elsif PriorityModeLoc then
  ObjMode := 1;
  elsif PanModeAct then
  ObjMode := 2;
  else
  ObjMode := ModeLoc;
  End_if;
  
  ManMode := ObjMode = 3 and GroupStartObject.Forward.EnableModeSwitch;
  AutoMode := ObjMode = 4 and GroupStartObject.Forward.EnableModeSwitch;
  GroupStartMode := ObjMode =5 and GroupStartObject.Forward.EnableModeSwitch;
  OutOfServiceMode := ObjMode =6 and GroupStartObject.Forward.EnableModeSwitch;
  
  GroupStartObject.Backward.Ready := ObjMode = 5;
  GroupStartObject.Backward.Connected := true;
  
  (\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Real boolean IO Output \*\*\*\*\*\*\*\*\*\*\*\*)
  
  if PulseOut then
  Out1IOLevel := Out1.IOValue or Out1IOLevel and not Out0.IOValue;
  else
  Out1IOLevel := Out1.IOValue;
  End_if;
  
  (\* Out displays \*)
  
  if ObjectTest then
  Out1Indication := Out1Level;
  elsif Out1.Forced then
  if PulseOut then
  if Out0.Forced Then
  Out1Indication := Out1IOLevel and not Out0.IOValue;
  else
  Out1Indication := Out1IOLevel and not Out0.Value;
  end_if;
  else
  Out1Indication := Out1.IOValue;
  end_if;
  else
  if PulseOut then
  if Out0.Forced Then
  Out1Indication := Out1Level and not Out0.IOValue;
  else
  Out1Indication := Out1Level and not Out0.Value;
  end_if;
  else
  Out1Indication := Out1.Value;
  end_if;
  end_if;
  
  if ObjectTest then
  Out0Indication := not Out1Level;
  elsif Out0.Forced then
  Out0Indication := Out0.IOValue or PulseOut and not Out1Level;
  else
  Out0Indication := Out0.Value or PulseOut and not Out1Level;
  end_if;
  
  (\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Feedback signals \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*);
  
  if ObjectTest then
  EffectiveFB1 := Out1Level;
  EffectiveFB0 := not Out1Level ;
  else
  If FBConfigInt = 0 then
  EffectiveFB1 := FB1.Value;
  EffectiveFB0 := FB0.Value ;
  elsif FBConfigInt = 1 then
  EffectiveFB1 := FB1.Value;
  EffectiveFB0 := Not FB1.Value;
  elsif FBConfigInt = 2 then
  EffectiveFB1 := not FB1.Value;
  EffectiveFB0 := FB1.Value;
  elsif FBConfigInt = 3 then
  EffectiveFB1 := not FB1.Value;
  EffectiveFB0 := not FB0.Value;
  elsif FBConfigInt = 4 then
  EffectiveFB1 := not FB0.Value;
  EffectiveFB0 := FB0.Value;
  elsif FBConfigInt = 5 then
  EffectiveFB1 := FB0.Value;
  EffectiveFB0 := not FB0.Value;
  else (\* No FeedBack \*)
  EffectiveFB1 := Out1IOLevel;
  EffectiveFB0 := Not EffectiveFB1;
  End_if;
  end_if;
  if ((Status and 16#FF) = 16#C0 and (StatusOld and 16#FF) \<\> 16#C0)
  or FirstScanAfterPowerUp() or
  (Enable and not EnableOld) then
  
  If EffectiveFB0 then
  Out1Level := false;
  Elsif EffectiveFB1 then
  Out1Level := true;
  End_if;
  
  End_if;
  StatusOld := Status;
  
  (\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Manouver selection 1 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*);
  
  If OutOfServiceMode then
  
  (\* Out of Service Mode activations \*);
  
  Out1Level := false;
  GroupStartObjectStartOld := GroupStartObject.Forward.Start;
  
  Elsif PriorityCmdMan0Loc or PriorityCmdMan1Loc then
  
  (\* Priority Man activations \*);
  
  If PriorityCmdMan0Loc then
  Out1Level := false;
  Elsif PriorityCmdMan1Loc then
  Out1Level := true;
  End_if;
  GroupStartObjectStartOld := GroupStartObject.Forward.Start;
  
  ModeLoc := 3;
  
  Elsif PriorityModeLoc then
  
  (\* Priority Mode activations \*);
  
  If PriorityCmd0Loc then
  Out1Level := false;
  Elsif PriorityCmd1Loc then
  Out1Level := true;
  End_if;
  GroupStartObjectStartOld := GroupStartObject.Forward.Start;
  
  Elsif LocMode then
  
  (\* Local Mode activations \*);
  
  If EffectiveFB0 then
  Out1Level := false;
  Elsif EffectiveFB1 then
  Out1Level := true;
  End_if;
  GroupStartObjectStartOld := GroupStartObject.Forward.Start;
  
  Elsif PanModeAct then
  
  (\* Panel mode activations \*);
  
  If PanCmd0 and Not Ilock0Loc then
  Out1Level := false;
  Elsif PanCmd1 and Not Ilock1Loc then
  Out1Level := true;
  End_if;
  GroupStartObjectStartOld := GroupStartObject.Forward.Start;
  
  Elsif ManMode then
  
  (\* Manual mode activations \*);
  
  If (ManCmd0 or ManCmd0E) and Not Ilock0Loc then
  Out1Level := false;
  Elsif (ManCmd1 or ManCmd1E) and Not Ilock1Loc then
  Out1Level := true;
  End_if;
  GroupStartObjectStartOld := GroupStartObject.Forward.Start;
  
  Elsif AutoMode then
  
  (\* Auto mode activations \*);
  
  If AutoCmd0 and Not Ilock0Loc then
  Out1Level := false;
  Elsif AutoCmd1 and Not Ilock1Loc then
  Out1Level := true;
  End_if;
  GroupStartObjectStartOld := GroupStartObject.Forward.Start;
  
  Elsif GroupStartModeCnt = 2 then
  
  (\* GroupStart mode activations \*);
  
  If not GroupStartObject.Forward.Start and Not Ilock0Loc then
  Out1Level := false;
  Elsif GroupStartObject.Forward.Start and not GroupStartObjectStartOld and Not Ilock1Loc then
  Out1Level := true;
  End_if;
  
  GroupStartObjectStartOld := GroupStartObject.Forward.Start;
  
  else
  
  GroupStartObjectStartOld := false;
  
  End_if;
  if ObjMode =5 then
  if GroupStartModeCnt \< 2 then
  GroupStartModeCnt := GroupStartModeCnt + 1;
  end_if;
  else
  GroupStartModeCnt := 0;
  end_if;
  
  if (AlStateInt = 2 or AlStateInt = 4) and not AlarmAckedOld then
  GroupStartObjectStartOld := false;
  end_if;
  AlarmAckedOld := AlStateInt = 2 or AlStateInt = 4;
  
  GroupStartObject.Backward.Started := EffectiveFB1;
  GroupStartObject.Backward.Stopped := EffectiveFB0;
  GroupStartConnected := GroupStartObject.Forward.Connected;
  
  (\* StatActiv / StatDeActiv \*);
  
  StatAct := Out1Level And EffectiveFB1 And Not EffectiveFB0 ;
  
  StatDeAct := Not Out1Level and EffectiveFB0 and Not EffectiveFB1;
  
  (\* Configuration and setting of Out signal \*)
  
  If PulseOut then
  
  (\* Pulsed outsignals \*)
  
  OutLoc0 := not Out1Level;
  
  If ObjectTest and Not Ilock0Loc then
  OutLoc0 := True;
  End_if;
  
  FBPulseOut1( In0 := OutLoc0,
  In1 := Out1Level and not OutLoc0,
  PulseTime := FBTimeInt );
  
  (\* Pulse Out1 \*)
  
  If FBPulseOut1.Out1Pulse and not(StatAct and FBConfigInt \< 4) then
  Out0.Value:=false;
  Out1.Value:=true;
  Else
  Out1.Value:= false;
  End_if;
  
  (\* Pulse Out0 \*)
  
  If FBPulseOut1.Out0Pulse and not(StatDeact and ((FBConfigInt = 0 or FBConfigInt \> 3) and FBConfigInt \< 6)) then
  Out0.Value:=true;
  Out1.Value:=false;
  Else
  Out0.Value:= false;
  End_if;
  
  Else
  
  Out1.Value := Out1Level;
  Out0.Value := not Out1Level;
  End_if;
  
  (\* ObjectTest \*)
  
  If (ObjectTest or ObjectTestOld) and not Ilock0Loc then
  
  Out1.Value := false;
  
  if not PulseOut then
  Out0.Value := true;
  end_if;
  
  End_if;
  
  If ObjectTest and not ObjectTestOld and Not Ilock0Loc then
  ModeBeforeObjectTest := ModeLoc;
  Out1Level := false;
  End_if;
  
  If not ObjectTest and ObjectTestOld and Not Ilock0Loc then
  ModeLoc := ModeBeforeObjectTest;
  Out1Level := false;
  End_if;
  
  If ObjectTest then
  StatAct := Out1Level;
  StatDeAct := not Out1Level;
  End_if;
  
  ObjectTestOld := ObjectTest;
  
  (\* ACOFActivate FB \*)
  
  IF FBConfigInt \>= 4 THEN
  (\* FB1 does not exist \*)
  ACOFUnit.AutoActivated := EffectiveFB0;
  else
  ACOFUnit.AutoActivated := true;
  END_IF;
  
  IF FBConfigInt = 1 or FBConfigInt = 2 or FBConfigInt = 6 THEN
  (\* FB0 does not exist \*)
  ACOFUnit.AutoDeactivated := EffectiveFB1;
  else
  ACOFUnit.AutoDeactivated := true;
  END_IF;
  
  FBTimeLoc := FBTimeInt;
  
  ACOFUnit( ElapsedTime := ElapsedTime,
  SupDel := FBTimeLoc,
  Enable := not (ObjectTest or OutOfServiceMode),
  Activate := Out1Level,
  AutoDeactivate := Out1Level,
  Activated := EffectiveFB1,
  Deactivated := EffectiveFB0,
  EnableParError := EnableParError );
  if EnableParError then
  ParError := ParError or ACOFUnit.ParError;
  end_if;
  
  if GroupStartObject.Forward.EnableObjectAlarm and not EnableObjectAlarmOld or not GroupStartObject.Forward.EnableObjectAlarm and EnableObjectAlarmOld then
  EnableObjErr := GroupStartObject.Forward.EnableObjectAlarm;
  end_if;
  EnableObjectAlarmOld := GroupStartObject.Forward.EnableObjectAlarm;
  
  (\* Sum Error \*)
  ObjErrEnabled := AEConfigInt \> 0 AND EnableObjErr AND EnableObjErrP;
  OEDisabled := AEConfigInt \< 1 or AEConfigInt \> 5 or LocMode or OutOfServiceMode or (not EnableSupOut and not ObjErrEnabled);
  AlarmDisabled := AEConfigInt \<\> 1 or (AlStateInt = 1 and AEConfigInt = 1) or LocMode or OutOfServiceMode or not ObjErrEnabled;
  ObjErrLoc := ACOFUnit.Alarm or ExtErr;
  ObjErr := ObjErrLoc and not OEDisabled;
  ObjErrStat := ObjErr AND ObjErrEnabled;
  
  GroupStartObject.Backward.AlarmInObject := AlStateInt =3 or AlStateInt = 5;
  
  Else
  
  EffectiveFB1 := false;
  EffectiveFB0 := false;
  ElapsedTime := cPOLConstants2.ZeroTime;
  Out1.Value := false;
  Out0.Value := false;
  Out1level := false;
  Out1IOLevel := false;
  Out1Indication := false;
  Out0Indication := false;
  Interlock := false;
  Forced := false;
  Status := 16#C0;
  PanModeAct := false;
  ObjErrLoc := false;
  ObjErr := false;
  OEDisabled := false;
  AlarmDisabled := false;
  StatAct := false;
  StatDeAct := false;
  ManMode := false;
  AutoMode := false;
  GroupStartMode := false;
  OutOfServiceMode := false;
  ObjMode := 3;
  ModeLoc := 3;
  ObjectTestOld := ObjectTest;
  
  End_if;
  
  EnableOld := Enable;
  SetAutoPOld := SetAutoP;
  
  (\* Reset the commands \*)
  
  SetOutOfService := false;
  SetAuto := false;
  SetMan := false;
  SetGroupStart := false;
  ManCmd1 := false;
  ManCmd0 := false;
  GroupStartObject.Forward.SelectGroupStart := false;
  
  ```
  
  *From \<<https://sibelco-my.sharepoint.com/personal/tonny_lemmens_sibelco_com/Documents/DEV/ABB/ABB%20unlocked%20code.docx>\>*