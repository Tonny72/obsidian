---
tags: [Linux]
modified:  2025-07-22
date created: 2020-11-02T00:00:00+02:00
date modified: 2025-10-19T22:14:29+02:00
---
# Linux Commands

## Detecteer nieuwe disks
  sudo rescan-scsi-bus
  *From \<<https://askubuntu.com/questions/1054612/how-to-reset-and-detect-plug-in-hdd-ssd-via-ide-or-sata-without-rebooting>\>*
## Creeer Zpool
  sudo zpool create tank mirror sdb sdc mirror sde sdd
## Toon disks
  Fdisk -f (fixed disk setup)
  Of
  Lsblk (lists block devices)
# Format
  Mkfs.brfs /dev/sdb
# btrs
  sudo mkfs.btrfs -f -m raid1 -d raid1 /dev/sdb /dev/sdc
  
  sudo btrfs device add -f /dev/sde /mnt/btrfs
# Toon UUID
  sudo btrfs filesystem show
  
  df = toont free disk space
  df -h (human readable)
# Herstart rdp service
  sudo systemctl disable xrdp
  
  *Van \<<https://raspberrypi.stackexchange.com/questions/87590/how-to-stop-xrdp-service-from-autostarting>\>*