\> [!caution] This page contained a drawing which was not converted.   
 
# 24/02/2015 13:06

Niveau aanduiding in dienst genomen.  
Extra klep AF6_SVA201 geplaatst
 
# 27/01/2015 14:49

Aanpassing gedaan aan niveau aanduiding buffersilo  
[https://sibelco.box.com/s/pkmrzko78ohncx4d8jlr2oqrtf9tj246](https://sibelco.box.com/s/pkmrzko78ohncx4d8jlr2oqrtf9tj246)
 
# 14/01/2015 13:19

Extra voorwaarde aansturing driller buffersilo (AF6_30)

![Machine generated alternative text AFS AFS 30 30 V...](../../../../../../../../assets/images/Exported%20image%2020250721204332-0.png)  

# 23/10/2014 14:48

AF6_LN_AFS_DI geinverteerd in programma

![Machine generated alternative text 143 f2 D Il 5AF...](../../../../../../../../assets/images/Exported%20image%2020250721204336-1.png)  

# 6/06/2014 14:47

Programma Rotoseal overgeprogrammeerd tot pc1.7.23  
Begonnen aan OB3 omdat pc1.7.23 signalen van OB3 gebruikt
 
# 28/05/2014 16:28

Gebleven bij seq. stap 125
 
# 27/05/2014 16:38

Veel communicatie geschreven vandaag  
Gebleven bij Programmatie Stap105
 
# 9/05/2014 11:29

Sequentie in Visio voor opstarten is klaar. Voor stoppen nog niet. =\> Na tekenen beelden om overzicht te krijgen.  
Begonnen met tekenen beeld
 
# 18/02/2014 9:56

Gisteren meeting gehad.  
Geert wil een visualisering van het overblaasketeltje.  
=\> PLC vervangen. Hiervoor is de de ombouw van zakscheur ook noodzakelijk (DAT communicatie)  
Het Lauer paneel kunnen we misschien behouden.
 
# 2/07/2013 16:26

Rapport: aantal zakken per minuut

![Machine generated alternative text 16 14 12 lo 8 6...](../../../../../../../../assets/images/Exported%20image%2020250721204336-2.png)  

# 21/03/2013 13:32
 
[Flashlamp voor wisselbuizen](file:///M:\OnderHd\Elektrische%20dienst\Public\Automation\Dessel\Toevoer%20Natzand\Aanpassingen\Flashlamp%20voor%20wisselbuizen.docx)
 
|   |   |   |
|---|---|---|
|DX102.57|TZ_WB1_H1|Flashlamp voor wisselbuis in beweging|
|DX102.58|TZ_WB2_H1|Flashlamp voor wisselbuis in beweging|
|DX102.59|TZ_WB3_H1|Flashlamp voor wisselbuis in beweging|
 
# Aanpassingen aan de Rotoseal PLC kunnen ook vanop afstand #important #remember-for-later

![Connection Path ROTOSEAL X3 3 1 1](../../../../../../../../assets/images/Exported%20image%2020250721204337-3.png)  

# 5/03/2013 13:27
 ![05MAR201313 2B 3Dpc 14 122 0 apc 122421 DAT6B2RLLB...](../../../../../../../../assets/images/Exported%20image%2020250721204337-4.png)  
![05MAR201313 29 42 SEQ 47SEQ ALG ALG ROT ROT PCI 72...](../../../../../../../../assets/images/Exported%20image%2020250721204338-5.png)  
![D5MAR2D1313 31 DAT6B2 RLL BI BI VAL UE2 s IE3 El V...](../../../../../../../../assets/images/Exported%20image%2020250721204338-6.png)     
![05MAR201313 34 D137ZKT 3 VAST D1122ZKT 3 DI DI DI ...](../../../../../../../../assets/images/Exported%20image%2020250721204339-7.png)  

# AF6_BV1_DO (DO7.1) verwijderd

# AF6_BV1_O_DI (DI3.3) en AF6_BV1_T_DI (DI3.4) verwijderd. Deze werden niet gebruikt in het programma

![1444 P DO 72AF6 12D PD073AF6 D135AF6 12D 12D D5MAR...](../../../../../../../../assets/images/Exported%20image%2020250721204342-8.png)     
**1/02/2013 9:28** **Uitbreiding zakkencontrole Rotoseal**  
**Beschrijving**

Band ZKT-4 geeft zakken af op band ZKT-3.  
Extra opstoppingscontrole ZKT-ZV5.  
Als er enkele seconden nadat er een zak is gepasseerd aan ZKT-ZV4, geen zak wordt gedetecteerd aan ZKT-ZV5, dan moet ZKT-4 stilvallen.
 
|   |   |   |
|---|---|---|
|DI3.11|ZKT_ZV5|Opstopping in schuif voor weegbrug controle|
 
Programma aangepast

![Exported image](../../../../../../../../assets/images/Exported%20image%2020250721204343-9.png)  
![Machine generated alternative text _1 _ngs contro ...](../../../../../../../../assets/images/Exported%20image%2020250721204343-10.png)  
![Machine generated alternative text INFO REMOTE UNI...](../../../../../../../../assets/images/Exported%20image%2020250721204344-11.png)