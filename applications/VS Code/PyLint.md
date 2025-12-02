---
date created: 2025-09-18T10:51:25+02:00
date modified: 2025-09-19T10:51:10+02:00
---
**Pylint** is een **Python static code analyzer** – een tool die je helpt om je Python-code te controleren op fouten, stijlproblemen en best practices **zonder de code uit te voeren**.

---

### 🔍 Wat doet Pylint precies?

Pylint analyseert je code en geeft waarschuwingen of fouten over:

- **Syntaxisproblemen** (zoals fout gespelde variabelen)
- **Stijlregels** (zoals of je wel een docstring hebt bij functies of klassen)
- **Best practices** (zoals het vermijden van globale variabelen)
- **Ongebruikte imports of variabelen**
- **Codecomplexiteit** (bijvoorbeeld te lange functies)

## Instellingen
### Uitzetten docstring warnings
In [[VS Code]] settings (ctrl ,) bij de Args deze regel toevoegen
```
--disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
```
![[_assets/Pasted image 20250918105442\.jpg]]

Dit is mogelijk de lijn in settings.json
```
"pylint.args": [
        "--disable=missing-function-docstring,missing-module-docstring,missing-class-docstring"
    ],
```
## Links
- [[VS Code]]
