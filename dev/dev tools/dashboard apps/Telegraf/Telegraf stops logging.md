---
date created: 2025-08-01T14:22:31+02:00
date modified: 2025-09-30T16:20:25+02:00
---
#Telegraf

- # Logs from [[dev/dev tools/dashboard apps/Telegraf/Telegraf]]
  ```
  [[2023-09-26]]T07:07:40Z E! [inputs.opcua] status not OK for node HSK153_K11_power: The node id refers to a node that does not exist in the server address space. StatusBadNodeIDUnknown (0x80340000)
  [[2023-09-26]]T07:07:40Z E! [inputs.opcua] status not OK for node HSK153_K24_power: The node id refers to a node that does not exist in the server address space. StatusBadNodeIDUnknown (0x80340000)
  [[2023-09-26]]T07:07:40Z E! [inputs.opcua] status not OK for node HSK153_K25_power: The node id refers to a node that does not exist in the server address space. StatusBadNodeIDUnknown (0x80340000)
  ```
- # Actions
  Started a test on DESENG1. (D:\\software\\telegraf)
  [[2023-10-03]]
- The old version is now woking for 2 days. 
  
  [[2023-09-29]]
	- changed Telegraf to old version.
	- again log stopped at the same time as snapshot VMWare.
	- started the same Telegraf on DESSRVHIS1 as DESENG1
-
- [[2023-09-28]]
	- [[Archive/applications/MES/MES Heerlen]] [[server storage]] was also stopped at 22:27
	- added log to test Telegraf on DESENG1
	- backup of [[800xA]] starts at 7:15, so no influence
	- VMWare snapshot of [[network/des/PCs en Servers/800xA/DESSRVHIS1 1]] at 22:26 !!
	  ![[assets/images/Pasted image 20230928150615\.jpg]]
-