reg delete /f HKLM\Software\Policies\Microsoft\Windows\WindowsUpdate\WUServer
reg delete /f HKLM\Software\Policies\Microsoft\Windows\WindowsUpdate\WUStatusServer
reg add HKLM\Software\Policies\Microsoft\Windows\WindowsUpdate /v DisableWindowsUpdateAccess /t REG_BINARY /d 0 /f
timeout /t 30
