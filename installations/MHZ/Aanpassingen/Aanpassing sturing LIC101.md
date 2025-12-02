---
title: Aanpassing sturing LIC101
updated: [[2019-01-17]]T08:23:07.0000000+01:00
created: [[2019-01-17]]T08:22:00.0000000+01:00
---

- # [[2019-01-17]] Backup code
  (\* LIC101 Track en TrackValue \*)
  (\* Indien PU101 uitvalt dan start Ton1 \*)
  (\* Na tijd Ton1 =\> Track=1 en TrackValue=0, en start Ton2 \*)
  (\* Na tijd Ton2 =\> Track=1 en TrackValue=20%, en start Ton3 \*)
  (\* Na tijd Ton3 =\> Track=poc.LIC101_Track en TrackValue=0% \*)
  
  Ton1( In := Par.PU101.AutoCmd AND Par.PU101.Statstop,
  PT := dint_to_time(2500) );
  Ton2( In := Ton1.Q,
  PT := dint_to_Time(60000) );
  Ton3( In := Ton2.Q,
  PT := dint_to_time(60000) );
  
  IF Ton1.Q AND (NOT Ton2.Q OR (Ton2.Q AND NOT Ton3.Q)) Then
  LIC101_Track := True;
  Else
  LIC101_Track := Poc.LIC101_Track;
  End_if;
  
  If Ton1.Q AND Ton2.Q AND NOT Ton3.Q Then
  LIC101_TrackValue := 20;
  Else
  LIC101_TrackValue := 0;
  End_if;
  
  LIC101_Track := poc.LIC101_Track;
  LIC102_Track := poc.LIC101_Track;