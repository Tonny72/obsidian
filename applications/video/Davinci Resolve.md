---
date created: 2018-02-12T00:00:00+01:00
modified: 2025-09-09 21:56
date modified: 2025-09-18T22:13:50+02:00
---
# Davinci Resolve

Davinci Resolve
maandag 12 februari 2018
7:13

- Kan niet op laptop installeren. Krijg foutmelding over domain password policy. =\> Eerst appart de database installeren
- Kan niet rechtstreeks camera bestanden inladen <https://www.easefab.com/topic-avchd/import-mts-files-to-davinci-resolve.html> Het geluid werkt niet
- Heeft maar heel weining toeters en bellen. Te weinig eigenlijk.
- Niet zoveel mee gespeeld, maar voldoet eigenlijk wel en is gratis
- Importeerd geen .mp3 bestanden
- Exporteerd geen H.264 of H.265
- **[[2016-04-21]]** versie 12.5 getest. Er is niet veel veranderd. Geen geluid op camera bestanden en geen H.264 export
- [[2017-02-27]] nog eens getest. Ik krijg niet gevonden hoe je transition insteld. In en uit zoomen gaat met Alt scroll. Hoogte van video kanaal wijzigen gaat. Volume aanpassen gaat ook, maar bij het verlagen van het volume, verdwijnt ook de wavevorm zoals bij Powerdirector  
  Conclusie: De gewenste features zullen er wel in zitten. Maar het geluid afkomstig van de video camera wordt niet ondersteund. Dus er is altijd een hercodering nodig. Ik heb dit getest met Adobe Media Encoder. Deze lijkt gratis, maar bij het omzetten naar een ander formaat worden deze 10x groter.  
  Gebruikelijke (export) codecs DPX, MXF OP-Atom (DNxHR), MXF OP1A (DNxHR).  
  Kan GEEN voordelen ontdekken tov Vegas
- [[2017-05-31]] Nieuwe versie Public beta 14  
  Nog altijd geen audio bij de .MTS bestanden van de videocamera  
  Ook nog altijd te traag bij het afspelen
- [[2017-07-29]] audio is opgelost
- [[2017-08-28]] beta8 nog altijd traag afspelen. Zelfs met optimized media en quarter resolution proxy mode
- [[2017-10-16]]
  Davinci Resolve is uit beta en werkt goed. Maar is zeer ingewikkeld.
- Video en audio niet in sync bij sommige clips !!!! (versie 14.0.1) =\> GEBRUIK XMedia Recode
- [[2017-12-03]]  
  Project gemaakt met DR, maar niet aan het audio sync probleem gedacht.
- [[2018-02-12]]  
  Het stabilize-effect van Resolve is goed
- [[2018-02-12]]  
  De integra van Fusion in Resolve is toch niet zo goed er moet telkens worden gerenderd als er iets wordt aangepast.  
  Zeer omslachtige workflow

- [[2018-05-11]]  
  Fusion zit nu in Resolve. Top feature
- # [[2019-02-15]] 
  We zitten ondertussen op 15.2.4
  
  Snelle test met camera beelden
- Audio gaat goed
- Export naar MP4 is goed
- Snel tekst toevoegen in Fusion, geen probleem
- Integratie van Fusion is perfect. Er moet niet meer gerendered worden bij het verlaten van Fusion.
- Na Prerender Fusion Cache is clip goed afspeelbaar 27 fps
- # [[2020-03-28]] 
  Ondertussen Davinci resolve 16.2
  
  Weetjes: OP MSI Nvidia Studio driver geïnstalleerd !
  
  Na toevoegen .MTS bestanden selecteer alle clips, rechtsklik en kies Clip Attributes
  
  ![image1](image1-51.png)