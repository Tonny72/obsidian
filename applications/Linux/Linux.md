---
date created: 2025-10-19T11:31:37+02:00
date modified: 2025-12-02T11:36:57+01:00
---
[[2025-10-19]]: Noticed that Windows has become slow propbly due to the Defenceder advanced thread protector. Time to evaluate some linux distro's.

## Distro's

Limit the evaluation to these distro's
- Ubuntu
- Pop!OS
- Mint

## Installation
- Both a USB disk and the T5 SSD are needed.
- Do not use Rufus, Use Ventoy. With Ventoy you only have to copy the .iso files to the USB stick.
- Install Ventoy of USB stick.
- Download the linux ISO file(s) and copy them on the USB stick

### Installing Running linux on [[computer/Hardware/HP Zbook]].
- Safe boot in BIOS must be disabled. 

> [!NOTE]
> **Be carefull, this results in a bitlocker problem. Keep the bitlocker recovery codes nearby.**
- Boot from the USB stick and follow instructions.
	- Ubuntu: choose Erase disk and install Ubuntu. You can select which disk afterwarts.
- Booting from the T5 SDD. Choose in Boot from file

## [[Linux Mint]]
- PyCharm and VSCode or not in the standard software manager.

## [[Ubuntu]]
- PyCharm and VSCode are in the App Center.
- Seems to be the most popular.

## [[Pop!OS]]
- PyCharm and VSCode are in the software manager.
- ❌ Big launcher in the middle of the screen and also a bar in the top of the screen.

## Log
[[2025-10-19]]: Giving Ubuntu a shot.


## Howto mount [[applications/OneDrive]]
### Install [[installations/common/Rclone|Rclone]]
- sudo apt update
- sudo apt install rclone

### Configure [[applications/OneDrive|OneDrive]] in [[installations/common/Rclone|Rclone]]
- rclone config
- new
- name: OneDrive
- 30) Microsoft Onedrive
- Accept default options
- 1) Microsoft Cloud Global
- 3) OneDrive (Personal)

Test
```cmd
rclone ls OneDrive:
```

### Mount Onedrive manual
- mkdir -p ~/OneDrive
- rclone --vfs-cache-mode writes mount onedrive: ~/OneDrive --daemon
- test: `ls OneDrive`


## Sync [[applications/OneDrive]] locally
- sudo apt install onedrive