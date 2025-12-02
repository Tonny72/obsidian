---
date created: 2025-05-22
modified: 2025-08-30
---
Tags: Visio, group policy
 
# Registry

Computer\HKEY_CURRENT_USER\Software\Policies\Microsoft\office\16.0\visio\security\fileblock
 
- Visio2003files op 0 zetten
 
# Converteer .vsd naar .vsdx
 
```
$directoryToUpdate='.'  
$visio= New-Object -com Visio.Application  
foreach($vsdFile in (get-childitem "$directoryToUpdate\*.vsd")){  
   write-host "Working on $vsdfile"  
   $doc=$visio.Documents.Open($vsdFile.FullName)  
   $vsdxFileName=[io.path]::ChangeExtension($vsdFile,'.vsdx')  
   $doc.SaveAs($VSDXFileName)  
   $doc.close();  
}
```