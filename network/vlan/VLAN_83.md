---
vlan: "83"
description: Brandcentrale secundair
color: Zwart
tags:
  - "#be_des_vlan"
---
# Items

```dataview
TABLE rack, switch, switchnr, description
FROM #be_des_vlan83
SORT asset ASC
```
