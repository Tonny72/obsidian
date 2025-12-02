---
date created: 2014-11-03
modified: 2025-07-21
---
# Updates Windows 8.1


[clean sibelco update settings.bat](clean_sibelco_update_settings.bat)

Run als administrator
Overrule Sibelco

WSUS

<http://wp.shaibn.com/automatica>
lly-override-windows-update-gp-restriction

[**Automatically override Windows Update GP Restriction**](http://wp.shaibn.com/automatically-override-windows-update-gp-restriction)
2012-July-1, 10:32

**Related documents:**
1.  [How to override Windows Update restriction when joined to Active Directory](http://wp.shaibn.com/how-to-override-windows-update-restriction-when-joined-to-active-directory)
After showing you [how to override the GP restriction to enable Windows Update](http://wp.shaibn.com/how-to-override-windows-update-restriction-when-joined-to-active-directory), I’m now going to show you how to get that change done automatically.
I’ve created two files, wupdate.cmd and wupdate.reg. The first one will use the latter to update the registry without user intervention.
**wupdate.cmd**
[?](http://wp.shaibn.com/automatically-override-windows-update-gp-restriction)
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p>
<p>7</p>
<p>8</p>
<p>9</p></th>
<th><p>@echo off</p>
<p></p>
<p>call regedit.exe /s x:\bin\wupdate.reg</p>
<p></p>
<p>net stop wuauserv</p>
<p>net start wuauserv</p>
<p></p>
<p>%windir%\system32\wuauclt.exe /detectnow</p>
<p>%windir%\system32\wuapp.exe</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
**wupdate.reg**
[?](http://wp.shaibn.com/automatically-override-windows-update-gp-restriction)
<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th><p>1</p>
<p>2</p>
<p>3</p>
<p>4</p>
<p>5</p>
<p>6</p></th>
<th><p>Windows Registry Editor Version 5.00</p>
<p></p>
<p>[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate]</p>
<p>"WUServer"=-</p>
<p>"WUStatusServer"=-</p>
<p>"DisableWindowsUpdateAccess"=dword:00000000</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Tags: [automatic](http://wp.shaibn.com/tag/automatic), [automatically](http://wp.shaibn.com/tag/automatically), [batch](http://wp.shaibn.com/tag/batch), [cmd](http://wp.shaibn.com/tag/cmd), [command line](http://wp.shaibn.com/tag/command-line), [registry](http://wp.shaibn.com/tag/registry), [update](http://wp.shaibn.com/tag/update), [updates](http://wp.shaibn.com/tag/updates), [windows update](http://wp.shaibn.com/tag/windows-update)
Category: [Batch/CMD/DOS](http://wp.shaibn.com/category/software/batchcmddos), [Fixes and workarounds](http://wp.shaibn.com/category/fixes-and-workarounds), [Operation Systems](http://wp.shaibn.com/category/operation-systems), [Registry](http://wp.shaibn.com/category/software/registry-software), [Tools and utilities](http://wp.shaibn.com/category/tools-and-utilities), [Windows 7](http://wp.shaibn.com/category/operation-systems/windows-7-operation-systems) \|[Comment](http://wp.shaibn.com/automatically-override-windows-update-gp-restriction#respond) ([RSS](http://wp.shaibn.com/automatically-override-windows-update-gp-restriction/feed)) \|[Trackback](http://wp.shaibn.com/automatically-override-windows-update-gp-restriction/trackback)
**3 Comments**
1.  [Shai's technical blog » Blog Archive » How to override Windows Update restriction when joined to Active Directory](http://wp.shaibn.com/how-to-override-windows-update-restriction-when-joined-to-active-directory) says:  
    [2012-July-1 at 10:33](http://wp.shaibn.com/automatically-override-windows-update-gp-restriction#comment-324)  
    \[...\] « How to backup a remote server via SSH and pipe the archive to the local machine Automatically override Windows Update GP Restriction \[...\]  
    [Reply to this comment](http://wp.shaibn.com/automatically-override-windows-update-gp-restriction?replytocom=324#respond)
![image1](image1-46.png)

Bruce H says:  
[2014-May-9 at 00:12](http://wp.shaibn.com/automatically-override-windows-update-gp-restriction#comment-5830)  
you can sub this in for the regedit.exe command, to avoid having the extra reg file. On Windows 8, you need to run at an Administrator-elevated command prompt.  
reg delete /f HKLM\Software\Policies\Microsoft\Windows\WindowsUpdate\WUServer  
reg delete /f HKLM\Software\Policies\Microsoft\Windows\WindowsUpdate\WUStatusServer  
reg add HKLM\Software\Policies\Microsoft\Windows\WindowsUpdate /v DisableWindowsUpdateAccess /t REG_BINARY /d 0 /f

*From \<<http://wp.shaibn.com/automatically-override-windows-update-gp-restriction>\>*
