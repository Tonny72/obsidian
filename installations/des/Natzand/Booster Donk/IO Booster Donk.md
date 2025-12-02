---
title: IO Booster Donk
updated: [[2010-11-22]]T09:44:53.0000000+01:00
created: [[2010-11-22]]T09:44:15.0000000+01:00
---

IO Booster Donk
maandag 22 november 2010
9:44

1.  ***Motoren***
| **TAG**    | **Omschrijving** | **Vergrendelingen**   |
|------------|------------------|-----------------------|
| **BD_DP**  | Dieptepomp       | BD_NSTPLOC (Auto/Man) |
| **BD_GWP** | Glandwaterpomp   | BD_NSTPLOC (Auto/Man) |
| **BD_ZP1** | Zandpomp1        | BD_NSTPLOC (Auto/Man) |
| **BD_ZP2** | Zandpomp2        | BD_NSTPLOC (Auto/Man) |
|           |                 |                      |
2.  ***Kleppen***
| **TAG** | **Omschrijving** | **Vergrendelingen** |
|---------|------------------|---------------------|
|        |                 |                    |
|        |                 |                    |
3.  ***Digitale Ingangen***
<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 24%" />
<col style="width: 15%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 19%" />
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
<td><strong>BD_STTLOC</strong></td>
<td>Start booster local</td>
<td></td>
<td></td>
<td>0.11.1.1</td>
<td></td>
</tr>
<tr class="even">
<td><strong>BD_STPLOC</strong></td>
<td>Stop booster local</td>
<td></td>
<td></td>
<td>0.11.1.2</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>BD_NSTPLOC</strong></td>
<td>Noodstop booster local</td>
<td></td>
<td></td>
<td>0.11.1.3</td>
<td></td>
</tr>
<tr class="even">
<td><strong>BD_PSL1</strong></td>
<td>Druk dieptepomp</td>
<td></td>
<td></td>
<td>0.11.1.4</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>BD_FSL1</strong></td>
<td>Glandwaterdebiet ZP1</td>
<td></td>
<td></td>
<td>0.11.1.5</td>
<td></td>
</tr>
<tr class="even">
<td><strong>BD_FSL2</strong></td>
<td>Glandwaterdebiet ZP2</td>
<td></td>
<td></td>
<td>0.11.1.6</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>BD_SZP1</strong></td>
<td>Storing ZP1</td>
<td></td>
<td></td>
<td>0.11.1.7</td>
<td></td>
</tr>
<tr class="even">
<td><strong>BD_DIZP1</strong></td>
<td>ZP1 in driehoek</td>
<td></td>
<td></td>
<td>0.11.1.8</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>BD_SZP2</strong></td>
<td>Storing ZP2</td>
<td></td>
<td></td>
<td>0.11.1.9</td>
<td></td>
</tr>
<tr class="even">
<td><strong>BD_DIZP2</strong></td>
<td>ZP2 in driehoek</td>
<td></td>
<td></td>
<td>0.11.1.10</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>BD_IDP1</strong></td>
<td>Dieptepomp in</td>
<td></td>
<td></td>
<td>0.11.1.11</td>
<td></td>
</tr>
<tr class="even">
<td><strong>BD_IGWP1</strong></td>
<td>Glandwaterpomp in</td>
<td></td>
<td></td>
<td>0.11.1.12</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>BD_LSH1</strong></td>
<td>Water in pompzaal</td>
<td></td>
<td></td>
<td>0.11.1.14</td>
<td></td>
</tr>
<tr class="even">
<td><strong>BD_TT1</strong></td>
<td>Temp. Motor te hoog</td>
<td></td>
<td></td>
<td>0.11.1.15</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>BD_TT2</strong></td>
<td>Temp. Motor te hoog</td>
<td></td>
<td></td>
<td>0.11.1.16</td>
<td></td>
</tr>
</tbody>
</table>
4.  ***Digitale Uitgangen***
| **TAG**            | **Omschrijving**             | **FP / IND** | **Aansluiting** | **Onderdeel van Object** |
|--------------------|------------------------------|--------------|-----------------|--------------------------|
| **BD_STTDP1**      | Dieptepomp start             |             | 0.11.2.1        | BD_DP                    |
| **BD_STTGWP1**     | Glandwaterpomp start         |             | 0.11.2.2        | BD_GWP                   |
| **BD_STTZP1**      | Zandpomp1 start              |             | 0.11.2.3        | BD_ZP1                   |
| **BD_STTZP2**      | Zandpomp2 start              |             | 0.11.2.4        | BD_ZP2                   |
| **BD_VERLICHTING** | Verlichting Booster          |             | 0.11.2.5        |                         |
| **BD_IH**          | Indicatie booster op hand    |             | 0.11.2.9        |                         |
| **BD_IB**          | Indicatie booster in bedrijf |             | 0.11.2.10       |                         |
| ****              |                             |             |                |                         |

******
******
5.  ***Analoge Ingangen***
| **TAG**      | **Omschrijving** | **FP/IN** | **Aansluiting** | **Onderdeel van Object** | **LLL** | **LL** | **L** | **H** | **HH** | **HHH** | **Range** | **Unit** | **Range channel** |
|--------------|------------------|-----------|-----------------|--------------------------|---------|--------|-------|-------|--------|---------|-----------|----------|-------------------|
| **BD_ITZP1** | Stroom ZP1       |          | 0.11.4.1        | BD_ZP1                   |        |       |      |      |       |        | ?         |         |                  |
| **BD_ITZP2** | Stroom ZP2       |          | 0.11.4.2        | BD_ZP2                   |        |       |      |      |       |        | ?         |         |                  |
| **BD_PT1**   | Voordruk         |          | 0.11.4.3        |                         |        |       |      |      |       |        | ?         |         |                  |
| **BD_PT2**   | Tussendruk       |          | 0.11.4.4        |                         |        |       |      |      |       |        | ?         |         |                  |
| **BD_PT3**   | Einddruk         |          | 0.11.4.5        |                         |        |       |      |      |       |        | ?         |         |                  |
|             |                 |          |                |                         |        |       |      |      |       |        |          |         |                  |
|             |                 |          |                |                         |        |       |      |      |       |        |          |         |                  |
|             |                 |          |                |                         |        |       |      |      |       |        |          |         |                  |

2.  **Testprocedure**
1.  ***DI’s***
<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 56%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>TAG</strong></p>
<p><strong>DI</strong></p></th>
<th><strong>Omschrijving</strong></th>
<th><strong></strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>BD_NSTPLOC</strong></td>
<td>Noodstop booster local</td>
<td>OK</td>
</tr>
<tr class="even">
<td><strong>BD_TT1</strong></td>
<td>Temp. Motor te hoog</td>
<td>OK</td>
</tr>
<tr class="odd">
<td><strong>BD_TT2</strong></td>
<td>Temp. Motor te hoog</td>
<td>OK</td>
</tr>
<tr class="even">
<td><strong>BD_PSL1</strong></td>
<td>Druk dieptepomp</td>
<td>OK</td>
</tr>
<tr class="odd">
<td><strong>BD_FSL1</strong></td>
<td>Glandwaterdebiet ZP1</td>
<td>OK</td>
</tr>
<tr class="even">
<td><strong>BD_FSL2</strong></td>
<td>Glandwaterdebiet ZP2</td>
<td>OK</td>
</tr>
<tr class="odd">
<td><strong>BD_LSH1</strong></td>
<td>Water in pompzaal</td>
<td>OK</td>
</tr>
<tr class="even">
<td><strong>BD_SZP1</strong></td>
<td>Storing ZP1</td>
<td>OK</td>
</tr>
<tr class="odd">
<td><strong>BD_SZP2</strong></td>
<td>Storing ZP2</td>
<td>OK</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>BD_STTLOC</strong></td>
<td><p>Start booster local</p>
<p>EERST SEQ MANUEEL ZETTEN</p></td>
<td>OK</td>
</tr>
<tr class="even">
<td><strong>BD_STPLOC</strong></td>
<td>Stop booster local</td>
<td>OK</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
2.  ***AI’s***
| **TAG**      | **Omschrijving** |    |
|--------------|------------------|-----|
| **BD_PT1**   | Voordruk         | OK  |
| **BD_PT2**   | Tussendruk       | OK  |
| **BD_PT3**   | Einddruk         | OK  |
| **BD_ITZP1** | Stroom ZP1       | OK  |
| **BD_ITZP2** | Stroom ZP2       | OK  |

3.  ***Motoren***
1.  BD_DP Dieptepomp

- Manueel starten =\> OK
  2.  BD_GWP Glandwaterpomp
- Manueel starten =\> OK
  3.  BD_ZP1 Zandpomp1
- Manueel starten =\> OK
- Stroom controleren (BD_ITZP1) =\> OK
  4.  BD_ZP2 Zandpomp2
- Manueel starten =\> OK
- Stroom controleren (BD_ITZP2) =\> OK
  5.  Noodstop
- BD_NSTPLOC vergrendelt alle 4 de pompen =\> OK
  4.  ***Sequentie***
- Start de sequentie lokaal (BD_STTLOC) =\> OK
- Stop de sequentie lokaal (BD_STPLOC) =\> OK
  
  5.  ***DO’s***
  | **TAG**            | **Omschrijving**             |    |
  |--------------------|------------------------------|-----|
  | **BD_VERLICHTING** | Verlichting Booster          | OK  |
  | **BD_IH**          | Indicatie booster op hand    |    |
  | **BD_IB**          | Indicatie booster in bedrijf | OK  |
  | ****              |                             |    |