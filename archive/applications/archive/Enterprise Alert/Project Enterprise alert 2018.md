---
date created: 2018-07-24
tags:
  - enterprise_alert
modified: 2025-08-30
---

- # TODO
- Waterpeilen schans
  
  Project [[Archive/applications/archive/Enterprise Alert/Enterprise Alert]] m2m
  C003201 35000€
- # [handleidingen](https://sibelco-my.sharepoint.com/personal/tonny_lemmens_sibelco_com/_layouts/15/onedrive.aspx?id=%2fpersonal%2ftonny_lemmens_sibelco_com%2fDocuments%2fLeveranciers%2fm2mcom+(derdack)&FolderCTID=0x01200085C23FB315EB744F93C218912CF4BBB4)
# [[2018-07-24]] 
  besteld
# [[2018-09-13]] 
  Nico heeft summiere opzet gedaan
# [[2018-09-14]] 
  Al wat gespeeld SMS van Safetel OK.
  Ook OPC UA werkt.
# [2018-09-18](2018-09-18.md) 
  Volgens oude prijslijst:
  Tweeweg user: 300€
  Subscription user: 30€
  Aan Nico gevraagd voor OPC handleiding
# [[2018-09-25]] 
  Mail naar Nico gestuurd ivm OPC UA binaire tags
  en naar status voice koppeling gevraagd.
# [[2018-09-25]] 15:33
  Ook komma getallen worden niet aanvaard.
  ![image1](image1-605.png)
# [[2018-09-28]]
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
# [[2018-11-13]] 
  Voice koppeling moet nog gebeuren. Zonet in meeting met Jef afgesproken dat Jef dit gaat regelen.
# [[2019-01-30]] 
  Ondertussen heeft Nico een PDF gestuurd wat nodig is voor voice support
  [VoIP config.pdf](VoIP_config.pdf)
  Naar Jef gemaild om een extra VOIP / SIP account te maken
# [[2019-02-20]] 
  Meeting gehad met Jef
  Hij gaat er werk van makken
# [[2019-02-26]] 
  Dinsdag 5 maart Voice koppeling
  Nico Deconinck \<<nico@m2mcom.be>\> ; Joeri Liekens \<<Joeri.Liekens@GTT.net>\>
  **Cc:** Rik De Backer \<<Rik.DeBacker@gtt.net>\>
  
  Hallo Nico,
  
  In verband met de voice koppeling. Ik kan al enkele parameters meegeven.
  SBC: 10.32.23.9
  Protocol: UDP
  Port: 5060
  
  De manual gaf ook nog een aantal configuratie details mee:
- Zowel een configuratie van een SIP trunk als een SIP endpoint zijn mogelijk  
  Ik zou daarom willen proberen om een SIP trunk op te zetten ipv een SIP endpoint
- SIPS en SRTP zijn niet ondersteund
  
  Kan jij het IP van je AE nog even bezorgen? Dan kan ik ook verder met de configuratie op de SBC.