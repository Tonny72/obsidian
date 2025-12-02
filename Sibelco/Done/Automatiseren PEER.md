---
title: Automatiseren PEER
date created: 0000-01-01
tags:
  - peer
  - energy
date modified: 2025-07-24
---

- # [Planner Automatiseren PEER](https://tasks.office.com/sibelco.onmicrosoft.com/nl-be/Home/Task/ermtzK1Uc0WbwEHpAhBmgZYAI1Ih)
# [[2018-09-26]] 
  SELECT \[key\]
  ,\[mo_code\]
  ,\[resource_key\]
  ,\[resource_code\]
  ,\[resource_description\]
  ,\[job_item_code\]
  ,\[job_item_description\]
  ,\[item_code\]
  ,\[item_description\]
  ,\[start_date\]
  ,\[stop_date\]
  ,\[calendarshift_start\]
  ,\[calendarshift_stop\]
  ,\[qty_plc_prod\]
  ,\[qty_manual_prod_test\]
  ,\[qty_prod\]
  ,\[energy_electric\]
  ,\[energy_fuel\]
  ,\[energy_gas\]
  FROM \[Linkworx\].\[dbo\].\[view_peer_data\]
- # Meeting Peer (TODO's)
- [[installations/mhl/watervang]] kWh verdelen over 3 W/C
- Manuele tonnage rapporteren voor afzakken
- ST10 verdelen AF09=20%, AF10=40%, AF11=40%
- kWh-meter LSK silo's komt bij Los Bulk
- LSB_AF5 splitsen onder BBzand en FFS
- kWh-meter van LLZ naar Los Bulk
- TNZ verdelen. Verdeelsleutel: C2=130000 ton, C3=80000 ton, D3=450000 ton, D4=0 ton.
- Som van de W/C's en kostenplaatsen berekenen, en vergelijken met som van feeders
- PAU29000 wordt kostenplaats PV
# [[2018-11-15]] 
  Stijn,
  
  Ik voor volgende Workcenters / kostenplaatsen zijn er geen kWh-en in de Peer View.
  
  PBA01, PBA02, PBA03, PBA04, PBA16, PMN04, PMN05, PMN06, PMN07, PAU27000
  
  PAU31000 (windmolens) moet negatief tellen en telt nu positief
  
  Kan je dit eens nazien.
  
  Mvg
  
  Tonny
# [[2018-11-23]] 
  | PBA01_kWh    | opc.tcp://10.32.29.60:59151 | kepware | NS2\|String\|800xA.MES.PBA01.PBA01_kWh       | READ | 4665,906 | Good | [[2018-11-23]] 9:05:53 |
  |--------------|-----------------------------|---------|----------------------------------------------|------|----------|------|--------------------|
  | PBA02_kWh    | opc.tcp://10.32.29.60:59151 | kepware | NS2\|String\|800xA.MES.PBA02.PBA02_kWh       | READ | 12428,03 | Good | [[2018-11-23]] 9:06:04 |
  | PBA03_kWh    | opc.tcp://10.32.29.60:59151 | kepware | NS2\|String\|800xA.MES.PBA03.PBA03_kWh       | READ | 534,1904 | Good | [[2018-11-23]] 9:06:11 |
  | PBA04_kWh    | opc.tcp://10.32.29.60:59151 | kepware | NS2\|String\|800xA.MES.PBA04.PBA04_kWh       | READ | 4128,281 | Good | [[2018-11-23]] 9:05:45 |
  | PBA16_kWh    | opc.tcp://10.32.29.60:59151 | kepware | NS2\|String\|800xA.MES.PBA16.PBA16_kWh       | READ | 43,42456 | Good | [[2018-11-23]] 9:06:02 |
  | PMN04_kWh    | opc.tcp://10.32.29.60:59151 | kepware | NS2\|String\|800xA.MES.PMN04_07.PMN04_kWh    | READ | 10109,59 | Good | [[2018-11-23]] 9:11:18 |
  | PMN05_kWh    | opc.tcp://10.32.29.60:59151 | kepware | NS2\|String\|800xA.MES.PMN04_07.PMN05_kWh    | READ | 51336,94 | Good | [[2018-11-23]] 9:11:29 |
  | PMN06_kWh    | opc.tcp://10.32.29.60:59151 | kepware | NS2\|String\|800xA.MES.PMN04_07.PMN06_kWh    | READ | 97808    | Good | [[2018-11-23]] 9:10:02 |
  | PMN07_kWh    | opc.tcp://10.32.29.60:59151 | kepware | NS2\|String\|800xA.MES.PMN04_07.PMN07_kWh    | READ | 3901,39  | Good | [[2018-11-23]] 9:11:29 |
  | PAU27000_kWh | opc.tcp://10.32.29.60:59151 | kepware | NS2\|String\|800xA.MES.PAU27000.PAU27000_kWh | READ | 134379,1 | Good | [[2018-11-23]] 9:11:20 |
  
  De ontbrekende tags zitten in underlying en zijn OK.
# [[2018-11-27]] 
  /\*\*\*\*\*\* Script for SelectTopNRows command from SSMS \*\*\*\*\*\*/
  SELECT \[resource_code\]
  ,SUM(\[energy_electric\]) AS kWh
  FROM \[Linkworx\].\[dbo\].\[view_peer_data\]
  WHERE start_date \> '2018/11/01'
  GROUP BY resource_code
  ORDER BY resource_code
  
  Alles zit erin