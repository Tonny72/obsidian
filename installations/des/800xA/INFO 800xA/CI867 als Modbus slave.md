---
title: CI867 als Modbus slave
updated: [[2020-09-17]]T12:51:00.0000000+02:00
created: [[2018-04-12]]T11:52:33.0000000+02:00
---

Hello,
Yes we can make CI867 as modbus tcp slave by using access variables.
please refer the attached snap for your ref.
![image1](image1-14.gif)
[CI867 Acting as Modb.pptx](http://www402.abbext.com/DownloadFile.aspx?file=UserFiles/Answers201411/CI867%20Acting%20as%20Modb.pptx&filename=CI867%20Acting%20as%20Modb.pptx)

*From \<<http://www402.abbext.com/CI867-AC800M-Modbus-TCP-IP-Configured-Slave-q892800.aspx>\>*
[CI867 Acting as Modb.pptx](assets/resources/CI867_Acting_as_Modb.pptx)![image2](image2-101.png)
![image3](image3-57.png)

- # modbus testjes gebruik modpoll
  
  ABB %MW2000 (int) geeft in modpoll adres 2001 de waarde terug
  ABB %MW2001 (int) geeft in modpoll adres 2002 de waarde terug
  enz
  abb %Wadres = Modbus adres+1