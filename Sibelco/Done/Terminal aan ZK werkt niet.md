---
created: [[2021-09-09]]T08:46:19.0000000+02:00
tags:
  - "#weegbrug"
  - loading_app
---

- # [[2021-09-09]] 
  IPv6 uitgeschakeld
  
  Slecht netwerk??
  
  [[2021-09-09]] 10:01:47.795 - Debug - TagCommunicator.QueueHandler (4) - linkworx.transaction.TransactionSession - commit - commit
  [[2021-09-09]] 10:01:47.795 - Error - TagCommunicator.QueueHandler (4) - sibelco.loadapplication.transaction.BunkerTransaction - notifyTagChangedEvent - pTimeStamp=\[[[2021-09-09]] 10:02:02\], tag=\[2244.stop\], category=\[BUNKER.STOP\], value=\[False\]
  [[2021-09-09]] 11:15:02.092 - Message - Method enter - opcUaSession_notifyConnectionLost
  [[2021-09-09]] 11:15:02.092 - Message - linkworx.io.opc.ua.client.OPCCommunicator.opcUaSession_notifyConnectionLost - pOPCUaSession=\[linkworx.io.opc.ua.client.util.OPCUaSession- name=\[opc.tcp://10.32.29.30:59151/linkworx/UAServer\];endpoint=\[opc.tcp://10.32.29.30:59151/linkworx/UAServer\]\]
  [[2021-09-09]] 11:15:02.092 - Verbose - 38 - sibelco.loadapplication.opc.OpcUaClientModule - notifyOPCConnectionLost - pSessionName=\[\]
  [[2021-09-09]] 11:15:02.092 - Message - linkworx.io.opc.ua.client.OPCCommunicator.opcUaSession_notifyConnectionLost - pOPCUaSession=\[linkworx.io.opc.ua.client.util.OPCUaSession- name=\[opc.tcp://10.32.29.30:59151/linkworx/UAServer\];endpoint=\[opc.tcp://10.32.29.30:59151/linkworx/UAServer\]\]
  [[2021-09-09]] 11:15:02.092 - Message - Method leave - opcUaSession_notifyConnectionLost
  [[2021-09-09]] 11:15:02.124 - Message - Method enter - startConnectionChecker
  [[2021-09-09]] 11:15:02.124 - Message - linkworx.io.opc.ua.client.util.OPCUaSession.startConnectionChecker
  [[2021-09-09]] 11:15:02.124 - Message - Thread enter - linkworx.io.opc.ua.client.util.OPCUaSession+OpcSessionMonitorPlugin
  [[2021-09-09]] 11:15:02.124 - Verbose - linkworx.io.opc.ua.client.util.OPCUaSession+OpcSessionMonitorPlugin (7) - linkworx.util.remote.ConnectionMonitor - checkConnection - linkworx.io.opc.ua.client.util.OPCUaSession+OpcSessionMonitorPlugin
  [[2021-09-09]] 11:15:02.124 - Message - linkworx.io.opc.ua.client.util.OPCUaSession.startConnectionChecker
  [[2021-09-09]] 11:15:02.124 - Message - Method leave - startConnectionChecker
  [[2021-09-09]] 11:15:03.014 - Warning - linkworx.io.opc.ua.client.util.OPCUaSession+OpcSessionMonitorPlugin (7) - linkworx.io.opc.ua.client.util.OPCUaSession+OpcSessionMonitorPlugin - checkConnection- Could not recreate session. opc.tcp://10.32.29.30:59151/linkworx/UAServer:
  at Opc.Ua.Client.Session.Recreate(Session template)
  at linkworx.io.opc.ua.client.util.OPCUaSession.OpcSessionMonitorPlugin.checkConnection()
  [[2021-09-09]] 11:15:08.015 - Verbose - linkworx.io.opc.ua.client.util.OPCUaSession+OpcSessionMonitorPlugin (7) - linkworx.util.remote.ConnectionMonitor - checkConnection - linkworx.io.opc.ua.client.util.OPCUaSession+OpcSessionMonitorPlugin
  [[2021-09-09]] 11:15:10.749 - Error - TagCommunicator.QueueHandler (4) - linkworx.util.queue.QueueHandler - handleQueue - A transport-level error has occurred when receiving results from the server. (provider: TCP Provider, error: 0 - The semaphore timeout period has expired.):
  at System.Data.SqlClient.SqlConnection.OnError(SqlException exception, Boolean breakConnection, Action\`1 wrapCloseInAction)
  at System.Data.SqlClient.SqlInternalConnection.OnError(SqlException exception, Boolean breakConnection, Action\`1 wrapCloseInAction)
  en ook
  
  [[2021-09-09]] 11:15:34.891 - Error - TagCommunicator.QueueHandler (4) - linkworx.util.queue.QueueHandler - handleQueue - A network-related or instance-specific error occurred while establishing a connection to SQL Server. The server was not found or was not accessible.Verify that the instance name is correct and that SQL Server is configured to allow remote connections. (provider: Named Pipes Provider, error: 40 - Could not open a connection to SQL Server):
  at System.Data.ProviderBase.DbConnectionPool.TryGetConnection(DbConnection owningObject, UInt32 waitForMultipleObjectsTimeout, Boolean allowCreate, Boolean onlyOneCheckConnection, DbConnectionOptions userOptions, DbConnectionInternal& connection)
  at System.Data.ProviderBase.DbConnectionPool.TryGetConnection(DbConnection owningObject, TaskCompletionSource\`1 retry, DbConnectionOptions userOptions, DbConnectionInternal& connection)
  at System.Data.ProviderBase.DbConnectionFactory.TryGetConnection(DbConnection owningConnection, TaskCompletionSource\`1 retry, DbConnectionOptions userOptions, DbConnectionInternal oldConnection, DbConnectionInternal& connection)
  at System.Data.ProviderBase.DbConnectionInternal.TryOpenConnectionInternal(DbConnection outerConnection, DbConnectionFactory connectionFactory, TaskCompletionSource\`1 retry, DbConnectionOptions userOptions)
  at System.Data.ProviderBase.DbConnectionClosed.TryOpenConnection(DbConnection outerConnection, DbConnectionFactory connectionFactory, TaskCompletionSource\`1 retry, DbConnectionOptions userOptions)
  at System.Data.SqlClient.SqlConnection.TryOpenInner(TaskCompletionSource\`1 retry)
  at System.Data.SqlClient.SqlConnection.TryOpen(TaskCompletionSource\`1 retry)
  at System.Data.SqlClient.SqlConnection.Open()
  at linkworx.transaction.TransactionSession.start(DbConnection pDbConnection)
  at linkworx.transaction.TransactionSession.save(DbConnection pDbConnection, Boolean pForce, Boolean pCommit)
  at linkworx.transaction.TransactionSession.save(Boolean pForce)
  at linkworx.bo.AbstractLinkworxClass.save(String pTable)
  at linkworx.bo.AbstractLinkworxClass.save()
  at sibelco.loadapplication.opc.OpcUaClientModule.onTagChanged(Tag pTag, String pTagCode, Object pTagValue, Object pScaledValue, Int64 pTagQuality, DateTime pDateTime)
  at linkworx.io.TagCommunicator.queueObjectRemoved(Object pObject, Object pRefObject)
  at linkworx.util.queue.QueueHandler.handleQueue()
  
  Mail Naar jef om de switch poort te controleren
  
  ![image1](image1-101.png)
  
  Antwoord van Jef
  
  Hieronder een screenshot van de statistieken van de switch port:
  
  ![image2](image2-9.jpg)
  
  Ziet er in eerste instantie goed uit volgens mij.
- # [[2021-09-13]] 
  laden via badge werkt.
  Maar screen moet worden gecallibreerd
  Na installatie van de drivers wordt scherm gecallibreerd
  D:\Sibelco\Elektrische Dienst en Automatisering - Documents\Automatisering\Leveranciers\iEi\Drivers
  Voorlopig alles OK
  
  User: USRWBTG0
  pw: Sibelco2019
  Er is ook een USRWBTG0_Admin (pw: Sibelco2019)
  
  [[BE-DES-TDC-017 1]]
- # [[2021-09-20]] 15:57 
  Log zag er normaal uit, maar pc moeten herstarten
  
  DES - Weegbrug: Log van Linkworx [[BE-DES-TDC-017 1]] controleren
-