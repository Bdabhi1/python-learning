"""
Abstract Base Classes in Python

This file demonstrates abstract base classes (ABCs) and how to use them
to define interfaces that must be implemented by subclasses.
"""

from abc import ABC, abstractmethod

# ============================================================================
# 1. BASIC ABSTRACT CLASS
# ============================================================================
print("=" * 60)
print("1. BASIC ABSTRACT CLASS")
print("=" * 60)

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# Cannot instantiate abstract class
# shape = Shape()  # TypeError

print("  Abstract classes cannot be instantiated directly")

print()  # Empty line


# ============================================================================
# 2. IMPLEMENTING ABSTRACT METHODS
# ============================================================================
print("=" * 60)
print("2. IMPLEMENTING ABSTRACT METHODS")
print("=" * 60)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

rect = Rectangle(5, 3)
circle = Circle(4)

print(f"  Rectangle area: {rect.area()}")
print(f"  Circle area: {circle.area()}")

print()  # Empty line


# ============================================================================
# 3. MIXING ABSTRACT AND CONCRETE METHODS
# ============================================================================
print("=" * 60)
print("3. MIXING ABSTRACT AND CONCRETE METHODS")
print("=" * 60)

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def speak(self):
        pass
    
    def move(self):
        return f"{self.name} is moving"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Buddy")
print(f"  {dog.speak()}")
print(f"  {dog.move()}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("ABSTRACT CLASSES SUMMARY:")
print("=" * 60)
print("  - Use ABC and @abstractmethod")
print("  - Cannot instantiate abstract classes")
print("  - Subclasses must implement abstract methods")
print("  - Can mix abstract and concrete methods")
print("=" * 60)

