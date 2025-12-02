---
modified:  2025-09-15 11:00
date created: 2018-11-21T00:00:00+02:00
date modified: 2025-10-13T07:44:19+02:00
---
# CredSSP encryption oracle remediation

- Patch te installeren
  <https://support.microsoft.com/en-au/help/4295591/credssp-encryption-oracle-remediation-error-when-to-rdp-to-azure-vm>
	- Deze is al gedownload bij Software - Microsoft
- Error message bij RDP connection
  
  ![image1](image1-7.jpg){:height 512, :width 486}
  
  Oplossing
  Open group policy edit (gpedit.msc)
  Zet de Encryption Oracle Remediation op Enabled : Protection Level Vulnerable
  
  ![image2](image2-17.png)