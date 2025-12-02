---
title: TDrive
date modified: 2025-09-18T22:09:03+02:00
tags: [800xA, dev]
date created: 2018-11-21T00:00:00+02:00
---

|                 | status | command |
|------------------|--------|---------|
| C1 in bedrijf    | 5943   | 1151    |
| C_WP4 in bedrijf | 4663   | 1151    |
| C_WP5 gestopt    | 4657   | 1142    |
| AF11 M14 gestopt | 561    | 1142    |
| C3_BE601         | 4919   | 1151    |
|                 |       |        |

<table>
<colgroup>
<col style="width: 51%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Command 1142 (gestopt)</p>
<p>![image1](../../../../../resources/image1-84.png)</p>
<p></p></th>
<th><p>Command 1151 (in bedrijf)</p>
<p>![image2](../../../../../resources/image2-50.png)</p>
<p></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- # Conversiehulp
  689(dec) = 0281(hex) = 0010 1011 0001
  1142(dec) = 0476(hex) = 0100 0111 0110
  2048(dec) = 0800(hex) = 1000 0000 0000
- # ControlWord - CommandSend
  <table>
  <colgroup>
  <col style="width: 9%" />
  <col style="width: 28%" />
  <col style="width: 21%" />
  <col style="width: 40%" />
  </colgroup>
  <thead>
  <tr class="header">
  <th></th>
  <th></th>
  <th>1</th>
  <th>0</th>
  </tr>
  </thead>
  <tbody>
  <tr class="odd">
  <td>Bit0:</td>
  <td><p>CommandSend-SwitchOn: Zet drive onder spanning</p>
  <p>OFF1</p></td>
  <td>Proceed Ready to operate</td>
  <td>Stop along currently active. Proceed to OFF1 active; Proceed to Ready to switch on unless other interlocks (off2, off3) are active</td>
  </tr>
  <tr class="even">
  <td>Bit1:</td>
  <td>OFF2 (free run)</td>
  <td>Continue operation (off2 inactive)</td>
  <td>Emergency OFF, coast to stop, Proceed to off2 active, proceed to switch-on inhibited</td>
  </tr>
  <tr class="odd">
  <td>Bit2</td>
  <td>OFF3</td>
  <td>Continue operation (OFF3 inactive)</td>
  <td>Emergency stop, stop within time defined; proceed to switch-on inhibited</td>
  </tr>
  <tr class="even">
  <td>Bit3</td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>Bit4</td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="even">
  <td>Bit5</td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>Bit6</td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="even">
  <td>Bit7</td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>Bit8</td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="even">
  <td>Bit9</td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>Bit10</td>
  <td>Master control by PLC<br />
  REMOTE_CMD</td>
  <td>Fieldbus control enabled</td>
  <td>Control word and reference not getting throug h to the drive except fot CW bits OFF1, OFF2 and OFF3</td>
  </tr>
  <tr class="even">
  <td>Bit11</td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>Bit12</td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="even">
  <td>Bit13</td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  </tbody>
  </table>
## StatusWoord - StatusReceive
|      |               | 1                                                                             | 0                                                                          |
|-------|----------------|-------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Bit0  | OFF1 (RDY_ON)  | Ready to switch on                                                            | Not ready to switch on                                                     |
| Bit1  | RDY_RUN        | Ready to operate                                                              | **Off1 active**                                                            |
| Bit2  | RDY_REF        |                                                                              |                                                                           |
| Bit3  | Tripped        | Fault                                                                         | No fault                                                                   |
| Bit4  | OFF2 status    | OFF2 inactief                                                                 | **OFF2 Active**                                                            |
| Bit5  | OFF3 Status    | OFF3 inactive                                                                 | **OFF3 Active**                                                            |
| Bit6  | SWC_ON_INHIBIT | SWITCH-ON INHIBIT ACTIVE                                                      | SWITCH-ON INHIBIT NOT ACTIVE                                               |
| Bit7  | ALARM          | Warning/Alarm                                                                 | No Warning/Alarm                                                           |
| Bit8  | AT_SETPOINT    | OPERATING. Actual value equals reference value (= is within tolerance limits) | Actual value differs from reference value (= is outside tolerance limits). |
| Bit9  |               |                                                                              |                                                                           |
| Bit10 |               |                                                                              |                                                                           |
| Bit11 |               |                                                                              |                                                                           |
| Bit12 |               |                                                                              |                                                                           |
| Bit13 |               |                                                                              |                                                                           |
| Bit14 |               |                                                                              |                                                                           |
| Bit15 |               |                                                                              |                                                                           |

  <table>
  <colgroup>
  <col style="width: 18%" />
  <col style="width: 19%" />
  <col style="width: 19%" />
  <col style="width: 21%" />
  <col style="width: 20%" />
  </colgroup>
  <thead>
  <tr class="header">
  <th><p>Status 4657 (stop)</p>
  <p>![image3](../../../../../resources/image3-27.png)</p>
  <p></p></th>
  <th><p>Status 561 (stop)</p>
  <p>![image4](../../../../../resources/image4-23.png)</p>
  <p></p></th>
  <th><p>Status 4919 (run)</p>
  <p>![image4](../../../../../resources/image4-23.png)</p>
  <p></p></th>
  <th><p>Status 5943 (run)</p>
  <p>![image5](../../../../../resources/image5-19.png)</p>
  <p></p></th>
  <th><p>Status 4663 (run)</p>
  <p>![image6](../../../../../resources/image6-16.png)</p>
  <p></p></th>
  </tr>
  </thead>
  <tbody>
  </tbody>
  </table>
  
  Bit0:
  Aan / Uit schakelen van de drive
  Command: 1142 = drive uit
  Command: 1143 = drive aan
  =\> Deze bit wordt eerst hoog gezet bij aansturing drive
  
  VOLGORDE (van Onder naar boven)
  ![image7](image7-9.png)