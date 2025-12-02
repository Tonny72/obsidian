---
title: Opvolging Emde
updated: [[2022-01-21]]T13:39:31.0000000+01:00
created: [[2019-04-25]]T12:10:21.0000000+02:00
---

- # [[2019-04-25]]
  Extra tags gelogd:
- IO.AF12_Grof.IOValue: Er wordt een MES_Pallet_request gestuurd op basis van IO.AF12_Grof.IOValue
- PalletNr die naar Emde wordt gestuurd: IO.AF12_DP_DP_Out6.IOValue
- # [[2019-05-10]] 
  Ondertussen al twee belangrijke aanpassen gedaan
  1.  Updates van de status liepen niet altijd goed
  
  ![image1](image1-61%201.png)
  
  Dit eruit gezwierd voor aansturing labelprinter
  ![image2](image2-37%201.png)
- # [[2019-05-14]] 
  Mails emde
  
  **Von:** Stijn Vandenbroucke \[[mailto:stijn.vandenbroucke@linkworx.eu](mailto:stijn.vandenbroucke@linkworx.eu)\]
  **Gesendet:** Samstag, 4. Mai 2019 09:25
  **An:** Heck, Ralph
  **Cc:** Jochem Janssen; Harry Stienen
  **Betreff:** RE: Big-Bag position follow up EMDE automatic
  
  Dear Ralph,
  
  As promised a small functional description of the communication between MES and the conveyor.
  
  If the weighing silo is filled, that quantity should get a lot and pallet number ; that information is followed position per position on the conveyor in the EMDE PLC
  
  We have 4 tags in the datablock for that:
  1. PLC -\> MES (bit): request pallet information (PALLET_REQUEST)
  
  2. MES -\> PLC (dint): lot number (PALLET_REQUEST_LOT_CODE)
  
  3. MES -\> PLC (dint): pallet number (PALLET_REQUEST_PALLET_CODE)
  
  4. MES -\> PLC (bit): confirm pallet request (PALLET_REQUEST_CONFIRM)
  
  Functionality:
  1. Emde plc knows that pallet information is required for the quantity in the weighing silo
  
  • PLC write: PALLET_REQUEST = true
  
  2. MES read (PALLET_REQUEST = true)
  
  • MES will generate the lot and pallet number:
  
  \- MES wirte: PALLET_REQUEST_LOT_CODE = 201905040001
  
  \- MES write: PALLET_REQUEST_PALLET_CODE = 1
  
  \- MES write: PALLET_REQUEST_CONFIRM = true
  
  3. PLC read (PALLET_REQUEST_CONFIRM = true)
  
  • PLC can take the lot and pallet information ; this is the start of the follow up position per position
  
  • If the plc has handled the data: PLC wite: PALLET_REQUEST = false
  
  4. MES read (PALLET_REQUEST = false):
  
  • MES will reset the communication:
  
  \- MES wirte: PALLET_REQUEST_LOT_CODE = 0
  
  \- MES write: PALLET_REQUEST_PALLET_CODE = 0
  
  \- MES write: PALLET_REQUEST_CONFIRM = false
  
  \[For information: this data is now coming via de DP-DP coupler with ABB\]
  
  Other tags that should be available in the datablock:
- Pallet information (lot code, pallet code and weight) on the following positions:
	- Pallet label position
	- Last 2 positions of the conveyor (where operator is taken the palllets).
	  
	  If any question, please do not hesitate to ask.
	  
	  Br,
	  Stijn Vandenbroucke.
	  
	  -----------------------------------------------------------------------------------------------------------------------------------------------
	  
	  **Van:** <Ralph.Heck@emde.de> \<<Ralph.Heck@emde.de>\>
	  **Verzonden:** donderdag 9 mei 2019 10:15
	  **Aan:** Stijn Vandenbroucke \<<stijn.vandenbroucke@linkworx.eu>\>
	  **CC:** Jochem Janssen \<<Jochem.Janssen@sibelco.com>\>; Harry Stienen \<<Harry.Stienen@sibelco.com>\>
	  **Onderwerp:** AW: Big-Bag position follow up EMDE automatic
	  
	  Good Mornig,
	  
	  I had a look into our PLC program and I have some questions regarding your request.
- How will the Data from MES get into our PLC? Same way like now from the ABB System?
- I assume, the remaining Communication should stay in place.
- Right now the format of the Lot Numer is an Array of 3 Dint, will that remain?
- Right now there is no Pallet Number, we use BigBag Number. Do you mean the same, or do you want a Pallet Number instead or in addition to the BigBag Number.
  
  Regarding the doubling of the BigBag Number, I talked to the guys from Software Engineering.
  There are 2 posibilities:
  1.  Manual interaction from the operator. E.g. if there is a problem somewhere and the operator switches to manual and moves a pallet manually.
  2.  The Lot Number and the BigBag Number is not supplied by the ABB System, when we start the filling process. In this case we still have the old Number in the DP-DP coupler. (There is no Handshake regarding the Lot Number and BigBag Number)
  
  If you want, we can have another phone call.
  
  Kind regards
  
  *Mit freundlichen Grüßen / Kind Regards*
  
  *Ralph**Heck*
  *Service Technician*
  
  ------------------------------------------------------------------------------------------------------------------------------------
  
  **Von:** Stijn Vandenbroucke \[[mailto:stijn.vandenbroucke@linkworx.eu](mailto:stijn.vandenbroucke@linkworx.eu)\]
  **Gesendet:** Donnerstag, 9. Mai 2019 10:23
  **An:** Heck, Ralph
  **Cc:** Jochem Janssen; Harry Stienen
  **Betreff:** RE: Big-Bag position follow up EMDE automatic
  
  Hi Ralph,
  
  Thanks fort he feedback!
  
  About your questions:
  1.  How will the Data from MES get into our PLC? Same way like now from the ABB System?
  The information should come into your plc using the logic described below. You reserve a datablock in the Siemens plc, where you have some tags that will be exchanged (via OPC) with the MES system.
  
  If this is not clear, we shoudl have a call.
  
  1.  I assume, the remaining Communication should stay in place
  Correct.
  
  1.  Right now the format of the Lot Numer is an Array of 3 Dint, will that remain?
  Lotnumber will stay exactly the same (10 digits)
  
  2.  Right now there is no Pallet Number, we use BigBag Number. Do you mean the same, or do you want a Pallet Number instead or in addition to the BigBag Number.
  I mean the same (pallet is just a bit more general then bigbag)
  
  About the possible cause:
  I completely understand that these cases can run into the issue and these are the same as our expectations ;
  the handshake can be the biggest issue as this results into a not understandable situation for the operator.
  
  If everything is clear, can you make an estimate for the change required?
  
  Br, Stijn.
  
  -----------------------------------------------------------------------------------------------------------------------------------------------
  **Van:** <Ralph.Heck@emde.de> \<<Ralph.Heck@emde.de>\>
  **Verzonden:** vrijdag 10 mei 2019 15:07
  **Aan:** Stijn Vandenbroucke \<<stijn.vandenbroucke@linkworx.eu>\>
  **CC:** Jochem Janssen \<<Jochem.Janssen@sibelco.com>\>; Harry Stienen \<<Harry.Stienen@sibelco.com>\>
  **Onderwerp:** AW: Big-Bag position follow up EMDE automatic
  
  Hello Stijn,
  
  the question I have is, how should we proceed, if we are ready to fill the big bag and did not receive a Lot Nr and BigBag Nr from MES at this time?
  I would recommend, to use 0 for Lot and BB Nr.
  The operator has the possibility toe enter the Lot and BB Nr. later on the touchscreen of the PLC.
  
  Have a nice weekend.
  
  Kind regards
  
  ----------------------------------------------------------------------------------------------------------------------------------------
  
  **From:** Stijn Vandenbroucke \<<stijn.vandenbroucke@linkworx.eu>\>
  **Sent:** vrijdag 10 mei 2019 15:43
  **To:** <Ralph.Heck@emde.de>
  **Cc:** Jochem Janssen \<<Jochem.Janssen@sibelco.com>\>; Harry Stienen \<<Harry.Stienen@sibelco.com>\>
  **Subject:** RE: Big-Bag position follow up EMDE automatic
  
  Hi Ralph,
  
  I prefer a manual confirmation by the operator:
- “Retry“ = Request pallet again (= make request bit low + wait 1 second + make high again)
- “Confirm manual” = use 0 for lot and BB nr.
  
  We suppose that this scenario also happens today but have not any control on it (probably due missing handshake / network delay / …).
  If it happens, the labelmachine will block later on in the process and will require extra effort of the operator to label manual, ...
  
  Have a good weekend!
  Best regards,
  Stijn.
- # [[2019-05-14]] 14:21 
  Geert Staes heeft Emde gecontacteerd, maar ze hebben nog niks laten weten.
- # [[2019-05-22]] 
  Aanpassing status lamp uitgevoerd
- # [[2019-05-24]] 
  Neem staal vanuit Lab dispatcher geprogrammeerd
- # [[2019-10-08]] 
  Dit is terug in handen van KR