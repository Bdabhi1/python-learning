# Working with JSON in Python

JSON (JavaScript Object Notation) is a lightweight data interchange format. Python's `json` module makes it easy to work with JSON data, allowing you to encode Python objects to JSON and decode JSON to Python objects.

## Table of Contents
1. [What is JSON?](#what-is-json)
2. [The `json` Module](#the-json-module)
3. [Encoding Python to JSON](#encoding-python-to-json)
4. [Decoding JSON to Python](#decoding-json-to-python)
5. [Reading and Writing JSON Files](#reading-and-writing-json-files)
6. [Pretty Printing JSON](#pretty-printing-json)
7. [Handling Complex Objects](#handling-complex-objects)
8. [Error Handling](#error-handling)
9. [Best Practices](#best-practices)

---

## What is JSON?

**JSON** is a text format for storing and exchanging data. It's:
- **Human-readable**: Easy to read and write
- **Language-independent**: Used across many programming languages
- **Lightweight**: Minimal syntax overhead
- **Commonly used**: Standard for APIs, configuration files, and data storage

**JSON Data Types:**
- String: `"text"`
- Number: `123` or `12.34`
- Boolean: `true` or `false`
- Null: `null`
- Array: `[1, 2, 3]`
- Object: `{"key": "value"}`

---

## The `json` Module

Python's `json` module provides functions for working with JSON.

### Main Functions

- `json.dumps()`: Convert Python object to JSON string
- `json.loads()`: Convert JSON string to Python object
- `json.dump()`: Write Python object to JSON file
- `json.load()`: Read JSON file to Python object

---

## Encoding Python to JSON

### Basic Encoding

```python
import json

# Python dictionary
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Convert to JSON string
json_string = json.dumps(data)
print(json_string)
# {"name": "Alice", "age": 30, "city": "New York"}
```

### Python to JSON Type Mapping

```python
import json

data = {
    "string": "text",
    "number": 42,
    "float": 3.14,
    "boolean": True,
    "null": None,
    "list": [1, 2, 3],
    "dict": {"key": "value"}
}

json_string = json.dumps(data)
print(json_string)
```

**Type Mapping:**
- `dict` → JSON object
- `list` → JSON array
- `str` → JSON string
- `int`, `float` → JSON number
- `True` → `true`
- `False` → `false`
- `None` → `null`

---

## Decoding JSON to Python

### Basic Decoding

```python
import json

json_string = '{"name": "Alice", "age": 30, "city": "New York"}'

# Convert JSON string to Python dict
data = json.loads(json_string)
print(data)
# {'name': 'Alice', 'age': 30, 'city': 'New York'}
```

### JSON to Python Type Mapping

```python
import json

json_string = '''
{
    "string": "text",
    "number": 42,
    "float": 3.14,
    "boolean": true,
    "null": null,
    "array": [1, 2, 3],
    "object": {"key": "value"}
}
'''

data = json.loads(json_string)
print(type(data["string"]))  # <class 'str'>
print(type(data["number"]))  # <class 'int'>
print(type(data["boolean"])) # <class 'bool'>
```

---

## Reading and Writing JSON Files

### Writing JSON to File

```python
import json

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Write to file
with open('data.json', 'w') as f:
    json.dump(data, f)
```

### Reading JSON from File

```python
import json

# Read from file
with open('data.json', 'r') as f:
    data = json.load(f)

print(data)
```

### Handling File Errors

```python
import json

try:
    with open('data.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
```

---

## Pretty Printing JSON

### Using `indent` Parameter

```python
import json

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "coding", "traveling"]
}

# Pretty print with indentation
json_string = json.dumps(data, indent=4)
print(json_string)
```

### Using `sort_keys` Parameter

```python
import json

data = {"z": 3, "a": 1, "b": 2}

# Sort keys alphabetically
json_string = json.dumps(data, sort_keys=True, indent=2)
print(json_string)
```

---

## Handling Complex Objects

### Custom Encoders

```python
import json
from datetime import datetime

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data = {
    "name": "Alice",
    "created": datetime.now()
}

json_string = json.dumps(data, cls=CustomEncoder)
```

### Custom Decoders

```python
import json
from datetime import datetime

def decode_datetime(dct):
    if 'created' in dct:
        dct['created'] = datetime.fromisoformat(dct['created'])
    return dct

json_string = '{"name": "Alice", "created": "2024-01-15T14:30:00"}'
data = json.loads(json_string, object_hook=decode_datetime)
```

---

## Error Handling

### JSONDecodeError

```python
import json

try:
    data = json.loads('{"invalid": json}')
except json.JSONDecodeError as e:
    print(f"JSON decode error: {e}")
    print(f"Error at position: {e.pos}")
```

### Handling Invalid JSON

```python
import json

def safe_json_loads(json_string):
    try:
        return json.loads(json_string)
    except json.JSONDecodeError:
        return None

result = safe_json_loads('invalid json')
if result is None:
    print("Invalid JSON")
```

---

## Best Practices

### 1. Always Use Context Managers

```python
# Good
with open('data.json', 'r') as f:
    data = json.load(f)

# Less preferred
f = open('data.json', 'r')
data = json.load(f)
f.close()
```

### 2. Validate JSON Before Processing

```python
import json

def is_valid_json(json_string):
    try:
        json.loads(json_string)
        return True
    except json.JSONDecodeError:
        return False
```

### 3. Use Pretty Printing for Debugging

```python
# Debugging
print(json.dumps(data, indent=2))

# Production (compact)
json_string = json.dumps(data)
```

### 4. Handle Missing Keys

```python
data = json.loads(json_string)
name = data.get('name', 'Unknown')  # Safe access
```

---

## Common Mistakes to Avoid

1. **Not handling JSONDecodeError**
   ```python
   # Wrong
   data = json.loads(json_string)  # May raise exception
   
   # Correct
   try:
       data = json.loads(json_string)
   except json.JSONDecodeError:
       # Handle error
   ```

2. **Confusing `dumps` and `dump`**
   ```python
   # dumps = dump string (returns string)
   json_string = json.dumps(data)
   
   # dump = dump to file (writes to file)
   json.dump(data, file)
   ```

3. **Not using `indent` for readability**
   ```python
   # Hard to read
   json.dumps(data)
   
   # Better
   json.dumps(data, indent=2)
   ```

---

## Summary

- **JSON** is a lightweight data interchange format
- Use `json.dumps()` to encode Python to JSON string
- Use `json.loads()` to decode JSON string to Python
- Use `json.dump()` to write JSON to file
- Use `json.load()` to read JSON from file
- Use `indent` parameter for pretty printing
- Always handle `JSONDecodeError` exceptions
- Use custom encoders/decoders for complex objects

**Remember**: JSON is the standard format for APIs and data exchange. Master it to work with modern applications!

---

## Next Steps

Now that you understand JSON:
1. Practice with the examples in this folder
2. Work with JSON APIs
3. Store configuration in JSON files
4. Move on to **24-working-with-csv** to learn CSV handling

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_json_basics.py`: Understanding JSON and the json module - start here!
2. `02_encoding_decoding.py`: Encoding Python to JSON and decoding JSON to Python
3. `03_json_files.py`: Reading and writing JSON files
4. `04_pretty_printing.py`: Formatting JSON for readability
5. `05_custom_encoders.py`: Handling complex objects with custom encoders
6. `06_practical_examples.py`: Real-world JSON examples and patterns

Run these files in order to see JSON handling in action!

