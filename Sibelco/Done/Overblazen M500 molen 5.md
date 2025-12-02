created:: [[2020-05-14]]
tags:: M5

- | **Subject**     | **Overblazen M500 molen 5**                     |
  |-----------------|-------------------------------------------------|
  | **From**        | Tom Noels                                       |
  | **To**          | Tonny Lemmens; Stef Valkiers; Geert Staes       |
  | **Cc**          | Harry Stienen                                   |
  | **Sent**        | donderdag 14 mei 2020 13:41                     |
  | **Attachments** | [flowsheet molen 5 (overblazen M500).pdf](flowsheet_molen_5_(overblazen_M500).pdf) |
  **<u>Overblazen M500 Molen 5: Sequentie</u>**
- Start Blower M5_60
- Open klep M5SVA411
- Wacht x seconden (instelbare tijd) 5sec
- Sluit klep M5SVA411
- Open regelklep M5SVA413 tot 50 % (instelbaar)
	- Als druk (M5PT507) in persleiding \> H limiet 0.50 bar (instelbaar) à sluit regelklep M5SVA413
	- Als druk (M5PT507) in persleiding \< L limiet 0.25 bar (instelbaar) à open regelklep M5SVA413 50 %
- Open klep M5SVA412
	- Als druk (M5PT507) = druk (M5PT412) en lager dan L limiet à buis is leeg.
- Sluit klep M5SVA412 en regelklep M5SVA413
- Hervat sequentie bij ‘Open klep M5SVA411’