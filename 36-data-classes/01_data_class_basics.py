"""
Data Class Basics in Python

This file demonstrates the fundamental concepts of data classes.
"""

from dataclasses import dataclass

# ============================================================================
# 1. WHAT ARE DATA CLASSES?
# ============================================================================
print("=" * 60)
print("1. WHAT ARE DATA CLASSES?")
print("=" * 60)

print("  Data classes automatically generate special methods")
print("  like __init__(), __repr__(), and __eq__().")
print("  ")
print("  Benefits:")
print("    - Less boilerplate code")
print("    - Type hints support")
print("    - Automatic method generation")
print("    - Clean, readable code")

print()  # Empty line


# ============================================================================
# 2. BASIC DATA CLASS
# ============================================================================
print("=" * 60)
print("2. BASIC DATA CLASS")
print("=" * 60)

@dataclass
class Point:
    x: int
    y: int

# Usage
p = Point(1, 2)
print(f"  Point: {p}")
print(f"  x: {p.x}, y: {p.y}")

print()  # Empty line


# ============================================================================
# 3. AUTOMATIC METHODS
# ============================================================================
print("=" * 60)
print("3. AUTOMATIC METHODS")
print("=" * 60)

@dataclass
class Person:
    name: str
    age: int

p1 = Person("Alice", 30)
p2 = Person("Alice", 30)
p3 = Person("Bob", 25)

print(f"  Person 1: {p1}")  # __repr__ automatically generated
print(f"  Person 2: {p2}")
print(f"  Person 1 == Person 2: {p1 == p2}")  # __eq__ automatically generated
print(f"  Person 1 == Person 3: {p1 == p3}")

print()  # Empty line


# ============================================================================
# 4. COMPARISON WITH REGULAR CLASS
# ============================================================================
print("=" * 60)
print("4. COMPARISON WITH REGULAR CLASS")
print("=" * 60)

print("  Regular class (verbose):")
print("    ")
print("    class PointRegular:")
print("        def __init__(self, x, y):")
print("            self.x = x")
print("            self.y = y")
print("        ")
print("        def __repr__(self):")
print("            return f\"Point(x={self.x}, y={self.y})\")")
print("        ")
print("        def __eq__(self, other):")
print("            return self.x == other.x and self.y == other.y")
print("  ")
print("  Data class (concise):")
print("    ")
print("    @dataclass")
print("    class Point:")
print("        x: int")
print("        y: int")

print()  # Empty line


# ============================================================================
# 5. TYPE HINTS REQUIRED
# ============================================================================
print("=" * 60)
print("5. TYPE HINTS REQUIRED")
print("=" * 60)

print("  Data classes require type hints:")
print("    ")
print("    @dataclass")
print("    class Person:")
print("        name: str  # Type hint required")
print("        age: int   # Type hint required")
print("  ")
print("  Type hints are used to generate __init__()")

print()  # Empty line


# ============================================================================
# 6. ACCESSING FIELDS
# ============================================================================
print("=" * 60)
print("6. ACCESSING FIELDS")
print("=" * 60)

@dataclass
class Product:
    name: str
    price: float
    quantity: int

product = Product("Laptop", 999.99, 5)
print(f"  Product: {product}")
print(f"  Name: {product.name}")
print(f"  Price: ${product.price}")
print(f"  Quantity: {product.quantity}")

print()  # Empty line


# ============================================================================
# 7. MULTIPLE FIELDS
# ============================================================================
print("=" * 60)
print("7. MULTIPLE FIELDS")
print("=" * 60)

@dataclass
class Employee:
    name: str
    employee_id: int
    department: str
    salary: float
    is_active: bool

emp = Employee("John Doe", 12345, "Engineering", 75000.0, True)
print(f"  Employee: {emp}")
print(f"  Active: {emp.is_active}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("DATA CLASS BASICS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Use @dataclass decorator")
print("  - Type hints are required")
print("  - Automatic __init__(), __repr__(), __eq__()")
print("  - Less boilerplate than regular classes")
print("  - Perfect for data-holding classes")
print("=" * 60)

