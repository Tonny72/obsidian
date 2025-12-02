---
title: Instellen van email en SMS
updated: [[2020-02-25]]T16:15:28.0000000+01:00
created: [[2014-10-29]]T07:29:39.0000000+01:00
---

Instellen van email en SMS
woensdag 29 oktober 2014
7:29

- # [[2016-12-19]]
  Het sturen van van emails op basis van events werkt niet.
  
  [Instellen 800xA email en Smssen](https://sibelco-my.sharepoint.com/personal/tonny_lemmens_sibelco_com/_layouts/15/guestaccess.aspx?guestaccesstoken=ylrDJPEg1JGodLksTWcV1c0mtKRn51OmyXt02y7pa08%3d&docid=2_14fecb6c9a766426a87304b5633bd3719&rev=1)
- # Onderstaand tekst is verouderd. Zie bovenstaande link
- #
- # Hoe controleren welke mails / smssen zijn verstuurd:
  Control Structure : Control Network : Messenger Event Log aspect
  1.  **Instellen 800xA email en SMSsen**
    1.  ***Per user***
  Voeg volgende aspecten per user (in user structure) toe:
- Message subscriber aspect en voeg Email adres of SMS nr toe.
  ![image1](image1-521.png)
- Message schedue
  ![image2](image2-205.png)
  1.  ***Per Alarm***
  Voeg volgende aspecten per Object / Alarm list toe:
- Alarm and Event message source.  
  Dit zorgt voor de opbouw van het bericht en de koppeling met de Alarm List.
  ![image3](image3-122.png)
  
  ![image4](image4-88.png)
- Message Handler
  ![image5](image5-74.png)
  
  ![image6](image6-71.png)
  
  2.  **Alarm en Event groepen voor email en SMS**
  Deze groepen zijn bepaald door de severity.
  
  Urgent : 801 – 1000
  
  Hoog : 601 – 800
  
  Normaal : 401 – 600
  
  Laag : 201 – 400
  
  Melding : 1 - 200
  
  | **Severity** | **Groep omschrijving**                         |
  |--------------|------------------------------------------------|
  | **125**      | Niet gebruiken. Default severity Calcineeroven |
  | **200**      | Niet gebruiken. Default severity               |
  | **400**      | Niet gebruiken. Default severity               |
  | **501**      | Niet gebruiken. Default severity               |
  | **502**      | SMS + Email Kurt                               |
  | **600**      | Niet gebruiken. Default severity               |
  | **750**      | Niet gebruiken. Default severity               |
  | **800**      | Niet gebruiken. Default severity               |
  | **801**      | Test Tonny                                     |
  | **802**      | Test Kurt                                      |
  | **803**      | Email Automation                               |
  | **804**      | SMS en Email Automation                        |
  | **805**      | ~~Email PV Dessel~~                            |
  | **806**      | Email PV Dessel                                |
  | **807**      | Email Mech. Onderhoud                          |
  | **808**      | SMS en Email Mech. Onderhoud                   |
  | **809**      | Email Mech. Onderhoud + PV Dessel              |
  | **810**      | SMS en Email Mech. Onderhoud + PV Dessel       |
  | **811**      | Email Elektrische dienst                       |
  
  Indien de doelgroep van een bepaalde tag wijzigt, maak eventueel een extra groep aan en wijzig de severity in de tags.
  
  Voor een nieuwe groep copy/paste een bestaande groep in Control Structure – Root – Control Network
  
  ![image7](image7-59.png)
  
  En hernoem deze naar de juiste severity.
  
  Pas in de ‘Alarm en Event List Configuration’ de Attribute Filter – Severity aan naar de juiste severity.
  
  Pas Message Handler aan voor de juiste personen. Disable / Enable de message source anders werkt het niet.
  
  Om te weten welke tags welke severity hebben, gebruik de snapshot report.