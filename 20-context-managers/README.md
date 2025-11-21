# Context Managers in Python

Context managers provide a clean way to manage resources, ensuring proper setup and teardown. They're essential for file handling, database connections, and any resource that needs cleanup.

## Table of Contents
1. [What are Context Managers?](#what-are-context-managers)
2. [The `with` Statement](#the-with-statement)
3. [Built-in Context Managers](#built-in-context-managers)
4. [Creating Custom Context Managers](#creating-custom-context-managers)
5. [Context Manager Protocol](#context-manager-protocol)
6. [Contextlib Module](#contextlib-module)
7. [Nested Context Managers](#nested-context-managers)
8. [Best Practices](#best-practices)

---

## What are Context Managers?

**Context managers** are objects that define what happens before and after a block of code runs. They ensure proper resource management and cleanup.

**Key concepts:**
- Use `with` statement to enter and exit context
- Automatically handle setup and teardown
- Guarantee cleanup even if exceptions occur
- Follow the context manager protocol

**Benefits:**
- **Automatic cleanup**: Resources are always released
- **Exception safety**: Cleanup happens even on errors
- **Clean code**: No need for try-finally blocks
- **Resource management**: Perfect for files, locks, connections

---

## The `with` Statement

The `with` statement is used to enter a context manager's context.

### Basic Usage

```python
with open('file.txt', 'r') as f:
    content = f.read()
    # File is automatically closed when block exits
```

### How It Works

```python
# This:
with expression as variable:
    # code block

# Is equivalent to:
manager = expression
variable = manager.__enter__()
try:
    # code block
finally:
    manager.__exit__()
```

---

## Built-in Context Managers

### File Handling

```python
# Automatically closes file
with open('data.txt', 'r') as f:
    content = f.read()
    # File closed automatically
```

### Multiple Files

```python
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    data = infile.read()
    outfile.write(data)
```

---

## Creating Custom Context Managers

### Class-Based Context Manager

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False  # Don't suppress exceptions

# Usage
with FileManager('data.txt', 'r') as f:
    content = f.read()
```

### Context Manager for Timing

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, *args):
        self.end = time.time()
        print(f"Elapsed time: {self.end - self.start:.4f} seconds")

with Timer():
    time.sleep(1)
```

---

## Context Manager Protocol

Context managers must implement two methods:

### `__enter__()`

Called when entering the `with` block. Can return a value that's assigned to the variable after `as`.

```python
def __enter__(self):
    # Setup code
    return self  # or any value
```

### `__exit__(exc_type, exc_val, exc_tb)`

Called when exiting the `with` block, even if an exception occurred.

```python
def __exit__(self, exc_type, exc_val, exc_tb):
    # Cleanup code
    return False  # False = don't suppress exceptions
    # True = suppress exceptions
```

**Parameters:**
- `exc_type`: Exception type (None if no exception)
- `exc_val`: Exception value
- `exc_tb`: Exception traceback

---

## Contextlib Module

The `contextlib` module provides utilities for creating context managers.

### `@contextmanager` Decorator

```python
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

# Usage
with file_manager('data.txt', 'r') as f:
    content = f.read()
```

### `contextlib.suppress`

```python
from contextlib import suppress

# Suppress specific exceptions
with suppress(FileNotFoundError):
    os.remove('file.txt')
```

### `contextlib.redirect_stdout`

```python
from contextlib import redirect_stdout
import io

f = io.StringIO()
with redirect_stdout(f):
    print("This goes to StringIO")
content = f.getvalue()
```

### `contextlib.ExitStack`

```python
from contextlib import ExitStack

with ExitStack() as stack:
    files = [stack.enter_context(open(fname)) for fname in filenames]
    # All files opened and will be closed
```

---

## Nested Context Managers

You can nest multiple context managers.

### Multiple Resources

```python
with open('input.txt', 'r') as infile:
    with open('output.txt', 'w') as outfile:
        data = infile.read()
        outfile.write(data)
```

### Using Commas

```python
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    data = infile.read()
    outfile.write(data)
```

---

## Best Practices

### 1. Always Use Context Managers for Resources

```python
# Good
with open('file.txt', 'r') as f:
    content = f.read()

# Less preferred
f = open('file.txt', 'r')
content = f.read()
f.close()  # Might not execute if exception occurs
```

### 2. Handle Exceptions in `__exit__`

```python
def __exit__(self, exc_type, exc_val, exc_tb):
    # Cleanup code
    if exc_type is not None:
        # Handle exception
        pass
    return False  # Don't suppress
```

### 3. Use `@contextmanager` for Simple Cases

```python
from contextlib import contextmanager

@contextmanager
def simple_context():
    # Setup
    yield
    # Cleanup
```

### 4. Return Useful Values from `__enter__`

```python
def __enter__(self):
    self.resource = acquire_resource()
    return self.resource  # Return what user needs
```

---

## Common Mistakes to Avoid

1. **Not using context managers for resources**
   ```python
   # Bad
   file = open('data.txt')
   content = file.read()
   file.close()
   
   # Good
   with open('data.txt') as file:
       content = file.read()
   ```

2. **Suppressing exceptions incorrectly**
   ```python
   # Bad - suppresses all exceptions
   def __exit__(self, *args):
       return True  # Suppresses all!
   
   # Good - only suppress specific ones
   def __exit__(self, exc_type, exc_val, exc_tb):
       if exc_type == ValueError:
           return True  # Suppress only ValueError
       return False
   ```

3. **Not handling cleanup in finally**
   ```python
   # Bad
   def __exit__(self, *args):
       if no_error:
           cleanup()
   
   # Good
   def __exit__(self, *args):
       cleanup()  # Always cleanup
   ```

---

## Summary

- **Context managers** ensure proper resource management
- Use `with` statement to enter context
- Implement `__enter__()` and `__exit__()` methods
- Use `@contextmanager` decorator for simple cases
- Context managers guarantee cleanup even on exceptions
- Perfect for files, locks, database connections, etc.

**Remember**: Always use context managers for resources that need cleanup. They make your code safer and cleaner!

---

## Next Steps

Now that you understand context managers:
1. Practice with the examples in this folder
2. Create custom context managers for your use cases
3. Use context managers for all resource management
4. Move on to **21-regular-expressions** to learn pattern matching

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_basic_context_managers.py`: Understanding the `with` statement - start here!
2. `02_file_handling.py`: Using context managers with files
3. `03_custom_context_managers.py`: Creating custom context manager classes
4. `04_contextlib_module.py`: Using contextlib utilities
5. `05_nested_contexts.py`: Working with multiple context managers
6. `06_practical_examples.py`: Real-world context manager examples

Run these files in order to see context managers in action!

