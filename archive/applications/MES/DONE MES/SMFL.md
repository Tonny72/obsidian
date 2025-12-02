---
date created: 2014-10-20
modified: 2025-08-31
---

De koppeling van SMFL komt van PLC zakscheur.

- # Programma PLC zakscheur (PC1.1.4.1)
  ![image1](image1-622.png)
- # Programma PLC Rotoseal (PC1.10.7.2)
  ![image2](image2-263.png)
- # Programma PLC Sibelco (PC14.7.13.4)
  ![image3](image3-155.png)
  Programma Molen_5
  DAT_From_S\_M4M5.OB3_K1_DI := BS_S\_M4M5_3\_B10.value27; (# OB3_K1_DI \#)
  DAT_From_S\_M4M5.OB3_K3_DI := BS_S\_M4M5_3\_B10.value28; (# OB3_K3_DI \#)
  DAT_From_S\_M4M5.OB3_K4_DI := BS_S\_M4M5_3\_B10.value29; (# OB3_K4_DI \#)
  DAT_From_S\_M4M5.OB3_SEQ_Run := BS_S\_M4M5_3\_B10.value30; (# OB3_SEQ_RUN \#)
  
  Communicatie
  | **Signaal**               | **Bit op PLC zakscheur** | **DAT op plc zakscheur** | **DAT op plc rotoseal** | **DAT op plc rotoseal** | **DAT op plc Sibelco** | **DAT op plc Sibelco** | **Prog Molen_5 DAT_From_S\_M4M5** |
  |---------------------------|--------------------------|--------------------------|-------------------------|-------------------------|------------------------|------------------------|-----------------------------------|
  | MS22 -\> MS101            | OB3_K1_DI                | S_HB1.B1:VALUE4          | R_ZS1.B1:VALUE4         | S_SIB3.B1:VALUE6        | R_RS1.B1:VALUE6        | S_M4M5_3.B10:VALUE27   | OB3_K1_DI                         |
  | MS65 -\> MS101            | OB3_K3_DI                | S_HB1.B1:VALUE5          | R_ZS1.B1:VALUE5         | S_SIB3.B1:VALUE7        | R_RS1.B1:VALUE7        | S_M4M5_3.B10:VALUE28   | OB3_K3_DI                         |
  | MS65 -\> MS102            | OB3_K4_DI                | S_HB1.B1:VALUE6          | R_ZS1.B1:VALUE6         | S_SIB3.B1:VALUE8        | R_RS1.B1:VALUE8        | S_M4M5_3.B10:VALUE28   | OB3_K4_DI                         |
  | Sequentie overblazen M500 | PC1.2:RUN                | S_HB1.B1:VALUE7          | R_ZS1.B1:VALUE7         | S_SIB3.B1:VALUE9        | R_RS1.B1:VALUE9        | S_M4M5_3.B10:VALUE29   | OB3_SEQ_RUN                       |
  ------------
  **From:** Stijn Vandenbroucke \<<stijn.vandenbroucke@linkworx.eu>\>
  **Sent:** maandag 20 oktober 2014 9:29
  **To:** Tonny Lemmens
  **Cc:** Peter Drees
  **Subject:** SMFL
  
  **Follow Up Flag:** Follow up
  **Flag Status:** Flagged
  
  Tonny, teller van SMFL loopt nog niet? Kan je daar eens naar kijken?
  
  (-\> veroorzaakt backflush errors)
  
  Met vriendelijke groet,
  
  Stijn Vandenbroucke