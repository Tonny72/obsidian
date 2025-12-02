---
vlan: "82"
description: Brandcentrale primair
color: Zwart
tags:
  - "#be_des_vlan"
---
# Items

```dataview
TABLE rack, switch, switchnr, description
FROM #be_des_vlan82
SORT asset ASC
```
