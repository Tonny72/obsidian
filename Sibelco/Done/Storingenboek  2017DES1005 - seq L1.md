---
title: 'Storingenboek : 2017/DES/1005 - seq L1+2 naar maat'
updated: [[2022-01-21]]T13:53:32.0000000+01:00
created: [[2017-11-14]]T16:35:57.0000000+01:00
---

| **Subject** | **Storingenboek : 2017/DES/1005 - seq L1+2 naar maat**                                                                              |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **From**    | <SEUAPPNTS2/SibelcoEurope/AMORG@sibelco.com>                                                                                        |
| **To**      | Tonny Lemmens; Kurt Regout; Harry Stienen; Jan Smolders; Henri Boonen; Peter Drees; Tim Cools; Peter Drees; Jan Smolders; Tim Cools |
| **Sent**    | dinsdag 14 november 2017 12:09                                                                                                      |
Installatie : SCR Hydro

Status : Nieuw

Omschrijving : 
Guy Claes schreef op [[2017-11-14]] 12:09:03
Bij het omschakelen van L1+2, die in produktie stond naar ms4, naar de maat (ms83), stond de klep (HY_KL30) nog op hand open.
De sequentie begint om te schakelen naar de maat en stuurt klep 31 open maar kan klep 30 dus niet sluiten aangezien deze op hand staat. Toch gaat de sequentie gewoon verder in haar stappen tot de volledige productiestap. Bijgevolg wordt het zand hier terug op gezet en beginnen de sizers op te vullen maar sturen niet open. Na enig zoekwerk het probleem gevonden en klep 30 dichtgestuurd en terug automatisch gezet. Bijgevolg gaan de sizers volledig open waarbij de pomp zich verslikt in het zand.
Als klep 30 niet dicht stuurt mag de sequentie toch niet in volledige productiestap komen volgens mij?!
Gelieve eens na te kijken.

Link : 
![image1](image1-9.gif)

- # [[journals/2017-11-16]] 
  Meeting met JSM belegd.
  In verband met storing:
  ![image1](image1-9.gif)
  
  ![image2](image2-2.jpg)
  
  Ik kan de sequentie aanpassen dat deze wacht opdat 1 klep open is, en 1 klep gesloten is.
  (Stap104 en Stap113)
  
  Ook klopt in mijn ogen de sequentie niet helemaal.
- # [[2017-11-20]] 
  Sequentie
  <https://sibelco.sharepoint.com/teams/Team_PlantDessel_Dessel_MiningandProcessingOperations_ProjectandTechnicalServices/_layouts/15/guestaccess.aspx?guestaccesstoken=tKHNBA9eyY0qNyzj%2FPEoIX5zphuwXSN3M4KXSbDClzY%3D&docid=2_116e05458f094413ba3e946068d9cf005&rev=1&e=efb8ddd21cbb45c6a3400724262ecfbf>
- # [[2017-11-21]] 
  Sequentie aangepast
  [Aanpassing Sequentie Hydro Lijn 1_2 (Hydro_Lijn_1\_2)](onenote:https://sibelco.sharepoint.com/teams/Team_PlantDessel_Dessel_MiningandProcessingOperations_ProjectandTechnicalServices/Public%20Documents/Installaties/Info%20Sibelco/Hydro%20(Natzand)/Aanpassingen.one#Aanpassing%20Sequentie%20Hydro%20Lijn%201_2%20(Hydro_Lijn_1_2)&section-id={97C43A44-0549-4315-B8F1-FD58F80809D4}&page-id={00414F57-8D86-4344-A08C-688466EFA040}&end)