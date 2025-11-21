# List Comprehensions in Python

List comprehensions provide a concise and elegant way to create lists in Python. They're more readable and often faster than traditional loops. This guide will teach you how to master this powerful Python feature.

## Table of Contents
1. [What are List Comprehensions?](#what-are-list-comprehensions)
2. [Basic Syntax](#basic-syntax)
3. [Conditional Comprehensions](#conditional-comprehensions)
4. [Nested Comprehensions](#nested-comprehensions)
5. [Dictionary and Set Comprehensions](#dictionary-and-set-comprehensions)
6. [When to Use List Comprehensions](#when-to-use-list-comprehensions)
7. [Performance Considerations](#performance-considerations)
8. [Best Practices](#best-practices)

---

## What are List Comprehensions?

**List comprehensions** are a Pythonic way to create lists by applying an expression to each item in an iterable (like a list, range, or string).

**Benefits:**
- **Concise**: Write less code
- **Readable**: Express intent clearly
- **Fast**: Often faster than equivalent loops
- **Pythonic**: Follows Python's philosophy of readability

**Comparison:**

```python
# Traditional approach (loop)
squares = []
for x in range(10):
    squares.append(x ** 2)

# List comprehension (concise)
squares = [x ** 2 for x in range(10)]
```

Both produce: `[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]`

---

## Basic Syntax

The general syntax is:
```python
[expression for item in iterable]
```

### Simple Examples

```python
# Square numbers
squares = [x ** 2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Convert to uppercase
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
# ["HELLO", "WORLD", "PYTHON"]

# Extract first letters
names = ["Alice", "Bob", "Charlie"]
initials = [name[0] for name in names]
# ["A", "B", "C"]

# String to list of characters
text = "Python"
chars = [char for char in text]
# ["P", "y", "t", "h", "o", "n"]
```

### Working with Different Iterables

```python
# From range
numbers = [x for x in range(5)]  # [0, 1, 2, 3, 4]

# From string
vowels = [char for char in "aeiou"]  # ["a", "e", "i", "o", "u"]

# From existing list
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]  # [2, 4, 6, 8, 10]

# From tuple
coordinates = [(1, 2), (3, 4), (5, 6)]
x_coords = [x for x, y in coordinates]  # [1, 3, 5]
```

### Using Functions in Comprehensions

```python
# Apply function to each element
numbers = [1, 2, 3, 4, 5]
squared = [pow(x, 2) for x in numbers]  # [1, 4, 9, 16, 25]

# Using built-in functions
words = ["hello", "world", "python"]
lengths = [len(word) for word in words]  # [5, 5, 6]
```

---

## Conditional Comprehensions

Add conditions to filter elements.

### Basic Filtering

```python
# Only even numbers
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Only positive numbers
numbers = [-2, -1, 0, 1, 2, 3]
positives = [x for x in numbers if x > 0]
# [1, 2, 3]

# Words longer than 5 characters
words = ["hello", "world", "python", "hi"]
long_words = [word for word in words if len(word) > 5]
# ["python"]
```

### Conditional Expression (Ternary Operator)

Use `if-else` in the expression part:

```python
# Mark even/odd
numbers = [1, 2, 3, 4, 5]
labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
# ["odd", "even", "odd", "even", "odd"]

# Absolute values
numbers = [-2, -1, 0, 1, 2]
abs_values = [x if x >= 0 else -x for x in numbers]
# [2, 1, 0, 1, 2]

# Or simply
abs_values = [abs(x) for x in numbers]
```

### Multiple Conditions

```python
# Multiple if conditions (AND)
numbers = range(20)
filtered = [x for x in numbers if x % 2 == 0 if x % 3 == 0]
# [0, 6, 12, 18] (divisible by both 2 and 3)

# Using and
filtered = [x for x in numbers if x % 2 == 0 and x % 3 == 0]

# Complex conditions
ages = [15, 18, 20, 25, 30, 35]
adults = [age for age in ages if age >= 18 and age < 65]
# [18, 20, 25, 30, 35]
```

---

## Nested Comprehensions

Create lists from nested structures or nested loops.

### Flattening Nested Lists

```python
# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Equivalent loop:
flattened = []
for row in matrix:
    for num in row:
        flattened.append(num)
```

### Creating 2D Lists

```python
# Create a 3x3 matrix
matrix = [[i * 3 + j for j in range(3)] for i in range(3)]
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# Multiplication table
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
# Creates a 5x5 multiplication table
```

### Nested with Conditions

```python
# Flatten and filter
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
evens = [num for row in matrix for num in row if num % 2 == 0]
# [2, 4, 6, 8]

# Cartesian product
colors = ["red", "green", "blue"]
sizes = ["S", "M", "L"]
combinations = [(color, size) for color in colors for size in sizes]
# [("red", "S"), ("red", "M"), ("red", "L"), ...]
```

---

## Dictionary and Set Comprehensions

Python also supports comprehensions for dictionaries and sets.

### Dictionary Comprehensions

```python
# Basic dictionary comprehension
squares = {x: x ** 2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# From list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
my_dict = {key: value for key, value in pairs}
# {"a": 1, "b": 2, "c": 3}

# With conditions
numbers = [1, 2, 3, 4, 5, 6]
even_squares = {x: x ** 2 for x in numbers if x % 2 == 0}
# {2: 4, 4: 16, 6: 36}

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {value: key for key, value in original.items()}
# {1: "a", 2: "b", 3: "c"}
```

### Set Comprehensions

```python
# Basic set comprehension
squares = {x ** 2 for x in range(5)}
# {0, 1, 4, 9, 16} (note: set, so unordered)

# Remove duplicates
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = {x for x in numbers}
# {1, 2, 3, 4}

# With conditions
evens = {x for x in range(10) if x % 2 == 0}
# {0, 2, 4, 6, 8}
```

---

## When to Use List Comprehensions

### ✅ Good Use Cases

1. **Simple transformations**
   ```python
   # Good
   squares = [x ** 2 for x in range(10)]
   ```

2. **Filtering**
   ```python
   # Good
   evens = [x for x in numbers if x % 2 == 0]
   ```

3. **Creating lists from iterables**
   ```python
   # Good
   upper_words = [word.upper() for word in words]
   ```

4. **Simple nested structures**
   ```python
   # Good
   flattened = [item for sublist in nested for item in sublist]
   ```

### ❌ When NOT to Use

1. **Complex logic** - Use a regular loop for clarity
   ```python
   # Too complex for comprehension
   result = []
   for item in data:
       if complex_condition(item):
           processed = complex_processing(item)
           if another_check(processed):
               result.append(processed)
   ```

2. **Side effects** - Comprehensions are for creating lists, not side effects
   ```python
   # Wrong - side effect
   [print(x) for x in range(10)]  # Don't do this!
   
   # Correct
   for x in range(10):
       print(x)
   ```

3. **Very long comprehensions** - Readability suffers
   ```python
   # Hard to read
   result = [f(x) for x in data if condition1(x) and condition2(x) and condition3(x)]
   
   # Better
   result = [f(x) for x in data 
             if condition1(x) and condition2(x) and condition3(x)]
   ```

---

## Performance Considerations

### List Comprehensions vs Loops

List comprehensions are generally faster:

```python
import timeit

# List comprehension
time1 = timeit.timeit('[x**2 for x in range(1000)]', number=10000)

# Loop
time2 = timeit.timeit('''
squares = []
for x in range(1000):
    squares.append(x**2)
''', number=10000)

# Comprehension is typically faster
```

**Why?**
- Optimized in C (for built-in functions)
- Less overhead than explicit loops
- More efficient memory usage

### Generator Expressions (Memory Efficient)

For large datasets, consider generator expressions:

```python
# List comprehension (creates full list in memory)
squares = [x ** 2 for x in range(1000000)]  # Uses memory

# Generator expression (lazy evaluation)
squares = (x ** 2 for x in range(1000000))  # Memory efficient
```

---

## Best Practices

### 1. Keep It Readable

```python
# Good - clear and readable
squares = [x ** 2 for x in range(10) if x % 2 == 0]

# Too complex - break it up
# Bad
result = [f(g(x)) for x in data if condition1(x) and condition2(x) and condition3(x)]

# Better
filtered = [x for x in data if condition1(x) and condition2(x) and condition3(x)]
result = [f(g(x)) for x in filtered]
```

### 2. Use Descriptive Variable Names

```python
# Good
user_ages = [person.age for person in users if person.is_active]

# Less clear
ages = [p.age for p in u if p.is_active]
```

### 3. Don't Overuse Nested Comprehensions

```python
# Too nested - hard to read
result = [[[i*j*k for k in range(3)] for j in range(3)] for i in range(3)]

# Better - use helper function or break it up
def create_cube(size):
    return [[[i*j*k for k in range(size)] for j in range(size)] for i in range(size)]
```

### 4. Use When It Improves Clarity

```python
# Good - comprehension is clearer
evens = [x for x in numbers if x % 2 == 0]

# Also good - loop might be clearer for complex logic
evens = []
for x in numbers:
    if x % 2 == 0:
        evens.append(x)
```

### 5. Combine with Functions

```python
# Good - use helper functions for complex expressions
def process_item(item):
    return item.upper().strip()

processed = [process_item(item) for item in items if item]
```

---

## Common Mistakes to Avoid

1. **Forgetting the brackets**
   ```python
   # Wrong - creates generator, not list
   squares = (x ** 2 for x in range(10))
   
   # Correct
   squares = [x ** 2 for x in range(10)]
   ```

2. **Using comprehension for side effects**
   ```python
   # Wrong - creates list of None
   [print(x) for x in range(10)]
   
   # Correct
   for x in range(10):
       print(x)
   ```

3. **Too complex comprehensions**
   ```python
   # Hard to read
   result = [f(g(h(x))) for x in data if c1(x) and c2(x) and c3(x)]
   
   # Better
   filtered = [x for x in data if c1(x) and c2(x) and c3(x)]
   result = [f(g(h(x))) for x in filtered]
   ```

4. **Variable name conflicts**
   ```python
   # Problematic - x is used in both
   x = 5
   squares = [x ** 2 for x in range(10)]  # x is shadowed
   
   # Better - use different names
   base = 5
   squares = [x ** 2 for x in range(10)]
   ```

5. **Not understanding order of operations**
   ```python
   # The if comes after the for in filtering
   evens = [x for x in range(10) if x % 2 == 0]
   
   # The if-else comes before the for in expressions
   labels = ["even" if x % 2 == 0 else "odd" for x in range(10)]
   ```

---

## Summary

- **List comprehensions** provide a concise way to create lists
- Syntax: `[expression for item in iterable]`
- Add conditions: `[expression for item in iterable if condition]`
- Use conditional expressions: `[value1 if condition else value2 for item in iterable]`
- Support **nested comprehensions** for complex structures
- **Dictionary** and **set comprehensions** work similarly
- Generally **faster** than equivalent loops
- Keep comprehensions **readable** - don't overcomplicate
- Use when it improves **clarity**, not just for the sake of it

**Remember**: List comprehensions are a powerful Python feature. Use them to write more concise and readable code, but don't sacrifice clarity for brevity!

---

## Next Steps

Now that you understand list comprehensions:
1. Practice with the examples in this folder
2. Try converting existing loops to comprehensions
3. Experiment with nested comprehensions
4. Move on to **12-modules-and-packages** to learn about organizing code

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_basic_comprehensions.py`: Basic list comprehension syntax - start here!
2. `02_conditional_comprehensions.py`: Adding conditions to comprehensions
3. `03_nested_comprehensions.py`: Working with nested structures
4. `04_dict_set_comprehensions.py`: Dictionary and set comprehensions
5. `05_advanced_examples.py`: Advanced comprehension patterns
6. `06_practical_examples.py`: Real-world list comprehension examples

Run these files in order to see list comprehensions in action!

