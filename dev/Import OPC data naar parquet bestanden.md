---
date created: 2025-09-17T15:02:38+02:00
date modified: 2025-09-18T08:29:37+02:00
---
# Sibelco

## Import OPC data naar parquet bestanden.
`python parquet3.py config.toml`

*Voorbeeld config.toml*
```
config_files = [
    "configs/des/silos.toml",
    "configs/des/drogers.toml",
    "configs/des/energy.toml",
    "configs/des/hydro.toml",
    "configs/des/afzakken.toml",
    "configs/des/molens.toml",
    "configs/des/calcineerovens.toml",
    "configs/des/bunkers.toml",
]

[db.pq]
type = "parquet"
path = "D:/Sibelco/Elektrische Dienst en Automatisering - Automatisering/Data/DES_PARQUET"

[db.opc]
type = "opc"

[db.pq3]
type = "parquet"
path = "C:/Users/LEMTON00/Sibelco/Elektrische Dienst en Automatisering - Automatisering/Data/DES_PARQUET_CALCULATED"
```
