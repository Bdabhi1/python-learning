# Python Best Practices

Writing clean, maintainable, and efficient Python code requires following best practices and conventions. This guide covers coding standards, style guides, and best practices for Python development.

## Table of Contents
1. [Code Style and PEP 8](#code-style-and-pep-8)
2. [Naming Conventions](#naming-conventions)
3. [Code Organization](#code-organization)
4. [Documentation](#documentation)
5. [Error Handling](#error-handling)
6. [Performance](#performance)
7. [Security](#security)
8. [Testing](#testing)
9. [Version Control](#version-control)

---

## Code Style and PEP 8

**PEP 8** is Python's official style guide. Following it makes code more readable and consistent.

### Indentation

```python
# Use 4 spaces (not tabs)
def function():
    if condition:
        do_something()
```

### Line Length

```python
# Maximum 79 characters per line
# For comments: 72 characters

# Break long lines
result = function_name(
    argument1,
    argument2,
    argument3
)
```

### Blank Lines

```python
# Two blank lines between top-level functions/classes
def function1():
    pass


def function2():
    pass

# One blank line between methods
class MyClass:
    def method1(self):
        pass
    
    def method2(self):
        pass
```

### Imports

```python
# Standard library imports
import os
import sys

# Third-party imports
import requests
import numpy

# Local application imports
from my_package import module
```

### Whitespace

```python
# Good
x = 1
y = 2
result = x + y

# Bad
x=1
y=2
result=x+y

# Good
if x == 5:
    pass

# Bad
if x==5:
    pass
```

---

## Naming Conventions

### Variables and Functions

```python
# Use lowercase with underscores
user_name = "John"
def calculate_total():
    pass
```

### Constants

```python
# Use uppercase with underscores
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30
```

### Classes

```python
# Use CamelCase
class UserAccount:
    pass

class DatabaseConnection:
    pass
```

### Private Variables

```python
# Single underscore for "internal use"
_internal_variable = 10

# Double underscore for name mangling
__private_variable = 20
```

### Special Methods

```python
# Use double underscores
class MyClass:
    def __init__(self):
        pass
    
    def __str__(self):
        return "MyClass"
```

---

## Code Organization

### Module Structure

```python
"""
Module docstring describing the module.
"""

# Imports
import os
import sys

# Constants
DEFAULT_VALUE = 10

# Classes
class MyClass:
    pass

# Functions
def my_function():
    pass

# Main execution
if __name__ == '__main__':
    main()
```

### Function Design

```python
# Good - Single responsibility
def calculate_total(items):
    """Calculate total price of items."""
    return sum(item.price for item in items)

# Bad - Multiple responsibilities
def process_order(order):
    validate_order(order)
    calculate_total(order.items)
    send_email(order.customer)
    update_inventory(order.items)
```

### Avoid Deep Nesting

```python
# Bad - Too nested
if condition1:
    if condition2:
        if condition3:
            do_something()

# Good - Early returns
if not condition1:
    return
if not condition2:
    return
if not condition3:
    return
do_something()
```

---

## Documentation

### Docstrings

```python
def function(param1, param2):
    """
    Brief description of function.
    
    Longer description if needed.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: When param1 is invalid
    """
    pass
```

### Comments

```python
# Good - Explain why, not what
# Use binary search for O(log n) performance
result = binary_search(items, target)

# Bad - Obvious comment
# Increment counter
counter += 1
```

### Type Hints

```python
from typing import List, Optional

def process_items(items: List[str]) -> Optional[int]:
    """Process list of items."""
    if not items:
        return None
    return len(items)
```

---

## Error Handling

### Use Specific Exceptions

```python
# Good
try:
    value = int(user_input)
except ValueError:
    print("Invalid number")

# Bad
try:
    value = int(user_input)
except Exception:
    print("Error")
```

### Don't Suppress Exceptions

```python
# Bad
try:
    risky_operation()
except:
    pass  # Silent failure

# Good
try:
    risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    handle_error(e)
```

### Use Context Managers

```python
# Good
with open('file.txt') as f:
    content = f.read()

# Bad
f = open('file.txt')
content = f.read()
f.close()  # Might not execute if exception occurs
```

---

## Performance

### Use List Comprehensions

```python
# Good
squares = [x**2 for x in range(10)]

# Less efficient
squares = []
for x in range(10):
    squares.append(x**2)
```

### Avoid Premature Optimization

```python
# Write clear code first
# Optimize only when needed and profiled
```

### Use Generators for Large Data

```python
# Good - Memory efficient
def process_large_file(filename):
    with open(filename) as f:
        for line in f:
            yield process(line)

# Less efficient
def process_large_file(filename):
    with open(filename) as f:
        return [process(line) for line in f]
```

### Cache Expensive Operations

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_function(n):
    # Expensive computation
    return result
```

---

## Security

### Input Validation

```python
# Always validate user input
def process_user_input(user_input):
    if not isinstance(user_input, str):
        raise TypeError("Input must be string")
    if len(user_input) > MAX_LENGTH:
        raise ValueError("Input too long")
    return sanitize(user_input)
```

### Avoid eval() and exec()

```python
# Dangerous
result = eval(user_input)

# Safe
result = json.loads(user_input)
```

### Use Parameterized Queries

```python
# Good - Prevents SQL injection
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

# Bad - Vulnerable
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
```

### Don't Hardcode Secrets

```python
# Bad
api_key = "secret-key-12345"

# Good
import os
api_key = os.getenv('API_KEY')
```

---

## Testing

### Write Tests

```python
import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)
```

### Test Edge Cases

```python
def test_edge_cases():
    # Empty input
    assert process([]) == []
    
    # Single item
    assert process([1]) == [1]
    
    # Large input
    assert len(process(range(10000))) == 10000
```

### Use pytest

```python
# pytest is more Pythonic
def test_function():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

---

## Version Control

### .gitignore

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
*.egg-info/
dist/
build/
```

### Meaningful Commit Messages

```bash
# Good
git commit -m "Add user authentication feature"
git commit -m "Fix bug in data processing"

# Bad
git commit -m "update"
git commit -m "fix"
```

### Use Branches

```bash
# Create feature branch
git checkout -b feature/new-feature

# Work on feature
# Commit changes

# Merge to main
git checkout main
git merge feature/new-feature
```

---

## Best Practices Summary

### DO

- ✅ Follow PEP 8 style guide
- ✅ Write clear, readable code
- ✅ Use meaningful names
- ✅ Write docstrings
- ✅ Handle errors properly
- ✅ Write tests
- ✅ Use version control
- ✅ Keep functions small and focused
- ✅ Use type hints
- ✅ Validate input

### DON'T

- ❌ Use global variables unnecessarily
- ❌ Suppress exceptions silently
- ❌ Write overly complex code
- ❌ Ignore warnings
- ❌ Hardcode values
- ❌ Use eval() or exec()
- ❌ Skip documentation
- ❌ Mix tabs and spaces
- ❌ Ignore security concerns
- ❌ Commit secrets

---

## Common Mistakes to Avoid

1. **Mutable default arguments**
   ```python
   # Wrong
   def append_item(item, list=[]):
       list.append(item)
       return list
   
   # Correct
   def append_item(item, list=None):
       if list is None:
           list = []
       list.append(item)
       return list
   ```

2. **Not using enumerate()**
   ```python
   # Less Pythonic
   for i in range(len(items)):
       print(i, items[i])
   
   # Better
   for i, item in enumerate(items):
       print(i, item)
   ```

3. **String concatenation in loops**
   ```python
   # Inefficient
   result = ""
   for word in words:
       result += word
   
   # Efficient
   result = "".join(words)
   ```

---

## Summary

- **Follow PEP 8** for code style
- **Use meaningful names** for variables and functions
- **Write documentation** (docstrings and comments)
- **Handle errors** properly with specific exceptions
- **Write tests** for your code
- **Use version control** effectively
- **Validate input** and handle security
- **Optimize** only when necessary
- **Keep code simple** and readable

**Remember**: Code is read more often than written. Write code that others (and future you) can understand!

---

## Next Steps

Now that you understand Python best practices:
1. Apply these practices to your code
2. Use linters (flake8, pylint) to check code
3. Use formatters (black, autopep8) to format code
4. Write comprehensive tests
5. Document your code
6. Move on to **36-data-classes** to learn about data classes

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_code_style.py`: PEP 8 and code style - start here!
2. `02_naming_conventions.py`: Naming conventions and best practices
3. `03_code_organization.py`: Organizing code effectively
4. `04_documentation.py`: Writing good documentation
5. `05_error_handling.py`: Proper error handling
6. `06_practical_examples.py`: Real-world best practices examples

Run these files in order to see best practices in action!

