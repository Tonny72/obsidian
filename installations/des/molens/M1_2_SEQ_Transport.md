---
date created: 2025-08-01 14:22
date modified: 2025-09-12 07:19
tags:
  - M1
  - M2
---
- #Meeltransport
- {{embed ((6719d6ca-01fc-4b4c-8a83-fc1103e7358d))}}
- {{renderer :mermaid_6719fbe6-c657-4d8d-b940-ab69b0891c28, 3}}
	- ```mermaid
	  ---
	  config:
	    look: handDrawn
	    layout: elk
	  ---
	  
	  flowchart LR
	  S49(S49: Keuzestap)
	  S51(S51: Keuzestap)
	  S60(S60: Open MT_MS01_KL_SV)
	  S70(S70: Open MT_MS02_KL_SV)
	  S80(S70: Open MT_MS03_KL_SV)
	  S90(S70: Open MT_MS03_KL_SV)
	  
	  S49 --> S51
	  subgraph one
	  S51 -- Tr51a: Keuze BU1 --> S60
	  end
	  S51 -- Tr51b: Keuze BU2 --> S70
	  subgraph two
	  S51 -- Tr51b: Keuze BU3 --> S80
	  end
	  S51 -- Tr51b: Keuze BU4 --> S90
	  S51 -- Tr51b: Keuze BU4 --> S100
	  S51 -- Tr51b: Keuze BU4 --> S110
	  S51 -- Tr51b: Keuze BU4 --> S120
	  S51 -- Tr51b: Keuze BU4 --> S130
	  S51 -- Tr51b: Keuze BU4 --> S140
	  S51 -- Tr51b: Keuze BU4 --> S150
	  S51 -- Tr51b: Keuze BU4 --> S160
	  S51 -- Tr51b: Keuze BU4 --> S170
	  S51 -- Tr51b: Keuze BU4 --> S180
	  S51 -- Tr51b: Keuze BU4 --> S190
	  S51 -- Tr51b: Keuze BU4 --> S200
	  S51 -- Tr51b: Keuze BU4 --> S210
	  
	  ```
	-