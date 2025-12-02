---
title: Panel Builder WPF
updated: [[2019-07-02]]T08:05:00.0000000+02:00
created: [[2018-06-01]]T14:53:08.0000000+02:00
---

- # Maak custom UserControls voor gebruik in PanelBuilder
  
  In Visual Studio maak een Project UserControl
- # Koppeling Panel Builder en Custom Control
  
  In de UserControl moet een method worden aangemaakt
  
  Voeg Resources toe. De Dlls zitten in
  D:\OneDrive - Sibelco\Toepassingen\Panel Builder 800\Import DLLs
  
  Voeg de nodige using regels toe
  
  In Panel Builder script moet per tag een delegate worden toegevoegd van de UserControl
  
  Gebruik hiervoor de setTag method van de UserControl.
  NIET VERGETEN de UnTag method bij unloading (=\> avoid memory leak).
- # Debuggen
  Om snel te kunnen debuggen moet project worden geImporteerd in Panel Builder Debug
- In Panel Builder klik op Project - Debug
- Visual Studio wordt geopend
- Voeg het SibWpfControlLibrary project in Visual Studio.  
  D:\OneDrive - Sibelco\Toepassingen\Panel Builder 800\SibWpfControlLibrary
- Verwijder de SibelcoControlLibrary bij de references en voeg het Project toe.
- # Import van Custom control
  In Panel Builder Home tab
  Klik bij Objects Add Control
  ![image1](image1-179.png)
  
  Klik Browse
  
  Neem de dll uit de debug directory van Visual Studio
  
  De dll wordt ook automatische gekopieerd naar
  C:\Users\Public\Documents\ABB\Panel Builder 800 Version 6\Thirdparty
- # [[2019-06-21]] 8:16 
  Een tijdje niet meer met Panel builder gewerkt, en computer was ondertussen geherïnstalleerd.
  Project kon niet meer worden geladen met de custom library.
  
  Eens testen of het niet kan met Command-woord en Status-woord.
- # Status woord - Command woord
  Omdat ik een multi-picture rechtsstreeks willen koppelen aan een tag, moet Status en Command bits worden gesplitst in twee woorden.
- # Statuswoord
  1 woord gebruiken voor Uni/Bi Motor en Valve
  
  Status bits
- FB0 / FB1 / FB2 / Onbepaald (2bits)
- Alarm
- ManMode
- Interlock
- SafetyStop
  
  6 bits -\> 64 combinaties, maar sommige combinaties kunnen niet voorkomen.
  
  <table>
  <colgroup>
  <col style="width: 8%" />
  <col style="width: 7%" />
  <col style="width: 12%" />
  <col style="width: 10%" />
  <col style="width: 12%" />
  <col style="width: 8%" />
  <col style="width: 13%" />
  <col style="width: 13%" />
  <col style="width: 13%" />
  </colgroup>
  <thead>
  <tr class="header">
  <th><strong>Status</strong></th>
  <th><strong>Bits</strong></th>
  <th><p><strong>SafetyStop</strong></p>
  <p>(BIT 5)</p></th>
  <th><p><strong>Interlock</strong></p>
  <p>(BIT 4)</p></th>
  <th><p><strong>ManMode</strong></p>
  <p>(BIT 3)</p></th>
  <th><p><strong>Alarm</strong></p>
  <p>(BIT 2)</p></th>
  <th><p><strong>Feedback</strong></p>
  <p>Motor: FB2 / FB1</p>
  <p>Valve: FB1 / FB0</p>
  <p>(BIT 1 / BIT 0)</p></th>
  <th><strong>MOTOR</strong></th>
  <th><strong>VALVE</strong></th>
  </tr>
  </thead>
  <tbody>
  <tr class="odd">
  <td>0</td>
  <td>0000 0000</td>
  <td>0</td>
  <td>0</td>
  <td>0</td>
  <td>0</td>
  <td>00</td>
  <td>![image2](../../../../../resources/image2-103.png)</td>
  <td>![image3](../../../../../resources/image3-58.png)</td>
  </tr>
  <tr class="even">
  <td>1</td>
  <td>0000 0001</td>
  <td>0</td>
  <td>0</td>
  <td>0</td>
  <td>0</td>
  <td>01</td>
  <td>![image4](../../../../../resources/image4-33.png)</td>
  <td>![image5](../../../../../resources/image5-28.png)</td>
  </tr>
  <tr class="odd">
  <td>2</td>
  <td>0000 0010</td>
  <td>0</td>
  <td>0</td>
  <td>0</td>
  <td>0</td>
  <td>10</td>
  <td>![image6](../../../../../resources/image6-23.png)</td>
  <td>![image7](../../../../../resources/image7-19.png)</td>
  </tr>
  <tr class="even">
  <td>3</td>
  <td>0000 0011</td>
  <td>0</td>
  <td>0</td>
  <td>0</td>
  <td>0</td>
  <td>11</td>
  <td>NOT USED</td>
  <td>NOT USED</td>
  </tr>
  <tr class="odd">
  <td>4</td>
  <td>0000 0100</td>
  <td>0</td>
  <td>0</td>
  <td>0</td>
  <td>1</td>
  <td>00</td>
  <td>![image8](../../../../../resources/image8-17.png)</td>
  <td>![image9](../../../../../resources/image9-14.png)</td>
  </tr>
  <tr class="even">
  <td>5</td>
  <td>0000 0101</td>
  <td>0</td>
  <td>0</td>
  <td>0</td>
  <td>1</td>
  <td>01</td>
  <td>![image10](../../../../../resources/image10-12.png)</td>
  <td>![image11](../../../../../resources/image11-11.png)</td>
  </tr>
  <tr class="odd">
  <td>6</td>
  <td>0000 0110</td>
  <td>0</td>
  <td>0</td>
  <td>0</td>
  <td>1</td>
  <td>10</td>
  <td>![image12](../../../../../resources/image12-10.png)</td>
  <td>![image13](../../../../../resources/image13-9.png)</td>
  </tr>
  <tr class="even">
  <td>7</td>
  <td>0000 0111</td>
  <td>0</td>
  <td>0</td>
  <td>0</td>
  <td>1</td>
  <td>11</td>
  <td>NOT USED</td>
  <td>NOT USED</td>
  </tr>
  <tr class="odd">
  <td>8</td>
  <td>0000 1000</td>
  <td>0</td>
  <td>0</td>
  <td>1</td>
  <td>0</td>
  <td>00</td>
  <td>![image14](../../../../../resources/image14-6.png)</td>
  <td>![image15](../../../../../resources/image15-7.png)</td>
  </tr>
  <tr class="even">
  <td>9</td>
  <td>0000 1001</td>
  <td>0</td>
  <td>0</td>
  <td>1</td>
  <td>0</td>
  <td>01</td>
  <td>![image16](../../../../../resources/image16-6.png)</td>
  <td>![image17](../../../../../resources/image17-5.png)</td>
  </tr>
  <tr class="odd">
  <td>10</td>
  <td>0000 1010</td>
  <td>0</td>
  <td>0</td>
  <td>1</td>
  <td>0</td>
  <td>10</td>
  <td>![image18](../../../../../resources/image18-4.png)</td>
  <td>![image19](../../../../../resources/image19-5.png)</td>
  </tr>
  <tr class="even">
  <td>11</td>
  <td>0000 1011</td>
  <td>0</td>
  <td>0</td>
  <td>1</td>
  <td>0</td>
  <td>11</td>
  <td>NOT USED</td>
  <td>NOT USED</td>
  </tr>
  <tr class="odd">
  <td>12</td>
  <td>0000 1100</td>
  <td>0</td>
  <td>0</td>
  <td>1</td>
  <td>1</td>
  <td>00</td>
  <td>![image20](../../../../../resources/image20-4.png)</td>
  <td>![image21](../../../../../resources/image21-4.png)</td>
  </tr>
  <tr class="even">
  <td>13</td>
  <td>0000 1101</td>
  <td>0</td>
  <td>0</td>
  <td>1</td>
  <td>1</td>
  <td>01</td>
  <td>![image22](../../../../../resources/image22-4.png)</td>
  <td>![image23](../../../../../resources/image23-4.png)</td>
  </tr>
  <tr class="odd">
  <td>14</td>
  <td>0000 1110</td>
  <td>0</td>
  <td>0</td>
  <td>1</td>
  <td>1</td>
  <td>10</td>
  <td>![image24](../../../../../resources/image24-4.png)</td>
  <td><p>![image25](../../../../../resources/image25-4.png)</p>
  <p></p></td>
  </tr>
  <tr class="even">
  <td>15</td>
  <td>0000 1111</td>
  <td>0</td>
  <td>0</td>
  <td>1</td>
  <td>1</td>
  <td>11</td>
  <td>NOT USED</td>
  <td>NOT USED</td>
  </tr>
  <tr class="odd">
  <td>16</td>
  <td>0001 0000</td>
  <td>0</td>
  <td>1</td>
  <td>0</td>
  <td>0</td>
  <td>00</td>
  <td>![image26](../../../../../resources/image26-4.png)</td>
  <td>![image27](../../../../../resources/image27-4.png)</td>
  </tr>
  <tr class="even">
  <td>17</td>
  <td>0001 0001</td>
  <td>0</td>
  <td>1</td>
  <td>0</td>
  <td>0</td>
  <td>01</td>
  <td>NOT USED</td>
  <td>![image28](../../../../../resources/image28-4.png)</td>
  </tr>
  <tr class="odd">
  <td>18</td>
  <td>0001 0010</td>
  <td>0</td>
  <td>1</td>
  <td>0</td>
  <td>0</td>
  <td>10</td>
  <td>NOT USED</td>
  <td>NOT USED</td>
  </tr>
  <tr class="even">
  <td>19</td>
  <td>0001 0011</td>
  <td>0</td>
  <td>1</td>
  <td>0</td>
  <td>0</td>
  <td>11</td>
  <td>NOT USED</td>
  <td>NOT USED</td>
  </tr>
  <tr class="odd">
  <td>20</td>
  <td>0001 0100</td>
  <td>0</td>
  <td>1</td>
  <td>0</td>
  <td>1</td>
  <td>00</td>
  <td>![image29](../../../../../resources/image29-4.png)</td>
  <td>![image30](../../../../../resources/image30-4.png)</td>
  </tr>
  <tr class="even">
  <td>21</td>
  <td>0001 0101</td>
  <td>0</td>
  <td>1</td>
  <td>0</td>
  <td>1</td>
  <td>01</td>
  <td>NOT USED</td>
  <td>![image31](../../../../../resources/image31-4.png)</td>
  </tr>
  <tr class="odd">
  <td>22</td>
  <td>0001 0110</td>
  <td>0</td>
  <td>1</td>
  <td>0</td>
  <td>1</td>
  <td>10</td>
  <td>NOT USED</td>
  <td>NOT USED</td>
  </tr>
  <tr class="even">
  <td>23</td>
  <td>0001 0111</td>
  <td>0</td>
  <td>1</td>
  <td>0</td>
  <td>1</td>
  <td>11</td>
  <td>NOT USED</td>
  <td>NOT USED</td>
  </tr>
  <tr class="odd">
  <td>24</td>
  <td>0001 1000</td>
  <td>0</td>
  <td>1</td>
  <td>1</td>
  <td>0</td>
  <td>00</td>
  <td>![image32](../../../../../resources/image32-3.png)</td>
  <td>![image33](../../../../../resources/image33-3.png)</td>
  </tr>
  <tr class="even">
  <td>25</td>
  <td>0001 1001</td>
  <td>0</td>
  <td>1</td>
  <td>1</td>
  <td>0</td>
  <td>01</td>
  <td>NOT USED</td>
  <td>![image34](../../../../../resources/image34-3.png)</td>
  </tr>
  <tr class="odd">
  <td>26</td>
  <td>0001 1010</td>
  <td>0</td>
  <td>1</td>
  <td>1</td>
  <td>0</td>
  <td>10</td>
  <td>NOT USED</td>
  <td>NOT USED</td>
  </tr>
  <tr class="even">
  <td>27</td>
  <td>0001 1011</td>
  <td>0</td>
  <td>1</td>
  <td>1</td>
  <td>0</td>
  <td>11</td>
  <td>NOT USED</td>
  <td>NOT USED</td>
  </tr>
  <tr class="odd">
  <td>28</td>
  <td>0001 1100</td>
  <td>0</td>
  <td>1</td>
  <td>1</td>
  <td>1</td>
  <td>00</td>
  <td>![image35](../../../../../resources/image35-3.png)</td>
  <td>![image36](../../../../../resources/image36-3.png)</td>
  </tr>
  <tr class="even">
  <td>29</td>
  <td>0001 1101</td>
  <td>0</td>
  <td>1</td>
  <td>1</td>
  <td>1</td>
  <td>01</td>
  <td>NOT USED</td>
  <td>![image37](../../../../../resources/image37-3.png)</td>
  </tr>
  <tr class="odd">
  <td>30</td>
  <td>0001 1110</td>
  <td>0</td>
  <td>1</td>
  <td>1</td>
  <td>1</td>
  <td>10</td>
  <td>NOT USED</td>
  <td>NOT USED</td>
  </tr>
  <tr class="even">
  <td>31</td>
  <td>0001 1111</td>
  <td>0</td>
  <td>1</td>
  <td>1</td>
  <td>1</td>
  <td>11</td>
  <td>NOT USED</td>
  <td>NOT USED</td>
  </tr>
  <tr class="odd">
  <td><p>32</p>
  <p>…</p>
  <p>63</p></td>
  <td><p>0010 0000</p>
  <p>…</p>
  <p>0011 1111</p></td>
  <td><p>1</p>
  <p>…</p>
  <p>1</p></td>
  <td><p>0</p>
  <p>…</p>
  <p>1</p></td>
  <td><p>0</p>
  <p>…</p>
  <p>1</p></td>
  <td><p>0</p>
  <p>...</p>
  <p>1</p></td>
  <td><p>00</p>
  <p>…</p>
  <p>11</p></td>
  <td>![image38](../../../../../resources/image38-3.png)</td>
  <td></td>
  </tr>
  <tr class="even">
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  </tbody>
  </table>