---
date created: 2020-01-24
modified: 2025-08-30
---
Op de server zelf kunnen queries uitgevoerd worden.
 
Deze uitgezocht met Profiler (type windows-toets Profiler)
   

```
SELECT [t1].[ID], [t1].[PolicyID], [t1].[EventType], [t1].[EventID], [t1].[Timestamp], [t1].[ResultType], [t1].[ResultID], [t1].[TriggerStatus], [t1].[Options], [t0].[ID] AS [ID2], [t0].[Active], [t0].[Name], [t0].[Description], [t0].[Groupname], [t0].[EventProviderID], [t0].[Destination], [t0].[DestinationType], [t0].[ServiceTo], [t0].[Type], [t0].[Condition], [t0].[Transform], [t0].[Flags], [t0].[OwnerID], [t0].[AccessControlItemID], [t0].[ActionID], [t0].[Options] AS [Options2], [t0].[DestinationID], [t0].[CalloutID], [t0].[ServiceID], [t0].[EventTypeID]  
FROM [dbo].[Policies] AS [t0]  
INNER JOIN [dbo].[PolicyExecutionJournal] AS [t1] ON [t0].[ID] = [t1].[PolicyID]  
ORDER BY Timestamp






SELECT [t1].[ID], [t1].[MSGINDEX], [t1].[MSGDATA], [t1].[MSGTIMESTAMP], [t1].[SERVICEFROM], [t1].[SERVICETO], [t1].[ORIGINATOR], [t1].[DESTINATION], [t1].[MSGTEXT], [t1].[MSGSUBJECT], [t1].[MSGOPTIONS], [t1].[SESSIONID], [t1].[STRINGREF], [t1].[USERNAME], [t1].[BILLCODE], [t1].[ATTACHMENTS], [t1].[SERVERID], [t1].[READFLAG], [t1].[MSGCATEGORY], [t1].[MEDIATYPE], [t1].[OPTIONS], [t1].[REFERENCEID], [t1].[TRIGGEREDRULE], [t1].[USERTYPE], [t1].[USERID], [t1].[MODULESERVICEID]  
FROM (  
    SELECT ROW_NUMBER() OVER (ORDER BY [t0].[ID] DESC, [t0].[ID] DESC) AS [ROW_NUMBER], [t0].[ID], [t0].[MSGINDEX], [t0].[MSGDATA], [t0].[MSGTIMESTAMP], [t0].[SERVICEFROM], [t0].[SERVICETO], [t0].[ORIGINATOR], [t0].[DESTINATION], [t0].[MSGTEXT], [t0].[MSGSUBJECT], [t0].[MSGOPTIONS], [t0].[SESSIONID], [t0].[STRINGREF], [t0].[USERNAME], [t0].[BILLCODE], [t0].[ATTACHMENTS], [t0].[SERVERID], [t0].[READFLAG], [t0].[MSGCATEGORY], [t0].[MEDIATYPE], [t0].[OPTIONS], [t0].[REFERENCEID], [t0].[TRIGGEREDRULE], [t0].[USERTYPE], [t0].[USERID], [t0].[MODULESERVICEID]  
    FROM [dbo].[MMINBOUND] AS [t0]  
    ) AS [t1]  
order by MSGTIMESTAMP






SELECT DISTINCT([t1].[ORIGINATOR])  
FROM (  
    SELECT ROW_NUMBER() OVER (ORDER BY [t0].[ID] DESC, [t0].[ID] DESC) AS [ROW_NUMBER], [t0].[ID], [t0].[MSGINDEX], [t0].[MSGDATA], [t0].[MSGTIMESTAMP], [t0].[SERVICEFROM], [t0].[SERVICETO], [t0].[ORIGINATOR], [t0].[DESTINATION], [t0].[MSGTEXT], [t0].[MSGSUBJECT], [t0].[MSGOPTIONS], [t0].[SESSIONID], [t0].[STRINGREF], [t0].[USERNAME], [t0].[BILLCODE], [t0].[ATTACHMENTS], [t0].[SERVERID], [t0].[READFLAG], [t0].[MSGCATEGORY], [t0].[MEDIATYPE], [t0].[OPTIONS], [t0].[REFERENCEID], [t0].[TRIGGEREDRULE], [t0].[USERTYPE], [t0].[USERID], [t0].[MODULESERVICEID]  
    FROM [dbo].[MMINBOUND] AS [t0]  
    ) AS [t1]





```
    
SELECT [t1].[ID], [t1].[MSGINDEX], [t1].[MSGDATA], [t1].[MSGTIMESTAMP], [t1].[SERVICEFROM], [t1].[SERVICETO], [t1].[ORIGINATOR], [t1].[DESTINATION], [t1].[MSGTEXT], [t1].[MSGSUBJECT], [t1].[MSGOPTIONS], [t1].[SESSIONID], [t1].[STRINGREF], [t1].[USERNAME], [t1].[BILLCODE], [t1].[ATTACHMENTS], [t1].[SERVERID], [t1].[READFLAG], [t1].[MSGCATEGORY], [t1].[MEDIATYPE], [t1].[OPTIONS], [t1].[REFERENCEID], [t1].[TRIGGEREDRULE], [t1].[USERTYPE], [t1].[USERID], [t1].[MODULESERVICEID]  
FROM (  
SELECT ROW_NUMBER() OVER (ORDER BY [t0].[ID] DESC, [t0].[ID] DESC) AS [ROW_NUMBER], [t0].[ID], [t0].[MSGINDEX], [t0].[MSGDATA], [t0].[MSGTIMESTAMP], [t0].[SERVICEFROM], [t0].[SERVICETO], [t0].[ORIGINATOR], [t0].[DESTINATION], [t0].[MSGTEXT], [t0].[MSGSUBJECT], [t0].[MSGOPTIONS], [t0].[SESSIONID], [t0].[STRINGREF], [t0].[USERNAME], [t0].[BILLCODE], [t0].[ATTACHMENTS], [t0].[SERVERID], [t0].[READFLAG], [t0].[MSGCATEGORY], [t0].[MEDIATYPE], [t0].[OPTIONS], [t0].[REFERENCEID], [t0].[TRIGGEREDRULE], [t0].[USERTYPE], [t0].[USERID], [t0].[MODULESERVICEID]  
FROM [dbo].[MMINBOUND] AS [t0]  
) AS [t1]  
order by MSGTIMESTAMP
 
# Toon de unieke telefoonnrs die in de message-log zitten

SELECT DISTINCT([t1].[ORIGINATOR])  
FROM (  
SELECT ROW_NUMBER() OVER (ORDER BY [t0].[ID] DESC, [t0].[ID] DESC) AS [ROW_NUMBER], [t0].[ID], [t0].[MSGINDEX], [t0].[MSGDATA], [t0].[MSGTIMESTAMP], [t0].[SERVICEFROM], [t0].[SERVICETO], [t0].[ORIGINATOR], [t0].[DESTINATION], [t0].[MSGTEXT], [t0].[MSGSUBJECT], [t0].[MSGOPTIONS], [t0].[SESSIONID], [t0].[STRINGREF], [t0].[USERNAME], [t0].[BILLCODE], [t0].[ATTACHMENTS], [t0].[SERVERID], [t0].[READFLAG], [t0].[MSGCATEGORY], [t0].[MEDIATYPE], [t0].[OPTIONS], [t0].[REFERENCEID], [t0].[TRIGGEREDRULE], [t0].[USERTYPE], [t0].[USERID], [t0].[MODULESERVICEID]  
FROM [dbo].[MMINBOUND] AS [t0]  
) AS [t1]