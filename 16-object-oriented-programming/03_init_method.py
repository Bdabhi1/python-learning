"""
The __init__ Method in Python

This file demonstrates the __init__ method, which is called when
an object is created to initialize its attributes.
"""

# ============================================================================
# 1. BASIC __init__ METHOD
# ============================================================================
print("=" * 60)
print("1. BASIC __init__ METHOD")
print("=" * 60)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"  Created person: {self.name}")

person = Person("Alice", 30)
print(f"  Name: {person.name}, Age: {person.age}")

print()  # Empty line


# ============================================================================
# 2. DEFAULT VALUES IN __init__
# ============================================================================
print("=" * 60)
print("2. DEFAULT VALUES IN __init__")
print("=" * 60)

class Car:
    def __init__(self, make, model, year=2020):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0  # Default value

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic", 2021)

print(f"  car1: {car1.year} {car1.make} {car1.model}, Mileage: {car1.mileage}")
print(f"  car2: {car2.year} {car2.make} {car2.model}, Mileage: {car2.mileage}")

print()  # Empty line


# ============================================================================
# 3. INITIALIZING MULTIPLE ATTRIBUTES
# ============================================================================
print("=" * 60)
print("3. INITIALIZING MULTIPLE ATTRIBUTES")
print("=" * 60)

class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance
        self.transactions = []  # List to track transactions
        self.account_number = f"ACC{id(self)}"  # Generate account number

account = BankAccount("Alice", 1000)
print(f"  Owner: {account.owner}")
print(f"  Balance: ${account.balance}")
print(f"  Account Number: {account.account_number}")

print()  # Empty line


# ============================================================================
# 4. VALIDATION IN __init__
# ============================================================================
print("=" * 60)
print("4. VALIDATION IN __init__")
print("=" * 60)

class Student:
    def __init__(self, name, age, grade):
        if age < 0:
            raise ValueError("Age cannot be negative")
        if grade not in ['A', 'B', 'C', 'D', 'F']:
            raise ValueError("Invalid grade")
        
        self.name = name
        self.age = age
        self.grade = grade

try:
    student = Student("Alice", 20, 'A')
    print(f"  Created: {student.name}, Age: {student.age}, Grade: {student.grade}")
except ValueError as e:
    print(f"  Error: {e}")

print()  # Empty line


# ============================================================================
# 5. COMPUTED ATTRIBUTES IN __init__
# ============================================================================
print("=" * 60)
print("5. COMPUTED ATTRIBUTES IN __init__")
print("=" * 60)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height  # Computed during initialization
        self.perimeter = 2 * (width + height)

rect = Rectangle(5, 3)
print(f"  Width: {rect.width}, Height: {rect.height}")
print(f"  Area: {rect.area}")
print(f"  Perimeter: {rect.perimeter}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("__init__ METHOD SUMMARY:")
print("=" * 60)
print("  - __init__ is called automatically when object is created")
print("  - First parameter is always 'self'")
print("  - Used to initialize instance attributes")
print("  - Can have default parameter values")
print("  - Can perform validation")
print("  - Can compute derived attributes")
print("=" * 60)

