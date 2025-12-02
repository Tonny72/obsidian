---
tags: [weighbridge]
modified: 2025-07-21
date created: 2025-05-26T00:00:00+02:00
date modified: 2025-10-20T20:45:13+02:00
---
# loading_app
- Loading App service is geïnstalleerd op **[[network/DESSRVAC800CS1]]**
- Inloggen in loading app
	- user: liejoo00
	- pw: Liejoo01
- SQLServer: [[network/des/PCs en Servers/BE-DES-SQL-003 2]]
	- database: LoadingApp
	- user: loadingapp
	- pw: loading
	-
- # Query LOGGED_ON_LICENSEPLATES
	- ```sql
	  SELECT LICENSEPLATE_CODE AS licenseplate,
	  	LICENSEPLATE_NUMERICREF  AS licenseplateNumericRef,
	      LICENSEPLATE_BADGE       AS badge,                           
	      LICENSEPLATE_PINCODE     AS pincode,
	      CARRIER_CODE             AS carrierName,
	      CARRIER_DESCRIPTION      AS carrierDescription,
	      CUSTOMER_CODE            AS customerName,
	      CUSTOMER_DESCRIPTION     AS customerDescription,
	      ITEM_CODE                AS productName,
	      ITEM_DESCRIPTION         AS productDescription,
	      BUNKERGROUP_CODE         AS bunkerGroupName,
	      BUNKER_CODE              AS bunkerName,
	      BUNKER_PERCENT           AS bunkerPercent,
	      QUANTITY_TOLOAD          AS toLoadWeight,
	      QUANTITY_MAXTOLOAD       AS maxLoadWeight,
	      QUANTITY_UNIT            AS unit,
	      LOADING_LOADERREQUIRED   AS loaderRequired,
	      LICENSEPLATE_EMPTYWEIGHT AS emptyWeight,
	      LOADING_LABCHECK         AS labCheck,
	      DELIVERY_NR              AS deliveryNumber
	  FROM VIEW_LOGGED_ON_LICENSEPLATES
	  WHERE LICENSEPLATE_PINCODE = '{0}'
	  	AND   BUNKER_PERCENT > 0
	  ```
- # Terminals
	- [[network/des/loading terminals/BE-DES-TDC-023 1]] : BU123-BU125
	- (CAL) [[network/des/loading terminals/BE-DES-TDC-019 1]]: BU52
	- [[BE-DES-TDC-017 1]]:
	- [[network/des/loading terminals/BE-DES-TDC-016 1]]: Meelkanaal
	- [[network/From ipadressen excel/BE-DES-WBT-008]]: Oude weegbrug
	- [[network/des/loading terminals/BE-DES-TDC-021 1]]: Zandkanaal
	- [[network/des/loading terminals/BE-DES-TDC-004 1]]: Bunkers71-74