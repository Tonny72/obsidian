---
title: Motor / Klep Faceplate indicator - AEConfig/ObjErr...
updated: [[2017-12-05]]T14:03:13.0000000+01:00
created: [[2017-12-05]]T12:09:15.0000000+01:00
---

- # MOTOR
- # Expression
  iif(\$'.:Control Module:AEConfig' \<\> 0 and not \$'.:Control Module:ObjErrEnabled',0,iif(\$'.:Control Module:Inhibit',2,1))
- # Icons
  ![image1](image1-74.png)
- # KLEP
- # Expression
  iif(\$'.:Control Module:AEConfig' \<\> 0 and not \$'.:Control Module:ObjErrEnabled',0,1)
- # Icons
  ![image2](image2-44.png)