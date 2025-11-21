"""
Reference Counting in Python

This file demonstrates how Python uses reference counting for memory management.
"""

import sys

# ============================================================================
# 1. WHAT IS REFERENCE COUNTING?
# ============================================================================
print("=" * 60)
print("1. WHAT IS REFERENCE COUNTING?")
print("=" * 60)

print("  Reference counting:")
print("    - Each object has a count of references to it")
print("    - When count reaches 0, object is deleted")
print("    - Primary memory management mechanism in Python")
print("    - Very efficient for most cases")

print()  # Empty line


# ============================================================================
# 2. HOW REFERENCE COUNTING WORKS
# ============================================================================
print("=" * 60)
print("2. HOW REFERENCE COUNTING WORKS")
print("=" * 60)

# Creating an object
x = "Hello"
print(f"  Created x = 'Hello'")
print(f"  Reference count: {sys.getrefcount(x)} (includes getrefcount's own reference)")

# Adding another reference
y = x
print(f"  Created y = x")
print(f"  Reference count: {sys.getrefcount(x)}")

# Adding more references
z = x
print(f"  Created z = x")
print(f"  Reference count: {sys.getrefcount(x)}")

# Removing references
del y
print(f"  Deleted y")
print(f"  Reference count: {sys.getrefcount(x)}")

del z
print(f"  Deleted z")
print(f"  Reference count: {sys.getrefcount(x)}")

del x
print(f"  Deleted x - object can now be garbage collected")

print()  # Empty line


# ============================================================================
# 3. REFERENCE COUNTING WITH DIFFERENT OBJECTS
# ============================================================================
print("=" * 60)
print("3. REFERENCE COUNTING WITH DIFFERENT OBJECTS")
print("=" * 60)

# Integers (small integers are cached)
a = 42
b = 42
print(f"  a = 42, reference count: {sys.getrefcount(a)}")
print(f"  b = 42, reference count: {sys.getrefcount(b)}")
print(f"  Note: Small integers are cached, so count is higher")

# Strings
s1 = "Hello"
s2 = "Hello"
print(f"  s1 = 'Hello', reference count: {sys.getrefcount(s1)}")
print(f"  s2 = 'Hello', reference count: {sys.getrefcount(s2)}")

# Lists (each list is a new object)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f"  list1 = [1, 2, 3], reference count: {sys.getrefcount(list1)}")
print(f"  list2 = [1, 2, 3], reference count: {sys.getrefcount(list2)}")
print(f"  Note: Different objects, so different counts")

print()  # Empty line


# ============================================================================
# 4. REFERENCE COUNTING IN FUNCTIONS
# ============================================================================
print("=" * 60)
print("4. REFERENCE COUNTING IN FUNCTIONS")
print("=" * 60)

def show_ref_count(obj, name):
    """Function that receives a reference to an object"""
    print(f"  {name} reference count inside function: {sys.getrefcount(obj)}")

data = [1, 2, 3]
print(f"  data reference count before function: {sys.getrefcount(data)}")
show_ref_count(data, "data")
print(f"  data reference count after function: {sys.getrefcount(data)}")
print("  Note: Function parameter creates temporary reference")

print()  # Empty line


# ============================================================================
# 5. REFERENCE COUNTING WITH NESTED STRUCTURES
# ============================================================================
print("=" * 60)
print("5. REFERENCE COUNTING WITH NESTED STRUCTURES")
print("=" * 60)

# List containing references to other objects
inner_list = [1, 2, 3]
outer_list = [inner_list, inner_list]
print(f"  inner_list reference count: {sys.getrefcount(inner_list)}")
print(f"  outer_list contains 2 references to inner_list")

# Dictionary with references
my_dict = {'a': inner_list, 'b': inner_list}
print(f"  inner_list reference count after adding to dict: {sys.getrefcount(inner_list)}")

# Removing from outer structure
del outer_list
print(f"  After deleting outer_list, inner_list count: {sys.getrefcount(inner_list)}")

print()  # Empty line


# ============================================================================
# 6. CIRCULAR REFERENCES
# ============================================================================
print("=" * 60)
print("6. CIRCULAR REFERENCES")
print("=" * 60)

class Node:
    """Simple node class for demonstrating circular references"""
    def __init__(self, value):
        self.value = value
        self.next = None

# Create circular reference
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node2.next = node1  # Circular reference!

print(f"  node1 reference count: {sys.getrefcount(node1)}")
print(f"  node2 reference count: {sys.getrefcount(node2)}")
print("  Circular reference prevents reference counting from freeing objects")
print("  Garbage collector handles this case")

# Break circular reference
node1.next = None
node2.next = None
print("  Breaking circular reference allows cleanup")

print()  # Empty line


# ============================================================================
# 7. REFERENCE COUNTING LIMITATIONS
# ============================================================================
print("=" * 60)
print("7. REFERENCE COUNTING LIMITATIONS")
print("=" * 60)

print("  Reference counting limitations:")
print("    - Cannot handle circular references")
print("    - Overhead of maintaining counts")
print("    - Not thread-safe (in older Python versions)")
print("  ")
print("  Solutions:")
print("    - Garbage collector handles circular references")
print("    - Overhead is minimal for most applications")
print("    - Modern Python has thread-safe reference counting")

print()  # Empty line


# ============================================================================
# 8. WHEN OBJECTS ARE DELETED
# ============================================================================
print("=" * 60)
print("8. WHEN OBJECTS ARE DELETED")
print("=" * 60)

class TrackedObject:
    """Object that prints when deleted"""
    def __init__(self, name):
        self.name = name
        print(f"  Created {self.name}")
    
    def __del__(self):
        print(f"  Deleted {self.name}")

print("  Creating objects:")
obj1 = TrackedObject("obj1")
obj2 = TrackedObject("obj2")
obj3 = obj1  # Another reference

print("  Deleting references:")
del obj2  # Should delete obj2
del obj1  # Won't delete yet (obj3 still references it)
print("  obj3 still exists, so obj1's object is not deleted yet")
del obj3  # Now obj1's object can be deleted

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("REFERENCE COUNTING SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Each object has a reference count")
print("  - Count increases when new reference is created")
print("  - Count decreases when reference is deleted")
print("  - Object is deleted when count reaches 0")
print("  - Use sys.getrefcount() to check reference count")
print("  - Circular references require garbage collector")
print("  - Primary memory management mechanism in Python")
print("=" * 60)

