---
title: M5_PT507 geeft veel events
updated: [[2022-01-20]]T09:12:20.0000000+01:00
created: [[2018-09-24]]T08:42:48.0000000+02:00
---

M5_PT507 geeft veel events
maandag 24 september 2018
8:42

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

- #
- # [[2018-09-24]] 
  Tijdens draaien veel L events.
- # [[2018-09-25]] 
  AEConfigH en AEConfigL op 4 gezet
- # [[2018-09-26]] 
  Dat was dus de oplossing
  Nu nog AF10BM101PT02