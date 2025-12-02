created:: 2010-11-19

created: [[2010-11-19]]T13:17:57.0000000+01:00
---

-
- Gebruik Valvecon
  Omschrijving
  Hoe een valvecon onder Advant gebruiken.
  Aanmaken in de database
  CRDB MMCX
  Aanmaken in programma
  IS OR(2) en VALVECON(0,1)
  Aansluiten
  ![image1](image1-551.png)
  Parameters in de database
  Om de klep in normale mode (=central mode) te laten werken en dat de operator de klep vrij kan bedienen, moet de **ORD_BLK** op **H’FC07** staan.
  Klep kan in central gezet worden, manueel / automatisch, open / toe en de interlock in override / normal.
  | bit             | 1        | 2   | 3   | 4   |    | 5        | 6        | 7     | 8    |    | 9                | 10              | 11  | 12   |    | 13       | 14      | 15   | 16    |
  |-----------------|----------|-----|-----|-----|-----|----------|----------|-------|------|-----|------------------|-----------------|-----|------|-----|----------|---------|------|-------|
  | 1 = block order | 1        | 1   | 1   | 1   |    | 1        | 1        | 0     | 0    |    | 0                | 0               | 0   | 0    |    | 0        | 1       | 1    | 1     |
  |                | Not Used |    |    |    |    | Not Used | Sequence | Close | Open |    | Normal interlock | Block interlock | Man | Auto |    | Centrail | Standby | Test | Local |
  Oude Methode
  Zet eerst de ORD_BLK op default. = H’0000
  Zet de klep via de faceplate in Central mode.
  Zet de order en event blocking in.
  ![image2](image2-222.png)
  De klep moet in central mode staan, anders kan de klep niet manueel bediend worden.