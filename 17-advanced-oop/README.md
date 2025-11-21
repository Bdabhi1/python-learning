# Advanced Object-Oriented Programming in Python

This guide covers advanced OOP concepts including abstract classes, multiple inheritance, method resolution order, descriptors, metaclasses, and design patterns.

## Table of Contents
1. [Abstract Base Classes](#abstract-base-classes)
2. [Multiple Inheritance and MRO](#multiple-inheritance-and-mro)
3. [Special Methods (Magic Methods)](#special-methods-magic-methods)
4. [Descriptors](#descriptors)
5. [Property Decorators](#property-decorators)
6. [Class Decorators](#class-decorators)
7. [Metaclasses](#metaclasses)
8. [Design Patterns](#design-patterns)
9. [Best Practices](#best-practices)

---

## Abstract Base Classes

Abstract Base Classes (ABCs) define a blueprint for other classes. They cannot be instantiated directly.

### Using `abc` Module

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# shape = Shape()  # Error: cannot instantiate
rect = Rectangle(5, 3)  # OK
```

---

## Multiple Inheritance and MRO

Python supports multiple inheritance. The Method Resolution Order (MRO) determines which method is called.

### Basic Multiple Inheritance

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
print(C.__mro__)   # Shows method resolution order
```

### Diamond Problem

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

d = D()
print(d.method())  # "B" (MRO: D -> B -> C -> A)
```

---

## Special Methods (Magic Methods)

Special methods customize object behavior with built-in operations.

### String Representation

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

### Comparison Methods

```python
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
print(p1 == p2)  # True
```

### Arithmetic Operations

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
v4 = v1 * 2
```

---

## Descriptors

Descriptors control attribute access through `__get__`, `__set__`, and `__delete__`.

### Property Descriptor

```python
class Property:
    def __init__(self, getter):
        self.getter = getter
    
    def __get__(self, instance, owner):
        return self.getter(instance)

class Person:
    def __init__(self, name):
        self._name = name
    
    @Property
    def name(self):
        return self._name
```

### Custom Descriptor

```python
class ValidatedAttribute:
    def __init__(self, validator):
        self.validator = validator
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if self.validator(value):
            instance.__dict__[self.name] = value
        else:
            raise ValueError(f"Invalid value for {self.name}")

class Person:
    age = ValidatedAttribute(lambda x: 0 <= x <= 150)
```

---

## Property Decorators

Properties provide controlled access to attributes.

### Basic Property

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
            raise ValueError("Too cold")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
```

---

## Class Decorators

Class decorators modify or enhance classes.

### Simple Class Decorator

```python
def add_method(cls):
    def new_method(self):
        return "New method"
    cls.new_method = new_method
    return cls

@add_method
class MyClass:
    pass

obj = MyClass()
print(obj.new_method())
```

---

## Metaclasses

Metaclasses are classes of classes. They control class creation.

### Basic Metaclass

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['created_by'] = 'Meta'
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

print(MyClass.created_by)  # 'Meta'
```

---

## Design Patterns

### Singleton Pattern

```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
```

### Factory Pattern

```python
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        raise ValueError("Unknown animal type")
```

### Observer Pattern

```python
class Observer:
    def update(self, message):
        pass

class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)
```

---

## Best Practices

1. **Use ABCs for interfaces**
2. **Understand MRO for multiple inheritance**
3. **Implement special methods appropriately**
4. **Use descriptors for reusable attribute logic**
5. **Prefer composition over complex inheritance**
6. **Keep metaclasses simple and documented**

---

## Summary

- **Abstract Base Classes** define interfaces
- **Multiple Inheritance** requires understanding MRO
- **Special Methods** customize object behavior
- **Descriptors** control attribute access
- **Metaclasses** control class creation
- **Design Patterns** solve common problems

**Remember**: Advanced OOP concepts should be used when they simplify code, not complicate it!

---

## Next Steps

Now that you understand advanced OOP:
1. Practice with the examples in this folder
2. Study design patterns
3. Experiment with metaclasses carefully
4. Move on to **18-iterators-and-generators** to learn about iteration

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_abstract_classes.py`: Abstract base classes and interfaces
2. `02_special_methods.py`: Magic methods and operator overloading
3. `03_multiple_inheritance.py`: Multiple inheritance and MRO
4. `04_descriptors.py`: Descriptors and property management
5. `05_metaclasses.py`: Metaclasses and class creation
6. `06_practical_examples.py`: Advanced OOP patterns and examples

Run these files in order to see advanced OOP concepts in action!

