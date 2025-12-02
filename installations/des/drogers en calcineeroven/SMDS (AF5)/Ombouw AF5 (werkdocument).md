---
title: Ombouw AF5 (werkdocument)
updated: [[2022-01-21]]T13:38:14.0000000+01:00
created: [[2019-02-18]]T13:18:26.0000000+01:00
---

- # Todo (tijdens ombouw)
  In LLZ2 - AF5 de communicatie variabelen koppelen
  
  ![image1](image1-216.png)
  
  Testen in sequentie AF5_10A, AF5_11, AF5_ZS41 -\> AF5_ZS47
  
  CalcineerTpt  
  Kleppen:
  
  CT_50_KL_SS2_Out1 koppelen aan CT_50_KL_AutoCmd
  
  CT_51_KL_SS2_Out1 koppelen aan CT_51_KL_AutoCmd
  
  Motoren:
  
  CT_25_SS2_Out1 koppelen aan CT_25_AutoCmd
  
  Hardware-variabelen terug koppelen.
  
  [Hardware- variabelen.xlsx](assets/resources/Hardware-_variabelen.xlsx)
  
  MES Koppeling omzetten
  
  AF5_15L testen vanuit calcineertpt
  
  AF5_15 PrioCmd0 testen
- # Todo
  Communicatie tussen AF5_TVAZ en LLZ2. Dit is geprogrammeerd.
  
  Communicatie tussen BBZ en AF5_AF7 voor aansturing Filtergroep (AF5_1, AF5_2, AF53, AF5_12)  
  18-Feb-2019 : Is OK
  
  Communicatie tussen Toevoer_FFS_BBZ en AF5_AF7 voor aansturing Filtergroep (AF5_1, AF5_2, AF53, AF5_12)  
  18-Feb-2019 : Is OK
  
  AF5_SMCAL_AutoOff  
  19-Feb-2019 : Is OK
  
  AF5_SMDS1_AutoOff  
  19-Feb-2019 : Is OK
  
  Units - Instrumentatie - Code  
  19-Feb-2019 : Is OK
  
  Units - Kleppen - Code  
  19-Feb-2019 : Is OK
  
  Units - Motoren - Code
- ## Objecten
  <table>
  <colgroup>
  <col style="width: 11%" />
  <col style="width: 15%" />
  <col style="width: 15%" />
  <col style="width: 14%" />
  <col style="width: 14%" />
  <col style="width: 5%" />
  <col style="width: 24%" />
  </colgroup>
  <thead>
  <tr class="header">
  <th><strong>Tag</strong></th>
  <th><strong>Out1</strong></th>
  <th><strong>Out2</strong></th>
  <th><strong>FB1</strong></th>
  <th><strong>FB0</strong></th>
  <th><strong>FB2</strong></th>
  <th><strong>Opmerking</strong></th>
  </tr>
  </thead>
  <tbody>
  <tr class="odd">
  <td>AF5_01</td>
  <td>DO800_10.1</td>
  <td></td>
  <td>DI800_14.1</td>
  <td></td>
  <td></td>
  <td><blockquote>
  <p>Wordt OOK gestart vanuit AF5_FGST_BB en AF5_FGST_FFS.</p>
  <p>Programmatie aansturing vanuit nieuw BBZ</p>
  <p>Programmatie aansturing vanuit FFS</p>
  <p>Aansturing vanuit SMCAL</p>
  <p>Aansturing vanuit SMDS1</p>
  </blockquote></td>
  </tr>
  <tr class="even">
  <td>AF5_02</td>
  <td>DO800_10.2</td>
  <td></td>
  <td>DI800_14.2</td>
  <td></td>
  <td></td>
  <td><blockquote>
  <p>Wordt OOK gestart vanuit AF5_FGST_BB en AF5_FGST_FFS.</p>
  <p>Programmatie aansturing vanuit nieuw BBZ</p>
  <p>Programmatie aansturing vanuit FFS</p>
  <p>Aansturing vanuit SMCAL</p>
  <p>Aansturing vanuit SMDS1</p>
  </blockquote></td>
  </tr>
  <tr class="odd">
  <td>AF5_03</td>
  <td>DO800_10.3</td>
  <td></td>
  <td>DI800_14.3</td>
  <td></td>
  <td></td>
  <td><blockquote>
  <p>Wordt OOK gestart vanuit AF5_FGST_BB en AF5_FGST_FFS.</p>
  <p>Programmatie aansturing vanuit nieuw BBZ</p>
  <p>Programmatie aansturing vanuit FFS</p>
  <p>Aansturing vanuit SMCAL</p>
  <p>Aanstruing vanuit SMDS1</p>
  </blockquote></td>
  </tr>
  <tr class="even">
  <td>AF5_04</td>
  <td>DO800_10.4</td>
  <td></td>
  <td>DI800_14.4</td>
  <td></td>
  <td></td>
  <td><blockquote>
  <p>Aansturing vanuit SMCAL</p>
  <p>Aansturing vanuit SMDS1</p>
  <p>PrioCmd0</p>
  </blockquote></td>
  </tr>
  <tr class="odd">
  <td>AF5_05</td>
  <td>DO800_10.5</td>
  <td></td>
  <td>DI800_14.5</td>
  <td></td>
  <td></td>
  <td><blockquote>
  <p>Aansturing vanuit SMCAL / SMDS1</p>
  <p>PrioCmd0</p>
  </blockquote></td>
  </tr>
  <tr class="even">
  <td>AF5_06</td>
  <td>DO800_10.6</td>
  <td></td>
  <td>DI800_14.6</td>
  <td></td>
  <td></td>
  <td><blockquote>
  <p>Aansturing vanuit SMCAL</p>
  <p>PrioCmd0</p>
  </blockquote></td>
  </tr>
  <tr class="odd">
  <td>AF5_07</td>
  <td>DO800_10.7</td>
  <td></td>
  <td>DI800_14.7</td>
  <td></td>
  <td></td>
  <td><blockquote>
  <p>Aansturing vanuit SMCAL</p>
  <p>PrioCmd0</p>
  </blockquote></td>
  </tr>
  <tr class="even">
  <td>AF5_08</td>
  <td>DO800_10.8</td>
  <td></td>
  <td>DI800_14.8</td>
  <td></td>
  <td></td>
  <td><blockquote>
  <p>Aansturing vanuit SMCAL</p>
  <p>PrioCmd0</p>
  </blockquote></td>
  </tr>
  <tr class="odd">
  <td>AF5_12</td>
  <td>DO800_10.10</td>
  <td></td>
  <td>DI800_14.9</td>
  <td></td>
  <td></td>
  <td><blockquote>
  <p>Wordt OOK gestart vanuit AF5_FGST_BB en AF5_FGST_FFS.</p>
  <p>Programmatie aansturing vanuit nieuw BBZ</p>
  <p>Programmatie aansturing vanuit FFS</p>
  <p>Aansturing vanuit SMCAL / SMDS1</p>
  <p>ProiCmd0</p>
  </blockquote></td>
  </tr>
  <tr class="even">
  <td>AF5_13</td>
  <td>DO800_10.11</td>
  <td></td>
  <td>DI800_14.10</td>
  <td></td>
  <td></td>
  <td><blockquote>
  <p>Aansturing vanuit SMCAL / SMDS1</p>
  <p>PrioCmd0</p>
  </blockquote></td>
  </tr>
  <tr class="odd">
  <td><del>AF5_14</del></td>
  <td><del>DO800_10.12</del></td>
  <td></td>
  <td><del>DI800_31.3</del></td>
  <td></td>
  <td></td>
  <td><del>Bestaat deze nog?</del></td>
  </tr>
  <tr class="even">
  <td>AF5_15</td>
  <td>DO800_10.14</td>
  <td>DO800_10.13</td>
  <td></td>
  <td></td>
  <td></td>
  <td><blockquote>
  <p>Aansturing vanuit SMDS1</p>
  <p>Aansturing vanuit CalcineerTPT</p>
  <p>PrioCmd0: nagekeken</p>
  </blockquote></td>
  </tr>
  <tr class="odd">
  <td>AF5_16</td>
  <td>DO800_11.15</td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td><blockquote>
  <p>Aansturing vanuit SMDS1</p>
  <p>PrioCmd0</p>
  </blockquote></td>
  </tr>
  <tr class="even">
  <td>AF5_17</td>
  <td>DO800_11.13</td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td><blockquote>
  <p>Aansturing vanuit SMDS1</p>
  <p>PrioCmd0</p>
  </blockquote></td>
  </tr>
  <tr class="odd">
  <td>AF5_18</td>
  <td>DO800_10.16</td>
  <td>DO800_10.15</td>
  <td></td>
  <td></td>
  <td></td>
  <td><blockquote>
  <p>Aansturing vanuit SMDS1</p>
  </blockquote></td>
  </tr>
  <tr class="even">
  <td>AF5_FGI</td>
  <td>DO800_10.9</td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>AF5_K1</td>
  <td>DO800_11.1</td>
  <td></td>
  <td>DI800_15.1</td>
  <td>DI800_15.2</td>
  <td></td>
  <td><blockquote>
  <p>Aansturing als SMCAL niet draait</p>
  </blockquote></td>
  </tr>
  <tr class="even">
  <td><del>AF5_K2</del></td>
  <td><del>DO800_11.9</del></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td><del>Weggevallen</del></td>
  </tr>
  <tr class="odd">
  <td>AF5_K3</td>
  <td>DO800_11.10</td>
  <td></td>
  <td><p>DI800_16.14</p>
  <p>Nakijken</p></td>
  <td><p>DI800_16.15</p>
  <p>Nakijken</p></td>
  <td></td>
  <td><blockquote>
  <p>Aansturing vanuit SMCAL / SMDS1</p>
  </blockquote></td>
  </tr>
  <tr class="even">
  <td>AF5_K4</td>
  <td>DO800_11.11</td>
  <td>Wordt deze nog gebruikt</td>
  <td>DI800_14.11</td>
  <td>DI800_14.12</td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td><del>AF5_K5</del></td>
  <td><del>DO800_11.12</del></td>
  <td><del>Wordt deze nog gebruikt ?</del></td>
  <td><del>DI800_14.13</del></td>
  <td><del>DI800_14.14</del></td>
  <td></td>
  <td><del>Wordt niet meer gebruikt</del></td>
  </tr>
  <tr class="even">
  <td>AF5_K6</td>
  <td>DO800_11.13</td>
  <td></td>
  <td>DI800_14.15</td>
  <td>DI800_14.16</td>
  <td></td>
  <td><blockquote>
  <p>Aansturing vanuit SMCAL / SMDS1</p>
  </blockquote></td>
  </tr>
  <tr class="odd">
  <td>AF5_SK2</td>
  <td>DO800_11.5</td>
  <td></td>
  <td>DI800_15.9</td>
  <td>DI800_15.10</td>
  <td></td>
  <td><blockquote>
  <p>Aansturing vanuit SMCAL / SMDS1</p>
  </blockquote></td>
  </tr>
  <tr class="even">
  <td>AF5_WK1</td>
  <td>DO800_11.2</td>
  <td></td>
  <td>DI800_15.3</td>
  <td>DI800_15.4</td>
  <td></td>
  <td><blockquote>
  <p>Aansturing vanuit SMCAL / SMDS1</p>
  </blockquote></td>
  </tr>
  <tr class="odd">
  <td>AF5_WK3</td>
  <td>DO800_11.4</td>
  <td></td>
  <td>DI800_15.8</td>
  <td>DI800_15.7</td>
  <td></td>
  <td><blockquote>
  <p>Aansturing vanuit SMCAL / SMDS1</p>
  </blockquote></td>
  </tr>
  <tr class="even">
  <td>AF5_ZS54</td>
  <td>DO800_11.6</td>
  <td></td>
  <td>DI800_15.11</td>
  <td>DI800_15.12</td>
  <td></td>
  <td><blockquote>
  <p>Aansturing vanuit SMCAL</p>
  <p>Vergrendeling LSH6</p>
  <p>AF5_6 statstop</p>
  </blockquote></td>
  </tr>
  <tr class="odd">
  <td>AF5_ZS55</td>
  <td>DO800_11.7</td>
  <td></td>
  <td>DI800_15.13</td>
  <td>DI800_15.14</td>
  <td></td>
  <td><blockquote>
  <p>Aansturing vanuit SMCAL</p>
  <p>AF5_7 statstop</p>
  </blockquote></td>
  </tr>
  <tr class="even">
  <td>AF5_ZS56</td>
  <td>DO800_11.8</td>
  <td></td>
  <td>DI800_15.15</td>
  <td>DI800_15.16</td>
  <td></td>
  <td><blockquote>
  <p>Aansturing vanuit SMCAL</p>
  <p>AF5_8 statstop</p>
  </blockquote></td>
  </tr>
  <tr class="odd">
  <td>AF5_ZS57</td>
  <td>DO800_11.14</td>
  <td></td>
  <td>DI800_31.1</td>
  <td>DI800_31.2</td>
  <td></td>
  <td><blockquote>
  <p>Aansturing vanuit SMCAL</p>
  <p>AF5_13 statstop</p>
  </blockquote></td>
  </tr>
  </tbody>
  </table>
- ## Klassieke DI - DO - AI
  <table>
  <colgroup>
  <col style="width: 20%" />
  <col style="width: 16%" />
  <col style="width: 21%" />
  <col style="width: 41%" />
  </colgroup>
  <thead>
  <tr class="header">
  <th><strong>TAG</strong></th>
  <th></th>
  <th></th>
  <th></th>
  </tr>
  </thead>
  <tbody>
  <tr class="odd">
  <td>AF5_IT1</td>
  <td>AI800_7.1</td>
  <td><p>=&gt; S_CAL_2.R14</p>
  <p>Stroom van AF5_1</p></td>
  <td>0 .. 20 mA (0 .. 100A)</td>
  </tr>
  <tr class="even">
  <td>--</td>
  <td>AI800_7.2</td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>AF5_TT1</td>
  <td>AI800_7.3</td>
  <td>niet gebruikt</td>
  <td></td>
  </tr>
  <tr class="even">
  <td>--</td>
  <td>AI800_7.4</td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>--</td>
  <td>AI800_7.5</td>
  <td></td>
  <td></td>
  </tr>
  <tr class="even">
  <td>--</td>
  <td>AI800_7.6</td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>--</td>
  <td>AI800_7.7</td>
  <td></td>
  <td></td>
  </tr>
  <tr class="even">
  <td>--</td>
  <td>AI800_7.8</td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="even">
  <td>--</td>
  <td>AO800_4.1</td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>AF5_SO1</td>
  <td>AO800_4.2</td>
  <td>Snelheid AF5_1 (staat vast op 30%)</td>
  <td>4 .. 20mA (0 .. 100%)</td>
  </tr>
  <tr class="even">
  <td>LT_ZS103_AO</td>
  <td>AO800_4.3</td>
  <td>niet gebruikt</td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>LT_ZS104_AO</td>
  <td>AO800_4.4</td>
  <td>niet gebruikt</td>
  <td></td>
  </tr>
  <tr class="even">
  <td>LT_ZS105_AO</td>
  <td>AO800_4.5</td>
  <td>niet gebruikt</td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>LT_ZS106_AO</td>
  <td>AO800_4.6</td>
  <td>niet gebruikt</td>
  <td></td>
  </tr>
  <tr class="even">
  <td>AF5_SO2</td>
  <td>AO800_4.7</td>
  <td>Snelheid AF5_2 (staat vast op 100%)</td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>--</td>
  <td>AO800_4.8</td>
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
  <td>AF6_BH_DI</td>
  <td>DI800_16.1</td>
  <td>Kast op hand =&gt; Verwijderen</td>
  <td></td>
  </tr>
  <tr class="even">
  <td>AF5_LSH1</td>
  <td>DI800_16.2</td>
  <td>Wordt niet meer gebruikt</td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>AF5_LSH4</td>
  <td>DI800_16.3</td>
  <td>Hoogniveau AF5_5</td>
  <td></td>
  </tr>
  <tr class="even">
  <td>AF5_LSH7</td>
  <td>DI800_16.4</td>
  <td>Hoogniveau WK1 - Wordt niet gebruikt</td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>AF5_LSH6</td>
  <td>DI800_16.5</td>
  <td>Hoogniveau AF5_6</td>
  <td></td>
  </tr>
  <tr class="even">
  <td>AF5_LSH103</td>
  <td>DI800_16.6</td>
  <td>Hoogniveau ZS103</td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>AF5_LSH104</td>
  <td>DI800_16.7</td>
  <td>Hoogniveau ZS104</td>
  <td></td>
  </tr>
  <tr class="even">
  <td>AF5_LSH105</td>
  <td>DI800_16.8</td>
  <td>Hoogniveau ZS105</td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>AF5_LSH106</td>
  <td>DI800_16.9</td>
  <td>Hoogniveau ZS106</td>
  <td></td>
  </tr>
  <tr class="even">
  <td>AF5_FGST_BB_DI</td>
  <td>DI800_16.10</td>
  <td>Filter start van BB</td>
  <td>DI wegwerken, dit zit in weger BBZ.<br />
  AF8_FGST_DO in BBZ.Weger de filtergroep (AF5_1, AF5_2_AF5_3, AF5_12) laten aansturen</td>
  </tr>
  <tr class="odd">
  <td>AF5_2_ST_DI</td>
  <td>DI800_16.11</td>
  <td>Filter storing</td>
  <td></td>
  </tr>
  <tr class="even">
  <td>AF5_K2_O</td>
  <td>DI800_16.12</td>
  <td>Nog gebruikt ? =&gt; Nee</td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>AF5_K2_T</td>
  <td>DI800_16.13</td>
  <td>Nog gebruikt ? =&gt; Nee</td>
  <td></td>
  </tr>
  <tr class="even">
  <td>AF5_FGST_FFS_DI</td>
  <td>DI800_16.16</td>
  <td>Filter start van FFS</td>
  <td><p>DI wegwerken, dit zit in Toevoer_FFS_BBZ.</p>
  <p>In Program2.AF7_FG_STT de filtergroep (AF5_1, AF5_2_AF5_3, AF5_12) laten aansturen</p></td>
  </tr>
  <tr class="odd">
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="even">
  <td>AF5_ZS57_O</td>
  <td>DI800_31.1</td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>AF5_ZS57_T</td>
  <td>DI800_31.2</td>
  <td></td>
  <td></td>
  </tr>
  <tr class="even">
  <td>AF5_14_DI</td>
  <td>DI800_31.3</td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>AF5_14_SOK_DI</td>
  <td>DI800_31.4</td>
  <td>Storing Magneet</td>
  <td></td>
  </tr>
  <tr class="even">
  <td>AF5_15_LSH_DI</td>
  <td>DI800_31.5</td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>AF5_4_WS</td>
  <td>DI800_31.6</td>
  <td></td>
  <td></td>
  </tr>
  <tr class="even">
  <td></td>
  <td>DI800_31.7</td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td></td>
  <td>DI800_31.8</td>
  <td></td>
  <td></td>
  </tr>
  <tr class="even">
  <td></td>
  <td>DI800_31.9</td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td></td>
  <td>DI800_31.10</td>
  <td></td>
  <td></td>
  </tr>
  <tr class="even">
  <td></td>
  <td>DI800_31.11</td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td></td>
  <td>DI800_31.12</td>
  <td></td>
  <td></td>
  </tr>
  <tr class="even">
  <td></td>
  <td>DI800_31.13</td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td></td>
  <td>DI800_31.14</td>
  <td></td>
  <td></td>
  </tr>
  <tr class="even">
  <td></td>
  <td>DI800_31.15</td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td></td>
  <td>DI800_31.16</td>
  <td></td>
  <td></td>
  </tr>
  </tbody>
  </table>
- # 19-Feb-2019 
  Hier wordt toch niemand blij of vrolijk van
  
  ![image2](image2-122.png)
  
  TOV
  
  AF5_SMCAL_AutoOff := (Par.Sequenties.SMCAL_SFC.OnSeq) AND
  
  (
  
  ((Par.MES.SMCAL_Recept.KeuzeActief.DoelSilo1=103) AND (Par.Instrumentatie.AF5_LSH103_OutDiff OR Comm_From.ZT.LT_ZS103_GTHHH)) OR
  
  ((Par.MES.SMCAL_Recept.KeuzeActief.DoelSilo1=104) AND (Par.Instrumentatie.AF5_LSH104_OutDiff OR Comm_From.ZT.LT_ZS104_GTHHH)) OR
  
  ((Par.MES.SMCAL_Recept.KeuzeActief.DoelSilo1=105) AND (Par.Instrumentatie.AF5_LSH105_OutDiff OR Comm_From.ZT.LT_ZS105_GTHHH)) OR
  
  ((Par.MES.SMCAL_Recept.KeuzeActief.DoelSilo1=106) AND (Par.Instrumentatie.AF5_LSH106_OutDiff OR Comm_From.ZT.LT_ZS106_GTHHH)) OR
  
  ((Par.MES.SMCAL_Recept.KeuzeActief.DoelSilo1=49) AND Comm_From.D3.LSH_ZS49) OR
  
  ((Par.MES.SMCAL_Recept.KeuzeActief.DoelSilo1=50) AND Comm_From.D3.LSH_ZS50) OR
  
  ((Par.MES.SMCAL_Recept.KeuzeActief.DoelSilo1=51) AND Comm_From.D3.LSH_ZS51)
  
  );