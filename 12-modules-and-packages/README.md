# Modules and Packages in Python

Modules and packages help organize code into reusable, maintainable units. Understanding how to use and create them is essential for writing professional Python programs.

## Table of Contents
1. [What are Modules?](#what-are-modules)
2. [Importing Modules](#importing-modules)
3. [Standard Library Modules](#standard-library-modules)
4. [Creating Your Own Modules](#creating-your-own-modules)
5. [Packages](#packages)
6. [Module Search Path](#module-search-path)
7. [Best Practices](#best-practices)

---

## What are Modules?

A **module** is a file containing Python definitions and statements. Modules allow you to:
- Organize code logically
- Reuse code across multiple programs
- Avoid naming conflicts
- Make code more maintainable

**Key concepts:**
- A module is just a `.py` file
- Can contain functions, classes, variables
- Can be imported and used in other programs
- Python has a large standard library of modules

**Example:**
```python
# math_module.py (a module)
def add(a, b):
    return a + b

# main.py (using the module)
import math_module
result = math_module.add(3, 5)
```

---

## Importing Modules

Python provides several ways to import modules.

### Basic Import

```python
import math
print(math.pi)  # 3.141592653589793
print(math.sqrt(16))  # 4.0
```

### Import with Alias

```python
import math as m
print(m.pi)
print(m.sqrt(16))
```

### Import Specific Items

```python
from math import pi, sqrt
print(pi)
print(sqrt(16))
```

### Import All (Not Recommended)

```python
from math import *
print(pi)
print(sqrt(16))
```

**Note:** `from module import *` is generally discouraged as it can cause naming conflicts.

---

## Standard Library Modules

Python comes with many built-in modules. Here are some commonly used ones:

### `math` - Mathematical Functions

```python
import math

math.pi          # 3.14159...
math.e           # 2.71828...
math.sqrt(16)    # 4.0
math.pow(2, 3)   # 8.0
math.ceil(4.3)   # 5
math.floor(4.7)  # 4
```

### `random` - Random Number Generation

```python
import random

random.randint(1, 10)      # Random integer between 1 and 10
random.choice(['a', 'b', 'c'])  # Random choice from list
random.shuffle([1, 2, 3])  # Shuffle list in place
```

### `datetime` - Date and Time

```python
from datetime import datetime, date, timedelta

now = datetime.now()
today = date.today()
tomorrow = today + timedelta(days=1)
```

### `os` - Operating System Interface

```python
import os

os.getcwd()           # Current working directory
os.listdir('.')       # List files in directory
os.path.exists('file.txt')  # Check if file exists
```

### `sys` - System-Specific Parameters

```python
import sys

sys.argv              # Command-line arguments
sys.path              # Module search path
sys.version           # Python version
```

### `json` - JSON Data Handling

```python
import json

data = {'name': 'Alice', 'age': 25}
json_str = json.dumps(data)  # Convert to JSON string
data = json.loads(json_str)  # Convert from JSON string
```

---

## Creating Your Own Modules

### Simple Module

Create a file `calculator.py`:

```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
```

Use it in another file:

```python
import calculator

result = calculator.add(5, 3)
print(result)  # 8
```

### Module with Variables

```python
# config.py
APP_NAME = "My Application"
VERSION = "1.0.0"
DEBUG = True
```

```python
import config
print(config.APP_NAME)
print(config.VERSION)
```

### `__name__` and `__main__`

```python
# my_module.py
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    # This code runs only when module is executed directly
    print(greet("World"))
```

---

## Packages

A **package** is a collection of modules organized in directories.

### Creating a Package

```
my_package/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
```

### Using Packages

```python
# Import from package
import my_package.module1
from my_package import module2
from my_package.subpackage import module3

# Import specific items
from my_package.module1 import function1
```

### `__init__.py`

The `__init__.py` file makes a directory a package:

```python
# my_package/__init__.py
from .module1 import function1
from .module2 import function2

__all__ = ['function1', 'function2']
```

---

## Module Search Path

Python searches for modules in these locations (in order):

1. Current directory
2. Directories in `PYTHONPATH`
3. Standard library directories
4. Site-packages directory

```python
import sys
print(sys.path)  # See all search paths
```

---

## Best Practices

### 1. Use Descriptive Module Names

```python
# Good
import user_authentication
import data_processing

# Less clear
import ua
import dp
```

### 2. Organize Imports

```python
# Standard library imports
import os
import sys

# Third-party imports
import requests
import numpy

# Local imports
from my_module import function1
```

### 3. Avoid Circular Imports

```python
# module_a.py
import module_b  # Don't do this if module_b imports module_a
```

### 4. Use `if __name__ == "__main__"`

```python
def main():
    # Main code here
    pass

if __name__ == "__main__":
    main()
```

### 5. Document Your Modules

```python
"""
This module provides utility functions for data processing.

Functions:
    process_data: Process input data
    validate_data: Validate input data
"""

def process_data(data):
    """Process the input data."""
    pass
```

---

## Common Mistakes to Avoid

1. **Circular imports**
   ```python
   # module_a.py
   import module_b
   
   # module_b.py
   import module_a  # Circular!
   ```

2. **Importing non-existent modules**
   ```python
   import non_existent_module  # ModuleNotFoundError
   ```

3. **Name conflicts**
   ```python
   from math import sqrt
   def sqrt(x):  # Overwrites imported sqrt!
       return x ** 0.5
   ```

4. **Not handling import errors**
   ```python
   try:
       import optional_module
   except ImportError:
       optional_module = None
   ```

---

## Summary

- **Modules** are `.py` files containing Python code
- Use `import` to use modules in your code
- Python has a rich **standard library** of modules
- Create your own modules to organize code
- **Packages** organize multiple modules in directories
- Use `__init__.py` to make directories packages
- Follow **best practices** for clean, maintainable code

**Remember**: Modules and packages are essential for organizing and reusing code. Master them to write professional Python programs!

---

## Next Steps

Now that you understand modules and packages:
1. Practice with the examples in this folder
2. Explore Python's standard library
3. Create your own modules
4. Move on to **13-file-handling** to learn about working with files

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_importing_modules.py`: How to import and use modules - start here!
2. `02_standard_library.py`: Using Python's standard library modules
3. `03_creating_modules.py`: Creating your own modules
4. `04_packages.py`: Working with packages
5. `05_module_attributes.py`: Understanding module attributes
6. `06_practical_examples.py`: Real-world module and package examples

Run these files in order to see modules and packages in action!

