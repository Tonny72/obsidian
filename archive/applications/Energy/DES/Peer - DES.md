---
title: Peer - DES
created: [[2021-01-06]]T13:36:45.0000000+01:00
---

- # How to run
  Run `import_ALL_to_All_eng1.py` on DESENG1
  Run `tools/tstore-DESPCENG1.py` on DESENG1
  Run `reports/peer/Peer DES.py` on DESENG1
- # [[2021-01-07]] 
  Hoe werkt de peer:
  
  1.  Data wordt elke dag via TTools2 van ABB naar CSV bestanden in Onedrive gezet.
  
  2.  Manueel moet het python script 'tstore.py' (Visual Studio Code) worden gedraaid. Dit leest de ABB CSV bestanden in, worden <u>gecleaned</u> en weggeschreven in een grote CSV file per tag
  
  3.  Draai in Peer.py de cell '**<u>Resample source files'</u>**. Dit leest de gecleande data en maakt een 'resample' csv file aan. Deze file is enkel voor **debug**.
  
  4.  Draai in Peer.py de cell '**<u>Peer HTML rapport'</u>**
  
  Dit is het peer rapport
  <https://sibelco-my.sharepoint.com/:u:/p/tonny_lemmens/EWvFWqBkzHtMsdniOGqR_-8Biqv_7yezgU9bTg18sJz8Cg?e=tahbUw>