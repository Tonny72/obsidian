---
title: Motor / Klep Faceplate indicator - Mode
updated: [[2017-12-05]]T14:22:59.0000000+01:00
created: [[2017-12-05]]T12:01:38.0000000+01:00
---

- # MOTOR
- #
- # Expression
  iif (\$'.:Control Module:ParError',
  iif (\$'.:Control Module:LocMode',18,
  iif (\$'.:Control Module:OutOfServiceMode',21,
  iif (\$'.:Control Module:PanModeAct',17,
  iif (\$'.:Control Module:ManMode',15,
  iif (\$'.:Control Module:AutoMode',16,
  iif (\$'.:Control Module:PriorityMode',19,
  iif (\$'.:Control Module:GroupStartMode',20,
  22
  )
  )
  )
  )))),
  iif (\$'.:Control Module:Status' & 0xB80000,
  iif (\$'.:Control Module:LocMode',4,
  iif (\$'.:Control Module:OutOfServiceMode',7,
  iif (\$'.:Control Module:PanModeAct',3,
  iif (\$'.:Control Module:ManMode',1,
  iif (\$'.:Control Module:AutoMode',2,
  iif (\$'.:Control Module:PriorityMode',5,
  iif (\$'.:Control Module:GroupStartMode',6,0))))))),
  iif (\$'.:Control Module:LocMode',11,
  iif (\$'.:Control Module:OutOfServiceMode',14,
  iif (\$'.:Control Module:PanModeAct',10,
  iif (\$'.:Control Module:ManMode',8,
  iif (\$'.:Control Module:AutoMode',9,
  iif (\$'.:Control Module:PriorityMode',12,
  iif (\$'.:Control Module:GroupStartMode',13,0)))))))))
- # Icons
  ![image1](image1-71.png)
- # KLEP
- #
- # Expression
  iif (\$'.:Control Module:ParError',
  iif (\$'.:Control Module:OutOfServiceMode',15,
  iif (\$'.:Control Module:ManMode',11,
  iif (\$'.:Control Module:AutoMode',12,
  iif (\$'.:Control Module:PriorityMode',13,
  iif (\$'.:Control Module:GroupStartMode',14,16))))),
  iif (\$'.:Control Module:Status' & 0xB80000,
  iif (\$'.:Control Module:OutOfServiceMode',5,
  iif (\$'.:Control Module:ManMode',1,
  iif (\$'.:Control Module:AutoMode',2,
  iif (\$'.:Control Module:PriorityMode',3,
  iif (\$'.:Control Module:GroupStartMode',4,0))))),
  iif (\$'.:Control Module:OutOfServiceMode',10,
  iif (\$'.:Control Module:ManMode',6,
  iif (\$'.:Control Module:AutoMode',7,
  iif (\$'.:Control Module:PriorityMode',8,
  iif (\$'.:Control Module:GroupStartMode',9,0)))))))
- #
- #
- #
- # Icons
  ![image2](image2-41.png)