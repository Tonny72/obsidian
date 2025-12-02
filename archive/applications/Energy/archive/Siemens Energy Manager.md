---
title: Siemens Energy Manager
tags: [energy]
date created: 2019-11-12T14:22:29+01:00
date modified: 2025-10-20T20:17:48+02:00
---
# Requirements Energy Manager Software
 
1. Omzetting kWh stand naar kWh￼Van de verschillende energy meters wordt de kWh-stang gelogd, maar voor rapportage wordt kWh per uur / dag / maand genomen. Dit moet makelijk kunnen gebeuren
 
2. Berekeningen voor verdeling￼Een kWh meter wordt soms gemeenschappelijk gebruikt voor meedere kostenplaasten￼￼Voorbeeld

|   |   |   |   |   |   |
|---|---|---|---|---|---|
|Datum tijd|kWh stand|verbruik|% verdeling|Kostenplaats 1|Kostenplaats 2|
|01:00u|100|||||
|02.00u|110|10 kWh|50%|5 kWh|5 kWh|
|03.00u|120|10 kWh|60%|6 kWh|4 kWh|
|04.00u|140|20 kWh|100%|20 kWh|0 kWh|
|05.00u|200|60 kWh|0%|0 kWh|60 kWh|
 4. Mogelijk tot query van de SQL server / Gebruik van Microsoft Power BI￼Toegang tot de data in de database is essentieel. Gebruik van een externe rapportage-tool.
   

5. Loggen van data op basis van events￼Bij wijziging van een tag de kWh stand loggen zodat deze een nauwkeurig verbruik in de rapportage weergeeft.￼Bv bij wijziging van 'product A' naar 'product B'￼
 
# Mogelijkheden?
 
1. Binnenhalen van web-data.￼Voorspellen van zon- en windenergie adv weervoorspellingen