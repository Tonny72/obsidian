---
created: [[2016-10-11]]T14:02:52.0000000+02:00
---
Communicatie uitgezocht. MMS laat geen tweeweg communicatie toe (Enfin toch niet op een simpele manier)
  
Besloten om IAC te gebruiken
  Nadeel:
  IAC communicatie vars moeten in POU (bovenste unit) worden gezet.
  Ook kunnen tweeweg structures (via reverse attribute) niet onieuw embed worden in een stucture.
  
  Bijvoorbeeld
  StartStopUni ziet zo uit
  S1 - bool - retain - Start - Open - Set
  S0 - bool - retain - Stop - Sluit - Reset
  Xboolretain reverse
  
  Deze kan niet embed worden in een IAC_M4_TO_M5. Men krijgt dan een compiler fout
