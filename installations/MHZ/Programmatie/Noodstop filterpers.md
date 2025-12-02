---
date created: 2012-07-26
date modified: 2025-09-01
---

PRODMAM

Eelco Dirkx schreef op [[2012-07-26]] 9:20:47
In het scherm "Algemeen/Alarmen" staat het alarm "Noodstop filterpers OK" geblokt, bij het automatisch zetten, gaat deze in alarm maar de zeefbandpers valt niet uit. Is hier misschien een reden voor, of is het een technisch probleem? De 2 noodstoppen en de trekkoord zijn niet geactiveerd (ook getest en ze werken goed -\> bij indrukken noodstop vallen de banden uit)

Fabio heeft gecontroleerd op DI-kaart C2.0.11.105 ingang NSFP_OK is hoog. D.w.z. dat de noodstoppen ok zijn.

mvg

-----------------------------

Er zijn 2 noodstoppen in dienst

| Aanvoer\Units\Algmeen\Alarmen\NSFP_OK        | C1.0.11.101.8 |    |
|----------------------------------------------|---------------|-----|
| Verwerking\Units\Zeefbandpers\FP652\FP652_RS | C2.0.11.105.8 |    |

De DI onder aanvoer bestaat niet. =\> Verwijderd
