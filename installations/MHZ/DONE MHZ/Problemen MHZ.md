---
date created: 2014-09-16]]T11:14:23.0000000+02:00
---
LINK SHARE ABB [Problemen MHZ](onenote:https://d.docs.live.net/648fe635197c5860/Documenten/TEST/New%20Section%201.one#Problemen%20MHZ&section-id={B065EC60-B8DD-4F52-9907-1C2DD8EC417C}&page-id={C12E883F-0B36-4C51-96CF-D6852A271E59}&end)
ZIE OOK [Opkuis SQL MHZ](onenote:#Opkuis%20SQL%20MHZ&section-id={7D21311A-5A29-4D4A-9AF9-A46A0666E433}&page-id={DBCC88BE-592E-480F-84CE-8B80B4E747B5}&end&base-path=https://d.docs.live.net/648fe635197c5860/Documenten/OneNote's/Persoonlijk%20(web)/TODO's.one)

- # [[2014-10-09]] 11:15 
  AS1: 49%
  AS2: 54%
  CS1: 29%
  CS2: 34%
- # [[2014-09-23]] 15:36 
  CS1: 28% =\> OK
  CS2: 34% =\> OK
  DC1: 24% =\> OK
  DC2: 27% =\> OK
  AS1: 41% =\> OK
  AS2: 50% =\> OK
  Aan Bart datum gevraagd voor upgrade ram.
- # [[2014-09-19]] 13:11 
  Met behulp van RamMap achterhaalt dat het grote geheugen gebruik op de 800xA servers word veroorzaakt door Driver Locked. Als ik dan verder ga zoeken kom ik op problemen met Vmware Tools. Heb voor een test dit stukje software van de servers verwijdert en heb nu geen uitzonderlijk gebruik van geheugen meer.
  
  | <http://communities.vmware.com/message/1714223> |
  |-------------------------------------------------|
  
  Ga dit ook nog even controleren op de SEC servers
  Hier blijkt het probleem zich niet voor te doen maar totdat ik een goede verklaring heb haal ik hier VMWare Tools ook weg
- # [[2014-09-18]] 14:47 
  Peter heeft ontdenkt dat blade 10.32.83.76 waar Linkworx SQL Server, CS1 en AS1 op draaien te weinig geheugen heeft.
- # [[2014-09-18]] 13:45 
  De Frothmaster netwerkconnectie uitgetrokken. De DCOM authenticatie failures blijven weg.
- # [[2014-09-17]] 9:55 
  Met Jef overlopen waarom de pimaire plc netwerk poorten veel collisions geven. Niet echt iets gevonden.
- # [[2014-09-17]] 8:27 
  Op de DC1 kreeg tijdens aanloggen deze fout.
  
  **Description:**
  A problem caused this program to stop interacting with Windows.
  
  **Problem signature:**
  Problem Event Name: AppHangXProcB1
  Application Name: Explorer.EXE
  Application Version: 6.0.6002.18005
  Application Timestamp: 49e01da5
  Hang Signature: bcba
  Hang Type: 32
  Waiting on Application Name: rnrpIconLog.exe
  Waiting on Application Version: 3.0.0.0
  OS Version: 6.0.6002.2.2.0.272.7
  Locale ID: 1033
  Additional Hang Signature 1: 18bddb606a81d83e86edb58aa9e65759
  Additional Hang Signature 2: b315
  Additional Hang Signature 3: fe9dfc086f3577031810e8ef8b75d23c
  Additional Hang Signature 4: bcba
  Additional Hang Signature 5: 18bddb606a81d83e86edb58aa9e65759
  Additional Hang Signature 6: b315
  Additional Hang Signature 7: fe9dfc086f3577031810e8ef8b75d23c
  
  **Read our privacy statement:**
  <http://go.microsoft.com/fwlink/?linkid=50163&clcid=0x0409>
  
  en toen ik rnrp monitor wilde starten, wilde deze zich terug installeren.
- #
- # [[2014-09-16]] 12:56 
  Op switch SWR01-2 fa0/19 (patch3-24) zat een Belgacom Bbox die als switch moest dienen. Deze verwijderd
- # [[2014-09-16]] 11:44 
  New Graphics demo verwijderd uit Functional Structure
  Backup staat op EngClient Libraries\Documents
- # [[2014-09-16]] 11:40 
  Diagnostics geprogrammeerd voor B1, B2, B3 en ZL
- #
- # [[2014-09-16]] 11:19 
  Frothmaster uit 800xA verwijderd. Backup staat op EngClient Libraries\Documents\Frothmaster.afw
  ![image1](image1-283.png)
- #
- # [[2014-09-16]] 11:15 
  Kabel2 van [[C2]] is slecht. Omgekoppeld naar Kabel3.
  
  Meting kabel2
  ![image2](image2-7.jpeg)
  
  Meting kabel3
  ![image3](image3-8.jpeg)
  
  [[2014-09-08]] 15:33
  Alweer enkele servers herstart inclusief DC1
  Kristof Loos gaat servers ontlasten
  
  [[2014-09-01]] 9:58
  CS1: 97%
  Dit is hopeloos.
  Kurt heeft deze morgen in de meeting gezegd dat hij ABB regelt.
  
  [[2014-08-12]] 16:20
  CS1 intern geheugen verhoogd van 3GB naar 4GB
  AS1 intern geheugen verhoogd van 3GB naar 4GB
  
  [[2014-08-04]] 13:15
  Kruis op alarm-lijsten
  CS1 op 93%: herstart
  AS1 op 88%:
  AS2 op 86%:
  Netwerkloop gedetecteerd
  
  [[2014-08-04]] 13:12
  Vorige week 2x spanningsdip geweest. Problemen met PLC .10
  Maar uiteindelijk ik alles goed gekomen.
  
  [[2014-07-08]] 10:34
  CS1 : 28% =\> ok
  CS2 : 44% =\> ok
  
  [[2014-06-30]] 11:27
  Vreemd iets
  Om 9u had één connectivity server een geheugen van 97%. Vanwege een meeting om 9u beslist om na de meeting de server te herstarten.
  Na de meeting 11.30u was het geheugen verbruik gezakt tot een normaal percentage.
  Enkel Kepserver gedeïnstalleerd.
  
  [[2014-06-23]] 16:25
  CS1 herstart. Geheugen zal op 98%
  ![image4](image4-57.png)