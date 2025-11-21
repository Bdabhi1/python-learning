# Memory Management in Python

Understanding how Python manages memory is crucial for writing efficient programs and avoiding memory-related issues. This guide covers Python's memory management system, garbage collection, and best practices.

## Table of Contents
1. [What is Memory Management?](#what-is-memory-management)
2. [Python's Memory Model](#pythons-memory-model)
3. [Reference Counting](#reference-counting)
4. [Garbage Collection](#garbage-collection)
5. [Memory Profiling](#memory-profiling)
6. [Memory Optimization Techniques](#memory-optimization-techniques)
7. [Common Memory Issues](#common-memory-issues)
8. [Best Practices](#best-practices)

---

## What is Memory Management?

**Memory management** is how a programming language allocates and deallocates memory for objects during program execution.

**Key Concepts:**
- **Allocation**: Reserving memory for objects
- **Deallocation**: Freeing memory when objects are no longer needed
- **Garbage Collection**: Automatic memory cleanup
- **Memory Leaks**: Memory that's never freed

**Why It Matters:**
- **Performance**: Efficient memory use improves performance
- **Stability**: Prevents out-of-memory errors
- **Resource Management**: Proper cleanup of resources

---

## Python's Memory Model

Python manages memory automatically, but understanding how it works helps write better code.

### Object Storage

```python
# Objects are stored in memory
x = 42  # Integer object created in memory
y = "Hello"  # String object created in memory
z = [1, 2, 3]  # List object created in memory
```

### Memory Locations

```python
import sys

x = 42
print(id(x))  # Memory address of object
print(sys.getsizeof(x))  # Size in bytes
```

### Variable References

```python
# Variables are references to objects
a = [1, 2, 3]
b = a  # b references the same object
b.append(4)
print(a)  # [1, 2, 3, 4] - both reference same object
```

---

## Reference Counting

Python uses **reference counting** as its primary memory management mechanism.

### How Reference Counting Works

```python
# Each object has a reference count
x = "Hello"  # Reference count = 1
y = x        # Reference count = 2
z = x        # Reference count = 3

del y        # Reference count = 2
del z        # Reference count = 1
del x        # Reference count = 0 -> object deleted
```

### Viewing Reference Counts

```python
import sys

x = "Hello"
print(sys.getrefcount(x))  # Note: getrefcount includes its own reference
```

### Circular References

```python
# Circular references prevent reference counting from working
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

a = Node(1)
b = Node(2)
a.next = b
b.next = a  # Circular reference!

# Reference counting alone can't free these
# Garbage collector handles this
```

---

## Garbage Collection

Python's **garbage collector** handles objects that reference counting can't free.

### Automatic Garbage Collection

```python
import gc

# Garbage collection happens automatically
# But you can control it
gc.collect()  # Force garbage collection
```

### Garbage Collection Generations

Python uses a generational garbage collector with three generations:

```python
import gc

# View garbage collection statistics
print(gc.get_stats())

# Get count of objects in each generation
print(gc.get_count())

# Force collection of specific generation
gc.collect(0)  # Generation 0
gc.collect(1)  # Generation 1
gc.collect(2)  # Generation 2
```

### Disabling Garbage Collection

```python
import gc

# Disable automatic garbage collection (rarely needed)
gc.disable()

# Re-enable
gc.enable()
```

---

## Memory Profiling

Profiling helps identify memory usage and leaks.

### Using `sys.getsizeof()`

```python
import sys

# Get size of objects
print(sys.getsizeof(42))  # Integer size
print(sys.getsizeof("Hello"))  # String size
print(sys.getsizeof([1, 2, 3]))  # List size
```

### Using `tracemalloc`

```python
import tracemalloc

# Start tracking memory
tracemalloc.start()

# Your code here
data = [i for i in range(10000)]

# Get current memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current: {current / 1024 / 1024:.2f} MB")
print(f"Peak: {peak / 1024 / 1024:.2f} MB")

# Stop tracking
tracemalloc.stop()
```

### Using `memory_profiler` (External)

```python
# Install: pip install memory-profiler
from memory_profiler import profile

@profile
def my_function():
    data = [i for i in range(10000)]
    return sum(data)

my_function()
```

---

## Memory Optimization Techniques

### 1. Use Generators Instead of Lists

```python
# Memory efficient - generates values on demand
def squares_generator(n):
    for i in range(n):
        yield i ** 2

# Less memory efficient - creates entire list
def squares_list(n):
    return [i ** 2 for i in range(n)]
```

### 2. Use `__slots__` for Classes

```python
# Without __slots__ - uses more memory
class RegularClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# With __slots__ - uses less memory
class SlotsClass:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

### 3. Delete Unused Objects

```python
# Explicitly delete large objects when done
large_data = [i for i in range(1000000)]
# Use large_data...
del large_data  # Free memory immediately
```

### 4. Use Weak References

```python
import weakref

# Weak references don't prevent garbage collection
class MyClass:
    pass

obj = MyClass()
weak_ref = weakref.ref(obj)

print(weak_ref())  # <__main__.MyClass object at ...>
del obj
print(weak_ref())  # None - object was garbage collected
```

### 5. Use Context Managers

```python
# Context managers ensure proper cleanup
with open('file.txt', 'r') as f:
    data = f.read()
# File automatically closed, resources freed
```

---

## Common Memory Issues

### 1. Memory Leaks

```python
# Memory leak example - objects never freed
cache = {}

def process_data(data):
    # Objects added but never removed
    cache[id(data)] = data
    # Process data...
    # cache never cleared = memory leak
```

**Solution:**
```python
# Clear cache periodically
cache = {}
MAX_CACHE_SIZE = 1000

def process_data(data):
    if len(cache) > MAX_CACHE_SIZE:
        cache.clear()
    cache[id(data)] = data
```

### 2. Circular References

```python
# Circular references can prevent garbage collection
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []

parent = Node(1)
child = Node(2)
parent.children.append(child)
child.parent = parent  # Circular reference

# Solution: Use weak references
import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []
    
    def set_parent(self, parent):
        self.parent = weakref.ref(parent)
```

### 3. Large Data Structures

```python
# Creating large lists can consume memory
large_list = [i for i in range(10000000)]  # Uses significant memory

# Use generators instead
large_gen = (i for i in range(10000000))  # Minimal memory
```

### 4. Not Closing Resources

```python
# File not closed - memory leak
f = open('large_file.txt', 'r')
data = f.read()
# File handle not closed

# Solution: Use context manager
with open('large_file.txt', 'r') as f:
    data = f.read()
# Automatically closed
```

---

## Best Practices

### 1. Use Generators for Large Sequences

```python
# Good
def process_large_data():
    for item in range(1000000):
        yield process(item)

# Less efficient
def process_large_data():
    return [process(item) for item in range(1000000)]
```

### 2. Delete Large Objects Explicitly

```python
# Good
large_data = load_data()
process(large_data)
del large_data  # Free memory
```

### 3. Use `__slots__` for Many Small Objects

```python
# Good for classes with many instances
class Point:
    __slots__ = ['x', 'y', 'z']
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
```

### 4. Monitor Memory Usage

```python
import tracemalloc

tracemalloc.start()
# Your code
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')
for stat in top_stats[:10]:
    print(stat)
```

### 5. Use Weak References for Caching

```python
import weakref

# Weak reference cache
cache = weakref.WeakValueDictionary()

def get_data(key):
    if key not in cache:
        cache[key] = expensive_operation(key)
    return cache[key]
```

### 6. Avoid Unnecessary Copies

```python
# Good - no copy
data = [1, 2, 3]
reference = data

# Less efficient - creates copy
data = [1, 2, 3]
copy = data[:]  # Only if copy is needed
```

---

## Common Mistakes to Avoid

1. **Not deleting large objects**
   ```python
   # Wrong
   large_data = load_data()
   # Never deleted
   
   # Correct
   large_data = load_data()
   # Use it...
   del large_data
   ```

2. **Creating unnecessary copies**
   ```python
   # Wrong - creates copy
   new_list = old_list[:]
   
   # Correct - if copy needed
   new_list = old_list.copy()  # More explicit
   ```

3. **Not using generators for large sequences**
   ```python
   # Wrong
   squares = [x**2 for x in range(1000000)]
   
   # Correct
   squares = (x**2 for x in range(1000000))
   ```

4. **Circular references without cleanup**
   ```python
   # Wrong
   parent.children.append(child)
   child.parent = parent  # Circular reference
   
   # Correct - use weak references
   child.parent = weakref.ref(parent)
   ```

---

## Summary

- **Memory management** is automatic in Python but understanding it helps
- **Reference counting** is the primary mechanism
- **Garbage collection** handles circular references
- **Use generators** for large sequences
- **Use `__slots__`** for memory-efficient classes
- **Delete large objects** explicitly when done
- **Monitor memory usage** with profiling tools
- **Use weak references** for caching and avoiding circular references

**Remember**: Python manages memory automatically, but being mindful of memory usage helps write efficient programs!

---

## Next Steps

Now that you understand memory management:
1. Practice with the examples in this folder
2. Profile your applications for memory usage
3. Use generators for large data processing
4. Monitor memory in production applications

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_memory_basics.py`: Understanding Python's memory model - start here!
2. `02_reference_counting.py`: How reference counting works
3. `03_garbage_collection.py`: Garbage collection mechanisms
4. `04_memory_profiling.py`: Tools and techniques for profiling memory
5. `05_memory_optimization.py`: Techniques to optimize memory usage
6. `06_practical_examples.py`: Real-world memory management examples

Run these files in order to see memory management in action!

