---
title: Vergelijking aansturingen motor
updated: [[2016-04-14]]T14:50:31.0000000+02:00
created: [[2010-11-22]]T09:15:03.0000000+01:00
---

Vergelijking aansturingen motor
maandag 22 november 2010
9:15

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 33%" />
<col style="width: 11%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th><p>PLC</p>
<p>Input / Output</p></th>
<th>TESYS</th>
<th>I/O</th>
<th>ACS350</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Ready</td>
<td>All the conditions that will permit the operation of a switching device by the the remote host controller hav been fullfilled</td>
<td>IN</td>
<td>x</td>
<td></td>
<td>RDY_RUN of RDY_ON</td>
</tr>
<tr class="even">
<td>On</td>
<td>The main circuit contacts are closed</td>
<td>IN</td>
<td>x</td>
<td>x</td>
<td></td>
</tr>
<tr class="odd">
<td>Fault</td>
<td>A fault condition exists</td>
<td>IN</td>
<td>x</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Warning</td>
<td>A warning condition exists</td>
<td>IN</td>
<td>x</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Tripped</td>
<td>Trip status</td>
<td>IN</td>
<td>x</td>
<td></td>
<td>x</td>
</tr>
<tr class="even">
<td>ResetAuthorized</td>
<td><p>0 = no fault or with reset inhibited</p>
<p>1 = reset is authorized now</p></td>
<td>IN</td>
<td>x</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>MotorRunning</td>
<td><p>0 = Motor not running</p>
<p>1 = Motor running</p></td>
<td>IN</td>
<td>x</td>
<td>x</td>
<td></td>
</tr>
<tr class="even">
<td>MotorCurrent</td>
<td>The motor current</td>
<td>IN</td>
<td>x (in %)</td>
<td>x (in A)</td>
<td>x</td>
</tr>
<tr class="odd">
<td>ButtonPositionON</td>
<td></td>
<td>IN</td>
<td>x</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ButtonPositionTRIP</td>
<td></td>
<td>IN</td>
<td>x</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ContactorStateIN</td>
<td></td>
<td>IN</td>
<td>x</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ExtDI1</td>
<td></td>
<td>IN</td>
<td>LI1</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ExtDI1</td>
<td></td>
<td>IN</td>
<td>Li2</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>RunForward</td>
<td></td>
<td>OUT</td>
<td>x</td>
<td>x</td>
<td>x</td>
</tr>
<tr class="even">
<td>RunReverse</td>
<td></td>
<td>OUT</td>
<td>x</td>
<td></td>
<td>x</td>
</tr>
<tr class="odd">
<td>TripReset</td>
<td></td>
<td>OUT</td>
<td>x</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Reset</td>
<td></td>
<td>OUT</td>
<td></td>
<td></td>
<td>x</td>
</tr>
</tbody>
</table>
