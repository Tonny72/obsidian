---
title: MHZ Automatisering toren0
updated: [[2022-01-21]]T14:00:56.0000000+01:00
created: [[2014-09-10]]T08:34:28.0000000+02:00
---

MHZ Automatisering toren0
woensdag 10 september 2014
8:34

En dan nog een programmatie voor toren0

- # [[2014-11-12]] 11:30 
  Programmatie en test vorige vrijdag afgerond
- # [[2014-09-16]] 15:41 
  Programmatie voorbereid. IO nog koppelen.
- # [[2014-09-16]] 15:03 
  Toren0 krijgt zand van stockpile fijn
- # [[2014-09-10]] 8:35 
  
  [MTW205.pdf](MTW205.pdf)
  
  Aangaande automatisering toren 0
  
  Doel:
  Dmv bediening in controlekamer de toren "0" in de juiste positie te plaatsen, uiterst links of uiterst rechts.
  
  Beschrijving:
  
  C2.0.11.106
  
  DI11 C6 MTW205_ML /eindkontakt max lks
  DI12 B6 MTW205_MR /eindkontakt max rts
  DI13 C7 MTW205_LOC /bediening locaal
  DI14 B7 MTW205_REM /bediening remote
  DI15 C8 MTW205_F /storing in servo
  DI16 B8 MTW205_WS /werkschak open
  
  C2.0.11.202
  
  DO9 C5 MTW205_L /start naar LKS
  DO10 B5 MTW205_R /start naar RTS
  
  Werking:
  
  Staat de toren uiterst links DI11 = 1
  Bediening naar rechts is enkel mogelijk als de MTW205 in remote bediening staat en werkschakelaar gesloten
  Wanneer eindcontact rechts DI12 = 1, stopt de servomotor
  
  Staat de toren uiterst rechts DI12 = 1
  Bediening naar links is enkel mogelijk als de MTW205 in remote bediening staat en werkschakelaar gesloten
  Wanneer eindcontact links DI11 = 1, stopt de servomotor
  
  Mogelijkheid om te stoppen tijdens beweging.
  
  Storing in servo, fout MTW205 genereren.
  
  Bediening op afstand enkel mogelijk bij DI14 = 1
  Bediening terplekke DI13 = 1
  
  Bij storing, DI15 = 1 melding genereren en servomotor stilleggen.