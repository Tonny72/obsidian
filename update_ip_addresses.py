
import os
import re

test = '''
---
ip: 10.32.27.62
description: Siemens Beckhoff
---
# BE-DES-TDC-025
## Mapping
`net use s: \\10.32.29.60\Automation`
## Applications
### Siemens Log
- path: `C:\Log`
	- Deze directory wordt gekopieerd naar `S:\Data\SIEMENS_SQL`
- Copy data: `robocopy "C:\Log" "S:\Data\Siemens_SQL" *.db3  /e /xf *.db3-shm *.db3-wal`
### [[WinCC Unified]]

## Links
- [[Sync Siemens Log files]]'''

# Define the folder containing the markdown files
folder_path = "D:/OneDrive/Dev/md"
# Regular expression to match IP addresses in the format x.x.x.x (case-insensitive, lowercase 'ip:')
ip_pattern = re.compile(r"[iI][pP]:\s*(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})")


# Function to zero-pad each segment of the IP address, always output 'ip:' in lowercase
def pad_ip(match):
    return f"ip: {int(match.group(1)):03}.{int(match.group(2)):03}.{int(match.group(3)):03}.{int(match.group(4)):03}"

updated_content = ip_pattern.sub(pad_ip, test)

# Process each markdown file in the folder
for root, _, files in os.walk(folder_path):
    for filename in files:
        if filename.endswith(".md"):
            file_path = os.path.join(root, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            # Debug: print all matches before replacement
            for ip_match in ip_pattern.finditer(content):
                print(f"Match gevonden in {file_path}: {ip_match.group(0)}")

            # Replace IP addresses with zero-padded format
            updated_content = ip_pattern.sub(pad_ip, content)

            # Save the updated content back to the file
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(updated_content)

print("Alle IP-adressen zijn bijgewerkt naar nul-gevuld formaat in de markdown-bestanden.")


