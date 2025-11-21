# Data Classes in Python

Data classes (introduced in Python 3.7) provide a decorator and functions for automatically adding generated special methods to classes. They're perfect for classes that primarily store data.

## Table of Contents
1. [What are Data Classes?](#what-are-data-classes)
2. [Basic Data Classes](#basic-data-classes)
3. [Default Values](#default-values)
4. [Field Customization](#field-customization)
5. [Immutability](#immutability)
6. [Inheritance](#inheritance)
7. [Post-Init Processing](#post-init-processing)
8. [Comparison with Alternatives](#comparison-with-alternatives)
9. [Best Practices](#best-practices)

---

## What are Data Classes?

**Data classes** are a decorator that automatically generates special methods like `__init__()`, `__repr__()`, `__eq__()`, and more for classes that primarily store data.

**Key features:**
- Automatic `__init__()` generation
- Automatic `__repr__()` generation
- Automatic `__eq__()` generation
- Type hints support
- Less boilerplate code

**Benefits:**
- **Less Code**: No need to write boilerplate methods
- **Type Safety**: Works with type hints
- **Readability**: Clear, concise class definitions
- **Maintainability**: Easy to modify and extend

---

## Basic Data Classes

### Simple Data Class

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

# Usage
p = Point(1, 2)
print(p)  # Point(x=1, y=2)
print(p.x, p.y)  # 1 2
```

### Automatic Methods

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p1 = Person("Alice", 30)
p2 = Person("Alice", 30)
p3 = Person("Bob", 25)

# __repr__ is automatically generated
print(p1)  # Person(name='Alice', age=30)

# __eq__ is automatically generated
print(p1 == p2)  # True
print(p1 == p3)  # False
```

---

## Default Values

### Fields with Defaults

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int = 0
    email: str = ""

# Usage
p1 = Person("Alice")  # age=0, email=""
p2 = Person("Bob", 25)  # email=""
p3 = Person("Charlie", 30, "charlie@example.com")
```

### Default Factory

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class ShoppingCart:
    items: List[str] = field(default_factory=list)
    total: float = 0.0

# Usage
cart = ShoppingCart()
cart.items.append("apple")
print(cart.items)  # ['apple']
```

### Mutable Default Values

```python
from dataclasses import dataclass, field
from typing import List

# Wrong - mutable default
@dataclass
class BadExample:
    items: List[str] = []  # Don't do this!

# Correct - use default_factory
@dataclass
class GoodExample:
    items: List[str] = field(default_factory=list)
```

---

## Field Customization

### Field Options

```python
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int = field(default=0)
    email: str = field(default="", repr=False)  # Don't show in repr
    _id: int = field(init=False)  # Not in __init__
    
    def __post_init__(self):
        self._id = hash(self.name)
```

### Comparing Fields

```python
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int
    email: str = field(compare=False)  # Not used in comparison

p1 = Person("Alice", 30, "alice@example.com")
p2 = Person("Alice", 30, "different@example.com")
print(p1 == p2)  # True (email not compared)
```

### Hashing

```python
from dataclasses import dataclass

@dataclass(frozen=True)  # Immutable, can be hashed
class Point:
    x: int
    y: int

p = Point(1, 2)
print(hash(p))  # Works because frozen=True
```

---

## Immutability

### Frozen Data Classes

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(1, 2)
# p.x = 3  # FrozenInstanceError!
```

### When to Use Frozen

```python
# Good for:
# - Constants
# - Hashable objects (for sets/dicts)
# - Immutable data structures

@dataclass(frozen=True)
class Configuration:
    host: str
    port: int
    timeout: int
```

---

## Inheritance

### Basic Inheritance

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

@dataclass
class Employee(Person):
    employee_id: int
    salary: float

# Usage
emp = Employee("Alice", 30, 12345, 50000.0)
print(emp)  # Employee(name='Alice', age=30, employee_id=12345, salary=50000.0)
```

### Field Ordering

```python
from dataclasses import dataclass

@dataclass
class Base:
    base_field: str

@dataclass
class Derived(Base):
    derived_field: int

# Fields from base class come first
d = Derived("base", 10)
```

---

## Post-Init Processing

### __post_init__

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str = ""
    
    def __post_init__(self):
        if not self.email:
            self.email = f"{self.name.lower()}@example.com"
        if self.age < 0:
            raise ValueError("Age cannot be negative")

# Usage
p = Person("Alice", 30)
print(p.email)  # alice@example.com
```

### Computed Fields

```python
from dataclasses import dataclass, field

@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)
    
    def __post_init__(self):
        self.area = self.width * self.height

r = Rectangle(10, 5)
print(r.area)  # 50
```

---

## Comparison with Alternatives

### vs. Named Tuples

```python
from collections import namedtuple
from dataclasses import dataclass

# Named tuple
PointNT = namedtuple('Point', ['x', 'y'])

# Data class
@dataclass
class PointDC:
    x: int
    y: int

# Data classes are more flexible
# - Can have mutable fields
# - Can have methods
# - Better type hints
```

### vs. Regular Classes

```python
# Regular class (verbose)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# Data class (concise)
@dataclass
class Point:
    x: int
    y: int
```

---

## Advanced Features

### asdict() and astuple()

```python
from dataclasses import dataclass, asdict, astuple

@dataclass
class Point:
    x: int
    y: int

p = Point(1, 2)

# Convert to dictionary
print(asdict(p))  # {'x': 1, 'y': 2}

# Convert to tuple
print(astuple(p))  # (1, 2)
```

### replace()

```python
from dataclasses import dataclass, replace

@dataclass(frozen=True)
class Point:
    x: int
    y: int

p1 = Point(1, 2)
p2 = replace(p1, x=3)  # Create new instance with modified field
print(p2)  # Point(x=3, y=2)
```

### fields()

```python
from dataclasses import dataclass, fields

@dataclass
class Person:
    name: str
    age: int
    email: str = ""

# Get field information
for field in fields(Person):
    print(f"{field.name}: {field.type}")
```

---

## Best Practices

### 1. Use Type Hints

```python
# Good
@dataclass
class Person:
    name: str
    age: int

# Less preferred
@dataclass
class Person:
    name: str = ""
    age: int = 0
```

### 2. Use default_factory for Mutable Defaults

```python
# Good
@dataclass
class Example:
    items: List[str] = field(default_factory=list)

# Bad
@dataclass
class Example:
    items: List[str] = []  # Mutable default!
```

### 3. Use Frozen for Immutable Data

```python
# Good for constants
@dataclass(frozen=True)
class Config:
    host: str
    port: int
```

### 4. Keep Data Classes Simple

```python
# Good - primarily data
@dataclass
class Point:
    x: float
    y: float

# Consider regular class for complex behavior
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, other):
        # Complex calculation
        pass
```

### 5. Use __post_init__ for Validation

```python
@dataclass
class Person:
    name: str
    age: int
    
    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age must be non-negative")
```

---

## Common Mistakes to Avoid

1. **Mutable default arguments**
   ```python
   # Wrong
   @dataclass
   class Example:
       items: List[str] = []
   
   # Correct
   @dataclass
   class Example:
       items: List[str] = field(default_factory=list)
   ```

2. **Forgetting type hints**
   ```python
   # Less clear
   @dataclass
   class Person:
       name = ""
       age = 0
   
   # Better
   @dataclass
   class Person:
       name: str = ""
       age: int = 0
   ```

3. **Using data classes for everything**
   ```python
   # Data classes are for data storage
   # Use regular classes for complex behavior
   ```

---

## Summary

- **Data classes** reduce boilerplate for data-holding classes
- Use `@dataclass` decorator
- Automatic `__init__()`, `__repr__()`, `__eq__()`
- Use `field()` for customization
- Use `frozen=True` for immutability
- Use `__post_init__()` for validation
- Use `default_factory` for mutable defaults
- Works great with type hints

**Remember**: Data classes are perfect for classes that primarily store data. Use them to write cleaner, more maintainable code!

---

## Next Steps

Now that you understand data classes:
1. Practice with the examples in this folder
2. Use data classes in your projects
3. Compare with named tuples and regular classes
4. Explore advanced features
5. Apply best practices

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_data_class_basics.py`: Understanding data classes - start here!
2. `02_default_values.py`: Working with default values
3. `03_field_customization.py`: Customizing fields
4. `04_immutability.py`: Frozen data classes
5. `05_inheritance.py`: Data class inheritance
6. `06_practical_examples.py`: Real-world data class examples

Run these files in order to see data classes in action!

