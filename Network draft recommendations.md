---
date created: 2025-11-14T13:35:07+01:00
date modified: 2025-12-02T20:33:40+01:00
---
## Aanbevelingen:

   1. Formeel Risicobeoordelingsproces: Voer een formeel proces in voor risicobeoordeling om de zoneplaatsing van
      bedrijfsmiddelen te bepalen.
   2. Introduceer Security Levels (SLs): Vervang de "Trust Levels" door de formele "Security Levels" (SL 1-4) uit
      IEC 62443 voor duidelijkere beveiligingseisen per zone.
   3. Richt u op de Foundational Requirements (FRs): Structureer uw beveiligingsmaatregelen rond de zeven FR's
      van IEC 62443 voor een completere aanpak.
   4. Breid Levenscyclusbeheer uit: Voeg een sectie toe over "Security Lifecycle Management" om de beveiliging
      gedurende de gehele levenscyclus van een systeem te beschrijven.
   5. Verbeter de Traffic Flow Matrix: Maak een gedetailleerde matrix die de toegestane en geweigerde
      verkeersstromen tussen alle zones en VRF's weergeeft.

## Toevoegen
   1. Incident Response Plan voor OT:
       * Wat: Een specifiek plan dat beschrijft hoe te reageren op een cyberincident in de OT-omgeving. Wie
         wordt gecontacteerd? Wat zijn de stappen om een systeem te isoleren? Hoe wordt de productie veilig
         hersteld?
       * Waarom: De responstijd en -methode in een OT-omgeving zijn totaal anders dan in IT. Prioriteit is hier
         veiligheid en continuïteit, niet alleen dataherstel. Dit is een kernonderdeel van IEC 62443-2-3.

   2. Gedetailleerd Patch Management Beleid:
       * Wat: Een strategie voor het beheren van patches en updates in zowel IT- als OT-omgevingen. Beschrijf
         hoe en wanneer er wordt gepatcht, hoe patches worden getest (vooral voor OT), en wat de procedure is
         voor systemen die niet (direct) gepatcht kunnen worden (compensating controls).
       * Waarom: "Patchability" is al een criterium in uw document. Een uitgewerkt beleid maakt dit concreet en
         afdwingbaar. Ongepatchte systemen zijn een van de grootste risico's.

   3. Beveiliging van Draadloze Netwerken (WiFi):
       * Wat: Breid de sectie over WiFi uit met specifieke eisen voor:
           * Corporate WiFi: Authenticatie via 802.1X/RADIUS, WPA3-Enterprise.
           * Guest WiFi: Volledige isolatie, captive portal, bandbreedtelimieten.
           * Industrial WiFi: Strikte toegangscontrole op basis van MAC-adres of certificaten, aparte SSID's
             voor vaste en mobiele apparaten (AGV's, tablets), en fysieke dekkingsanalyse om signaal "lekken"
             buiten de fabriek te minimaliseren.
       * Waarom: Elk type WiFi-netwerk heeft een ander risicoprofiel en vereist specifieke
         beveiligingsmaatregelen.

   4. Fysieke Beveiliging van Netwerkapparatuur:
       * Wat: Een sectie die eist dat kritieke netwerkapparatuur (switches, firewalls, servers) in afgesloten
         ruimtes staat met toegangscontrole. Beschrijf ook de beveiliging van netwerkaansluitingen in de
         fabriekshal om ongeautoriseerde aansluitingen te voorkomen.
       * Waarom: Cyberbeveiliging begint met fysieke beveiliging. Iemand met fysieke toegang kan veel digitale
         barrières omzeilen.

   5. Secure Remote Access (Gedetailleerd):
       * Wat: Werk de regels voor remote access verder uit. Specificeer welke protocollen zijn toegestaan via de
         Jump Servers (bv. alleen RDP/SSH via een PAM-oplossing), dat alle sessies worden opgenomen (session
         recording), en dat Multi-Factor Authenticatie (MFA) verplicht is.
       * Waarom: Remote access is een favoriet doelwit voor aanvallers. Strikte, gedetailleerde regels zijn
         essentieel om dit risico te beheersen.

   6. Configuratiebeheer (Configuration Management):
       * Wat: Een proces om een veilige basisconfiguratie (baseline) voor alle systemen (servers, PLC's,
         switches) vast te leggen en te onderhouden. Alle wijzigingen aan deze configuratie moeten via een
         change management proces lopen.
       * Waarom: Dit voorkomt "configuration drift" waarbij systemen over tijd onveiliger worden door
         ongecontroleerde wijzigingen. Het zorgt voor consistentie en traceerbaarheid.

   7. Training en Bewustzijn:
       * Wat: Een paragraaf die het belang van training benadrukt. Operators in de fabriek hebben andere
         training nodig (bv. herkennen van afwijkend systeemgedrag) dan IT-personeel (bv. security best
         practices).
       * Waarom: De menselijke factor is cruciaal. Goedgetrainde medewerkers vormen een belangrijke
         verdedigingslaag.
   * 