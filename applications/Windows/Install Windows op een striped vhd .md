---
date created: 2013-05-14
modified: 2025-07-21
---
# Install Windows op een striped vhd 

Install Windows op een striped vhd
dinsdag 14 mei 2013
9:12

Boot de installatie Win8

Wanneer "Windows 8 Install now" op scherm komt druk Shift F10

List disk

Select disk=0
Convert dynamic
Select disk=1
Convert dynamic
Create volume stripe disk=0,1
Format
List volume
Select volume=x
Assign letter=L
Create vdisk file=L:\win.vhd maximum=120000 type=expandable
Attach vdisk

Install Windows
![image1](image1-32.png)
