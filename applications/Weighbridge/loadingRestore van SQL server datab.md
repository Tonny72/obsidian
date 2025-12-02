---
title: loadingRestore van SQL server database
updated: [[2018-08-30]]T10:43:02.0000000+02:00
created: [[2016-01-20]]T16:16:10.0000000+01:00
---

- # Procedure om de backup van een SQL database naar een nieuwe SQL Server te restoren
  
  1.  Maak op de destination server een nieuwe database aan.
  2.  Rechtsklik op de database: Tasks - Restore - Database
  3.  Source: Device  
    Kies de juiste filename (\*.bak)
  4.  Destination - Database
  5.  Kies bij Options  
    Overwrite the existing database (WITH REPLACE)
  <u>GEEN</u> Take tail-log backup before restore