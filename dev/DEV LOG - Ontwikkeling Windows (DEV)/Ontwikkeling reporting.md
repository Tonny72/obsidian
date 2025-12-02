---
tags: [reporting]
modified:  2025-08-29
date created: 2021-10-15T00:00:00+02:00
date modified: 2025-09-19T21:11:09+02:00
---
## Links
- [[DEV LOG]]

## Log
[[2021-10-15]]

Doel: automatiseren van energie-rapporten  
Bouwen van het (dag, week, maand) rapport  
Clean Data bewaren per 5 minuten, opsplitsen per maand
 
- inlezen van config
- inlezen van de raw CSV data om de laatste raw dts te bekomen
- inlezen van de volledige laatste clean CSV data om de laatste clean dts te bekomen en omdat waarschijnlijk de data van de volledige maand wordt gebruikt.
- inlezen van OPCHDA data
- wegschrijven van raw CSV data
- cleanen van de CSV data

[[2021-10-18]] 
Mooi werkend script in **tutils.py**
  
  ```python
  if __name__=='__main__':
    path = "D:/OneDrive - Sibelco/Energy/DES/DATA/FPV_Active_Energy_Export/"
    tag = "FPV_Active_Energy_Export"
    path = "D:/OneDrive - Sibelco/Energy/DES/DATA/"
  
  if len(sys.argv) \> 1:
   config_file = sys.argv\[1\]
  else:
  
  config_file = "D:/OneDrive - Sibelco/DEV/Python/configs/dessel_config.yaml"
  file_location, hda_server, tag_config_list = parse_config.parse_config(config_file)
  
  for tagconfig in tag_config_list:
  	tag_name = tagconfig\['Name'\] \#, tagconfig\['Path'\], tagconfig\['SignalType'\], tagconfig\['Log'\], file_location, hda_server)
  	tag_signal_type = tagconfig\['SignalType'\]
  
  tag_log = tagconfig\['Log'\]
  
  tag_use_in_energy_calculation = tagconfig\['UseInEnergyCalculation'\]
  
  print("path: " + path + ", Tagname = " + tag_name)
  pathTag = path + tag_name + "/"
  pathCleaned = pathTag + "Cleaned/"
  pathRaw = pathTag + "/" + tag_log + "/"
  
  if tag_signal_type=="counter":
  latestCleanDts = GetLastestFileName(pathCleaned)
  
  if latestCleanDts == "" :
  # Geen Cleaned bestanden aanwezig
  os.makedirs(pathCleaned, exist_ok=True)
  dfRaw = LoadAllRawCSV(pathRaw)
  dfClean = CleanRawCounter(dfRaw, 6.0)
  WriteCleanCSV(dfClean, pathCleaned, tag)
  else:
  print(latestCleanDts)
  \#dfClean = LoadCleanCSV(latestCleanDts)
  \# -------------------
  \# Hier verder werken
  ```