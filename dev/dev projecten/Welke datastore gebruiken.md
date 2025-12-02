---
modified:  2025-08-29
date created: 2023-04-11T00:00:00+02:00
date modified: 2025-09-19T21:05:37+02:00
---
PowerBI valt uit de scope vanwege te trage import.
 
# Bestandsgrootte

![Exported image](Exported%20image%2020250721193505-0.png)  

Voor MSSQL (met columnstore index): 100 miljoen records: ongeveer 7GB =\> 15_267_44 records/GB  
Voor CSV 19_079_960 records = 1,1 GB =\> 18_891_049 records/GB
 
**Conclusie: DuckDB heeft de beste compressie**
 
# Vergelijking features

|   |   |   |   |   |   |
|---|---|---|---|---|---|
||CSV|duckdb|MSSQL|parquet|json|
|Import in Excel|ja|nee|ja|nee|ja|
|editor available|ja|DBeaver|ja|nee|ja|
|Import in Polars|ja|ja|niet werkend gekregen|ja|ja|
|View Online|deels|nee|nee|nee|nee|
|SQL Views mogelijk|nee|ja|ja|nee|nee|
|kleine files|ja|nee|nee|ja|ja|
 
# Duckdb in [[dev/dev tools/pycharm/PyCharm]]

Download de driver  
[Central Repository: org/duckdb/duckdb_jdbc/0.8.1 (maven.org)](https://repo1.maven.org/maven2/org/duckdb/duckdb_jdbc/0.8.1/)
 
En voeg de .jar toe tot  
**Vergeet niet de Class te kiezen**

![Exported image](Exported%20image%2020250721193505-1.png)  
Maak een datasource koppeling  
voorbeeld: jdbc:duckdb:C:\Users\lemton00\OneDrive - Sibelco\DEV\engineering_test_timezone\DATA\duck2.duckdb
 
Kies No Authentication. Als er een melding van Authentication komt, dan is de db mogelijk ergens anders in gebruik  
**Zelfs in Pycharm kan de connectie bij Database en een console niet tegelijk open**
 ![Exported image](Exported%20image%2020250721193506-2.png)
 