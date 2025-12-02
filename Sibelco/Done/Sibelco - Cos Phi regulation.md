---
title: Sibelco - Cos Phi regulation
updated: [[2022-01-21]]T13:45:00.0000000+01:00
created: [[2018-04-24]]T12:51:42.0000000+02:00
---

| **Subject** | **RE: Sibelco - Cos Phi regulation**                               |
|-------------|--------------------------------------------------------------------|
| **From**    | [Vansantvoort, Olivier](mailto:Olivier.Vansantvoort@edfluminus.be) |
| **To**      | Tonny Lemmens; Vloebergs, Roel                                     |
| **Cc**      | Verwimp, Grégory; Simon, Benoît; Harry Stienen                     |
| **Sent**    | maandag 16 april 2018 17:22                                        |

Hi Tonny,
Thanks for quick feedback.
So let’s go with the Modbus TCP communication.

When you will be ready with the ABB , I propose we come on site and tests together (with specialist) the Modbus TCP between ABB and a PLC S7-1200 configured in mode test for the communication.
It’s maybe better to proceed like that for the fine tuning ? Unfortunately I believe no more in the “plud and play” mode. J

Do you agree ?

**@Roel,**
It will be necessary to foreseen with ATS two new module MOXA Eth/FO model **EDS-308-SS-SC-T** for the junction optical fiber.
\+ optical patch cord.

Thanks in advance
Kr,
Olivier

![image1](image1-4%201.jpg)
**Olivier VANSANTVOORT**

**Guidance & Control**

**I&C Hydrauliques - Transmission Data**

**Generation**

Quai du Halage, 1

4400 Flémalle

Belgium

P  +32 (0)4 330 30 26

F  +32 (0)4 337 29 42

M  +32 (0)496 58 24 17

<olivier.vansantvoort@edfluminus.be>

[www.edfluminus.be](https://emea01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.edfluminus.be%2F&data=02%7C01%7CTonny.Lemmens%40sibelco.com%7C02316f8002014ac592d508d5a3addfe7%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C1%7C636594889577110113&sdata=6HEo9phitEhuv7dVuWd8Pt82KojzmThAVRQTqYyDzQQ%3D&reserved=0)

[www.luminus.be](https://emea01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.luminus.be&data=02%7C01%7CTonny.Lemmens%40sibelco.com%7C02316f8002014ac592d508d5a3addfe7%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C1%7C636594889577110113&sdata=6UDHIXTPJBSbGj4yVqMla6rX4AngISMhX7n9OX1GrUo%3D&reserved=0)

**De:** Tonny Lemmens \[[mailto:Tonny.Lemmens@sibelco.com](mailto:Tonny.Lemmens@sibelco.com)\]
**Envoyé:** jeudi 12 avril 2018 11:18
**À:** Vansantvoort, Olivier \<Olivier.Vansantvoort@edfluminus.be\>
**Cc:** Verwimp, Grégory \<gregory.verwimp@edfluminus.be\>; Vloebergs, Roel \<Roel.Vloebergs@edfluminus.be\>; Simon, Benoît \<Benoit.Simon@edfluminus.be\>; Harry Stienen \<Harry.Stienen@sibelco.com\>
**Objet:** RE: Sibelco - Cos Phi regulation

Hi Olivier,

About Profibus / Modbus I have the same problem but the opposite.

If we want to communicate with Modbus TCP then we need an additional Modbus TCP Hardware card for the ABB PLC.
I have no experience with Modbus, but I think we can configure things out to get it to work.

In my opinion it easier to use Modbus TCP because then we don’t need a profibus DP/DP coupler.

Best regards

Tonny Lemmens
Automation engineer
Sibelco Benelux
De Zate 1•BE-2480 Dessel

mob. +32494500 437
tel. +32 14 83 72 83
[tonny.lemmens@sibelco.com](mailto:otonny.lemmens@sibelco.com)
[www.sibelco.eu](https://emea01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.sibelco.eu%2F&data=02%7C01%7CTonny.Lemmens%40sibelco.com%7C02316f8002014ac592d508d5a3addfe7%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C1%7C636594889577110113&sdata=agQ8%2FINUOmhOWtk4QD3Nzg7sUZ0JHHIEM5JBwi0njYM%3D&reserved=0)
![image2](image2-28%201.png)

SCR-SIBELCO NV - Maatschappelijke zetel - Siège social - Registered Office: Plantin en Moretuslei 1A - BE-2018 Antwerpen
RPR Antwerpen - BTW BE 0 404 679 941 - ING IBAN BE38 3200 0042 7072

**From:** Vansantvoort, Olivier \[[mailto:Olivier.Vansantvoort@edfluminus.be](mailto:Olivier.Vansantvoort@edfluminus.be)\]
**Sent:** woensdag 11 april 2018 16:10
**To:** Tonny Lemmens \<<Tonny.Lemmens@sibelco.com>\>
**Cc:** Verwimp, Grégory \<<gregory.verwimp@edfluminus.be>\>; Vloebergs, Roel \<<Roel.Vloebergs@edfluminus.be>\>; Simon, Benoît \<<Benoit.Simon@edfluminus.be>\>
**Subject:** Sibelco - Cos Phi regulation

Hello Tonny,
Concerning this regulation I just heard from Roel that the best way should be to create the connection to your ABB PLC.
As all information are present in this device, I would like to see which communication is available on your ABB and what could be the effort to realize the communication dependent of the protocol used.
****
**Profibus or ModBus TCP**:
From my point of view, as we already use ModBus TCP for the telecontrol Turbine and substation… sure It’s more easier for us to use this mode.
But Profibus is also possible with additional Profibus HW card.

For both It will be necessary to adapt the communication over FO
If *Modbus TCP* , we can use converter ETH/FO with ***MOXA EDS 30x***,40x…  NB: Good experience . often use on EDFLuminus
If *Profibus* , We can use converter Profibus/FO with ***MOXA ICF-1180I***   NB: no experience yet with this kind of device

Please can you also give me your point of view concerning the possible protocol to use?

Thanks in advance
Kr,
Olivier

![image1](image1-4%201.jpg)
**Olivier VANSANTVOORT**

**Guidance & Control**

**I&C Hydrauliques - Transmission Data**

**Generation**

Quai du Halage, 1

4400 Flémalle

Belgium

P  +32 (0)4 330 30 26

F  +32 (0)4 337 29 42

M  +32 (0)496 58 24 17

<olivier.vansantvoort@edfluminus.be>

[www.edfluminus.be](https://emea01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.edfluminus.be%2F&data=02%7C01%7Ctonny.lemmens%40sibelco.com%7C0a1f6f790f614c6b00ce08d59fb5fb38%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C636590526342389908&sdata=fNDyzCE5HtY1phMOrX37KaKUO4WHRZ8JvytDbOTi9cE%3D&reserved=0)

[www.luminus.be](https://emea01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.luminus.be&data=02%7C01%7Ctonny.lemmens%40sibelco.com%7C0a1f6f790f614c6b00ce08d59fb5fb38%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C636590526342389908&sdata=QP98e5tcRk0GrPy87i62Agji7TXyGTJNWacRymA5y7k%3D&reserved=0)

**De:** Vloebergs, Roel
**Envoyé:** mercredi 11 avril 2018 10:02
**À:** Vansantvoort, Olivier \<<Olivier.Vansantvoort@edfluminus.be>\>
**Objet:** contact Sibelco

Tonny Lemmens
Automation engineer
Sibelco Benelux
De Zate 1•BE-2480 Dessel

mob. +32494500 437
tel. +32 14 83 72 83
[tonny.lemmens@sibelco.com](mailto:otonny.lemmens@sibelco.com)
[www.sibelco.eu](https://emea01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.sibelco.eu%2F&data=02%7C01%7Ctonny.lemmens%40sibelco.com%7C0a1f6f790f614c6b00ce08d59fb5fb38%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C636590526342389908&sdata=GYZdGyjpvuFvVFptLAZbcMZeeJGMuv5ETRpCGXpqbtU%3D&reserved=0)

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th>![image3](../../resources/image3-1.jpg)</th>
<th><p>Met vriendelijke groeten</p>
<p>Kind Regards</p>
<p></p>
<p><strong>Roel VLOEBERGS</strong></p>
<p><strong>Project Manager</strong></p>
<p><strong>Project Team 3</strong></p>
<p><strong>PRODUCTION</strong></p>
<p></p>
<p>HAM 68</p>
<p>9000 Gent</p>
<p>Belgium</p>
<p>P  +32 (0)9 269 50 41</p>
<p>F  +32 (0)9 269 50 12</p>
<p>M  +32 (0)472 64 51 64</p>
<p></p>
<p><a href="mailto:roel.vloebergs@edfluminus.be">roel.vloebergs@edfluminus.be</a></p>
<p><a href="https://emea01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.edfluminus.be%2F&amp;data=02%7C01%7Ctonny.lemmens%40sibelco.com%7C0a1f6f790f614c6b00ce08d59fb5fb38%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C636590526342389908&amp;sdata=fNDyzCE5HtY1phMOrX37KaKUO4WHRZ8JvytDbOTi9cE%3D&amp;reserved=0">www.edfluminus.be</a></p>
<p><a href="https://emea01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.luminus.be%2F&amp;data=02%7C01%7Ctonny.lemmens%40sibelco.com%7C0a1f6f790f614c6b00ce08d59fb5fb38%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C636590526342389908&amp;sdata=aNv3B61X9AfZI0DHpvBRQkRsJINfbOLdLLjI04xS9yU%3D&amp;reserved=0">www.luminus.be</a></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><strong></strong></td>
</tr>
</tbody>
</table>

- # [[../../journals/older/2018/2018-04-24]] 
  Modbus TCP kaart besteld