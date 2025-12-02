---
date created: 2014-10-09
modified: 2025-08-31
---

[Vullingen - Spreadsheet.xlsx](assets/resources/Vullingen_-_Spreadsheet.xlsx)
![image1](image1-598.png)
![image2](image2-253.png)

- # SQL query
  SELECT SUM(\[Aantal_Pulsen\]/10.0) as Liter
  FROM \[tankstation\].\[dbo\].\[Resultaten\]
  --WHERE Datum_Tijd \>= '2013/11/7 12:00' and Datum_Tijd \< '2014/02/5 12:00'
  WHERE Datum_Tijd \>= '2014/02/5 12:00' and Datum_Tijd \< '2014/07/8 12:00'
  --WHERE Datum_Tijd \>= '2014/07/8 12:00' and Datum_Tijd \< '2014/09/12 12:00'