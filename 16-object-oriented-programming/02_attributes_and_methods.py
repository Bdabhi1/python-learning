"""
Attributes and Methods in Python OOP

This file demonstrates instance attributes, class attributes, and
different types of methods in Python classes.
"""

# ============================================================================
# 1. INSTANCE ATTRIBUTES
# ============================================================================
print("=" * 60)
print("1. INSTANCE ATTRIBUTES")
print("=" * 60)

class Person:
    def __init__(self, name, age):
        self.name = name      # Instance attribute
        self.age = age        # Instance attribute

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(f"  person1.name: {person1.name}, person1.age: {person1.age}")
print(f"  person2.name: {person2.name}, person2.age: {person2.age}")

print("\n  Instance attributes belong to specific objects")

print()  # Empty line


# ============================================================================
# 2. CLASS ATTRIBUTES
# ============================================================================
print("=" * 60)
print("2. CLASS ATTRIBUTES")
print("=" * 60)

class Student:
    school = "Python Academy"  # Class attribute
    total_students = 0         # Class attribute
    
    def __init__(self, name):
        self.name = name
        Student.total_students += 1

student1 = Student("Alice")
student2 = Student("Bob")

print(f"  student1.school: {student1.school}")
print(f"  student2.school: {student2.school}")
print(f"  Student.school: {Student.school}")
print(f"  Total students: {Student.total_students}")

print("\n  Class attributes are shared by all instances")

print()  # Empty line


# ============================================================================
# 3. INSTANCE METHODS
# ============================================================================
print("=" * 60)
print("3. INSTANCE METHODS")
print("=" * 60)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):  # Instance method
        return self.width * self.height
    
    def perimeter(self):  # Instance method
        return 2 * (self.width + self.height)

rect = Rectangle(5, 3)
print(f"  Rectangle: {rect.width} x {rect.height}")
print(f"  Area: {rect.area()}")
print(f"  Perimeter: {rect.perimeter()}")

print()  # Empty line


# ============================================================================
# 4. CLASS METHODS
# ============================================================================
print("=" * 60)
print("4. CLASS METHODS")
print("=" * 60)

class Circle:
    pi = 3.14159
    
    def __init__(self, radius):
        self.radius = radius
    
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)
    
    @classmethod
    def get_pi(cls):
        return cls.pi

circle1 = Circle(5)
circle2 = Circle.from_diameter(10)

print(f"  circle1.radius: {circle1.radius}")
print(f"  circle2.radius: {circle2.radius}")
print(f"  Circle.get_pi(): {Circle.get_pi()}")

print("\n  Class methods work with the class, not instances")

print()  # Empty line


# ============================================================================
# 5. STATIC METHODS
# ============================================================================
print("=" * 60)
print("5. STATIC METHODS")
print("=" * 60)

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b

print(f"  MathUtils.add(5, 3): {MathUtils.add(5, 3)}")
print(f"  MathUtils.multiply(4, 7): {MathUtils.multiply(4, 7)}")

# Can also call from instance
utils = MathUtils()
print(f"  utils.add(2, 8): {utils.add(2, 8)}")

print("\n  Static methods don't need self or cls")

print()  # Empty line


# ============================================================================
# 6. PROPERTIES
# ============================================================================
print("=" * 60)
print("6. PROPERTIES")
print("=" * 60)

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

temp = Temperature(25)
print(f"  Celsius: {temp.celsius}°C")
print(f"  Fahrenheit: {temp.fahrenheit}°F")

temp.celsius = 30
print(f"  After setting to 30°C: {temp.fahrenheit}°F")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("ATTRIBUTES AND METHODS SUMMARY:")
print("=" * 60)
print("Instance Attributes: self.attr (unique to each object)")
print("Class Attributes: Class.attr (shared by all)")
print("Instance Methods: def method(self) (operate on instance)")
print("Class Methods: @classmethod def method(cls) (operate on class)")
print("Static Methods: @staticmethod def method() (no self/cls)")
print("Properties: @property (controlled attribute access)")
print("=" * 60)

