---
date created: 2018-01-26
date modified: 2025-08-30
---

- # Signalen
  | PalletOnPlace | PLC -\> Getra | Er is een pallet aanwezig                                          |
  |---------------|---------------|--------------------------------------------------------------------|
  | RunConveyer   | Getra -\> PLC | Rollenbaan mag draaien                                             |
  | Ready         | Getra -\> PLC | Printer is ready. Parallel contact met groene lamp bovenop printer |
  
  1.  Er komt een pallet aan: PalletOnPlace wordt 1
  2.  RunConveyer wordt 0
  3.  Als Getra klaar is, wordt RunConveyer terug 1
  
  **RunConveryer bij in serie met AutoCmd zetten**
  
  ![image1](image1-505.png)
  
  ![image2](image2-198.png)