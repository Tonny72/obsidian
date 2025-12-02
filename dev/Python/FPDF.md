---
date created: 2025-07-24 00:00
modified: 2025-09-15 10:27
---
## Log
- [[journals/2025/07/2025-07-24]] Gekozen voor [ReportLab](dev/Python/ReportLab.md)
## Copilot example
```python
import polars as pl
from fpdf import FPDF

df = pl.DataFrame({
    "Naam": ["Tonny", "Lisa", "Mark"],
    "Score": [88, 92, 75],
    "Status": ["Geslaagd", "Geslaagd", "Herexamen"]
})

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Studentenrapport", ln=True, align="C")

    def table(self, df):
        self.set_font("Arial", "B", 12)
        col_width = self.w / (len(df.columns) + 1)
        row_height = self.font_size * 1.5

        # Kolomkoppen
        for header in df.columns:
            self.cell(col_width, row_height, header, border=1, align='C')
        self.ln(row_height)

        # Rijen
        self.set_font("Arial", "", 12)
        for row in df.rows():
            for item in row:
                self.cell(col_width, row_height, str(item), border=1, align='C')
            self.ln(row_height)

pdf = PDF()
pdf.add_page()
pdf.table(df)
pdf.output("fpdf_output.pdf")

```