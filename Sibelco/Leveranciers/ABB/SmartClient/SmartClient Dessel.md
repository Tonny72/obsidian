---
date created: 2014-12-05T00:00:00+01:00
date modified: 2025-10-20T13:37:42+02:00
tags: [des]
---
created:: 2014-12-05
tags:: [[SmartClient]]

[http://10.32.29.51/SC?feature=SCPG2](http://10.32.29.51/SC?feature=SCPG2) (werkt niet in Chrome)

- # Rode kruisen (na herstart van CS1)
  ![[assets/images/Pasted image 20240806144857\.jpg]]
- # Toevoegen van user
  1.  Start de User configuration tool
  2.  Klik op de Replicate button
  3.  Haal de user(s) uit Active Directory
  4.  Create een private directory voor de user  
  Rechtsklik op de user en kies Create Private directory.  
  Na Save wordt er een directory aangemaakt onder C:\Program Files\ABB Industrial IT\Operate IT\ABB Smart Client\SC\Files\Private
  5.  Voeg de user toe de juiste group
- # Configuratie bestanden van Smart Client
  C:\Program Files\ABB Industrial IT\Operate IT\ABB Smart Client\SC
  DESSEL
  <http://10.32.29.51/SC?feature=SCPG2>
  MHZ
  <http://10.32.84.51/SC?feature=SCPG2>
- # EDGE ondersteuning
  [edge://flags/#edge-click-once](edge://flags/#edge-click-once)
  ![image1](image1-560.png)
- # Gebruik voor Energy
  
  User energy
  pw Sibelco1
- # Log
- # [[2017-08-30]]
  Rode kruisen op het scherm CS1 services gestopt en terug gestart.
- # [[2018-01-11]]
  Opnieuw rode kruisen. Smart Client service herstart
  ![image1](image1-18%201.png)
- # [[2018-12-10]] 
  Vanwege het vele vastlopen van SmartClient, een script op CS1 gescheduled.
  ![image2](image2-14%201.png)
  
  In script zit:
  Stop-Service -Name "ABB Smart Client Program Supervision" -Force
- # [[2018-12-20]] 
  Getest. Smart client werkt nog altijd.
- # [[2019-01-07]] 
  Alles nog maar eens herstart
- # [[2019-02-15]] 
  Script op SmartClient server
  Write-Host "Begin Restart Service"
  Restart-Service -Name "ABB Smart Client Program Supervision" -Force
  Write-Host "End Restart Service"
- # [[2019-02-26]]
  Gisteren mail naar ABB gestuurd.
  Smart Client blijft hangen op Checking for license
- # [[2019-03-04]]
  Op vraag van Peter Stroop, de CS1 herstart.
  Nu nog wel rode kruisen.
  
  ![image3](image3-9%201.png)
- # [[2019-03-14]]
  Al geruime tijd terug stabiel