---
date created: 2025-08-20T08:01:29+02:00
date modified: 2025-09-18T19:29:12+02:00
---
# Sequentie C3_Burner

```mermaid
---
config:
  layout: elk
---

flowchart TB

%% bepaal classes
  classDef step fill: #2dcfff, stroke: #000000, color: #000000
    
S1("S1: Verberg knop Doorstap <br>(hmi_doorstap_visible = 0)"):::step
S1 -- "(geen voorwaarde)" --> S2

S2("S2: BU320_Int_release = 1"):::step
S2 -- "BU320 in remote" --> S3


```

# Buttons and variables



| Tag                       | Value                           | Comment                                                |
| ------------------------- | ------------------------------- | ------------------------------------------------------ |
| BU320_Reset               |                                 |                                                        |
| BU320_00_DIESEL_READY     |                                 |                                                        |
