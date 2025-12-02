---
date created: 2025-01-23 08:33
tags:
  - sequentie
description:
---

```mermaid
flowchart TB

%% bepaal classes
    classDef init fill: #2daeef, stroke: #000000, color: #ffffff
    classDef tr fill: #ffffff, stroke: #000000, color: #000000
    classDef step fill: #2daeef, stroke: #000000, color: #ffffff


S800(S800: Start MT_6):::step
S805(S805: Open MT_KD):::step
S810(S810: Keuzestap):::step
S815(S815: Stop MT_5):::step
S850(S850: Keuzestap):::step
S855(S855: Sluit MT_WK01):::step

S800 -- Tr800: MT_6 draait --> S805
S805 -- Tr805: MT_KD is open --> S810
S810 -- Tr810a: MT_5 draait --> S815
S810 -- Tr810b: MT_5 draait niet --> S850
S815 -- Tr815: MT_5 draait niet --> S850
S850 -- Tr850a: MT_WK01 is open --> S855
S855 -- Tr860: MT_WK01 is toe --> S865
S865 -- Tr865: Wacht 1 minuut --> S870
```
