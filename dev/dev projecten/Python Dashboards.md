---
date created: 2021-12-22T00:00:00+01:00
tags: [Dash, Python, Streamlit]
modified: 2025-08-29
date modified: 2025-12-03T14:48:27+01:00
---
# Python Dashboards

- # Vergelijking
  [Streamlit vs Dash vs Voilà vs Panel — Battle of The Python Dashboarding Giants \| by Stephen Kilcommins \| DataDrivenInvestor](https://medium.datadriveninvestor.com/streamlit-vs-dash-vs-voil%C3%A0-vs-panel-battle-of-the-python-dashboarding-giants-177c40b9ea57)
  
  Voorlopige keuze [[dev/dev projecten/Dash]] (plotly) of [[dev/dev projecten/Streamlit]]
  ![image1](image1-8.jpg)
  
  [[2021-12-22]]
  
  <table>
  <colgroup>
  <col style="width: 44%" />
  <col style="width: 27%" />
  <col style="width: 28%" />
  </colgroup>
  <thead>
  <tr class="header">
  <th></th>
  <th><h5 id="dash">Dash</h5></th>
  <th><h5 id="streamlit">Streamlit</h5></th>
  </tr>
  </thead>
  <tbody>
  <tr class="odd">
  <td>Authenication</td>
  <td>ja</td>
  <td>nee</td>
  </tr>
  <tr class="even">
  <td>Editable table</td>
  <td>ja</td>
  <td>nee</td>
  </tr>
  <tr class="odd">
  <td>Auto refresh</td>
  <td>ja</td>
  <td>ja</td>
  </tr>
  <tr class="even">
  <td></td>
  <td></td>
  <td></td>
  </tr>
  </tbody>
  </table>
  
  Voorlopige keuze Dash
- # [[2022-05-31]] 
  De vraag van een dashboard staat in mijn [[doelstellingen]]
  Dus verder kijken
  
  <table style="width:100%;">
  <colgroup>
  <col style="width: 8%" />
  <col style="width: 8%" />
  <col style="width: 7%" />
  <col style="width: 6%" />
  <col style="width: 11%" />
  <col style="width: 8%" />
  <col style="width: 6%" />
  <col style="width: 8%" />
  <col style="width: 11%" />
  <col style="width: 22%" />
  </colgroup>
  <thead>
  <tr class="header">
  <th></th>
  <th><p>Dash / Plotly</p>
  <p>(gratis)</p></th>
  <th><p>Azure</p>
  <p>(powerbi)</p></th>
  <th>Ignition</th>
  <th><p>Grafana</p>
  <p>(gratis)</p></th>
  <th>TwinCat (Beckhoff)</th>
  <th>Siemens WinCC</th>
  <th>PRTG</th>
  <th>Influxdb</th>
  <th>Open Automation Software</th>
  </tr>
  </thead>
  <tbody>
  <tr class="odd">
  <td>main purpose</td>
  <td>data analytics</td>
  <td></td>
  <td></td>
  <td>dashboards</td>
  <td>scada</td>
  <td>scada</td>
  <td>network monitoring</td>
  <td>tsdb</td>
  <td>scada</td>
  </tr>
  <tr class="even">
  <td></td>
  <td><a href="https://dash.gallery/Portal/">Dash Enterprise App Gallery</a></td>
  <td></td>
  <td></td>
  <td><p><a href="https://tonnylemmens.grafana.net/a/cloud-home-app">Grafana</a></p>
  <p></p></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td><a href="https://openautomationsoftware.com/products/visualization-tools/">Visualization Tools | Industrial IoT Data Platform (openautomationsoftware.com)</a></td>
  </tr>
  <tr class="odd">
  <td>Tonen van historian data</td>
  <td>via TSDB</td>
  <td></td>
  <td></td>
  <td>via TSDB</td>
  <td></td>
  <td></td>
  <td>via OPC UA sensors</td>
  <td>via telegraph plugin</td>
  <td></td>
  </tr>
  <tr class="even">
  <td>In cloud</td>
  <td>mogelijk</td>
  <td>ja</td>
  <td></td>
  <td>mogelijk</td>
  <td>nee</td>
  <td>nee</td>
  <td>ja</td>
  <td>mogelijk</td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>Tonen van SQL queries</td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="even">
  <td>Alerting</td>
  <td></td>
  <td></td>
  <td></td>
  <td>ja</td>
  <td></td>
  <td></td>
  <td>ja</td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="even">
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="even">
  <td>Voorlopige conclusie</td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
  </tr>
  <tr class="odd">
  <td>Extra info</td>
  <td></td>
  <td></td>
  <td></td>
  <td>Geïnstalleerd op <strong>EnergyManger</strong> pc</td>
  <td></td>
  <td></td>
  <td></td>
  <td>Geïnstalleerd op <strong>EnergyManager</strong> pc</td>
  <td></td>
  </tr>
  </tbody>
  </table>