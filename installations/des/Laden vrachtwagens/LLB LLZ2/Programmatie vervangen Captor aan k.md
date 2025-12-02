---
title: Programmatie vervangen Captor aan kanaal
updated: [[2012-05-29]]T12:48:48.0000000+02:00
created: [[2012-03-06]]T10:12:00.0000000+01:00
---

| **Bunker** | **Groep** | **** | **** | **PLC**         | **Start**              | **Stop** | **Noodwerking** |
|------------|-----------|-------|-------|-----------------|------------------------|----------|-----------------|
| **BU01**   | MK1       | BB    |      | LLB pc1.1.4     | Zie laadplaats B01-B08 |         |                |
| **BU02**   | MK1       | BB    |      | LLB pc1.1.4     | Zie laadplaats B01-B08 |         |                |
| **BU03**   | MK1       | BB    |      | LLB pc1.1.4     | Zie laadplaats B01-B08 |         |                |
| **BU04**   | MK1       | BB    |      | LLB pc1.1.4     | Zie laadplaats B01-B08 |         |                |
| **BU05**   | MK1       | BB    |      | LLB pc1.1.4     | Zie laadplaats B01-B08 |         |                |
| **BU06**   | MK1       | BB    |      | LLB pc1.1.4     | Zie laadplaats B01-B08 |         |                |
| **BU07**   | MK1       | BB    |      | LLB pc1.1.4     | Zie laadplaats B01-B08 |         |                |
| **BU08**   | MK1       | BB    |      | LLB pc1.1.4     | Zie laadplaats B01-B08 |         |                |
| **BU09**   | MK2       | BB    |      | LLB pc1.1.5     | Zie laadplaats B09-B12 |         |                |
| **BU10**   | MK2       | BB    |      | LLB pc1.1.5     | Zie laadplaats B09-B12 |         |                |
| **BU11**   | MK2       | BB    |      | LLB pc1.1.5     | Zie laadplaats B09-B12 |         |                |
| **BU12**   | MK2       | BB    |      | LLB pc1.1.5     | Zie laadplaats B09-B12 |         |                |
| **BU23**   | MK3       | BB    |      | LLB pc1.1.3     |                       |         |                |
| **BU24**   | MK3       | BB    |      | LLB pc1.1.3     |                       |         |                |
| **BU25**   | MK3       | BB    |      | LLB pc1.1.3     |                       |         |                |
| **BU26**   | MK3       | BB    |      | LLB pc1.1.3     |                       |         |                |
| **BU27**   | MK3       | BB    |      | LLB pc1.1.2     |                       |         |                |
| **BU28**   | MK3       | BB    |      | LLB pc1.1.2     |                       |         |                |
| **BU60**   | MK4       | EB    |      | LLB5 pc1.3.1.13 |                       |         |                |
| **BU60b**  | MK4       | EB    |      |                |                       |         |                |
| **BU61**   | MK4       | EB    |      | LLB5 pc1.3.1.13 |                       |         |                |
| **BU61b**  | MK4       | EB    |      |                |                       |         |                |
| **BU62**   | MK4       | EB    |      | LLB5 pc1.3.1.13 |                       |         |                |
| **BU63**   | MK4       | EB    |      | LLB5 pc1.3.1.13 |                       |         |                |
| **BU63b**  | MK4       | EB    |      |                |                       |         |                |
| **BU64**   | MK4       | EB    |      | LLB5 pc1.3.1.15 |                       |         |                |
| **BU65**   | MK4       | EB    |      | LLB5 pc1.3.1.15 |                       |         |                |
| **BU66**   | MK4       | EB    |      | LLB5 pc1.3.1.15 |                       |         |                |
| **BU67**   | MK4       | EB    |      | LLB5 pc1.3.1.15 |                       |         |                |
| **BU68**   | MK4       | EB    |      | LLB5 pc1.3.1.15 |                       |         |                |
| **BU69**   | MK4       | EB    |      | LLB5 pc1.3.1.16 |                       |         |                |
| ****      |          |      |      |                |                       |         |                |
| **BU85**   | MK4       | EB    |      | LLB5 pc1.3.1.16 |                       |         |                |
| **BU86**   | MK4       | EB    |      | LLB5 pc1.3.1.16 |                       |         |                |

Laadplaats signalen
| **Laadplaats** | **Start Drukknop**        | **Stop Drukknop**        | **Noodwerking**        | **Sequentie Nr.** | **** |
|----------------|---------------------------|--------------------------|------------------------|-------------------|-------|
| **B01-B08**    | LLB3_STT1_DI (DI800_3.11) | LLB3_STP_DI (DI800_3.13) | LLB3_H\_DI (DI800_3.3) |                  |      |
| **B09-B12**    | LLB4_STT1_DI (DI800_3.14) | LLB_STP_DI (DI800_3.16)  | LLB4_H\_DI (DI800_3.4) |                  |      |
| **B23-B28**    | LLB2_STT1_DI (DI800_3.8)  | LLB2_STP_DI (DI800_3.10) | LLB2_H\_DI (DI800_3.2) |                  |      |
| B21            |                          |                         |                       |                  |      |

- ## Oude weegb