---
date created: 2025-07-18
modified: 2025-08-20
---
# VMWare


## Split een monolitic disc

-  in een Prompt met admin rechten: 
	- `cd C:\Program Files (x86)\VMware\VMware Workstation`
	- `vmware-vdiskmanager –r "C:\Users\LEMTON00\OneDrive - Sibelco\Virtual machines\800xA 6.1.1\800xA_6.1.1_Template-cl1.vmdk" –t 1 "C:\Users\LEMTON00\OneDrive - Sibelco\Virtual machines\800xA 6.1.1\disk1.vmdk"`

## Installeer VMWare tools in Linux
```bash
sudo apt update
sudo apt install open-vm-tools open-vm-tools-desktop
```
Path naar de gedeelde map: `/mnt/hgfs`

### Handmatig mounten via terminal
`sudo vmhgfs-fuse .host:/ /mnt/hgfs -o allow_other`



## Serials
from https://github.com/hegdepavankumar/VMware-Workstation-Pro-17-Licence-Keys
```
MC60H-DWHD5-H80U9-6V85M-8280D
4A4RR-813DK-M81A9-4U35H-06KND
NZ4RR-FTK5H-H81C1-Q30QH-1V2LA
JU090-6039P-08409-8J0QH-2YR7F
4Y09U-AJK97-089Z0-A3054-83KLA
4C21U-2KK9Q-M8130-4V2QH-CF810
HY45K-8KK96-MJ8E0-0UCQ4-0UH72
JC0D8-F93E4-HJ9Q9-088N6-96A7F
NG0RK-2DK9L-HJDF8-1LAXP-1ARQ0
0U2J0-2E19P-HJEX1-132Q2-8AKK6
```
## Links
- [Running Obsidian in Linux in VMWare](applications/Obsidian/Running%20Obsidian%20in%20Linux%20in%20vmware.md)
