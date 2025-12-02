---
modified:  2025-08-20
date created: 2025-07-24T00:00:00+02:00
date modified: 2025-09-19T20:59:16+02:00
---
## Voorbeeld van Copilot
```python
import polars as pl

from reportlab.lib.pagesizes import A4, landscape

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

from reportlab.lib import colors

  

# Simuleer een Polars dataframe

df = pl.DataFrame({

    "Naam": ["Tonny", "Lisa", "Mark"],

    "Score": [88, 92, 75],

    "Status": ["Geslaagd", "Geslaagd", "Herexamen"]

})

  

# Zet om naar lijst van lijsten
data = [df.columns] + df.rows()

# Maak PDF
doc = SimpleDocTemplate("reportlab_output.pdf", pagesize=landscape(A4))

table = Table(data, hAlign="LEFT")
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("GRID", (0, 0), (-1, -1), 1, colors.grey),
    ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
]))

doc.build([table])
```