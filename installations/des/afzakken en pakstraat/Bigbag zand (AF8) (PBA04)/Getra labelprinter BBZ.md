---
title: Getra labelprinter BBZ
updated: [[2018-09-24]]T16:27:12.0000000+02:00
created: [[2018-02-14]]T16:34:59.0000000+01:00
---

Componenten
<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 31%" />
<col style="width: 22%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><h6 id="naam"><em>Naam</em></h6></th>
<th><h6 id="netwerk-aansluiting"><em>Netwerk aansluiting</em></h6></th>
<th><h6 id="ip-adres"><em>Ip adres</em></h6></th>
<th><h6 id="switch-poort"><em>Switch poort</em></h6></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Sato printer</td>
<td>P1</td>
<td>10.32.17.41</td>
<td>SWS21 2/15</td>
</tr>
<tr class="even">
<td>Scanner / Moxa</td>
<td>P2</td>
<td>10.32.17.89</td>
<td>SWS21 2/16</td>
</tr>
<tr class="odd">
<td>PLC</td>
<td>P3</td>
<td>10.32.27.196</td>
<td>SWS21 2/17</td>
</tr>
<tr class="even">
<td>HMI</td>
<td>P4</td>
<td>10.32.27.197</td>
<td>SWS21 2/18</td>
</tr>
</tbody>
</table>

- # DI (Getra -\> ABB)
  | .1.2.1.11 | AF8_RB_STT  | Rollenbaan mag draaien                 |
  |-----------|-------------|----------------------------------------|
  | .1.2.1.12 | AF8_PRT_RDY | Labelprinter ready (klaar met printen) |
- # DO (ABB -\> Getra)
  | .1.2.6.11 | AF8_PAL_OK | Pallet aanwezig |
  |-----------|------------|-----------------|
- # Scanner wil niet scannen
  [[2018-09-24]] : op bigbag zand wilde de scanner de barcode niet herkennen. Simpelweg het glasplaatje van de scanner kuisen loste het probleem op.