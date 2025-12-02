---
date created: 2025-09-18T07:13:09+02:00
date modified: 2025-09-19T07:53:20+02:00
---
UV is een Python package manager.
1. Na een git clone: `uv venv`
2. `.venv/scrpts/activate`

## Exporteer project naar pc zonder internet
```commandline
uv sync --no-dev
pip freeze > requirements.txt
pip download --dest ./packages -r requirements.txt
```
