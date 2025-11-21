# Working with CSV in Python

CSV (Comma-Separated Values) is a simple file format for storing tabular data. Python's `csv` module provides easy-to-use functions for reading and writing CSV files, making it simple to work with spreadsheet-like data.

## Table of Contents
1. [What is CSV?](#what-is-csv)
2. [The `csv` Module](#the-csv-module)
3. [Reading CSV Files](#reading-csv-files)
4. [Writing CSV Files](#writing-csv-files)
5. [CSV Dialects](#csv-dialects)
6. [Working with Dictionaries](#working-with-dictionaries)
7. [Handling Headers](#handling-headers)
8. [Error Handling](#error-handling)
9. [Best Practices](#best-practices)

---

## What is CSV?

**CSV** is a simple text format for storing tabular data:
- **Rows**: Each line is a row
- **Columns**: Values separated by commas (or other delimiters)
- **Headers**: First row often contains column names
- **Widely used**: Compatible with Excel, databases, and data analysis tools

**Example CSV:**
```csv
name,age,city
Alice,30,New York
Bob,25,London
Charlie,35,Paris
```

---

## The `csv` Module

Python's `csv` module provides functions for working with CSV files.

### Main Functions

- `csv.reader()`: Read CSV file row by row
- `csv.writer()`: Write CSV file row by row
- `csv.DictReader()`: Read CSV as dictionary
- `csv.DictWriter()`: Write CSV from dictionary

---

## Reading CSV Files

### Basic Reading

```python
import csv

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

### Reading with Headers

```python
import csv

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)  # Skip header row
    for row in reader:
        print(row)
```

### Reading All Rows

```python
import csv

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)
    print(rows)
```

---

## Writing CSV Files

### Basic Writing

```python
import csv

data = [
    ['name', 'age', 'city'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'London']
]

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
```

### Writing Row by Row

```python
import csv

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'city'])
    writer.writerow(['Alice', '30', 'New York'])
    writer.writerow(['Bob', '25', 'London'])
```

**Note:** Always use `newline=''` when opening CSV files for writing to avoid extra blank lines.

---

## CSV Dialects

CSV files can use different delimiters and formats.

### Custom Delimiter

```python
import csv

# Tab-separated values
with open('data.tsv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        print(row)
```

### Custom Quote Character

```python
import csv

with open('data.csv', 'r') as f:
    reader = csv.reader(f, quotechar='"')
    for row in reader:
        print(row)
```

### Common Dialects

```python
import csv

# Excel dialect
reader = csv.reader(f, dialect='excel')

# Unix dialect
reader = csv.reader(f, dialect='unix')
```

---

## Working with Dictionaries

### DictReader

```python
import csv

with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['age'])
```

### DictWriter

```python
import csv

data = [
    {'name': 'Alice', 'age': '30', 'city': 'New York'},
    {'name': 'Bob', 'age': '25', 'city': 'London'}
]

with open('output.csv', 'w', newline='') as f:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
```

---

## Handling Headers

### Reading Headers

```python
import csv

with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    headers = reader.fieldnames
    print(headers)  # ['name', 'age', 'city']
```

### Writing Headers

```python
import csv

with open('output.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age', 'city'])
    writer.writeheader()  # Write header row
    writer.writerow({'name': 'Alice', 'age': '30', 'city': 'New York'})
```

---

## Error Handling

### Handling Missing Files

```python
import csv

try:
    with open('data.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("File not found")
```

### Handling Invalid Data

```python
import csv

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        try:
            # Process row
            pass
        except Exception as e:
            print(f"Error in row {i}: {e}")
```

---

## Best Practices

### 1. Always Use Context Managers

```python
# Good
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    # Process file

# Less preferred
f = open('data.csv', 'r')
reader = csv.reader(f)
# Process file
f.close()
```

### 2. Use `newline=''` for Writing

```python
# Correct
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)

# May cause issues
with open('output.csv', 'w') as f:
    writer = csv.writer(f)
```

### 3. Use DictReader/DictWriter for Named Columns

```python
# Better for named columns
reader = csv.DictReader(f)

# Less clear
reader = csv.reader(f)
headers = next(reader)
```

### 4. Handle Encoding

```python
# For non-ASCII characters
with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
```

---

## Common Mistakes to Avoid

1. **Forgetting `newline=''` when writing**
   ```python
   # Wrong - may add extra blank lines
   with open('output.csv', 'w') as f:
       writer = csv.writer(f)
   
   # Correct
   with open('output.csv', 'w', newline='') as f:
       writer = csv.writer(f)
   ```

2. **Not handling headers properly**
   ```python
   # Wrong - includes header in data
   reader = csv.reader(f)
   for row in reader:
       process(row)
   
   # Correct
   reader = csv.reader(f)
   headers = next(reader)
   for row in reader:
       process(row)
   ```

3. **Not handling encoding**
   ```python
   # May fail with non-ASCII
   with open('data.csv', 'r') as f:
       reader = csv.reader(f)
   
   # Better
   with open('data.csv', 'r', encoding='utf-8') as f:
       reader = csv.reader(f)
   ```

---

## Summary

- **CSV** is a simple format for tabular data
- Use `csv.reader()` to read CSV files
- Use `csv.writer()` to write CSV files
- Use `csv.DictReader()` for named columns
- Use `csv.DictWriter()` to write from dictionaries
- Always use `newline=''` when writing
- Handle encoding for non-ASCII characters

**Remember**: CSV is perfect for simple tabular data. For complex data, consider JSON or databases!

---

## Next Steps

Now that you understand CSV:
1. Practice with the examples in this folder
2. Work with CSV data from spreadsheets
3. Process CSV files for data analysis
4. Move on to **25-functional-programming** to learn functional programming concepts

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_csv_basics.py`: Understanding CSV and the csv module - start here!
2. `02_reading_csv.py`: Reading CSV files with csv.reader
3. `03_writing_csv.py`: Writing CSV files with csv.writer
4. `04_dict_reader_writer.py`: Using DictReader and DictWriter
5. `05_csv_dialects.py`: Working with different CSV formats
6. `06_practical_examples.py`: Real-world CSV examples and patterns

Run these files in order to see CSV handling in action!

