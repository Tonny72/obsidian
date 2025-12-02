---
created: [[2017-12-05]]T14:08:03.0000000+01:00
tags:
  - 800xA
---

![image1](image1-79.png)

- # SetMan
  iif (\$'.:Control Module:ObjMode' =4 or \$'.:Control Module:ObjMode' =5 or \$'.:Control Module:ObjMode' =6 or \$'.:Control Module:ObjModeHold' =4,1,0)
- # SetAuto
  iif( (\$'.:Control Module:ObjMode' = 3 or \$'.:Control Module:ObjMode' = 5 or \$'.:Control Module:ObjMode' = 6) or \$'.:Control Module:ObjModeHold' =3,1,0)
- # ManCmd0
  iif ( \$'.:Control Module:ManMode' AND \$'.:Control Module:Out1Level' AND NOT \$'.:Control Module:ILock0',1,0)
- # ManCmd1
  iif (NOT \$'.:Control Module:Out1Level' AND \$'.:Control Module:ManMode' AND NOT \$'.:Control Module:ILock1',1,0)
- # SetOutOfService
  iif (NOT \$'.:Control Module:Out1Indication' AND NOT \$'.:Control Module:OutOfServiceMode' AND NOT \$'.:Control Module:PriorityMode',1,0)