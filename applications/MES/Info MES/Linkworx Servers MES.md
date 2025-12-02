---
title: Linkworx Servers MES
date created: 2016-05-18T12:16:32+02:00
tags: [MES]
date modified: 2025-10-20T20:32:32+02:00
---
# DESSEL
## Productie
MES
  Server: BE-DES-APS-031 (10.32.19.80)
  Weblink: <http://be-des-aps-031:59171/>
  Directory: [\\\be-des-aps-014\c\$\linkworx\sites\DES\server_mes](file://be-des-aps-014/c$/linkworx/sites/DES/server_mes)  
  UA: opc.tcp://dessrvac800cs2:59153/linkworx/UAServer
## Storage
  server: BE-DES-APS-031
  Weblink: <http://be-des-aps-031:59181/?module=tagoverview>
## PBA18
  Server: CS1 (10.32.29.30)
  Weblink: <http://10.32.29.30:59250/>
### DA-LOG1
  Server: CS1 (10.32.29.30)
  Weblink: <http://10.32.29.30:59254/>
  Directory: "[\\\10.32.29.30\c\$\linkworx\server_da_log](file://10.32.29.30/c$/linkworx/server_da_log)"
### ENG
  Server: Eng1 (10.32.29.100)
  Weblink: <http://10.32.29.100:59253/>
  Directory: [\\\10.32.29.100\c\$\linkworx\server_da_mes](file://10.32.29.100/c$/linkworx/server_da_mes)
### ENG Hist
  Directory: [\\\10.32.29.100\c\$\linkworx\linkworx_hist\server_hist](file://10.32.29.100/c$/linkworx/linkworx_hist/server_hist)
  
  HIST: <http://10.32.29.100:59271/?module=joboverview&command=execute&reference=datalogger.getdata$kwh_PML01_02/kwh_PML01_02>
### SIEMENS
  Server: BEDESSIOPC
  Weblink: <http://bedessiopc:59160/>
  Directory: [\\\BEDESSIOPC\c\$\linkworx\server](file://BEDESSIOPC/c$/linkworx/server)
## Rosa - Server (lab dispatcher)
![[Sibelco/installations/des/drogers en calcineeroven/C3/Rosa]]
## Test
- ### MES
  Server: BE-DES-APS-015 (10.32.17.31)
  Weblink: <http://be-des-aps-953:59271>
  Directory: [\\\be-des-aps-015\c\$\linkworx\sites\DES\server_mes](file://be-des-aps-015/c$/linkworx/sites/DES/server_mes)
  UA: opc.tcp://dessrvac800cs2:59153/linkworx/UAServer
## Loading APP
  Server: CS1 (10.32.29.30)  
  Weblink: <http://10.32.29.30:59160/>
  Directory: [\\\10.32.29.30\c\$\opcuaserver](file://10.32.29.30/c$/opcuaserver)
## Loading VZ
  Server: CS1 (10.32.29.30)
  Weblink: <http://10.32.29.30:59255/>
  Directory: [\\\10.32.29.30\c\$\opcuaserver](file://10.32.29.30/c$/opcuaserver) 
  
-------------------------------------------------------------------------------------------------------
# LOMMEL
## Productie
### MES
  Server: [[BE-DES-APS-015]] (10.32.17.27)
  Weblink: <http://be-des-aps-031:60171>
### LOG
  Server: [[BE-DES-APS-014]] (10.32.17.27)
  Weblink: <http://be-des-aps-014:60173>
## Test
### MES
  Server: [[BE-DES-APS-015]] (10.32.17.31) 
  Weblink: <http://be-des-aps-015:59251>
  Directory: [\\\be-des-aps-015\c\$\linkworx\sites\MHL\server_mes](file://be-des-aps-015/c$/linkworx/sites/MHL/server_mes)
   
  -------------------------------------------------------------------------------------------------------
# Maasmechelen
## Productie
### LOG en DA_LOG
  Server: CS2 (10.32.84.22)
  Weblink: <http://10.32.84.22:59160/> (werkt niet, firewall moet worden aangepast)
  Directory: [\\\10.32.84.22\c\$\linkworx\monitoringserver](file://10.32.84.22/c$/linkworx/monitoringserver)
 
 # Heerlen
## DA-MES (TEST) → DEZE IS UIT DIENST 
zie [IFix Info ([[2022-03-11]])](onenote:..\..\Installaties\HRL\IFix.one#IFix%20Info%20([[2022-03-11]])&section-id={5E2523D4-01C6-4B88-A684-2E2B3B7E0E5A}&page-id={15229ED4-1E41-43A6-A2D0-575F5A067BFC}&end&base-path=https://sibelco-my.sharepoint.com/personal/tonny_lemmens_sibelco_com/Documents/Sibelco%20-%20Onedrive%20Personal)
  MES maakt rechtstreeks verbinding
  ~~Server: 10.31.250.40 (ifix)~~
  ~~Weblink: <http://10.31.250.40:59171/?module=tagoverview>~~
## MES
  Server: NL-HRL-APS-002
  Weblink: <http://nl-hrl-aps-002:59171/>
  Weblink Enkel OPC <http://nl-hrl-aps-002:59271/>
  ~~Na het herstarten van de IFIX server, moet de linkworx service worden herstart.~~