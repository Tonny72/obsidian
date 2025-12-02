---
date created: 2025-07-22 00:00
links:
  - Jupyter Notebook
  - Marimo
modified: 2025-09-09 21:41
---
# Marimo vs Jupyter Notebook

| feature          | Marimo                                                           | Jupyter Notebook                                                                                                                      |
| ---------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Export naar PDF  | Kan exporteren naar HTML en MD. PDF-export vereist Pandoc en Tex | Makkelijk te combineren met nbconvert voor PDF-export                                                                                 |
| ondersteuning    | minder community ondersteuning                                   | zeer populair en breed ondersteund                                                                                                    |
| VScode / PyCharm | nee                                                              | ja                                                                                                                                    |
| Git              | ja                                                               | nee<br>[[nbconvert]] gebruiken om op te slaan als .py<br>`jupyter nbconvert notebook.ipynb --to script`<br>Of `nbdime` eens bekijken. |
|                  |                                                                  |                                                                                                                                       |
## Conclusie
- [[journals/2025/07/2025-07-22]] Gebruik Jupyter Notebook: Deze is de de facto standaard. 

## Links
- [Marimo](dev/Python/Marimo.md)
- [Jupyter Notebook](dev/Python/Jupyter%20Notebook.md)
