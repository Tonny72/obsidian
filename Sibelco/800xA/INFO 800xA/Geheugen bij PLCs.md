---
date created: 2013-03-25
date modified: 2025-07-22
---
[[2013-04-11]]: Er is een case aangemaakt bij ABB
 
# 3/04/2013 9:12

Geen antwoord ontvangen  
Nogmaals mail gestuurd
 
Hennie,  
Engelbert,
 
Hebben jullie nog iets vinden waarom de Compiler statistics in Control Builder maar enkele van de applicaties laat zien.  
Ik heb de indruk dat nieuw aangemaakte applicatie wel goed getoond worden. Misschien heeft het iets met de upgrade te maken.

![Machine generated alternative text collection data...](../../../../../../../assets/images/Exported%20image%2020250721203829-0.png)   
# 25/03/2013 14:01

Mail naar ABB gestuurd waarom de Compiler Statistics maar 5 apps laat zien.
 
# 25/03/2013 12:23

Naar aanleiding van het geheugen probleem bij de controller van M3, wat opzoekingen gedaan.
 
=\> Zie [Conclusie](Sibelco/800xA/INFO%20800xA/Geheugen%20bij%20PLCs.md)
 
![[../../../assets/pdf/Compiler Statistics.pdf]]

![[../../../assets/pdf/Task Execution en Offset.pdf]]

![[../../../assets/pdf/Memory Usage per Component.pdf]]
   

Prijs PM861 = 5519€  
Prijs PM864 = 9546€
 
Of eventueel zelf een bibliotheek te maken die veel efficienter is. Enfin met minder alarm functie blocks. HH, H, L, LL  
Een AlarmCond FB neemt 1.9kB in beslag. En zo zitten er 6 in een SignalRealIn =\> 11.4kB
 
De SibMotorUni en de SibRealIn zijn objecten gebouwd op de standaard bibliotheek en deze gebruiken vrij veel geheugen.  
Standaard best PM864 controller kopen. Deze heeft 3x zoveel geheugen als een PM861.

# Conclusie
   
![SystemDiagnostics MainFacepIate System Diagnostics...](../../../../../../../assets/images/Exported%20image%2020250721203843-14.png)

   
Molen5

![Exported image](../../../../../../../assets/images/Exported%20image%2020250721203842-13.jpeg)

Molen6 7 (PM861)

![Exported image](../../../../../../../assets/images/Exported%20image%2020250721203842-12.jpeg)

Silo’s (PM861)

![Exported image](../../../../../../../assets/images/Exported%20image%2020250721203838-11.jpeg)

Droger3 (PM861)

![Machine generated alternative text](../../../../../../../assets/images/Exported%20image%2020250721203838-10.jpeg)

Hydro (PM866)

![Machine generated alternative text](../../../../../../../assets/images/Exported%20image%2020250721203837-9.jpeg)

Molen3 (PM861)
 ![Machine generated alternative text](../../../../../../../assets/images/Exported%20image%2020250721203837-8.png)  
![Machine generated alternative text](../../../../../../../assets/images/Exported%20image%2020250721203836-7.png)  

ONLINE:
   
![Machine generated alternative text](../../../../../../../assets/images/Exported%20image%2020250721203836-6.png)  
![Machine generated alternative text](../../../../../../../assets/images/Exported%20image%2020250721203835-5.png)  

Controller memory gebruik:
   
![Machine generated alternative text](../../../../../../../assets/images/Exported%20image%2020250721203831-4.png)   ![Machine generated alternative text](../../../../../../../assets/images/Exported%20image%2020250721203831-3.png)   ![Compiler Statistics Select nput data Type statisti...](../../../../../../../assets/images/Exported%20image%2020250721203830-2.png)     
![Machine generated alternative text](../../../../../../../assets/images/Exported%20image%2020250721203830-1.png)   
Applicatie memory gebruik: