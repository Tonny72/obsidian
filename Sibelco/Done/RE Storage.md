---
title: 'RE: Storage'
updated: [[2020-10-20]]T14:36:04.0000000+02:00
created: [[2020-10-20]]T14:36:04.0000000+02:00
---

| **Subject** | **RE: Storage**                                               |
|-------------|---------------------------------------------------------------|
| **From**    | [Stijn Vandenbroucke](mailto:stijn.vandenbroucke@linkworx.eu) |
| **To**      | Tonny Lemmens                                                 |
| **Cc**      | Jochem Janssen                                                |
| **Sent**    | maandag 12 oktober 2020 10:23                                 |

Ter info: er zat een locatie dubbel in, waardoor de storage module eigenlijk niet deftig liep (UA structuur was niet beschikbaar) ; P45MS01 zit er nu maar 1x meer in.

Voor ZS01:
Het lijkt erop dat ZS01 niet gebruikt wordt, althans niet volgens de M3 stock.

![image1](image1-93.png)

SELECT wh_loc.code as location_code, item.code as item_code, item.description as item_description, SUM(inv.stockvalue) as 'stock'
FROM LNKWRX_INVENTORY inv with(nolock)
 inner join LNKWRX_WAREHOUSELOCATION wh_loc with(nolock) on wh_loc.rid = inv.locationrid
 inner join LNKWRX_ITEM item with(nolock) on item.rid = inv.itemrid
where wh_loc.code like 'P45ZS%'
group by wh_loc.code, item.code, item.description
order by wh_loc.code

**Van:** Tonny Lemmens \<<Tonny.Lemmens@sibelco.com>\>
**Verzonden:** donderdag 8 oktober 2020 9:10
**Aan:** Stijn Vandenbroucke \<stijn.vandenbroucke@linkworx.eu\>
**CC:** Jochem Janssen \<Jochem.Janssen@sibelco.com\>
**Onderwerp:** Storage

Stijn,

Ik heb een probleem gehad met de plc van de Silo’s
Hier zit de natzand storage gekoppeld. Deze had ik al op de nieuwe storage gezet.

Ik heb gemerkt dat er nog wat fouten in de config zit (ZS vs MS in de silonaam).

Maar de P45ZS01 zou moeten goed staan, maar toch komen er geen waarden in.
![image2](image2-54.png)

Kan jij eens nazien wat er fout is?

**Tonny Lemmens**
Automation Engineer

![image3](image3-31.png)

De Zate 1
BE-2480 Dessel
Belgium
**Tel** +32 (0) 14 837 283
**Mob** +32 (0) 494500 437
[www.sibelco.com](https://eur01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.sibelco.com%2F&data=02%7C01%7CTonny.Lemmens%40sibelco.com%7Cf04d8b4dd8454292d6b108d86e882d69%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C637380878458650980&sdata=lBBmC2C2FP9vn4FNRbmjXSSzYLZ7UW07Lh14qVfNwOw%3D&reserved=0)

**Maatschappelijke zetel - Siège social - Registered Office: Plantin en Moretuslei 1A - BE-2018 Antwerpen RPR Antwerpen - BTW BE 0 404 679 941 - ING IBAN BE38 3200 0042 7072**

This e-mail (including any attachments) is confidential and may contain proprietary , commercially sensitive or legally privileged information. You must not use, disclose, or act on the email unless you are the intended direct recipient. If you receive this email in error, please immediately notify the sender and delete it from your system. No confidentiality or privilege is waived or lost by any error in transmission. Any views expressed in this email are those of the individual sender, except where the sender has authority to expressly state them to be the views of SCR-Sibelco NV and/or any of the affiliates of Sibelco ( together “ the Sibelco Group”).
