"""
Inheritance in Python

This file demonstrates class inheritance, method overriding, and
the super() function.
"""

# ============================================================================
# 1. BASIC INHERITANCE
# ============================================================================
print("=" * 60)
print("1. BASIC INHERITANCE")
print("=" * 60)

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"
    
    def move(self):
        return f"{self.name} is moving"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(f"  {dog.speak()}")
print(f"  {dog.move()}")
print(f"  {cat.speak()}")
print(f"  {cat.move()}")

print()  # Empty line


# ============================================================================
# 2. THE super() FUNCTION
# ============================================================================
print("=" * 60)
print("2. THE super() FUNCTION")
print("=" * 60)

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent's __init__
        self.breed = breed
    
    def info(self):
        return f"{self.name} is a {self.breed}"

dog = Dog("Buddy", "Golden Retriever")
print(f"  {dog.info()}")

print()  # Empty line


# ============================================================================
# 3. METHOD OVERRIDING
# ============================================================================
print("=" * 60)
print("3. METHOD OVERRIDING")
print("=" * 60)

class Shape:
    def area(self):
        return 0
    
    def perimeter(self):
        return 0

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
# 4. MULTIPLE INHERITANCE
# ============================================================================
print("=" * 60)
print("4. MULTIPLE INHERITANCE")
print("=" * 60)

class Flyable:
    def fly(self):
        return "Flying"

class Swimmable:
    def swim(self):
        return "Swimming"

class Duck(Flyable, Swimmable):
    def quack(self):
        return "Quack!"

duck = Duck()
print(f"  {duck.fly()}")
print(f"  {duck.swim()}")
print(f"  {duck.quack()}")

print()  # Empty line


# ============================================================================
# 5. isinstance() AND issubclass()
# ============================================================================
print("=" * 60)
print("5. isinstance() AND issubclass()")
print("=" * 60)

class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

print(f"  isinstance(dog, Dog): {isinstance(dog, Dog)}")
print(f"  isinstance(dog, Animal): {isinstance(dog, Animal)}")
print(f"  issubclass(Dog, Animal): {issubclass(Dog, Animal)}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("INHERITANCE SUMMARY:")
print("=" * 60)
print("  - Child class inherits from parent class")
print("  - Use super() to call parent methods")
print("  - Override methods by redefining them")
print("  - Multiple inheritance is supported")
print("  - isinstance() checks object type")
print("  - issubclass() checks class relationship")
print("=" * 60)

