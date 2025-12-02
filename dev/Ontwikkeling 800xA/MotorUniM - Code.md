---
title: MotorUniM - Code
updated: [[2017-12-05]]T16:31:25.0000000+01:00
created: [[2017-12-05]]T16:29:22.0000000+01:00
---

- # Code
  if Init then
  Init := false;
  EnParError := EnableParError or GetApplicationSIL() \<\> 0;
  ParErrorInternal := false;
  end_if;
  
  (\* Parameter range test \*)
  ParErrorInternal := false;
  if EnParError then
  if AEConfig \< 0 or AEConfig \> 4 then
  AEConfigInt := 1;
  ParErrorInternal := true;
  else
  AEConfigInt := AEConfig;
  end_if;
  else
  AEConfigInt := AEConfig;
  end_if;
  
  (\* Vote interface logic \*)
  
  VotedCmdLoc.Forward := VotedCmd.Forward;
  
  InternalInhibit := Inhibit or OutOfServiceMode or InteractionPar.SetOutOfService;
  
  DetectOverride( VotedCmd := VotedCmdLoc,
  VotedCmdInt =\> VotedCmdInt,
  Reset := InteractionPar.Reset,
  ResetEnabled =\> ResetEnabled,
  Inhibit := InternalInhibit,
  ActivePriority =\> Priority,
  PriorityCmd0 := PriorityCmd01 or PriorityCmd02 or PriorityCmd03,
  PriorityCmd023 := PriorityCmd02 or PriorityCmd03,
  PriorityCmd0Config := PriorityCmd0Config,
  PriorityCmd1 := PriorityCmd1,
  PriorityCmd1Config := PriorityCmd1Config,
  PriorityCmdMan0 := PriorityCmdMan0,
  PriorityCmdMan0Config := PriorityCmdMan0Config,
  PriorityCmdMan1 := PriorityCmdMan1,
  PriorityCmdMan1Config := PriorityCmdMan1Config,
  ActiveILock =\> ILock,
  ILock0 := Ilock01 or Ilock02,
  ILock0Config := ILock0Config,
  ILock1 := Ilock11 or Ilock12,
  ILock1Config := ILock1Config,
  EnableParError := EnParError );
  
  VotedCmd.Backward := VotedCmdLoc.Backward;
  
  If Enable then
  
  (\* Priority command logic \*)
  
  PrioritySup( Enable := Enable,
  PriorityMode =\> PriorityModeInternal,
  PriorityCmd1 := DetectOverride.EffectivePriorityCmd1 or DetectOverride.EffectivePriorityCmdMan1,
  PriorityCmd0 := DetectOverride.EffectivePriorityCmd0 or DetectOverride.EffectivePriorityCmdMan0,
  PriorityCmd023 := DetectOverride.EffectivePriorityCmd023 or DetectOverride.EffectivePriorityCmdMan0,
  KeepOutAtErr := InteractionPar.KeepOutAtErr,
  AlarmAck := AlarmAck or InteractionPar.ObjErrAck or AlStateInternal = 4 or AEConfigInt = 0 or not(EnableSupOut or (EnableObjErr AND InteractionPar.EnableObjErr)),
  Inhibit := Inhibit,
  ObjErr := Core.ObjErrLoc,
  PriorityCmd0L =\> PriorityCmd0L,
  PriorityCmd023L =\> PriorityCmd023L );
  
  (\* Precalculations like limitations of auto commands signals may be
  entered in this position \*)
  
  (\* Input automatic start/stop command delay \*)
  
  DelayOfAutoCmd( Enable := AutoModeInternal,
  ReadyToStart =\> ReadyToStartInternal,
  Cmd1 := AutoCmd1,
  Cmd0 := AutoCmd0,
  Cmd1Delay =\> AutoCmd1Delay,
  Cmd0Delay =\> AutoCmd0Delay,
  OnDelayTime := InteractionPar.OnDelayTime,
  OffDelayTime := InteractionPar.OffDelayTime,
  Out1Level := Out1Level,
  AlState := AlStateInternal,
  EnableParError := EnParError );
  Else
  
  PriorityModeInternal := false;
  
  End_if;
  
  (\* Compute the level detection on the associated analog input signal \*)
  
  LevelDetection( Enable := InteractionPar.EnableLevelDetection,
  EnableDetection := Out1IOLevel and OldOut1IOLevel,
  Value := MotorValue.Value,
  Level := InteractionPar.Level,
  StartDelay := InteractionPar.StartDelay,
  FilterTime := InteractionPar.FilterTime,
  Hysteresis := InteractionPar.Hysteresis,
  GTLevel =\> MotorValueCondition,
  EnableParError := EnParError );
  
  OldOut1IOLevel := Out1IOLevel;
  
  (\* Initialize Jog functionality in manual mode \*)
  
  Jog( ManMode := ManMode,
  EffectiveFB1 := Core.EffectiveFB1,
  ManCmd1 := InteractionPar.ManCmd1,
  ManCmd0 := InteractionPar.ManCmd0,
  JogCmd1 := InteractionPar.JogCmd1,
  JogTime1 := InteractionPar.JogTime1,
  Jogging1 =\> Jogging,
  JogCmd2 := JogCmd2 );
  
  (\* This is the core function block containing mode switch logic,
  the interlock logic, Object test logic, time supervision ... \*)
  
  Core( Enable := Enable,
  Interlock =\> Interlock,
  Forced =\> Forced,
  Status =\> Status,
  SetAutoP := SetAuto,
  SetAuto := InteractionPar.SetAuto,
  AutoMode =\> AutoModeInternal,
  AutoCmd1 := DelayOfAutoCmd.Cmd1Delayed and not Ilock1Loc,
  AutoCmd0 := DelayOfAutoCmd.Cmd0Delayed,
  SetMan := InteractionPar.SetMan,
  ManMode =\> ManModeInternal,
  ManModeInit := ManModeInit,
  ManCmd1 := InteractionPar.ManCmd1,
  ManCmd0 := InteractionPar.ManCmd0,
  ManCmd1E := Jog.JogActivate1,
  ManCmd0E := Jog.JogActivate0,
  PanExists := PanExists,
  OpPanelMode := OpPanelMode,
  PanModeAct =\> PanModeAct,
  PanMode := PanMode,
  PanCmd1 := PanCmd1,
  PanCmd0 := PanCmd0,
  LocMode := LocMode,
  SetGroupStart := SetGroupStart,
  GroupStartObject := GroupStartObject,
  GroupStartMode =\> GroupStartModeInternal,
  GroupStartILock := GroupStartILock,
  PriorityMode := PriorityModeInternal,
  PriorityCmd1 := DetectOverride.EffectivePriorityCmd1,
  PriorityCmd0 := PriorityCmd0L,
  PriorityCmdMan1 := DetectOverride.EffectivePriorityCmdMan1,
  PriorityCmdMan0 := DetectOverride.EffectivePriorityCmdMan0,
  SetOutOfService := InteractionPar.SetOutOfService,
  OutOfServiceMode =\> OutOfServiceModeInternal,
  FB1 := FB1,
  FB0 := FB0,
  FBConfig := FBConfig,
  EffectiveFB1 =\> EffectiveFB1,
  EffectiveFB0 =\> EffectiveFB0,
  Ilock1 := DetectOverride.EffectiveIlock1 or Ilock1Loc,
  Ilock0 := DetectOverride.EffectiveIlock0,
  Inhibit := Inhibit,
  ObjectTest := ObjectTest,
  StatAct =\> StatActInternal,
  StatDeact =\> StatDeactInternal,
  PulseOut := InteractionPar.PulseOut,
  Out1 := Out1,
  Out0 := Out0,
  Out1IOLevel =\> Out1IOLevel,
  Out1Level =\> Out1Level,
  Out1Indication =\> Out1Indication,
  Out0Indication =\> Out0Indication,
  ExtStatus := MotorValue.Status,
  AEConfig := AEConfigInt,
  AlState := AlStateInternal,
  ObjErrEnabled =\> ObjErrEnabledInternal,
  AlarmDisabled =\> AlarmDisabledInternal,
  EnableSupOut := EnableSupOut,
  EnableObjErr := InteractionPar.EnableObjErr,
  EnableObjErrP := EnableObjErr,
  FBTime := InteractionPar.FBTime,
  ExtErr := ExtErr,
  ObjMode =\> ObjMode,
  EnableParError := EnParError );
  
  GSSetMan := not GroupStartModeInternal;
  
  AnyDisablingInhibiting := AlarmDisabledInternal and AEConfig \<\> 0;
  AnyAction := DetectOverride.EffectivePriorityCmd0 or DetectOverride.EffectivePriorityCmd1
  or DetectOverride.EffectivePriorityCmdMan0 or DetectOverride.EffectivePriorityCmdMan1
  or DetectOverride.EffectiveILock0 or DetectOverride.EffectiveILock1;
  
  If Enable then
  
  (\* Create alarm strings to be printed \*);
  
  ObjErrInternal := (Core.ObjErrLoc or PriorityCmd023L or MotorValueCondition) and AEConfigInt \> 0 and AEConfigInt \< 5 and (ObjErrEnabled or EnableSupOut);
  ObjErrStatInternal := ObjErrInternal AND ObjErrEnabledInternal;
  ObjErrInd := ObjErrInternal or PriorityCmd0L and not PriorityCmd023L;
  
  OEtext( ObjErr := ObjErrInternal,
  ObjMode := ObjMode,
  OEDescription := OEDescription,
  Name := Name,
  Out1Level := Out1Level,
  FBConfig := FBConfig,
  FB1 := FB1,
  FB0 := FB0,
  ExtErr := ExtErr,
  PriorityCmd01 := DetectOverride.PriorityCmd0Vote,
  PriorityCmd01Txt := PriorityCmd0VoteTxt,
  PriorityCmd02 := PriorityCmd02,
  PriorityCmd02Txt := PriorityCmd02Txt,
  PriorityCmd03 := PriorityCmd03,
  PriorityCmd03Txt := PriorityCmd03Txt,
  PriorityCmdMan0 := PriorityCmdMan0,
  PriorityCmdMan0Txt := PriorityCmdMan0Txt,
  ValueCondition := MotorValueCondition,
  ValueTxt := MotorValueTxt,
  Status := Status,
  EnableParError := EnParError );
  
  (\* Alarm supervision with event log functionality \*)
  
  Acknowledge := Alarmack or GroupStartObject.Forward.AlarmAck;
  Disable := LocMode or not ObjErrEnabledInternal;
  Condition2 := OEText.StatusError or OutOfServiceModeInternal;
  
  ObjectAE( CondNameObjErr := CondNameObjectError,
  AckCond := Acknowledge,
  DisCond := Disable,
  AEClass := AEClass,
  AEError =\> AEErrorInt,
  Condition1 := ObjErrStatInternal,
  Condition2 := Condition2,
  AEConfig := AEConfigInt,
  AESeverity := AESeverity,
  AlState =\> AlStateInternal,
  Message := OEDescription,
  EnableParError := EnParError );
  End_if;
  
  (\* Reset InteractionPar.ObjErrAck \*)
  SetBoolValue( Variable := InteractionPar.ObjErrAck,
  Expression := false );
  
  if VoteConnected then
  if VoteInit then
  (\*Update the Name in the connection \*)
  VoteOut.Forward.Name := Name;
  (\*Update the Forced in the connection \*)
  VoteOut.Forward.Forced := false;
  (\* Define the input signal type. Definition in description field of the FB CheckSupInputType in SignalLib \*)
  VoteOut.Forward.RealType := 10;
  end_if;
  VoteInit := false;
  
  (\* Calculate XAct outputs \*)
  VoteOut.Forward.GTH.Act := EffectiveFB1;
  VoteOut.Forward.DiffNormal.Act := EffectiveFB0;
  VoteOut.Forward.LTL.Act := ObjErrStatInternal or OEText.StatusError or OutOfServiceModeInternal;
  (\* Calculate XEnabled outputs \*)
  VoteOut.Forward.GTH.Enabled := true;
  VoteOut.Forward.DiffNormal.Enabled := true;
  VoteOut.Forward.LTL.Enabled := ObjErrEnabledInternal;
  (\* Calculate XActInh outputs \*)
  VoteOut.Forward.GTH.Inhibited := False;
  VoteOut.Forward.DiffNormal.Inhibited := False;
  VoteOut.Forward.LTL.Inhibited := False;
  
  (\* Alarm state \*)
  VoteOut.Forward.LTL.ALState := AlStateInternal;
  VoteOut.Forward.RealValue := 0.0;
  
  (\*Update the Status in the connection \*)
  VoteOut.Forward.Status := Status;
  (\* Inform the next control module that a previous control module exists \*)
  VoteOut.Forward.Connected := True;
  
  end_if;
  
  if EnParError then
  ParErrorInternal := ParErrorInternal or GSConnParError or
  DetectOverride.ParError or DelayOfAutoCmd.ParError or
  LevelDetection.ParError or Core.ParError or
  OEtext.ParError or ObjectAE.ParError;
  end_if;
  
  (\* NOTE: The backward components shall be handled in the same code block as the forward components as
  this object is regarded as the end object of the SIS loop\*)
  (\* Inform the previous control module that a next control module exists \*)
  VotedCmd.Backward.Connected := True;
- # SetOutputs
  (\* Copy internal variables to out parameters \*)
  
  AutoMode := AutoModeInternal;
  ManMode := ManModeInternal;
  PriorityMode := PriorityModeInternal;
  ReadyToStart := ReadyToStartInternal;
  StatAct := StatActInternal;
  StatDeact := StatDeactInternal;
  AlarmDisabled := AlarmDisabledInternal;
  ObjErrEnabled := ObjErrEnabledInternal;
  ObjErr := ObjErrInternal;
  ObjErrStat := ObjErrStatInternal;
  AlState := AlStateInternal;
  AEError := AEErrorInt;
  GroupStartMode := GroupStartModeInternal;
  OutOfServiceMode := OutOfServiceModeInternal;
  ParError := ParErrorInternal;