---
title: Logging Herzien
updated: [[2022-07-13]]T14:19:49.0000000+02:00
created: [[2019-10-11]]T08:22:07.0000000+02:00
---

> Logging Herzien
vrijdag 11 oktober 2019
8:22

(Recurring task in Outlook)

1s – 31dagen = 2678400 punten
5s – 31 dagen = 535680 punten
10s – 31 dagen = 267840 punten
30s – 31 dagen = 89280 punten
1min – 31 dagen = 44640 punten

1s – 14 dagen (1209600), 5s – 3maanden (1607040) = 2816640 punten
1s – 14 dagen (1209600), 5s – 1 maand (535680), 30s – 1 jaar (1051200) = 2796480 punten
1s – 7 dagen (604800), 5s – 1 maand (535680), 30s – ½ jaar (527040),
1s – 14 dagen (1209600), 1m - 62 dagen (89280), 1h - 620 dagen (14880) = 1313760 punten
[[2019-10-11]]
De logging via HDA logger werkt.

- # [[2019-10-16]] 
  En Goed :-)
  Geert Staes op de hoogte gebracht
- # [[2020-01-06]] 
  Taak verhuist naar Outlook
- # [[2020-03-23]] 
  Database Logging
  Geen logging per seconde bewaren. Enkel de laatste om te weten waar men was gebleven
  5s - 2 maanden = 1071360 punten
  
  1min - 1 jaar = 525600
  
  Totaal = 1.596.960 punten
- # [[2020-05-29]] 
  Due date naar 09/2020
- # [[2020-07-30]] 
  Voor de sentron pacs deze logging
  1s – 14 dagen (1209600), 1m - 62 dagen (89280), 1h - 620 dagen (14880) = 1313760 punten
  voor TotalActivePower toegevoegd
  
  Door gebruik te maken van geagregreerde datalog, worden deze mooi afgerond en
- # [[2021-05-01]] 
  Bij opslag in CSV bestanden is er eigenlijk geen beperking
  Op dit moment bevat de DES\DATA directory 24GB met .csv bestanden
  Data wordt gebruikt voor:
- Peer berekening (logging 1min of 5min)
- Trend data: (logging 1h, 1 dag, 1 week, 1 maand)
- # [[2021-12-23]] 
  Voor Sentron Pacs logging op 1 minuut gezet
- # [[2022-07-13]] 
  Harde schijf van CS loopt vol.
  Logging aangepast