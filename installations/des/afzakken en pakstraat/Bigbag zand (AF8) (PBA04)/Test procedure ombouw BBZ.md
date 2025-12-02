---
title: Test procedure ombouw BBZ
updated: [[2019-01-17]]T14:11:14.0000000+01:00
created: [[2018-09-19]]T12:53:51.0000000+02:00
---

- # Wat moet er worden getest ?
  LIJNEN in het groen zijn volledig geprogrammeerd en getest.
  
  [Test Sheet omprogrammatie BBZ.docx](https://sibelco-my.sharepoint.com/:w:/p/tonny_lemmens/EbAV7D3Sz9xKpBHzNIomHsABa0V9Ve1MtQYR7fNP998C2A?e=5IoeHW)
  
  [IO omprogrammatie BBZ.xlsx](https://sibelco-my.sharepoint.com/:x:/p/tonny_lemmens/ERFi8t-bdKpMjhEei9zrIFUBywNmfMS8--tdIQgMs2HWhA?e=XZHmaR)
- # VIA Local Panel
- ## Kruisassen
- Neem volgende pallet.
- Kruisas naar boven of beneden via drukknop aan paal
- Display kruisas in de juiste stand
- Display pallet aanwezig
- # VIA WORKPLACE
- ## MotorUni
- Security voor PV Des
- ## IO
  (is alle IO gebruikt)
- ### DI1
  | Input 1  | bool | Controller_1.\_48VAC_OK         | Enkel visualisering en alarm |
  |----------|------|---------------------------------|------------------------------|
  | Input 2  | bool | Controller_1.MACH_UIT           | Enkel visualisering en alarm |
  | Input 3  | bool | Controller_1.NOODSTOP           | Enkel visualisering en alarm |
  | Input 4  | bool |                                |                             |
  | Input 5  | bool | Controller_1.Kruisas1_C\_FWD    |                             |
  | Input 6  | bool | Controller_1.Kruisas1_C\_BWD    |                             |
  | Input 7  | bool | Controller_1.Kruisas2_C\_FWD    |                             |
  | Input 8  | bool | Controller_1.Kruisas2_C\_BWD    |                             |
  | Input 9  | bool | Controller_1.Rol_aanvoer_C\_FWD |                             |
  | Input 10 | bool | Controller_1.Rol_aanvoer_C\_BWD |                             |
  | Input 11 | bool | AF8_RB_STT                      | Rollenbaan mag draaien       |
  | Input 12 | bool | AF8_PRT_RDY                     | Labelprinter ready           |
  | Input 13 | bool | Disp_6pall                      | Nog 6 palletten              |
  | Input 14 | bool | Controller_1.Disp_leeg          | Dispencer leeg               |
  | Input 15 | bool | Controller_1.Kruis1_gedr        |                             |
  | Input 16 | bool | Controller_1.Kruis2_gedr        |                             |
- ### DI2
  | Input 1  | bool | Controller_1.Disp_lichtsch             |    |
  |----------|------|----------------------------------------|-----|
  | Input 2  | bool | Controller_1.Disp_Pall_geval           |    |
  | Input 3  | bool | Controller_1.Rol_aanvoer_pall_aanwezig |    |
  | Input 4  | bool | Controller_1.Reserve_1\_1_2\_4         |    |
  | Input 5  | bool | Controller_1.Reserve_1\_1_2\_5         |    |
  | Input 6  | bool | Controller_1.Reserve_1\_1_2\_6         |    |
  | Input 7  | bool | Controller_1.Reserve_1\_1_2\_7         |    |
  | Input 8  | bool | Controller_1.Vent_vormbl_C\_FWD        |    |
  | Input 9  | bool | Controller_1.Lift_VFD_OK               |    |
  | Input 10 | bool | Controller_1.Tril_A\_C_FWD             |    |
  | Input 11 | bool | Controller_1.Tril_B\_C_FWD             |    |
  | Input 12 | bool | Controller_1.Rol_BBvuller_C\_FWD       |    |
  | Input 13 | bool | Controller_1.Rol_BBvuller_C\_BWD       |    |
  | Input 14 | bool | Controller_1.Sibelco_in_OK             |    |
  | Input 15 | bool | Controller_1.Sibelco_in_AL             |    |
  | Input 16 | bool | Controller_1.Reserve_1\_1_2\_16        |    |
- ### DI3
  | Input 1  | bool | Controller_1.Draaiblok_OK      |    |
  |----------|------|--------------------------------|-----|
  | Input 2  | bool | Controller_1.Haak1_OK          |    |
  | Input 3  | bool | Controller_1.Haak2_OK          |    |
  | Input 4  | bool | Controller_1.Haak3_OK          |    |
  | Input 5  | bool | Controller_1.Haak4_OK          |    |
  | Input 6  | bool | Controller_1.Haak5_OK          |    |
  | Input 7  | bool | Controller_1.Haak6_OK          |    |
  | Input 8  | bool | Controller_1.BB_aanwezig       |    |
  | Input 9  | bool | Controller_1.Wurgdruk_OK       |    |
  | Input 10 | bool | Controller_1.Blaasklep_open    |    |
  | Input 11 | bool | Controller_1.Blaasklep_dicht   |    |
  | Input 12 | bool | Controller_1.Losklep_open      |    |
  | Input 13 | bool | Controller_1.Losklep_dicht     |    |
  | Input 14 | bool | Controller_1.BB_pall1_aanwezig |    |
  | Input 15 | bool | Controller_1.BB_pall2_aanwezig |    |
  | Input 16 | bool | Controller_1.BB_lift_MAXMAX    |    |
- ### DI4
  | Input 1  | bool | Controller_1.BB_lift_minmin     |    |
  |----------|------|---------------------------------|-----|
  | Input 2  | bool | Controller_1.BB_lift_veilig_L   |    |
  | Input 3  | bool | Controller_1.BB_lift_veilig_R   |    |
  | Input 4  | bool |                                |    |
  | Input 5  | bool | Controller_1.BB_lift_puls_zero  |    |
  | Input 6  | bool | Controller_1.Reserve_1\_1_4\_6  |    |
  | Input 7  | bool | Controller_1.Reserve_1\_1_4\_7  |    |
  | Input 8  | bool | Controller_1.Reserve_1\_1_4\_8  |    |
  | Input 9  | bool | Controller_1.Weeg_in_grof       |    |
  | Input 10 | bool | Controller_1.Weeg_in_mid        |    |
  | Input 11 | bool | Controller_1.Weeg_in_fijn       |    |
  | Input 12 | bool | Controller_1.Weeg_in_dos_gereed |    |
  | Input 13 | bool | Controller_1.Weeg_in_leeg       |    |
  | Input 14 | bool | Controller_1.Weeg_in_gereed     |    |
  | Input 15 | bool | Controller_1.Weeg_in_tol_fout   |    |
  | Input 16 | bool | Controller_1.Weeg_in_alarm      |    |
- ### DI5
  | Input 1  | bool | Controller_1.Rol_afvoer12_C\_FWD                  |    |
  |----------|------|---------------------------------------------------|-----|
  | Input 2  | bool | Controller_1.Rol_afvoer12_C\_BWD                  |    |
  | Input 3  | bool | Controller_1.Rol_afvoer34_C\_FWD                  |    |
  | Input 4  | bool | Controller_1.Rol_afvoer34_C\_BWD                  |    |
  | Input 5  | bool | Controller_1.Rol_afvoer56_C\_FWD                  |    |
  | Input 6  | bool | Controller_1.Rol_afvoer56_C\_BWD                  |    |
  | Input 7  | bool | Controller_1.Reserve_1\_1_5\_7                    |    |
  | Input 8  | bool | Controller_1.Reserve_1\_1_5\_8                    |    |
  | Input 9  | bool | Controller_1.Rol_afvoer1_pall_aanwezig            |    |
  | Input 10 | bool | Controller_1.Rol_afvoer2_pall_aanwezig            |    |
  | Input 11 | bool | Controller_1.Rol_afvoer3_pall_aanwezig            |    |
  | Input 12 | bool | Controller_1.Rol_afvoer4_pall_aanwezig            |    |
  | Input 13 | bool | Controller_1.Rol_afvoer5_pall_aanwezig            |    |
  | Input 14 | bool | Controller_1.Rol_afvoer6_pall_aanwezig            |    |
  | Input 15 | bool | Controller_1.Rol_afvoer6_truck_aanwezig           |    |
  | Input 16 | bool | Controller_1.Program2.Aanvoer_pall_truck_aanwezig |    |
- ### DO6
  | Output 1  | bool | Controller_1.RST_noodstop       |    |
  |-----------|------|---------------------------------|-----|
  | Output 2  | bool | Controller_1.Overbrug_mach_uit  |    |
  | Output 3  | bool | Controller_1.Reserve_1\_1_6\_3  |    |
  | Output 4  | bool | Controller_1.Reserve_1\_1_6\_4  |    |
  | Output 5  | bool | Controller_1.C_Kruisas1_FWD     |    |
  | Output 6  | bool | Controller_1.C_Kruisas1_BWD     |    |
  | Output 7  | bool | Controller_1.C_Kruisas2_FWD     |    |
  | Output 8  | bool | Controller_1.C_Kruisas2_BWD     |    |
  | Output 9  | bool | Controller_1.C_Rol_aanvoer_FWD  |    |
  | Output 10 | bool | Controller_1.C_Rol_aanvoer_BWD  |    |
  | Output 11 | bool | Controller_1.Reserve_1\_1_6\_11 |    |
  | Output 12 | bool | Controller_1.C_Vent_vormbl_FWD  |    |
  | Output 13 | bool | Controller_1.VFD_Lift_start     |    |
  | Output 14 | bool | Controller_1.VFD_Lift_omkeer    |    |
  | Output 15 | bool | Controller_1.VFD_Lift_HS        |    |
  | Output 16 | bool | Controller_1.C_Tril_FWD         |    |
- ### DO7
  | Output 1  | bool | Controller_1.C_Tril_rem         |    |
  |-----------|------|---------------------------------|-----|
  | Output 2  | bool | Controller_1.C_Rol_BBvuller_FWD |    |
  | Output 3  | bool | Controller_1.C_Rol_BBvuller_BWD |    |
  | Output 4  | bool | Controller_1.Reserve_1\_1_7\_4  |    |
  | Output 5  | bool | Controller_1.Wurgophang         |    |
  | Output 6  | bool | Controller_1.Blaasklep          |    |
  | Output 7  | bool | Controller_1.Haak1_2\_3_4       |    |
  | Output 8  | bool | Controller_1.Losklep            |    |
  | Output 9  | bool | Controller_1.Wurgophang_af      |    |
  | Output 10 | bool | Controller_1.Weeg_out_start     |    |
  | Output 11 | bool | Controller_1.Weeg_out_rst       |    |
  | Output 12 | bool | Controller_1.Weeg_out_grof      |    |
  | Output 13 | bool | Controller_1.Weeg_out_mid       |    |
  | Output 14 | bool | Controller_1.Weeg_out_fijn      |    |
  | Output 15 | bool | Controller_1.Reserve_1\_1_7\_15 |    |
  | Output 16 | bool | Controller_1.Reserve_1\_1_7\_16 |    |
- ### DO8
  | Output 1  | bool | Controller_1.C_Rol_afvoer12_FWD |    |
  |-----------|------|---------------------------------|-----|
  | Output 2  | bool | Controller_1.C_Rol_afvoer12_BWD |    |
  | Output 3  | bool | Controller_1.Reserve_1\_1_8\_3  |    |
  | Output 4  | bool | Controller_1.C_Rol_afvoer34_FWD |    |
  | Output 5  | bool | Controller_1.C_Rol_afvoer34_BWD |    |
  | Output 6  | bool | Controller_1.Reserve_1\_1_8\_6  |    |
  | Output 7  | bool | Controller_1.C_Rol_afvoer56_FWD |    |
  | Output 8  | bool | Controller_1.C_Rol_afvoer56_BWD |    |
  | Output 9  | bool | Controller_1.Reserve_1\_1_8\_9  |    |
  | Output 10 | bool | Controller_1.Reserve_1\_1_8\_10 |    |
  | Output 11 | bool | Controller_1.Reserve_1\_1_8\_11 |    |
  | Output 12 | bool | Controller_1.Reserve_1\_1_8\_12 |    |
  | Output 13 | bool | Controller_1.Reserve_1\_1_8\_13 |    |
  | Output 14 | bool | Controller_1.Reserve_1\_1_8\_14 |    |
  | Output 15 | bool | Controller_1.Reserve_1\_1_8\_15 |    |
  | Output 16 | bool | Controller_1.Reserve_1\_1_8\_16 |    |