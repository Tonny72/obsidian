---
date created: 2024-07-26T15:46:00
---

```dataview
TABLE FM.description as description, FM.range, FM.unit, FM.HHH, FM.HH, FM.H, FM.L, FM.LL, FM.LLL
from #C2 FLATTEN file.frontmatter as FM
WHERE contains(file.folder, this.file.folder)
AND contains(app-categories, this.link)
SORT FM.description
```
