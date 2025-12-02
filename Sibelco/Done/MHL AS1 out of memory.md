---
title: MHL AS1 out of memory
updated: [[2022-01-21]]T13:53:02.0000000+01:00
created: [[2018-09-25]]T10:20:17.0000000+02:00
modified:  2025-07-21
---
# MHL AS1 out of memory

Stijn,

Volgens log lijkt alles normaal te werken, tot ik de service herstart.

[[2018-09-25]] 09:21:56.470 - Message - linkworx.io.TagModule.onTagChanged - pTag=\[PPM02_Counter_production: opcda://ABB.AfwOpcDaSurrogate.1 - DR - Applications.S200.Communication_MES:MES_GQ317_Counter\];pTagCode=\[PPM02_Counter_production\];pTagValue=\[947274.1\]
[[2018-09-25]] 09:21:56.845 - Verbose - 181 - linkworx.io.program.server.CommunicationServer - applicationExit -
[[2018-09-25]] 09:21:56.845 - Message - Method enter - shutdown
[[2018-09-25]] 09:21:56.845 - Message - linkworx.modules.mail.MailModule.shutdown
[[2018-09-25]] 09:21:56.845 - Message - Method enter - stop
[[2018-09-25]] 09:21:56.845 - Message - linkworx.modules.mail.MailModule.stop
[[2018-09-25]] 09:21:56.845 - Message - linkworx.modules.mail.MailModule.stop
[[2018-09-25]] 09:21:56.845 - Message - Method leave - stop
[[2018-09-25]] 09:21:56.845 - Message - linkworx.modules.mail.MailModule.shutdown
[[2018-09-25]] 09:21:56.845 - Message - Method leave - shutdown
[[2018-09-25]] 09:21:56.845 - Message - Method enter - stop
[[2018-09-25]] 09:21:56.845 - Message - linkworx.io.TagModule.stop
[[2018-09-25]] 09:21:56.860 - Message - Thread leave - TagCommunicator.QueueHandler
[[2018-09-25]] 09:21:56.860 - Message - Thread leave - TagCommunicator.QueueHandler
[[2018-09-25]] 09:21:56.860 - Message - Method enter - stop
[[2018-09-25]] 09:21:56.860 - Message - linkworx.io.TagModule.stop
[[2018-09-25]] 09:21:56.860 - Message - linkworx.io.TagModule.stop
[[2018-09-25]] 09:21:56.860 - Message - Method leave - stop
[[2018-09-25]] 09:21:56.860 - Message - linkworx.io.TagModule.stop
[[2018-09-25]] 09:21:56.860 - Message - Method leave - stop
[[2018-09-25]] 09:21:56.891 - Debug - 181 - linkworx.io.opc.da.net.OPCCommunicator - shutdown -
[[2018-09-25]] 09:21:57.910 - Debug - 181 - linkworx.io.opc.da.net.OPCCommunicator - shutdown -

Ik krijg wel deze fout
![image1](image1-6%201.jpg)

Maar na herstart van de DA-MES komt wel als terug goed.

Dit staat in de event viewer 24-Sep-2018 06:19:23
Faulting application name: linkworx.server.exe, version: 1.0.0.0, time stamp: 0x54d34827

Faulting module name: KERNELBASE.dll, version: 6.3.9600.17415, time stamp: 0x54504ade

Exception code: 0xe0434352

Fault offset: 0x00014598

Faulting process id: 0x57ec

Faulting application start time: 0x01d424ef19a0fdd7

Faulting application path: C:\linkworx\sites\MHL\server_DA_MES\linkworx.server.exe

Faulting module path: C:\Windows\SYSTEM32\KERNELBASE.dll

Report Id: 03c27331-bfb1-11e8-80cd-005056ac243f

Faulting package full name:

Faulting package-relative application ID:

Application: linkworx.server.exe
Framework Version: v4.0.30319
Description: The process was terminated due to an unhandled exception.
Exception Info: System.OutOfMemoryException
Stack:
 at System.Text.StringBuilder.ExpandByABlock(Int32)
 at System.Text.StringBuilder.Append(Char\*, Int32)
 at System.Text.StringBuilder.AppendHelper(System.String)
 at System.Text.StringBuilder.Append(System.String)
 at System.Diagnostics.StackTrace.ToString(TraceFormat)
 at System.Environment.GetStackTrace(System.Exception, Boolean)
 at System.Exception.GetStackTrace(Boolean)
 at System.Exception.get_StackTrace()
 at Opc.Ua.ServiceResult.BuildExceptionTrace(System.Exception)
 at Opc.Ua.ServiceResult..ctor(System.Exception, UInt32, System.String, System.String, Opc.Ua.LocalizedText)
 at Opc.Ua.ServiceResult..ctor(Opc.Ua.StatusCode, System.String, System.String, Opc.Ua.LocalizedText, System.String, System.Exception)
 at Opc.Ua.ServiceResult.Create(System.Exception, UInt32, System.String, System.Object\[\])
 at Opc.Ua.Bindings.TcpMessageSocket.OnReadComplete(System.IAsyncResult)
 at System.Net.LazyAsyncResult.Complete(IntPtr)
 at System.Net.ContextAwareResult.CompleteCallback(System.Object)
 at System.Threading.ExecutionContext.RunInternal(System.Threading.ExecutionContext, System.Threading.ContextCallback, System.Object, Boolean)
 at System.Threading.ExecutionContext.Run(System.Threading.ExecutionContext, System.Threading.ContextCallback, System.Object, Boolean)
 at System.Threading.ExecutionContext.Run(System.Threading.ExecutionContext, System.Threading.ContextCallback, System.Object)
 at System.Net.ContextAwareResult.Complete(IntPtr)
 at System.Net.LazyAsyncResult.ProtectedInvokeCallback(System.Object, IntPtr)
 at System.Net.Sockets.BaseOverlappedAsyncResult.CompletionPortCallback(UInt32, UInt32, System.Threading.NativeOverlapped\*)
 at System.Threading.\_IOCompletionCallback.PerformIOCompletionCallback(UInt32, UInt32, System.Threading.NativeOverlapped\*)

Er zit 8GB in de server en er is 4GB in gebruik. Dus niet echt problematisch.

Als er morgen nog een probleem is, herstart ik de server.

- # [[2018-09-25]] 10:30u
  ![image2](image2-31%201.png)
- # [[2018-09-25]] 15:49u
  ![image3](image3-20%201.png)
- # [[2018-09-26]] 
  ![image4](image4-13%201.png)
- # [[2018-09-27]] 
  ![image5](image5-10%201.png)
- #
- # [[2018-09-28]] 
  ![image6](image6-9%201.png)
- # [[2018-11-14]] 
  (12/11 22.00u)
  ![image7](image7-6%201.png)
  
  (13/11 14.10u)
  ![image8](image8-4%201.png)
  
  (14/11 9.55u)
  ![image9](image9-4%201.png)
- # [[2018-11-16]] 
  ![image10](image10-3%201.png)
- # [[2018-11-21]] 
  ![image11](image11-2%201.png)
- #
- # [[2018-12-20]] 
  ![image12](image12-1%201.png)
- # [[2019-01-14]] 
  Kepware server geïnstalleerd en geconfigureerd voor ombouw Linkworx naar Kepware
  ![image13](image13-1%201.png)
  
  KEPWARE in dienst genomen