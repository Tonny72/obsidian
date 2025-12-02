---
created: [[2020-06-22]]T12:15:44.0000000+02:00
---

| **Subject**     | **RE: OPC interface to control the retraction of the kiln camera** |
|-----------------|--------------------------------------------------------------------|
| **From**        | [Antoine Cotinat](mailto:antoine.cotinat@hgh.fr)                   |
| **To**          | Jean-Francois Boissou; Tonny Lemmens; Harry Stienen                |
| **Cc**          | Geert Staes; Romain Guider                                         |
| **Sent**        | woensdag 17 juni 2020 15:28                                        |
| **Attachments** | [HGH Pyroscan - OPC Configuration EN.pdf](HGH_Pyroscan_-_OPC_Configuration_EN.pdf)                    |

Hello,

Following your conversations with Jean-François, here are some details on the OPC interface with [[Pyroscan]].

First of all, you will find enclosed an extract from the [[Pyroscan]] software manual, describing its operation as an OPC DA client. In particular, you will find the list of variables and their respective types.

Concerning the emergency extraction by OPC, a new link will be possible to a boolean type variable. The server-side variable will be read at a frequency in the order of 1Hz. When this boolean is read True (1), the PYROSCAN software will command the immediate extraction of the camera. The software operator will then be informed of this OPC-controlled extraction by an on-screen message.
As long as this variable is read at True :
\- It will be impossible for the operator to request a camera insertion via PYROSCAN (a message will indicate that this is impossible).
\- If the camera is inserted by pressing the Insert button on the control cabinet next to the camera, the software will immediately command a new extraction of the camera.
As soon as the boolean is set to False, it will be possible to insert/extract the camera normally.

Finally, it is important to note that this functionality requires that the connection between the software and the PLC is active.

Does this OPC camera extraction command, as described above, meet your needs ?

Regards,

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Antoine COTINAT</strong></p>
<p>Software Project Engineer</p>
<p><strong>HGH Systèmes Infrarouges</strong></p>
<p>10 rue Maryse Bastié</p>
<p>91430 Igny – France</p>
<p>T: + 33 1 69 35 36 47</p></th>
<th><blockquote>
<p>![image1](../../resources/image1-106.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><a href="mailto:antoine.cotinat@hgh.fr">antoine.cotinat@hgh.fr</a> | <a href="https://eur01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.hgh.fr%2F&amp;data=02%7C01%7CTonny.Lemmens%40sibelco.com%7C47114148617a48e9745008d812c256cf%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C637279973340244874&amp;sdata=Hr7kFDWHD9WTpbm9DZJzqcZSDxJolzHP6dbZDTZOyf8%3D&amp;reserved=0">www.hgh.fr</a></td>
</tr>
</tbody>
</table>
*<u></u>*
*<u></u>*
*HGH Systèmes Infrarouges harmonise son nom de marque dans le monde entier. [En savoir plus](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.hgh.fr%2FActualites%2FToute-l-actu%2FHGH-Systemes-Infrarouges-accelere-son-internationalisation-en-harmonisant-son-nom-de-marque&data=02%7C01%7CTonny.Lemmens%40sibelco.com%7C47114148617a48e9745008d812c256cf%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C637279973340264862&sdata=0zT%2FApM7vx0wFBhz33Ww09L5FRlfyTFZGUNSvKm49R0%3D&reserved=0)*
*HGH Infrared Systems will operate under the new unified HGH brand, strenghtening the company’s development worldwide, while giving even more value to our customers. [Read more](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.hgh-infrared.com%2FNews%2FWhat-s-new%2FHGH-expands-its-brand-name-Worldwide&data=02%7C01%7CTonny.Lemmens%40sibelco.com%7C47114148617a48e9745008d812c256cf%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C637279973340274856&sdata=d6upL7SwI1aohjTXFlEeJtavcqIRRtXDpRAYgiNyvBA%3D&reserved=0)*
**
*<u>Note</u>: Ce message et toutes les pièces jointes (ci-après le "message") sont confidentiels et établis à l'intention exclusive de ses destinataires. Toute utilisation ou diffusion non autorisée est interdite. Tout message électronique est susceptible d'altération. La société décline toute responsabilité au titre de ce message s'il a été altéré, déformé ou falsifié.*
**
*<u>Notice</u>: This message is for the designated recipient only and may contain privileged, proprietary, or otherwise private information. If you have received it in error, please notify the sender immediately and delete the original. Any other use of this email is prohibited.*

**De:** Jean-Francois Boissou \<Jean-Francois.Boissou@hgh.fr\>
**Envoyé:** mardi 2 juin 2020 10:27
**À:** Tonny Lemmens \<Tonny.Lemmens@sibelco.com\>; Harry Stienen \<Harry.Stienen@sibelco.com\>
**Cc:** Geert Staes \<Geert.Staes@sibelco.com\>; Romain Guider \<romain.guider@hgh.fr\>; Antoine Cotinat \<antoine.cotinat@hgh.fr\>
**Objet:** RE: OPC interface to control the retraction of the kiln camera

Dear Tonny,

Following our telephone conversation today, we note that we can use OPC DA in the present case, without impairing the operation of your system in the medium term.
Romain and Antoine will get back to you soon to discuss the details of the interface more in detail.

Best regards

Jean-Francois

**De:** Tonny Lemmens \<<Tonny.Lemmens@sibelco.com>\>
**Envoyé:** mardi 2 juin 2020 08:55
**À:** Jean-Francois Boissou \<<Jean-Francois.Boissou@hgh.fr>\>; Harry Stienen \<<Harry.Stienen@sibelco.com>\>
**Cc:** Geert Staes \<<Geert.Staes@sibelco.com>\>; Romain Guider \<<romain.guider@hgh.fr>\>; Antoine Cotinat \<<antoine.cotinat@hgh.fr>\>
**Objet:** RE: OPC interface to control the retraction of the kiln camera

Dear Jean-François,

I didn’t know that the camera only has OPC DA. I thought you could choose.
OPC DA is based on Microsoft’s old COM/DCOM standard, which is sometimes difficult to get is working.

Knowing this I assume that you need a pc running Windows. And that pc will run software (opc server or client) that controls the camera.

Once we have an OPC connection, It’s quite easy to exchange signals.
I’ve read Leaflet_Kilnscan_HGH_HR.pdf brochure from your website. It’s says that you can also interface with 4-20mA and dry contact outputs. Depending on the number of signals this might be a better option to use.

Best regards,

**Tonny Lemmens**
Automation Engineer

![image5](image5-15%201.png)

De Zate 1
BE-2480 Dessel
Belgium
**Tel** +32 (0) 14 837 283
**Mob** +32 (0) 494500 437
[www.sibelco.com](https://eur01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.sibelco.com%2F&data=02%7C01%7CTonny.Lemmens%40sibelco.com%7C47114148617a48e9745008d812c256cf%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C637279973340274856&sdata=FwrQ1HQ29c3Q0ybgRou%2BwRHVoaiVrgfXZ6xNKrQdsDs%3D&reserved=0)

**Maatschappelijke zetel - Siège social - Registered Office: Plantin en Moretuslei 1A - BE-2018 Antwerpen RPR Antwerpen - BTW BE 0 404 679 941 - ING IBAN BE38 3200 0042 7072**

**From:** Jean-Francois Boissou \<<Jean-Francois.Boissou@hgh.fr>\>
**Sent:** vrijdag 29 mei 2020 20:52
**To:** Tonny Lemmens \<<Tonny.Lemmens@sibelco.com>\>; Harry Stienen \<<Harry.Stienen@sibelco.com>\>
**Cc:** Geert Staes \<<Geert.Staes@sibelco.com>\>; Romain Guider \<<romain.guider@hgh.fr>\>; Antoine Cotinat \<<antoine.cotinat@hgh.fr>\>
**Subject:** RE: OPC interface to control the retraction of the kiln camera

Dear Tonny,

First of all I wish to thank you for your prompt reply.
From your email below, we understand that your server basically uses OPC DA and that you can as well use OPC UA through a bridge.
The situation is exactly the same on our side: our camera uses OPC DA and can interface with OPC UA via a bridge.
So if the above is correct if we interface our systems with UA the overall architecture would be to have in the middle two DA\<-\>UA bridges back-to-back.
If this is right, we could as well interface directly with DA, which would make the architecture simpler.
As you advise to interface using UA, probably there is a reason which we don’t know in favor of such a solution.
Of course UA is newer and in the future it should be more and more used in the industry; nevertheless in the present case it does not seem that it is needed.
Again, this is just our (limited) understanding!

Beyond the choice of the OPC version, we will also need to discuss the details of the interface and exchange of controls between your DCS and the camera.
Antoine Cotinat, who belongs to our software team and who will be in charge of this project, will be back to the office on week 24; at that time we will get in touch with you to see how to draw the detailed specification for the interface.

Thank you in advance for your support!

With best regards

<table>
<colgroup>
<col style="width: 51%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Jean-François BOISSOU</strong></p>
<p>Product Line Manager - Thermography</p>
<p><strong>HGH Systèmes Infrarouges</strong></p>
<p>10 rue Maryse Bastié</p>
<p>F91430 Igny - France</p>
<p>T: + 33 (0)1 69 35 47 77</p></th>
<th><blockquote>
<p>![image6](../../resources/image6-13.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><a href="mailto:jean-francois.boissou@hgh.fr">jean-francois.boissou@hgh.fr</a> |<a href="https://eur01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.hgh.fr%2F&amp;data=02%7C01%7CTonny.Lemmens%40sibelco.com%7C47114148617a48e9745008d812c256cf%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C637279973340284849&amp;sdata=MkzZwFQg6AgOWQNnvaKXp%2BDh7MCuxf1si8Q8SExEz6k%3D&amp;reserved=0">www.hgh.fr</a></td>
</tr>
</tbody>
</table>
**
*Follow us on:*

![image2](image2-64.png)

![image3](image3-6.jpg)

![image4](image4-4.jpg)
*<u></u>*
*HGH Infrared Systems will operate under the new unified HGH brand, strengthening the company’s development worldwide, while giving even more value to our customers. [Read more](https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.hgh-infrared.com%2FNews%2FWhat-s-new%2FHGH-expands-its-brand-name-Worldwide&data=02%7C01%7CTonny.Lemmens%40sibelco.com%7C47114148617a48e9745008d812c256cf%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C637279973340304844&sdata=YYXLdD174QZxgP6qGxZvtnhfzBVzZxGOKVRz2Hvkp4Q%3D&reserved=0)*
**
*<u>Notice</u>: This message is for the designated recipient only and may contain privileged, proprietary, or otherwise private information. If you have received it in error, please notify the sender immediately and delete the original. Any other use of this email is prohibited.*

**De:** Tonny Lemmens \<<Tonny.Lemmens@sibelco.com>\>
**Envoyé:** mercredi 27 mai 2020 14:16
**À:** Harry Stienen \<<Harry.Stienen@sibelco.com>\>; Jean-Francois Boissou \<<Jean-Francois.Boissou@hgh.fr>\>
**Cc:** Geert Staes \<<Geert.Staes@sibelco.com>\>; Romain Guider \<<romain.guider@hgh.fr>\>
**Objet:** RE: OPC interface to control the retraction of the kiln camera

Hi,

I can surely help you with developing the OPC feature.
Our DCS system has only OPC DA, but we have an OPC UA bridge (KepServerEx).

My advise is to implement an OPC UA interface. This is the newer, better interface.

I’ve played with the examples from the OPC foundation that you can find on Github, but I haven’t built anything yet.

With best regards,

**Tonny Lemmens**
Automation Engineer

![image5](image5-15%201.png)

De Zate 1
BE-2480 Dessel
Belgium
**Tel** +32 (0) 14 837 283
**Mob** +32 (0) 494500 437
[www.sibelco.com](https://eur01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.sibelco.com%2F&data=02%7C01%7CTonny.Lemmens%40sibelco.com%7C47114148617a48e9745008d812c256cf%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C637279973340304844&sdata=%2Bx32HfHlyv0sQYLTwSp2gYm4soLT5Isea2jR9bjOJYE%3D&reserved=0)

**Maatschappelijke zetel - Siège social - Registered Office: Plantin en Moretuslei 1A - BE-2018 Antwerpen RPR Antwerpen - BTW BE 0 404 679 941 - ING IBAN BE38 3200 0042 7072**

**From:** Harry Stienen \<<Harry.Stienen@sibelco.com>\>
**Sent:** woensdag 27 mei 2020 12:51
**To:** Jean-Francois Boissou \<<Jean-Francois.Boissou@hgh.fr>\>; Tonny Lemmens \<<Tonny.Lemmens@sibelco.com>\>
**Cc:** Geert Staes \<<Geert.Staes@sibelco.com>\>; <romain.guider@hgh.fr>
**Subject:** RE: OPC interface to control the retraction of the kiln camera

Hello,

My college Tonny Lemmens can advise you on this matter , depending on the functionality you need he can
develope a solution to communicate with the ABB DCS controller.

Groet,

Harry Stienen
Maintenance Supervisor
Sibelco Benelux
De Zate 1•BE-2480 Dessel

mob. +32 475 78 59 84
tel. +32 148 37 33 5
fax. +32 148 37 33 2
<Harry.Stienen@sibelco.com>

![image7](image7-9%201.png)
[www.sibelco.eu](https://eur01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.sibelco.eu%2F&data=02%7C01%7CTonny.Lemmens%40sibelco.com%7C47114148617a48e9745008d812c256cf%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C637279973340314837&sdata=T5B%2FB%2FsfpQR0TQJtR66QxkPVjZMJ10%2Fwl4I%2B5qz%2FCMQ%3D&reserved=0)

SCR-SIBELCO NV - Maatschappelijke zetel - Siège social - Registered Office: Plantin en Moretuslei 1A - BE-2018 Antwerpen
RPR Antwerpen - BTW BE 0 404 679 941 - ING IBAN BE38 3200 0042 7072

**Van:** Geert Staes
**Verzonden:** Tuesday, May 26, 2020 8:22
**Aan:** Harry Stienen \<<Harry.Stienen@sibelco.com>\>
**Onderwerp:** FW: OPC interface to control the retraction of the kiln camera

Harry,

Sebiet even over babbelen.

Geert
**From:** Jean-Francois Boissou \<<Jean-Francois.Boissou@hgh.fr>\>
**Sent:** Monday, May 25, 2020 20:30
**To:** Geert Staes \<<Geert.Staes@sibelco.com>\>; Benoit Boone \<<Benoit.Boone@sibelco.com>\>
**Cc:** Romain Guider \<<romain.guider@hgh.fr>\>
**Subject:** OPC interface to control the retraction of the kiln camera

Dear Sirs,

I hope that this email finds you well and that yourselves, your nears and your colleagues haven’t been affected by the pandemic.
During past discussions, you mentioned your interest for a function which would allow to trigger the retraction of the camera via OPC (for instance to bring it to a safe position in case the kiln enters a critical operating mode).
We plan to develop this feature.
In order to specify the interface in a suitable manner, we would appreciate a lot if we could benefit from recommendations from your IT engineers.
If you agree, would you please be kind enough to let us know who we should contact to that aim?

Thank you in advance for your help.

With best regards

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Jean-François BOISSOU</strong></p>
<p>Chef de Produit - Thermographie</p>
<p><strong>HGH Systèmes Infrarouges</strong></p>
<p>10 rue Maryse Bastié</p>
<p>91430 Igny - France</p>
<p>T: + 33 (0)1 69 35 47 77</p></th>
<th><blockquote>
<p>![image8](../../resources/image8-6.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><a href="mailto:jean-francois.boissou@hgh.fr">jean-francois.boissou@hgh.fr</a> |<a href="https://eur01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.hgh.fr%2F&amp;data=02%7C01%7CTonny.Lemmens%40sibelco.com%7C47114148617a48e9745008d812c256cf%7Ca0cac58c12b94f1fb95d2405875a18d6%7C0%7C0%7C637279973340314837&amp;sdata=7kDfjPU9NHwl464uoZDz3NYD08XocxILBFX4bTOv400%3D&amp;reserved=0">www.hgh.fr</a></td>
</tr>
</tbody>
</table>
**
*Retrouvez nous sur:*

- # [[2020-06-22]] 
  **From:** Geert Staes \<Geert.Staes@sibelco.com\>
  **Sent:** maandag 22 juni 2020 12:51
  **To:** Tonny Lemmens \<Tonny.Lemmens@sibelco.com\>; Harry Stienen \<Harry.Stienen@sibelco.com\>
  **Subject:** RE: OPC interface to control the retraction of the kiln camera
  
  Tonny,
  
  Camera wordt half juli geleverd. Daarna kunnen wij pas starten met het maken van een mechanisch statief.
  aansluitend met het plaatsen van de elekkast/bekabeling. à Harry
  Gaat snel begin augustus zijn voor op te starten.
  
  Regards,
  
  Geert Staes