---
date created: 2015-11-06
modified: 2025-08-30
---

- # Alle log data verplaatsen naar datalog_energy_calc
- ## Verplaats data van datalog_energy naar datalog_energy_calc
  
  // 0. Zoek de volgende tagid
  SELECT DISTINCT(tagid), tag
  FROM datalog_energy dl
  join tags t
  on t.ID = dl.tagID
  ORDER BY tagid
  
  // 1. Zoek per tag de data
  SELECT TOP (1000) \[tagID\], tag
  ,\[dts\]
  ,\[value\]
  FROM \[Linkworx_DES_LOG\].\[dbo\].\[Datalog_energy\] dl
  LEFT join tags t
  ON t.ID = dl.tagID
  WHERE tagID = 5
  
  // 2. Per tag de data in de juiste kolom van datalog_energy_calc steken
  MERGE INTO datalog_energy_calc T
  USING (
  SELECT dts, VALUE
  FROM Datalog_energy
  WHERE TagId = 5
  ) S
  ON T.dts = s.dts
  WHEN MATCHED THEN
  UPDATE
  SET AF09_E = value;
  
  // 3. Data uit de datalog_energy verwijderen
  DELETE
  FROM datalog_energy
  WHERE tagid = 5