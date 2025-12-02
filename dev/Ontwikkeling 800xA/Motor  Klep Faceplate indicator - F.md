---
title: Motor / Klep Faceplate indicator - Forced/Interloc...
updated: [[2017-12-05]]T14:05:29.0000000+01:00
created: [[2017-12-05]]T12:03:47.0000000+01:00
---

- # MOTOR
- #
- # Expression
  iif (\$'.:Control Module:Forced',1,iif (\$'.:Control Module:Interlock',2,0))
- # Icons
  ![image1](image1-72.png)
- # KLEP
- #
- # Expression
  iif (\$'.:Control Module:Forced',1,iif (\$'.:Control Module:Interlock',2,0))
- # Icons
  ![image2](image2-42.png)