---
title: Gebruik van sibSequenceInterface_v2
updated: [[2017-03-01]]T14:31:25.0000000+01:00
created: [[2017-03-01]]T13:02:05.0000000+01:00
---

- # Opbouw een Control Module voor een sequentie
  
  1.  Maak een Control Module met 4 tabs.
- Code
- SFC
- HeaderCode
- Reset
  
  2.  Maak variabelen aan
  | StepInfo  | SibSFCStepInfo | retain hidden        |
  |-----------|----------------|----------------------|
  | SFCPar    | SibSFCPar      | retain hidden        |
  | SFCHeader | SibSFCHeader   | retain hidden        |
  | AutoOn    | bool           | retain nosort hidden |
  | AutoOff   | bool           | retain nosort hidden |
  | AutoRes   | bool           | retain nosort hidden |
  
  3.  Voeg de sibSequenceInterface_v2 toe
  ![image1](image1-524.png)
- # 
  4.  Vul code in tabs.
- ## Code 
  (\* AutoOn \*)
  
  (\* ------ \*)
  
  AutoOn := AutoCmd.S1;
  
  (\* AutoStop \*)
  
  (\* -------- \*)
  
  AutoOff := AutoCmd.S0;
  
  (\* AutoRes \*)
  
  (\* ------- \*)
  
  AutoRes := Poc.ResetSequentie;
- ## SFC
  ![image2](image2-207.png)
- ### In elke Step
- ### In transitie 'OnSeq'
  SFCPar.OnSeq
- ### In transitie 'OffSeq'
  SFCPar.OffSeq
- ### Laaste stap Off-sequentie
  (\* StepInfo \*)
  
  (\* -------- \*)
  
  StepInfo.StepNo := 2000;
  
  StepInfo.T := S2000.T;
  
  StepInfo.Tmax := 5;
  
  (\* Reset sequentie \*)
  
  (\* --------------- \*)
  
  Poc.ResetSequentie := S2000.X;
- ## HeaderCode
  (\* SFC interactie \*)
  
  (\* --------------- \*)
  
  SFC.Check := SFCHeader.Check;
  
  SFC.DisableActions := SFCHeader.DisableActions;
  
  SFC.Hold := SFCHeader.Hold;
  
  SFC.MaxStepTime := SFCHeader.MaxStepTime;
  
  SFC.Reset := SFCHeader.Reset;
  
  SFCHeader.StepTimedOut := SFC.StepTimedOut;
- ## Reset
  (\* Reset \*)
  
  (\* ----- \*)
  
  If NOT SFCPar.Run Then
  
  StepInfo.StepNo := 0;
  
  Poc.MAF1.S0 := SFCPar.Reset;
  
  Poc.MAF1.S1 := False;
  
  End_if;