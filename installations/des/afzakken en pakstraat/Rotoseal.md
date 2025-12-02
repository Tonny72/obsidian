created:: [[2013-03-05]]
alias:: Rot

- ---
  created: [[2013-03-05]]T13:27:00.0000000+01:00
  ---
- # [[2015-02-24]] 13:06 
  Niveau aanduiding in dienst genomen.
  Extra klep AF6_SVA201 geplaatst
- # [[2015-01-27]] 14:49 
  Aanpassing gedaan aan niveau aanduiding buffersilo  
  <https://sibelco.box.com/s/pkmrzko78ohncx4d8jlr2oqrtf9tj246>
- # [[2015-01-14]] 13:19 
  Extra voorwaarde aansturing driller buffersilo (AF6_30)
  
  ![image1](image1-192.png)
- # [[2014-10-23]] 14:48 
  AF6_LN_AFS_DI geinverteerd in programma
  
  ![image2](image2-108.png)
- # [[2014-06-06]] 14:47 
  Programma Rotoseal overgeprogrammeerd tot pc1.7.23
  Begonnen aan OB3 omdat pc1.7.23 signalen van OB3 gebruikt
- # [[2014-05-28]] 16:28 
  Gebleven bij seq. stap 125
- # [[2014-05-27]] 16:38 
  Veel communicatie geschreven vandaag
  Gebleven bij Programmatie Stap105
- # [[2014-05-09]] 11:29 
  Sequentie in Visio voor opstarten is klaar. Voor stoppen nog niet. =\> Na tekenen beelden om overzicht te krijgen.  
  Begonnen met tekenen beeld
- # [[2014-02-18]] 9:56 
  Gisteren meeting gehad.
  
  Geert wil een visualisering van het overblaasketeltje.
  
  =\> PLC vervangen. Hiervoor is de de ombouw van zakscheur ook noodzakelijk (DAT communicatie)
  
  Het Lauer paneel kunnen we misschien behouden.
- # [[2013-07-02]] 16:26 
  Rapport: aantal zakken per minuut
  ![image3](image3-61.png)
- # [[2013-03-21]] 13:32   
  [Flashlamp voor wisselbuizen](file:///M:/OnderHd/Elektrische%20dienst/Public/Automation/Dessel/Toevoer%20Natzand/Aanpassingen/Flashlamp%20voor%20wisselbuizen.docx)
  
  | DX102.57 | TZ_WB1_H1 | Flashlamp voor wisselbuis in beweging |
  |----------|-----------|---------------------------------------|
  | DX102.58 | TZ_WB2_H1 | Flashlamp voor wisselbuis in beweging |
  | DX102.59 | TZ_WB3_H1 | Flashlamp voor wisselbuis in beweging |
- # Aanpassingen aan de Rotoseal PLC kunnen ook vanop afstand
  ![image4](image4-36.png)
- # [[2013-03-05]] 13:27   
  ![image5](image5-31.png)
  
  ![image6](image6-26.png)
  
  ![image7](image7-22.png)
  
  ![image8](image8-20.png)
- AF6_BV1_DO (DO7.1) verwijderd
- AF6_BV1_O\_DI (DI3.3) en AF6_BV1_T\_DI (DI3.4) verwijderd. Deze werden niet gebruikt in het programma
  ![image9](image9-17.png)
- # [[2013-02-01]] 9:28
- ## Uitbreiding zakkencontrole Rotoseal
- ## Beschrijving
  Band ZKT-4 geeft zakken af op band ZKT-3.
  Extra opstoppingscontrole ZKT-ZV5.
  Als er enkele seconden nadat er een zak is gepasseerd aan ZKT-ZV4, geen zak wordt gedetecteerd aan ZKT-ZV5, dan moet ZKT-4 stilvallen.
  Programma aangepast
  ![image10](image10-15.png){:height 581, :width 953}
  
  ![image11](image11-13.png)
  
  ![image12](image12-12.png)