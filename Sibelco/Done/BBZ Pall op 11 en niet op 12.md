---
date created: 2018-04-09]]T11:41:17.0000000+02:00
---

![image1](image1-4%201.jpeg)

Nog foutmeldingen:
BB: gn pall op 1/pos1, gn op BB -\> Intlk_366
BB: pall detectie op 2 & nt op 1 -\> Intlk_349

- # Werking / verklaring code
  | Auto_sta_Rol_afvoer12_FWD := M67 OR M73 OR M81 | Rol12 wordt gestart                                                                                 |
  |------------------------------------------------|-----------------------------------------------------------------------------------------------------|
  | M67 = Start afvoer rollenbaan sectie 1         |                                                                                                    |
  | OP_BB_Opgehangen                               | Drukknop panel 'Bigbag Hangt'. Deze wordt bediend als de bigbag is opgehangen en mag worden gevuld. |
  | OP_BB_afhalen                                  | Drukknop panel 'Bigbag Weg'. Deze wordt bediend als de bigbag volledig is gevuld.                   |
- # [[2018-05-07]] 
  T_intlk366 op 5minuten gezet (stond op 50s)