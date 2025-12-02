---
title: Todo's Ombouw Molen5
updated: [[2019-07-08]]T08:22:56.0000000+02:00
created: [[2016-05-26]]T12:28:18.0000000+02:00
---

- # Noteer de zaken die nog moeten nagekeken worden bij herprogrammatie M5
  
  Sequentie Meeltransport
  
  M5_PDT9000 = M5_PT161 - M5_PT162 maken (S100)
  M5_60 en M5_60V goed nakijken en oude code verwijderen. (unit overblazen BU64)  
  
  Druk airlift nakijken en indien mogelijk verhogen.
- # Ombouw maandag [[2016-06-20]]
  (inclusief werkschakelaars)
  <table>
  <colgroup>
  <col style="width: 40%" />
  <col style="width: 24%" />
  <col style="width: 18%" />
  <col style="width: 16%" />
  </colgroup>
  <thead>
  <tr class="header">
  <th><h1 id="tag">Tag</h1></th>
  <th><h1 id="section"></h1></th>
  <th><h1 id="old">Old</h1></th>
  <th><h1 id="new">New</h1></th>
  </tr>
  </thead>
  <tbody>
  <tr class="odd">
  <td>M5FA401_FA (koelventilator)</td>
  <td>FB1</td>
  <td>0.11.107.3</td>
  <td>0.1.10.4.3</td>
  </tr>
  <tr class="even">
  <td></td>
  <td>WS</td>
  <td>0.11.107.4</td>
  <td>0.1.10.6.6</td>
  </tr>
  <tr class="odd">
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="even">
  <td>M5FI401</td>
  <td>FS (filter storing)</td>
  <td>0.11.107.5</td>
  <td>0.1.10.5.11</td>
  </tr>
  <tr class="odd">
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="even">
  <td><p>M5PT401 (AI)</p>
  <p>(0-500 mmH20)</p></td>
  <td>AI</td>
  <td>0.11.307.3</td>
  <td>0.1.14.3.7</td>
  </tr>
  <tr class="odd">
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="even">
  <td>M5SC401</td>
  <td>FB1</td>
  <td>0.11.107.6</td>
  <td>0.1.10.4.4</td>
  </tr>
  <tr class="odd">
  <td></td>
  <td>WS</td>
  <td>0.11.107.7</td>
  <td>0.1.10.6.7</td>
  </tr>
  <tr class="even">
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>M5SA401</td>
  <td>FB2</td>
  <td>0.11.107.8</td>
  <td>0.1.10.4.5</td>
  </tr>
  <tr class="even">
  <td></td>
  <td>FB1</td>
  <td>0.11.107.9</td>
  <td>0.1.10.4.6</td>
  </tr>
  <tr class="odd">
  <td></td>
  <td>WS</td>
  <td>0.11.107.10</td>
  <td>0.1.10.6.9</td>
  </tr>
  <tr class="even">
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>M5SA402</td>
  <td>FB2</td>
  <td>0.11.107.11</td>
  <td>0.1.10.4.7</td>
  </tr>
  <tr class="even">
  <td></td>
  <td>FB1</td>
  <td>0.11.107.12</td>
  <td>0.1.10.4.8</td>
  </tr>
  <tr class="odd">
  <td></td>
  <td>WS</td>
  <td>0.11.107.13</td>
  <td>0.1.10.6.10</td>
  </tr>
  <tr class="even">
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>M5FA402</td>
  <td>FB1</td>
  <td>0.11.107.14</td>
  <td>0.1.10.4.9</td>
  </tr>
  <tr class="even">
  <td></td>
  <td>WS</td>
  <td>0.11.107.15</td>
  <td>0.1.10.6.11</td>
  </tr>
  <tr class="odd">
  <td></td>
  <td>Out1</td>
  <td></td>
  <td></td>
  </tr>
  <tr class="even">
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>M5BE401 + toerenwachter</td>
  <td>FB1</td>
  <td>0.11.108.1</td>
  <td>0.1.10.4.10</td>
  </tr>
  <tr class="even">
  <td></td>
  <td>WS</td>
  <td>0.11.108.2</td>
  <td>0.1.10.6.12</td>
  </tr>
  <tr class="odd">
  <td></td>
  <td>TW</td>
  <td>0.11.108.3</td>
  <td>0.1.10.4.11</td>
  </tr>
  <tr class="even">
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  </tbody>
  </table>
	- # Ombouw maandag [[2016-06-27]]
	  Old
	  
	  ![image1](image1-255.png)
	  
	  ![image2](image2-144.png)
	  
	  New
	  
	  | M5_8ABC    | Storing motoren           | DI 1.10.8.1 |
	  |------------|---------------------------|-------------|
	  | M5_8C_EKV  | EK spoeltransport vooruit | DI 1.10.8.2 |
	  | M5_8C_EKT  | EK spoeltransport terug   | DI 1.10.8.3 |
	  | M5_8C_TAKT | EK takt positie           | DI 1.10.8.4 |
	  | M5_8B_DKT  | EK draaiklep toe          | DI 1.10.8.5 |
	  | M5_8C_V    | Spoeltransport vooruit    | DI 1.10.8.6 |
	  | M5_8C_T    | Spoeltransport terug      | DI 1.10.8.7 |
	  | M5\_       |                          |            |
	  
	  | M5_8A_STT | Spoelventilator        | DO 1.12.6.1 |    |
	  |-----------|------------------------|-------------|-----|
	  | M5_8B_STT | Spoeldraaiklep         | DO 1.12.6.2 |    |
	  | M5_8C_V   | Spoeltransport terug   | DO 1.12.6.3 |    |
	  | M5_8C_T   | Spoeltransport vooruit | DO 1.12.6.4 |    |