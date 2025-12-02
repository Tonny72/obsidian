---
date created: 2022-11-15
date modified: 2025-08-30
---

- # [[2022-11-15]]
  Harry heeft gevraagd voor een THD lijn-schema.
- # Hoe rapporteren?
- **Het 1-lijns-schema van ABB aanpassen**  
  Nadeel:
	- De PLC van 15.1 heeft waarschijnlijk hier niet genoeg geheugen voor.
	- Enkel momentele waarden de zien.
	  Voordeel:
- 1-lijn schema. Makkelijk zien vanwaar data komt.
- **Power BI**  
  Nadeel:
	- Data wordt wordt telkens volledig en traag ingelezen. (testen gedaan met inlezen van parquet bestanden)  
	  Zelfs het inlezen van bestanden van enkele MB duurt lang.  
	  Een .parquet bestand van 420MB duurt 77 seconden.  
	  ~~Het opsplisten van de parquet bestanden dmv een dataset en dan inlezen met een Python script werkt niet. Krijg de foutmelding "kan module pyarrow" niet vinden, terwijl deze toch geïnstalleerd is.~~ Opgelost.
	- Geen makkelijke groepering op uur, minuut. Dit moet handmatig gebeuren. Maar zeker wel bruikbaar
	  
	  Voordeel:
- Visuele voorstelling van de data
- Men kan met de data 'spelen'
  
  Mogelijke oplossing:
- Data consolideren. Minder data om in te lezen
- **Python Rapport**
  Nadeel:
- Veel manueel werk.