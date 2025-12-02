---
title: IO Booster Maat
updated: [[2010-11-22]]T10:09:09.0000000+01:00
created: [[2010-11-22]]T10:08:44.0000000+01:00
---

1.  ***Motoren***
<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 27%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>TAG</strong></th>
<th><strong>Omschrijving</strong></th>
<th><strong>Vergrendelingen</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>BM_ZP1</strong></td>
<td>Zandpomp</td>
<td><p>BM_GP1 moet draaien</p>
<p>BM_GP2 moet draaien</p>
<p>BM_WP1 moet draaien</p>
<p>BM_OP1 moet draaien</p>
<p>BM_FSL1=1</p>
<p>BM_FSL2=1</p>
<p>BM_FSL3=1</p>
<p>BM_FSL4=1</p>
<p>BM_FSL5=1</p>
<p>BM_FSH=0</p>
<p>BM_VC1=0</p>
<p>BM_VC2=0</p>
<p>BM_VC3=0</p>
<p>BM_VC4=0</p>
<p>BM_LSH=0</p>
<p>BM_PCT1=0</p>
<p>PM_PT1&gt;LL (2bar)</p>
<p>BM_PT1&lt;HH (6bar)</p>
<p>BM_TT4 &gt; HH (75°C)</p>
<p>BM_TT5 &gt; HH (75°C)</p>
<p>BM_TT6 &gt; HH (85°C)O</p>
<p>(BR1_3_DI=0 Fout softstarter</p></td>
</tr>
<tr class="odd">
<td><strong>BM_GP1</strong></td>
<td>Glandpomp1</td>
<td>BM_WP1 moet draaien</td>
</tr>
<tr class="even">
<td><strong>BM_GP2</strong></td>
<td>Glandpomp2</td>
<td>BM_WP1 moet draaien</td>
</tr>
<tr class="odd">
<td><strong>BM_WP1</strong></td>
<td>Waterpomp1</td>
<td>geen vergrendelingen</td>
</tr>
<tr class="even">
<td><strong>BM_OP1</strong></td>
<td>Oliepomp1</td>
<td>geen vergrendelingen</td>
</tr>
</tbody>
</table>

******
2.  ***Digitale Ingangen***
| **TAG**         | **Omschrijving**                          | **Aktieve waarde** | **Faceplate / Indicatie** | **Aansluiting** | **Onderdeel van Object** |
|-----------------|-------------------------------------------|--------------------|---------------------------|-----------------|--------------------------|
| **BM_ZP1I**     | Zandpomp draait                           | 1                  | \-                        | C1.0.11.1.1     | BM_ZP1                   |
| **BM_ZP1S**     | Zandpomp in storing                       | 1                  | \-                        | C1.0.11.1.2     | BM_ZP1                   |
| **BM_GP1I**     | Glandpomp1 draait                         | 1                  | \-                        | C1.0.11.1.3     | BM_GP1                   |
| **BM_GP2I**     | Glandpomp2 draait                         | 1                  | \-                        | C1.0.11.1.4     | BM_GP2                   |
| **BM_WP1I**     | Waterpomp1 draait                         | 1                  | \-                        | C1.0.11.1.5     | BM_WP1                   |
| **BM_OP1I**     | Oliepomp1 draait                          | 1                  | \-                        | C1.0.11.1.6     | BM_OP1                   |
|                |                                          |                   |                          |                |                         |
| **BM_FSL1**     | Debiet glandpomp1                         | 1                  | FP                        | C1.0.11.1.9     |                         |
| **BM_FSL2**     | Debiet glandpomp2                         | 1                  | FP                        | C1.0.11.1.10    |                         |
| **BM_FSL3**     | Oliedebiet oliekoeling lagers zandpomp    | 1                  | FP                        | C1.0.11.1.11    |                         |
| **BM_FSL4**     | Waterdebiet oliekoeling lagers zandpomp   | 1                  | FP                        | C1.0.11.1.12    |                         |
| **BM_FSL5**     | Waterdebiet koeling reductiekast zandpomp | 1                  | FP                        | C1.0.11.1.13    |                         |
| **BM_TR_AL_DI** | Alarm HStrafo DGPT2                       | 1                  | FP                        | C1.0.11.1.14    |                         |
| **BM_NSTP_IN**  | Noodstop in                               | 0                  | IN                        | C1.0.11.1.15    |                         |
| **BM_LSH1**     | Water in pompzaal                         | 1                  | FP                        | C1.0.11.1.16    |                         |
|                |                                          |                   |                          |                |                         |
| **BM_VC1_DI**   | Trillingsmeting motor aszijde             | 1                  | FP                        | C1.0.11.2.1     |                         |
| **BM_VC2_DI**   | Trillingsmeting motor ventzijde           | 1                  | FP                        | C1.0.11.2.2     |                         |
| **BM_VC3_DI**   | Trillingsmeting reductiekast              | 1                  | FP                        | C1.0.11.2.3     |                         |
| **BM_VC4_DI**   | Trillingsmeting lager pomp                | 1                  | FP                        | C1.0.11.2.4     |                         |
| **BM_FSH1**     | Glandwaterlek na pomp                     | 1                  | FP                        | C1.0.11.2.5     |                         |
| **BM_PCT1**     | Temp. Motor zandpomp 1                    | 1                  | FP                        | C1.0.11.2.6     |                         |
3.  ******
******
4.  ***Digitale Uitgangen***
| **TAG**        | **Omschrijving** | **Faceplate** | **indicatie op scherm** | **Aansluiting** | **Onderdeel van Object** |
|----------------|------------------|---------------|-------------------------|-----------------|--------------------------|
|               |                 |              |                        |                |                         |
| **BM_ZP1_STT** | Zandpomp start   |              |                        |                |                         |
| **BM_GP1_STT** | Glandpomp1 start |              |                        |                |                         |
| **BM_GP2_STT** | Glandpomp2 start |              |                        |                |                         |
| **BM_WP1_STT** | Waterpomp start  |              |                        |                |                         |
| **BM_OP1_STT** | Oliepomp start   |              |                        |                |                         |

******
******
5.  ***Analoge Ingangen***
| **TAG**      | **Omschrijving**                        | **FP/IN** | **Aansluiting** | **Onderdeel van Object** | **LLL** | **LL** | **L** | **H** | **HH** | **HHH** | **Range** | **Unit** | **Range channel** |
|--------------|-----------------------------------------|-----------|-----------------|--------------------------|---------|--------|-------|-------|--------|---------|-----------|----------|-------------------|
|             |                                        |          |                |                         |        |       |      |      |       |        |          |         |                  |
| **BM_PT1**   | Aanzuigdruk                             | FP        | C1.1.90.4.1     |                         |        |       |      |      |       |        |          |         |                  |
| **BM_PT2**   | Persdruk                                | FP        | C1.1.90.4.2     |                         |        |       |      |      |       |        |          |         |                  |
| **BM_VT1**   | Spanning trafo 690                      | FP        | C1.1.90.4.3     |                         |        |       |      |      |       |        |          |         |                  |
| **BM_IT1**   | Stroom trafo 690                        | FP        | C1.1.90.4.4     |                         |        |       |      |      |       |        |          |         |                  |
| **BM_ITZP1** | Stroom ZP1                              | \-        | C1.1.90.4.5     | BM_ZP1                   |        |       |      |      |       |        |          |         |                  |
|             |                                        |          |                |                         |        |       |      |      |       |        |          |         |                  |
| **BM_TT4**   | Temp. olie voor lager ZP                | FP        | C1.1.90.5.1     |                         |        |       |      |      |       |        |          |         |                  |
| **BM_TT5**   | Temp. olie na lager ZP                  | FP        | C1.1.90.5.2     |                         |        |       |      |      |       |        |          |         |                  |
| **BM_TT6**   | Temp. koeling reductiekast              | FP        | C1.1.90.5.3     |                         |        |       |      |      |       |        |          |         |                  |
| **BM_FT1**   | Lekdetectie tussen binnen en buitenpomp | FP        | C1.1.90.5.5     |                         |        |       |      |      |       |        |          |         |                  |
