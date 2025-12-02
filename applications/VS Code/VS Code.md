---
date created: 2025-09-18T07:13:09+02:00
date modified: 2025-09-18T12:02:58+02:00
---
## Project overzetten naar pc zonder internet
    1. Installeer VS Code op de pc zonder internet
    2. Activeer je venv
        venv\Scripts\activate
    2. Kopieer je volledige project naar de pc zonder internet
    3. Op je pc met internet maak je requirements.txt aan en download de modules naar map packages
        pip freeze > requirements.txt
        pip download -r requirements.txt -d packages/
    4. Kopieer de map packages naar de pc zonder internet en intalleer ze hier
        pip install --no-index --find-links=packages/ -r requirements.txt
    5. Kopieer de map C:\Users\<jouw gebruikersnaam>\.vscode\extensions naar de map op de pc zonder internet en start VS Code opnieuw op

## Fout van opc
    1. Kopieer file gbhda_aw.dll naar map C:\windows\SysWOW64
    2. Run regsvr32 gbhda_aw.dll in cmd as admin

## Instellingen
### Verbergen van bestanden (files.exclude)
Voeg dit toe aan .vscode/settings.json
```
"files.exclude": {
        //"**/.gitignore": true,
        //"**/.pylintrc": true,
        "**/__pycache__": true,
        "**/uv.lock": true,
        "**/.venv": true,
        "**/.mypy_cache": true,
        "**/.pytest_cache": true,
        "**/.idea": true,
        "**/.obsidian": true,
    },
```
## Extensions
 - [[applications/VS Code/PyLint]]
