---
date created: 2025-09-12T22:07:00+02:00
date modified: 2025-09-22T09:30:34+02:00
tags: [dev, Python]
---


Door elke class in een aparte file te plaatsen, kun je je project **modulair en overzichtelijk** houden. En door een centrale `models.py` (de facade module) te maken, hoef je in je hoofdcode of andere modules **alleen maar**:

```python
from models import TaskGroup, CommandTask, Server
```

te doen, zonder je zorgen te maken over waar die klassen precies gedefinieerd zijn.

### Hoe je dit kunt structureren

Bijvoorbeeld:

```
project/
│
├── models.py              # Facade module
├── task_models/
│   ├── __init__.py        # Eventueel leeg of met imports
│   ├── base_task.py
│   ├── email_task.py
│   ├── backup_task.py
│   ├── command_task.py
│   ├── import_task.py
│   └── task_group.py
│
├── server_models/
│   ├── __init__.py
│   ├── server.py
│   ├── file_database_server.py
│   ├── opc_server.py
│   ├── email_server.py
│   └── server_types.py
```

In `models.py` importeer je dan alles wat je publiek beschikbaar wilt maken:


```python
"""Facade module for backward-compatible and simplified imports.

This module re-exports task and server models from their dedicated modules
so that imports like `from models import TaskGroup, CommandTask` keep working.
"""

from __future__ import annotations
from typing import Any
import dataclasses

# Task-related imports
from task_models.base_task import BaseTask
from task_models.email_task import EmailTask
from task_models.backup_task import BackupTask
from task_models.command_task import CommandTask
from task_models.import_task import ImportTask
from task_models.task_group import TaskGroup
from task_models import TASK_TYPES

# Server-related imports
from server_models.server import Server
from server_models.file_database_server import FileDatabaseServer
from server_models.opc_server import OPCServer
from server_models.email_server import EmailServer
from server_models import SERVER_TYPES

# Public API of this module
__all__ = [
    # Tasks
    "BaseTask",
    "EmailTask",
    "BackupTask",
    "CommandTask",
    "ImportTask",
    "TaskGroup",
    "TASK_TYPES",
    # Servers
    "Server",
    "FileDatabaseServer",
    "OPCServer",
    "EmailServer",
    "SERVER_TYPES",
]

```

### Voordelen

- ✅ **Schaalbaarheid**: Je kunt makkelijk nieuwe klassen toevoegen zonder je hoofdcode aan te passen.
- ✅ **Leesbaarheid**: Elke class zit in een eigen bestand, dus makkelijker te onderhouden.
- ✅ **Herbruikbaarheid**: Andere modules kunnen ook gewoon `from models import ...` doen.

