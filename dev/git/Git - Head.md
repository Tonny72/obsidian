---
date created: 2025-07-25
modified: 2025-07-25
---
In Git is `HEAD` **een verwijzing naar de huidige commit waarop je werkt**. Je kunt het zien als een soort “marker” die aangeeft waar je je bevindt in de geschiedenis van je project.

### 🔍 Wat doet `HEAD` precies?
- Het **wijst naar de laatste commit** in de branch die je hebt uitgecheckt.    
- Als je van branch wisselt, **verplaatst** `HEAD` **mee** naar die nieuwe branch.
- Als je een commit maakt, **verschuift** `HEAD` **automatisch** naar die nieuwe commit.

### 🧠 Voorbeeld
Stel je zit op branch `main`, dan wijst `HEAD` naar de laatste commit op `main`. Als je overschakelt naar branch `LEMTON00`, dan wijst `HEAD` naar de laatste commit op `LEMTON00`.
Je kunt dit zelf bekijken met:
```bash
cat .git/HEAD
```
Dat geeft bijvoorbeeld:
```
ref: refs/heads/main
```
### ⚠️ Detached HEAD
Soms wijst `HEAD` niet naar een branch maar direct naar een commit. Dat heet een **“detached HEAD”**. Dan werk je buiten een branch en je commits zijn moeilijker terug te vinden tenzij je ze opslaat in een nieuwe branch.
Wil je dat ik je help om te zien waar jouw `HEAD` nu naar wijst of wat je ermee kunt doen in jouw situatie?