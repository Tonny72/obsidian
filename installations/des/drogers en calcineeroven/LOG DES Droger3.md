---
title: LOG DES Droger3
updated: [[2017-05-02]]T13:12:17.0000000+02:00
created: [[2014-03-15]]T19:07:44.0000000+01:00
---

- # [[2012-12-04]]
  D3_LT2_HHH staat vast op 1.35m
  
  In storingenboek vraag gezet: Naar hoeveel moet dit worden aangepast.
  
  ------------
  
  **From:** Maxime Van Bavel \<<maxime.van.bavel@sibelco.com>\> on behalf of Ronny Lodewyckx \<<Ronny_Lodewyckx@sibelco.com>\>
  
  **Sent:** maandag 3 december 2012 7:43
  
  **To:** Rob Vreys; Tonny Lemmens; Kurt Regout; Geert Staes; Peter Drees; Jos Vanhoof; Kurt Regout
  
  **Subject:** Storingenboek : 2012/DES/1034 - pompbak dr3
  
  Storing :Gelive de HHH level van de 'niveaumeting in pompbak afvalzand' te verhogen.Telkens bij het spoelen (elk uur) van klep D3 MVA2 = droger uit,niveau HHH juist overschreden.
  
  Link naar storing : <Notes://BEDESNTS1/C1256F4E00516589/E31A945EFF57FC2CC1256F5B004B505B/3253FD46197470BDC1257AC70039A012>
- # [[2012-12-06]] 10:22 
  Storing: 2012/DES/1131
  
  Mail naar Geert Staes: Vraag wat moet hiervoor gebeuren.
- # [[2012-12-06]] 13:32 
  Antwoord van Geert: tijd van klep op halve seconde zetten.
  
  ![image1](image1-11%201.png)
  
  Oscilator op 500ms gezet
- # [[2013-02-01]] 8:20 
  Even wat nagekeken. Is niet mogelijk
  
  *aardgasdebiet (indien beschikbaar, eventueel via dagelijkse tellerstanden)*
  <table>
  <colgroup>
  <col style="width: 73%" />
  <col style="width: 26%" />
  </colgroup>
  <thead>
  <tr class="header">
  <th>Branderlast</th>
  <th>D3_BRANDERLAST</th>
  </tr>
  </thead>
  <tbody>
  <tr class="odd">
  <td>Windboxtemperatuur</td>
  <td>D3_TT1</td>
  </tr>
  <tr class="even">
  <td>Druk boven/onder het drogerbed</td>
  <td>D3_PT1 en D3_PT3</td>
  </tr>
  <tr class="odd">
  <td>Zanddebiet</td>
  <td>D3_GT1</td>
  </tr>
  <tr class="even">
  <td>Toerental van de twee toerentalgeregelde ventilatoren</td>
  <td>D3_3 ScaledSpdAct<br />
  D3_1</td>
  </tr>
  <tr class="odd">
  <td>Temperatuur en dauwpunt afgas</td>
  <td>D3_TT7 en D3_TT8</td>
  </tr>
  </tbody>
  </table>
  
  Mail van Geert:
  
  *Tonny,*
  
  *Is dit nog allemaal mogelijk?*
  
  *Mvg*
  
  *Geert*
  
  *----- Forwarded by Geert Staes/DES/SIBELCOBE/AMORG on [[2013-01-31]] 17:25 -----*
  
  *From:Koen Remans \<koen.remans@cee-engineering.be\>*
  
  *To:"geert.staes@sibelco.com" \<geert.staes@sibelco.com\>*
  
  *Cc:"Bart Van Herck \<Bart.Van.Herck@sibelco.com\> (Bart.Van.Herck@sibelco.com)"\<Bart.Van.Herck@sibelco.com\>*
  
  *Date:[[2013-01-31]] 16:06*
  
  *Subject:meetgegevens uit droger 3 sturing*
  
  *Beste Geert,*
  
  *Voor een eerste evaluatie van de meetgegevens zou ik graag de volgende gegevens uit jullie systeem ontvangen:*
  
  *· aardgasdebiet (indien beschikbaar, eventueel via dagelijkse tellerstanden)*
  
  *· branderlast*
  
  *· windboxtemperatuur*
  
  *· druk boven/onder het drogerbed*
  
  *· temperatuur en dauwpunt afgas*
  
  *· zanddebiet*
  
  *· toerental van de twee toerentalgeregelde ventilatoren*
  
  *Is het mogelijk om van de voorbije twee weken deze gegevens al te ontvangen?*
  
  *Met vriendelijke groeten,*
  
  *Koen Remans*
  
  *DESIGN & BUILD CENTER*
  
  *Gsm: +32 498 57 23 38*
- # [[2013-02-04]] 13:09 
  Excel sheet gemaild naar koen.remans@cee-engineering.be
- # [[2013-02-06]] 11:09 
  Excel met nieuwe metingen opgestuurd. Lang gezocht naar bug
  
  Maand en Dag en omgewisseld.
  
  ![image2](Sibelco/resources/image2-7.png)
- # [[2013-07-03]] 11:34 
  D3_13 start niet automatisch (D3_SEQ_DZ)
- # [[2013-07-05]] 10:35 
  D3_13 wordt in verschillende stappen gestart en gestopt. Uitzoeken welke stap een probleem geeft
- # [[2013-07-05]] 11:45 
  Sequentie aangepast
- # [[2014-03-15]] 19:08 
  DX200 van MF2 vervangen door Wim Peeters
- # [[2014-03-18]] 9:01 
  Gisteren is een coax kabel van de MF2 vervangen. Geen uitval meer voorgekomen.
- # [[2016-02-19]] 14:06 
  Voorbereiding geprogrammeerd om D3_18 en D3_21 van werkschakelaars te voorzien.