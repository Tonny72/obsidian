---
date created: 2025-05-26
date modified: 2025-07-21
---
# C2 Analoog

```dataview
TABLE FM.description as description, FM.range, FM.unit, FM.HHH, FM.HH, FM.H, FM.L, FM.LL, FM.LLL
from #C2 FLATTEN file.frontmatter as FM
WHERE contains(file.folder, this.file.folder)
AND contains(app-categories, this.link)
SORT FM.description
```
