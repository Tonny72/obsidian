---
date created: 2024-07-25
tags:
  - SQL
modified: 2025-08-30
---
## Event Query
#SQL 
```SQL
  SELECT TOP (1000) [datetime]
      ,[source]
      ,[condition]
      ,[message]
      ,[severity]
      ,[ackrequired]
  FROM [datalogging].[dbo].[ABBOPCAE]
  ORDER by [datetime] desc
```
## Meest voorkomende events
#SQL 
```SQL
  SELECT source, COUNT(*) 
  FROM abbopcae where datetime > '2024-07-26' 
  GROUP BY source 
  ORDER BY 2 DESC
```
## Log
  [[../../journals/older/2024/07/2024-07-25]]
- Het project AE logging terug werkend gemaakt om logging van Molen 4 en Hydro te kunnen doen.
- Path: D:\\OneDrive - Sibelco\\DEV\\.NET Legacy\\TTools - AE only
- **Dit werkt enkel op een server, niet ENGClient ("access denied")**
- Is vermoedelijk 32bit.
- Ik krijg het niet in [[dev/Python/Python]] klaar. Ik weet niet naar welk COM object ik moet connecteren