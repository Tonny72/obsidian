---
date created: 2020-07-07T10:08:00
sticker: ""
modified: 2025-07-21
---
# RDP - Remote Desktop

## RDP full screen op 2 van de 3 monitoren
  
  use multimon:i:1
  selectedmonitors:s:0,1,2
  
  Om monitor nummers op te lijsten
  MSTSC /l
  
  mRemoteNG
  
  [Default.rdp](Default.rdp)
  
  Da marcheert :-)
  Dit is het enige dat in de .rdp file staat
  
  prompt for credentials:i:1
  administrative session:i:1
  screen mode id:i:2
  span monitors:i:1
  use multimon:i:1
  selectedmonitors:s:3,4,5
  
  ---
- # CTRL-ALT-DEL in RDP
  CTRL-ALT-DEL in RDP
  => CTRL-ALT-END
- # Copy - Paste werkt niet wanneer RDP actief
  Volgens [Copy/paste not working while RDP MS Remote Desktop Connection is running - Super User](https://superuser.com/questions/1587903/copy-paste-not-working-while-rdp-ms-remote-desktop-connection-is-running)
  ```
  taskkill /f /im rdpclip.exe
  rdpclip.exe
  ```