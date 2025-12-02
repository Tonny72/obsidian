---
title: SQL voor dashboard
updated: [[2017-01-20]]T15:31:18.0000000+01:00
created:  0000-01-01
modified:  2025-08-29
---

Peter, kan jij Geert werk laten maken van de ABB stuurparameters per item \[= welke in dashboard?
\].
Onderstaande geeft al de Unilab data terug.

Tonny, ik het wat sql voorbereid voor dashboard:

DECLARE @paramList VARCHAR(MAX)
SET @paramList = STUFF((
 SELECT DISTINCT ',\[' + tmp.parametercode + '\]'
 FROM view_dashboard_item_parameters tmp INNER JOIN sys.columns sys_col ON sys_col.object_id = OBJECT_ID('dbo.SIBELCO_LABO_STEERING_SAMPLE') and sys_col.name = tmp.parametercode
 WHERE tmp.prd_item_rid = 760377
 FOR XML PATH('')
 )
 ,1,1,'')

DECLARE @query NVARCHAR(MAX)
SET @query = 'SELECT pvt.dtsvalidfrom,
 res.code as workcenter_code,
 item.code as item_code,
 item.description as item_description,
 loc.code as location,
 pvt.code as sample_code,
 parameter,
 (select tmp.minvalue from view_dashboard_item_parameters tmp where tmp.prd_item_rid = pvt.itemrid and tmp.parametercode = pvt.parameter) as minvalue,
 parametervalue,
 (select tmp.maxvalue from view_dashboard_item_parameters tmp where tmp.prd_item_rid = pvt.itemrid and tmp.parametercode = pvt.parameter) as maxvalue
  FROM SIBELCO_LABO_STEERING_SAMPLE
  unpivot
  (
 parametervalue
 for parameter IN (' + @paramList + ')
  ) pvt INNER JOIN LNKWRX_PRD_PRODUCTIONRESOURCE res ON res.rid = pvt.productionresourcerid
  INNER JOIN LNKWRX_ITEM item ON item.rid = pvt.itemrid
 INNER JOIN LNKWRX_PRD_OUTPUTOPERATION out_op ON out_op.rid = pvt.outputoperationrid
 INNER JOIN LNKWRX_WAREHOUSELOCATION loc ON loc.rid = out_op.tolocationrid
  ORDER BY dtsvalidfrom desc'

EXEC sp_executesql @query

![image1](image1-2%201.jpg)

Met vriendelijke groet,
Stijn Vandenbroucke
Mobiel: +32 (0)478 92 96 92

![image2](image2-1%201.jpg)
**Linkworx BVBA**
Brouwerijstraat 78
9880 Aalter
Tel: +32 (0)9 277 93 10
Fax: +32 (0)9 277 93 11
Mail:<stijn.vandenbroucke@linkworx.eu>
Web: [www.linkworx.eu](https://emea01.safelinks.protection.outlook.com/?url=http%3A%2F%2Fwww.linkworx.eu%2F&data=01%7C01%7CTonny.Lemmens%40sibelco.com%7Cd3065d78f148487d8f9a08d3e7e0536a%7Ca0cac58c12b94f1fb95d2405875a18d6%7C1&sdata=UIkI%2BoBie8fzEB34AGxHRh%2BRxbAPZZLXbtN3TDCWGgA%3D&reserved=0)
