# TODO

- Waterpeilen schans
 
Project Enterprise alert m2m  
C003201 35000€
 
# [handleidingen](https://sibelco-my.sharepoint.com/personal/tonny_lemmens_sibelco_com/_layouts/15/onedrive.aspx?id=%2fpersonal%2ftonny_lemmens_sibelco_com%2fDocuments%2fLeveranciers%2fm2mcom+\(derdack\)&FolderCTID=0x01200085C23FB315EB744F93C218912CF4BBB4)
 
# 24/07/2018
besteld
 
# 13/09/2018

Nico heeft summiere opzet gedaan
 
# 14/09/2018

Al wat gespeeld SMS van Safetel OK.  
Ook OPC UA werkt.
 
# 18/09/2018
Volgens oude prijslijst:  
Tweeweg user: 300€  
Subscription user: 30€  
Aan Nico gevraagd voor OPC handleiding
 
# 25/09/2018
Mail naar Nico gestuurd ivm OPC UA binaire tags  
en naar status voice koppeling gevraagd.
   

# 25/09/2018 15:33

Ook komma getallen worden niet aanvaard.

![Alert Center 
Insights 
Incoming Events 
Alert Policies 
Raise Alert 
DES C3_LT300 High Prio 
General Conditions Alerting Message Actions 
Add Condition O Link Conditions AND (D Link Conditions OR 
C3 LT300 Number greater than 60 
C3 LT300 Number less thon -I 
Duplicate Suppression Activated (Define: Exceptions) 
Wait for recovery / delay alert for 1m 
o 
Wait for multi le event occurrences 
Ownership 
Unlink X Delete Conditions ](https://graph.microsoft.com/v1.0/users('tonnylemmens@outlook.com')/onenote/resources/0-4db0b8c1df0441d3856cfdb964a5f31f!1-648FE635197C5860!805721/$value)  

# 28/09/2018

**From:** Nico Deconinck \<nico@m2mcom.be\>  
**Sent:** woensdag 26 september 2018 9:17  
**To:** Tonny Lemmens \<Tonny.Lemmens@sibelco.com\>  
**Subject:** RE: OPC koppeling en Voice  
   
Hallo Tonny,  
   
Antwoord van Derdack dat ik maandag heb ontvangen:  
   
“  
It might be that absolute deadband for Boolean values is not supported by the server:  
[http://www.opclabs.com/forum/ua-reading-writing-subscriptions/1415-badfilternotallowed-with-reactive-subscription-to-a-boolean](https://emea01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.opclabs.com%2Fforum%2Fua-reading-writing-subscriptions%2F1415-badfilternotallowed-with-reactive-subscription-to-a-boolean&data=02%7C01%7CTonny.Lemmens%40sibelco.com%7C3887d4a2653c4476e76408d623800c48%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C636735430241110858&sdata=Pi7m34mWx9pFyDFJmuHSxGyhrRbmNECgV%2BPv4Vpz4Ac%3D&reserved=0)  
   
I suggest to double-check if and how this is supported with support of the vendor (or ducumentation) of the OPC server. From our side, right now, we only support absolute deadband but not percentage deadband.  
   
I hope this helps you.  
“  
Voor je opmerking hieronder hoor ik nog even.  
   
Voor voice neem ik morgen contact op.  
   
Met vriendelijke groeten,  
   
Nico Deconinck
   

# 13/11/2018

Voice koppeling moet nog gebeuren. Zonet in meeting met Jef afgesproken dat Jef dit gaat regelen.
 
# 30/01/2019

Ondertussen heeft Nico een PDF gestuurd wat nodig is voor voice support

![[undefined]]
   

   
Kan jij het IP van je AE nog even bezorgen? Dan kan ik ook verder met de configuratie op de SBC.

- Zowel een configuratie van een SIP trunk als een SIP endpoint zijn mogelijk￼Ik zou daarom willen proberen om een SIP trunk op te zetten ipv een SIP endpoint
- SIPS en SRTP zijn niet ondersteund

Hallo Nico,  
   
In verband met de voice koppeling. Ik kan al enkele parameters meegeven.  
SBC: 10.32.23.9  
Protocol: UDP  
Port: 5060  
   
De manual gaf ook nog een aantal configuratie details mee:
 
Dinsdag 5 maart Voice koppeling  
Nico Deconinck \<[nico@m2mcom.be](mailto:nico@m2mcom.be)\> ; Joeri Liekens \<[Joeri.Liekens@GTT.net](mailto:Joeri.Liekens@GTT.net)\>  
**Cc:** Rik De Backer \<[Rik.DeBacker@gtt.net](mailto:Rik.DeBacker@gtt.net)\>

# 26/02/2019
 
Meeting gehad met Jef  
Hij gaat er werk van makken

# 20/02/2019
 
Naar Jef gemaild om een extra VOIP / SIP account te maken