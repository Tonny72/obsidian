---
date created: 2013-05-27
tags:
  - Video
modified: 2025-08-06
---
# VidCoder
Omzetten van video bestanden
Werkt op basis van [[applications/video/Handbrake]]

## Insights
- Used [[ffmepg]] and python script to convert old video files to [[H.265]]
## Log
[[journals/2025/2025-08-02]] Versie 12.2 (beta) getest.

## Screenshot

![image1](image1-14.png)

Wat ook eens volgens tweakers moet bekeken worden is
<http://www.clonead.co.uk/>

Omzetten van video bestanden
Werkt op basis van Handbrake

![image1](image1-42.png)

Wat ook eens volgens tweakers moet bekeken worden is
<http://www.clonead.co.uk/>

## Copilot instellingen
### VidCoder H.265-profiel voor SD-video (8-bit)
- **Container**: MP4
- **Video Encoder**: H.265 (x265)
- **Bitrate/Quality**:
    - Selecteer **Constant Quality (CQ)**
    - **RF-waarde**: `20` _(balans tussen kwaliteit en compressie voor SD)_
- **Preset**: `Slow` _(voor betere compressie)_
- **Tune**: `None` _(of_ `film` _als het cinematisch materiaal betreft)_
- **Framerate**: `Constant (25 fps)` _(past bij PAL video)_
- **Filters**:
    - **Deinterlace**: `Yadif` of `Decomb` _(indien je bronmateriaal interlaced is)_
- **Audio**:
    - Encoder: `AAC`
    - Bitrate: `160 kbps` _(of behoud origineel via passthrough)_

## Experiment instellingen
### Origineel Video Londen Tonny.mpg
- 2.44GB
- resolutie: 720x576
- Codec: MPEG-2
- Framerate: 25 FPS

	- H.265 NVidia Snel (Maar gebruik de studio driver)
	- H.265 Intel => OK
	- H.265 x265 => Zeer traag = CPU based
