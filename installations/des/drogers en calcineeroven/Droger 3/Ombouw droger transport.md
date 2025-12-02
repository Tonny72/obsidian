---
title: Ombouw droger transport
updated: [[2017-04-26]]T08:45:41.0000000+02:00
created: [[2016-09-07]]T08:20:58.0000000+02:00
---

Ombouw DX200, DX201

- # DONE bij ombouw D3 transport
  SCHEDULED: <[[2023-09-22]] Fri>
- DT_LSH_ZS41 -\> DT_LSH_ZS51 zit in advant van pc7.9.2.3:10  
  Er zijn naam variabelen voor aangemaakt.  
  LSH_ZS41_DI (DI) vervangen door DT_LSH_ZS41 (naam variabele) op alle plaatsen.
- DT_LSH_ZS41 -\> DT_LSH_ZS51 op schem zetten.
- Stalennemer herprogrammeren (ZT_SN1_xxx)
- MES Controleren
- GMP
- Lossen BU41 - BU51
- LZ2_ZS51 : FBConfig op 0 zetten FB0 werkt niet goed momenteel
  
  PROGRAMMA IS KLAAR, MAAR DE COMMUNICATIE IS TE TRAAG VOOR EEN GOEIE WERKING.
  =\> O.A. Probleem met gewicht pulsteller display aan kanaal
- #
- # [[2016-09-09]] 13:45
  Voor alle DT_LSH_ZSxx communicatie geschreven.
- # [[2017-03-22]] 
  Zie link
  <https://sibelco-my.sharepoint.com/personal/tonny_lemmens_sibelco_com/Documents/Installaties/DES%20-%20Dessel/Drogers/Ombouw%20Droger%20Transport.xlsx?web=1>
  
  HET PLAN
  
  Het Object (Motor, Klep) programmeren waar de IO zit, met alle communicatie
  
  DX200 en DX201 zijn omgebouwd.
- # [[2017-03-24]] 
  Sequentie CM is getekend.