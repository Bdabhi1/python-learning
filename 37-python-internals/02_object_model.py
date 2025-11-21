"""
Python Object Model

This file demonstrates Python's object model - everything is an object.
"""

import sys

# ============================================================================
# 1. EVERYTHING IS AN OBJECT
# ============================================================================
print("=" * 60)
print("1. EVERYTHING IS AN OBJECT")
print("=" * 60)

print("  In Python, everything is an object:")
print("    - Numbers")
print("    - Strings")
print("    - Functions")
print("    - Classes")
print("    - Modules")

x = 42
print(f"  Integer: {x}, type: {type(x)}")

def func():
    pass
print(f"  Function: {func}, type: {type(func)}")

class MyClass:
    pass
print(f"  Class: {MyClass}, type: {type(MyClass)}")

print()  # Empty line


# ============================================================================
# 2. OBJECT IDENTITY
# ============================================================================
print("=" * 60)
print("2. OBJECT IDENTITY")
print("=" * 60)

x = 42
y = 42
print(f"  x = {x}, id: {id(x)}")
print(f"  y = {y}, id: {id(y)}")
print(f"  x is y: {x is y}")  # May be True (small integers cached)

a = [1, 2, 3]
b = [1, 2, 3]
print(f"  a = {a}, id: {id(a)}")
print(f"  b = {b}, id: {id(b)}")
print(f"  a is b: {a is b}")  # False (different objects)
print(f"  a == b: {a == b}")  # True (same values)

print()  # Empty line


# ============================================================================
# 3. TYPE AND isinstance
# ============================================================================
print("=" * 60)
print("3. TYPE AND isinstance")
print("=" * 60)

x = 42
print(f"  type(42): {type(x)}")
print(f"  isinstance(42, int): {isinstance(x, int)}")
print(f"  isinstance(42, object): {isinstance(x, object)}")

class Parent:
    pass

class Child(Parent):
    pass

obj = Child()
print(f"  isinstance(obj, Child): {isinstance(obj, Child)}")
print(f"  isinstance(obj, Parent): {isinstance(obj, Parent)}")
print(f"  isinstance(obj, object): {isinstance(obj, object)}")

print()  # Empty line


# ============================================================================
# 4. OBJECT ATTRIBUTES
# ============================================================================
print("=" * 60)
print("4. OBJECT ATTRIBUTES")
print("=" * 60)

class MyClass:
    def __init__(self):
        self.value = 42

obj = MyClass()
print(f"  obj.value: {obj.value}")
print(f"  hasattr(obj, 'value'): {hasattr(obj, 'value')}")
print(f"  getattr(obj, 'value'): {getattr(obj, 'value')}")

# Functions have attributes too
def func():
    pass

func.custom_attr = "test"
print(f"  func.custom_attr: {func.custom_attr}")

print()  # Empty line


# ============================================================================
# 5. REFERENCE COUNTING
# ============================================================================
print("=" * 60)
print("5. REFERENCE COUNTING")
print("=" * 60)

x = [1, 2, 3]
print(f"  Reference count of x: {sys.getrefcount(x)}")
# Note: getrefcount includes its own reference

y = x
print(f"  After y = x, refcount: {sys.getrefcount(x)}")

del y
print(f"  After del y, refcount: {sys.getrefcount(x)}")

print()  # Empty line


# ============================================================================
# 6. OBJECT METHODS
# ============================================================================
print("=" * 60)
print("6. OBJECT METHODS")
print("=" * 60)

x = [1, 2, 3]
print(f"  x.__class__: {x.__class__}")
print(f"  x.__dict__: {x.__dict__ if hasattr(x, '__dict__') else 'N/A'}")
print(f"  dir(x): {dir(x)[:5]}...")  # First 5 methods

print()  # Empty line


# ============================================================================
# 7. METACLASSES
# ============================================================================
print("=" * 60)
print("7. METACLASSES")
print("=" * 60)

print("  Classes are objects too, created by metaclasses:")
print(f"    type(int): {type(int)}")
print(f"    type(str): {type(str)}")
print(f"    type(MyClass): {type(MyClass)}")
print("  ")
print("  type is the default metaclass")

class MyClass:
    pass

print(f"  MyClass is instance of type: {isinstance(MyClass, type)}")

print()  # Empty line


# ============================================================================
# 8. OBJECT HIERARCHY
# ============================================================================
print("=" * 60)
print("8. OBJECT HIERARCHY")
print("=" * 60)

print("  All objects inherit from object:")
print(f"    int.__bases__: {int.__bases__}")
print(f"    str.__bases__: {str.__bases__}")
print(f"    list.__bases__: {list.__bases__}")
print("  ")
print("  Everything is ultimately an object")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("OBJECT MODEL SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Everything in Python is an object")
print("  - id() returns object identity")
print("  - 'is' checks identity, '==' checks equality")
print("  - type() and isinstance() check types")
print("  - Objects have attributes and methods")
print("  - Classes are objects (metaclasses)")
print("  - Everything inherits from object")
print("=" * 60)

