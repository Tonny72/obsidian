
tags:
  - "#network"
IP: 10.32.29.11
links:
  - - SQL server
aliases:
  - DES-800xA-Test
description: (draait op ESX-009)

# Warning 
Gebruik deze niet als fileserver!
# SQL Server
- user: sa
- pw: Sibelco01
# Firewall rules
- Grafana: TCP 3000
- SQL server: UDP 1434, TCP 1433
```shell
New-NetFirewallRule -DisplayName "SQLServer default instance" -Direction Inbound -LocalPort 1433 -Protocol TCP -Action Allow
New-NetFirewallRule -DisplayName "SQLServer Browser service" -Direction Inbound -LocalPort 1434 -Protocol UDP -Action Allow
```
- Remote Desktop TCP 3389
- File and Printer Sharing (Echo Request - ICMPv4-In) PING: Protocol type ICMPv4 (enkel voor private network)
# Networks
- Production (10.32.29.11)   Firewall Private network
- Office (10.32.18.131) Firewall Public Network
- File and Printer Sharing (Echo request ICMPv4-In) 
  ![[assets/images/Pasted image 20240905131924\.jpg]]
- File and Printer Sharing (NB-Session-In)
	- Bij scope 10.32.25.0/24 toevoegen
- File and Printer Sharing (SMB-In)
	- Bij scope 10.32.25.0/24 toevoegen
# Log
## 2024-09-25
Als je op een 800xA server een mapping wil leggen naar \\10.32.29.11\automatisering wil leggen, dan loopt de 800xA Server vast. Als je hetzelfde doet op een ABB client, dan is er geen probleem.
Een andere share-naam lukte in eerste instantie wel, maar na een reboot werkte het weer niet.
![[assets/images/Pasted image 20240905123704\.jpg]]