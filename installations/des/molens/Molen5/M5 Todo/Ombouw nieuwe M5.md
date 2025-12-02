---
title: Ombouw nieuwe M5
updated: [[2022-01-21]]T13:38:26.0000000+01:00
created: [[2014-01-28]]T11:21:09.0000000+01:00
---

<table>
<colgroup>
<col style="width: 0%" />
<col style="width: 99%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><table>
<colgroup>
<col style="width: 53%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th>DI0.11.103.16</th>
<th>M5_COND_F</th>
</tr>
</thead>
<tbody>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Range analoge signalen  
M5_TT110 en M5_TT120 -25 - 100°C

M5_PT110 en M5_PT120 0 - 250 bar

Seq. Aanpassen. Sprong uit seq. verwijderen

Trendingen

Commentaar nog verwijderen Unit_S100 Noodstop

PriorityCmd op oliepompen bij afkoeltijd? Of Stop interlock  
Hoe kritisch is dit? vragen aan Mike.

Alarm niveau's nog bepalen van Flows en Druk in en uitloop  

Wat bij uitval van Temp  
=\> Oplossing: bij onderbreking wordt ISP 100°C genomen

Tijdsvertraging Start Stop Crawl

AEClass nog goed zetten voor Operatoren

M5_MI101FA1 Normal Bij het stoppen van de hoofdmotor zal koelventilator nog 5 minuten nadraaien.  

Data sheets controleren :

<https://sibelco.box.com/s/twxfik0on5fkycwc274a>

<https://sibelco.box.com/s/uat9940m07299l0n1cta>

<https://sibelco.box.com/s/gyorx3vsmrguxw93zpx6>

Email nog juist zetten voor Mike en Rocco

Stroom drive trenden. Zit al in log maar nog nakijken

M5_29 nog in productie testen.

Werkschakelaar van REM nog testen

(Dit kon niet omdat deze niet mag aanzetten vanwege inmetselen stenen)

Aanpassen vetberekening  

Settings from this moment on, until 180kg barrel is empty are:

cyclus 9min

14 pulses

Which means, every 9 minutes, 14 pulses have to be reached.

**=\> 60min/9min x 14pulses x 3outlets x 1.31cm³/outlet x 0.92g/cm³ = 337,45g/h (+334.8g/h)**

First step - 24 hours :

Quantity : 8 cm3/h of grease for each linear centimeter of crown.

Crown width : 36cm.

In this case must be pumped 288 cm3/h of grease type Ceplattyn KG10 or similar.

Specific weight of the grease : 0,92/0,94 gr/cm3

In this phase you need to pump 0,93x288 = 267,84 gr/h.

Running time : 24 hours.

Second step - 24 hours :

Quantity : 6 cm3/h of grease for each linear centimeter of crown.

Crown width : 36cm.

In this case must be pumped 216 cm3/h of grease type Ceplattyn KG10 or similar.

Specific weight of the grease : 0,92/0,94 gr/cm3

In this phase you need to pump 0,93x216 = 200,88 gr/h.

Running time : 24 hours.

Third step - 24 hours :

Quantity : 4 cm3/h of grease for each linear centimeter of crown.

Crown width : 36cm.

In this case must be pumped 144 cm3/h of grease type Ceplattyn KG10 or similar.

Specific weight of the grease : 0,92/0,94 gr/cm3

In this phase you need to pump 0,93x144 = 133,92 gr/h.

Running time : 24 hours.

Last step - for a lifetime :

Quantity : 2 cm3/h of grease for each linear centimeter of crown.

Crown width : 36cm.

In this case must be pumped 72 cm3/h of grease type Ceplattyn KG10 or similar.

Specific weight of the grease : 0,92/0,94 gr/cm3

In this phase you need to pump 0,93x72 = 66,96 gr/h.

Running time : for a lifetime.

Vergrendeling Filtersturing M5_7\_DI

Verwijder K_M5_1 en K_M5_2 uit advant. Let op. Worden mogelijk nog gebruikt

SEQ3_M5 verwijderen
