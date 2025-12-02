---
created: [[2010-11-22]]T10:18:32.0000000+01:00
tags:
  - AF6
---

1.  ***Motoren***
<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 22%" />
<col style="width: 35%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>TAG</strong></th>
<th><strong>Omschrijving</strong></th>
<th><strong>Vergrendelingen</strong></th>
<th><strong></strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>M4_AF6_1</strong></td>
<td>Afzuigventilator</td>
<td>PT1 langer dan 10min &gt; -190</td>
<td></td>
</tr>
<tr class="even">
<td><strong>M4_AF6_4</strong></td>
<td>Cellenrad</td>
<td>geen</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>M4_AF6_5</strong></td>
<td>Filter Rotoseal</td>
<td><p>M4_AF6_4 moet draaien</p>
<p>M4_AF6_5_F_DI = 0</p></td>
<td>FB1 valt na tijdje weg</td>
</tr>
<tr class="even">
<td><strong>M4_AF6_6</strong></td>
<td>Vijs uitloop filter</td>
<td>geen</td>
<td></td>
</tr>
</tbody>
</table>
2.  ***Kleppen***
| **TAG** | **Omschrijving** | **Vergrendelingen** |
|---------|------------------|---------------------|
|        |                 |                    |
|        |                 |                    |
3.  ***Digitale Ingangen***
<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 32%" />
<col style="width: 11%" />
<col style="width: 6%" />
<col style="width: 14%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>TAG</strong></p>
<p><strong>DI</strong></p></th>
<th><strong>Omschrijving</strong></th>
<th><strong>Aktieve waarde</strong></th>
<th><strong>FP / IND</strong></th>
<th><strong>Aansluiting</strong></th>
<th><strong>Onderdeel van Object</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>M4_AF6_1_CIN</strong></td>
<td>Hoofdcontactor in</td>
<td></td>
<td>FP</td>
<td>0.11.401.1</td>
<td></td>
</tr>
<tr class="even">
<td><strong>M4_AF6_4_DI</strong></td>
<td>Cellenrad draait</td>
<td></td>
<td></td>
<td>0.11.401.2</td>
<td>AF6_4</td>
</tr>
<tr class="odd">
<td><strong>M4_AF6_5_DI</strong></td>
<td>Filter Rotoseal in (DI niet gekoppeld. DI valt weg na een tijdje en FBConfig=6 werkt niet)</td>
<td></td>
<td></td>
<td>0.11.401.3</td>
<td>AF6_5</td>
</tr>
<tr class="even">
<td><strong>M4_AF6_5_F_DI</strong></td>
<td>Filter Rotoseal in storing</td>
<td>0</td>
<td></td>
<td>0.11.401.4</td>
<td>AF6_5</td>
</tr>
<tr class="odd">
<td><strong>M4_AF6_6_DI</strong></td>
<td>Vijs uitloop filter draait</td>
<td></td>
<td></td>
<td>0.11.401.5</td>
<td>AF6_6</td>
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
<td><strong>M4_1_CIN</strong></td>
<td>Hoofdcontactor in</td>
<td></td>
<td>FP</td>
<td>0.11.401.8</td>
<td></td>
</tr>
<tr class="even">
<td><strong></strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>M4_AF6_I_DI</strong></td>
<td>Start filter AF6 vanaf Rotoseal</td>
<td></td>
<td>IND</td>
<td>0.11.402.14</td>
<td></td>
</tr>
<tr class="even">
<td><strong>M4_BUN_UPS</strong></td>
<td>Alarm UPS</td>
<td></td>
<td>IND</td>
<td>0.11.402.15</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>M4_BUN_BATT</strong></td>
<td>Mode niet ok</td>
<td></td>
<td>IND</td>
<td>0.11.402.16</td>
<td></td>
</tr>
</tbody>
</table>
4.  ***Digitale Uitgangen***
| **TAG**          | **Omschrijving**                             | **FP / IND** | **Aansluiting** | **Onderdeel van Object** |
|------------------|----------------------------------------------|--------------|-----------------|--------------------------|
| **M4_AF6_4**     | Cellenrad afvoer rotoseal start              |             | 0.11.501.1      | AF6_4                    |
| **M4_AF6_5**     | Filter rotoseal start                        |             | 0.11.501.2      | AF6_5                    |
| **M4_AF6_6**     | Vijs afvoer rotoseal start                   |             | 0.11.501.3      | AF6_6                    |
| **M4_AF6_I\_DO** | Filter rotoseal draait melding naar rotoseal |             | 0.11.501.4      |                         |
|                 |                                             |             |                |                         |
******
5.  ***Analoge Ingangen***
| **TAG** | **Omschrijving** | **FP/IN** | **Aansluiting** | **Onderdeel van Object** | **LLL** | **LL** | **L** | **H** | **HH** | **HHH** | **Range** | **Unit** | **Range channel** |
|---------|------------------|-----------|-----------------|--------------------------|---------|--------|-------|-------|--------|---------|-----------|----------|-------------------|
|        |                 |          |                |                         |        |       |      |      |       |        |          |         |                  |
|        |                 |          |                |                         |        |       |      |      |       |        |          |         |                  |
|        |                 |          |                |                         |        |       |      |      |       |        |          |         |                  |
|        |                 |          |                |                         |        |       |      |      |       |        |          |         |                  |
|        |                 |          |                |                         |        |       |      |      |       |        |          |         |                  |
|        |                 |          |                |                         |        |       |      |      |       |        |          |         |                  |
|        |                 |          |                |                         |        |       |      |      |       |        |          |         |                  |
|        |                 |          |                |                         |        |       |      |      |       |        |          |         |                  |
|        |                 |          |                |                         |        |       |      |      |       |        |          |         |                  |
|        |                 |          |                |                         |        |       |      |      |       |        |          |         |                  |
|        |                 |          |                |                         |        |       |      |      |       |        |          |         |                  |
