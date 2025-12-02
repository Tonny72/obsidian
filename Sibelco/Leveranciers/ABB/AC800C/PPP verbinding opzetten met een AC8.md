---
title: PPP verbinding opzetten met een AC800C.
updated: [[2013-06-12]]T16:54:22.0000000+02:00
created: [[2012-08-01]]T09:45:42.0000000+02:00
---

PPP verbinding opzetten met een AC800C.
woensdag 1 augustus 2012
9:45

- # PPP verbinding opzetten met een AC800C.
  Omschrijving.
  Het is mogelijk om met Control Builder een seriële verbinding op te zetten met een AC800C.
  Aansluiting.
  Gebruik een Ipconfig kabel en sluit deze aan op COM0 van de AC800C (=linkse poort).
  Opzetten van een Active (guest) PPP verbinding.
  · Klik Start-Settings – Network and Dial-up Connections – Make new Connection en klik Next.
  · Klik “Connect directly to another computer” en klik Next.
  · Klik **Guest** en klik Next.
  · Selecteer de COM poort die wordt gebruikt voor de seriële verbinding. En klik Next.
  · Klik “For all users” en klik Next.
  · Typ een naam in voor de connectie, en klik Finish.
  · Maak geen connectie. Connectie worden gemaakt door de MMS server. Vul geen username of password in. Klik Cancel.
  Configureer een active (guest) PPP verbinding.
  · Klik Start-Settings – Network and Dial-up Connections – Uw PPP connectie naam.
  · Rechts-klik en kies Properties.
  · In de General tab, klik Configure.
  · Zet Maximum speed op 9600 en Uncheck alle opties, en klik ok.
  · In het networking tab: selecteer TCP/IP en klik Properties
  Obtain an IP address automatically.
  Obtain DNS server address automatically.
  · Klik Advanced
  · Uncheck Use default gateway on remote network.
  · Check Use IP header compression. Klik op OK 2x.
  Configureer de MMS server voor een PPP verbinding.
  De PPP verbindingen moeten gebruikt worden via de MMS server. De MMS server heeft dialoog vensters voor PPP. Eén voor configuratie en één voor supervisie van PPP verbindingen.
  Voeg een nieuwe PPP verbinding toe aan de MMS server.
  · Klik Setup – PPP setup in de MMS server operator panel.
  · Klik Add en selecteer de Direct Connection en klik Select.
  · Zet de “Link supervision” op True. Dit wil zeggen dat de PPP link wordt gechecked door een Ping.
  · Username en Password mag leeg zijn. (Enkel nodig voor een PPP verbinding naar een ander Windows workstation).
  · Klik Save en herstart de MMS server om de instellingen toe te passen.
  STEEK DE KABEL IN DE LINKSE POORT van de AC800C
- # [[2013-06-12]] 16:53 
  Instellingen stonden niet op DHCP
  
  Mogelijke Ipadressen AfzakInstallatie
  172.16.255.254
  192.168.255.254
  192.168.255.253
  
  PLC
  
  ![image1](image1-557.png)