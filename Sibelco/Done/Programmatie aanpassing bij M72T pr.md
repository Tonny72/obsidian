---
created: [[2019-09-02]]T13:20:07.0000000+02:00
tags:
  - C2
---
# Aanpassing calcineertransport

# Bunker kwaliteiten
 | BU55 | M71  | FIJN zeef                            |
  |------|------|--------------------------------------|
  | BU56 | M72  | GROF zeef                            |
  | BU57 | M72T | FIJN zeef                            |
  | BU71 | M62  | GROF zeef                            |
  | BU72 | M72  | GROF zeef                            |
  | BU73 | M72T | FIJN zeef                            |
  | BU74 | M72  | GROF zeef (vroeger soms zonder zeef) |
# Simulatie
  Niet vergeten na ombouw de simulatie-motoren te verwijderen.
# Controle van 'Oude Code'
  MMS_From
  
| CT12_KL_SV        | verwijderd                                   |
  |-------------------|----------------------------------------------|
  | CT_11_Run         | verwijderd                                   |
  | Start_overgang    | verwijderd                                   |
  | C_18_StatRun     | ok                                           |
  | C_SEQ_DZ_Stap50\_ | verwijderd                                   |
  | C_NOODWERKING     | ok                                           |
  | [[C_GT21]]            | Ok (gerbuikt voor mes)                       |
  | C_7_StatRun      | Gebruikt voor mes (enable productioncounter) |
  | C_SVZ4_StatRun    |                                             |
  | PCA01_Run         |                                             |
# TODO
  CT_16 MotorValue C.1.12.4.5
  IO unspecified in kleppen
  Controle CT_DV301 =\> OK
# Fouten
  Omschakeling bunker 72 start eerst CT 1 op wat goed is.
  Daarna wil sequentie CT4 starten maar eerst moet CT3 gestart worden.
  
  =\> Aangepast
  
  -------------------------------------------------------------------------
  
  Overgang van Bu74 naar Bu73 wordt er niet voldoende gespoeld voor T kwaliteit. BU73 is M72T en er wordt maar enkele seconden gespoeld naar Bu74 waarna snik [[CT_2]] word omgedraaid naar Bu73
  
  Spoelen aanpassen.
  
  -------------------------
  
  Bij overgang 73 naar 74 valt [[CT_8]] uit
  =\> In stap 240 wordt ST_07_SVA162 geopend. Er komt dan een vergrendeling actief
  
  Bij overgang van Bu73 naar Bu72 moet snik [[CT_3]] ook gestart worden.
  Maar dan gaat de sequentie verder: start [[CT_7]] en dan valt alles ervoor uit Dus CT_8-9-10-11-12-13 vallen uit en worden in een latere stap terug opgestart.
  Deze snikken moeten alle tijden blijven draaien anders valt heel het transport uit.