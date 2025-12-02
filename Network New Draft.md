

DTS-10 Digital Technology Standards: Network 

The Digital Technology Standards documents detail controls that must be observed in the implementation or adaptation of technology solutions into the Sibelco IS environment.  

Table of Contents  

Tables & Figures 

1. Introduction 
    

2. Audience 
    

The intended audience for this standard is Project Managers, Architects and Engineers involved in the implementation of new solutions or the change to existing technology services. 

2. Scope 
    

This document covers standards and guidelines relating to Cybersecurity linked to the Technical Reference Model ​[1]​. 

This document addresses the segmentation requirements set out in ​[2]​. 

1. In Scope 
    

- Network Segmentation layout  
    

- Network Segmentation for Sibelco DataCenters, offices & sites 
    

- Definition of Trusted Zones & VRFs (Virtual Routing and Forwarding) 
    

- Mapping with PERA (Purdue Enterprise Reference Architecture) 
    

- Placement Criteria for Zones & VFRs 
    

- General Security controls required for zones & VRFs 
    

- Traffic Flow and conduit High-Level criteria 
    

- General rules for traffic flow 
    

- Traffic Flow Matrix 
    

- FW management criteria 
    

- General rule management criteria 
    

- Capabilities required 
    

- Traffic lights protocols: forbidden / limited / allowed 
    

- WiFi requirements 
    

- Corporate WiFi 
    

- Guest WiFi 
    

- Industrial WiFi 
    

- IP Management & DNS 
    

- IP Addressing 
    

- DNS 
    

- DHCP 
    

2. Out of scope 
    

- Remote Access Standard 
    

- Security Standard for Network Devices 
    

3. Content control 
    

4. Update Frequency 
    

This document will be reviewed annually and updated in line with technology strategy changes. 

2. Contact Person 
    

This document is owned by IS Strategy, Governance and Risks Team and queries regarding this document should be directed to [enterprise.architecture@sibelco.com](mailto:enterprise.architecture@sibelco.com). enterprise.architecture@sibelco.com. 

4. Document Conventions 
    

|   |   |
|---|---|
|DESCRIPTION:|A description of the Subject|
|STANDARD:|The Standard (policy, process or technology preference)|
|APPROVED ALTERNATIVE:|An Approved Alternative to the Standard|
|GUIDELINE:|Approved implementations of the standard|

2. Network segmentation layout 
    

The following diagrams describes the different trust zones as well as the main VRFs (Virtual Routing & Forwarding) for both Sibelco Data center (including Azure) & Sites/ Offices 

1. General layout for datacenterdatacentre offices & sites 
    

Figure 1 General Network Segmentation Layout 

3. Definition of Trusted ZonesEFINITION OF TRUSTED ZONES & VRFSvrfs 
    

The following table below shows the summary mapping of Trusted zones with PERA (Purdue Enterprise Architecture) model and provides placement criteria and examples 

|   |   |   |   |   |
|---|---|---|---|---|
|PURDUE|ZONE|VRF|Placement criteria|Assets examples|
|IT:5|UNTRUSTED|N/A|All Internet borne services|Internet, Users, Third Party Providers, Cloud|
|LOW TRUST|BPA|S2S interfaces &VPN gateways|IPSEC VPN, Site to Site routers|
|DMZ EXTERNAL|Any service requiring Internet facing, inbound or inbound/outbound|Web services; Proxy, Reverse Proxies, WAF, Edge On-Prem to Cloud Servers|
|VDI|Virtual desktops VLANS equivalent to Corporate Office VLAN|AVD Desktops, Citrix VDIs (EUC machines not Citrix Servers)|
|OFFICE|Corporate laptops/ workstations connecting to internal services|Corporate WiFi, Corporate LAN|
|IoT|Office network aimed for IoT devices/ applications|Printers, VideoConferencing; VoIP, Building controls, Clock-in/out devices.|
|GUEST|BYOD Devices and devices not managed by IS|Guest WiFi|
|SURVEILLANCE|Security Camaras & required equipment|Security surveillance at offices & sites|
|IT:4|MEDIUM TRUST|PROD|Production workloads|Enterprise servers and servivesservices supporting production workloads|
|NON-PROD|Non-Prod workloads|Q/A & development environments|
|OT-SERVICES|Colocation for servers connecting to OT networks|SCADA servers hosted centrally in IT, any other server to run OT world applications|
|HIGH TRUST|MONITORING|IT Monitoring tools; Backup & Recovery|Monitoring services (i.e. Nagios, SolarwindsSolarWinds); Backup & Recovery services|
|SECURITY / JUMP|Security  devicesSecurity devices management interfaces; Jump stations|Central FW management consoles; Network devices managementconsolesmanagement console; SIEM on-prem connectors; PAM connectors for DC|
|SHARED SERVICES|Shared services for DatacenterDatacentre|Active Directory, DNS, DHCP, PKI, SCCM|
|IT/OT:3.5|DMZ IT/OT|SECURITY / JUMP|Jump servers; Brokering devices|PAM connectors, Jump stations for IT/OT, SIEM connectors|
||SHARED SERVICES|Shared services for sites|Active Directory, DNS, DHCP, SCCM|
|OT:3|OT TRUST|OT SERVICES|Local servers at the sites|WeightbridgeWeighbridge servers, HCI hosted servers|
|MES|Operational services: level 3|MES, historian, industrial workstations, Shopfloor terminals|
|LABS|Laboratory  instruments|Laboratory PCs, LabotoryLaboratory devices|
|OT:2|SCADA/HMI|Supervisory services: level 2|SCADA, HMIs, Control Servers|
|OT:0-1|AUTOMATION CELLS|Process services: level 0-1|PLCs, Sensors, Pumps, Kilns, Silos|

Table 1 Zones & VRFs mapping to PERA 

The main criteria used to decide on the zone/vrf placement: 

Business Criticality Higher criticality = lower Purdue level or higher trust 

Attack Exposure Higher exposure = higher Purdue level or lower trust 

Data Sensitivity Confidential or restricted data must not reside in Low Trust 

Connectivity Cross-zone connections must be minimal, controlled, and documented 

Patch ability Unpatchable systems shall be placed on specific isolated VRFs 

Operational Impact OT systems shall maintain determinism and availability under segmentation 

|   |   |
|---|---|
|Business Criticality|Higher criticality = lower Purdue level or higher trust|
|Attack Exposure|Higher exposure = higher Purdue level or lower trust|

|   |   |
|---|---|
|Data Sensitivity|Confidential or restricted data must not reside in Low Trust|

|   |   |
|---|---|
|Connectivity|Cross-zone connections must be minimal, controlled, and documented|

|   |   |
|---|---|
|Patchability|Unpatchable systems shall be placed on specific isolated VRFs|

|   |   |
|---|---|
|Operational Impact|OT systems shall maintain determinism and availability under segmentation|

1. Untrusted zone 
    

This zone represents all traffic coming from Internet such as: 

- Public (Internet), 
    

- Remote (IPsec/SSL VPN Users) 
    

- Partner (Site-to-Site) 
    

- Outside interface of Sibelco external firewalls 
    

2. Low trust Trust zone 
    

The Low trust zone contains elements that hold a higher level of exposure to Threats, hence less trusted.  

In Sibelco Data Centers (including Cloud Hyper scalars) we have the following VRFs: 

- DMZ External: Security zone for servers that required access from / to Internet either Inbound or outbound. Inside interfaces of the external firewalls. 
    

- Business Partner Access: Security zone for VPN landing networks and remote access connectors placement. 
    

- VDI: Security zone for virtual desktop placement to be used by external Third Parties. 
    

In Sibelco Offices / Sites the following VRFs: 

- Office: For Sibelco Managed laptops and workstations. Sibelco Unmanaged devices cannot be connected to this network. 
    

- IoT: For devices that do not required connection to Sibelco internal applications, including Meeting room videoconferencing devices, VoIP phones, clock-in / out devices, building controllers / heating, vending machines, etc. 
    

- Guest: For non-Sibelco managed devices, such as vendor laptops or employees BYOD. 
    

3. Medium trust Trust zone 
    

This zone is aimed at hosting business workloads within Sibelco Data Centres.  

The following VRFs belong to this zone: 

- PROD: Business application and services and environments hosting real data: i.e. Quality, pre-prod, staging. 
    

- NON-PROD:  Business development environments, sandbox and test environments with no real data. 
    

- OT Services: Services that connect directly to OT Trusted zones shall be placed here. This zone shall be the only one with routing enabled towards OT trusted and below zones. 
    

4. High trust Trust zone 
    

This zone is aimed at hosting services that will have broad connectivity to any other zones and hence shall be highly protected. 

- SECURITY / JUMP VRF: Security consoles for FWs, backup, SIEM, central logging, vulnerability management, etc. All secure Jump hosts (like in Privileged Access Management solution) for remote access to systems are placed here. 
    

- TOOLS MONITORING: IT monitoring tools that typically require connection to all assets across all zones, like Nagios, SolarWinds, NDR, etc. 
    

- Shared Services: Required core IT foundational services to be shared among all other applications, like Active Directory, DNS, File Servers and Data storage cabins, etc. 
    

5. DMZ IT/OT 
    

This zone is aimed at hosting brokering services that interconnect IT with OT and vice-versa. 

- SECURITY / JUMP VRF: Secure Jump hosts (Privileged Access Management) that allow remote access from LOW TRUST to OT TRUST  
    

- Shared Services (sites): Required foundational services to be shared among all other applications, like Active Directory, DNS, File Servers and Data storage cabins, etc. 
    

6. OT Ttrust 
    

This zone is dedicated to operational technology assets at plants. 

- OT SERVICES: Equivalent to the OT SERVICES VRF hosted in IT but physically at the site (HCI). 
    

- MES: Specially aimed to host MES machines and setups, including historians & terminals that connect to SCADAS. 
    

- SCADA/HMI: Placement for SCADAS /HMI control servers. 
    

- AUTOMATION CELLS: PLCs, Sensors, Pumps, industrial machinery (kilns, silos, etc.) 
    

2. General segmentation rules 
    

|   |   |   |
|---|---|---|
|ID|CONTROL|RATIONALE|
|NT-G-01|All assets SHALL be placed on a Network Zone/VRF, and this shall be properly registered in CMDB|Network placement shall be decided at build phase by architects and maintained under run.|
|NT-G-02|Unsupported and/or non-compliant assets are NOT allowed to connect to any network zone.|Assets that do not follow corporate policies (i.e. cannot be patched or are not hardened) pose a risk to other assets that do follow them and hence these cannot be placed in the same network zone.|
|NT-G-03|Direct access from IT to OT zones SHALL NOT be allowed, unless a jump solution is used from DMZ IT/OT|To prevent malicious traffic from affecting operational zones, direct access will never be allowed from IT to OT. A jump solution (typically Privileged Access Management) shall be in place in DMZ IT/OT to allow that connectivity.|
|NT-G-04|All outbound Internet Access SHALL be protected with centralized proxy services|To have proper visibility and to provide network-borne security controls, all Internet breakouts shall be protected using central proxy services integrated with SIEM solution for security monitoring.|
|NT-G-05|General outbound Internet Access will be limited to assets placed in LOW TRUST zone only; Rest of zones will have limited “cloud agent” access required only to very specific URIs, IPS or DNS names. ANY outbound access will not be allowed|Assets placed in MEDIUM trust and below shall never have outbound Internet connection to prevent side channel and Command & Control connections. Should this be required as cloud services are required to run, this will be only limited to required URLs/DNS names or Ips for the service to work|
|NT-G-06|All inbound Internet connections towards Sibelco hosted applications SHALL be protected with Web Application Firewall (WAF) & Anti-DDoS capabilities|Any Internet facing Sibelco application or API that shall be exposed to ANY Internet access MUST have a WAF upfront as well as capabilities to prevent Denial of Service attacks.|
|NT-G-07|Any non-compliant or unsupported assets that are not remediated in two months’ time, shall be moved to isolated VRFs.|Assets that do not observe required security controls and/or cannot be patched shall be moved to isolated VRFs. <br><br>This is needed to ensure that these cannot cause security issues to other compliant assets place within the same network segment.|
|NT-G-08|No direct remote access SHALL be allowed from LOW TRUST towards any other zone.|Direct interactive remote access protocols (RDP, SSH, VNC, etc.) initiated from LOW TRUST are NOT allowed to any other Zone except for SECURITY / JUMP VRF in both HIGH TRUST and DMZ IT/OT|
|NT-G-09|Traffic cannot be allowed from a less trusted zone that traverses two higher trust zones at the same time. <br><br>Exceptions: VRF Shared Services for required datacenter core connections; VRF SECURITY/JUMP for required ports to jump.|i.e. UNTRUSTED to MEDIUM TRUST; LOW TRUST to HIGH TRUST, LOW TRUST to OT TRUST|
|NT-G-10|All zones SHALL exist in any deployment, however, VRFs can be simplified depending on the size and requirements of the site but always following the principles.|In small sites both office VRFs and OT VRFs can be simplified if needed but always preserving the minimum segmentation layout based on TRUST boundaries. <br><br>i.e. there might be sites where all OT levels (purdue 0-3) are merged under one VRF but all the other zones: DMZ IT/OT & LOW TRUST shall be preserved|

Table 2  General segmentation rules 

3. Required security controls per zone/vrf 
    

Below table shows the required minimum-security controls per each of the zones divided in Network, Identity and Data. 

In addition, all assets placed on every zone must also observe the controls set out within existent Standards for Server, Network devices and OT devices as stated under NT-G-02 to be deemed as compliant. 

|   |   |   |   |   |
|---|---|---|---|---|
|ZONE|VRF|Network Controls|Identity Controls|Data|
|UNTRUSTED|N/A|N/A|N/A|N/A|
|LOW TRUST|BPA|Edge Firewall, IPS filtering|MFA, Zero Trust Network Access|TLS encryption|
|DMZ EXTERNAL|Web Application Firewall (WAF), Anti-DdoS; , no direct remote access (RDP, SSH) allowed|Federated Auth|TLS encryption, SSL Inspection (outbound)|
|VDI|Proxy, CASB, NAC|MFA, Zero Trust Network Access|DLP|
|OFFICE|Proxy, CASB, NAC, Enterprise Wifi, endpoint FW, EDR, intra-VLAN isolation, no direct remote access (RDP, SSH) allowed|Machine certificate, MFA, Zero Trust Network Access|DLP, MAM, CASB, full disk encryption|
|IoT|Proxy, NAC|MAC auth, certificate auth|TLS encryption|
|GUEST|Intra-VLAN traffic isolation|MFA, Zero Trust Network Access|MAM|
|SURVEILLANCE|Isolation (Micro-segmentation)|Standalone not integrated with Sibelco IDP|TLS encryption|
|MEDIUM TRUST|PROD|Proxy,EDR, XDR,  internal FW, IPS;  No direct Remote Access Connection (RDP, SSH, VNC)|MFA,  SSO, PAM, Zero Trust Network Access|Backup offsite; TLS encryption|
|NON-PROD|Proxy,EDR, XDR,  internal FW, IPS;  No direct Remote Access Connection (RDP, SSH, VNC)|MFA, SSO, PAM, Zero Trust Network Access|Backup; TLS encryption|
|OT-SERVICES|Proxy,EDR, XDR,  internal FW, IPS, micro-segmentation ; No direct Remote Access Connection (RDP, SSH, VNC)|MFA, SSO, PAM, Zero Trust Network Access|Backup; TLS encryption|
|HIGH TRUST|MONITORING|Proxy, EDR, XDR, Internal FW, IPS ; No direct Remote Access Connection (RDP, SSH, VNC)|Monitoring services (i.e. Nagios, Solarwinds); Backup & Recovery services|Backup; TLS encryption|
|SECURITY / JUMP|Proxy,EDR, XDR,  internal FW, IPS, strict filtering|Phishing resistant MFA, PAM, Zero Trust Network Access|Backup; TLS encryption|
|SHARED SERVICES|Proxy,EDR, XDR,  internal FW, IPS, strict filtering; No direct Remote Access Connection (RDP, SSH, VNC)|Phishing resistant MFA, PAM, Zero Trust Network Access|Backup offsite inmutable; TLS encryption|
|DMZ IT/OT|SECURITY / JUMP|Proxy,EDR, XDR,  internal FW, IPS, strict filtering; No direct Remote Access Connection (RDP, SSH, VNC)|Phishing resistant MFA, PAM, Zero Trust Network Access|Backup; TLS encryption|
|SHARED SERVICES|Proxy,EDR, XDR,  internal FW, IPS, strict filtering; No direct Remote Access Connection (RDP, SSH, VNC)|Phishing resistant MFA, PAM, Zero Trust Network Access|Backup offsite inmutable; TLS encryption|
|OT TRUST|OT SERVICES|Proxy,EDR, XDR,  internal FW, IPS, micro-segmentation; ; No direct Remote Access Connection (RDP, SSH, VNC)|MFA, SSO, PAM, Zero Trust Network Access|Backup|
|MES|Proxy,EDR, XDR,  internal FW, IPS ; No direct Remote Access Connection (RDP, SSH, VNC)|MFA, SSO, PAM, Zero Trust Network Access|Backup|
|LABS|Isolation (Micro-segmentation)|Local/ Standalone|N/A|
|SCADA/HMI|Proxy, EDR, XDR,  internal FW, IPS ; No direct Remote Access Connection (RDP, SSH, VNC)|MFA, SSO, PAM, Zero Trust Network Access|Backup|
|AUTOMATION CELLS|Isolation (Micro-segmentation)|Local/ Standalone|Backup|

Table 3 Security controls per zone/VRF 

4. Traffic flows 
    

General rules applicable to traffic flows: 

|   |   |   |
|---|---|---|
|ID|![A picture containing drawing, shirt<br>Description automatically generated](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD8AAABRCAYAAABloX71AAAQAElEQVR4AcRcCXQUxdb+qntmMplskEDYEggkiAiKPj2uoLjhggvqU1xwV0DcnttRcff43N5TnyDu64/bUQR/XJ5P9AgqB1Fk+9l3ZBMkEJYkZGa6+79fJT3pycxkwWRep6ur+tatW/erunWrutM1huM4tuOkJ0QiEbu8vNyeN2+ePWHCBHvUqFE6XrBggaYz33HSo4vjOLYBQAFtFxzHURUVFWr27Nlq4sSJavz48erVV19VAlgxj/HLL7+sxo0bp959913Nt2vXrjbVCajFS/BozUMAwbZt7Nu3D0uXLsXrr7+OBx54AG+++SZ++uknbN68GZZlxVXJ+y1btmDWrFma7/7778drr72my9fU1Gh5cQVa6aZVwFP5nTt3YtmyZfjmm2/wxhtv4NFHH8Xzzz+POXPmIBwOt0hd8rMcy1MOG27atGlaPuth47ZIYArm/QZPwBs3btRgxZTx9NNPQ8wXkydP1oBlbINWkKJe5OXlYfDgwTpOxcPy27dvxy+//KLlUj7rkSGCb7/9FqyfeqQq3xS9UfCsnL0gY1Cb65IlSzRYmuTYsWPx2GOP4eOPP9bmuWPHDlRXV6c0Ub/fj8LCQhx66KG45ppr8Mgjj+CSSy7R8dVXX43DDjtM55MvmdLsbcpnPRxOH330ka7/3nvv1UOElkH9OKyoL/Wm/slkubQ48CzAHlu+fDmmT5+O999/H6+88grEM4OtzZhgaZIVFRWN9iwrMAwDnTp1wkknnYTrr78eN910k46POuooZGZmkkXHRx99NK677rpYPvlZjuU1U4oLwREo9Zk0aVKcnrQS6k8cHI60IOLzijJ++OEHfPjhh3jqqadw991347777sOzzz6LDz74AN9//z0WLVqE9evXg2MtGo16yyakTdNEMBjUgE8++WSwVzhmhw8fjgEDBmi6z+dLKEcC6QRMPvI//PDDujwbghaTkZEByldKkT1poH7Uk/ouXrxY608czz33nMZFfMRJvMRtyPSC7777DmvWrEFVVVWTvemtlcq0b98eBx54IE455RRcdtlluOOOO7R3v+iii9C9e3cve1zagS1/jtAYJGpwstdZng3x4IMP4s4778SIESPARmV9rJf1NyjW6C3xESfxEnec2Tdasi4zFAqhd+/eOOus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)CONTROL|![A close up of a sign<br>Description automatically generated](data:image/png;base64,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)RATIONALE|
|NT-FL-01|Direct connections between OT zones and IT LOW TRUST zones (bi-directional) is NOT allowed.|No direct access can be granted from OT to IT zones or from IT to OT zones that is not brokered via DMZ IT/OT. <br><br>This is to reduce the risk of IT compromise impacting operations and that an OT compromise of a plant can be spread across Global IT and other plants|
|NT-FL-02|Connection to OT zones and IT MEDIUM TRUST can only be allowed from assets placed under OT Services VRF. <br><br>In addition, only required connectivity from IT Shared Services zone will also be allowed|Any workload aimed at providing service for OT areas SHALL be hosted in dedicated VRFs either on IT data center (MEDIUM TRUST/ OT Services) or in HCI in the plant (OT Services)|
|NT-FL-03|Remote access protocols (SSH, RDP, VNC) towards OT zones can only be allowed via DMZ IT/OT Jump solutions (i.e. PAM)|Direct connection is not allowed as this is exposing attack surface of OT assets from LOW trust zones.|
|NT-FL-04|All VRFs SHALL be protected with a firewalling device with required capabilities as required under section 5 of this document.|To ensure proper segmentation a firewalling device must be in place to maintain segmentation appropriately. <br><br>For very small offices/sites a router with ACLs can be leveraged as compensatory control, but such architecture shall be first approved by Architecture Review Board. (ARB)|
|NT-FL-05|Micro-segmentation where technically viable shall be applied to highly exposed or sensitive Zones / VRFs: DMZ External & OT Services.|Micro-segmentation will prevent any East-West lateral movement between workloads belonging to different applications. <br><br>In case a hosted application is compromised, it cannot spread to other nearby applications hosted within same Zone/VRF thus containing the threat.|
|NT-FL-06|Direct access from Business Partner VRF (S2S / Third Party VPN) shall be limited to required specific services and jump VRFs only|Direct access to sensitive zones like Shared Services (AD, DNS), OT Zones, shall be avoided as this could open the door to threats coming from the Third-Party vendor’s network.  <br><br>Also, direct access with insecure protocols as listed under section 5 Shall be restricted|
|NT-FL-07|Any inter-zone flow requires: <br><br>- Business documented justification <br>    <br><br>- Security Architecture Review (ARB approval) <br>    <br><br>- Specific Firewall rule with strict access control|The risk of inter-zone connectivity Shall be first assessed before granting access and required documentation shall be provided. <br><br>In case temporary access is agreed firewall rules shall be created with an expiration date.|
|NT-FL-08|Any Intra-Zone flow requires: <br><br>- Business justification <br>    <br><br>- Security operations review <br>    <br><br>- Strict FW access control|All FW rules, even within the same zone, shall be reviewed and assessed for risk before this is approved and implemented. Only required ports for the business process to run will be opened.|

Table 4 Traffic flow general rules