---
date created: 2020-06-26
tags:
  - MES
date modified: 2025-08-30
---

- # [[2020-06-26]] 
  Bunkers van MES automatisch invullen in ABB.
  
  Men mag nog enkel op Start drukken in ABB ter bevestiging.
  
  Hiervoor moet eerst het MES objectl worden herzien.
  Zie [800xA Library - MES](onenote:https://d.docs.live.net/648fe635197c5860/Docs/OneNote's/Persoonlijk%20(web)/Personal/Computer/Develop/Ontwikkeling%20800xA.one#800xA%20Library%20-%20MES&section-id={CFC7F9A5-4F11-4063-BECD-A548B673DB61}&page-id={C26BB0A8-F317-4B54-984C-113C6DF23E26}&end)
- # [[2021-09-13]] 
  Underlying voor PML01 is in test omgeving gemaakt
- # [[2021-09-20]] 
  \<!-- PML01 - MOLEN 1 --\>
  \<tag code="M1_Tonnage"  group="kepware" id="NS2\|String\|800xA.MES.PML01.PML01_Counter_production" handlingtype="READ" \>
  \<option code="DEADBAND" value="yes" /\>
  \<option code="DEADBAND.TYPE" value="ABSOLUTE"/\>
  \<option code="DEADBAND.VALUE" value="0.01"/\>
  \</tag\>
  \<tag code="M1_Source1"  group="kepware" id="NS2\|String\|800xA.MES.PML01.PML01_Source1_locationId" handlingtype="READ" /\>
  \<tag code="M1_Dest1" group="kepware" id="NS2\|String\|800xA.MES.PML01.PML01_Dest1_locationId" handlingtype="READ" /\>
  \<tag code="M1_started" group="kepware" id="NS2\|String\|800xA.MES.PML01.PML01_Started"  handlingtype="READWRITE" /\>
  \<tag code="M1_Item_No" group="kepware" id="NS2\|String\|800xA.MES.PML01.PML01_ItemNo"  handlingtype="READWRITE" /\>
  \<tag code="M1_Item_No_Plc" group="kepware" id="NS2\|String\|800xA.MES.PML01.PML01_ItemNoPlc"  handlingtype="READ" /\>
  \<tag code="M1_Job_Rid" group="kepware" id="NS2\|String\|800xA.MES.PML01.PML01_JobRid"   handlingtype="READWRITE" /\>
  \<tag code="PML01_Order_no" group="kepware" id="NS2\|String\|800xA.MES.PML01.PML01_Order"  handlingtype="READWRITE" /\>
  \<tag code="PML01_kWh"  group="kepware" id="NS2\|String\|800xA.MES.PML01.PML01_kWh" handlingtype="READ" \>
  \<option code="DEADBAND" value="yes" /\>
  \<option code="DEADBAND.TYPE" value="ABSOLUTE"/\>
  \<option code="DEADBAND.VALUE" value="0.01"/\>
  \</tag\>
  \<tag code="PML01_ActiveEnergyImport" group="kepware" id="NS2\|String\|800xA.MES.PML01.ActiveEnergyImport" handlingtype="READ" \>
  \<option code="DEADBAND" value="yes" /\>
  \<option code="DEADBAND.TYPE" value="ABSOLUTE"/\>
  \<option code="DEADBAND.VALUE" value="0.01"/\>
  \</tag\>
  
  \<tag code="PML01_toerental_separator_1" group="kepware" id="NS2\|String\|800xA.Plant.M1.M1RS301_Speed" handlingtype="READ" /\>
  \<tag code="PML01_omloop" group="kepware" id="NS2\|String\|800xA.Plant.M1.M1WHC112_SP" handlingtype="READ" /\>
  \<tag code="PML01_stroom_hoofdmotor" group="kepware" id="NS2\|String\|800xA.Plant.M1.M1MI101IT" handlingtype="READ" /\>
  
  **Dit zijn de nieuwe tags**
  \<tag code="PML01_LOCATION_REQUEST_TYPE" description="" group="kepware" id="" handlingtype="READWRITE"/\>
  \<tag code="PML01_LOCATION_REQUEST_SEQUENCE" description="" group="kepware" id="" handlingtype="READWRITE"/\>
  \<tag code="PML01_LOCATION_REQUEST_LOCATION_ID" description="" group="kepware" id="" handlingtype="READWRITE"/\>
  \<tag code="PML01_LOCATION_REQUEST_ITEM_ID" description="" group="kepware" id="" handlingtype="READWRITE"/\>
  \<tag code="PML01_LOCATION_REQUEST_ITEM_NAME" description="" group="kepware" id="" handlingtype="READWRITE"/\>
  \<tag code="PML01_LOCATION_REQUEST_BATCH_ID" description="" group="kepware" id="" handlingtype="READWRITE"/\>
  \<tag code="PML01_LOCATION_REQUEST_QTY_PLANNED" description="" group="kepware" id="" handlingtype="READWRITE"/\>
  \<tag code="PML01_LOCATION_REQUEST_START"  description="" group="kepware" id="" handlingtype="READWRITE"/\>
  \<tag code="PML01_LOCATION_REQUEST_STATUS_CODE" description="" group="kepware" id="" handlingtype="READWRITE"/\>
  \<tag code="PML01_LOCATION_RESPONSE_AVAILABLE" description="" group="kepware" id="" handlingtype="READ"/\>
  \<tag code="PML01_LOCATION_RESPONSE_LOCATION_ID" description="" group="kepware" id="" handlingtype="READ"/\>
  \<tag code="PML01_LOCATION_RESPONSE_STATUS_CODE" description="" group="kepware" id="" handlingtype="READ"/\>
- # [[2021-09-20]] 15:58 
  Jochem was nog met de test server bezig.
- # [[2021-09-21]] 
  en vandaag ook
  en met lemton00 werken is niet niet werkbaar
- # [[2021-11-24]] 
  ![image1](image1-24%201.png)
  
  ![image2](image2-17%201.png)
  
  Het starten van een MO (PML01_Test) in de testomgeving duurt : 42 seconden
- # OPC:Signals heeft een test scherm
  ![image3](image3-12%201.png)
- #
- # PML01_Dst1 heeft een knoppen scherm
  ![image4](image4-6%201.png)
- #
- #
- # [[2022-04-28]] TODO en vordering
- # [[2022-07-05]] 
  gisteren had stijn een fout in de config gevonden. maar is nog niet actief
- # Koppeling OPC. Starten en Stoppen van een MO komt in ABB terecht
  
  | C2      | ok                                                                                                                                                     |
  |---------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
  | C3      | [[2022-04-28]] getest. de bunker volgorde klopt niet en er wordt meermaals een bunker naar destination1 geschreven. Een mail hiervoor naar Stijn gestuurd. |
  | D3      | ok                                                                                                                                                     |
  | D4      | geen MO beschikbaar                                                                                                                                    |
  | M1 / M2 | [[2022-04-28]] Molens draaien                                                                                                                              |
  | M3      | [[2022-04-28]] Molen draait                                                                                                                                |
  | M4      | [[2022-04-28]] Molen draait                                                                                                                                |
  | [[installations/des/molens/Molen5/Molen 5]] |                                                                                                                                                       |
- # Koppeling Item
  | C2      | OK:                                                                                                                   |
  |---------|-----------------------------------------------------------------------------------------------------------------------|
  | C3      |                                                                                                                      |
  | D3      |                                                                                                                      |
  | D4      |                                                                                                                      |
  | M1 / M2 | [[2022-04-28]] : M1 en M2 draaien. Het is niet te doen om live PML01 en PML02 om te zetten naar gemeenschappelijke velden |
  | M3      | OK: Omzetten als M3 stil ligt                                                                                         |
  | M4      | OK:                                                                                                                   |
  | [[installations/des/molens/Molen5/Molen 5]]      | OK:                                                                                                                   |