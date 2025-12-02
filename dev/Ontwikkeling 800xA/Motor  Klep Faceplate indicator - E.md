---
title: Motor / Klep Faceplate indicator - Effective feedb...
updated: [[2017-12-05]]T14:04:47.0000000+01:00
created: [[2017-12-05]]T12:06:38.0000000+01:00
---

- # MOTOR
- # Expression
  iif (\$'.:Control Module:EffectiveFB0',1,iif (\$'.:Control Module:EffectiveFB1',2,0))
- # Icons
  ![image1](image1-73.png)
- # KLEP
- # Expression
  iif (\$'.:Control Module:EffectiveFB0',1,iif (\$'.:Control Module:EffectiveFB1',2,0))
- # Icons
  ![image2](image2-43.png)