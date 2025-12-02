---
date created: 2025-08-01T14:22:29+02:00
date modified: 2025-09-18T22:07:22+02:00
---
[[applications/loading_app]]

# How to configure NISE 106 & DM-F12A/PC-R30 for kiosk use
- Unbox NISE 106 (Industrial Computer) and connect to power.
- Unbox iEi DM-F12A/PC-R30 (Touchscreen) and connect to power as per below picture :
  
  ![[assets/images/Pasted image 20231004121623\.jpg]]

- Connect the touchscreen to the industrial computer :
	- via DisplayPort-cable (not included in the box) **AND**
	- via USB-A to USB-A cable (included in the box)
		- This is required to have the touchscreen-functionalities enabled.
- When connected properly the device will startup.  
    The device will, by default, automatically logon with admin credentials.
- Change the computer name in the standard format (e.g. BE-DES-TDC-001)  
    _(When re-using a computer name please make sure to rename the old computer first, and rebooting it, before using the old computer name again. Otherwise it will cause problems.)_
	- Press Win + R
	- Type _sysdm. cpl_
	- Click Change (next to: To rename this computer...)
	- Change the Computer name and click OK when done.
	- Click Close and then Restart Now to restart the device
- Connect a LAN-cable to the device (this should be on the Sibelco Network)
- Change the password for user Admin to _Sibelco1872_
- Press Win + R
- type _lusrmgr.msc_
- Open Users
- Right-click Admin and click Set Password
- Click Proceed in the next window and enter twice the password mentioned above.
- Add the PC to the domain _amorg.group_ (for forklift_donk it should be sibelco-europe.amorg.group)
- Press Win + R
- Type _sysdm. cpl_
- Click Change (next to: To rename this computer...)
- Click Domain and fill in _amorg.group_  in the white box below
- Click OK when done.
- Make use of a domain-account with elevated rights
- Click OK twice
- Click Close and then Restart Now to restart the device
- Make a request in ServiceNow to have the computer name (eg. BE-DES-TDC-001) added as touchdevice in the weighbridge configuration.  
    (This step be skipped when re-using a computer name)
- Service Request Catalog / End User Services / User Access Management
- Access For Weighbridge
  
- Create a label, with a DYMO label printer, with the new computer name (eg. BE-DES-TDC-001) and stick this in the right upper corner on the device.
- Open Active Directory using an admin-account and move the computer to the relevant OU (eg. sibelco-europe.amorg.group/Global/Computers/Workspace/Staged Computers/BE/DES/Production Systems/)
- Perform a gpupdate /force
- Press Win + R
- Type cmd
- Type _gpupdate /force_
- Restart and logon with credentials _sibeur\usrwbtg0_ (pass: Sibelco2013)
- Install the latest Java RunTime Environment version (JRE)
- [https://java.com/en/download](https://java.com/en/download)
- Make use of a domain-account with elevated rights
- Restart and logon with credentials _sibeur\usrwbtg0_
- Open Internet Explorer and navigate to the relevant Weighbridge server (e.g. [http://be-des-wbs-001:59380](http://be-des-wbs-001:59380) (the URL can be different, based on location)
- Click Installation
- Under Kiosk
- Click Install Exclusive KioskOperator Client (add functions in Configurator)
- Also download the jpnl-file from the same Install Generic Load Operator Client-link and copy it to the startup folder.  
    (To directly access this startup folder, open Run, type shell:startup and hit Enter)
  
  ·         When this device will be mounted into mobile equipment with an AP then the WiFi-adapter should be disabled.
- Press Win + R
- Type _ncpa.cpl_
  
  o    Right-click the wireless adapter and select Disable
- Open Registry (right-click and Run as Admin) to setup AutoAdminLogon
- Search for _regedit_ (left below corner Search-icon)
- Right-click it and select Run as administrator
- Click on the expansion markers (>) down the navigation tree on the left to open the following key branches:
  
  Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon
- Left-click on the ‘Winlogon’ key itself to display its values in the right pane.
- If not present in the right pane, create String Values :
- DefaulDomainName
- DefaultPassword
- DefaultUserName
- AutoAdminLogon
- To create/edit String Values (based on below overview) :
  
  |   |   |
  |---|---|
  |DefaultDomainName|SIBEUR|
  |DefaultPassword|Sibelco2013|
  |DefaultUserName|usrwbtg0|
- In the right pane right-click in an empty area and hover the mouse pointer over ‘New’
- Left-click on the ‘String Value’ item in the pop-out menu.
- Type e.g. ‘DefaulPassword’ into the name box without the quotes and press the Enter key on your keyboard.
- Right-click on the value called ‘DefaultPassword’. Hit the ‘Modify…’ item in the contextual menu.
- In the Value Data text box, type your password and hit the ‘OK’ button to save it.
  
  Repeat above steps if required for f.e. DefaultDomainName.
- To create AutoAdminLogon
- Left-click on the ‘Edit’ item in the main menu area. Hover your mouse pointer over ‘New’ and left-click on the ‘String Value’ item in the pop-out menu.
- Type in ‘AutoAdminLogon’ for the value’s name and press enter.
- Right-click on the ‘AutoAdminLogon’ value and select the ‘Modify…’ item listed in the contextual menu.
- In the Value data text box, Make sure it’s value contains a 1. If it has a 0, erase it, and type in ‘1’. Select on the ‘OK’ button.
- Restart the device to do a final test, device should logon automatically and startup the Kiosk Operator Client.