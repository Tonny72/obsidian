---
title: Vragen over PG2
date created: 2010-11-19]]T10:01:40.0000000+01:00
---

Ik heb bij een aantal objecten van de standaard library een wrapper gemaakt zodat ik custom graphic elements kan bij maken en de faceplate kan aanpassen.
![image1](image1-554.png)
De SibMotorUni is een wrapper rond de MotorUniM.
Dit motor-object is een standaard motor volgens onze specifieke wensen. Wij maken bijvoorbeeld o.a. gebruik van directe logica voor het aansturen van de motor. In tegenstelling tot gebruik te maken van AutoCmd1 en AutoCmd0, hebben enkel een AutoCmd. AutoCmd=True start de motor.
De SibSimocode is een wrapper rond SibMotorUni.
De SibSimocode is een standaard motor die door profibus wordt aangestuurd. Deze moet een extra tab in de faceplate krijgen die de profibus signalen laat zien.
Hoe krijg ik dit op de meest efficiënte manier voor elkaar ?
Voor elk object heb ik de Faceplate elements en de Graphic elements gecopy/paste van het ge-embedde object.
Ik heb Aspect Object uitgezet omdat:
Stel dat SibMotorUni een alarm genereert. Bij het klikken op het alarm wordt de SibMotorUni faceplate getoond, terwijl eigenlijk de SibSimocode faceplate getoond moet worden.
Men zou de Alarm Owner van SibMotorUni kunnen uitzetten, maar deze moet aanstaan omdat SibMotorUni zelf als object geïnstantieerd kan worden.
![image2](image2-28.jpg)
Doordat het Aspect Object is uitgezet, kunnen er bij de Faceplate elements en de Graphic elements geen references naar het ge-embedde object gelegd worden.
Dit geeft de nodige problemen als de elements approved moeten worden.

Een volgend probleem:
Sommige objecten geven een lange popup.
![image3](image3-137.png)
Ik wil enkel de tagnaam (VS101a) laten zien. Waar kan je dit instellen?
