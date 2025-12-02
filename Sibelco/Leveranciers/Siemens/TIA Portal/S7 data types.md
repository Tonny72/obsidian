---
title: Siemens PLC data types
updated: [[2019-07-16]]T10:53:53.0000000+02:00
created: [[2019-07-16]]T09:43:48.0000000+02:00
---

Siemens PLC data types
dinsdag 16 juli 2019
9:43

![image1](image1-583.png)

**Step 7 Elementary Data Types**
<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 5%" />
<col style="width: 14%" />
<col style="width: 33%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Type and</strong></p>
<p><strong>Description</strong></p></th>
<th><p><strong>Size</strong></p>
<p><strong>in</strong></p>
<p><strong>Bits</strong></p></th>
<th><strong>Format Options</strong></th>
<th><p><strong>Range and Number Notation</strong></p>
<p><strong>(lowest to highest values)</strong></p></th>
<th><strong>Example in STL</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>BOOL (Bit)</td>
<td>1</td>
<td>Boolean text</td>
<td>TRUE/FALSE</td>
<td>TRUE</td>
</tr>
<tr class="even">
<td>BYTE (Byte)</td>
<td>8</td>
<td>Hexadecimal number</td>
<td>B#16#0 to B#16#FF</td>
<td><p>L B#16#10</p>
<p>L byte#16#10</p></td>
</tr>
<tr class="odd">
<td>WORD (Word)</td>
<td>16</td>
<td>Binary number</td>
<td>2#0 to 2#1111_1111_1111_1111</td>
<td>L 2#0001_0000_0000_0000</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>Hexadecimal number</td>
<td>W#16#0 to W#16#FFFF</td>
<td><p>L W#16#1000</p>
<p>L word#16#1000</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>BCD</td>
<td>C#0 to C#999</td>
<td>L C#998</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>Decimal number unsigned</td>
<td>B#(0,0) to B#(255,255)</td>
<td><p>L B#(10,20)</p>
<p>L byte#(10,20)</p></td>
</tr>
<tr class="odd">
<td>DWORD (Double word)</td>
<td>32</td>
<td>Binary number</td>
<td><p>2#0 to 2#1111_1111_1111_1111_</p>
<p>1111_1111_1111_1111</p></td>
<td><p>L 2#1000_0001_0001_1000_</p>
<p>1011_1011_0111_1111</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>Hexadecimal number</td>
<td>W#16#0000_0000 to W#16#FFFF_FFFF</td>
<td><p>L DW#16#00A2_1234</p>
<p>L dword#16#00A2_1234</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>Decimal number unsigned</td>
<td>B#(0,0,0,0) to B#(255,255,255,255)</td>
<td><p>L B#(1, 14, 100, 120)</p>
<p>L byte#(1,14,100,120)</p></td>
</tr>
<tr class="even">
<td>INT (Integer)</td>
<td>16</td>
<td>Decimal number signed</td>
<td>-32768 to 32767</td>
<td>L 101</td>
</tr>
<tr class="odd">
<td>DINT (Double integer)</td>
<td>32</td>
<td>Decimal number signed</td>
<td>L#-2147483648 to L#2147483647</td>
<td>L L#101</td>
</tr>
<tr class="even">
<td>REAL (Floating-point number)</td>
<td>32</td>
<td>IEEE Floating-point number</td>
<td><p>Upper limit +/-3.402823e+38</p>
<p>Lower limit +/-1.175495e-38</p></td>
<td>L 1.234567e+13</td>
</tr>
<tr class="odd">
<td>S5TIME (SIMATIC time)</td>
<td>16</td>
<td>S7 time in steps of 10ms (default)</td>
<td><p>S5T#0H_0M_0S_10MS to</p>
<p>S5T#2H_46M_30S_0MS and</p>
<p>S5T#0H_0M_0S_0MS</p></td>
<td><p>L S5T#0H_1M_0S_0MS</p>
<p>L S5TIME#0H_1H_1M_0S_0MS</p></td>
</tr>
<tr class="even">
<td>TIME (IEC time)</td>
<td>32</td>
<td>IEC time in steps of 1 ms, integer signed</td>
<td><p>T#24D_20H_31M_23S_648MS</p>
<p>to</p>
<p>T#24D_20H_31M_23S_647MS</p></td>
<td><p>L T#0D_1H_1M_0S_0MS</p>
<p>L TIME#0D_1H_1M_0S_0MS</p></td>
</tr>
<tr class="odd">
<td>DATE (IEC date)</td>
<td>16</td>
<td>IEC date in steps of 1 day</td>
<td><p>D#1990-1-1 to</p>
<p>D#[[2168-12-31]]</p></td>
<td><p>L D#1996-3-15</p>
<p>L DATE#1996-3-15</p></td>
</tr>
<tr class="even">
<td>TIME _OF_DAY (Time)</td>
<td>32</td>
<td>Time in steps of 1 ms</td>
<td><p>TOD#0:0:0.0 to</p>
<p>TOD#23:59:59.999</p></td>
<td><p>L TOD#1:10:3.3</p>
<p>L TIME_OF_DAY#1:10:3.3</p></td>
</tr>
<tr class="odd">
<td>CHAR (Character)</td>
<td>8</td>
<td>ASCII characters</td>
<td>A', 'B' etc.</td>
<td>L 'E'</td>
</tr>
</tbody>
</table>

*From \<<http://www.plcdev.com/book/export/html/373>\>*
