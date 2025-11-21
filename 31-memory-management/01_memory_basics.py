"""
Memory Basics in Python

This file demonstrates the fundamental concepts of Python's memory management.
"""

import sys

# ============================================================================
# 1. WHAT IS MEMORY MANAGEMENT?
# ============================================================================
print("=" * 60)
print("1. WHAT IS MEMORY MANAGEMENT?")
print("=" * 60)

print("  Memory management is how Python:")
print("    - Allocates memory for objects")
print("    - Deallocates memory when objects are no longer needed")
print("    - Handles memory automatically (no manual memory management)")
print("    - Prevents memory leaks")

print()  # Empty line


# ============================================================================
# 2. OBJECT STORAGE IN MEMORY
# ============================================================================
print("=" * 60)
print("2. OBJECT STORAGE IN MEMORY")
print("=" * 60)

# Objects are stored in memory
x = 42
y = "Hello"
z = [1, 2, 3]

print(f"  Integer object: {x}")
print(f"  String object: {y}")
print(f"  List object: {z}")

print()  # Empty line


# ============================================================================
# 3. MEMORY ADDRESSES (ID)
# ============================================================================
print("=" * 60)
print("3. MEMORY ADDRESSES (ID)")
print("=" * 60)

# Every object has a unique memory address
x = 42
y = "Hello"
z = [1, 2, 3]

print(f"  ID of integer 42: {id(x)}")
print(f"  ID of string 'Hello': {id(y)}")
print(f"  ID of list [1, 2, 3]: {id(z)}")

# Same value may have same ID (for small integers/strings)
a = 42
b = 42
print(f"  ID of a (42): {id(a)}")
print(f"  ID of b (42): {id(b)}")
print(f"  Same ID? {id(a) == id(b)}")  # True for small integers

print()  # Empty line


# ============================================================================
# 4. OBJECT SIZE
# ============================================================================
print("=" * 60)
print("4. OBJECT SIZE")
print("=" * 60)

# Get size of objects in bytes
print(f"  Size of integer 42: {sys.getsizeof(42)} bytes")
print(f"  Size of string 'Hello': {sys.getsizeof('Hello')} bytes")
print(f"  Size of list [1, 2, 3]: {sys.getsizeof([1, 2, 3])} bytes")
print(f"  Size of empty list: {sys.getsizeof([])} bytes")
print(f"  Size of empty dict: {sys.getsizeof({})} bytes")

# Size grows with content
small_list = [1, 2, 3]
large_list = list(range(1000))
print(f"  Size of small list: {sys.getsizeof(small_list)} bytes")
print(f"  Size of large list: {sys.getsizeof(large_list)} bytes")

print()  # Empty line


# ============================================================================
# 5. VARIABLES AS REFERENCES
# ============================================================================
print("=" * 60)
print("5. VARIABLES AS REFERENCES")
print("=" * 60)

# Variables are references to objects in memory
a = [1, 2, 3]
b = a  # b references the same object

print(f"  a = {a}")
print(f"  b = {b}")
print(f"  id(a) == id(b): {id(a) == id(b)}")  # Same object

# Modifying through one reference affects the other
b.append(4)
print(f"  After b.append(4):")
print(f"  a = {a}")  # Also changed!
print(f"  b = {b}")

# Creating a copy creates a new object
c = a.copy()
print(f"  c = a.copy()")
print(f"  id(a) == id(c): {id(a) == id(c)}")  # Different objects
c.append(5)
print(f"  After c.append(5):")
print(f"  a = {a}")  # Unchanged
print(f"  c = {c}")  # Changed

print()  # Empty line


# ============================================================================
# 6. IMMUTABLE VS MUTABLE OBJECTS
# ============================================================================
print("=" * 60)
print("6. IMMUTABLE VS MUTABLE OBJECTS")
print("=" * 60)

# Immutable objects (int, str, tuple)
x = 42
print(f"  Integer x = 42, id: {id(x)}")
x = 43  # Creates new object
print(f"  Integer x = 43, id: {id(x)}")  # Different ID

# Mutable objects (list, dict, set)
y = [1, 2, 3]
print(f"  List y = [1, 2, 3], id: {id(y)}")
y.append(4)  # Modifies same object
print(f"  List y = [1, 2, 3, 4], id: {id(y)}")  # Same ID

print()  # Empty line


# ============================================================================
# 7. MEMORY ALLOCATION
# ============================================================================
print("=" * 60)
print("7. MEMORY ALLOCATION")
print("=" * 60)

# Python automatically allocates memory when creating objects
print("  Creating objects automatically allocates memory:")
data1 = [i for i in range(100)]
print(f"  Size of list with 100 items: {sys.getsizeof(data1)} bytes")

data2 = [i for i in range(1000)]
print(f"  Size of list with 1000 items: {sys.getsizeof(data2)} bytes")

# Memory is allocated as needed
print("  Python handles memory allocation automatically")

print()  # Empty line


# ============================================================================
# 8. MEMORY DEALLOCATION
# ============================================================================
print("=" * 60)
print("8. MEMORY DEALLOCATION")
print("=" * 60)

# Memory is deallocated when objects are no longer referenced
large_data = [i for i in range(10000)]
print(f"  Created large_data, size: {sys.getsizeof(large_data)} bytes")
print(f"  ID before deletion: {id(large_data)}")

del large_data  # Explicitly delete
print("  Deleted large_data - memory will be freed")
print("  Python's garbage collector handles deallocation")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("MEMORY BASICS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Objects are stored in memory with unique IDs")
print("  - Variables are references to objects")
print("  - Use id() to get memory address")
print("  - Use sys.getsizeof() to get object size")
print("  - Immutable objects create new objects when modified")
print("  - Mutable objects modify the same object")
print("  - Memory is allocated and deallocated automatically")
print("=" * 60)

