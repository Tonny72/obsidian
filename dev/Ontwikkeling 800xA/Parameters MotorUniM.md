---
created: [[2017-12-05]]T15:13:35.0000000+01:00
---

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 21%" />
<col style="width: 6%" />
<col style="width: 3%" />
<col style="width: 14%" />
<col style="width: 22%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th>Parameter in TMotor</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><del>Enable</del></td>
<td><del>bool</del></td>
<td><del>in</del></td>
<td><del>no</del></td>
<td><del>TRUE</del></td>
<td><del>IN Enables execution</del></td>
<td></td>
</tr>
<tr class="even">
<td>Name</td>
<td>string[30]</td>
<td>in</td>
<td>yes</td>
<td></td>
<td>IN EDIT Name of the object. Edit for alarm.</td>
<td>Name</td>
</tr>
<tr class="odd">
<td>Description</td>
<td>string[40]</td>
<td>in</td>
<td>no</td>
<td>'MotorUniM'</td>
<td>IN Object Description.</td>
<td>Description</td>
</tr>
<tr class="even">
<td>SetAuto</td>
<td>bool</td>
<td>in</td>
<td>no</td>
<td>default</td>
<td>IN Set to automode on positive edge</td>
<td>SetAuto</td>
</tr>
<tr class="odd">
<td>AutoMode</td>
<td>bool</td>
<td>out</td>
<td>no</td>
<td>default</td>
<td>OUT Indicates Auto mode</td>
<td><em>In Par</em></td>
</tr>
<tr class="even">
<td>ReadyToStart</td>
<td>bool</td>
<td>out</td>
<td>no</td>
<td>default</td>
<td>OUT Ready to start auto mode</td>
<td><em>In Par</em></td>
</tr>
<tr class="odd">
<td>AutoCmd1</td>
<td>bool</td>
<td>in</td>
<td>yes</td>
<td>default</td>
<td>IN Set output signal 1 (In AutoMode)</td>
<td><em>In AutoCmd_A</em></td>
</tr>
<tr class="even">
<td>AutoCmd0</td>
<td>bool</td>
<td>in</td>
<td>yes</td>
<td>default</td>
<td>IN Reset of output signals 1 and 2</td>
<td><em>In AutoCmd_A</em></td>
</tr>
<tr class="odd">
<td>ManMode</td>
<td>bool</td>
<td>out</td>
<td>no</td>
<td>default</td>
<td>OUT Indicates Manual mode</td>
<td><em>In Par</em></td>
</tr>
<tr class="even">
<td>ManModeInit</td>
<td>bool</td>
<td>in</td>
<td>no</td>
<td>TRUE</td>
<td>IN Init value for Manual/Auto mode at cold start</td>
<td>ManModeInit</td>
</tr>
<tr class="odd">
<td>PanExists</td>
<td>bool</td>
<td>in</td>
<td>no</td>
<td>TRUE</td>
<td>IN Informs that transfer to panel mode is possible</td>
<td>PanExists</td>
</tr>
<tr class="even">
<td>PanMode</td>
<td>bool</td>
<td>in</td>
<td>no</td>
<td>default</td>
<td>IN Indicates panel mode</td>
<td><em>In Par</em></td>
</tr>
<tr class="odd">
<td>PanCmd1</td>
<td>bool</td>
<td>in</td>
<td>no</td>
<td>default</td>
<td>IN Manual set of output signal 1 (In PanMode), (level signal with hold function)</td>
<td>PanCmd1</td>
</tr>
<tr class="even">
<td>PanCmd0</td>
<td>bool</td>
<td>in</td>
<td>no</td>
<td>default</td>
<td>IN Manual reset of output signals 1 and 2 (In PanMode)</td>
<td>PanCmd0</td>
</tr>
<tr class="odd">
<td><del>LocMode</del></td>
<td><del>bool</del></td>
<td><del>in</del></td>
<td><del>no</del></td>
<td><del>default</del></td>
<td><del>IN Indicates Local Mode</del></td>
<td></td>
</tr>
<tr class="even">
<td><del>GroupStartIn</del></td>
<td><del>GroupStartStepConnection</del></td>
<td><del>in</del></td>
<td><del>yes</del></td>
<td><del>default</del></td>
<td><del>IN NODE &lt;=&gt; Order of output 1 and feedback in GroupStart mode</del></td>
<td></td>
</tr>
<tr class="odd">
<td><del>GroupStartMode</del></td>
<td><del>bool</del></td>
<td><del>out</del></td>
<td><del>no</del></td>
<td><del>default</del></td>
<td><del>OUT Indicates GroupStart mode</del></td>
<td></td>
</tr>
<tr class="even">
<td><del>GroupStartILock</del></td>
<td><del>bool</del></td>
<td><del>in</del></td>
<td><del>no</del></td>
<td><del>default</del></td>
<td><del>IN Interlock transfer to GroupStart mode</del></td>
<td></td>
</tr>
<tr class="odd">
<td><del>ContinueStartSeq</del></td>
<td><del>bool</del></td>
<td><del>in_out</del></td>
<td><del>no left</del></td>
<td><del>TRUE</del></td>
<td><del>IN Feedback that the process object has started</del></td>
<td></td>
</tr>
<tr class="even">
<td><del>ContinueStartSeqTxt</del></td>
<td><del>string[40]</del></td>
<td><del>in</del></td>
<td><del>no</del></td>
<td><del>''</del></td>
<td><del>IN Info why the external started feedback not is present</del></td>
<td></td>
</tr>
<tr class="odd">
<td><del>ContinueStopSeq</del></td>
<td><del>bool</del></td>
<td><del>in</del></td>
<td><del>no</del></td>
<td><del>TRUE</del></td>
<td><del>IN Feedback that the process object has stopped</del></td>
<td></td>
</tr>
<tr class="even">
<td><del>ContinueStopSeqTxt</del></td>
<td><del>string[40]</del></td>
<td><del>in</del></td>
<td><del>no</del></td>
<td><del>''</del></td>
<td><del>IN Info why the external stopped feedback not is present</del></td>
<td></td>
</tr>
<tr class="odd">
<td><del>VoteOut</del></td>
<td><del>VoteConnection</del></td>
<td><del>out</del></td>
<td><del>yes</del></td>
<td><del>default</del></td>
<td><del>OUT NODE Output to vote objects</del></td>
<td></td>
</tr>
<tr class="even">
<td><del>VotedCmd</del></td>
<td><del>VotedConnection</del></td>
<td><del>in</del></td>
<td><del>yes</del></td>
<td><del>default</del></td>
<td><del>IN NODE Input from voting logic</del></td>
<td></td>
</tr>
<tr class="odd">
<td><del>PriorityCmdMan1Config</del></td>
<td><del>dword</del></td>
<td><del>in</del></td>
<td><del>no</del></td>
<td><del>0</del></td>
<td><del>IN Specify which Voted Command number(s) to set PriorityCmdMan1 Bit number=Command number. (1-16#FFFFFFFF, else 1 + ParError)</del></td>
<td></td>
</tr>
<tr class="even">
<td><del>PriorityCmdMan0Config</del></td>
<td><del>dword</del></td>
<td><del>in</del></td>
<td><del>no</del></td>
<td><del>0</del></td>
<td><del>IN Specify which Voted Command number(s) to set PriorityCmdMan0 Bit number=Command number. (1-16#FFFFFFFF, else 1 + ParError)</del></td>
<td></td>
</tr>
<tr class="odd">
<td><del>PriorityCmd1Config</del></td>
<td><del>dword</del></td>
<td><del>in</del></td>
<td><del>no</del></td>
<td><del>0</del></td>
<td><del>IN Specify which Voted Command number(s) to set PriorityCmd1 Bit number=Command number. (1-16#FFFFFFFF, else 1 + ParError)</del></td>
<td></td>
</tr>
<tr class="even">
<td><del>PriorityCmd0Config</del></td>
<td><del>dword</del></td>
<td><del>in</del></td>
<td><del>no</del></td>
<td><del>0</del></td>
<td><del>IN Specify which Voted Command number(s) to set PriorityCmd0 Bit number=Command number. (1-16#FFFFFFFF, else 1 + ParError)</del></td>
<td></td>
</tr>
<tr class="odd">
<td><del>ILock1Config</del></td>
<td><del>dword</del></td>
<td><del>in</del></td>
<td><del>no</del></td>
<td><del>0</del></td>
<td><del>IN Specify which Voted Command number(s) to set ILock1 Bit number=Command number. (1-16#FFFFFFFF, else 1 + ParError)</del></td>
<td></td>
</tr>
<tr class="even">
<td><del>ILock0Config</del></td>
<td><del>dword</del></td>
<td><del>in</del></td>
<td><del>no</del></td>
<td><del>0</del></td>
<td><del>IN Specify which Voted Command number(s) to set ILock0 Bit number=Command number. (1-16#FFFFFFFF, else 1 + ParError)</del></td>
<td></td>
</tr>
<tr class="odd">
<td>PriorityMode</td>
<td>bool</td>
<td>out</td>
<td>no</td>
<td>default</td>
<td>OUT PriorityMode</td>
<td></td>
</tr>
<tr class="even">
<td>PriorityCmd1</td>
<td>bool</td>
<td>in</td>
<td>no</td>
<td>default</td>
<td>IN Forcing of object to position 1</td>
<td></td>
</tr>
<tr class="odd">
<td>PriorityCmd01</td>
<td>bool</td>
<td>in</td>
<td>no</td>
<td>default</td>
<td>IN Forcing of object to position 0, condition 1 with alarm and hold function</td>
<td></td>
</tr>
<tr class="even">
<td>PriorityCmd02</td>
<td>bool</td>
<td>in</td>
<td>no</td>
<td>default</td>
<td>IN Forcing of object to position 0, condition 2 with alarm and hold function</td>
<td></td>
</tr>
<tr class="odd">
<td>PriorityCmd02Txt</td>
<td>string</td>
<td>in</td>
<td>no</td>
<td>'PriorityCmd 02'</td>
<td>IN Text for PriorityCmd02</td>
<td></td>
</tr>
<tr class="even">
<td>PriorityCmd03</td>
<td>bool</td>
<td>in</td>
<td>no</td>
<td>default</td>
<td>IN Forcing of object to position 0, condition 3 with alarm and hold function</td>
<td></td>
</tr>
<tr class="odd">
<td>PriorityCmd03Txt</td>
<td>string</td>
<td>in</td>
<td>no</td>
<td>'PriorityCmd 03'</td>
<td>IN Text for PriorityCmd03</td>
<td></td>
</tr>
<tr class="even">
<td>PriorityCmdMan1</td>
<td>bool</td>
<td>in</td>
<td>no</td>
<td>default</td>
<td>IN Forcing of object to position 1 and switch to manual mode</td>
<td></td>
</tr>
<tr class="odd">
<td>PriorityCmdMan0</td>
<td>bool</td>
<td>in</td>
<td>no</td>
<td>default</td>
<td>IN Forcing of object to position 0 and switch to manual mode</td>
<td></td>
</tr>
<tr class="even">
<td>PriorityCmdMan0Txt</td>
<td>string</td>
<td>in</td>
<td>no</td>
<td>'PriorityCmdMan 0'</td>
<td>IN Text for PriorityCmdMan0</td>
<td></td>
</tr>
<tr class="odd">
<td>OutOfServiceMode</td>
<td>bool</td>
<td>out</td>
<td>no</td>
<td>default</td>
<td>OUT Indicates Out of Service mode</td>
<td><em>In Par</em></td>
</tr>
<tr class="even">
<td>Ilock11</td>
<td>bool</td>
<td>in</td>
<td>no</td>
<td>default</td>
<td>IN Interlocks changes from state 0 to state 1 Note! ILock11 and ILock12 are identical</td>
<td>ILock1</td>
</tr>
<tr class="odd">
<td><del>Ilock12</del></td>
<td><del>bool</del></td>
<td><del>in</del></td>
<td><del>no</del></td>
<td><del>default</del></td>
<td><del>IN Interlocks changes from state 0 to state 1 Note! ILock11 and ILock12 are identical</del></td>
<td></td>
</tr>
<tr class="even">
<td>Ilock01</td>
<td>bool</td>
<td>in</td>
<td>no</td>
<td>default</td>
<td>IN Interlocks changes from state 1 to state 0 Note! ILock01 and ILock02 are identical</td>
<td>ILock0</td>
</tr>
<tr class="odd">
<td><del>Ilock02</del></td>
<td><del>bool</del></td>
<td><del>in</del></td>
<td><del>no</del></td>
<td><del>default</del></td>
<td><del>IN Interlocks changes from state 1 to state 0 Note! ILock01 and ILock02 are identical</del></td>
<td></td>
</tr>
<tr class="even">
<td>Inhibit</td>
<td>bool</td>
<td>in</td>
<td>no</td>
<td>default</td>
<td>IN Inhibition of all Ilock and PriorityCmd signals</td>
<td></td>
</tr>
<tr class="odd">
<td>ObjectTest</td>
<td>bool</td>
<td>in</td>
<td>no</td>
<td>default</td>
<td>IN Set to object test</td>
<td>Via Faceplate</td>
</tr>
<tr class="even">
<td>StatAct</td>
<td>bool</td>
<td>out</td>
<td>no</td>
<td>default</td>
<td>OUT Object Status: pos.1 activated. To application program</td>
<td><em>In Par</em></td>
</tr>
<tr class="odd">
<td>StatDeact</td>
<td>bool</td>
<td>out</td>
<td>no</td>
<td>default</td>
<td>OUT Object Status: deactivated. To application program</td>
<td><em>In Par</em></td>
</tr>
<tr class="even">
<td>FBConfig</td>
<td>dint</td>
<td>in</td>
<td>no</td>
<td>1</td>
<td>IN Feedback conf. 0:FB1,FB0 1:FB1 2:FB1' 3:FB1',FB0' 4:FB0 5:FB0' 6:No FB, else FB1,FB0 + ParError</td>
<td><p>FBConfig</p>
<p></p></td>
</tr>
<tr class="odd">
<td>FB1</td>
<td>BoolIO</td>
<td>in_out</td>
<td>yes left</td>
<td>default</td>
<td>IN Feedback from activated position 1</td>
<td>IO</td>
</tr>
<tr class="even">
<td><del>FB0</del></td>
<td><del>BoolIO</del></td>
<td><del>in_out</del></td>
<td><del>yes left</del></td>
<td><del>default</del></td>
<td><del>IN Feedback from deactivated position</del></td>
<td></td>
</tr>
<tr class="odd">
<td>Out1</td>
<td>BoolIO</td>
<td>out</td>
<td>yes</td>
<td>default</td>
<td>OUT Output signal to IO for object activation 1</td>
<td>IO</td>
</tr>
<tr class="even">
<td><del>Out0</del></td>
<td><del>BoolIO</del></td>
<td><del>out</del></td>
<td><del>yes</del></td>
<td><del>default</del></td>
<td><del>OUT Output signal to IO for object deactivation</del></td>
<td></td>
</tr>
<tr class="odd">
<td><del>CondNameObjectError</del></td>
<td><del>string[15]</del></td>
<td><del>in</del></td>
<td><del>no</del></td>
<td><del>'||SL_OE'</del></td>
<td><del>IN EDIT Name of the condition for Object error</del></td>
<td></td>
</tr>
<tr class="even">
<td>AlarmDisabled</td>
<td>bool</td>
<td>out</td>
<td>no</td>
<td>default</td>
<td>OUT Object error alarm disabled</td>
<td></td>
</tr>
<tr class="odd">
<td>ObjErrEnabled</td>
<td>bool</td>
<td>out</td>
<td>no</td>
<td>default</td>
<td>OUT True when InteractionPar.EnableObjErr and EnableObjErr are true</td>
<td></td>
</tr>
<tr class="even">
<td><del>ExtErr</del></td>
<td><del>bool</del></td>
<td><del>in</del></td>
<td><del>no</del></td>
<td><del>default</del></td>
<td><del>IN External error signal</del></td>
<td></td>
</tr>
<tr class="odd">
<td>ObjErr</td>
<td>bool</td>
<td>out</td>
<td>no</td>
<td>default</td>
<td>OUT Object error generated</td>
<td></td>
</tr>
<tr class="even">
<td>ObjErrStat</td>
<td>bool</td>
<td>out</td>
<td>no</td>
<td>default</td>
<td>OUT Indicates active condition ObjErr. This output can be controlled via Enable.</td>
<td></td>
</tr>
<tr class="odd">
<td>AlState</td>
<td>dint</td>
<td>out</td>
<td>no</td>
<td>default</td>
<td>OUT NONSIL Alarm Status (1:Inh 2:Inact 3:Not ack'ed and inact 4:Ack'ed and act 5:Not ack'ed and act 6:Auto-inh)</td>
<td></td>
</tr>
<tr class="even">
<td>AlarmAck</td>
<td>bool</td>
<td>in</td>
<td>no</td>
<td>default</td>
<td>IN Alarm acknowledge</td>
<td></td>
</tr>
<tr class="odd">
<td>AEConfig</td>
<td>dint</td>
<td>in</td>
<td>no</td>
<td>1</td>
<td>IN AEConfig (0=None, 1=Alarm, 2=Event, 3=Event1, 4=Indication, else Alarm + ParError)</td>
<td></td>
</tr>
<tr class="even">
<td>AESeverity</td>
<td>dint</td>
<td>in</td>
<td>no</td>
<td>600</td>
<td>IN Alarm severity. Range 1 - 1000 else ParError + (Alarms: Prev valid value used else no alarm created; Events: No event generated).</td>
<td></td>
</tr>
<tr class="odd">
<td>AEClass</td>
<td>dint</td>
<td>in</td>
<td>no</td>
<td>1</td>
<td>IN Class for alarm/event. Range 1 - 9999 else ParError + (Alarms: Prev valid value used else no alarm created; Events: No event generated).</td>
<td></td>
</tr>
<tr class="even">
<td>AEError</td>
<td>bool</td>
<td>out</td>
<td>no</td>
<td>default</td>
<td>OUT NONSIL Used to indicate alarm/event error</td>
<td></td>
</tr>
<tr class="odd">
<td>EnableObjErr</td>
<td>bool</td>
<td>in</td>
<td>no</td>
<td>TRUE</td>
<td>IN Enables object error indication</td>
<td></td>
</tr>
<tr class="even">
<td>EnableSupOut</td>
<td>bool</td>
<td>in</td>
<td>no</td>
<td>TRUE</td>
<td>IN When false, out parameter ObjErr is is controlled by InteractionPar.EnableObjErr</td>
<td></td>
</tr>
<tr class="odd">
<td><del>MotorValue</del></td>
<td><del>RealIO</del></td>
<td><del>in_out</del></td>
<td><del>yes left</del></td>
<td><del>default</del></td>
<td><del>IN A characteristic measured value for the object</del></td>
<td></td>
</tr>
<tr class="even">
<td><del>MotorValueTxt</del></td>
<td><del>string</del></td>
<td><del>in</del></td>
<td><del>no</del></td>
<td><del>'MotorValue'</del></td>
<td><del>IN Text for MotorValue</del></td>
<td></td>
</tr>
<tr class="odd">
<td>EnableParError</td>
<td>bool</td>
<td>in</td>
<td>no</td>
<td>FALSE</td>
<td>EDIT Enables ParError calculation for non-SIL applications, always enabled in SIL applications</td>
<td></td>
</tr>
<tr class="even">
<td>ParError</td>
<td>bool</td>
<td>out</td>
<td>yes</td>
<td>default</td>
<td>OUT Indicates parameter range error.</td>
<td></td>
</tr>
<tr class="odd">
<td>InteractionPar</td>
<td>MotorUniPar</td>
<td>in_out</td>
<td>no left</td>
<td>default</td>
<td>IN Interaction parameter</td>
<td></td>
</tr>
</tbody>
</table>
