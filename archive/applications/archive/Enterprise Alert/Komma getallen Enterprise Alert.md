---
date created: 2019-02-26
tags:
  - enterprise_alert
modified: 2025-08-30
---

| **Subject** | **RE: overzicht toepassingen**          |
|-------------|-----------------------------------------|
| **From**    | [Nico Deconinck](mailto:nico@m2mcom.be) |
| **To**      | Tonny Lemmens                           |
| **Cc**      | Kristof Loos                            |
| **Sent**    | Tuesday, 23 October 2018 14:36          |

Hallo Tonny,

Antwoord van Derdack:

“talking about time frames, this could be fixed in a patch which should come out sometimes in December. Will this work for you and your costumer?

You can find the value of the policy condition in the table Policies – Column Condition
There you have to replace the -1 value in the XSL with the value you want to have for the condition. Then restart the EA kernel. After that never change and save that value via the EA portal again as it will overwrite the value with -1 again.

\<?xml version="1.0"?\>
\<xsl:stylesheet xmlns:xsl="[http://www.w3.org/1999/XSL/Transform](https://emea01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.w3.org%2F1999%2FXSL%2FTransform&data=02%7C01%7CTonny.Lemmens%40sibelco.com%7C848e598a4a1c4f6fcb4d08d638e436a6%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C636758950192402118&sdata=YMEO87Ewzmwy4Voy2RsBNZ4AWKU6BqU5W3WePPhQhW8%3D&reserved=0)" version="1.0"\>
 \<xsl:output method="text"/\>
 \<xsl:variable name="apos"\>
 \<xsl:text disable-output-escaping="yes"\>'\</xsl:text\>
 \</xsl:variable\>
 \<xsl:template match="/"\>
 \<xsl:choose\>
 \<xsl:when test="(string(mm_message/mm_header/@type)='event') and (contains(string(mm_message/mm_header/@service_from),'/Internal File Interface Manager')) and (number(mm_message/mm_event/param\[@name=&quot;EventText&quot;\]/value)&lt;0.4)"\>Y\</xsl:when\>
 \<xsl:otherwise\>N\</xsl:otherwise\>
 \</xsl:choose\>
 \</xsl:template\>
\</xsl:stylesheet\>
“

Met vriendelijke groeten,

Nico Deconinck

Tel(+32 3 216 71 50
Gsm(+32 486 56 42 11

a[www.m2mcom.be](https://emea01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.m2mcom.be%2F&data=02%7C01%7CTonny.Lemmens%40sibelco.com%7C848e598a4a1c4f6fcb4d08d638e436a6%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C636758950192402118&sdata=lY3hGT1pU6Lsw8v%2BZHPsiJVbEAyo%2BOBTidH%2BVzaxdb8%3D&reserved=0)

**From:** Tonny Lemmens \<Tonny.Lemmens@sibelco.com\>
**Sent:** Tuesday, 23 October 2018 11:20
**To:** Nico Deconinck \<nico@m2mcom.be\>
**Cc:** Kristof Loos \<Kristof.Loos@sibelco.com\>
**Subject:** RE: overzicht toepassingen

Nico,

Heb je een idee wanneer er een volgende release komt.

Voor mij geen probleem om rechtstreeks in de DB te editen, zoals ik maar weet in welke tabel de waarden staan.

Mvg

Tonny

**From:** Nico Deconinck \<<nico@m2mcom.be>\>
**Sent:** maandag 22 oktober 2018 14:27
**To:** Tonny Lemmens \<<Tonny.Lemmens@sibelco.com>\>
**Cc:** Kristof Loos \<<Kristof.Loos@sibelco.com>\>
**Subject:** RE: overzicht toepassingen

Tonny,

Zonet al antwoord gekregen van Derdack. Kommagetallen worden voor kleiner en groter dan niet gesupporteerd vanuit de webinterface. Je kan deze wel blijkbaar direct ingeven in de database maar dit lijkt me niet de meest elegante oplossing.

Ze gaan dit aanpassen in één van de volgende releases/patches.

“
The DEV team was investigating a bit deeper and found that, if they put the values directly in the database, it is working. The problem is that it is not supported via the GUI entries. BUT they told me that it could be fixed and will be included in one of the next releases.

“

Met vriendelijke groeten,

Nico Deconinck

Tel(+32 3 216 71 50
Gsm(+32 486 56 42 11

a[www.m2mcom.be](https://emea01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.m2mcom.be%2F&data=02%7C01%7CTonny.Lemmens%40sibelco.com%7C848e598a4a1c4f6fcb4d08d638e436a6%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C636758950192412128&sdata=r3wHo1vdYdbBgC3CW7QZ4erJFq%2BZ82HpimJhj5vkm14%3D&reserved=0)

This e-mail (including any attachments) is confidential and may contain proprietary , commercially sensitive or legally privileged information. You must not use, disclose, or act on the email unless you are the intended direct recipient. If you receive this email in error, please immediately notify the sender and delete it from your system. No confidentiality or privilege is waived or lost by any error in transmission. Any views expressed in this email are those of the individual sender, except where the sender has authority to expressly state them to be the views of SCR-Sibelco NV and/or any of the affiliates of Sibelco ( together “ the Sibelco Group”).
