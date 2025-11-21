"""
Memory Optimization Techniques in Python

This file demonstrates techniques to optimize memory usage.
"""

import sys

# ============================================================================
# 1. USE GENERATORS INSTEAD OF LISTS
# ============================================================================
print("=" * 60)
print("1. USE GENERATORS INSTEAD OF LISTS")
print("=" * 60)

# List comprehension - creates entire list in memory
def squares_list(n):
    """Creates entire list in memory"""
    return [i**2 for i in range(n)]

# Generator - generates values on demand
def squares_generator(n):
    """Generates values on demand"""
    for i in range(n):
        yield i**2

# Compare memory usage
n = 10000
list_result = squares_list(n)
gen_result = squares_generator(n)

print(f"  List size for {n} items: {sys.getsizeof(list_result)} bytes")
print(f"  Generator size: {sys.getsizeof(gen_result)} bytes")
print("  Generator uses much less memory!")

# Use generator expression
gen_expr = (i**2 for i in range(n))
print(f"  Generator expression size: {sys.getsizeof(gen_expr)} bytes")

print()  # Empty line


# ============================================================================
# 2. USE __SLOTS__ FOR CLASSES
# ============================================================================
print("=" * 60)
print("2. USE __SLOTS__ FOR CLASSES")
print("=" * 60)

# Regular class - uses __dict__ for attributes
class RegularPoint:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# Class with __slots__ - no __dict__, uses less memory
class SlotsPoint:
    __slots__ = ['x', 'y', 'z']
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# Compare memory usage
regular = RegularPoint(1, 2, 3)
slots = SlotsPoint(1, 2, 3)

print(f"  Regular class instance: {sys.getsizeof(regular)} bytes")
print(f"  Slots class instance: {sys.getsizeof(slots)} bytes")
print("  __slots__ uses less memory, especially with many instances")

# Create many instances
regular_points = [RegularPoint(i, i+1, i+2) for i in range(1000)]
slots_points = [SlotsPoint(i, i+1, i+2) for i in range(1000)]

print(f"  1000 regular instances: ~{sys.getsizeof(regular_points)} bytes")
print(f"  1000 slots instances: ~{sys.getsizeof(slots_points)} bytes")

print()  # Empty line


# ============================================================================
# 3. DELETE UNUSED OBJECTS
# ============================================================================
print("=" * 60)
print("3. DELETE UNUSED OBJECTS")
print("=" * 60)

# Create large object
large_data = [i for i in range(100000)]
print(f"  Created large_data, size: {sys.getsizeof(large_data)} bytes")

# Use it
total = sum(large_data)
print(f"  Sum: {total}")

# Delete when done
del large_data
print("  Deleted large_data - memory freed")
print("  Explicit deletion helps free memory immediately")

print()  # Empty line


# ============================================================================
# 4. USE WEAK REFERENCES
# ============================================================================
print("=" * 60)
print("4. USE WEAK REFERENCES")
print("=" * 60)

import weakref

class MyClass:
    def __init__(self, name):
        self.name = name
        print(f"    Created {self.name}")
    
    def __del__(self):
        print(f"    Deleted {self.name}")

# Regular reference
obj = MyClass("regular")
regular_ref = obj

# Weak reference
weak_ref = weakref.ref(obj)

print(f"  Regular reference: {regular_ref}")
print(f"  Weak reference: {weak_ref()}")

# Delete object
del obj
print("  Deleted obj")

# Check references
print(f"  Regular reference still exists: {regular_ref}")
print(f"  Weak reference: {weak_ref()}")  # None - object was deleted

print()  # Empty line


# ============================================================================
# 5. USE CONTEXT MANAGERS
# ============================================================================
print("=" * 60)
print("5. USE CONTEXT MANAGERS")
print("=" * 60)

# Context managers ensure proper cleanup
class Resource:
    def __init__(self, name):
        self.name = name
        print(f"    Opened {self.name}")
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"    Closed {self.name}")
        return False

# Using context manager
print("  Using context manager:")
with Resource("file.txt") as res:
    print(f"    Using {res.name}")
# Automatically closed here

print()  # Empty line


# ============================================================================
# 6. AVOID UNNECESSARY COPIES
# ============================================================================
print("=" * 60)
print("6. AVOID UNNECESSARY COPIES")
print("=" * 60)

# Original data
original = [i for i in range(10000)]
print(f"  Original list size: {sys.getsizeof(original)} bytes")

# Reference (no copy)
reference = original
print(f"  Reference size: {sys.getsizeof(reference)} bytes")
print("  Reference uses no extra memory")

# Copy (uses memory)
copy = original.copy()
print(f"  Copy size: {sys.getsizeof(copy)} bytes")
print("  Copy uses additional memory - only create if needed")

print()  # Empty line


# ============================================================================
# 7. USE APPROPRIATE DATA STRUCTURES
# ============================================================================
print("=" * 60)
print("7. USE APPROPRIATE DATA STRUCTURES")
print("=" * 60)

size = 1000

# List - good for ordered, mutable sequences
list_data = list(range(size))
list_size = sys.getsizeof(list_data)

# Tuple - good for immutable sequences (slightly more efficient)
tuple_data = tuple(range(size))
tuple_size = sys.getsizeof(tuple_data)

# Set - good for unique items, fast membership testing
set_data = set(range(size))
set_size = sys.getsizeof(set_data)

print(f"  Memory usage for {size} items:")
print(f"    List: {list_size} bytes")
print(f"    Tuple: {tuple_size} bytes (slightly less)")
print(f"    Set: {set_size} bytes")
print("  Choose the right structure for your use case")

print()  # Empty line


# ============================================================================
# 8. LAZY EVALUATION
# ============================================================================
print("=" * 60)
print("8. LAZY EVALUATION")
print("=" * 60)

# Eager evaluation - creates all values
def eager_range(n):
    """Creates all values immediately"""
    return list(range(n))

# Lazy evaluation - generates on demand
def lazy_range(n):
    """Generates values on demand"""
    i = 0
    while i < n:
        yield i
        i += 1

# Compare
n = 1000000
print(f"  Creating range of {n} items:")

# Eager - uses memory immediately
eager_result = eager_range(n)
print(f"    Eager: {sys.getsizeof(eager_result)} bytes")

# Lazy - minimal memory
lazy_result = lazy_range(n)
print(f"    Lazy: {sys.getsizeof(lazy_result)} bytes")
print("    Lazy evaluation uses minimal memory")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("MEMORY OPTIMIZATION SUMMARY:")
print("=" * 60)
print("Key Techniques:")
print("  - Use generators instead of lists for large sequences")
print("  - Use __slots__ for classes with many instances")
print("  - Delete large objects explicitly when done")
print("  - Use weak references to avoid preventing garbage collection")
print("  - Use context managers for proper resource cleanup")
print("  - Avoid unnecessary copies of data")
print("  - Choose appropriate data structures")
print("  - Use lazy evaluation for large datasets")
print("=" * 60)

