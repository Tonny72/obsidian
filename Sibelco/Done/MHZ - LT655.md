---
title: MHZ - LT655
updated: [[2022-09-14]]T09:46:09.0000000+02:00
created: [[2022-09-07]]T12:47:54.0000000+02:00
---

| **Subject** | **Lt655**                      |
|-------------|--------------------------------|
| **From**    | Kurt Gerrits                   |
| **To**      | Tonny Lemmens                  |
| **Sent**    | woensdag 7 september 2022 7:15 |

Dag Tonny,

Vandaag vastgesteld dat PU651 en PU661 blijven draaien zonder dat ze voeding krijgen.

Zou je dit zo kunnen maken dat als LT655 \<lll deze 2 uitvallen?

Ook zag ik dat de amperages van de fp661 en fp662 op 0 blijven op de visualisatie.

[[2022-09-09]]

aan het Kurt gevraagd of het niet beter is dat de sequentie van de zeefbandpers worden gestopt

- # [[2022-09-14]] 
  Extra vergrendeling op PU651 en PU652
  1.  LT655 – Niveaumeting
  <table>
  <colgroup>
  <col style="width: 36%" />
  <col style="width: 63%" />
  </colgroup>
  <thead>
  <tr class="header">
  <th>Parameter</th>
  <th>Commentaar</th>
  </tr>
  </thead>
  <tbody>
  <tr class="odd">
  <td>IO</td>
  <td>C2.0.11.309.3 (4 .. 20 mA)</td>
  </tr>
  <tr class="even">
  <td>Range</td>
  <td>0 .. 165 cm</td>
  </tr>
  <tr class="odd">
  <td>HHH</td>
  <td><p>Alarm (155 cm)</p>
  <p>Vergrendeling PU603</p></td>
  </tr>
  <tr class="even">
  <td>HH (130 cm)</td>
  <td>Alarm (130 cm)</td>
  </tr>
  <tr class="odd">
  <td>H (125 cm)</td>
  <td>Event log (125 cm)</td>
  </tr>
  <tr class="even">
  <td>L</td>
  <td><p>Event log (60 cm)</p>
  <p>Seq. Zeefbandpers1.Tr85</p>
  <p>Seq. Zeefbandpers2.Tr85</p></td>
  </tr>
  <tr class="odd">
  <td>LL</td>
  <td>Alarm (55 cm)</td>
  </tr>
  <tr class="even">
  <td>LLL</td>
  <td><p>Alarm (45 cm)</p>
  <p>Vergrendeling PU651</p>
  <p>Vergrendeling PU661</p></td>
  </tr>
  </tbody>
  </table>
  
  2.  PU651 – Wormpomp1
  | Parameter      | Commentaar                |
  |----------------|---------------------------|
  | Motor          | Drive                     |
  | IO             | C2.1.95.1                 |
  | WS             | C2.0.11.107.3             |
  | CI             | C2.0.11.107.4             |
  | Toerental      | 1700 rpm                  |
  | Vergrendeling1 | FP651 / FP652 draait niet |
  | Vergrendeling2 | LT655 \< LLL              |
  | Vergrendeling3 | CPU651 draait niet        |
  | Vergrendeling4 | MI653 draait niet         |
  | SP             | FIC651                    |
  | Start          | Seq. Zeefbandpers.S90     |
  | Stop           | Seq. Zeefbandpers.S500    |
  
  3.  PU661 – Wormpomp2
  | Parameter      | Commentaar                |
  |----------------|---------------------------|
  | Motor          | Drive                     |
  | IO             | C2.1.94.1                 |
  | WS             | C2.0.11.107.1             |
  | CI             | C2.0.11.107.2             |
  | Toerental      | 1700 rpm                  |
  | Vergrendeling1 | FP661 / FP662 draait niet |
  | Vergrendeling2 | LT655 \< LLL              |
  | Vergrendeling3 | CPU661 draait niet        |
  | Vergrendeling4 | MI663 draait niet         |
  | SP             | FIC661                    |
  | Start          | Seq. Zeefbandpers2.S90    |
  | Stop           | Seq. Zeefbandpers2.S500   |
  
  *From \<<https://sibelco.sharepoint.com/teams/Team_SBXMHZ_Benelux_Operations/Public%20Documents/Automatisatie/Beschrijvingen%20installaties/Processbeschrijving%20MHZ.docx>\>*