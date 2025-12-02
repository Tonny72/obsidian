# Maak custom UserControls voor gebruik in PanelBuilder
 
In Visual Studio maak een Project UserControl
 
# Koppeling Panel Builder en Custom Control
 
In de UserControl moet een method worden aangemaakt
 
Voeg Resources toe. De Dlls zitten in  
D:\OneDrive - Sibelco\Toepassingen\Panel Builder 800\Import DLLs
 
Voeg de nodige using regels toe
 
In Panel Builder script moet per tag een delegate worden toegevoegd van de UserControl
 
Gebruik hiervoor de setTag method van de UserControl.  
NIET VERGETEN de UnTag method bij unloading (=\> avoid memory leak).
 
# Debuggen

Om snel te kunnen debuggen moet project worden geImporteerd in Panel Builder Debug

- In Panel Builder klik op Project - Debug
- Visual Studio wordt geopend
- Voeg het SibWpfControlLibrary project in Visual Studio.￼D:\OneDrive - Sibelco\Toepassingen\Panel Builder 800\SibWpfControlLibrary
- Verwijder de SibelcoControlLibrary bij de references en voeg het Project toe.
 
# Import van Custom control

In Panel Builder Home tab  
Klik bij Objects Add Control

![Shape Colors Shape _Lagout x Objects TabMenu x L T...](../../../../../../../assets/images/Exported%20image%2020250721204224-0.png)  

Klik Browse
   

Neem de dll uit de debug directory van Visual Studio
 
De dll wordt ook automatische gekopieerd naar  
C:\Users\Public\Documents\ABB\Panel Builder 800 Version 6\Thirdparty
   

# 21/06/2019 8:16

Een tijdje niet meer met Panel builder gewerkt, en computer was ondertussen geherïnstalleerd.  
Project kon niet meer worden geladen met de custom library.
 
Eens testen of het niet kan met Command-woord en Status-woord.
 
# Status woord - Command woord

Omdat ik een multi-picture rechtsstreeks willen koppelen aan een tag, moet Status en Command bits worden gesplitst in twee woorden.
 
# Statuswoord

1 woord gebruiken voor Uni/Bi Motor en Valve
 
Status bits

- FB0 / FB1 / FB2 / Onbepaald (2bits)
- Alarm
- ManMode
- Interlock
- SafetyStop
 
6 bits -\> 64 combinaties, maar sommige combinaties kunnen niet voorkomen.
 
|   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|
|**Status**|**Bits**|**SafetyStop**  <br>(BIT 5)|**Interlock**  <br>(BIT 4)|**ManMode**  <br>(BIT 3)|**Alarm**  <br>(BIT 2)|**Feedback**  <br>Motor: FB2 / FB1  <br>Valve: FB1 / FB0  <br>(BIT 1 / BIT 0)|**MOTOR**|**VALVE**|
|0|0000 0000|0|0|0|0|00|![Machine generated alternative text](Exported%20image%2020250721204224-1.octet-stream)|![Machine generated alternative text](Exported%20image%2020250721204228-2.octet-stream)|
|1|0000 0001|0|0|0|0|01|![Machine generated alternative text](Exported%20image%2020250721204228-3.octet-stream)|![Machine generated alternative text](Exported%20image%2020250721204229-4.octet-stream)|
|2|0000 0010|0|0|0|0|10|![Exported image](Exported%20image%2020250721204229-5.octet-stream)|![Exported image](Exported%20image%2020250721204229-6.octet-stream)|
|3|0000 0011|0|0|0|0|11|NOT USED|NOT USED|
|4|0000 0100|0|0|0|1|00|![Exported image](Exported%20image%2020250721204230-7.octet-stream)|![Exported image](Exported%20image%2020250721204230-8.octet-stream)|
|5|0000 0101|0|0|0|1|01|![Exported image](Exported%20image%2020250721204234-9.octet-stream)|![Exported image](Exported%20image%2020250721204234-10.octet-stream)|
|6|0000 0110|0|0|0|1|10|![Exported image](Exported%20image%2020250721204235-11.octet-stream)|![Exported image](Exported%20image%2020250721204235-12.octet-stream)|
|7|0000 0111|0|0|0|1|11|NOT USED|NOT USED|
|8|0000 1000|0|0|1|0|00|![Exported image](Exported%20image%2020250721204235-13.octet-stream)|![Exported image](Exported%20image%2020250721204236-14.octet-stream)|
|9|0000 1001|0|0|1|0|01|![Exported image](Exported%20image%2020250721204236-15.octet-stream)|![Exported image](Exported%20image%2020250721204239-16.octet-stream)|
|10|0000 1010|0|0|1|0|10|![Exported image](Exported%20image%2020250721204240-17.octet-stream)|![Exported image](Exported%20image%2020250721204241-18.octet-stream)|
|11|0000 1011|0|0|1|0|11|NOT USED|NOT USED|
|12|0000 1100|0|0|1|1|00|![Exported image](Exported%20image%2020250721204241-19.octet-stream)|![MAN](Exported%20image%2020250721204242-20.octet-stream)|
|13|0000 1101|0|0|1|1|01|![Exported image](Exported%20image%2020250721204243-21.octet-stream)|![MAN](Exported%20image%2020250721204243-22.octet-stream)|
|14|0000 1110|0|0|1|1|10|![Exported image](Exported%20image%2020250721204247-23.octet-stream)|![MAN](Exported%20image%2020250721204247-24.octet-stream)|
|15|0000 1111|0|0|1|1|11|NOT USED|NOT USED|
|16|0001 0000|0|1|0|0|00|![](https://graph.microsoft.com/v1.0/users('tonnylemmens@outlook.com')/onenote/resources/0-aec2d1ce95d301843f1a668f4c91fce5!1-648FE635197C5860!805796/$value)|![Exported image](Exported%20image%2020250721204247-26.octet-stream)|
|17|0001 0001|0|1|0|0|01|NOT USED|![Exported image](Exported%20image%2020250721204248-27.octet-stream)|
|18|0001 0010|0|1|0|0|10|NOT USED|NOT USED|
|19|0001 0011|0|1|0|0|11|NOT USED|NOT USED|
|20|0001 0100|0|1|0|1|00|![Exported image](Exported%20image%2020250721204248-28.octet-stream)|![Exported image](Exported%20image%2020250721204249-29.octet-stream)|
|21|0001 0101|0|1|0|1|01|NOT USED|![Exported image](Exported%20image%2020250721204252-30.octet-stream)|
|22|0001 0110|0|1|0|1|10|NOT USED|NOT USED|
|23|0001 0111|0|1|0|1|11|NOT USED|NOT USED|
|24|0001 1000|0|1|1|0|00|![Exported image](Exported%20image%2020250721204252-31.octet-stream)|![Exported image](Exported%20image%2020250721204253-32.octet-stream)|
|25|0001 1001|0|1|1|0|01|NOT USED|![Exported image](Exported%20image%2020250721204253-33.octet-stream)|
|26|0001 1010|0|1|1|0|10|NOT USED|NOT USED|
|27|0001 1011|0|1|1|0|11|NOT USED|NOT USED|
|28|0001 1100|0|1|1|1|00|![Exported image](Exported%20image%2020250721204254-34.octet-stream)|![MAN](Exported%20image%2020250721204254-35.octet-stream)|
|29|0001 1101|0|1|1|1|01|NOT USED|![MAN](Exported%20image%2020250721204254-36.octet-stream)|
|30|0001 1110|0|1|1|1|10|NOT USED|NOT USED|
|31|0001 1111|0|1|1|1|11|NOT USED|NOT USED|
|32  <br>…  <br>63|0010 0000  <br>…  <br>0011 1111|1  <br>…  <br>1|0  <br>…  <br>1|0  <br>…  <br>1|0  <br>...  <br>1|00  <br>…  <br>11|![Exported image](Exported%20image%2020250721204258-37.octet-stream)||
||||||||||