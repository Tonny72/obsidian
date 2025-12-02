---
date created: Invalid date
date modified: 2025-08-30
---
Open de device catalog
![image1](image1-33.jpg)
In de catalog, selecteer de ilc150 en sleep deze met ingedrukte linkermuistoets naar de bustructuur bovenaan:
![image2](image2-21.jpg)
Sleep naar boven tot de naam van het project ‘ voorbeeld ip connect’
![image3](image3-11.jpg)
De ilc150 komt eronder te staan, de rode R van resource mankeert nog zoals bij de andere PLC’s.
![image4](image4-10.jpg)
Deze Resource moet via program worx geimporteerd worden:
Ga naar program worx
![image5](image5-6.jpg)

Ga naar de physical hardware en via rchtermuistoets import configuration
![image6](image6-3.jpg)
Type als naam de derde configuratiehardware in ‘STD_CNF3’ en plc type eCLR (=cpu voor ilc150)
![image7](image7-2.jpg)
De physicale hardware configuration is geupdated
![image8](image8-3.jpg)
Nu nog invoegen van hardware resource via
![image9](image9-2.jpg)
Afhankelijk van de hardwareversie van de ilc150 moet verschillende processor type (ilc150 of ilc150_2) gekozen worden:
![image10](image10-3.jpg)
Voeg een taak in via
![image11](image11-2.jpg)
Benoem deze default (=snelste taak)
![image12](image12-1.jpg)
De taaksettings verschijnen, druk op ok;
![image13](image13-2.jpg)
Ga naar de busview via
![image14](image14-2.jpg)
en bemerk dat er een resource is bijgekomen onder not connected. Deze moet nog versleept worden onder de ilc150 ter activatie hardware

![image15](image15.jpg)

Versleep naar boven onder resource toegevoegde ILC150 en bekom volgend resultaat
![image16](image16.jpg)

Ga terug naar de program view via
![image17](image17-1.jpg)

Nu moeten er nog POU aangemaakt worden, bv een ‘test’ en ingevoegd worden in de default task ter uitvoering;
![image18](image18-1.jpg)

Een test program wordt geimporteerd
![image19](image19.jpg)

Dit programma (momenteel leeg) is aangevuld in de POU’s en moet nog geactiveerd worden in de physicale hardware via

![image20](image20.jpg)

Benoem deze programinstance ‘test’ en selecteer uw POU via program type ‘test’
![image21](image21.jpg)
en bekom volgende venster
![image22](image22.jpg)

Ten laatste rebuild project via ter testen ofdat alles gelukt is (via menu build \> rebuild)
![image23](image23.jpg)
In de message window zullen dan geen fouten getoond worden, indien zo \> OK , indien niet is er ergens een fout geslopen.
![image24](image24.jpg)
OPMERKING
Bij het verslepen van een resource van Unconnected naar Resource, plaats de pijl achter resource.
![image25](image25.jpg)
