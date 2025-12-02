---
date created: 2014-02-06
modified: 2025-08-31
---

Stijn,

Voor de implementatie van Lawson gaat men ook een nieuwe versie van Objective installeren.

DCS gaat uw view in de database overnemen.

Maar de bunkernamen worden ook aangepast.

De nieuwe namen zien er zo uit:
![image1](image1-19.gif)

Als ik in de view RIGHT(Bunker_Code,4) dan werkt dit in de loading app.
Maar dit willen we liever niet doen omdat er mogelijk ooit een P45BU52 komt.

Ik heb een keer het .sdf bestand aangepast, maar ik weet niet juist welke velden worden gebruikt.

![image2](image2-5.gif)

Ik heb zowel loadingplace als silocode aangepast gehad, maar dat lijkt niet te werken.

Jij hebt ook een 'loading' database op de objective server aangemaakt. Moet die ook worden overgezet.

Ik heb download.config.xml en upload.xml aangepast naar de nieuwe (test) database. Maar ik kan niet aanloggen in de loadingApp.

Er is ook nog een bug (ik denk devexpress versie porbleem). Als ik op een Sailor het scherm overneem en aanlog en op Silos klik, dan crasht de loadingApp

![image3](image3-3.gif)
