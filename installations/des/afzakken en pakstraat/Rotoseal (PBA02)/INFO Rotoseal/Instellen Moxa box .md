---
created: [[2019-07-02]]T10:50:30.0000000+02:00
---

Poort 2 van de Moxa is nu als volgt ingesteld:

- Operation mode: TCP Server Mode (ipv Real COM Mode)
- Local TCP port heb ik de default behouden: 4002
  
  ![image1](image1-29.jpg)
  
  Voor MES is config aanpassing als volgt:
  
  ![image2](image2-17.jpg)
  
  Extra setting:
- Seriële parameters dienen ook correct ingesteld te worden bij gebruik van TCP Server
- Dit verschil bij gebruik van virtuele com =\> daar is het de client seriële instelling die baudrate ed bepaald
  
  ![image3](image3-8.jpg)