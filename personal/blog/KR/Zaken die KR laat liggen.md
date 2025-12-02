---
date created: 2018-09-18
modified: 2025-07-20
---
# Zaken die KR laat liggen
## Events AF10
Query:
```sql
With gr as (
SELECT Count(\*) as aantal_events, source, (Count(\*)\*100.0) / (SUM(Count(\*)) OVER()) AS \[percent\]
FROM \[Linkworx_DES_LOG\].\[dbo\].\[ABBOPCAE\]
group by source
),
bovenste as (
SELECT TOP 50 \* from gr
order by aantal_events desc
)
select \* from bovenste
union
SELECT SUM(aantal_events), 'ANDERE', SUM(\[percent\]) from gr
where source NOT in (select source from bovenste)
order by aantal_events desc
```
  geeft
  
| **source**    | **aantal_events** |
|---------------|-------------------|
| AF10BM101PT02 | 48968             |
| Andere        | 2501              |
| M3_H1         | 510               |
| AF6_MA        | 488               |
| AF6_KLBS      | 486               |
| AF6_SVA201    | 480               |
| C_SV11        | 426               |
| C_SV31        | 426               |
| C_LT71        | 425               |
| C3_ZS302_09   | 280               |
| AF10BM101OP2  | 264               |
| M4_VS_STT     | 236               |
| Klep          | 236               |
| M3_PT7        | 224               |
| M3_KL27       | 220               |

  ![image1](image1-7.png)
  87% van de events zijn voor rekening van AF10BM101PT02