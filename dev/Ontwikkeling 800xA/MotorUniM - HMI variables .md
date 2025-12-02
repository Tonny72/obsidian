---
title: 'MotorUniM - HMI variables '
updated: [[2017-12-06]]T11:59:42.0000000+01:00
created: [[2017-12-06]]T07:57:57.0000000+01:00
---

MotorUniM - HMI variables
woensdag 6 december 2017
7:57

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 6%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th>AnyAction</th>
<th>bool</th>
<th><p>![image1](../../../../../resources/image1-82.png)</p>
<p>AnyAction := DetectOverride.EffectivePriorityCmd0 or DetectOverride.EffectivePriorityCmd1</p>
<p>or DetectOverride.EffectivePriorityCmdMan0 or DetectOverride.EffectivePriorityCmdMan1</p>
<p>or DetectOverride.EffectiveILock0 or DetectOverride.EffectiveILock1;</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AnyDisablingInhibiting</td>
<td>bool</td>
<td><p>![image2](../../../../../resources/image2-49.png)</p>
<p>AnyDisablingInhibiting := AlarmDisabledInternal and AEConfig &lt;&gt; 0;</p></td>
</tr>
<tr class="even">
<td>EffectiveFB1</td>
<td>bool</td>
<td><p>![image3](../../../../../resources/image3-26.png)</p>
<p>Core. EffectiveFB1 =&gt; EffectiveFB1,</p></td>
</tr>
<tr class="odd">
<td>Forced</td>
<td>bool</td>
<td><p>![image4](../../../../../resources/image4-22.png)</p>
<p>Core.Forced =&gt; Forced</p></td>
</tr>
<tr class="even">
<td>LocMode</td>
<td>bool</td>
<td><p>![image5](../../../../../resources/image5-18.png)</p>
<p>Parameter</p></td>
</tr>
<tr class="odd">
<td>ManMode</td>
<td>bool</td>
<td><p>![image6](../../../../../resources/image6-15.png)</p>
<p>ManMode := ManModeInternal;</p></td>
</tr>
<tr class="even">
<td>ParError</td>
<td>bool</td>
<td><p>![image7](../../../../../resources/image7-8.png)</p>
<p></p></td>
</tr>
<tr class="odd">
<td>Status</td>
<td>dint</td>
<td><p>![image8](../../../../../resources/image8-7.png)</p>
<p></p></td>
</tr>
<tr class="even">
<td>HoldsData</td>
<td>bool</td>
<td><p>![image9](../../../../../resources/image9-6.png)</p>
<p></p></td>
</tr>
</tbody>
</table>
