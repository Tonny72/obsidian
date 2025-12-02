---
date created: 2010-11-22]]T10:09:50.0000000+01:00
tags:
  - C2
---

lle IO wordt gedeclareerd in 1 global variabele.
1.  ***Motoren***
De IO van de motoren wordt declareerd als sibMotorIO.
Er wordt een AlarmCondM op elke FB1 gekoppeld

| **TAG**     | **Omschrijving**                       | **Aansluiting DO** | **Aansluiting DI** | **** |
|-------------|----------------------------------------|--------------------|--------------------|-------|
|[[installations/des/drogers en calcineeroven/C2/C2_1]]| Hoofdventilator Start                  | 0.11.301.1         | 0.11.201.1         |      |
| [[C2_3]]     | Ventilator Syphons Start               | 0.11.301.2         | 0.11.202.9         |      |
| **C_4**     | Transportvijs Onder Silo Start         | 0.11.301.3         | 0.11.202.9         |      |
| **C_5**     | Transportvijs Boven Buffersilo Start   | 0.11.301.4         | 0.11.202.9         |      |
| **C_6**     | Elevator Natzand Start                 | 0.11.301.5         | 0.11.203.5         |      |
| **C_7**     | Weegband Start                         | 0.11.301.6         | 0.11.203.5         |      |
| **C_8**     | Sodapomp Start                         | 0.11.301.7         | 0.11.202.9         |      |
| **C_8B**    | Sodapomp Bypass Start                  | 0.11.301.8         | 0.11.203.1         |      |
| **C_8C**    | Circulatiepomp Soda Start              | 0.11.301.9         | 0.11.203.1         |      |
| **C_11**    | Hydrauliekpomp Start                   | 0.11.301.10        | 0.11.201.10        |      |
| **C_12A**   | Oventrommel Start                      | 0.11.301.11        | 0.11.201.13        |      |
| **C_12C**   | Hulpaandrijving Trommel Start          | 0.11.301.12        | 0.11.201.12        |      |
| **C_13**    | Ventilator Koeling Brander Start       | 0.11.301.13        | 0.11.201.14        |      |
| **C_14**    | Ventilator Primair Lucht Brander Start | 0.11.301.14        | 0.11.201.15        |      |
| **C_18**    | Transportvijs Afvoer Zand Start        | 0.11.301.15        | 0.11.201.16        |      |
| **C_19**    | Transportband Afval Start              | 0.11.301.16        | 0.11.202.1         |      |
| **C_20**    | Vibratoren Uitloop Vvh Start           | 0.11.302.1         | 0.11.202.2         |      |
| **C_21**    | Vetsmeerapp Start                      | 0.11.302.2         | 0.11.202.3         |      |
| **C_22**    | Ventilator 1 Wervelbedkoeler Start     | 0.11.302.3         | 0.11.202.5         |      |
| **C_23**    | Transportvijs Onder Koeler Start       | 0.11.302.4         | 0.11.202.6         |      |
| **C_24**    | Ventilator 2 Wervelbedkoeler Start     | 0.11.302.5         | 0.11.202.8         |      |
| **C_25**    | Ventilator Uitloop Oven Start          | 0.11.302.6         | 0.11.202.9         |      |
| **C_WP4**   | Waterpomp 4 Start                      | 0.11.302.7         | 1.10.3.12          |      |
| **C_WP5**   | Waterpomp 5 Start                      | 0.11.302.8         | 1.10.3.12          |      |
| **C_WP1**   | Pomp 1 Start                           | 0.11.302.9         | 1.10.3.12          |      |
| **C_WP2**   | Pomp 2 Start                           | 0.11.302.10        | 1.10.3.12          |      |
| **C_28**    | Hogedrukpomp Start                     | 0.11.302.11        | ??                 |      |
| **C_29**    | Vibrator Uitloop Start                 | 0.11.302.12        | 0.11.202.15        |      |
| **C_31**    | Nalcopomp 1 Start                      | 0.11.302.13        | 0.11.202.16        |      |
| **C_32**    | Nalcopomp 2 Start                      | 0.11.302.14        | 0.11.203.1         |      |
| **C_OP1**   | Stookoliepomp 1 Start                  | 0.11.302.15        | 0.11.206.2         |      |
| **C_OP2**   | Stookoliepomp 2 Start                  | 0.11.302.16        | 1.10.2.16          |      |
| **C_33**    | Transportvijs Start                    | 0.11.303.2         | 0.11.203.1         |      |
|            |                                       |                   |                   |      |
| **C_30**    | Vibrator Inloop C_6 Start              | 0.11.304.2         |                   |      |
| **C_24I**   | Vent C_14 In                           | 1.10.4.7           |                   |      |
| **CT1_L**   | Vijs Naar Zs73 Start                   | 1.12.1.1           | 1.11.3.14          |      |
| **CT1_R**   | Vijs Naar Zs71 Start                   | 1.12.1.2           | 1.11.3.14          |      |
| **CT2_L**   | Vijs Naar Zs72 Start                   | 1.12.1.3           | 1.11.3.14          |      |
| **CT2_R**   | Vijs Naar Zs74 Start                   | 1.12.1.4           | 1.11.4.14          |      |
| **CT3**     | Vijs Start                             | 1.12.1.5           | 1.11.4.14          |      |
| **CT4**     | Vijs Start                             | 1.12.1.6           | 1.11.4.14          |      |
| **CT5**     | Elevator Start                         | 1.12.1.7           | 1.11.4.14          |      |
| **CT6**     | Vijs Start                             | 1.12.1.8           | 1.11.4.14          |      |
| **CT7**     | Vijs Start                             | 1.12.1.9           | 1.11.4.14          |      |
| **CT8**     | Vijs Start                             | 1.12.1.10          | 1.11.4.14          |      |
| **CT9**     | Vijs Start                             | 1.12.1.11          | 1.11.4.14          |      |
| **CT10**    | Vijs Start                             | 1.12.1.12          | 1.11.4.14          |      |
| **CT11**    | Vijs Start                             | 1.12.1.13          | 1.11.4.14          |      |
| **CT12**    | Vijs Start                             | 1.12.1.14          | 1.11.4.14          |      |
| **CT13**    | Elevator Start                         | 1.12.1.15          | 1.11.1.2           |      |
| **CT14**    | Zeef Start                             | 1.12.1.16          | 1.11.1.16          |      |
| **CT15**    | Zeef Start                             | 1.12.2.1           | 1.11.3.14          |      |
| **CT23**    | Afzuigventilator Start                 | 1.12.2.2           | 1.11.3.14          |      |
| **CT21**    | Cellenrad Start                        | 1.12.2.3           | 1.11.2.9           |      |
| **CT_VAFZ** | Afzuigventilator Start                 | 1.12.2.4           | 1.10.3.12          |      |
| **CT16**    | Elevator Start                         | 1.12.2.5           | 1.11.4.14          |      |
| **CT17**    | Ventilator Filter Afzeving Start       | 1.12.2.6           | 1.11.3.14          |      |
| **CT17B**   | Filtermekaniek Afzeving Start          | 1.12.2.7           | 1.11.3.14          |      |
| **CT19**    | Pulsklep Start                         | 1.12.2.8           | 1.11.3.14          |      |
| **CT18**    | Magneet Start                          | 1.12.2.9           | 1.11.3.14          |      |
| **CT24**    | Transportvijs Start                    | 1.12.2.10          | 1.11.3.14          |      |
| **CT25**    | Rotexzeef Start                        | 1.12.2.11          | 1.11.3.14          |      |
| **CT16_T**  | Ct16 Elevator Trage Snelheid           | 1.12.3.9           | 1.11.3.14          |      |
| **CT23B**   | Filtermek Start                        | 1.12.3.10          | 1.11.3.14          |      |

| **C_VS_RS_I** | **Vetsmeringrollenbaan Start** | **0.11.304.1** | **1.10.3.6** |
|---------------|--------------------------------|----------------|--------------|

2.  ***Kleppen***
| **TAG** | **Omschrijving** | **Vergrendelingen** |
|---------|------------------|---------------------|
|        |                 |                    |
|        |                 |                    |
3.  ***Digitale Ingangen***
| **TAG**               | **Omschrijving**                       | **Aansluiting** |
|-----------------------|----------------------------------------|-----------------|
| **C_1\_DI**           | Hoofdventilator Draait                 | 0.11.201.1      |
| **C_3\_DI**           | Ventilator Syphons Draait              | 0.11.201.2      |
| **C_4\_DI**           | Transportvijs Onder Silo Draait        | 0.11.201.3      |
| **C_5\_DI**           | Transportvijs Boven Buffersilo Draait  | 0.11.201.4      |
| **C_6\_DI**           | Elevator Natzand Draait                | 0.11.201.5      |
| **C_7\_DI**           | Weegband Draait                        | 0.11.201.6      |
| **C_8\_DI**           | Sodapomp Draait                        | 0.11.201.7      |
| **C_8B_DI**           | Sodapomp Bypass Draait                 | 0.11.201.8      |
| **C_8C_DI**           | Circulatie Sodapomp Draait             | 0.11.201.9      |
| **C_11_DI**           | Hydrauliekgroep Draait                 | 0.11.201.10     |
| **C_12A_DI**          | Oventrommel Draait                     | 0.11.201.11     |
| **C_12C_DI**          | Hulpaandrijvingtrommel Draait          | 0.11.201.12     |
| **C_12_NS_DI**        | Noodstop Oventrommel ( In Bedrijf=0)   | 0.11.201.13     |
| **C_13_DI**           | Ventilator Koeling Brander Draait      | 0.11.201.14     |
| **C_14_DI**           | Ventilator Primairlucht Brander Draait | 0.11.201.15     |
| **C_18_DI**           | Transportvijs Afvoer Zand Draait       | 0.11.201.16     |
| **C_19_DI**           | Transportband Afval Draait             | 0.11.202.1      |
| **C_20_DI**           | Vibratoren Uitloop Vvh Draaien         | 0.11.202.2      |
| **C_21_DI**           | Vetsmeerapp Draait                     | 0.11.202.3      |
| **C_21_VL_DI**        | Vetsmeerapp Leegmelding                | 0.11.202.4      |
| **C_22_DI**           | Ventilator 1 Wervelbedkoeler Draait    | 0.11.202.5      |
| **C_23_DI**           | Transportvijs Onder Koeler Draait      | 0.11.202.6      |
| **C_23_stt_DI**       | Start C_23                             | 0.11.202.7      |
| **C_24_DI**           | Ventilator 2 Wervelbedkoeler Draait    | 0.11.202.8      |
| **C_25_DI**           | Ventilator Uitloop Oven Draait         | 0.11.202.9      |
| **C_WP4_DI**          | Pomp 4 Draait                          | 0.11.202.10     |
| **C_WP5_DI**          | Pomp 5 Draait                          | 0.11.202.11     |
| **C_WP1_DI**          | Pomp 1 Draait                          | 0.11.202.12     |
| **C_WP2_DI**          | Pomp 2 Draait                          | 0.11.202.13     |
| **C_28_DI**           | Hogedrukpomp Draait                    | 0.11.202.14     |
| **C_29_DI**           | Vibrator Uitloop Draait                | 0.11.202.15     |
| **C_31_DI**           | Nalcopomp 1 Draait                     | 0.11.202.16     |
| **C_32_DI**           | Nalcopomp 2 Draait                     | 0.11.203.1      |
| **C_OP1_DI**          | Stookoliepomp 1 Draait                 | 0.11.203.2      |
| **C_OP2_DI**          | Stookoliepomp 2 Draait                 | 0.11.203.3      |
| **C_33_DI**           | Transportvijs Draait                   | 0.11.203.5      |
| **C_LSH22_DI**        | Hoogniveau Uitloop C_6                 | 0.11.204.2      |
| **C_EKHY_O\_MAX_DI**  | Ek Abex Max Op                         | 0.11.204.3      |
| **C_EKHY_N\_MAX_DI**  | Ek Abex Max Neer                       | 0.11.204.4      |
| **C_LSL_HY_DI**       | Oliedruk Abex Laagniveau               | 0.11.204.5      |
| **C_VS_RSI_AL_DI**    | Alarm Vetsmering Rollenstation Inloop  | 0.11.204.6      |
| **C_VS_RSU_AL_DI**    | Alarm Vetsmering Rollenstation Uitloop | 0.11.204.7      |
| **C_AFHD_DI**         | Alarm Waterfilter                      | 0.11.204.8      |
| **C_KL_O\_VVH_A\_DI** | Kleppen Onder Vvh Op Auto              | 0.11.204.9      |
| **C_FSL_31_DI**       | Flow Voorverhitter                     | 0.11.204.10     |
| **C_FSL_1\_DI**       | Flow Gaswasser                         | 0.11.204.11     |
| **C_KP4_DI**          | Keuze C_Wp4                            | 0.11.204.12     |
| **C_KP5_DI**          | Keuze C_Wp5                            | 0.11.204.13     |
| **C_KWVS_DI**         | Keuze Pompen Wv Freq Sturing           | 0.11.204.14     |
| **C_KWVD_DI**         | Keuze Pompen Wv Dol                    | 0.11.204.15     |
| **C_TSH51_DI**        | Temp In Tandwielkast Oven              | 0.11.204.16     |
| **C_LSH21_DI**        | Hoogniveau Buffersilo                  | 0.11.205.1      |
| **C_PSL21_DI**        | Onderdruk In Buffersilo                | 0.11.205.2      |
| **C_FSL11_DI**        | Flow Water In C1                       | 0.11.205.3      |
| **C_EKHY_O\_DI**      | Ek Abex Op Inloop                      | 0.11.205.4      |
| **C_EKHY_N\_DI**      | Ek Abex Neer Uitloop                   | 0.11.205.5      |
| **C_AL101_DI**        | Calibratie Bezig                       | 0.11.205.6      |
| **C_AL102_DI**        | Systeem Alarm                          | 0.11.205.7      |
| **C_9UPS1_A\_DI**     | Alarm Ups Sa9                          | 0.11.206.1      |
| **C_9UPS1_BATT_DI**   | Mode Nok Sa9                           | 0.11.206.2      |
| **C_SPAN_DI**         | Stuurspanning In                       | 1.10.1.1        |
| **C_KG_DI**           | Keuze Gas                              | 1.10.1.2        |
| **C_KO_DI**           | Keuze Olie                             | 1.10.1.3        |
| **C_KGOK_DI**         | Keuze Gas Ok                           | 1.10.1.4        |
| **C_KOOK_DI**         | Keuze Olie Ok                          | 1.10.1.5        |
| **C_BIN_DI**          | Brander In                             | 1.10.1.6        |
| **C_OB_DI**           | Ontsteking Brander                     | 1.10.1.7        |
| **C_VOK_DI**          | Vlam Ok                                | 1.10.1.8        |
| **C_PRMN_DI**         | Primaire Luchtdruk Niet Te Laag        | 1.10.1.9        |
| **C_GFNH_DI**         | Gasfilter Dp Niet Te Hoog              | 1.10.1.10       |
| **C_GDOK_DI**         | Gasdruk Ok                             | 1.10.1.11       |
| **C_OGDNL_DI**        | Onsteking Gasdruk Niet Te Laag         | 1.10.1.12       |
| **C_STLNL_DI**        | Stuurluchtdruk Niet Te Laag            | 1.10.1.13       |
| **C_EKGOK_DI**        | Ek Gasklep Ok                          | 1.10.1.14       |
| **C_GAT_DI**          | Gasafsluiter Toe                       | 1.10.1.15       |
| **C_GAO_DI**          | Gasafsluiter Open                      | 1.10.1.16       |
| **C_GRKT_DI**         | Gasregelklep Toe                       | 1.10.2.1        |
| **C_GRKO_DI**         | Gasregelklep Open                      | 1.10.2.2        |
| **C_KLT_DI**          | Koelluchtklep 1+2 Toe                  | 1.10.2.3        |
| **C_ODOK_DI**         | Oliedusenstock In Pos                  | 1.10.2.4        |
| **C_OTNL_DI**         | Olietemp Niet Te Laag                  | 1.10.2.5        |
| **C_ODNL_DI**         | Oliedruk Niet Te Laag                  | 1.10.2.6        |
| **C_STNL_DI**         | Stuurlucht Niet Te Laag                | 1.10.2.7        |
| **C_OVOK_DI**         | Olieventiel In Pos                     | 1.10.2.8        |
| **C_OVPMN_DI**        | Olie Prim Vent In Pos Min              | 1.10.2.9        |
| **C_OVPMX_DI**        | Olie Prim Vent In Pos Max              | 1.10.2.10       |
| **C_OVSMN_DI**        | Olie Sec Vent In Pos Min               | 1.10.2.11       |
| **C_OVSMX_DI**        | Olie Sec Vent In Pos Max               | 1.10.2.12       |
| **C_ULDNL_DI**        | Uitblaasluchtdruk Niet Te Laag         | 1.10.2.13       |
| **C_VVWI_DI**         | Voorverwarming In                      | 1.10.2.14       |
| **C_FSL61_DI**        | Waterflow Wervelbed Koeler             | 1.10.2.15       |
| **C_NS_BUBR_DI**      | Noodstop Bubr                          | 1.10.2.16       |
| **C_VB_PILLARD_DI**   | Op Hand                                | 1.10.3.1        |
| **C_OVLB_DI**         | Voorloop Bedrijf Olie                  | 1.10.3.2        |
| **C_OTLB_DI**         | Terugloop Bedrijf Olie                 | 1.10.3.3        |
| **C_VAFK_DI**         | Uitloop Afval Koeler Verstopt          | 1.10.3.4        |
| **C_PSL101_DI**       | Voordruk Perslucht                     | 1.10.3.5        |
| **C_FSL101_DI**       | Detectie Perslucht Debiet              | 1.10.3.6        |
| **C_ZSL101_DI**       | Ek Ventiel Water Dicht                 | 1.10.3.7        |
| **C_ZSL102_DI**       | Ek Ventiel Nh3 Dicht                   | 1.10.3.8        |
| **C_VV1_DI**          | Vlamveiligheid 1 In Storing            | 1.10.3.9        |
| **C_VV2_DI**          | Vlamveiligheid 2 In Storing            | 1.10.3.10       |
| **C_BR_UPS_DI**       | Alarm Ups                              | 1.10.3.11       |
| **C_BR_BAT_MODE_DI**  | Batterij Mode                          | 1.10.3.12       |
| **CT1_L\_DI**         | Vijs Draait Naar Zs73                  | 1.11.1.1        |
| **CT1_R\_DI**         | Vijs Draait Naar Zs71                  | 1.11.1.2        |
| **CT2_L\_DI**         | Vijs Draait Naar Zs72                  | 1.11.1.3        |
| **CT2_R\_DI**         | Vijs Draait Naar Zs74                  | 1.11.1.4        |
| **CT3_DI**            | Vijs Draait                            | 1.11.1.5        |
| **CT4_DI**            | Vijs Draait                            | 1.11.1.6        |
| **CT5_DI**            | Elevator Draait                        | 1.11.1.7        |
| **CT6_DI**            | Vijs Draait                            | 1.11.1.8        |
| **CT7_DI**            | Vijs Draait                            | 1.11.1.9        |
| **CT3_DI**            | Vijs Draait                            | 1.11.1.10       |
| **CT9_DI**            | Vijs Draait                            | 1.11.1.11       |
| **CT10_DI**           | Vijs Draait                            | 1.11.1.12       |
| **CT11_DI**           | Vijs Draait                            | 1.11.1.13       |
| **CT12_DI**           | Vijs Draait                            | 1.11.1.14       |
| **CT13_DI**           | Elevator Draait                        | 1.11.1.15       |
| **CT14_DI**           | Zeef Draait                            | 1.11.1.16       |
| **CT15_DI**           | Zeef Draait                            | 1.11.2.1        |
| **CT23_DI**           | Ventilator Draait                      | 1.11.2.2        |
| **CT21_DI**           | Cellenrad Draait                       | 1.11.2.3        |
| **CT_VAFZ_DI**        | Ventilator Draait                      | 1.11.2.4        |
| **CT_16_DI**          | Elevator Draait                        | 1.11.2.5        |
| **CT17_DI**           | Ventilator Draait                      | 1.11.2.6        |
| **CT17B_DI**          | Filtermek Draait                       | 1.11.2.7        |
| **CT19_DI**           | Pulsklep Draait                        | 1.11.2.8        |
| **CT18_DI**           | Magneet Draait                         | 1.11.2.9        |
| **CT24_DI**           | Transportvijs Draait                   | 1.11.2.10       |
| **CT25_DI**           | Zeef Draait                            | 1.11.2.11       |
| **CT_KL57_O\_DI**     | Klep Open                              | 1.11.3.1        |
| **CT_KL57_T\_DI**     | Klep Toe                               | 1.11.3.2        |
| **CT_KL56_O\_DI**     | Klep Open                              | 1.11.3.3        |
| **CT_KL56_T\_DI**     | Klep Toe                               | 1.11.3.4        |
| **CT_KL55A_O\_DI**    | Klep Open                              | 1.11.3.5        |
| **CT_KL55A_T\_DI**    | Klep Toe                               | 1.11.3.6        |
| **CT_KL54_O\_DI**     | Klep Open                              | 1.11.3.7        |
| **CT_KL54_T\_DI**     | Klep Toe                               | 1.11.3.8        |
| **CT_KLAFV_O\_DI**    | Klep Open                              | 1.11.3.9        |
| **CT_KLAFV_T\_DI**    | Klep Toe                               | 1.11.3.10       |
| **CT_KL55B_O\_DI**    | Klep Open                              | 1.11.3.11       |
| **CT_KL55B_T\_DI**    | Klep Toe                               | 1.11.3.12       |
| **CT_KL14_KL_O\_DI**  | Klep Open                              | 1.11.3.13       |
| **CT_KL14_KL_T\_DI**  | Klep Toe                               | 1.11.3.14       |
| **LSH_ZS57_DI**       | Hoogniveau Zs57                        | 1.11.4.1        |
| **LSH_ZS56_DI**       | Hoogniveau Zs56                        | 1.11.4.2        |
| **LSH_ZS55_DI**       | Hoogniveau Zs55                        | 1.11.4.3        |
| **LSH_ZS54_DI**       | Hoogniveau Zs54                        | 1.11.4.4        |
| **CT_16_LSH_DI**      | Hoogniv Uitloop Ct_16                  | 1.11.4.7        |
| **CT_16_H\_DI**       | Elevator Op Hand                       | 1.11.4.8        |
| **CT_AS_LSH_DI**      | Hoogniv Afvalsilo                      | 1.11.4.9        |
| **CT_14_ZS_DI**       | Kontrole Zeef Stuk                     | 1.11.4.10       |
| **CT_NS_IN_DI**       | Noodstop In                            | 1.11.4.11       |
| **CT_18_SOK_DI**      | Status Magn Ok                         | 1.11.4.12       |
| **CT_A\_UPS_DI**      | Alarm Ups                              | 1.11.4.13       |
| **CT_BAT_MODE_DI**    | Batterij Mode                          | 1.11.4.14       |

4.  ***Digitale Uitgangen***
| **TAG** | **Omschrijving** | **FP / IND** | **Aansluiting** | **Onderdeel van Object** |
|---------|------------------|--------------|-----------------|--------------------------|
|        |                 |             |                |                         |
|        |                 |             |                |                         |
|        |                 |             |                |                         |
|        |                 |             |                |                         |
| ****   |                 |             |                |                         |
| ****   |                 |             |                |                         |
| ****   |                 |             |                |                         |
| ****   |                 |             |                |                         |

******
******
5.  ***Analoge Ingangen***
| **TAG** | **Omschrijving** | **FP/IN** | **Aansluiting** | **Onderdeel van Object** | **LLL** | **LL** | **L** | **H** | **HH** | **HHH** | **Range** | **Unit** | **Range channel** |
|---------|------------------|-----------|-----------------|--------------------------|---------|--------|-------|-------|--------|---------|-----------|----------|-------------------|
|        |                 |          |                |                         |        |       |      |      |       |        |          |         |                  |
|        |                 |          |                |                         |        |       |      |      |       |        |          |         |                  |
|        |                 |          |                |                         |        |       |      |      |       |        |          |         |                  |
|        |                 |          |                |                         |        |       |      |      |       |        |          |         |                  |
|        |                 |          |                |                         |        |       |      |      |       |        |          |         |                  |
|        |                 |          |                |                         |        |       |      |      |       |        |          |         |                  |
|        |                 |          |                |                         |        |       |      |      |       |        |          |         |                  |
|        |                 |          |                |                         |        |       |      |      |       |        |          |         |                  |

2.  **Testprocedure**
1.  ***DI’s***
<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 47%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>TAG</strong></p>
<p><strong>DI</strong></p></th>
<th><strong>Omschrijving</strong></th>
<th><strong></strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
2.  ***AI’s***
| **TAG** | **Omschrijving** |    |
|---------|------------------|-----|
|        |                 |    |
|        |                 |    |
|        |                 |    |
|        |                 |    |
| ****   |                 |    |

3.  ***Motoren***
1.  BD_DP Dieptepomp

- Manueel starten =\> OK
  2.  BD_GWP Glandwaterpomp
- Manueel starten =\> OK
  3.  BD_ZP1 Zandpomp1
- Manueel starten =\> OK
- Stroom controleren (BD_ITZP1) =\> OK
  4.  BD_ZP2 Zandpomp2
- Manueel starten =\> OK
- Stroom controleren (BD_ITZP2) =\> OK
  5.  Noodstop
- BD_NSTPLOC vergrendelt alle 4 de pompen =\> OK
  4.  ***Sequentie***
- Start de sequentie lokaal (BD_STTLOC) =\> OK
- Stop de sequentie lokaal (BD_STPLOC) =\> OK
  
  5.  ***DO’s***
  | **TAG**            | **Omschrijving**             |    |
  |--------------------|------------------------------|-----|
  | **BD_VERLICHTING** | Verlichting Booster          | OK  |
  | **BD_IH**          | Indicatie booster op hand    |    |
  | **BD_IB**          | Indicatie booster in bedrijf | OK  |
  | ****              |                             |    |