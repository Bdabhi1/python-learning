# Functional Programming in Python

Functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions. Python supports functional programming features like higher-order functions, lambda functions, map, filter, reduce, and list comprehensions.

## Table of Contents
1. [What is Functional Programming?](#what-is-functional-programming)
2. [Lambda Functions](#lambda-functions)
3. [Map, Filter, and Reduce](#map-filter-and-reduce)
4. [List Comprehensions](#list-comprehensions)
5. [Higher-Order Functions](#higher-order-functions)
6. [Function Composition](#function-composition)
7. [Immutable Data](#immutable-data)
8. [Best Practices](#best-practices)

---

## What is Functional Programming?

**Functional Programming** is a programming paradigm that:
- **Emphasizes functions**: Functions are first-class citizens
- **Avoids side effects**: Functions don't modify external state
- **Uses immutable data**: Data doesn't change after creation
- **Focuses on what, not how**: Declarative rather than imperative

**Key Concepts:**
- **Pure functions**: Same input always produces same output
- **Higher-order functions**: Functions that take/return functions
- **Immutability**: Data doesn't change
- **Function composition**: Building complex functions from simple ones

**Benefits:**
- **Easier to test**: Pure functions are predictable
- **Easier to reason about**: No hidden state changes
- **Parallelizable**: No shared state to worry about
- **More concise**: Expressive and readable code

---

## Lambda Functions

**Lambda functions** are anonymous functions defined with the `lambda` keyword.

### Basic Lambda

```python
# Regular function
def add(x, y):
    return x + y

# Lambda equivalent
add = lambda x, y: x + y

# Usage
result = add(5, 3)  # 8
```

### Lambda with map

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
# [1, 4, 9, 16, 25]
```

### Lambda with filter

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6]
```

---

## Map, Filter, and Reduce

### Map

`map()` applies a function to every item in an iterable.

```python
numbers = [1, 2, 3, 4, 5]

# Using map
squared = list(map(lambda x: x ** 2, numbers))

# Equivalent list comprehension
squared = [x ** 2 for x in numbers]
```

### Filter

`filter()` filters items based on a condition.

```python
numbers = [1, 2, 3, 4, 5, 6]

# Using filter
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Equivalent list comprehension
evens = [x for x in numbers if x % 2 == 0]
```

### Reduce

`reduce()` applies a function cumulatively to items.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum using reduce
total = reduce(lambda x, y: x + y, numbers)
# 15

# Product using reduce
product = reduce(lambda x, y: x * y, numbers)
# 120
```

---

## List Comprehensions

List comprehensions provide a concise way to create lists.

### Basic List Comprehension

```python
# Traditional approach
squares = []
for x in range(10):
    squares.append(x ** 2)

# List comprehension
squares = [x ** 2 for x in range(10)]
```

### List Comprehension with Condition

```python
# Even numbers
evens = [x for x in range(10) if x % 2 == 0]

# Squares of even numbers
squares_of_evens = [x ** 2 for x in range(10) if x % 2 == 0]
```

### Nested List Comprehensions

```python
# Matrix
matrix = [[i * j for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

---

## Higher-Order Functions

**Higher-order functions** are functions that take other functions as arguments or return functions.

### Functions as Arguments

```python
def apply_twice(func, value):
    return func(func(value))

result = apply_twice(lambda x: x * 2, 5)
# 20 (5 * 2 * 2)
```

### Functions as Return Values

```python
def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

### Built-in Higher-Order Functions

```python
# map, filter, reduce are higher-order functions
numbers = [1, 2, 3, 4, 5]

# map applies function to each element
squared = list(map(lambda x: x ** 2, numbers))

# filter applies condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

---

## Function Composition

**Function composition** combines simple functions to create complex ones.

### Basic Composition

```python
def compose(f, g):
    return lambda x: f(g(x))

# Example
add_one = lambda x: x + 1
multiply_two = lambda x: x * 2

add_then_multiply = compose(multiply_two, add_one)
result = add_then_multiply(5)  # (5 + 1) * 2 = 12
```

### Using functools.reduce for Composition

```python
from functools import reduce

def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions)

# Chain multiple functions
func = compose(lambda x: x * 2, lambda x: x + 1, lambda x: x ** 2)
result = func(3)  # ((3^2) + 1) * 2 = 20
```

---

## Immutable Data

Functional programming emphasizes immutable data.

### Tuples (Immutable)

```python
# Tuple is immutable
point = (3, 4)
# point[0] = 5  # Error!

# Create new tuple
new_point = (5, point[1])
```

### Avoiding Mutations

```python
# Instead of modifying
def add_item(items, item):
    items.append(item)  # Mutates original

# Create new list
def add_item(items, item):
    return items + [item]  # Returns new list
```

---

## Best Practices

### 1. Prefer List Comprehensions Over map/filter

```python
# Good
squares = [x ** 2 for x in range(10)]

# Also good, but less Pythonic
squares = list(map(lambda x: x ** 2, range(10)))
```

### 2. Use Lambda for Simple Functions

```python
# Good for simple operations
sorted_items = sorted(items, key=lambda x: x['age'])

# Use def for complex logic
def complex_key(item):
    # Complex logic here
    return processed_value
```

### 3. Keep Functions Pure

```python
# Pure function (good)
def add(a, b):
    return a + b

# Impure function (avoid when possible)
counter = 0
def impure_add(a, b):
    global counter
    counter += 1
    return a + b
```

### 4. Use functools for Common Patterns

```python
from functools import reduce, partial

# Partial application
def multiply(x, y):
    return x * y

double = partial(multiply, 2)
result = double(5)  # 10
```

---

## Common Mistakes to Avoid

1. **Overusing lambda**
   ```python
   # Too complex for lambda
   complex_func = lambda x: x ** 2 if x > 0 else (x * 2 if x < 0 else 0)
   
   # Better
   def complex_func(x):
       if x > 0:
           return x ** 2
       elif x < 0:
           return x * 2
       return 0
   ```

2. **Not using list comprehensions**
   ```python
   # Less Pythonic
   squares = list(map(lambda x: x ** 2, range(10)))
   
   # More Pythonic
   squares = [x ** 2 for x in range(10)]
   ```

3. **Mutating data in functions**
   ```python
   # Bad
   def process(items):
       items.sort()  # Mutates original
       return items
   
   # Good
   def process(items):
       return sorted(items)  # Returns new list
   ```

---

## Summary

- **Functional programming** emphasizes functions and immutability
- **Lambda functions** are anonymous functions
- **map, filter, reduce** are higher-order functions
- **List comprehensions** are Pythonic way to create lists
- **Higher-order functions** take/return functions
- **Function composition** combines functions
- **Immutability** avoids side effects

**Remember**: Functional programming makes code more predictable and testable. Use it where it makes sense, but don't force it everywhere!

---

## Next Steps

Now that you understand functional programming:
1. Practice with the examples in this folder
2. Use list comprehensions for data transformation
3. Write pure functions when possible
4. Explore more advanced functional programming concepts

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_functional_basics.py`: Understanding functional programming concepts
2. `02_lambda_functions.py`: Working with lambda functions
3. `03_map_filter_reduce.py`: Using map, filter, and reduce
4. `04_list_comprehensions.py`: List comprehensions and generator expressions
5. `05_higher_order_functions.py`: Higher-order functions and function composition
6. `06_practical_examples.py`: Real-world functional programming examples

Run these files in order to see functional programming in action!

