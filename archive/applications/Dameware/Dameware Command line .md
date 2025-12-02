---
date created:
  - - 2014-03-14
modified: 2025-07-21
---
# Dameware Command line 

**Versions 4.6 and Newer**

**dwrcc.exe \[-?\|-?:\] \[-c:\] \[-h:\] \[-m:machinename\] \[-u:username\] \[-p:password \| -p:"pass word"\] \[-d:domain\] \[-o:TCPport\] \[-s:sharedsecret\] \[-r:\] \[-a:0\|1\|2\] \[-v:\] \[-md:\] \[-i:*n*\] \[-x:\]**
<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>-?:</strong></th>
<th>Displays this Help menu.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>Example dwrcc.exe <strong>-?:</strong></td>
</tr>
<tr class="even">
<td><strong>-c:</strong></td>
<td>Connect automatically.</td>
</tr>
<tr class="odd">
<td></td>
<td>Example: dwrcc.exe <strong>-c:</strong> -m:123.123.123.123</td>
</tr>
<tr class="even">
<td><strong>-h:</strong></td>
<td>Will bypass the MRC Host Entry settings using the default connection settings unless specified otherwise by additional command line options (used with -c).</td>
</tr>
<tr class="odd">
<td></td>
<td>Example: dwrcc.exe -c: <strong>-h:</strong> -m:123.123.123.123</td>
</tr>
<tr class="even">
<td><strong>-m:</strong></td>
<td>Sets the machine or host name or IP address.</td>
</tr>
<tr class="odd">
<td></td>
<td>Example: dwrcc.exe -c: <strong>-m:123.123.123.123</strong></td>
</tr>
<tr class="even">
<td><strong>-u:</strong></td>
<td>Sets the User ID.</td>
</tr>
<tr class="odd">
<td></td>
<td>Example dwrcc.exe -c: -m:123.123.123.123 <strong>-u:myUsername</strong></td>
</tr>
<tr class="even">
<td><strong>-p:</strong></td>
<td>The password field now has the ability to be enclosed in double quotes.</td>
</tr>
<tr class="odd">
<td></td>
<td><p>Example dwrcc.exe -c: -m:123.123.123.123 -u:myUsername <strong>-p:"my Password"</strong></p>
<p></p>
<p><strong>*Note:</strong> When Smart Card Logon authentication method selected (i.e. -a:3), <strong>-p:</strong> parameter is used to supply PIN, instead of Password.</p>
<p></p>
<p>Example dwrcc.exe -c: -m:123.123.123.123 <strong>-a:3 -p:PIN</strong> (v5.5 and above)</p></td>
</tr>
<tr class="even">
<td><strong>-d:</strong></td>
<td>Specifies the Domain name.</td>
</tr>
<tr class="odd">
<td></td>
<td>Example dwrcc.exe -c: -m:123.123.123.123 -u:myUsername -p:myPassword <strong>-d:myDomainName</strong></td>
</tr>
<tr class="even">
<td><strong>-o:</strong></td>
<td>Specifies the TCP Port Number.</td>
</tr>
<tr class="odd">
<td></td>
<td>Example dwrcc.exe -c: -m:123.123.123.123 <strong>-o:6129</strong></td>
</tr>
<tr class="even">
<td><strong>-s:</strong></td>
<td>Specifies the Pre-Shared Secret Password (version 4.4 and above).</td>
</tr>
<tr class="odd">
<td></td>
<td>Example dwrcc.exe -c: -h: -m:123.123.123.123 -u:myUsername -p:myPassword <strong>-s:mySharedSecret</strong></td>
</tr>
<tr class="even">
<td><strong>-r:</strong></td>
<td>Specifies the use of the Remote Desktop Protocol (RDP) (version 4.4 and above).</td>
</tr>
<tr class="odd">
<td></td>
<td>Example dwrcc.exe -m:myMachineName <strong>-r:</strong></td>
</tr>
<tr class="even">
<td><strong>-a:</strong></td>
<td>Specifies the Authentication Method. (0=Proprietary Challenge/Response, 1=NT Challenge/Response, 2=Encrypted Windows Logon, 3=Smart Card Logon).</td>
</tr>
<tr class="odd">
<td></td>
<td><p>Example dwrcc.exe -c: -m:123.123.123.123 -u:myUsername -p:myPassword -d:myDomainName <strong>-a:2</strong></p>
<p></p>
<p><strong>*Note:</strong> When Smart Card Logon authentication method selected (i.e. -a:3), <strong>-p:</strong> parameter is used to supply PIN.</p>
<p></p>
<p>Example dwrcc.exe -c: -m:123.123.123.123 <strong>-a:3 -p:PIN</strong> (v5.5 and above)</p></td>
</tr>
<tr class="even">
<td><strong>-v:</strong></td>
<td>Open this DMRC session in View Only Mode (version 5.0 and above).</td>
</tr>
<tr class="odd">
<td></td>
<td>Example dwrcc.exe <strong>-c:</strong> -m:123.123.123.123 <strong>-v:</strong></td>
</tr>
<tr class="even">
<td><strong>-md:</strong></td>
<td>Specifies the use of the DameWare Mirror Driver (if installed) (version 5.0 and above).</td>
</tr>
<tr class="odd">
<td></td>
<td>Example dwrcc.exe <strong>-c:</strong> -m:123.123.123.123 <strong>-md:</strong></td>
</tr>
<tr class="even">
<td><strong>-i:</strong></td>
<td>Instance number override (version 5.0 and above).</td>
</tr>
<tr class="odd">
<td></td>
<td>Example dwrcc.exe <strong>-c:</strong> -m:123.123.123.123 <strong>-i:<em>n</em></strong> (where 0&lt;n&lt;40)</td>
</tr>
<tr class="even">
<td><strong>-x:</strong></td>
<td>Automatically close the DMRC application after disconnection from the remote machine (via command line). (version 5.0.1.5 and above).</td>
</tr>
<tr class="odd">
<td></td>
<td>Example dwrcc.exe <strong>-c:</strong> -m:123.123.123.123 <strong>-x:</strong></td>
</tr>
</tbody>
</table>
