---
date created: 2025-08-01
modified: 2025-08-29
---
created:: [[2018-11-22]]

-
- # Bibliotheken
- ## Opclabs
  <http://www.opclabs.com/products/quickopc/opc-specifications/unified-architecture?gclid=EAIaIQobChMIi8SDtuHn3gIVx-d3Ch06VQDLEAAYASAAEgL4ZfD_BwE>
  
  Prijslijst
  <http://www.opclabs.com/purchase/full-price-list>
- ## Advosol
  <http://www.advosol.com/category/3/client-components>
  Prijstlijst
  <http://www.advosol.com/product/45/opcda-net-ua>
-
- ## Unified Automation
  <http://documentation.unified-automation.com/uasdkdotnet/2.5.5/html/index.html>
  
  Prijslijst niet online beschikbaar.
- ## Git OPC Foundation
  <https://github.com/OPCFoundation/UA-.NETStandard>
-
- ## Tonny72/Sibelco/Ttool
  [[2018-11-22]] : Lib / TTool lib kan worden gecompileerd.
- # [[2018-11-22]] 
  Begonnen met Git OPC Foundation
  
  Aanpassing in UA-NetStandard - NetCoreConsoleClient - Opc.Ua.SampleClinet.Config.xml
  
  \<SecurityConfiguration\>
  
  ....
  
  \<!-- WARNING: The following setting (to automatically accept untrusted certificates) should be used
  
  for easy debugging purposes ONLY and turned off for production deployments! --\>
  
  \<AutoAcceptUntrustedCertificates\>true\</AutoAcceptUntrustedCertificates\>
  
  \<!-- WARNING: SHA1 signed certficates are by default rejected and should be phased out.--\>
  
  \<RejectSHA1SignedCertificates\>false\</RejectSHA1SignedCertificates\>
  
  \<MinimumCertificateKeySize\>1024\</MinimumCertificateKeySize\>