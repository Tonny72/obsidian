---
date created: 2010-10-21
date modified: 2025-07-21
---
# AlarmConditionstate

> AlarmConditionstate

1.  **Alarm Parameters.**
The following parameters are used in alarms and events.

**Alarm Levels.** The alarm level can be initially set in the flat parameters AELevelxxx (IN INIT), which is an initialization parameter. The InteractionPar.AExxx.Level is then maintained either from application logic or from the faceplate.

**Alarm Properties.** There are two systems that report the current evaluation of an alarm. **Alarm Condition** is mainly based in the controller code (in Control BuilderM), but can be read by aspects in the PPA system. **Alarm State** is based in the supervisory alarm system in PPA and is not normally available to the controller code.

Although in many cases either system can be used to evaluate the alarm indication, the values used in each are not the same for most conditions and the two systems should not be confused.

**Alarm Condition.** An alarm can be in one of the following conditions in the CBM parameters AlarmCond, OECond etc. Condition 0 is rarely seen.

| **Alarm Condition** | **Alarm activity**                       |
|---------------------|------------------------------------------|
| 0                   | Not defined                              |
| 1                   | Disabled                                 |
| 2                   | Inactive, Acknowledged and Enabled       |
| 3                   | Inactive, Unacknowledged and Enabled     |
| 4                   | Active, Acknowledged and Enabled         |
| 5                   | Active, Unacknowledged and Enabled       |
| 6                   | AutoDisabled, Unacknowledged and Enabled |
******

**Alarm State.** An alarm can be in one or two of the following states. These are the values of state properties which correspond to the PPA AlarmList:AlarmState in all system versions and also to AlarmConditionState and AlarmConditionState_Descendants in SV4.1 and later. Note that each state corresponds to a bit being set in the binary word.
| **Alarm activity**      | **Alarm State (Alarm List or Global)** |       |                |
|-------------------------|----------------------------------------|--------|-----------------|
|                        | Integer                                | 16#Hex | 2#Binary (bits) |
| AlarmInActive           | 0                                      | 0x00   | 00000000        |
| AlarmDisabled           | 1                                      | 0x01   | 00000001        |
| AlarmActiveAck          | 2                                      | 0x02   | 00000010        |
| AlarmInActiveUnAck      | 4                                      | 0x04   | 00000100        |
| AlarmActiveUnAck        | 8                                      | 0x08   | 00001000        |
| AlarmAutoDisabled       | 16                                     | 0x10   | 00010000        |
| AlarmActiveAckHidden    | 32                                     | 0x20   | 00100000        |
| AlarmActiveUnAckHidden  | 64                                     | 0x40   | 01000000        |
| AlarmAutoDisabledHidden | 128                                    | 0x80   | 10000000        |

Theoretically an alarm can have more than one of the above states, though only a few pairings are likely. Known examples are:

- With the Disabled state. Eg. If an Active, unacknowledged alarm is disabled it will become an Inactive, unacknowledged alarm. Both AlarmInActiveUnAck and AlarmDisabled will now be set; therefore the State will be 4+1 = 5.
- When an alarm has been active, then inactive and then goes active again, without being acknowleged at any point, both AlarmActiveUnAck and AlarmInActiveUnAck will be true; therefore the State will be 8+4 = 12.
- When an alarm has been active, then inactive three times without being acknowleged at any point, it becomes AutoDisabled. In this State both AlarmAutoDisabled and AlarmInActiveUnAck will be true; therefore State will be 16+4 = 20. ***Note.*** This State is maintained until the alarm is acknowleged regardless of whether the alarm switches between inactive and active.
  The presentation of the alarm in the alarm list reflects the current state. Each state change is also recorded in the event list.
  
  The Graphic Element colors used for the display of alarm states on the graphic element status indicator square 1 and on the graphic element icon body are as follows:
  | **Alarm State**                 | **Status Indicator 1 / Icon color**    | **Logical Color**         | **Color defined in**    |
  |---------------------------------|----------------------------------------|---------------------------|-------------------------|
  | Inactive, Acknowledged (Normal) | Background / Based on device feedbacks | GeneralBackColor          | Process Graphics Colors |
  | Disabled                        | Background / Based on device feedbacks | GeneralBackColor          | Process Graphics Colors |
  | Active, Acknowledged            | Red                                    | AlarmIndicationColor      | AC 800M/C Colors        |
  | Inactive, Unacknowledged        | Yellow flashing                        | unackLowAlarm             | Event Colors            |
  | Active, Unacknowledged          | Red flashing                           | AlarmIndicationUnAckColor | AC 800M/C Colors        |
  | AutoDisabled, Unacknowledged    | Red flashing                           | AlarmIndicationUnAckColor | AC 800M/C Colors        |
  | Hidden, Active, Acknowledged    | Background / Based on device feedbacks | GeneralBackColor          | Process Graphics Colors |
  | Hidden, Active, Unacknowledged  | Background / Based on device feedbacks | GeneralBackColor          | Process Graphics Colors |
  ****
  
  **Alarm Enable.** The alarms are provided with a check box to enable/disable the alarm on the faceplate Alarm/Event tab. This is intended to be used during normal operation if an alarm needs to be temporarily disabled because of a mechanical or electrical fault, for example a valve position feedback switch is faulty and is causing a large number of nuisance alarms, or a sequence can not proceed, etc. The alarm enable box should be normally left ticked. ***Note***. The check box should not be unticked for alarms that are not required. The DigitalInput and Transmitter/4L can also be put into forced mode from the faceplate in order to stop the alarms.
  
  ***Note***. If the box is unticked to disable the alarm from the HSI, then square six in the graphic element status indicator display will indicate that an inhibit/disable from the HSI has been set. If the alarm is disabled then the previous value of the alarm setting is still shown on the faceplate Parameters tab.
  
  Alarms can also be enabled/disabled from their entry in an Alarm List by use of the context menu, right click on the line in the Alarm List. When disabled, the line in the Alarm List is then shown with strikethrough.
  
  ***Caution.*** The alarm disable from the alarm list line does not change the Alarm Control triangle presentation.
  
  ***Caution.*** If an alarm/event is not required at all then it is recommended to set the AEConf to 0. The Enable/Disable check box and the value of the alarm level are then not shown on the faceplate.
  
  ***Note***. The check box should not be unticked for alarms that are not required, the AE should still be enabled. If the AEConf has a value not = 0 and then the alarm is not required, it is necessary to tick the enable check box before AEConf is set = 0, otherwise the check box is no longer visible and can not be ticked again.
  
  **AEConf.** Alarms and events can be individually configured from a set of permutations. The AEConfxxx options, where xxx is the name of the alarm/event, are:-
  
  0\. No alarm, no event, status is always false.
  1.  Alarm on condition going abnormal, events on going abnormal and returning to normal, status is true or false.
  2\. No alarm, events on going abnormal and returning to normal, status is true or false.
  
  3\. No alarm, event on going abnormal, status is true or false.
  
  4\. No alarm, no events, status is true or false.
  
  **AE.Stat.** The status is a boolean output indicating the status of the alarm/event flag inside the device. ***Note.*** The AE.Stat is used to set the Outgoing PCC command to Execute.
  
  **AlarmAck.** The alarm acknowledge is for the common acknowledgement of all alarms on a device from a Process Panel. Alarms can be acknowledged individually from the object faceplate, or from the object alarm list or from common alarm lists.
  
  **AEClass.** AEClass (process section or process unit) for all of the alarms on a device. The value can be changed in runtime, and are not IN EDIT parameters. The allowable range is 1 to 9999. Entry of an invalid value sets the ParError to true on SIL2 marked devices.
  
  **AESev.** All alarms can be independently assigned a severity (importance) level AESevxxx. The value can be changed in runtime, and are not IN EDIT parameters. The allowable range is 1 to 1000. Entry of an invalid value sets the ParError to true on SIL2 marked devices. The 800xA PPA alarm and event system utilizes a maximum of 32 Alarm Priority Levels and a number of colors are used to present different Alarm Severity and Priority Levels. PCDeviceLib initial values for Severity are set with project constants, and these need to be set for each project.
  
  **ExtErr.** The external error alarm allows connection of an external error input, for example from a common shutdown system for a process section or unit, equipment module, external vibration monitoring system, tripped digital input signal from a motor control center etc. The ExtErr is connected to the device OE ObjectError alarm, this means that if ExtErr is true, the AEOE is raised. ***Caution***. This might stop a Motor, depending on the value of OELatchConf.
  
  **OE ObjectError.** The OE object error alarm is intended to alert the Operator to a hardware or electrical fault. For example, an input is bad data quality. For example, a consistency (discrepancy) check error such as a Valve with two feedbacks showing that the Valve is both fully opened and fully closed at the same time. For example, Feedbacks fail to confirm that the Valve is fully open, after a preset tunable time, following a command to open. The OE alarm can be enabled and disabled from the faceplates and/or from the application logic. ***Note.*** The AEConfOE should not be set = 0.
  
  When a device Object Error is raised that indicates a mechanical or electrical fault, then further information about the reason for the alarm is included on the faceplate Alarm/Event tab in the Error cause faceplate element. This element is dynamic and indications appear in accordance with the device configuration options. For example, the potential error fault for a feedback is not shown if the feedback is not configured. If the FBLoc (feedback from the field mounted Local switch) is bad data quality, this is shown in the I/O tab on the faceplate and not as a cause on the A/E tab.
  
  ***Note.*** OE for Motors can be configured to stop , or not to stop the motor, refer to sections below on Motors and OELatchConf. OE for valves do not close the valves.
  
  **InhPriCmd.** The InhibitPriCmd, inhibit priority command alarm/event, is active if an incoming pcc command is activated and the device incoming Priority Commands and Interlocks are also simultaneously Inhibited. This advises the operator that the device has not acted on the incoming pcc command (because of the Inhibit). This alarm is always enabled, but would not be active if there are no incoming pcc commands connected to the device.
  
  **PriCmdOE.** The PriorityCommandOE, priority command object error alarm/event, is active if an incoming pcc command is activated and the device ObjectError is also simultaneously active. This advises the operator that the device may not have acted on the incoming pcc command (because the device object error is active). This alarm is always enabled, but would not be active if there are no connections to the pcc commands for the device.
  
  **Digital Alarms.** The DigitalInput, BoolInput and pccBoolToPCC (boolean) input devices have an optional event to indicate a change of state, either going active or deactivated.
  
  **Analogue Alarms.** The Transmitter has six optional alarms/events (HHH, HH, H and L, LL, LLL). The Transmitter4L has four optional alarms/events (HH, H and L, LL). They have AlarmCondM control modules and do not use the standard Level6CC control module. They also have optional high and low rate of change alarms.
  
  ***Caution.*** The control module CBM code checks whether the value entered for the alarm limit, AELevelxxx is within the engineering units range IO.Parameters.Max and IO.Parameters.Min. If an entry outside this range is entered from CBM, or by application logic, then the alarm limit will be set to the Min for a high alarm and the Max for a low alarm, and therefore the alarm will always be active. The Parameter Error is also set to true. This functionality is for SIL2 compliance. The operator is prevented from entering erroneous values from the faceplate.
  
  ***Caution.*** If it is necessary to change the engineering units range on a device, then it is essential to move any alarm limits to within the new range before changing the engineering units. For example a flow transmitter has a range 0 to 7250 Nm3/h, and a high alarm level of 6750. It has been decided to rerange the instrument because the density of the gas has changed, to 0 to 6500 and to change the high alarm level to 6250. It is necessary to move the alarm to 6250 before the range is reduced from 7250 to 6500, because the alarm was set at 6750, ie above 6500.
  
  **AlarmCondM.SrcName** \[30\]. The parent CM instance Source Name is used.
  
  **AlarmCondM.CondName** \[15\]. Blank, refer to Condition.
  
  **AlarmCondM.Message** \[60\]. A project constant is used as the initial value. Refer to AEMsgDiff \[30\] parameter description.
  
  **SimpleEventDetector.SrcName** \[30\]. The parent CM instance Source Name is used.
  
  **SimpleEventDetector.Message** \[70\]. A project constant is used as the initial value, or is copied from the associated AlarmCondM. Refer to AEMsgDiff \[30\] parameter description