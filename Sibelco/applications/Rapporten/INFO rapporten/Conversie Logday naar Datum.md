---
date created: 2014-03-20
date modified: 2025-08-31
---
# Tag: SSRS, Report
 
## =DateAdd("d", Val(Right( Str(Fields!logday.Value), Len( Fields!logday.Value)-6))-1, DateSerial(Val(Left(Str(Fields!logday.Value),5)), 1, 1))