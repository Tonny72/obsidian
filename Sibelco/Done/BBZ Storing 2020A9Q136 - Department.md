---
title: BBZ Storing 2020/A9Q/136 - Department PA&I - Insta...
updated: [[2020-03-05]]T12:59:56.0000000+01:00
created: [[2020-02-24]]T07:49:24.0000000+01:00
---

| **Subject**     | **WOPP - Storing 2020/A9Q/136 - Department PA&I - Installatie Dessel Bagging Big Bag Sand - Reported by VANBRABANT, WIM : Nummering labelaar**                                        |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **From**        | [WOPP @ Sibelco](mailto:no-reply@sibelco.com)                                                                                                                                         |
| **To**          | Geert Staes; Nico Gerinckx; Joost Lievens; Tom Noels; Geert Staes; Nico Gerinckx; Joost Lievens; Tom Noels; Tonny Lemmens; Kurt Regout; Stef Valkiers; Mike Van de Put; Harry Stienen |
| **Sent**        | Monday, 24 February 2020 07:34                                                                                                                                                        |
| **Attachments** | [2020A9Q136.pdf](assets/pdf/2020A9Q136.pdf)                                                                                                                                                                |

**Melding** 2020/A9Q/136

**Aangemaakt door:** VANBRABANT, WIM
**Uit te voeren door:** PA&I afdeling

**Titel:** Nummering labelaar

**Installatie:** Dessel Bagging Big Bag Sand

**Tag:** - Nummering labelaar

**Omschrijving:**
Nog steeds problemen bij opstart nieuwe MO

**Oorzaak:**

- # [[2020-02-27]] 
  Afgelopen dagen veel tijd in nummering BBZ gestoken.
  
  Niet gemakkelijk want er wordt meer niet afgezakt dan wel.
  
  Wat mogelijk een oorzaak is, is de problemen ivm OPC
  
  Een test-watchdog gemaakt. Deze console app kopieert de out-value naar de in-value.
  In de plc wordt de out- en in-value
  
  ![image1](image1-83%201.png)
  
  De MaxTimeValue wordt gelogd
  
  Nakijken wat de MaxTimeValue wordt.
- # [[2020-03-02]] 
  Er wordt niet afgezakt
- # [[2020-03-03]] 
  In de log:
  Op een paar seconden tijd krijgt de buffersilo een ander zaknr.
  Waarschijnlijk zijn er verschillende aanvragen geweest
  
  timesourceconditionmessage
  
  [[2020-03-03]] 06:18:29.6670000BBZ_BufferSilo150
  
  [[2020-03-03]] 06:18:50.6670000BBZ_BufferSilo151
  
  [[2020-03-03]] 06:19:08.6670000BBZ_BufferSilo152
  
  [[2020-03-03]] 06:19:38.6670000BBZ_BufferSilo153
  
  [[2020-03-03]] 06:21:15.5670000BBZ_Vuller153
  
  [[2020-03-03]] 06:21:28.1670000BBZ_BufferSilo154
- # [[2020-03-03]] 
  Het lijkt erop dat MES 's morgens niet kan volgen. Extra events toegevoegd.
  
  Bekijk events met deze query
  
  SELECT \[time\]
  ,\[source\]
  ,\[condition\]
  ,\[message\]
  ,\[severity\]
  ,\[ackrequired\]
  FROM \[Linkworx_DES_LOG\].\[dbo\].\[ABBOPCAE\]
  WHERE (source LIKE 'BBZ_Rollenbaan%' OR source = 'BBZ_Vuller' OR source = 'BBZ_Buffersilo' or source like 'BBZ_ConfirmPallet%' or source like 'BBZ_RequestPallet%' or source = '') AND time \>= '2020/03/03 15:30:10'
  ORDER BY time
- # [[2020-03-05]] 
  Probleem getraceerd tot backup van BE-DES-SQL-100