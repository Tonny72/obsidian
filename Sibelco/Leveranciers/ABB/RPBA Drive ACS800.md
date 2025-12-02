---
title: RPBA Drive ACS800
updated: [[2021-08-23]]T08:55:03.0000000+02:00
created: [[2010-12-10]]T11:29:15.0000000+01:00
---

Voor ACS550 zie [RPBA Drive ACS550](onenote:#RPBA%20Drive%20ACS550&section-id={71DC46C3-50CB-4E25-A2E6-44D5FF9BB3FD}&page-id={A07A9FD1-A5C5-43DD-BA6D-F2253F610DEA}&end&base-path=https://d.docs.live.net/648fe635197c5860/Docs/OneNote's/Persoonlijk%20(web)/Leveranciers/ABB/ABB.one)
Drive Parameters ACS350

| 1001     | COMM                                       |
|----------|--------------------------------------------|
| 1103     | COMM                                       |
| 1601     | COMM                                       |
| 1604     | COMM                                       |
| 9802     | EXT FBA vb ADAPT                           |
| 3018     | ~~FOUT~~ NEE                               |
| 5101     | Profibus DP                                |
| 5102     | Adres                                      |
| 5103     | Baudrate                                   |
| 5104     | PPO4 (1 of 4 instellen en terug refreshen) |
| 5105     | 1202                                       |
| 5106     | 104                                        |
| 5107     | 2501                                       |
| 5108     | 105                                        |
| 5109     | 2502                                       |
| 5110     | 106                                        |
| 5111     | 2503                                       |
| 5121     | DP mode                                    |
| **5127** | **Refresh**                                |
<u>[[2015-11-04]] 8:37</u>
Extra parameters:
5112 : temperatuur (0110)
5114 : DI's van VSD (0117)
5116 : Alarm woord1 (0308)
5118 : Alarm woord5 (0318)
5120 : Nom. Vermogen ??

Drive Parameters ACS800
(Als communicatie module in PPO1 blijft staan: Trek PB stekker uit. Zet parameter op PPO4, refresh en steek stekker terug

| 1001     | COMM.CW       |
|----------|---------------|
| 1002     | COMM.CW       |
| 1003     | Verzoek       |
| 1102     | COMM.CW       |
| 1103     | COMM.REF      |
| 1601     | COMM.CW       |
| 1604     | COMM.CW       |
| 9802     | Fieldbus      |
| 9807     | ABB           |
| 3018     | FOUT of nee   |
| 5101     | Profibus DP   |
| 5102     | Adres         |
| 5103     | Baudrate      |
| 5104     | PPO4          |
| 5105     | 1202          |
| 5106     | 104 (current) |
| 5107     | 2501          |
| 5108     | 105 (torque)  |
| 5109     | 2502          |
| 5110     | 106 (power)   |
| 5111     | 2503          |
| 5121     | 0             |
| **5127** | **Refresh**   |

1104 ext ref min moet op nul staan

- # Drive Standaard
  | 1   | Status |
  |-----|--------|
  | 2   |       |
  
  ![image1](image1-531.png)
  
  Vermogen wordt in % weegegeven