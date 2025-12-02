tags:: Toepassingen

- ### Memory requirements of plc
	- => Program Info
	- ![image.png](assets/images/image_1734419044350_0\.jpg)
- ### Memory & CPU usage
	- Rechts-klik - Online & Diagnostics
	- ![image.png](assets/images/image_1734419171468_0\.jpg)
- ### Download without reinitialization
	- Kies **Program blocks** in het project
	- Klik **Overview** button 
	  ![image.png](assets/images/image_1734425075869_0\.jpg)
	- Vink **Download with reinitialization** aan.
	  ![image.png](assets/images/image_1734425142032_0\.jpg)
-
- ### STOP mode
	- |Error|S7-1200|S7-1500|
	  |--|--|--|
	  |Cycle monitoring time exceeded once|RUN|STOP (when OB80 is not configured)|
	  |Cycle monitoring time exceeded twice|STOP|STOP|
	  |Programming Error|RUN|STOP (when OB121 is not configured)|
	- #### (Error) OBs:
		- OB80: "Time error interrupt" is called by the operating system when the maximum cycle time of the controller is exceed.
		- OB121: "Programming error" is called by the operating system when an error occurs during program execution.
		- OB100: Startup
		- OB30: Cyclic interrupt