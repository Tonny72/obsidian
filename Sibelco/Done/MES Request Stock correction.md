---
title: MES Request Stock correction
updated: [[2022-01-21]]T13:54:47.0000000+01:00
created: [[2019-05-20]]T08:56:55.0000000+02:00
---

MES Request Stock correction
maandag 20 mei 2019
8:56

Men wil via ABB een stock correctie doen.

In ABB op de faceplate van storage (zie Sibelco – Molens – Niveaumetingen – Tonnages) al een extra button ‘apply stock correction’ voorzien.

ABB -\> MES
Silo name (string)
Item (dint)
ErpStock (real)
Calc_Stock (real)
Request (bit)

MES -\> ABB
Confirm

**Programmatie**
Programma is al aangepast en kepware storage – PU40BU21 al van tags voorzien

Opzoeken van Name moet via import in kepware gebeuren

- #
- # [[2019-06-28]] 
  On hold
  M3 interface is niet goedgekeurd