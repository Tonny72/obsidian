---
title: Weegcel
updated: [[2021-01-23]]T16:08:45.0000000+01:00
created: [[2021-01-23]]T15:23:44.0000000+01:00
---

![image1](image1-506.png)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 28%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><h1 id="nr-gsd">NR GSD</h1></th>
<th><h1 id="naam-gsd">Naam GSD</h1></th>
<th><h1 id="no-byte-swap">No byte swap</h1></th>
<th><h1 id="byte-swap">Byte swap</h1></th>
<th><h1 id="af10">AF10</h1></th>
<th><h1 id="bbz">BBZ</h1></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Byte16, Bit0</td>
<td>Input8</td>
<td>nr of decimals</td>
<td>canopen network default</td>
<td>I8_B7_Weight_error</td>
<td></td>
</tr>
<tr class="even">
<td>Byte16, Bit1</td>
<td>Input9</td>
<td>nr of decimals</td>
<td>DSD weights displayed</td>
<td>I9_B8_Network_error</td>
<td></td>
</tr>
<tr class="odd">
<td>Byte16, Bit2</td>
<td>Input10</td>
<td>nr of decimals</td>
<td>Not used B10</td>
<td>I10_B9_DSD</td>
<td></td>
</tr>
<tr class="even">
<td>Byte16, Bit3</td>
<td>Input11</td>
<td>stable weight</td>
<td>correctly executed command</td>
<td>I11_B10_Spare</td>
<td>I12_B11_Cmd_Correct</td>
</tr>
<tr class="odd">
<td>Byte16, Bit4</td>
<td>Input12</td>
<td>valid weight</td>
<td>Not correctly executed command</td>
<td>I12_B11_Cmd_Correct</td>
<td></td>
</tr>
<tr class="even">
<td>Byte16, Bit5</td>
<td>Input13</td>
<td>ouside range + weight</td>
<td>Not used B13</td>
<td>I13_B12_Cmd_Not_Correct</td>
<td>I13_B12_Cmd_Not_Correct</td>
</tr>
<tr class="odd">
<td>Byte16, Bit6</td>
<td>Input14</td>
<td>ouside rande - weight</td>
<td>Not used B14</td>
<td>I14_B13_Spare</td>
<td></td>
</tr>
<tr class="even">
<td>Byte16, Bit7</td>
<td>Input15</td>
<td>weight failure</td>
<td>Not used B15</td>
<td>I15_B14_Spare</td>
<td></td>
</tr>
<tr class="odd">
<td>Byte17, Bit0</td>
<td>Input1</td>
<td>canopen netwok default</td>
<td>nr of decimals</td>
<td>I1_B0_Dec_Point</td>
<td>I1_B0_Dec_Point</td>
</tr>
<tr class="even">
<td>Byte17, Bit1</td>
<td>Input2</td>
<td>DSD weights displayed</td>
<td>nr of decimals</td>
<td>I2_B1_Dec_Point</td>
<td>I2_B1_Dec_Point</td>
</tr>
<tr class="odd">
<td>Byte17, Bit2</td>
<td>Input3</td>
<td>Not used B10</td>
<td>nr of decimals</td>
<td>I3_B2_Dec_Point</td>
<td>I3_B2_Dec_Point</td>
</tr>
<tr class="even">
<td>Byte17, Bit3</td>
<td>Input4</td>
<td>correctly executed command</td>
<td>stable weight</td>
<td>I4_B3_Stable_Weight</td>
<td>I4_B3_Stable_Weight</td>
</tr>
<tr class="odd">
<td>Byte17, Bit4</td>
<td>Input5</td>
<td>Not correctly executed command</td>
<td>valid weight</td>
<td>I5_B4_Valid_Weight</td>
<td>I5_B4_Valid_Weight</td>
</tr>
<tr class="even">
<td>Byte17, Bit5</td>
<td>Input6</td>
<td>Not used B13</td>
<td>ouside range + weight</td>
<td>I6_B5_Weight_Out_Plus</td>
<td>I6_B5_Weight_Out_Plus</td>
</tr>
<tr class="odd">
<td>Byte17, Bit6</td>
<td>Input7</td>
<td>Not used B14</td>
<td>ouside rande - weight</td>
<td>I7_B6_Weight_Out_Min</td>
<td>I7_B6_Weight_Out_Min</td>
</tr>
<tr class="even">
<td>Byte17, Bit7</td>
<td>Input16</td>
<td>Not used B15</td>
<td>weight failure</td>
<td>I16_B15_Spare</td>
<td>(WEIGHT ERROR)</td>
</tr>
</tbody>
</table>
