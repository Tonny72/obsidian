1. **Motoren**

|   |   |   |   |
|---|---|---|---|
|**TAG**|**Omschrijving**|**Vergrendelingen**||
|**M4_AF6_1**|Afzuigventilator|PT1 langer dan 10min \> -190||
|**M4_AF6_4**|Cellenrad|geen||
|**M4_AF6_5**|Filter Rotoseal|M4_AF6_4 moet draaien  <br>M4_AF6_5_F_DI = 0|FB1 valt na tijdje weg|
|**M4_AF6_6**|Vijs uitloop filter|geen||

3. **Kleppen**

|   |   |   |
|---|---|---|
|**TAG**|**Omschrijving**|**Vergrendelingen**|
||||
||||

5. **Digitale Ingangen**

|   |   |   |   |   |   |
|---|---|---|---|---|---|
|**TAG**  <br>**DI**|**Omschrijving**|**Aktieve waarde**|**FP / IND**|**Aansluiting**|**Onderdeel van Object**|
|**M4_AF6_1_CIN**|Hoofdcontactor in||FP|0.11.401.1||
|**M4_AF6_4_DI**|Cellenrad draait|||0.11.401.2|AF6_4|
|**M4_AF6_5_DI**|Filter Rotoseal in (DI niet gekoppeld. DI valt weg na een tijdje en FBConfig=6 werkt niet)|||0.11.401.3|AF6_5|
|**M4_AF6_5_F_DI**|Filter Rotoseal in storing|0||0.11.401.4|AF6_5|
|**M4_AF6_6_DI**|Vijs uitloop filter draait|||0.11.401.5|AF6_6|
|||||||
|**M4_1_CIN**|Hoofdcontactor in||FP|0.11.401.8||
|||||||
|**M4_AF6_I_DI**|Start filter AF6 vanaf Rotoseal||IND|0.11.402.14||
|**M4_BUN_UPS**|Alarm UPS||IND|0.11.402.15||
|**M4_BUN_BATT**|Mode niet ok||IND|0.11.402.16||

7. **Digitale Uitgangen**

|   |   |   |   |   |
|---|---|---|---|---|
|**TAG**|**Omschrijving**|**FP / IND**|**Aansluiting**|**Onderdeel van Object**|
|**M4_AF6_4**|Cellenrad afvoer rotoseal start||0.11.501.1|AF6_4|
|**M4_AF6_5**|Filter rotoseal start||0.11.501.2|AF6_5|
|**M4_AF6_6**|Vijs afvoer rotoseal start||0.11.501.3|AF6_6|
|**M4_AF6_I_DO**|Filter rotoseal draait melding naar rotoseal||0.11.501.4||
||||||

1. **Analoge Ingangen**

|   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**TAG**|**Omschrijving**|**FP/IN**|**Aansluiting**|**Onderdeel van Object**|**LLL**|**LL**|**L**|**H**|**HH**|**HHH**|**Range**|**Unit**|**Range channel**|
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||