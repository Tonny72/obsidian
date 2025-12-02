---
date created:
  - - 2010-11-22
---


Motor Object SibMotorUni_PG2

Kopieer Function block UniDelayOfCmd uit de Basic lib lokaal en vervand de variabele ‘ReadyToStop’ als parameter.

Kopieer Control Module MotorUniM uit de ProcessObjExtLib.

Voeg de variabele ReadyToStopInternal en de parameter ReadyToStop toe.

Vervang de Function BlockType van DelayOfAutoCmd door de aangepast UniDelayOfCmd.

DelayOfAutoCmd( Enable := AutoModeInternal,
ReadyToStart =\> ReadyToStartInternal,
ReadyToStop =\> ReadyToStopInternal,
Cmd1 := AutoCmd1,
Cmd0 := AutoCmd0,
Cmd1Delay =\> AutoCmd1Delay,
Cmd0Delay =\> AutoCmd0Delay,
OnDelayTime := InteractionPar.OnDelayTime,
OffDelayTime := InteractionPar.OffDelayTime,
Out1Level := Out1Level,
AlState := AlStateInternal,
EnableParError := EnParError );

In het tabblad Set_output voeg je deze regel toe.

ReadyToStop := ReadyToStopInternal;

Uitbreiding van PriorityCmd02 en PriorityCmd02Txt met PriorityCmd04 en PriorityCmd05

Pas DetectOverride aan

DetectOverride( VotedCmd := VotedCmdLoc,
VotedCmdInt =\> VotedCmdInt,
Reset := InteractionPar.Reset,
ResetEnabled =\> ResetEnabled,
Inhibit := Inhibit,
ActivePriority =\> Priority,
PriorityCmd0 := PriorityCmd01 or PriorityCmd02 or PriorityCmd03 OR PriorityCmd04 OR PriorityCmd05,
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

Pas OEtext aan voor de extra PriorityCmd04 OR PriorityCmd05

LevelDetection verwijderen
