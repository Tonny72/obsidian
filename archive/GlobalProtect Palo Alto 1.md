---
date created: 2012-10-29
modified: 2025-07-21
---
# GlobalProtect Palo Alto 1

created: [[2014-10-29]]T14:50:14.0000000+01:00
  
  Sibelco VPN client
  
  [\\\bedesnas1\software\SMSINST\Standardsoftware\GlobalProtect_PA](file://bedesnas1/software/SMSINST/Standardsoftware/GlobalProtect_PA)
  
  PROCESS DESCRIPTION
- **Global Protect Client**
  
  <table>
  <colgroup>
  <col style="width: 11%" />
  <col style="width: 13%" />
  <col style="width: 24%" />
  <col style="width: 19%" />
  <col style="width: 15%" />
  <col style="width: 13%" />
  </colgroup>
  <thead>
  <tr class="header">
  <th>1</th>
  <th>[[2012-10-16]]</th>
  <th>Global Protect Client</th>
  <th>Gert Carpentier</th>
  <th></th>
  <th></th>
  </tr>
  </thead>
  <tbody>
  <tr class="odd">
  <td>2</td>
  <td>[[2013-05-30]]</td>
  <td>Global Protect Client v2</td>
  <td><p>Tom De Schrijver</p>
  <p>Gert Carpentier</p></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="even">
  <td><strong>Rev</strong></td>
  <td><strong>Date</strong></td>
  <td><strong>Description</strong></td>
  <td><strong>Author</strong></td>
  <td><strong>Maintenance</strong></td>
  <td><strong>Engineering</strong></td>
  </tr>
  </tbody>
  </table>
  
  Table
  
  1 User prerequisites to use the Palo Alto GlobalProtect Client 3
  
  2 Download the GlobalProtect Client 4
  
  3 How to connect to the Sibelco SMART-WAN network 8
  
  ****
  1.  **User prerequisites to use the Palo Alto GlobalProtect client:**
  ****
  
  In order for the Single Sign on to work, the user and computer should be a member of the domain Sibelco-Europe.amorg.group or SibelcoAsia.amorg.group.
  
  (An exception is for the Foreign Users OU in the amorg.group domain)
  
  Your username has to be in the same form as your Lawson userID (SCHTOM00).
  
  Your token needs to be linked to your user (information you can request from kadia.van.de.plas@sibelco.com)
  
  This is because we have installed a new ACE server. Therefore it could be that your token needs to be linked to your user. You can check this via the new self-service portal <https://new_securid.sibelco.com/console-selfservice>
  
  A group policy is in place in the sibelco-europe.amorg.group domain that will install a registry setting to preconfigure the client
  
  ![image1](image1-45.png)
  
  Make sure this registry key already exists before you install the client.
  
  You can run this file to import the correct setting:
  
  ![image2](image2-21.png)
  
  PA_client_vpn_settting.reg
  
  1.  **Download the Global Protect Client**
  Type in the address in your internet explorer
  
  <https://client_vpn.sibelco.com>
  
  Logon with your AD credentials (without specifying the domain)
  
  ![image3](image3-9.png)
  
  According to your operating system, click on the download link on the page to download the
  
  GlobalProtect agent.
  
  *!Note -If you do not know what is your operation system, please contact your local helpdesk*
  
  ![image4](image4-8.png)
  
  After downloading, double click to install it
  
  ![image5](image5-5.png)
  
  Follow the prompts, press next
  
  ![image6](image6-4.png)
  
  Choose where you want it installed, and press next
  
  ![image7](image7-2.png)
  
  Confirm by pressing next
  
  ![image8](image8-1.png)
  
  .
  
  ![image9](image9-1.png)
  
  You will get a UAC prompt, press Yes
  
  ![image10](image10-1.png)
  
  To complete close and reboot your device. If you do not reboot, the SSO will not work
  
  ![image11](image11-1.png)
  
  1.  **How to connect to the Sibelco SMART WAN network via the Palo Alto GlobalProtect client**
  ****
  
  ****
  
  Look for the GlobalProtect icon in the system tray
  
  ![image12](image12-1.png)
  
  Right-click, and select connect
  
  ![image13](image13-1.png)
  
  After a few seconds you will get this prompt:
  
  ![image14](image14-1.png)
  
  In the password field, fill in your **<u>PIN+tokencode</u>**, the username should be automatically populated.
  
  After another few seconds the message <u>Connected</u> should appear.
  
  ![image15](image15-1.png)