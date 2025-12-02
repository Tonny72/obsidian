---
tags: [dev]
modified:  2025-07-30
date created: 2025-05-26T00:00:00+02:00
date modified: 2025-09-19T14:40:09+02:00
---

## Install uv
```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```


## Install latest python

 ```
  uv python install
```
## View available Python versions
```
  uv python list
```

## Executing standalone Python scripts, e.g., `example.py`.
- `uv run`: Run a script.


## [Projects](https://docs.astral.sh/uv/getting-started/features/#projects)
Creating and working on Python projects, i.e., with a `pyproject.toml`.
- `uv init`: Create a new Python project.
- `uv add`: Add a dependency to the project.
- `uv remove`: Remove a dependency from the project.
- `uv sync`: Sync the project's dependencies with the environment.
- `uv lock`: Create a lockfile for the project's dependencies.
- `uv run`: Run a command in the project environment.
- `uv tree`: View the dependency tree for the project.
- `uv build`: Build the project into distribution archives.
- `uv publish`: Publish the project to a package index.

## [Creating a virtual environment](https://docs.astral.sh/uv/pip/environments/#creating-a-virtual-environment)
```
  uv venv
```
### Activate
`.venv/scripts/activate`

### Als het weer eens niet wil werken
- verwijder .venv directory
- `uv venv`
- `.venv/scripts/activate`
