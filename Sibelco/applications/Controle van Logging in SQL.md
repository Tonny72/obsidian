---
date created: 2020-10-15T00:00:00+02:00
date modified: 2025-10-19T22:36:35+02:00
---
# Periode '2020/01/01' tot '2020/10/13'
 
Meter: SCR_1_PM1_Active_Energy_Import
 
## Begin en Eind van de meter

```
  With b as   
  (  
  SELECT top 1 *  
  from [SCR_1_PM1_Active_Energy_Import]  
  where dts \>= '2020/01/01' and dts \< '2020/10/13' AND VALUE \> 0 and Log = 'log1'  
  order by dts  
  ),  
  e as (

   SELECT top 1 *  
  from [SCR_1_PM1_Active_Energy_Import]  
  where dts \>= '2020/01/01' and dts \< '2020/10/13' AND VALUE \> 0 and Log = 'log1'  
  order by dts desc  
  )  
  SELECT * from b  
  union  
  SELECT * from e

WITH x AS (  
SELECT *  
  ,lag([value]) over (order by dts) as lag  
  ,[Value] - lag([value]) over (order by dts) as diff  
  FROM [SCR_1_PM1_Active_Energy_Import]  
  where log = 'log1'  
  )  
  SELECT sum (diff)  
  FROM X  
  where dts \>= '2020/01/01' AND dts \< '2020/10/13'

  SELECT sum(SCR_1_PM1_Active_Energy_Import)  
  FROM datalog_calc  
  where dts \>= '2020/01/01' and dts \< '2020/10/13'

```
 
SELECT top 1 *  
from [SCR_1_PM1_Active_Energy_Import]  
where dts \>= '2020/01/01' and dts \< '2020/10/13' AND VALUE \> 0 and Log = 'log1'  
order by dts desc  
)  
SELECT * from b  
union  
SELECT * from e
 
dts Log Value Quality  
2020-01-01 00:00:58.287 Log1 38866668 good  
2020-10-12 23:55:25.541 Log1 44390056 good

### Verschil = 5 523 388 kWh
 
## Begin en Eind van de meter met calc

dts Log Value Quality  
2020-01-01 00:00:00.000 Calc 38866658.6742043  
2020-10-12 23:55:00.000 Calc 44390054.978377 calc

### Verschil = 5 523 396.3042
 
## Max - Min

### Resultaat = 5 523 388
 
## Max - Min calc

### Resultaat = 5 523 396.30417269
 
## SUM van Diffs

WITH x AS (  
SELECT *  
,lag([value]) over (order by dts) as lag  
,[Value] - lag([value]) over (order by dts) as diff  
FROM [SCR_1_PM1_Active_Energy_Import]  
where log = 'log1'  
)  
SELECT sum (diff)  
FROM X  
where dts \>= '2020/01/01' AND dts \< '2020/10/13'
 
### Resultaat = 5 523 436
 
## SUM van Diffs calc

### Resultaat = 5 523 447.41183503
 
## Sum van datalog calc

SELECT sum(SCR_1_PM1_Active_Energy_Import)  
FROM datalog_calc  
where dts \>= '2020/01/01' and dts \< '2020/10/13'
 
### resultaat = 5 518 034.18689025
 
# Conclusie1:

Het verschil tussen Min-Max-Calc en DatalogCalc is

### 5 523 396.30417269 - 5 518 034.18689025 = 5 362.11728244

DIT VERSCHIL IS TE GROOT
 
Het verschil tussen Min-Max-Calc en Sum Diffs Calc is

### 5 523 396.30417269 - 5 523 447.41183503 = -51.10766234

51.107 is exact de eerste waarde van 1/01/2020
 
Tabel gekopieerd naar SCR_1_PM1_Active_Energy_Import_decimal  
dts datetime2(3) False  
Log varchar(255) False  
Value decimal(13,3) True  
Quality varchar(255) True
 
## Begin en Eind van de meter met calc

dts Log Value Quality  
2020-01-01 00:00:00.000 Calc 38866658.674  
2020-10-12 23:55:00.000 Calc 44390054.978 calc
 
### 44390054.978 - 38866658.674 = 5 523 396.304
 
## SUM van Diffs calc

5 523 447.411
 
# Conclusie2:

Met decimalen werken geeft geen beter resultaat. Probleem zit waarschijnlijk in de datalog_calc tabel. Vermoedelijk zitten niet alle dts-sen in deze tabel.
 
DUS:  
De Calc-values in elke tabel zijn goed. Ook het werken met diffs van de calc-kWh standen geeft een nauwkeurig resultaat.
 
==TODO: Voor elke tabel nagaan of er foute log waarden in zitten.==
 
1. Ignore ALLE records met VALUE=0.
2. Ignore ALLE records met QUALITY=bad