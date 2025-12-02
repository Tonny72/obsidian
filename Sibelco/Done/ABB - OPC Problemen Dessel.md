---
created: [[2018-06-11]]T09:08:30.0000000+02:00
tags:
  - 800xA
---
# ABB

# Opvolging van de OPC problemen in Dessel
# [[2018-06-11]] 
  Date Time Level Source Event
  08-06-2018 01:32:19 Warning OPC DA Client Write request timeout on device '800xA_Slow.Storage'.
  08-06-2018 01:32:19 Warning OPC DA Client 800xA_Slow.Storage \| Unable to write to address on device. \| Address = 'Applications.Meeltransport.Communicatie.MES.Storage.P40BU69:MES.item_no'.
  08-06-2018 22:27:22 Warning OPC DA Client Write request timeout on device '800xA_Slow.Storage'.
  08-06-2018 22:27:22 Warning OPC DA Client 800xA_Slow.Storage \| Unable to write to address on device. \| Address = 'Applications.ST01.Units.Unit_MS112.P40BU112:MES.location_id'.
  08-06-2018 22:44:11 Warning OPC DA Client Write request timeout on device '800xA_Slow.Storage'.
  08-06-2018 22:44:11 Warning OPC DA Client 800xA_Slow.Storage \| Unable to write to address on device. \| Address = 'Applications.ST02.Communicatie.MES.Storage.P40BU64:MES.location_id'.
  09-06-2018 06:44:53 Warning OPC DA Client Add item failed for 'AF12_PM1' on device '800xA.Energy'. Item error: 0xC0040008 'OPC_E\_INVALIDITEMID(0xc0040008) The item definition doesn't conform to the server's syntax. '
  09-06-2018 08:16:32 Warning OPC DA Client Async Write 2.0 failed for 'Applications.Meeltransport.Communicatie.MES.Storage.P40BU86:MES.location_id' on device '800xA_Slow.Storage'. Item error: 0x8ABB150C 'E_AFW_OPCDA_INVALID_SERVERHANDLE(0x8abb150c) The Data Access Read/Write operation was rejected because AddItems has not yet completed. '
  09-06-2018 08:16:33 Warning OPC DA Client Write request timeout on device '800xA_Slow.Storage'.
  09-06-2018 08:16:33 Warning OPC DA Client 800xA_Slow.Storage \| Unable to write to address on device. \| Address = 'Applications.Meeltransport.Communicatie.MES.Storage.P40BU86:MES.location_id'.
  09-06-2018 08:16:33 Warning OPC DA Client Async Write 2.0 failed for 'Applications.Meeltransport.Communicatie.MES.Storage.P40BU86:MES.item_no' on device '800xA_Slow.Storage'. Item error: 0x8ABB150C 'E_AFW_OPCDA_INVALID_SERVERHANDLE(0x8abb150c) The Data Access Read/Write operation was rejected because AddItems has not yet completed. '
  09-06-2018 08:16:35 Warning OPC DA Client Write request timeout on device '800xA_Slow.Storage'.
  09-06-2018 08:16:35 Warning OPC DA Client 800xA_Slow.Storage \| Unable to write to address on device. \| Address = 'Applications.Meeltransport.Communicatie.MES.Storage.P40BU86:MES.item_no'.
  09-06-2018 08:16:41 Warning OPC DA Client Write request timeout on device '800xA_Slow.Storage'.
  09-06-2018 08:16:41 Warning OPC DA Client 800xA_Slow.Storage \| Unable to write to address on device. \| Address = 'Applications.ST09_AF09_AF10.Communicatie.MES.Storage.P40BU92:MES.item_no'.
  10-06-2018 18:26:21 Warning OPC DA Client Write request timeout on device '800xA_Slow.Storage'.
  10-06-2018 18:26:21 Warning OPC DA Client 800xA_Slow.Storage \| Unable to write to address on device. \| Address = 'Applications.ST01.Units.Unit_MS06.P40BU06:MES.erp_stock_qty'.
  11-06-2018 08:51:15 Security KEPServerEX\Runtime Configuration session started by LEMTON00 as Default User (R/W).
# [[2018-06-11]] 9:19 
  Config van Productie naar Engineering gekopieerd
  
  Log van Engineering
  Date Time Level Source Event
  11-06-2018 09:15:21 Warning Licensing Feature Data Logger Plug-in is time limited and will expire at 11-06-2018 11:15.
  11-06-2018 09:15:21 Error KEPServerEX\Runtime Attempt to add item '800xA.Plant.C3.C3_PT303_15' failed.
  11-06-2018 09:15:21 Warning Data Logger Plug-in Failed to register log item for log group 'C3'. (Log Item: 800xA.Plant.C3.C3_PT303_15)
  11-06-2018 09:15:21 Error KEPServerEX\Runtime Attempt to add item '800xA.Energy.AF09PM_Energy' failed.
  11-06-2018 09:15:21 Warning Data Logger Plug-in Failed to register log item for log group 'Energy Datalog Energy Calc'. (Log Item: 800xA.Energy.AF09PM_Energy)
  11-06-2018 09:15:21 Error KEPServerEX\Runtime Attempt to add item '800xA.MES.PBA01.PBA01_Started' failed.
  11-06-2018 09:15:21 Warning Data Logger Plug-in Failed to register log item for log group 'MES Start Stop'. (Log Item: 800xA.MES.PBA01.PBA01_Started)
  11-06-2018 09:15:21 Error KEPServerEX\Runtime Attempt to add item '800xA.Storage.P40BU01.CalculatedStockQty' failed.
  11-06-2018 09:15:21 Warning Data Logger Plug-in Failed to register log item for log group 'Storage'. (Log Item: 800xA.Storage.P40BU01.CalculatedStockQty)
  11-06-2018 09:15:21 Information KEPServerEX\Runtime Runtime project replaced.
  
  Op Engineering
  Data Logger disabled
  
  Siemens Kepware verwijderd
  
  Watchdog verwijderd
  
  De meeste tags komen niet actief. Nieuwe kepserver versie (v6.4) downloaden.
  
  Test opgezet: ST01 Unit_OPC_TEST
# [[2018-06-11]] 13:32 
  Mail naar Stijn
  
  Stijn,
  
  Ik heb op mijn engineering pc kepserver geïnstalleerd en veel test-tags aangemaakt.
  
  Met de Kepware OPC Quick Client kan je een bulk synchrone schrijf test doen.
  
  Ik heb twee configs in de OPC Quick Client opgezet.
  
  1.  3000 tags rechtstreeks naar de ABB OPC DA server
  2.  1550 tags naar de Kepware DA server
  
  Test 1 heeft een average schrijftijd van 2375ms en verloopt zonder problemen.
  
  Test 2 geeft initieel veel fouten gelijkaardig als in de productie omgeving
  ![image1](image1-24.jpg)
  
  Het aanpassen van de write-timeout naar 5000ms lost de fouten op, maar de gemiddelde schrijftijd, bij verschillende tests, bedraagt tussen de 4000ms en 7500ms.
  
  Conclusie:
  Rechtstreeks naar ABB: 0.791 ms/tag
  Via KepWare: 3,921 ms/tag
  
  Op de Kepware productie server staat de write time-out voor MES-tags op 1000ms en voor Storage-tags op 1500ms.
  Ik vermoed dat we soms over deze limiet gaan, wat een bad tag geeft.
  
  Ik denk dat we, op korte termijn, de write time-out op 10000ms moeten zetten.
  En op lange termijn het aantal tags moeten beperken.
# [[2018-11-12]] 
  Op vraag van Harry Prioriteit verhoogd
# [[2018-11-22]] 
  Ik heb mogelijk iets gevonden, maar is onlogisch.
  
  Op dit moment staat de started-bit van PBA01, PBA02 en PBA04 in het rood bij Linkworx en ook bij UAExpert.
  
  ![image2](image2-10.jpg)
  
  Ik heb eens in Kepware via de import-functie de started-bit van PBA01, PBA02 en PBA04 toegevoegd.
  Je krijgt dan in UAExpert een lange NodeID, maar werkende tags
  
  ![image3](image3-7.jpg)
  
  Ik heb dan in Kepware de werkende tags gecopy/paste (dus het opc-da path is hetzelfde gebleven) naar de plaats 800xA.MES waar de niet werkende tags staan.
  Als ik dan kijk in UAExpert werken deze tags ook niet altijd
  
  ![image4](image4-5.jpg)
  
  Dus voor PBA02
  Config die niet werkt.
  ![image5](image5-2.jpg)
  
  Config die wel werkt.
  ![image6](image6-1%201.jpg)
  
  Van het moment dat ik voor PBA02 bij de werkende tag de status wijzig, komt alles goed.
  ![image7](image7%201.jpg)
  
  Dit ga ik al doen:
- Voor elk workcenter voeg ik een test-bit toe. Op deze manier kunnen we plc gebonden communicatie uitsluiten.
- Ik maak een test-programma / script dat willekeurig deze bit leest en schrijft. Zowel de manueel aangemaakte bits, als de geïmporteerde bits.
  
  Stel dat de geïmporteerde bits soms ook falen, dan ga ik op OPC-DA niveau proberen. Dus zonder Kepware.
  Stel dat de geimporteerde bits goed blijven, dan moeten de tags in [[applications/MES/MES]] worden aangepast.
  Stel dat alle statussen goed blijven, dan verander ik de ‘struct’ in ABB, naar apparte variabelen.
# [[2018-11-23]] 
  Ticket bij [[Archive/applications/Kepware/Kepware]] geopend
  
  Thank you for submitting your question to us.
  Case \#14662666: "**Add item failed for ... OPC_E\_INVALIDITEMID The item definition doesn't conform to the server syntax.**” has been created.
  
  **NOTE!** To correspond with the PTC representative assigned to your Case, please "reply ALL" to this email or submit a comment using the Case Viewer: <https://ptc.force.com/cs/s/case/5005A00001012ss>
# [[2018-11-23]] 14:12 
  Kepware heeft info gevraagd en deze opgestuurd
  
  Test programma gemaakt en gestart op Eng.
# [[2018-11-23]] 14:58 
  ![image8](image8-7%201.png)
  
  ![image9](image9-6%201.png)
  
  23/11\*14:06:36.262 ConfError: Suspected network loop, short interface block made on area=0 path=0
  23/11\*14:06:39.426 Node_down = 86 area= 0 path=0 last (10.32.29.86 )
  23/11\*14:06:39.905 Node_down = 6 area= 0 path=0 last (10.32.29.6 )
  23/11\*14:06:39.910 Node_down = 15 area= 0 path=0 last (10.32.29.15 )
  23/11\*14:06:39.915 Node_down = 25 area= 0 path=0 last (10.32.29.25 )
  23/11\*14:06:39.919 Node_down = 26 area= 0 path=0 last (10.32.29.26 )
  ...
  23/11\*14:06:52.325 Node_up = 54 area= 4 path=0 (10.32.47.54 )
  23/11\*14:06:52.329 Node_up = 55 area= 4 path=0 (10.32.47.55 )
  23/11\*14:06:52.428 Node_down = 25 area= 2 path=0 last (10.32.48.25 )
  23/11\*14:08:47.884 Node_up = 25 area= 2 path=0 (10.32.48.25 )
  23/11\*14:08:47.956 Node_down = 30 area= 2 path=1 (10.32.49.30 )
  23/11\*14:08:48.030 Node_up = 31 area= 2 path=1 (10.32.49.31 )
  23/11\*14:34:11.629 ConfError: Suspected network loop, short interface block made on area=0 path=0
  23/11\*14:34:14.907 Node_down = 6 area= 0 path=0 last (10.32.29.6 )
  23/11\*14:34:14.981 Node_down = 32 area= 0 path=0 last (10.32.29.32 )
  23/11\*14:34:15.056 Node_down = 60 area= 0 path=0 last (10.32.29.60 )
  ...
  23/11\*14:34:31.174 Node_up = 30 area= 2 path=0 (10.32.48.30 )
  23/11\*14:34:31.254 Node_up = 40 area= 2 path=0 (10.32.48.40 )
# [[2018-11-26]] 11:12 
  **From:** Tonny Lemmens
  **Sent:** Monday, 26 November 2018 10:59
  **To:** peter.stroop@nl.abb.com; Stijn Vandenbroucke \<stijn.vandenbroucke@linkworx.eu\>; Jef Mertens \<Jef.Mertens@sibelco.com\>
  **Cc:** Kurt Regout \<Kurt.Regout@sibelco.com\>; Harry Stienen \<Harry.Stienen@sibelco.com\>
  **Subject:** OPC Communicatie probleem
  
  Heren,
  
  Al geruime tijd ervaren wij OPC communicatie probleem.
  
  Even de situatie schetsen.
  Een OPC UA Client wil een waarde in een bepaalde tag in OPC DA schrijven.
  
  Centraal staat hierin een KEPServerEX server die zorgt voor de omzetting van OPC UA -\> OPC DA en draait op een ABB server.
  
  Omdat het probleem moeilijk te simuleren is, heb ik heb vorige vrijdag een test opgezet dat 4 test-bits om de 5 seconden van true naar false zet en omgekeerd.
  In de log van de KEPServerEx staan nu meer warnings van Writes failed en timeouts.
  
  Een kleine stukje van de log
  24-11-2018 03:43:48 Warning OPC DA Client Async Write 2.0 failed for 'Applications.Labo:test' on device 'WatchDog.Device1'. Item error: 0x8ABB150C 'E_AFW_OPCDA_INVALID_SERVERHANDLE(0x8abb150c) The Data Access Read/Write operation was rejected because AddItems has not yet completed. '
  24-11-2018 03:43:48 Warning OPC DA Client Async Write 2.0 failed for 'Applications.Molen_5.Communicatie.MES.WatchDog:MES_TO_ABB' on device '800xA.Plant'. Item error: 0x8ABB150C 'E_AFW_OPCDA_INVALID_SERVERHANDLE(0x8abb150c) The Data Access Read/Write operation was rejected because AddItems has not yet completed. '
  24-11-2018 03:43:48 Warning OPC DA Client Async Write 2.0 failed for 'Applications.Toevoer_FFS_BBZ.Communicatie.PBA01\_:MES.test' on device '800xA.MES'. Item error: 0x8ABB150C 'E_AFW_OPCDA_INVALID_SERVERHANDLE(0x8abb150c) The Data Access Read/Write operation was rejected because AddItems has not yet completed. '
  24-11-2018 03:43:54 Warning OPC DA Client Write request timeout on device '800xA.MES'.
  24-11-2018 03:43:54 Warning OPC DA Client 800xA.MES \| Unable to write to address on device. \| Address = 'Applications.Toevoer_FFS_BBZ.Communicatie.PBA01\_:MES.test'.
  24-11-2018 03:43:54 Warning OPC DA Client 800xA.MES \| Unable to write to address on device. \| Address = 'Root/Control Network/Sibelco_Dessel/Applications/Rotoseal/Control Modules/Communicatie/MES/PBA02:MES.test'.
  24-11-2018 03:43:54 Warning OPC DA Client 800xA.MES \| Unable to write to address on device. \| Address = 'Applications.ST09_AF09_AF10.Communicatie.MES.PBA03\_:MES.test'.
  
  We hebben hier met verschillende componenten te maken waar het kan fout lopen.
  Ik wil de logs van de verschillende systemen samenleggen om te zien wat er gebeurt.
  
  [@peter.stroop@nl.abb.com](mailto:peter.stroop@nl.abb.com)
  Peter,
  Wat ik vermoed, is dat ABB OPC servers het soms druk hebben met de afhandeling van al de OPC communicatie. Mogelijk hebben wij (te) veel PLC’s voor de connectivity servers.
  Kan jij de nodige ABB OPC specialisten contacteren en de nodige logging opzetten (OPC).
  
  [@Jef Mertens](mailto:Jef.Mertens@sibelco.com)
  Jef,
  Mogelijk is een netwerk probleem de oorzaak.
  Kan jij ervoor zorgen dat ik logs uit switchen kan trekken.
  
  Ik heb ook al een ticket bij Kepware ingelegd. Zij zijn ook al op de hoogte.
  
  Met vriendelijke groeten,
  
  Tonny Lemmens
# [[2018-11-26]] 11:13 
  ConsoleAPP1 en ConsoleAPP2 gestart op engineering
# [[2018-11-26]] 16:33 
  Controle
  
  | PBA01_started | opc.tcp://10.32.29.60:59151 | kepware | NS2\|String\|800xA.MES.PBA01.PBA01_Started | READWRITE | Bad | [[2018-11-26]] 13:59:49 |
  |---------------|-----------------------------|---------|--------------------------------------------|-----------|-----|---------------------|
  | PBA05_started | opc.tcp://10.32.29.60:59151 | kepware | NS2\|String\|800xA.MES.PBA05.PBA05_Started | READWRITE | Bad | [[2018-11-26]] 15:27:04 |
  **
  Twee tags staan bad, niet in de logs te zien.
# [[2018-11-27]] 08:24 
  Log staat nu vol met
  26-11-2018 16:37:18 Warning OPC DA Client WatchDog.Device1 \| Unable to write to address on device. \| Address = 'Applications.Labo:test'.
  26-11-2018 16:37:28 Warning OPC DA Client WatchDog.Device1 \| Unable to write to address on device. \| Address = 'Applications.Labo:test'.
# [[2018-11-27]] 11:02 
  Kreeg rode kruisen op scherm
  ![image10](image10-4%201.png)
  In RNRP log niks te zien, maar deze draaide al maar op 1 netwerk
  
  ConsoleApp2
  SMWS_TEST: True, 27-Nov-2018 10:00:36, Good
  Tijd: 11:00:40
  SMDS2_TEST: False, 27-Nov-2018 10:00:41, Good
  SMWS_TEST: False, 27-Nov-2018 10:00:41, Good
  Tijd: 11:00:46
  Bad
  SMDS2_TEST: False, 27-Nov-2018 10:01:00, Good
  SMWS_TEST: False, 27-Nov-2018 10:01:00, Good
  Tijd: 11:01:07
  Tijd: 11:01:13
  SMDS2_TEST: True, 27-Nov-2018 10:01:14, Good
  SMWS_TEST: True, 27-Nov-2018 10:01:14, Good
  Tijd: 11:01:19
- ## In de log van opc server CS1
  [[2018-11-27]] 10:55:03.980 OPC Data Access: Contact again with controller: 10.32.48.15
  E [[2018-11-27]] 10:55:03.980 Off Unit= SubDataAccess 10.32.48.15 ConnErr OPCServer 5500 Conn error to DA subscr controller
  E [[2018-11-27]] 11:00:53.906 On Unit= SubAlarmEvent 10.32.48.40 ConnErr OPCServer 6500 Conn error to AE subscr controller
  E [[2018-11-27]] 11:00:54.183 On Unit= SubAlarmEvent 10.32.48.28 ConnErr OPCServer 6500 Conn error to AE subscr controller
  E [[2018-11-27]] 11:00:54.484 On Unit= SubAlarmEvent 10.32.48.14 ConnErr OPCServer 6500 Conn error to AE subscr controller
  E [[2018-11-27]] 11:00:54.634 On Unit= SubAlarmEvent 10.32.48.21 ConnErr OPCServer 6500 Conn error to AE subscr controller
  E [[2018-11-27]] 11:00:55.236 On Unit= SubAlarmEvent 10.32.48.15 ConnErr OPCServer 6500 Conn error to AE subscr controller
  E [[2018-11-27]] 11:00:56.723 On Unit= SubAlarmEvent 10.32.48.29 ConnErr OPCServer 6500 Conn error to AE subscr controller
  E [[2018-11-27]] 11:00:58.767 On Unit= SubAlarmEvent 10.32.48.18 ConnErr OPCServer 6500 Conn error to AE subscr controller
  E [[2018-11-27]] 11:00:59.127 On Unit= SubAlarmEvent 10.32.48.11 ConnErr OPCServer 6500 Conn error to AE subscr controller
  E [[2018-11-27]] 11:01:00.592 On Unit= SubAlarmEvent 10.32.48.16 ConnErr OPCServer 6500 Conn error to AE subscr controller
  E [[2018-11-27]] 11:01:07.153 On Unit= SubDataAccess 10.32.48.21 ConnErr OPCServer 5500 Conn error to DA subscr controller
  E [[2018-11-27]] 11:01:20.159 On Unit= SubDataAccess 10.32.48.28 ConnErr OPCServer 5500 Conn error to DA subscr controller
  E [[2018-11-27]] 11:01:33.165 On Unit= SubDataAccess 10.32.48.16 ConnErr OPCServer 5500 Conn error to DA subscr controller
  E [[2018-11-27]] 11:01:47.091 On Unit= SubDataAccess 10.32.48.11 ConnErr OPCServer 5500 Conn error to DA subscr controller
  E [[2018-11-27]] 11:02:00.097 On Unit= SubDataAccess 10.32.48.18 ConnErr OPCServer 5500 Conn error to DA subscr controller
  E [[2018-11-27]] 11:02:13.332 On Unit= SubDataAccess 10.32.48.29 ConnErr OPCServer 5500 Conn error to DA subscr controller
  E [[2018-11-27]] 11:02:26.339 On Unit= SubDataAccess 10.32.48.14 ConnErr OPCServer 5500 Conn error to DA subscr controller
  E [[2018-11-27]] 11:02:39.346 On Unit= SubDataAccess 10.32.48.15 ConnErr OPCServer 5500 Conn error to DA subscr controller
  E [[2018-11-27]] 11:02:52.203 Off Unit= SubAlarmEvent 10.32.48.11 ConnErr OPCServer 6500 Conn error to AE subscr controller
  E [[2018-11-27]] 11:02:52.449 Off Unit= SubAlarmEvent 10.32.48.40 ConnErr OPCServer 6500 Conn error to AE subscr controller
  E [[2018-11-27]] 11:02:52.465 Off Unit= SubAlarmEvent 10.32.48.28 ConnErr OPCServer 6500 Conn error to AE subscr controller
  E [[2018-11-27]] 11:02:52.710 Off Unit= SubAlarmEvent 10.32.48.14 ConnErr OPCServer 6500 Conn error to AE subscr controller
  E [[2018-11-27]] 11:02:52.798 Off Unit= SubAlarmEvent 10.32.48.16 ConnErr OPCServer 6500 Conn error to AE subscr controller
  E [[2018-11-27]] 11:02:52.820 On Unit= SubDataAccess 10.32.48.40 ConnErr OPCServer 5500 Conn error to DA subscr controller
  E [[2018-11-27]] 11:02:52.880 Off Unit= SubAlarmEvent 10.32.48.21 ConnErr OPCServer 6500 Conn error to AE subscr controller
  E [[2018-11-27]] 11:02:52.988 Off Unit= SubAlarmEvent 10.32.48.29 ConnErr OPCServer 6500 Conn error to AE subscr controller
  E [[2018-11-27]] 11:02:53.060 Off Unit= SubAlarmEvent 10.32.48.18 ConnErr OPCServer 6500 Conn error to AE subscr controller
  E [[2018-11-27]] 11:02:53.418 On Unit= SubAlarmEvent 10.32.48.40 ConnErr OPCServer 6500 Conn error to AE subscr controller
  E [[2018-11-27]] 11:02:53.494 Off Unit= SubAlarmEvent 10.32.48.40 ConnErr OPCServer 6500 Conn error to AE subscr controller
  E [[2018-11-27]] 11:02:54.362 Off Unit= SubAlarmEvent 10.32.48.15 ConnErr OPCServer 6500 Conn error to AE subscr controller
  E [[2018-11-27]] 11:02:56.008 On Unit= SubAlarmEvent 10.32.48.15 ConnErr OPCServer 6500 Conn error to AE subscr controller
  E [[2018-11-27]] 11:02:56.093 Off Unit= SubAlarmEvent 10.32.48.15 ConnErr OPCServer 6500 Conn error to AE subscr controller
  
  I [[2018-11-27]] 11:03:08.928 OPC Data Access: Contact again with controller: 10.32.48.21 (Molen3)
  E [[2018-11-27]] 11:03:08.928 Off Unit= SubDataAccess 10.32.48.21 ConnErr OPCServer 5500 Conn error to DA subscr controller
  I [[2018-11-27]] 11:03:09.451 OPC Data Access: Contact again with controller: 10.32.48.28 (Rotoseal)
  E [[2018-11-27]] 11:03:09.451 Off Unit= SubDataAccess 10.32.48.28 ConnErr OPCServer 5500 Conn error to DA subscr controller
  I [[2018-11-27]] 11:03:09.614 OPC Data Access: Contact again with controller: 10.32.48.16 (C2)
  E [[2018-11-27]] 11:03:09.614 Off Unit= SubDataAccess 10.32.48.16 ConnErr OPCServer 5500 Conn error to DA subscr controller
  I [[2018-11-27]] 11:03:10.550 OPC Data Access: Contact again with controller: 10.32.48.11 (overblazen)
  E [[2018-11-27]] 11:03:10.550 Off Unit= SubDataAccess 10.32.48.11 ConnErr OPCServer 5500 Conn error to DA subscr controller
  I [[2018-11-27]] 11:03:10.632 OPC Data Access: Contact again with controller: 10.32.48.18 (C3)
  E [[2018-11-27]] 11:03:10.632 Off Unit= SubDataAccess 10.32.48.18 ConnErr OPCServer 5500 Conn error to DA subscr controller
  I [[2018-11-27]] 11:03:10.776 OPC Data Access: Contact again with controller: 10.32.48.29 (Molen4)
  E [[2018-11-27]] 11:03:10.776 Off Unit= SubDataAccess 10.32.48.29 ConnErr OPCServer 5500 Conn error to DA subscr controller
  I [[2018-11-27]] 11:03:11.211 OPC Data Access: Contact again with controller: 10.32.48.14 (Pompstation)
  E [[2018-11-27]] 11:03:11.211 Off Unit= SubDataAccess 10.32.48.14 ConnErr OPCServer 5500 Conn error to DA subscr controller
  I [[2018-11-27]] 11:03:11.355 OPC Data Access: Contact again with controller: 10.32.48.15 (Molen4_5)
  E [[2018-11-27]] 11:03:11.355 Off Unit= SubDataAccess 10.32.48.15 ConnErr OPCServer 5500 Conn error to DA subscr controller
  I [[2018-11-27]] 11:03:11.960 OPC Data Access: Contact again with controller: 10.32.48.40 (LLZ2)
  E [[2018-11-27]] 11:03:11.960 Off Unit= SubDataAccess 10.32.48.40 ConnErr OPCServer 5500 Conn error to DA subscr controller
# [[2018-11-28]] 08:22 
  Om 6.33u
  ![image11](image11-3%201.png)
# [[2018-12-20]] 
  Kepserver in MHL op CS1 geïnstalleerd. Offerte voor licentie is aangevraagd
# [[2019-01-14]] 
  Kepserver in MHL in dienst genomen
# [[2019-02-14]] 
  Alles lijkt veel stabieler
# [[2020-05-25]] 
  Mail naar Peter Stroop gestuurd
# [[2020-06-16]] 
  Het lijkt in kepware te zitten.
  
  De tags die Bad staan in kepware, staan good in advdsopcclient.
  De Bad tags toegevoegd in Kepware Watchdog Device1.
  In UAExpert
  ![image12](image12-2%201.png)
# [[2020-07-14]] 
  Test opgezet:
  In CM MES_COMMUNICATION_BULK, een extra CM MES_OPC_Communication_Compatible toegevoegd. Dit om OPC problemen bij samengestelde datatypes te onderzoeken.
  **Zie UAEXPERT Bad Tags**
  
  Test opgezet voor:
- PML01_order
- PML05_started
- SMOB2_started
- PBA05_started
# [[2020-07-22]] 
  toegevoegd
- PML02_itemNo
- PML02_order
# [[2020-07-23]] 
  toegevoegd
- PML01_started
- PBA01_started
- PBA18_started