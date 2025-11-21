# Object-Oriented Programming in Python

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects, which contain both data (attributes) and behavior (methods). Python is a powerful OOP language that supports classes, objects, inheritance, and more.

## Table of Contents
1. [What is Object-Oriented Programming?](#what-is-object-oriented-programming)
2. [Classes and Objects](#classes-and-objects)
3. [Attributes and Methods](#attributes-and-methods)
4. [The `__init__` Method](#the-__init__-method)
5. [Instance vs Class Attributes](#instance-vs-class-attributes)
6. [Methods: Instance, Class, and Static](#methods-instance-class-and-static)
7. [Encapsulation](#encapsulation)
8. [Inheritance](#inheritance)
9. [Polymorphism](#polymorphism)
10. [Special Methods (Magic Methods)](#special-methods-magic-methods)
11. [Best Practices](#best-practices)

---

## What is Object-Oriented Programming?

**Object-Oriented Programming (OOP)** is a programming paradigm based on the concept of "objects" that contain:
- **Data** (attributes/properties)
- **Behavior** (methods/functions)

**Key OOP Concepts:**
- **Class**: A blueprint for creating objects
- **Object**: An instance of a class
- **Encapsulation**: Bundling data and methods together
- **Inheritance**: Creating new classes from existing ones
- **Polymorphism**: Using objects of different types through a common interface

**Benefits of OOP:**
- **Modularity**: Code organized into logical units
- **Reusability**: Classes can be reused in different programs
- **Maintainability**: Easier to update and maintain
- **Scalability**: Easier to extend functionality

---

## Classes and Objects

### Defining a Class

```python
class Dog:
    pass  # Empty class

# Create an object (instance)
my_dog = Dog()
```

### Basic Class with Attributes

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.name)  # "Buddy"
print(dog2.age)   # 5
```

**Key Points:**
- `class` keyword defines a class
- `self` refers to the instance
- Objects are created by calling the class like a function
- Each object has its own attributes

---

## Attributes and Methods

### Instance Attributes

Attributes that belong to a specific instance:

```python
class Person:
    def __init__(self, name, age):
        self.name = name      # Instance attribute
        self.age = age        # Instance attribute

person = Person("Alice", 30)
print(person.name)  # "Alice"
```

### Instance Methods

Methods that operate on instance data:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 3)
print(rect.area())       # 15
print(rect.perimeter())  # 16
```

---

## The `__init__` Method

The `__init__` method is a special method called when an object is created. It initializes the object's attributes.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0  # Default value
    
    def drive(self, miles):
        self.mileage += miles

car = Car("Toyota", "Camry", 2020)
car.drive(100)
print(car.mileage)  # 100
```

**Key Points:**
- `__init__` is called automatically when creating an object
- `self` is the first parameter (refers to the instance)
- You can set default values for attributes

---

## Instance vs Class Attributes

### Instance Attributes

Belong to a specific instance:

```python
class Student:
    def __init__(self, name):
        self.name = name  # Instance attribute

student1 = Student("Alice")
student2 = Student("Bob")
print(student1.name)  # "Alice"
print(student2.name)  # "Bob"
```

### Class Attributes

Shared by all instances:

```python
class Student:
    school = "Python Academy"  # Class attribute
    
    def __init__(self, name):
        self.name = name  # Instance attribute

student1 = Student("Alice")
student2 = Student("Bob")
print(student1.school)  # "Python Academy"
print(student2.school)  # "Python Academy"
print(Student.school)    # "Python Academy"
```

---

## Methods: Instance, Class, and Static

### Instance Methods

Operate on instance data (most common):

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):  # Instance method
        return 3.14159 * self.radius ** 2
```

### Class Methods

Operate on the class itself:

```python
class Circle:
    pi = 3.14159
    
    def __init__(self, radius):
        self.radius = radius
    
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)  # cls refers to the class

circle = Circle.from_diameter(10)
```

### Static Methods

Don't need access to instance or class:

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

result = MathUtils.add(5, 3)  # 8
```

---

## Encapsulation

Encapsulation is the bundling of data and methods that operate on that data. Python uses naming conventions to indicate access levels.

### Public Attributes

```python
class Person:
    def __init__(self, name):
        self.name = name  # Public attribute
```

### Protected Attributes

Convention: prefix with single underscore `_`:

```python
class Person:
    def __init__(self, name):
        self._name = name  # Protected (convention only)
```

### Private Attributes

Convention: prefix with double underscore `__`:

```python
class Person:
    def __init__(self, name):
        self.__name = name  # Private (name mangling)
    
    def get_name(self):
        return self.__name
```

### Properties

Use `@property` for controlled access:

```python
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

temp = Temperature(25)
print(temp.celsius)  # 25
temp.celsius = 30
```

---

## Inheritance

Inheritance allows a class to inherit attributes and methods from another class.

### Basic Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Buddy")
print(dog.speak())  # "Woof!"
```

### The `super()` Function

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent's __init__
        self.breed = breed

dog = Dog("Buddy", "Golden Retriever")
```

### Multiple Inheritance

```python
class A:
    def method(self):
        return "A"

class B:
    def method(self):
        return "B"

class C(A, B):
    pass

c = C()
print(c.method())  # "A" (first in MRO)
```

---

## Polymorphism

Polymorphism allows objects of different types to be used through a common interface.

```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

# Polymorphism in action
shapes = [Rectangle(5, 3), Circle(4)]
for shape in shapes:
    print(shape.area())  # Works for both types
```

---

## Special Methods (Magic Methods)

Special methods (dunder methods) define how objects behave with built-in operations.

### `__str__` and `__repr__`

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

person = Person("Alice", 30)
print(str(person))   # Uses __str__
print(repr(person))  # Uses __repr__
```

### `__len__` and `__getitem__`

```python
class MyList:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]

my_list = MyList([1, 2, 3, 4])
print(len(my_list))    # 4
print(my_list[2])      # 3
```

### `__add__` and Other Operators

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3.x, p3.y)  # 4, 6
```

---

## Best Practices

### 1. Use Descriptive Class Names

```python
# Good
class BankAccount:
    pass

# Less preferred
class BA:
    pass
```

### 2. Keep Classes Focused

```python
# Good - single responsibility
class Rectangle:
    def area(self):
        pass

# Less preferred - multiple responsibilities
class RectangleAndCircle:
    pass
```

### 3. Use Docstrings

```python
class Calculator:
    """A simple calculator class."""
    
    def add(self, a, b):
        """Add two numbers."""
        return a + b
```

### 4. Prefer Composition Over Inheritance

```python
# Composition
class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()  # Has-a relationship
```

### 5. Use Properties for Computed Attributes

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def area(self):
        return self.width * self.height
```

---

## Common Mistakes to Avoid

1. **Forgetting `self` parameter**
   ```python
   # Wrong
   def method():
       pass
   
   # Correct
   def method(self):
       pass
   ```

2. **Modifying mutable class attributes**
   ```python
   # Problematic
   class MyClass:
       items = []
   
   # Better
   class MyClass:
       def __init__(self):
           self.items = []
   ```

3. **Not using `super()` in inheritance**
   ```python
   # Less preferred
   class Child(Parent):
       def __init__(self):
           Parent.__init__(self)
   
   # Better
   class Child(Parent):
       def __init__(self):
           super().__init__()
   ```

---

## Summary

- **Classes** are blueprints for creating objects
- **Objects** are instances of classes
- **Attributes** store data, **methods** define behavior
- **`__init__`** initializes objects
- **Inheritance** allows code reuse
- **Polymorphism** enables flexible code
- **Encapsulation** bundles data and methods
- **Special methods** customize object behavior

**Remember**: OOP helps organize code into logical, reusable components. Master these concepts to write maintainable Python programs!

---

## Next Steps

Now that you understand object-oriented programming:
1. Practice with the examples in this folder
2. Create your own classes and objects
3. Experiment with inheritance and polymorphism
4. Move on to **17-advanced-oop** to learn advanced OOP concepts

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_classes_and_objects.py`: Understanding classes and objects - start here!
2. `02_attributes_and_methods.py`: Instance attributes and methods
3. `03_init_method.py`: The `__init__` method and object initialization
4. `04_inheritance.py`: Class inheritance and method overriding
5. `05_encapsulation.py`: Encapsulation and access control
6. `06_practical_examples.py`: Real-world OOP examples

Run these files in order to see object-oriented programming in action!

