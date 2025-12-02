---
date created: 2012-07-04
tags: []
modified: 2025-07-22
---
# [[KR]] Programmeer fouten

**[[2012-07-04]] 11:21**
KR heeft LLZ1 geprogrammeerd. Er staan nergens commentaren bij de IO datatype.
## [[2012-07-04]] 13:58
De PLC van LLZ zit niet in de OPC server van CS1.
## [[2012-07-04]] 16:20 
  Booster_Donk.IO.BoosterDonk.ZP1.MotorValue zowel gekoppeld aan IO kaart als aan PB SS stroommeting
## [[2012-07-05]] 8:51 
[[KR]] heeft de Sentron PAC van MHZ geexporteerd van MHZ en geïmporteerd in Dessel.
Faceplate werkt niet.

## [[2012-07-09]] 14:34 
  Niet echt een programmeerfout, maar op scherm van D4 zijn de LT's van de bunkers niet aanpast aan de nieuwe programmatie. De operators zien dus geen silo standen.
## [[2012-07-19]] 11:46 
  Nick Swinnen komt vragen waarom de kleppen op scherm inkleuren terwijl de eindcontacten zijn afgekoppeld.
  [[KR]] weet het niet.
  2x klikken en je krijgt dit te zien.
  IO.OB_KL1.FB1.Value := IO.OB_KL1.Out1.Value;
  IO.OB_KL2.FB1.Value := IO.OB_KL2.Out1.Value;
  
  De Di's zijn wel gekoppeld
  Molen_4.IO.Units.Overblazen_64.OB_KL1.FB1
  Molen_4.IO.Units.Overblazen_64.OB_KL2.FB1
  Waarom hij dit heeft gedaan, geen flauw idee.
# [[2013-04-15]] 9:50 
  Een aantal zaken niet meer gemeld maar
  IO.C_8.Out1.Value := NOT Par.C_NOODWERKING AND DAT_From_S\_CAL_1\_B1.value7; (\* To Del KR 17-02-2012 \*)
  IO.C_8B.Out1.Value := NOT Par.C_NOODWERKING AND DAT_From_S\_CAL_1\_B1.value8; (\* To Del KR 17-02-2012 \*)
  IO.C_8C.Out1.Value := NOT Par.C_NOODWERKING AND DAT_From_S\_CAL_1\_B1.value9; (\* To Del KR 17-02-2012 \*)
  Was niet verwijderd maar al wel gebruikt in.
  ![image1](image1-4.png)
# [[2014-01-29]] 13:18 
  Pendelkleppen M3 hebben een parameterfout.
  ![image2](image2-1.png)
- #
# [[2014-01-31]] 8:35 
  Sentron PACs van M1 en M2 waren omgewisseld. Variabelen waren aan de verkeerde PAC gekoppeld
# [[2014-04-25]] 17:01
  Nieuwe regeling niet OK.
  ![image3](image3-1.png)
  Ook C_PIC31 niet
# [[2014-12-29]] 9:29 
  Ik heb Units in SibST02 aangepast. Deze waren fout
  ![image4](image4-1.png)
# [[2014-12-29]] 10:54 
  KR zet code in commentaar, waardoor andere zaken niet werken
  =\> Koppeling van Objective voor niveau standen zat in LLB3 en nu in ST01
  Ik kan alles gaan aanpassen.
# [[2015-01-09]] 14:25 
  KR had vorige week verlof.
  Er is wel wat binnengekomen van fouten
  Niveaumetingen zijn niet gekoppeld.
  
  Kleppen gaan dicht bij GMP. Meel naar BU67.
  
  PLC M3 heeft sinds 18/12 geen koppeling met Advant PLC
  
  Er is IO in plc M3, maar programma zit nog in Advant.
  
  Op het scherm van M2 staan de tagnamen van M1
  
  Meeltpt M1 M2 onduidelijk
  
  C_TT11 range fout en oude IO nog in advant
  
  Scherm Status Alarmen Calcineeroven niet in orde
  
  C_SVA212 en C_SVA202 zijn onbenoemd op scherm. IO is op twee plaatsen gedefineerd
  
  C_IO_S200_DT en C_IO_Voorverhitter
  
  LT_MS65 is nog in twee plc’s gedefineerd.
  
  MT_F2V en MT_F2M worden niet automatisch bij laden uit BU67
  
  Filter M1 M2 kleurt in, maar werkt niet.
# [[2015-01-12]] 8:26 
  Alweer mogelijk verkeerd materiaal in de bunker.
  ![image5](image5-1.png)
# [[2015-01-23]] 11:46 
  KR had een vergrendeling van M4_5 zomaar afgekoppeld. Ik heb dit dan maar opgelost.
# [[2015-01-26]] 11:59 
  Weliswaar een kleine fout. Maar het is er toch alweer één.
  ![image6](image6-1.png)
  In de onderste regel stond MT_F2_Start_Van_LLB en die var. werd werd al in de 1ste regel gebruikt.
# [[2015-02-13]] 7:40 
  In het storingenboek
  Installatie : SIB Molen 1
  
  Status : Nieuw
  
  Omschrijving : 
  Dirk Vangeel schreef op [[2015-02-12]] 20:44:09
  bij het starten sequentie van molen 1 kan je de hoofdmotor starten zonder dat de koeling van motor aan staat !! werkschakelaar.
  dit is ook voor de vet smering !! vergrendeling na kijken AUB.
  
  Link : 
  ![image7](image7.gif)
  
  =\> Het is goed getest volgens KR. Pfff Not
# [[2015-07-27]] 15:46 
  Aansturen van MT_F2 vanuit M4 en M5 werkte voor geen kanten (dit kon ook niet)
  Ik heb dan maar zelf alweer alles opgelost …. Alweer
  Vanaf nu doe ik het op mijn manier. Dwz correcte, duidelijke, eenvoudige en efficiente programma code
# [[2015-09-29]] 8:18 
  In het storingenboek alweer een fout opgelost te wijten aan KR.
  Hij heeft de niveaumetingen van BU103 -\> BU106 verplaatst gehad. Maar wat er achter hangt, dat past hij niet aan.
  Sequentie van TVAZ stopte niet meer bij HH bij deze bunkers.
# [[2016-02-01]] 09:27 
  KR heeft de MAF4_1 geprogrammeerd. Maar heeft de oude niet weggehaald. En deze staat nog op verschillende schermen.
- #