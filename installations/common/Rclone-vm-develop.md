---
date created: 2021-02-05T00:00:00+01:00
date modified: 2025-12-04T07:54:09+01:00
---
# Rclone

RCLONE config

Kies 26 Microsoft Onedrive

Keuze3
![image1](image1-145.png)

<https://sibelco.sharepoint.com/sites/elektrischedienst>

Voorbeeld

![image2](image2-81.png)
D:\Software\rclone\rclone copy "[\\\10.32.29.60\d\$\KepServer Data](file://10.32.29.60/d$/KepServer%20Data)" "ElekAutomation:/Automation/Backups/DES/Kepware"

- # Commando's
- rclone listremotes: toont de remote "Drives"
- rclone lsd AutomationOneDrive:
  
  ZIE SCRIPT D:\OneDrive - Sibelco\Apps\rclone\Sync.bat
  
  rclone copy "[\\\10.32.29.26\d\$\backup](file://10.32.29.26/d$/backup)" "automation:Automatisering/Backups/Des/800xA" --progress --max-age 31d
  
  **TOKEN EXPIRED**
  rclone config reconnect AutomationOneDrive:
  
  **
  title:: Sibelco/installations/Common/Rclone.md
-