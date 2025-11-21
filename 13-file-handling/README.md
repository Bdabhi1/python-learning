# File Handling in Python

File handling allows your programs to read from and write to files, enabling data persistence and interaction with the file system. This guide covers everything you need to know about working with files in Python.

## Table of Contents
1. [What is File Handling?](#what-is-file-handling)
2. [Opening and Closing Files](#opening-and-closing-files)
3. [Reading from Files](#reading-from-files)
4. [Writing to Files](#writing-to-files)
5. [File Modes](#file-modes)
6. [Working with File Paths](#working-with-file-paths)
7. [Error Handling](#error-handling)
8. [Working with Different File Types](#working-with-different-file-types)
9. [Best Practices](#best-practices)

---

## What is File Handling?

**File handling** is the process of reading from and writing to files on your computer's storage system.

**Why use files?**
- **Data persistence**: Save data between program runs
- **Data exchange**: Share data between programs
- **Configuration**: Store settings and preferences
- **Logging**: Record program activity
- **Data processing**: Work with large datasets

**Common file operations:**
- Read data from files
- Write data to files
- Append data to existing files
- Check if files exist
- Delete files
- Navigate directories

---

## Opening and Closing Files

### Using `open()` Function

```python
# Open file for reading
file = open("data.txt", "r")
content = file.read()
file.close()  # Important: always close files
```

### Using `with` Statement (Recommended)

```python
# Automatically closes file when done
with open("data.txt", "r") as file:
    content = file.read()
# File is automatically closed here
```

**Why use `with`?**
- Automatically closes file
- Handles errors gracefully
- More Pythonic
- Prevents resource leaks

---

## Reading from Files

### Read Entire File

```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

### Read Line by Line

```python
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes newline
```

### Read All Lines into List

```python
with open("data.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
```

### Read Single Line

```python
with open("data.txt", "r") as file:
    first_line = file.readline()
    second_line = file.readline()
```

### Read with Size Limit

```python
with open("data.txt", "r") as file:
    chunk = file.read(100)  # Read first 100 characters
```

---

## Writing to Files

### Write to File

```python
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2.\n")
```

### Write Multiple Lines

```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)
```

### Append to File

```python
with open("output.txt", "a") as file:
    file.write("This line is appended.\n")
```

---

## File Modes

Python supports various file modes:

| Mode | Description |
|------|-------------|
| `'r'` | Read (default, file must exist) |
| `'w'` | Write (overwrites existing file) |
| `'a'` | Append (adds to end of file) |
| `'x'` | Exclusive creation (fails if file exists) |
| `'b'` | Binary mode (e.g., `'rb'`, `'wb'`) |
| `'t'` | Text mode (default) |
| `'+'` | Read and write (e.g., `'r+'`, `'w+'`) |

**Examples:**
```python
open("file.txt", "r")    # Read text file
open("file.txt", "w")    # Write text file
open("file.txt", "a")    # Append to text file
open("file.bin", "rb")   # Read binary file
open("file.bin", "wb")   # Write binary file
open("file.txt", "r+")   # Read and write
```

---

## Working with File Paths

### Absolute vs Relative Paths

```python
# Relative path (from current directory)
with open("data.txt", "r") as file:
    pass

# Absolute path
with open("/Users/username/data.txt", "r") as file:
    pass
```

### Using `os.path`

```python
import os

# Join paths (cross-platform)
path = os.path.join("folder", "subfolder", "file.txt")

# Get directory name
directory = os.path.dirname("/path/to/file.txt")

# Get filename
filename = os.path.basename("/path/to/file.txt")

# Check if path exists
if os.path.exists("file.txt"):
    print("File exists")
```

### Using `pathlib` (Python 3.4+)

```python
from pathlib import Path

# Create Path object
path = Path("folder") / "subfolder" / "file.txt"

# Check if exists
if path.exists():
    print("File exists")

# Read file
content = path.read_text()
```

---

## Error Handling

### File Not Found

```python
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
```

### Permission Errors

```python
try:
    with open("protected.txt", "w") as file:
        file.write("Hello")
except PermissionError:
    print("Permission denied!")
```

### General Exception Handling

```python
try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
except Exception as e:
    print(f"An error occurred: {e}")
```

---

## Working with Different File Types

### Text Files

```python
# Read text file
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Write text file
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello, World!")
```

### CSV Files

```python
import csv

# Read CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Write CSV
with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 25])
```

### JSON Files

```python
import json

# Read JSON
with open("data.json", "r") as file:
    data = json.load(file)

# Write JSON
data = {"name": "Alice", "age": 25}
with open("output.json", "w") as file:
    json.dump(data, file, indent=2)
```

### Binary Files

```python
# Read binary
with open("image.jpg", "rb") as file:
    data = file.read()

# Write binary
with open("copy.jpg", "wb") as file:
    file.write(data)
```

---

## Best Practices

### 1. Always Use `with` Statement

```python
# Good
with open("file.txt", "r") as file:
    content = file.read()

# Bad
file = open("file.txt", "r")
content = file.read()
file.close()  # Might forget to close
```

### 2. Handle Errors

```python
try:
    with open("file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
```

### 3. Specify Encoding for Text Files

```python
# Good
with open("file.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

### 4. Use Context Managers for Multiple Files

```python
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        outfile.write(line.upper())
```

### 5. Check File Existence

```python
import os

if os.path.exists("file.txt"):
    with open("file.txt", "r") as file:
        content = file.read()
else:
    print("File does not exist")
```

### 6. Use Appropriate File Modes

```python
# For reading
with open("file.txt", "r") as file:
    pass

# For writing (overwrites)
with open("file.txt", "w") as file:
    pass

# For appending
with open("file.txt", "a") as file:
    pass
```

---

## Common Mistakes to Avoid

1. **Forgetting to close files**
   ```python
   # Bad
   file = open("data.txt", "r")
   content = file.read()
   # Forgot file.close()
   
   # Good
   with open("data.txt", "r") as file:
       content = file.read()
   ```

2. **Not handling file errors**
   ```python
   # Bad
   with open("nonexistent.txt", "r") as file:
       content = file.read()  # FileNotFoundError!
   
   # Good
   try:
       with open("nonexistent.txt", "r") as file:
           content = file.read()
   except FileNotFoundError:
       print("File not found!")
   ```

3. **Using wrong file mode**
   ```python
   # Bad - tries to read non-existent file
   with open("newfile.txt", "r") as file:
       content = file.read()
   
   # Good - creates file for writing
   with open("newfile.txt", "w") as file:
       file.write("Hello")
   ```

4. **Not specifying encoding**
   ```python
   # May cause issues with special characters
   with open("file.txt", "r") as file:
       content = file.read()
   
   # Better
   with open("file.txt", "r", encoding="utf-8") as file:
       content = file.read()
   ```

---

## Summary

- **File handling** allows reading from and writing to files
- Always use **`with` statement** for automatic file closing
- Use appropriate **file modes** (`'r'`, `'w'`, `'a'`, etc.)
- **Handle errors** with try-except blocks
- Use **`os.path`** or **`pathlib`** for path operations
- Specify **encoding** for text files
- Different file types require different approaches (CSV, JSON, binary)

**Remember**: File handling is essential for data persistence. Master these techniques to create programs that can save and load data!

---

## Next Steps

Now that you understand file handling:
1. Practice with the examples in this folder
2. Work with different file types (CSV, JSON)
3. Create programs that save and load data
4. Move on to **14-exception-handling** to learn about error handling

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_reading_files.py`: Reading from files - start here!
2. `02_writing_files.py`: Writing to files
3. `03_file_modes.py`: Understanding different file modes
4. `04_file_paths.py`: Working with file paths
5. `05_error_handling.py`: Handling file errors
6. `06_practical_examples.py`: Real-world file handling examples

Run these files in order to see file handling in action!

