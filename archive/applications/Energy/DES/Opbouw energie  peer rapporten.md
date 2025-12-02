---
tags: [energy, peer, reporting]
modified:  2025-08-30
date created: 2025-08-01T14:22:29+02:00
date modified: 2025-10-20T20:18:39+02:00
---

# [[2017-02-27]] 
  In het energie rapport van Microsoft wordt **om de 5 minuten gelogd**
  
  <https://app.powerbi.com/view?r=eyJrIjoiYjNkOWFkN2UtN2U2Yi00MjU0LWFjZjAtNzYzOTNmODY2MmRiIiwidCI6IjU3NGMzZTU2LTQ5MjQtNDAwNC1hZDFhLWQ4NDI3ZTdkYjI0MSIsImMiOjZ9>
  
  Ideale tabel:
  
  DTS, kWh stand
- # OPBOUW PEER
  Locatie Peer excel sheet
  
  [M:\Energy\Public](file:///M:/Energy/Public)
- # Velden Peer
  DTS, Kostenplaat, Item, uren, kWh, tonnen, gas
  
  1.  Job Linkworx_DES_Log_Update
  Deze scheduled job draait elke 5 minuten en bevat volgende stappen:
- Import MES (sp_Import_MES)
- Update Calculation (sp_UpdateCalculations2)
- Update Peer (sp_UpdatePeer)
  2.  sp_Import_MES
  De stored procedure sp_import_MES importeert data van MES en doet een merge met MES_PRD_Opr.
  
  Code
```SQL
  ;WITH lw as
  
  (
  
  -- Tabel van Linkworx MES
  -- W/C id, Dtsstart, item, qtyproduced, item_description
  
  SELECT prd_job.productionresourcerid as resid
  
  ,prd_job.dtsstart
  
  ,(select MAX(out_opt.dtsstop) from \[Linkworx\].\[dbo\].LNKWRX_PRD_OUTPUTOPERATION out_opt WITH(NOLOCK) where out_opt.productionjoboperationrid = prd_job.rid) as 'dtsstop'
  
  ,item.code as item
  
  ,prd_job.qtyproduced
  
  ,item.description as item_description
  
  FROM \[Linkworx\].\[dbo\].LNKWRX_PRD_JOBOPERATION prd_job WITH(NOLOCK)
  
  INNER JOIN \[Linkworx\].\[dbo\].LNKWRX_ITEM item WITH(NOLOCK) ON item.rid = prd_job.itemrid
  
  --WHERE prd_job.dtsstart \>= '2016/01/01'
  
  UNION ALL
  
  SELECT intrrpt.productionresourcerid
  
  ,intrrpt.dtsstart
  
  ,intrrpt.dtsstop
  
  ,rsn.code
  
  ,intrrpt.qtyproduced
  
  ,'No Item'
  
  FROM \[Linkworx\].\[dbo\].\[LNKWRX_PRD_DUR_INTERRUPT\] intrrpt WITH(NOLOCK)
  
  INNER JOIN \[Linkworx\].\[dbo\].LNKWRX_RSN_DUR_INTERRUPT rsn WITH(NOLOCK) ON rsn.rid = intrrpt.reasonrid
  
  WHERE rsn.code = 'NO ORDER' --and intrrpt.dtsstart \>= '2016/01/01'
  
  ),
  
  -- Linkworx Full
  
  lw_full as (
  
  SELECT res.code as res_code
  
  ,res.description as res_description
  
  ,LW.item as item
  
  ,LW.item_description as item_description
  
  ,LW.dtsstart as dtsstart
  
  ,LW.dtsstop as dtsstop
  
  ,Datediff(second, dtsstart,dtsstop)/3600.0 as runtime -- SQL2016 heeft een DATEDIFF_BIG functie voor meer nauwkeurigheid
  
  ,ISNULL(LW.qtyproduced,0) as qtyproduced
  
  ,IIF(Datediff(second, dtsstart,dtsstop) \<\> 0, ISNULL(LW.qtyproduced,0)/CONVERT(float, Datediff(second, dtsstart,dtsstop))\*3600.0, 0) AS troughput
  
  ,ROW_NUMBER() OVER (PARTITION BY res.code, LW.item, LW.dtsstart ORDER BY LW.dtsstart) as rn
  
  FROM LW
  
  INNER JOIN \[Linkworx\].\[dbo\].LNKWRX_PRD_PRODUCTIONRESOURCE res WITH(NOLOCK) ON res.rid = resid
  
  WHERE res.code is not null and LW.item is not null and LW.dtsstart is not null
  
  )
  
  MERGE MES_PRD_Opr AS TARGET
  
  USING (SELECT \* FROM lw_full where rn=1) AS SOURCE
  
  ON (TARGET.res_code = SOURCE.res_code AND TARGET.item = SOURCE.ITEM AND TARGET.dtsstart = SOURCE.dtsstart)
  
  WHEN NOT MATCHED THEN
  
  INSERT (res_code, res_description, item, item_description, dtsstart, dtsstop, runtime, qtyproduced, troughput)
  
  VALUES (SOURCE.res_code, SOURCE.res_description, SOURCE.item, SOURCE.item_description, SOURCE.dtsstart, SOURCE.dtsstop, SOURCE.runtime, SOURCE.qtyproduced, SOURCE.troughput)
  
  WHEN MATCHED THEN
  
  UPDATE
  
  SET target.res_code = source.res_code,
  
  target.res_description = source.res_description,
  
  target.item = source.item,
  
  target.item_description = source.item_description,
  
  target.dtsstart = source.dtsstart,
  
  target.dtsstop = source.dtsstop,
  
  target.runtime = source.runtime,
  
  target.qtyproduced = source.qtyproduced,
  
  target.troughput = source.troughput;
  
  END
```

  
  3.  \[MES_PRD_Opr\]
  Deze tabel wordt opgevuld door sp_Import_MES
  
  ![image1](image1-590.png)
  4.  sp_UpdateCalculations2
  De stored procedure sp_UpdateCalculations2 berekent / update de value_diff van \[datalog_energy\]
  5.  \[datalog_energy\]
  ![image2](image2-250.png)
  6.  sp_UpdatePeer
  De stored procedure sp_UpdatePeer berekent data op met de func_Peer en doet een merge met \[peer\]
  
  BeginDTS is 15 dagen tov van huidige datum/tijd.
  
  TijdInterval is 1 uur
  7.  Func_peer
  Func_peer is opgebouwd rond
- DateSequence: een tabel met vaste tijdintervallen
- MES_PRD_Opr
- \[peer\]