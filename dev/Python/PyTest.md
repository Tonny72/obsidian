---
date created: 2025-08-13 00:00
modified: 2025-09-15 10:27
---
## Example with parameters
```python
import pytest
from main import is_prime

@pytest.mark.paramtrize("num, expected", [
  (1, False),
  (2, True),
  (3, True),
  (4, False)
])
def test_is_prime(num, expected):
	assert is_prime(num) == expected
```

## Mock
### db.py
```python
def save_user(name, age):
	conn = sqlite3.connect("user.db)
	cursor = conn.cursor()
	cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
	conn.commit()
	conn.close()
```
### test_db.py
```python
from db import save_user

def test_save_user(mocker):
	mock_conn = mocker.patch("sqlite3.connect")
	mock_cursor = mock_conn.return_value.cursor.return_value

	save_user("Alice", 30)

	mock_conn.assert_called_once_with("users.db")
	mock_cursor.execute.assert_called_once_With(
		"INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30)
	)
```
