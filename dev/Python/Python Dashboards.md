---
date created: 2021-12-22 00:00
modified: 2025-09-15 10:27
---
vergelijking  
[Streamlit vs Dash vs Voilà vs Panel — Battle of The Python Dashboarding Giants | by Stephen Kilcommins | DataDrivenInvestor](https://medium.datadriveninvestor.com/streamlit-vs-dash-vs-voil%C3%A0-vs-panel-battle-of-the-python-dashboarding-giants-177c40b9ea57)
 
Voorlopige keuze Dash (plotly) of Streamlit

![Exported image](Exported%20image%2020250721193446-0.jpeg)  

22/12/2021
 
|   |   |   |
|---|---|---|
||##### Dash|##### Streamlit|
|Authenication|ja|nee|
|Editable table|ja|nee|
|Auto refresh|ja|ja|
||||
 
Voorlopige keuze Dash
 
# 31/05/2022

De vraag van een dashboard staat in mijn doelstellingen  
Dus verder kijken
 
|   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
||Dash / Plotly  <br>(gratis)|Azure  <br>(powerbi)|Ignition|Grafana  <br>(gratis)|TwinCat (Beckhoff)|Siemens WinCC|PRTG|Influxdb|Open Automation Software|
|main purpose|data analytics|||dashboards|scada|scada|network monitoring|tsdb|scada|
||[Dash Enterprise App Gallery](https://dash.gallery/Portal/)|||[Grafana](https://tonnylemmens.grafana.net/a/cloud-home-app)|||||[Visualization Tools \| Industrial IoT Data Platform (openautomationsoftware.com)](https://openautomationsoftware.com/products/visualization-tools/)|
|Tonen van historian data|via TSDB|||via TSDB|||via OPC UA sensors|via telegraph plugin||
|In cloud|mogelijk|ja||mogelijk|nee|nee|ja|mogelijk||
|Tonen van SQL queries||||||||||
|Alerting||||ja|||ja|||
|||||||||||
|||||||||||
|||||||||||
|Voorlopige conclusie||||||||||
|Extra info||||Geïnstalleerd op **EnergyManger** pc||||Geïnstalleerd op **EnergyManager** pc||