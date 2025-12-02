---
created: [[2017-12-05]]T12:15:53
tags:
  - 800xA
  - dev
---

![image1](image1-77.png)

- # SetMan
  iif (\$'.:Control Module:ObjMode' =4 or \$'.:Control Module:ObjMode' =5 or \$'.:Control Module:ObjMode' =6 or \$'.:Control Module:ObjModeHold' =4 ,1,0)
- # SetAuto
  iif ((\$'.:Control Module:ObjMode' =3 or \$'.:Control Module:ObjMode' =5 or \$'.:Control Module:ObjMode' = 6 or \$'.:Control Module:ObjModeHold' =3 ),1,0)
- # ManCmd0
  iif (NOT \$'.:Control Module:StatDeact' AND (\$'.:Control Module:ManMode' ),1,0)
- # ManCmd1
  iif (NOT \$'.:Control Module:StatAct' AND \$'.:Control Module:ManMode' AND (NOT \$'.:Control Module:ILock11' AND NOT \$'.:Control Module:ILock12' AND NOT \$'.:Control Module:ILock1Loc' OR \$'.:Control Module:Inhibit'),1,0)
- # SetGroupStart
  iif (\$'.:Control Module:GroupStartUsed' and (\$'.:Control Module:ObjMode' =3 or \$'.:Control Module:ObjMode' =4 or \$'.:Control Module:ObjMode' =6),1,0)
- # SetOutOfService
  iif (\$'.:Control Module:Out0Indication' AND NOT \$'.:Control Module:OutOfServiceMode' AND NOT \$'.:Control Module:PanMode' AND NOT \$'.:Control Module:PriorityMode',1,0)
- # OpPanelMode
  iif(not (\$'.:Control Module:PanMode' OR \$'.:Control Module:OutOfServiceMode' OR \$'.:Control Module:PriorityMode') and not \$'.:Control Module:PanModeAct', 1,0)
- # NOT OpPanelMode
  iif(not (\$'.:Control Module:PanMode' OR \$'.:Control Module:OutOfServiceMode' OR \$'.:Control Module:PriorityMode') and \$'.:Control Module:PanModeAct', 1,0)