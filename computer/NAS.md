---
date created: 2020-04-28
modified: 2025-07-22
---
## [[2020-04-28]] 
  Op zoek naar een NAS distro.
### FreeNAS: 
  Heeft al een tijdje stabiel gedraaid, ZFS laat snapshots toe, maar laat geen uitbreidingen toe, of er kunnen geen disk worden samengenomen.
### OpenMediaVault
  Een snapshot maken lukte enkel als er dubbel diskspace beschikbaar was.
### Fedora server
  Geen ZFS
### XigmaNAS
  Deze lijkt het allemaal te hebben
- ZFS
- Snapshots
- Syncthing
- File explorer
  
  <https://www.freenas.org/freenas-vs-xigmanas/>
  FreeNAS heeft build in onedriveSync

## [[2020-05-26]] 
Ik krijg het niet gevonden om OneDrive for Business te syncen.
Eens proberen of Ubuntu for Desktop geschikt is als NAS

## [[2020-11-01]] 
  Ik heb een desktop pc van een paar jaar oud dat ik als home server wil laten fungeren.
  Een paar jaar geleden ben ik geleden het slachtoffer geworden van WannaCry ransomeware.
  Gelukkig bewaar ik alle data op externe USB drives.
  
  Momenteel maak ik manueel een backup van deze schijven, maar ik ben het gehannes met de schijven een beetje beu.
  
  Wat zoek ik?
  \- Een Linux distro. WannaCry maakte gebruik van een zeroday in Windows. De kans dat een virus dat beide OSsen aanvalt, lijkt mij klein.
  \- Een filesysteem met snapshot mogelijkheden (ZFS of Btrfs)
  \- Eenvoudig. Ik heb een zeer beperkte Linux kennis en het servertje staat in de kelder. Dus een beheer via een webbrowser is een must. Of is beheer via 'RDP' of iets dergelijks mogelijk?
  
  Ik heb ongeveer 4TB aan data. Ik heb 2 x 4TB schijven en 2 x 2TB schijven. Ik wil 4TB schijf gebruiken om te sharen. De andere schijven wil ik in een stripe plaatsen als backup van de andere.
  
  Dit heb ik al geprobeerd:
  De NAS distros (TrueNas, OpenMediaVault, Xigmanas).
  
  RockStor werkt niet met VMWare.
  Dit werkt niet
  disk.EnableUUID=“TRUE”
  
  *From \<<https://forum.rockstor.com/t/vmware-giving-error-not-a-valid-btrfs-filesystem-dev-disk-by-id-sda3/2543/2>\>*

# [[2020-12-11]] 
om onedrive-sync met TrueNas aan het werk te krijgen
[Tutorial: Get Onedrive Access Token For Freenas \| Freenas Cloud Credentials Tutorial : freenas (reddit.com)](https://www.reddit.com/r/freenas/comments/dzm02q/tutorial_get_onedrive_access_token_for_freenas/)
