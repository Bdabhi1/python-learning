"""
Special Methods (Magic Methods) in Python

This file demonstrates special methods that customize object behavior
with built-in operations.
"""

# ============================================================================
# 1. STRING REPRESENTATION
# ============================================================================
print("=" * 60)
print("1. STRING REPRESENTATION")
print("=" * 60)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

person = Person("Alice", 30)
print(f"  str(person): {str(person)}")
print(f"  repr(person): {repr(person)}")

print()  # Empty line


# ============================================================================
# 2. COMPARISON METHODS
# ============================================================================
print("=" * 60)
print("2. COMPARISON METHODS")
print("=" * 60)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(2, 1)

print(f"  p1 == p2: {p1 == p2}")
print(f"  p1 < p3: {p1 < p3}")

print()  # Empty line


# ============================================================================
# 3. ARITHMETIC OPERATIONS
# ============================================================================
print("=" * 60)
print("3. ARITHMETIC OPERATIONS")
print("=" * 60)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
v4 = v1 * 2

print(f"  v1 + v2: {v3}")
print(f"  v1 * 2: {v4}")

print()  # Empty line


# ============================================================================
# 4. LENGTH AND INDEXING
# ============================================================================
print("=" * 60)
print("4. LENGTH AND INDEXING")
print("=" * 60)

class MyList:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value

my_list = MyList([1, 2, 3, 4])
print(f"  len(my_list): {len(my_list)}")
print(f"  my_list[2]: {my_list[2]}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("SPECIAL METHODS SUMMARY:")
print("=" * 60)
print("  - __str__: User-friendly string representation")
print("  - __repr__: Developer-friendly string representation")
print("  - __eq__, __lt__: Comparison operations")
print("  - __add__, __mul__: Arithmetic operations")
print("  - __len__, __getitem__: Container operations")
print("=" * 60)

