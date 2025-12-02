---
title: TSFCInteraction
date modified: 2025-09-18T22:08:48+02:00
tags: [800xA, dev]
date created: 2018-09-12T08:39:00+02:00
---
## Parameters  
| Name          | string\[20\]      | in     | yes      |               | Object name                                            |
| ------------- | ----------------- | ------ | -------- | ------------- | ------------------------------------------------------ |
| Description   | string\[40\]      | in     | yes      | 'Description' | Object Description                                     |
| AutoStart     | bool              | in     | yes      | FALSE         | IN On command in automatic mode                        |
| AutoHold      | bool              | in     | yes      | FALSE         | IN Stop command in automatic mode                      |
| AutoRes       | bool              | in     | yes      | FALSE         | IN Reset command in automatic mode ( Edge_detection)   |
| AutoRestart   | bool              | in     | yes      | default       | IN Restart sequence in automatic mode (Edge detection) |
| AutoStop      | bool              | in     | yes      | FALSE         | IN Off command in automatic mode                       |
| EnManCmds     | bool              | in     | yes      | TRUE          | Enable Manual command buttons                          |
| EnDoorstappen | bool              | in     | yes      | default       | Enable Doorstappen                                     |
| EnRestart     | bool              | in     | yes      | default       | Enable Restart                                         |
| EnRuntimeErr  | bool              | in     | yes      | default       | Enable Runtime error alarm                             |
| EnEvents      | bool              | in     | no       | TRUE          | Enable Events                                          |
| ILockOn       | bool              | in     | yes      | FALSE         | IN Interlock On                                        |
| ILockStop     | bool              | in     | yes      | FALSE         | IN Interlock Stop                                      |
| ILockOff      | bool              | in     | yes      | FALSE         | IN Interlock Off                                       |
| Par           | TSFC_Par          | out    | yes      | default       | SFC Parameters connect to application                  |
| SFCHeader     | SeqListAttributes | in_out | yes left | default       | Connect with SFC                                       |
| AEClass       | dint              | in     | yes      | 1             |                                                        |
