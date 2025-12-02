---
title: Vote - Werking VoteConnection
updated: [[2018-04-20]]T14:04:02.0000000+02:00
created: [[2018-04-20]]T11:41:47.0000000+02:00
---

Dit diagramma toont de aansturing van een motor. Een activatie van MotorUniM.PriorityCmd0Config geeft altijd een alarm, ook als de motor niet draait.
![image1](image1-180.png)

- # SignalInRealM
  | VoteOut            | VoteConnection | out | NODE Output to vote objects                                                        |
  |--------------------|----------------|-----|------------------------------------------------------------------------------------|
  | EnableLatchQuality | bool           | in  | Enables latch of bad quality that may be reset by InteractionPar.ResetLatchQuality |
- # Vote1oo1Q
  Voor een enkel signaal Vote1oo1Q gebruiken.
  <table>
  <colgroup>
  <col style="width: 25%" />
  <col style="width: 18%" />
  <col style="width: 7%" />
  <col style="width: 49%" />
  </colgroup>
  <thead>
  <tr class="header">
  <th>In</th>
  <th>VoteConnection</th>
  <th>in</th>
  <th><p>IN NODE Input</p>
  <p>Afkomstig van SignalInRealM.VoteOut</p></th>
  </tr>
  </thead>
  <tbody>
  <tr class="odd">
  <td>VoteOut</td>
  <td>VoteConnection</td>
  <td>out</td>
  <td>OUT(IN) for cascade connection of vote objects</td>
  </tr>
  <tr class="even">
  <td>InLevelConfig</td>
  <td>dint</td>
  <td>in</td>
  <td><p>IN Specification of Level included in voting (-3=LLL, -2=LL, -1=L, 0=DiffN, 1=H, 2=HH, 3=HHH (Obj dep.), else (0 if Bool else 1) + ParError)</p>
  <p>Welk alarm-niveau moet worden genomen</p></td>
  </tr>
  <tr class="odd">
  <td>LatchEnable</td>
  <td>bool</td>
  <td>in</td>
  <td>IN Enables latch on output</td>
  </tr>
  <tr class="even">
  <td>OutCommandNumber</td>
  <td>dint</td>
  <td>in</td>
  <td>IN Command number to be set on Out. Range 1-32, else 1 +ParError.<br />
  Welk commando-nummer is dit signaal van 1 tot 32</td>
  </tr>
  </tbody>
  </table>
- # MotorUniM
  | VotedCmd              | VotedConnection | in  | IN NODE Input from voting logic                                                                                               |
  |-----------------------|-----------------|-----|-------------------------------------------------------------------------------------------------------------------------------|
  | PriorityCmdMan1Config | dword           | in  | IN Specify which Voted Command number(s) to set PriorityCmdMan1 Bit number=Command number. (`1-16#FFFFFFFF`, else 1 + ParError) |
  | PriorityCmdMan0Config | dword           | in  | IN Specify which Voted Command number(s) to set PriorityCmdMan0 Bit number=Command number. (`1-16#FFFFFFFF`, else 1 + ParError) |
  | PriorityCmd1Config    | dword           | in  | IN Specify which Voted Command number(s) to set PriorityCmd1 Bit number=Command number. (`1-16#FFFFFFFF`, else 1 + ParError)    |
  | PriorityCmd0Config    | dword           | in  | IN Specify which Voted Command number(s) to set PriorityCmd0 Bit number=Command number. (`1-16#FFFFFFFF`, else 1 + ParError)    |
  | ILock1Config          | dword           | in  | IN Specify which Voted Command number(s) to set ILock1 Bit number=Command number. (`1-16#FFFFFFFF`, else 1 + ParError)          |
  | ILock0Config          | dword           | in  | IN Specify which Voted Command number(s) to set ILock0 Bit number=Command number. (`1-16#FFFFFFFF`, else 1 + ParError)          |