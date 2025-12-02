"""
Read 'IP adressen.xlsx' and create markdown files in an 'import' folder.
- Filename: value from column A with .md extension
- Content: YAML front matter (Obsidian-style) with one property per Excel column

Assumptions:
- The Excel file is located in the same folder as this script (detailed path can be changed)
- The first row contains headers which will be used as property names
- Column A contains unique filenames (if not, files will be overwritten)

Usage:
    python import_ips_from_excel.py

"""

import os
import sys
import pandas as pd

# Config
WORKDIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_FILE = os.path.join(WORKDIR, "IP adressen.xlsx")
OUTPUT_DIR = os.path.join(WORKDIR, "import")


def sanitize_key(key: str) -> str:
    """Make header safe for YAML/Obsidian property names."""
    return str(key).strip()


def sanitize_value(value) -> str:
    """Convert NaN to empty string and ensure string representation."""
    if pd.isna(value):
        return ""
    return str(value)


def main():
    if not os.path.exists(EXCEL_FILE):
        print(f"Excel file not found: {EXCEL_FILE}")
        sys.exit(1)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Read Excel
    df = pd.read_excel(EXCEL_FILE, engine="openpyxl")

    if df.empty:
        print("Excel sheet is empty - nothing to do")
        return

    headers = [sanitize_key(h) for h in df.columns]

    for idx, row in df.iterrows():
        # Use first column as filename (column A)
        filename_base = sanitize_value(row.iloc[0])
        if not filename_base:
            print(f"Skipping row {idx+1}: empty filename column")
            continue

        # Build YAML front matter
        yaml_lines = ["---"]
        for col, header in zip(df.columns, headers):
            value = sanitize_value(row[col])
            yaml_lines.append(f"{header}: {value}")
        yaml_lines.append("---")
        yaml = "\n".join(yaml_lines) + "\n\n"

        content = yaml

        out_path = os.path.join(OUTPUT_DIR, f"{filename_base}.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)

    print(f"Generated {len(df)} markdown files in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
