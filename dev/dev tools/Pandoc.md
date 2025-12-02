---
modified:  2025-07-23
date created: 2025-07-11T00:00:00+02:00
date modified: 2025-09-19T21:01:30+02:00
---
# Pandoc
## Convert Word .docx to markdown
`pandoc -s "Project_1827_-_Vervangen_Captors_door_Sailors.docx" -t markdown --extract-media=images -o "Project_1827_-_Vervangen_Captors_door_Sailors.md"`


## conversie .html to pdf
Dit werkt niet.
```shell
pandoc jouw_bestand.html -o output.pdf
```