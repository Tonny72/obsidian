---
date created: 2025-08-20T08:01:29+02:00
date modified: 2025-10-19T22:46:41+02:00
tags: [Obsidian]
---
 TEST mermaid
>*On sequentie*

>**Start bij INIT**

Stopt bij ***Productiestap***

<!--
https://mermaid.js.org/syntax/flowchart.html#minimum-length-of-a-link
https://fontawesome.com/

-->

```mermaid
flowchart TD

%% bepaal classes
    classDef init fill: #2daeef, stroke: #000000, color: #ffffff
    classDef tr fill: #ffffff, stroke: #000000, color: #000000 
    classDef step fill: #2daeef, stroke: #000000, color: #ffffff

%% stappen
    INIT([INIT fa:fa-camera-retro]):::init
    TrOnSeq[[OnSeq: OnSeq]]:::tr
    S1(S1: Start pomp 1
    P1_Out1):::step
    Tr1[/Tr1: Pomp 1 gestart
    P1_FB1/]:::tr
    S2>S2: Open klep 1
    KL1_Out1]:::step
    Tr2{{Tr2: Klep 2 geopend
    KL1_FB1 fa:fa-download}}:::tr
    S100[(S100: Productiestap fa:fa-spinner)]:::step

%% stapvolgorde
    INIT --OnSeq--> TrOnSeq --o |test| S1 --> Tr1 --x S2 -.-> Tr2 ==> S100 --> INIT
    
```

<!--
https://www.htmlsymbols.xyz/
-->


```mermaid
%%{init: {"theme":"forest"}}%%
pie

"part 1": 25
"part 2": 48
"part 3": 27
```

```mermaid

%%{init: {"theme":"base"}}%%
packet-beta

0-15: "Higher word fa:fa-twitter"
16-31: "Lower word"
32-63: "All"
64: "b0"
65: "b1"
66: "b2"
67: "b3"
68: "b4"
69: "b5"
70: "b6"
71: "b7"
72-79: "byte 0 #127783;"
80-95: "word 0 #9829;"
```

![test](Test mermaid in obsidian.md)  