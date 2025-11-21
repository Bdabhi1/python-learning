# Database Connectivity in Python

Python provides excellent support for connecting to and working with databases. The most common approach is using database-specific adapters like `sqlite3` (built-in) or third-party libraries like `mysql-connector-python` and `psycopg2` for PostgreSQL.

## Table of Contents
1. [What is Database Connectivity?](#what-is-database-connectivity)
2. [SQLite Database](#sqlite-database)
3. [Connecting to Databases](#connecting-to-databases)
4. [Executing Queries](#executing-queries)
5. [Parameterized Queries](#parameterized-queries)
6. [Transactions](#transactions)
7. [Error Handling](#error-handling)
8. [Best Practices](#best-practices)

---

## What is Database Connectivity?

**Database connectivity** allows Python programs to:
- **Connect** to databases
- **Execute** SQL queries
- **Retrieve** data from databases
- **Insert, update, delete** data
- **Manage** transactions

**Common Databases:**
- **SQLite**: Lightweight, file-based (built-in)
- **MySQL**: Popular open-source database
- **PostgreSQL**: Advanced open-source database
- **SQL Server**: Microsoft database
- **Oracle**: Enterprise database

**Python Database Libraries:**
- `sqlite3`: Built-in SQLite support
- `mysql-connector-python`: MySQL connector
- `psycopg2`: PostgreSQL adapter
- `pyodbc`: ODBC database access

---

## SQLite Database

SQLite is a lightweight, file-based database that comes built-in with Python.

### Creating a Database

```python
import sqlite3

# Connect to database (creates if doesn't exist)
conn = sqlite3.connect('example.db')

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        age INTEGER
    )
''')

# Commit changes
conn.commit()

# Close connection
conn.close()
```

### Using Context Manager

```python
import sqlite3

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE
        )
    ''')
    conn.commit()
```

---

## Connecting to Databases

### SQLite Connection

```python
import sqlite3

# Basic connection
conn = sqlite3.connect('database.db')

# Connection with options
conn = sqlite3.connect(
    'database.db',
    timeout=5.0,
    isolation_level=None  # Auto-commit mode
)

# In-memory database
conn = sqlite3.connect(':memory:')
```

### MySQL Connection (Example)

```python
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='username',
    password='password',
    database='mydb'
)
```

### PostgreSQL Connection (Example)

```python
import psycopg2

conn = psycopg2.connect(
    host='localhost',
    user='username',
    password='password',
    database='mydb'
)
```

---

## Executing Queries

### SELECT Queries

```python
import sqlite3

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    
    # Fetch all rows
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    # Fetch one row
    cursor.execute('SELECT * FROM users WHERE id = ?', (1,))
    row = cursor.fetchone()
    
    # Fetch many rows
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchmany(5)  # Fetch 5 rows
```

### INSERT Queries

```python
import sqlite3

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    
    # Insert single row
    cursor.execute(
        'INSERT INTO users (name, email, age) VALUES (?, ?, ?)',
        ('Alice', 'alice@example.com', 30)
    )
    
    # Insert multiple rows
    users = [
        ('Bob', 'bob@example.com', 25),
        ('Charlie', 'charlie@example.com', 35)
    ]
    cursor.executemany(
        'INSERT INTO users (name, email, age) VALUES (?, ?, ?)',
        users
    )
    
    conn.commit()
```

### UPDATE and DELETE Queries

```python
import sqlite3

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    
    # Update
    cursor.execute(
        'UPDATE users SET age = ? WHERE id = ?',
        (31, 1)
    )
    
    # Delete
    cursor.execute('DELETE FROM users WHERE id = ?', (2,))
    
    conn.commit()
```

---

## Parameterized Queries

**Always use parameterized queries** to prevent SQL injection attacks.

### Using Placeholders

```python
import sqlite3

# SQLite uses ? placeholders
cursor.execute('SELECT * FROM users WHERE name = ?', (name,))

# MySQL uses %s placeholders
cursor.execute('SELECT * FROM users WHERE name = %s', (name,))

# PostgreSQL uses %s placeholders
cursor.execute('SELECT * FROM users WHERE name = %s', (name,))
```

### Named Parameters

```python
import sqlite3

# SQLite supports named parameters
cursor.execute(
    'SELECT * FROM users WHERE name = :name AND age > :age',
    {'name': 'Alice', 'age': 25}
)
```

---

## Transactions

Transactions ensure data integrity by grouping operations.

### Manual Transaction Control

```python
import sqlite3

conn = sqlite3.connect('example.db')
try:
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name) VALUES (?)', ('Alice',))
    cursor.execute('INSERT INTO users (name) VALUES (?)', ('Bob',))
    conn.commit()  # Commit transaction
except Exception as e:
    conn.rollback()  # Rollback on error
    print(f"Error: {e}")
finally:
    conn.close()
```

### Context Manager (Auto-commit)

```python
import sqlite3

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name) VALUES (?)', ('Alice',))
    # Auto-commits on successful exit
```

---

## Error Handling

### Database Exceptions

```python
import sqlite3

try:
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM nonexistent_table')
except sqlite3.OperationalError as e:
    print(f"Database error: {e}")
except sqlite3.IntegrityError as e:
    print(f"Integrity error: {e}")
except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    if conn:
        conn.close()
```

### Connection Error Handling

```python
import sqlite3

def connect_db(db_name):
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None
```

---

## Best Practices

### 1. Always Use Context Managers

```python
# Good
with sqlite3.connect('db.db') as conn:
    cursor = conn.cursor()
    # Use connection

# Less preferred
conn = sqlite3.connect('db.db')
# Use connection
conn.close()
```

### 2. Use Parameterized Queries

```python
# Good - prevents SQL injection
cursor.execute('SELECT * FROM users WHERE name = ?', (name,))

# Bad - vulnerable to SQL injection
cursor.execute(f'SELECT * FROM users WHERE name = "{name}"')
```

### 3. Handle Exceptions Properly

```python
try:
    # Database operations
    pass
except sqlite3.Error as e:
    # Handle error
    pass
```

### 4. Close Connections

```python
# Always close connections
conn.close()

# Or use context manager (automatic)
with sqlite3.connect('db.db') as conn:
    pass
```

### 5. Use Transactions

```python
# Group related operations in transactions
conn.begin()
try:
    # Multiple operations
    conn.commit()
except:
    conn.rollback()
```

---

## Common Mistakes to Avoid

1. **SQL Injection**
   ```python
   # Wrong - vulnerable
   cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")
   
   # Correct - safe
   cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
   ```

2. **Not closing connections**
   ```python
   # Wrong
   conn = sqlite3.connect('db.db')
   # Forgot to close
   
   # Correct
   with sqlite3.connect('db.db') as conn:
       pass
   ```

3. **Not handling exceptions**
   ```python
   # Wrong
   cursor.execute('SELECT * FROM users')
   
   # Correct
   try:
       cursor.execute('SELECT * FROM users')
   except sqlite3.Error as e:
       print(f"Error: {e}")
   ```

---

## Summary

- **Database connectivity** allows Python to work with databases
- **SQLite** is built-in and great for learning
- **Always use parameterized queries** to prevent SQL injection
- **Use context managers** for automatic connection management
- **Handle exceptions** properly
- **Use transactions** for data integrity
- **Close connections** when done

**Remember**: Always use parameterized queries and handle exceptions properly when working with databases!

---

## Next Steps

Now that you understand database connectivity:
1. Practice with the examples in this folder
2. Work with SQLite for simple projects
3. Learn about ORMs (Object-Relational Mappers) like SQLAlchemy
4. Move on to **27-web-scraping** to learn web scraping

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_database_basics.py`: Understanding database connectivity - start here!
2. `02_sqlite_connection.py`: Connecting to SQLite databases
3. `03_executing_queries.py`: Executing SELECT, INSERT, UPDATE, DELETE queries
4. `04_parameterized_queries.py`: Using parameterized queries safely
5. `05_transactions.py`: Working with transactions
6. `06_practical_examples.py`: Real-world database examples

Run these files in order to see database connectivity in action!

