---
date created: 2013-06-18
tags:
  - SQL
modified: 2025-07-20
---
# AutoClose
Zet AutoClose uit voor databases. AutoClose dealloceert resources indien niemand met de database is verbonden.
```SQL
Select name, is_auto_close_on
From sys.databases
Alter database linkworx
Set auto_close Off
```
# AutoShrink
Zet AutoShrink uit. Dit zorgt voor fragmentatie
```SQL
Select name, is_auto_shrink_on
From sys.databases
Alter database linkworx
Set auto_shrink off
```

# Recovery Models
Afhankelijk van het recovery model kan een backup worden gerestored
```SQL
Select name, recovery_model_desc
From Sys.databases
Alter database linkworx
Set recovery simple
-- simple, bulk_logged, full
```

# Statistics update mode
Used by sql server to decide which index to use
Synchronous forces queries to wait when stats are out of date
Asynchronous allows queries to continue with ols stats and builds new ones in the background =\> Meestal beter

  Select name, is_auto_update_stats_on, is_auto_stats_async_on
  From sys.databases
  Alter database linkworx
  Set auto_update_statistics_async ON
# Restricted Access
  Single_user, Restricted_user, Multi_user
  
  Gebruik Multi_user. Dit is default
# Verwijderen replicatie
  1.  sp_removedbreplication ‘dbname’
  
