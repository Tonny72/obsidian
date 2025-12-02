---
date created: 2018-03-26
date modified: 2025-08-31
---

- ## ESXi server
  User: ifixadmin
  Pw: A2ifi12. (inclusief punt)
  IP ESX server: 10.31.250.29
  (als je op het Ifix netwerk zit 10.31.244.200. Timo en Tom gebruiken dit)
  
  <https://10.31.250.29/ui/#/login> gebruik chrome of firefox
  
  **BOOTEN van de ESXi server duurt 5 minuten**
- ## IFIX Server
  IP Adres = (office) en 10.31.244.50 (IFIX netwerk)
  
  PASWOORD IN DAMEWARE is A2ifi12 (zonder punt)
  
  Linkworx server: <http://10.31.250.40:59171/>
  
  ~~(om naar [\\\10.31.250.40\d\$](file://10.31.250.40/d$) te kunnen moet SMB1 geactiveerd worden)~~
  [[2018-12-07]]: Dit lukt niet =\> Wel op VM Automation
- # HERINSTALLATIE van ESXi
- ## Installatie ESXi
  ESXi kan van de Vmware site worden gedownload.
  Hier staat versie 6.7 "[\\\bedesnas1\Production_Software\Software\VmWare ESXi\VMware-VMvisor-Installer-6.7.0.update02-13006603.x86_64.iso](file://bedesnas1/Production_Software/Software/VmWare%20ESXi/VMware-VMvisor-Installer-6.7.0.update02-13006603.x86_64.iso)"
  
  Brand de ISO en boot hiermee op de server. ESXi kan zo op een USB worden geïnstalleerd.
- ## Enable PCI Profibus kaart
  Log aan met Chrome of Firefox.
  
  Manage Host - Hardware - PCI devices
  Toggle Siemens AG SIMATIC kaart en reboot.
  De server moet passthrough ondersteunen. IBM x3550 M3 odersteund dit niet. IBM x3550 M4 ondersteund dit wel.
  
  Als de Siemens kaart niet zichtbaar is, probeer een ander slot en mogelijk de spanning eraf om de kaart zichtbaar in ESXi te maken.
  
  ![image1](image1-271.png)
- ## Restore van VM backup
  Om bestanden van en naar ESXi te kopieren is WinSCP nodig. En SSH moet enabled worden in de ESXi services.
  Na een restore moet .vmx bestand worden aangepast en lijnen met pci passthrough worden verwijderd.
  
  Bij Virtual Machines, create / Register VM en verwijs naar de restored .vmx file
  
  Verwijder de passtrough uit de .vmx file
  
  Dit verwijderen anders start de VM niet op
  ~~pciPassthru0.id = "12:00.0"~~
  ~~pciPassthru0.deviceId = "0x4069"~~
  ~~pciPassthru0.vendorId = "0x110a"~~
  ~~pciPassthru0.systemId = "53df6eeb-079e-0ee4-6608-e41f13eeb2da"~~
  ~~pciPassthru0.pciSlotNumber = "160"~~
  
  pciPassthru0.id = "00000:006:00.0"
  pciPassthru0.deviceId = "0x4069"
  pciPassthru0.vendorId = "0x110a"
  pciPassthru0.systemId = "5cf50c99-bcb9-376f-cf64-f40343fc506c"
  pciPassthru0.present = "TRUE"
  
  Na het aanpassen van de .vmx file, unregister en register de VM
  Passtrough is een echt geklungel :-(
- ## Netwerk
  Bij Networking - Port groups, voeg een Port group *IFix*
  
  Bij Networking - Virtual switches, voeg een virtual switch toe.