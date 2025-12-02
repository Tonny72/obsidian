---
date created: 2020-06-04 00:00
modified: 2025-09-15 10:59
---
# Windows updates
Pas deze [[registry]] key aan

Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU
UseWUServer = 0

Herstart Windows update service
Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate

Pas deze registry key aan:
- ``Computer\\HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU``
- ``UseWUServer = 0``
- ``Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate``
- Herstart Windows update service

## Windows 11 key
Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsUpdate
Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsUpdate\UpdatePolicy\PolicyState