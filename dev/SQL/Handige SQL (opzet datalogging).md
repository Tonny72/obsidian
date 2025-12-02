---
tags: [SQL]
modified:  2025-07-20
date created: 2023-04-14T00:00:00+02:00
date modified: 2025-09-24T09:17:34+02:00
---
# Handige SQL (opzet datalogging)
vrijdag 14 april 2023
9:48

Step 2: Create partition function
*From \<<https://www.mssqltips.com/sqlservertip/6974/sql-server-table-partitioning-columnstore-index/>\>*
```SQL
--Create date partition function with increment by month.
DECLARE @DatePartitionFunction nvarchar(max) =
N'CREATE PARTITION FUNCTION DatePartitionFunction (datetime2)
AS RANGE RIGHT FOR VALUES (';
DECLARE @i datetime2 = '20180101';
WHILE @i \< '20401201'
BEGIN
SET @DatePartitionFunction += '''' + CAST(@i as nvarchar(10)) + '''' + N', ';
SET @i = DATEADD(MM, 1, @i);
END
SET @DatePartitionFunction += '''' + CAST(@i as nvarchar(10))+ '''' + N');';
EXEC sp_executesql @DatePartitionFunction;
GO

Step 3: Create partition scheme
**
CREATE PARTITION SCHEME DatePartitionScheme
AS PARTITION DatePartitionFunction
ALL TO (\[PRIMARY\])
GO
```


