"""
Inheritance in Data Classes

This file demonstrates inheritance with data classes.
"""

from dataclasses import dataclass

# ============================================================================
# 1. BASIC INHERITANCE
# ============================================================================
print("=" * 60)
print("1. BASIC INHERITANCE")
print("=" * 60)

@dataclass
class Person:
    name: str
    age: int

@dataclass
class Employee(Person):
    employee_id: int
    salary: float

emp = Employee("Alice", 30, 12345, 50000.0)
print(f"  Employee: {emp}")
print(f"  Name: {emp.name}, Age: {emp.age}")
print(f"  ID: {emp.employee_id}, Salary: ${emp.salary}")

print()  # Empty line


# ============================================================================
# 2. FIELD ORDERING
# ============================================================================
print("=" * 60)
print("2. FIELD ORDERING")
print("=" * 60)

@dataclass
class Base:
    base_field: str

@dataclass
class Derived(Base):
    derived_field: int

d = Derived("base_value", 10)
print(f"  Derived: {d}")
print("  Fields from base class come first")

print()  # Empty line


# ============================================================================
# 3. OVERRIDING FIELDS
# ============================================================================
print("=" * 60)
print("3. OVERRIDING FIELDS")
print("=" * 60)

@dataclass
class Animal:
    name: str
    age: int

@dataclass
class Dog(Animal):
    breed: str
    age: int = 0  # Override with default

dog = Dog("Buddy", "Golden Retriever")
print(f"  Dog: {dog}")
print("  age has default value in subclass")

print()  # Empty line


# ============================================================================
# 4. MULTIPLE INHERITANCE
# ============================================================================
print("=" * 60)
print("4. MULTIPLE INHERITANCE")
print("=" * 60)

@dataclass
class Flyable:
    max_altitude: float

@dataclass
class Swimmable:
    max_depth: float

@dataclass
class Duck(Animal, Flyable, Swimmable):
    pass

duck = Duck("Donald", 5, 1000.0, 10.0)
print(f"  Duck: {duck}")
print("  Inherits from multiple classes")

print()  # Empty line


# ============================================================================
# 5. INHERITANCE WITH METHODS
# ============================================================================
print("=" * 60)
print("5. INHERITANCE WITH METHODS")
print("=" * 60)

@dataclass
class Shape:
    name: str
    
    def area(self):
        return 0.0

@dataclass
class Rectangle(Shape):
    width: float
    height: float
    
    def area(self):
        return self.width * self.height

rect = Rectangle("Rectangle", 10, 5)
print(f"  Rectangle: {rect}")
print(f"  Area: {rect.area()}")

print()  # Empty line


# ============================================================================
# 6. FROZEN INHERITANCE
# ============================================================================
print("=" * 60)
print("6. FROZEN INHERITANCE")
print("=" * 60)

@dataclass(frozen=True)
class BaseFrozen:
    base_value: int

@dataclass(frozen=True)
class DerivedFrozen(BaseFrozen):
    derived_value: str

df = DerivedFrozen(10, "test")
print(f"  Derived frozen: {df}")
print("  Both base and derived are frozen")

print()  # Empty line


# ============================================================================
# 7. INHERITANCE BEST PRACTICES
# ============================================================================
print("=" * 60)
print("7. INHERITANCE BEST PRACTICES")
print("=" * 60)

print("  Best practices:")
print("    - Keep inheritance simple")
print("    - Use composition when possible")
print("    - Be careful with field ordering")
print("    - All classes in hierarchy should use @dataclass")
print("    - Frozen status must match in hierarchy")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("INHERITANCE SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Data classes support inheritance")
print("  - Base class fields come first")
print("  - Can override fields with defaults")
print("  - Supports multiple inheritance")
print("  - Can add methods to subclasses")
print("  - Frozen status must be consistent")
print("=" * 60)

