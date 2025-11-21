# Iterators and Generators in Python

Iterators and generators are powerful Python features that allow you to work with sequences of data efficiently. They enable lazy evaluation, memory efficiency, and elegant code patterns.

## Table of Contents
1. [What are Iterators?](#what-are-iterators)
2. [Creating Custom Iterators](#creating-custom-iterators)
3. [What are Generators?](#what-are-generators)
4. [Generator Functions](#generator-functions)
5. [Generator Expressions](#generator-expressions)
6. [Itertools Module](#itertools-module)
7. [Common Patterns](#common-patterns)
8. [Best Practices](#best-practices)

---

## What are Iterators?

An **iterator** is an object that implements the iterator protocol:
- `__iter__()`: Returns the iterator object itself
- `__next__()`: Returns the next value or raises `StopIteration`

### Built-in Iterators

```python
# Lists, tuples, strings are iterable
my_list = [1, 2, 3]
iterator = iter(my_list)

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# print(next(iterator))  # StopIteration
```

### Iterating with `for` Loop

```python
# for loop automatically handles iteration
for item in [1, 2, 3]:
    print(item)
```

---

## Creating Custom Iterators

### Iterator Class

```python
class CountDown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for num in CountDown(5):
    print(num)  # 5, 4, 3, 2, 1
```

### Iterator with `__iter__` Method

```python
class Range:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
    def __iter__(self):
        return RangeIterator(self.start, self.stop)

class RangeIterator:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop
    
    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        self.current += 1
        return self.current - 1
```

---

## What are Generators?

**Generators** are a simpler way to create iterators. They use `yield` instead of `return` and automatically implement the iterator protocol.

### Generator Function

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)  # 5, 4, 3, 2, 1
```

### Generator vs Regular Function

```python
# Regular function (returns all at once)
def squares_list(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

# Generator function (yields one at a time)
def squares_gen(n):
    for i in range(n):
        yield i ** 2

# Memory efficient - generates on demand
for square in squares_gen(1000000):
    print(square)
```

---

## Generator Functions

### Basic Generator

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib))
```

### Generator with Parameters

```python
def range_generator(start, stop, step=1):
    current = start
    while current < stop:
        yield current
        current += step

for num in range_generator(0, 10, 2):
    print(num)  # 0, 2, 4, 6, 8
```

### Generator with `send()`

```python
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

acc = accumulator()
next(acc)  # Start generator
print(acc.send(10))  # 10
print(acc.send(20))  # 30
print(acc.send(5))   # 35
```

---

## Generator Expressions

Generator expressions are like list comprehensions but create generators.

### Basic Generator Expression

```python
# List comprehension (creates list)
squares_list = [x**2 for x in range(10)]

# Generator expression (creates generator)
squares_gen = (x**2 for x in range(10))

print(list(squares_gen))  # Convert to list if needed
```

### Memory Efficiency

```python
# List comprehension - stores all in memory
big_list = [x**2 for x in range(1000000)]

# Generator expression - generates on demand
big_gen = (x**2 for x in range(1000000))

# Much more memory efficient!
```

### Filtering with Generator Expressions

```python
# Generator with condition
evens = (x for x in range(20) if x % 2 == 0)

for num in evens:
    print(num)  # 0, 2, 4, 6, 8, ...
```

---

## Itertools Module

The `itertools` module provides iterator building blocks.

### Infinite Iterators

```python
import itertools

# Count
counter = itertools.count(10, 2)
print([next(counter) for _ in range(5)])  # [10, 12, 14, 16, 18]

# Cycle
cycle = itertools.cycle(['A', 'B', 'C'])
print([next(cycle) for _ in range(5)])  # ['A', 'B', 'C', 'A', 'B']

# Repeat
repeat = itertools.repeat(5, 3)
print(list(repeat))  # [5, 5, 5]
```

### Combinatoric Iterators

```python
import itertools

# Permutations
perms = itertools.permutations([1, 2, 3], 2)
print(list(perms))  # [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]

# Combinations
combs = itertools.combinations([1, 2, 3, 4], 2)
print(list(combs))  # [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]
```

### Iterator Tools

```python
import itertools

# Chain
chain = itertools.chain([1, 2], [3, 4])
print(list(chain))  # [1, 2, 3, 4]

# Groupby
data = [1, 1, 2, 2, 2, 3]
grouped = itertools.groupby(data)
for key, group in grouped:
    print(key, list(group))  # 1 [1, 1], 2 [2, 2, 2], 3 [3]

# Tee (split iterator)
iter1, iter2 = itertools.tee([1, 2, 3], 2)
print(list(iter1))  # [1, 2, 3]
print(list(iter2))  # [1, 2, 3]
```

---

## Common Patterns

### Reading Large Files

```python
def read_large_file(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

# Memory efficient - processes one line at a time
for line in read_large_file('large_file.txt'):
    process(line)
```

### Pipeline Pattern

```python
def numbers():
    for i in range(10):
        yield i

def square(nums):
    for num in nums:
        yield num ** 2

def even(nums):
    for num in nums:
        if num % 2 == 0:
            yield num

# Chain generators
pipeline = even(square(numbers()))
print(list(pipeline))  # [0, 4, 16, 36, 64]
```

### Generator for Pagination

```python
def paginate(items, page_size):
    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]

pages = paginate(list(range(20)), 5)
for page in pages:
    print(page)
```

---

## Best Practices

### 1. Use Generators for Large Datasets

```python
# Good - memory efficient
def process_large_data():
    for item in large_dataset:
        yield process(item)

# Less preferred - loads all in memory
def process_large_data():
    return [process(item) for item in large_dataset]
```

### 2. Generator Expressions for Simple Cases

```python
# Good - simple generator
squares = (x**2 for x in range(10))

# Also good - for complex logic
def squares():
    for x in range(10):
        yield x**2
```

### 3. Don't Reuse Exhausted Generators

```python
gen = (x for x in range(5))
print(list(gen))  # [0, 1, 2, 3, 4]
print(list(gen))  # [] (exhausted!)
```

### 4. Use `itertools` for Common Patterns

```python
# Good
import itertools
chain = itertools.chain(list1, list2)

# Less preferred
chain = list1 + list2  # Creates new list
```

---

## Common Mistakes to Avoid

1. **Reusing exhausted generators**
   ```python
   gen = (x for x in range(5))
   list(gen)  # Consumes generator
   list(gen)  # Empty!
   ```

2. **Not using generators for large data**
   ```python
   # Bad - loads all in memory
   data = [process(x) for x in huge_list]
   
   # Good - processes on demand
   data = (process(x) for x in huge_list)
   ```

3. **Forgetting to call `next()` before `send()`**
   ```python
   gen = accumulator()
   gen.send(10)  # TypeError!
   next(gen)     # Must start first
   gen.send(10)  # OK
   ```

---

## Summary

- **Iterators** implement `__iter__()` and `__next__()`
- **Generators** use `yield` and are simpler iterators
- **Generator expressions** are memory-efficient comprehensions
- **`itertools`** provides useful iterator tools
- Use generators for **large datasets** and **lazy evaluation**
- Generators are **memory efficient** and **elegant**

**Remember**: Generators are perfect for processing large amounts of data without loading everything into memory!

---

## Next Steps

Now that you understand iterators and generators:
1. Practice with the examples in this folder
2. Use generators for large data processing
3. Explore the `itertools` module
4. Move on to **19-decorators** to learn about function decorators

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_iterators.py`: Understanding iterators and the iterator protocol
2. `02_custom_iterators.py`: Creating custom iterator classes
3. `03_generators.py`: Generator functions and the yield keyword
4. `04_generator_expressions.py`: Generator expressions and comprehensions
5. `05_itertools_module.py`: Using the itertools module
6. `06_practical_examples.py`: Real-world iterator and generator examples

Run these files in order to see iterators and generators in action!

