---
title: LOG ALG SQL
date created: 2017-01-03
---

- # [[2017-01-03]] 15:01 
  Veel geprulled met SQL server.
  
  De db Linkworx_DES_Log is veel te groot geworden.
  Geprobeerd te werken met partitioning maar dit wordt enkel door de Enterprise versie ondersteund.
  Dan maar een extra table aangemaakt om de data van de calcineeroven er heen te sluizen. Maar hierdoor werd de transaction log zo groot dat de database crashte. De E:\\ schijf was vol gelopen.
  
  Op dit moment is een recovery aan de gang.
  
  In de Log van SQL Server kan je zien hoe lang het duurt. =\> 4297 seconden
- # [[2017-01-06]] 15:10 
  Het is veeel moeilijker dan gedacht om te werken met grote hoeveelheden data.
  Het opbouwen van indexen gaat veel trager
  Het opvragen van data is soms ook traag
  
  =\> Noodzaak om de tabel datalog te partitioneren
- ## Partitioneren per doelgroep
  Dit gebeurt adv de datalog in tags
  1.  Tabel: Datalog_CAL  
    Calcineeroven voor Mckinesey. Datalog=1
  2.  Tabel: Datalog_D3  
    Enerprof logging. Datalog=2
  3.  Tabel: Datalog_Perslucht  
    Voor Tom Noels. Datalog = 4
  4.  Tabel: Datalog_Energy  
    Voor kWh berekening. datalog = 3