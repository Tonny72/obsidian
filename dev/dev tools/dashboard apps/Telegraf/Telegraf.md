---
modified:  2025-08-29
date created: 2025-08-01T00:00:00+02:00
date modified: 2025-09-30T20:22:32+02:00
---
# Testomgeving
Zie file:///C:\Users\lemton00\Sibelco\Elektrische%20Dienst%20en%20Automatisering%20-%20Documents\Automatisering\Toepassingen\Telegraf
- # Python 
  ```
  [[inputs.exec]]
  commands = [ "python3 run.py" ]
  data_format = "influx"
  timeout = "15s"
  ```
- # Issues
  [[dev/dev tools/dashboard apps/Telegraf/Telegraf stops logging]]
-
- # [[network/des/PCs en Servers/800xA/DESSRVHIS1 1]]
	- [[dev/dev tools/dashboard apps/Telegraf/Telegraf]] "H:\\Influxdb\\telegraf.exe"
		- version: 1.23.1-686717fe
	- [[dev/dev tools/dashboard apps/Telegraf/Telegraf]] OPCUA ""H:\\telegraf_opcua\\run telegraf.bat"
	- ### Telegraf as a service
		- ```
		  telegraf.exe --service install --config H:\telegraf_opcua\telegraf.conf --config-directory H:\telegraf_opcua\telegraf.d --service-name telegraf-opcua --service-display-name "Telegraf OPCUA"
		  ```
		- In the config-file, set the logfile in this format
			- ```toml
			  logfile = "h:\\influxdb\\log\\service_log.txt"
			  ```
			-
-