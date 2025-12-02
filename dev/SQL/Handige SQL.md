---
date created: 2014-04-10
tags:
  - SQL
  - dev
modified: 2025-07-20
---
# Round to nearest 15 minute
```sql
dateadd(mi, datediff(mi, 0, dts) / 15 \* 15, 0)
of
DATE_BUCKET(MINUTE, 15, datetime)
	  ```
# Verwijder de niet uren
```sql
DELETE
FROM [LNKWRX_DATALOG_TM_0D0H1M0S]
WHERE dateadd(HOUR, datediff(hour, 0, timestamp), 0) != timestamp
```
# Copy data from one table into another
```SQL
INSERT INTO AA(rid, timestamp, [C_GT21_TOT_f])
SELECT rid, timestamp, [C_GT21_TOT_f] 
FROM [DATALOG_TOTAL_1M]
```
# Update column
```SQL
UPDATE database2.dbo.tablename
SET database2.dbo.tablename.colname = database1.dbo.tablename.colname
FROM database2.dbo.tablename
INNER JOIN database1.dbo.tablename ON database2.dbo.tablename.keycol = database1.dbo.tablename.keycol

UPDATE [DATALOG_DIFF_1M]
SET [DATALOG_DIFF_1M].[C_GT21_TOT_f] = [DATALOG_TOTAL_1M].[C_GT21_TOT_f] / 60
FROM [DATALOG_DIFF_1M] D
INNER JOIN [DATALOG_TOTAL_1M] ON D.timestamp = [DATALOG_TOTAL_1M].timestamp
WHERE D.timestamp >= '2014/04/10 12:16' AND D.timestamp <= '2014/04/11 8:47'
```
# Zie de velden van een VIEW
```SQL
EXEC SP_HELP VIEW_EMPLOYEES
```
# VUL TABEL MET VASTE DATUM/TIJDEN
```SQL
;With DateSequence( Date ) as
(
Select @dtsFrom as Date
union all
Select CASE @intervalType
WHEN 'minute' THEN dateadd(minute, @interval, Date)
WHEN 'hour' THEN dateadd(hour, @interval, Date)
WHEN 'day' THEN dateadd(day, @interval, Date)
WHEN 'month' THEN dateadd(month, @interval, Date)
END
from DateSequence
where Date \< @dtsTo
)

SELECT \*
FROM DateSequence
option (maxrecursion 0)
```
*From \<<https://stackoverflow.com/questions/9650045/the-maximum-recursion-100-has-been-exhausted-before-statement-completion>\>*
# Opzoeken van gelogde tags
```SQL
SELECT COLUMN_NAME,\*
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME LIKE 'DATALOG%' AND COLUMN_NAME LIKE 'C%'
```
# Lineaire regressie
  Tabel met vaste tijdstippen = Log_Energy
  Tabel met RAW values = Log_Inkoop_Import
```SQL
SELECT e.dts
	,prev.dts as prev
	,next.dts as next
	,e.HSK_PV_Inkoop_Import, ((next.HSK_PV_Inkoop_Import-prev.HSK_PV_Inkoop_Import)/(DATEDIFF(SECOND,next.dts, prev.dts))\*(DATEDIFF(SECOND,e.dts,prev.dts))) + prev.HSK_PV_Inkoop_Import
	,e.HSK_PV_Inkoop_Import - (((next.HSK_PV_Inkoop_Import-prev.HSK_PV_Inkoop_Import)/(DATEDIFF(SECOND,next.dts, prev.dts))\*(DATEDIFF(SECOND,e.dts,prev.dts))) + prev.HSK_PV_Inkoop_Import)
FROM LOG_Energy e
CROSS APPLY (
SELECT TOP 1 *
FROM LOG_Inkoop_Import Inkoop
WHERE inkoop.dts >= e.dts
ORDER BY ABS(DATEDIFF(SECOND, e.dts, Inkoop.dts))) next
CROSS APPLY (
SELECT TOP 1 *
FROM LOG_Inkoop_Import Inkoop
WHERE inkoop.dts <= e.dts
ORDER BY ABS(DATEDIFF(SECOND, e.dts, Inkoop.dts))) prev
WHERE e.dts > '2015/10/16' AND DATEDIFF(HOUR, e.dts, next.dts) < 5 AND DATEDIFF(HOUR, e.dts, next.dts) > -5 AND e.HSK_PV_Inkoop_Import is null
ORDER BY e.dts
```
  
# Leg Primary key op log tabel
```
ALTER TABLE Log_energy
ALTER COLUMN dts datetime NOT NULL
ALTER TABLE log_energy ADD PRIMARY KEY (dts)
```
