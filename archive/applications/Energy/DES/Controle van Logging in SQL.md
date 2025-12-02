---
date created: 2020-10-15T00:00:00+02:00
modified: 2025-08-30
date modified: 2025-12-02T11:40:08+01:00
---
- created: [[2020-10-15]]
  tags: #energy
- # Periode '2020/01/01' tot '2020/10/13'
  
  Meter: SCR_1\_PM1_Active_Energy_Import
- ## Begin en Eind van de meter
  
  ```sql
  With b as
  (
  SELECT top 1 \*
  from \[SCR_1\_PM1_Active_Energy_Import\]
  where dts \>= '2020/01/01' and dts \< '2020/10/13' AND VALUE \> 0 and Log = 'log1'
  order by dts
  ),
  e as (
  
  SELECT top 1 \*
  from \[SCR_1\_PM1_Active_Energy_Import\]
  where dts \>= '2020/01/01' and dts \< '2020/10/13' AND VALUE \> 0 and Log = 'log1'
  order by dts desc
  )
  SELECT * from b
  union
  SELECT * from e
  ```
	- Verschil = 5 523 388 kWh
- ## Begin en Eind van de meter met calc
	- Verschil = 5 523 396
- ## Max - Min
	- Resultaat = 5 523 388
- ## Max - Min calc
	- Resultaat = 5 523 396
- ## SUM van Diffs
  
  ```sql
  WITH x AS (
  SELECT \*
  ,lag(\[value\]) over (order by dts) as lag
  ,\[Value\] - lag(\[value\]) over (order by dts) as diff
  FROM \[SCR_1\_PM1_Active_Energy_Import\]
  where log = 'log1'
  )
  SELECT sum (diff)
  FROM X
  where dts \>= '2020/01/01' AND dts \< '2020/10/13'
  ```
	- Resultaat = 5 523 436
- ## SUM van Diffs calc
	- Resultaat = 5 523 447
- ## Sum van datalog calc
- ```sql
  SELECT sum(SCR_1\_PM1_Active_Energy_Import)
  FROM datalog_calc
  where dts \>= '2020/01/01' and dts \< '2020/10/13'
  ```
	- resultaat = 5 518 034
- # Conclusie 1:
	- Het verschil tussen Min-Max-Calc en DatalogCalc is 5 523 396 - 5 518 034 = 5 362
-
- DIT VERSCHIL IS TE GROOTHet verschil tussen Min-Max-Calc en Sum Diffs Calc is
- 5 523 396 - 5 523 447 = -51.10766234 
  51.107 is exact de eerste waarde van [[2020-01-01]]
  
  Tabel gekopieerd naar SCR_1\_PM1_Active_Energy_Import_decimal
  dtsdatetime2(3)False
  Logvarchar(255)False
  Valuedecimal(13,3)True
  Qualityvarchar(255)True
- ## Begin en Eind van de meter met calc
- dtsLogValueQuality
  [[2020-01-01]] 00:00:00.000Calc38866658.674
  [[2020-10-12]] 23:55:00.000Calc44390054.978calc
- 44390054.978 - 38866658.674 = 5 523 396.304
- ## SUM van Diffs calc
  5 523 447.411
- # Conclusie2:
  Met decimalen werken geeft geen beter resultaat. Probleem zit waarschijnlijk in de datalog_calc tabel. Vermoedelijk zitten niet alle dts-sen in deze tabel.
  
  DUS:
  De Calc-values in elke tabel zijn goed. Ook het werken met diffs van de calc-kWh standen geeft een nauwkeurig resultaat.
  
  TODO: Voor elke tabel nagaan of er foute log waarden in zitten.
  
  1.  Ignore ALLE records met VALUE=0.
  2.  Ignore ALLE records met QUALITY=bad