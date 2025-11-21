"""
Classes and Objects in Python

This file demonstrates the fundamental concepts of classes and objects
in object-oriented programming.
"""

# ============================================================================
# 1. WHAT IS A CLASS?
# ============================================================================
print("=" * 60)
print("1. WHAT IS A CLASS?")
print("=" * 60)

print("  A class is a blueprint for creating objects.")
print("  It defines attributes (data) and methods (behavior).")
print("  ")
print("  Think of a class as a cookie cutter,")
print("  and objects as the cookies made from it.")

print()  # Empty line


# ============================================================================
# 2. DEFINING A SIMPLE CLASS
# ============================================================================
print("=" * 60)
print("2. DEFINING A SIMPLE CLASS")
print("=" * 60)

# Empty class
class Dog:
    pass

# Create an object (instance) from the class
my_dog = Dog()
print(f"  Created object: {my_dog}")
print(f"  Type: {type(my_dog)}")
print(f"  Is instance of Dog? {isinstance(my_dog, Dog)}")

print()  # Empty line


# ============================================================================
# 3. CLASS WITH ATTRIBUTES
# ============================================================================
print("=" * 60)
print("3. CLASS WITH ATTRIBUTES")
print("=" * 60)

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(f"  dog1.name: {dog1.name}")
print(f"  dog1.age: {dog1.age}")
print(f"  dog2.name: {dog2.name}")
print(f"  dog2.age: {dog2.age}")

print("\n  Each object has its own attributes!")

print()  # Empty line


# ============================================================================
# 4. CLASS WITH METHODS
# ============================================================================
print("=" * 60)
print("4. CLASS WITH METHODS")
print("=" * 60)

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says Woof!"
    
    def get_info(self):
        return f"{self.name} is {self.age} years old"

dog = Dog("Buddy", 3)
print(f"  {dog.bark()}")
print(f"  {dog.get_info()}")

print()  # Empty line


# ============================================================================
# 5. THE 'self' PARAMETER
# ============================================================================
print("=" * 60)
print("5. THE 'self' PARAMETER")
print("=" * 60)

class Person:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        return f"Hi, I'm {self.name}"

person = Person("Alice")
print(f"  {person.introduce()}")

print("\n  'self' refers to the instance (object) itself")
print("  It's automatically passed when calling methods")

print()  # Empty line


# ============================================================================
# 6. MULTIPLE OBJECTS
# ============================================================================
print("=" * 60)
print("6. MULTIPLE OBJECTS")
print("=" * 60)

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

# Create multiple objects
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2021)
car3 = Car("Ford", "Mustang", 2019)

print("  Cars:")
print(f"    {car1.display_info()}")
print(f"    {car2.display_info()}")
print(f"    {car3.display_info()}")

print("\n  Each object is independent!")

print()  # Empty line


# ============================================================================
# 7. MODIFYING ATTRIBUTES
# ============================================================================
print("=" * 60)
print("7. MODIFYING ATTRIBUTES")
print("=" * 60)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Insufficient funds"

account = BankAccount("Alice", 1000)
print(f"  Initial balance: ${account.balance}")
print(f"  {account.deposit(500)}")
print(f"  {account.withdraw(200)}")
print(f"  {account.withdraw(2000)}")

print()  # Empty line


# ============================================================================
# 8. CLASS ATTRIBUTES VS INSTANCE ATTRIBUTES
# ============================================================================
print("=" * 60)
print("8. CLASS ATTRIBUTES VS INSTANCE ATTRIBUTES")
print("=" * 60)

class Student:
    school = "Python Academy"  # Class attribute (shared)
    
    def __init__(self, name, student_id):
        self.name = name        # Instance attribute (unique)
        self.student_id = student_id  # Instance attribute

student1 = Student("Alice", "S001")
student2 = Student("Bob", "S002")

print(f"  student1.name: {student1.name}")
print(f"  student1.school: {student1.school}")
print(f"  student2.name: {student2.name}")
print(f"  student2.school: {student2.school}")
print(f"  Student.school: {Student.school}")

print("\n  Class attributes are shared by all instances")
print("  Instance attributes are unique to each object")

print()  # Empty line


# ============================================================================
# 9. PRACTICAL EXAMPLE: RECTANGLE
# ============================================================================
print("=" * 60)
print("9. PRACTICAL EXAMPLE: RECTANGLE")
print("=" * 60)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def is_square(self):
        return self.width == self.height

rect = Rectangle(5, 3)
print(f"  Rectangle: {rect.width} x {rect.height}")
print(f"  Area: {rect.area()}")
print(f"  Perimeter: {rect.perimeter()}")
print(f"  Is square? {rect.is_square()}")

square = Rectangle(4, 4)
print(f"\n  Square: {square.width} x {square.height}")
print(f"  Is square? {square.is_square()}")

print()  # Empty line


# ============================================================================
# 10. CHECKING OBJECT TYPE
# ============================================================================
print("=" * 60)
print("10. CHECKING OBJECT TYPE")
print("=" * 60)

class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()
print(f"  type(dog): {type(dog)}")
print(f"  isinstance(dog, Dog): {isinstance(dog, Dog)}")
print(f"  isinstance(dog, Animal): {isinstance(dog, Animal)}")
print(f"  isinstance(dog, object): {isinstance(dog, object)}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("CLASSES AND OBJECTS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Class is a blueprint for creating objects")
print("  - Object is an instance of a class")
print("  - Attributes store data (self.attribute)")
print("  - Methods define behavior (def method(self))")
print("  - 'self' refers to the instance")
print("  - Each object has its own attributes")
print("  - Class attributes are shared by all instances")
print("=" * 60)

