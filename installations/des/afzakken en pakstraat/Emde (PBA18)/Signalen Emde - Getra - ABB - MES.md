---
title: Signalen Emde - Getra - ABB - MES
updated: [[2018-06-19]]T15:15:56.0000000+02:00
created: [[2018-06-19]]T14:24:54.0000000+02:00
---

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 16%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th><h1 id="signaal">Signaal</h1></th>
<th><h1 id="richting">Richting </h1></th>
<th><h1 id="omschrijving">Omschrijving</h1></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>IaPar.AF12_Labelprinter_ready_start</td>
<td>Emde -&gt; ABB</td>
<td>Start print cyclus</td>
</tr>
<tr class="even">
<td>IaPar.AF12_Labelprinter_Start</td>
<td>ABB -&gt; Emde)</td>
<td>Start voor labelprinter</td>
</tr>
<tr class="odd">
<td>IaPar.AF12_Start_FB_PLC</td>
<td>Emde -&gt; ABB (en ook naar printer)</td>
<td>Dit is het hard-wired signal dat Emde naar de labelprinter stuurt.<br />
<em>Is eigenlijk gelijk aan IaPar.AF12_Labelprinter_Start</em></td>
</tr>
<tr class="even">
<td>IaPar.AF12_OK_print_label</td>
<td>Emde -&gt; ABB</td>
<td>Einde print cyclus</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 40%" />
<col style="width: 35%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><h1 id="stap">Stap</h1></th>
<th><h1 id="actie">Actie</h1></th>
<th><h1 id="gevolg">Gevolg</h1></th>
<th><h1 id="volgende-stap">Volgende stap</h1></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>IaPar_MES.PBA18.Release = 1, en IO.AF12_Grof.IOValue = 1</td>
<td>IaPar_MES.MES_Pallet_Request = 1</td>
<td>2</td>
</tr>
<tr class="even">
<td>2</td>
<td>MES genereert nieuwe data (IaPar_MES.MES_Lot_Code en IaPar_MES.MES_Pallet_Code)</td>
<td>Iapar_MES.MES_Pallet_Info = 1<br />
(ABB zet Lot, Pallet en Gewicht in Array)</td>
<td>3</td>
</tr>
<tr class="odd">
<td>3</td>
<td></td>
<td>IaPar_MES.MES_Pallet_Request = 0</td>
<td></td>
</tr>
</tbody>
</table>
