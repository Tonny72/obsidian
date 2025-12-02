---
date created: 2015-09-09
tags:
  - SQL
modified: 2025-07-20
---
# Oproepen van een stored procedure
```SQL
USE [Linkworx_DES_LOG]
GO

DECLARE@return_value int,
@interval int = 87000,
@maxpunt int = 1000,
@intervalIsMonth bit

EXEC\[dbo\].\[sp_CalculateTimeInterval\]
@dtsFrom = '2015/01/01 00:00',
@dtsTo = '2015/10/01 15:30',
@maxPoint = @maxpunt OUTPUT,
@interval = @interval OUTPUT,
@intervalIsMonth = @intervalIsMonth OUTPUT

SELECT@interval as N'@interval',
@intervalIsMonth as N'@intervalIsMonth'

SELECT'Return Value' = @return_value

GO
```

