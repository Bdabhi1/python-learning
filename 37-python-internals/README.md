# Python Internals

Understanding Python's internals helps you write more efficient code and debug issues effectively. This guide covers how Python works under the hood, including the interpreter, object model, memory management, and execution model.

## Table of Contents
1. [What are Python Internals?](#what-are-python-internals)
2. [The Python Interpreter](#the-python-interpreter)
3. [Object Model](#object-model)
4. [Name Binding and Scopes](#name-binding-and-scopes)
5. [Execution Model](#execution-model)
6. [Bytecode and Compilation](#bytecode-and-compilation)
7. [GIL (Global Interpreter Lock)](#gil-global-interpreter-lock)
8. [Best Practices](#best-practices)

---

## What are Python Internals?

**Python internals** refer to how Python works at a low level - how code is executed, how objects are managed, and how the interpreter processes your code.

**Key concepts:**
- **Interpreter**: CPython, the reference implementation
- **Object Model**: Everything is an object
- **Name Binding**: How variables reference objects
- **Bytecode**: Intermediate representation of code
- **GIL**: Global Interpreter Lock

**Why learn internals?**
- **Performance**: Understand what makes code fast or slow
- **Debugging**: Better understand error messages
- **Optimization**: Write more efficient code
- **Understanding**: Know how Python really works

---

## The Python Interpreter

### CPython

**CPython** is the reference implementation of Python, written in C.

```python
# Python code
x = 42
print(x)

# CPython interprets this and executes it
```

### Interpreter Steps

1. **Lexical Analysis**: Tokenizes source code
2. **Parsing**: Creates Abstract Syntax Tree (AST)
3. **Compilation**: Converts AST to bytecode
4. **Execution**: Python Virtual Machine (PVM) executes bytecode

### Python Virtual Machine (PVM)

The PVM executes bytecode instructions. It's a stack-based virtual machine.

---

## Object Model

### Everything is an Object

In Python, everything is an object - integers, strings, functions, classes, modules.

```python
# Everything is an object
x = 42
print(type(x))  # <class 'int'>
print(id(x))    # Memory address

def func():
    pass

print(type(func))  # <class 'function'>
```

### Object Identity

```python
# id() returns object identity (memory address)
x = 42
y = 42
print(id(x) == id(y))  # May be True (small integers are cached)

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a) == id(b))  # False (different objects)
```

### Type and isinstance

```python
# type() returns exact type
print(type(42))  # <class 'int'>

# isinstance() checks type hierarchy
print(isinstance(42, int))      # True
print(isinstance(42, object))   # True
```

---

## Name Binding and Scopes

### Names are References

```python
# Names are references to objects
x = [1, 2, 3]  # x references a list object
y = x          # y references the same object
y.append(4)
print(x)  # [1, 2, 3, 4] - both reference same object
```

### Scope Resolution (LEGB)

Python resolves names in this order:
1. **L**ocal
2. **E**nclosing (non-local)
3. **G**lobal
4. **B**uilt-in

```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)  # "local"
    
    inner()

outer()
```

### Global and Nonlocal

```python
x = "global"

def func():
    global x
    x = "modified"  # Modifies global x

def outer():
    x = "outer"
    
    def inner():
        nonlocal x
        x = "modified"  # Modifies outer's x
    
    inner()
    print(x)  # "modified"
```

---

## Execution Model

### Code Objects

```python
# Functions have code objects
def func():
    pass

print(func.__code__)
print(func.__code__.co_name)      # Function name
print(func.__code__.co_varnames)  # Local variables
print(func.__code__.co_consts)    # Constants
```

### Frame Objects

```python
import sys

def func():
    frame = sys._getframe()
    print(frame.f_code.co_name)  # Current function name
    print(frame.f_locals)        # Local variables

func()
```

### Execution Context

```python
# Each function call creates a new frame
def recursive(n):
    if n > 0:
        return recursive(n - 1)
    return sys._getframe()

frame = recursive(5)
print(frame.f_code.co_name)  # "recursive"
```

---

## Bytecode and Compilation

### Viewing Bytecode

```python
import dis

def add(a, b):
    return a + b

dis.dis(add)
# Output shows bytecode instructions
```

### Compilation Process

```python
# Source code -> AST -> Bytecode -> Execution

import ast

code = "x = 1 + 2"
tree = ast.parse(code)
print(ast.dump(tree))
```

### .pyc Files

Python compiles `.py` files to `.pyc` (bytecode) files for faster loading.

```python
# Python automatically creates __pycache__/ directory
# with .pyc files
```

---

## GIL (Global Interpreter Lock)

### What is the GIL?

The **Global Interpreter Lock** is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecode simultaneously.

### GIL Impact

```python
# CPU-bound tasks: GIL limits parallelism
# I/O-bound tasks: GIL released during I/O

import threading

# CPU-bound: Limited by GIL
def cpu_task():
    total = sum(i**2 for i in range(1000000))

# I/O-bound: GIL released during I/O
def io_task():
    import time
    time.sleep(1)  # GIL released
```

### Bypassing the GIL

- **Multiprocessing**: Separate processes (no shared GIL)
- **C Extensions**: Release GIL in C code
- **NumPy/SciPy**: Operations release GIL

---

## Memory Management

### Reference Counting

```python
import sys

x = [1, 2, 3]
print(sys.getrefcount(x))  # Reference count (includes getrefcount's reference)
```

### Garbage Collection

```python
import gc

# Automatic garbage collection
gc.collect()  # Force collection

# View statistics
print(gc.get_stats())
```

### Object Lifecycle

```python
class MyClass:
    def __init__(self):
        print("Object created")
    
    def __del__(self):
        print("Object deleted")

obj = MyClass()
del obj  # Triggers __del__
```

---

## Special Methods

### Magic Methods

```python
class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"MyClass({self.value})"
    
    def __repr__(self):
        return f"MyClass(value={self.value!r})"
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __hash__(self):
        return hash(self.value)
```

### Attribute Access

```python
class MyClass:
    def __getattr__(self, name):
        return f"Attribute {name} not found"
    
    def __setattr__(self, name, value):
        super().__setattr__(name, value)
    
    def __delattr__(self, name):
        super().__delattr__(name)
```

---

## Best Practices

### 1. Understand Object Identity

```python
# Use 'is' for identity, '==' for equality
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)  # True (same values)
print(x is y)   # False (different objects)
```

### 2. Be Aware of GIL Limitations

```python
# Use multiprocessing for CPU-bound tasks
from multiprocessing import Process

# Use threading for I/O-bound tasks
import threading
```

### 3. Understand Scope

```python
# Know LEGB rule
# Use global/nonlocal when needed
```

### 4. Use __slots__ for Memory Efficiency

```python
class Point:
    __slots__ = ['x', 'y']  # Reduces memory usage
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

### 5. Profile Before Optimizing

```python
import cProfile

def my_function():
    # Code to profile
    pass

cProfile.run('my_function()')
```

---

## Common Mistakes to Avoid

1. **Confusing identity and equality**
   ```python
   # Wrong assumption
   x = [1, 2, 3]
   y = [1, 2, 3]
   assert x is y  # Fails!
   
   # Correct
   assert x == y  # True
   ```

2. **Not understanding GIL**
   ```python
   # Threading won't speed up CPU-bound tasks
   # Use multiprocessing instead
   ```

3. **Modifying during iteration**
   ```python
   # Dangerous
   items = [1, 2, 3]
   for item in items:
       items.remove(item)  # Can cause issues
   ```

---

## Summary

- **Python internals** explain how Python works under the hood
- **Everything is an object** in Python
- **Names are references** to objects
- **LEGB rule** for scope resolution
- **Bytecode** is intermediate representation
- **GIL** limits thread parallelism for CPU-bound tasks
- **Reference counting** is primary memory management
- **Understanding internals** helps write better code

**Remember**: Understanding Python internals helps you write more efficient code and debug issues effectively!

---

## Next Steps

Now that you understand Python internals:
1. Explore bytecode with `dis` module
2. Profile your code to find bottlenecks
3. Understand when to use threading vs multiprocessing
4. Study object model and special methods
5. Move on to **38-projects** to apply your knowledge

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_python_interpreter.py`: Understanding the Python interpreter - start here!
2. `02_object_model.py`: Python's object model
3. `03_name_binding.py`: Name binding and scopes
4. `04_execution_model.py`: Execution model and frames
5. `05_bytecode.py`: Bytecode and compilation
6. `06_practical_examples.py`: Real-world internals examples

Run these files in order to see Python internals in action!

