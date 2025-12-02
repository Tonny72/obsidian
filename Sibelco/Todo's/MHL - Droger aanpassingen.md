---
date created: 2022-09-12
date modified: 2025-08-30
---

[Meeting MHL Droger - 2022/09/12](onenote:https://sibelco-my.sharepoint.com/personal/tonny_lemmens_sibelco_com/Documents/Sibelco%20-%20Onedrive%20Personal/Meetings/Meetings%20Sibelco.one#MHL%20Droger%20-%202022/09/12&section-id={0BF91C91-09F9-451D-AF7E-A322100AC78C}&page-id={E88A716C-148F-48B9-999A-1162F0D0D6C1}&end)

[Procesbeschrijving Droger MHL.docx](https://sibelco.sharepoint.com/:w:/r/sites/OperationsBelgium/Shared%20Documents/Lommel/Droger/Procesbeschrijving%20Droger%20MHL.docx?d=wac1356ed8b444186ac27387b92688ba3&csf=1&web=1&e=DnZics)

[C:\Users\lemton00\Sibelco\Cluster Dessel Operations - Documents\Lommel](file:///C:/Users/lemton00/Sibelco/Cluster%20Dessel%20Operations%20-%20Documents/Lommel)

- Uitschrijven wat gebeurt er als TT605 \> HHH  
  =\> Brander OFF sequentie wordt gestart.
- GIC601 moet sneller reageren.  
  =\> zie suggesties
- Uitschrijven werking bij delta-T  
  =\> Regeling delta-T (TIC604) is gelijkaardig aan GIC601 en TIC603
- BR1_BS_OK (=noodstop) Hoe is deze geprogrammeerd. (moet zijn: zo snel mogelijk alles uit en niet stap per stap)  
  =\> Rechtstreeks hangen op brander vrijgave
- Sequentie voeding aanpassen. Als de klep onder silo open is, dan eerst GIC601 even op een vast toerental zetten, nadien pas automatisch  
  =\> Eerst de andere aanpassingen ivm GIC601 proberen
  
  Suggesties:
  1.  Extra voorwaarde voor GIC601 Track: Er moet ook een klep open zijn.
  2.  Track waarde voor GIC601 op bijvoorbeeld 350 rpm zetten
  3.  ~~TT611 koppelen BR1_BS_OK rechtstreeks koppelen op brander vrijgave~~
- # [[2022-09-29]]
- Stein brengt delta T meting en freq. sturing [[B604]] in orde
- Tonny: suggestie 1 en 2 programmeren (vrijdag 30/09 in NM)  
  **IS AL VOORBEREID**
- # [[2022-09-30]] aanpassing
  Regeling GIC601 staat in Track als
- De banden (B602, B603) zijn gestopt.
- En de kleppen onder de silo’s (601 .. 604) gesloten zijn.
  
  Als deze regeling in Track staat, wordt er een vast toeren naar de uitgang gestuurd.
  Dit is toerental is afhankelijk van TT601 en staat op het scherm.
  
  ![image1](image1%201.jpg)
  
  De regeling werkt automatisch als een band draait en er een klep open is.