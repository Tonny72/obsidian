---
modified:  2025-09-09 21:32
tags: [dev]
date created: 2025-07-10T00:00:00+02:00
date modified: 2025-10-06T12:06:07+02:00
---
## VSCode shortcuts
Poging om een editor te hebben met zo weinig mogelijk muis gebruik.
[VSCode shortcuts](dev/dev%20tools/VSCode/VSCode%20shortcuts.md)

## Also read the manual
[Basic editing](https://code.visualstudio.com/docs/editing/codebasics)

## Active Editor Group
There is no standard shortcut to activate the editor window.
- Ctrl k Ctrl s to activate Keyboard shortcuts
- type: focus active editor group
- Add a new keybinding


## Instellingen
### ⚙️ Instelling: `editor.cursorSurroundingLines`

1. Open je **Instellingen** (`Ctrl + ,`)
2. Zoek naar: `cursorSurroundingLines`
3. Zet de waarde op bijvoorbeeld `100` (een hoog getal)
    ```
    "editor.cursorSurroundingLines": 100,
    "editor.cursorSurroundingLinesStyle": "default"
    ```
🔁 Hierdoor blijft de cursor visueel in het midden van het scherm terwijl je door je code navigeert met pijltjestoetsen.

## Extensions
- Paste Image
	- Copy paste images in a markdown document
	- [Paste Image - Visual Studio Marketplace](https://marketplace.visualstudio.com/itemsitemName=mushan.vscode-paste-image&ssr=false#review-details)
- Even Better Toml
	- Syntax highlighting for toml documents
- Data Wrangler
	- ([[2025-07-11]]: Ik krijg Data Wrangler niet werkend onder Windows 8.1)
- emojisense
	- adds suggestions and autocomplete for emoji
- Black Formatter
	- Formatting support for Python files using the Black formatter.
- Data Preview of Data Wrangler
	- preferred Data Wrangler
	- Data viewing
- Even Better TOML
- Git Graph
- Github Copilot
- Jupyter Notebook
- Jupyter Notebook renders
- Markdown Paste
- Markdown PDF
- Markdown Preview enhanced 
- Markdown Table
- markdown lint 
- [[dev/documentation tools/Mermaid]] Chart 
- [[dev/documentation tools/Mermaid]] Preview
- Mypy Type Checker
- Parquet viewer
- Pylance
- Python
- Python Codelens
- Python Debugger 
- Ruff
### [[applications/Obsidian/Obsidian]] MD for VSCode
Met deze plugin kan je [[applications/Obsidian/Obsidian]] bedienen vanuit VSCode. Weinig spectaculair. Er is altijd Obsidian nodig.
## Settings
- [markdown automatic link updates-on-file-move-or-rename](https://code.visualstudio.com/docs/languages/markdown#_automatic-link-updates-on-file-move-or-rename)
## De praktische middenweg: VS Code Workspaces 
Voor jouw situatie is er een oplossing die het beste van twee werelden combineert: **VS Code Workspaces**.
Hiermee hou je je projecten in **aparte mappen met hun eigen `git`-repository**, maar je opent ze samen in **één enkel VS Code-venster**.
  
💡 **Hoe het werkt:**
- **Houd je mappen gescheiden.** Maak bijvoorbeeld een mappenstructuur zoals:
- `/projecten/data-analyse-scripts/` (met eigen `.git`)
- `/projecten/marimo-rapporten/` (met eigen `.git`, of in dezelfde repo als de scripts als ze heel nauw verbonden zijn)
- `/projecten/pkm/` (je notities, eventueel met een eigen `.git`)
- **Open deze mappen in VS Code.** Ga naar `File > Add Folder to Workspace...` en voeg de verschillende mappen toe.
- **Sla de Workspace op.** Ga naar `File > Save Workspace As...` en sla het `.code-workspace` bestand op. Vanaf nu kun je dit bestand openen om direct je volledige setup met alle mappen te laden.

**Voordelen van deze aanpak:**
- **Overzicht:** Je ziet al je projectmappen in de verkenner van VS Code, net als in een monorepo.
- **Isolatie:** Elk project heeft zijn eigen `git`-geschiedenis en kan zijn eigen dependencies hebben (al kun je ze ook delen).
- **Duidelijkheid:** Je scheidt je code (scripts, rapporten) van je documentatie (PKM), wat logisch en opgeruimd is.

## Debug Python
- Ctrl Shift P
- Open "Launch.json"
```
  "name": "Python Debugger: Current File",
  "type": "debugpy",
  "request": "launch",
  "program": "${file}",
  "console": "integratedTerminal",
  "env": {"PYTHONPATH": "${workspaceFolder}"},
  "args": ["configs\\local\\deseng1_config.toml"],
``` 
## UNC path
to allow UNC path in project
	- File -> Preferences -> Settings
		- Application -> Experimental: **Restrict UNCAccess**
		- Application -> Settings Sync -> Security: **Allowed UNCHosts**
		- ![image.png](assets/images/image_1699275748673_0\.jpg)

## Coding fonts
[Programming Fonts - Test Drive](https://www.programmingfonts.org/#chivo)
[Monaspace](https://monaspace.githubnext.com/)
