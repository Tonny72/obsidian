#K287 

---
title: Band 4 - K287
updated: [[2020-06-11]]T13:16:31.0000000+02:00
created: [[2020-06-05]]T12:35:05.0000000+02:00
---

| LA_B4_DO     | DO13.6.4 | Band 4 start             |
|--------------|----------|--------------------------|
| LA_B4_RES    | DO13.6.5 | Band 4 reset softstarter |
| LA_B4_Draait | DI13.1.6 | B4 draait                |
| LA_B4_F      | DI13.1.7 | Softstarter in fout      |
| LA_B4_NS     | DI13.1.8 | Noodstop OK              |

# [[2020-06-08]] 
  DIT MOET OOK WORDEN AANGEPAST IN PREPARE PROJECT
- Verwijder uit SibKaai287.IO
  LA_NS4 en LA_NS4_P
- Verwijder uit SibKaai287.Laden_Par  
  LA_NS4 en LA_NS4_P
- Verwijder de Control Modules uit Algemeen  
  LA_NS4 en LA_NS4_P
- Voeg toe aan SibKaai287.Transportband_Uni  
  NS (TBoolIn noodstop)  
  F (TBoolIn softstart in fout)  
  RES (Enkel BoolIO, Reset softstarter, Noodstop)