---
aliases:
  - Daily note simple
---





## Last Modified Today

```dataview
TABLE string(split(string(file.mtime), " - ")[0]) as "Last Modified"
WHERE !contains(file.path, "{{date:YYYY-MM-DD}}")
  AND !contains(file.path, "{{date:YYYY-MM-DD}} Daily Note")
  AND file.mday = date("{{date:YYYY-MM-DD}}")
SORT file.mtime DESC
```

