# Built-in Functions in Python

Python comes with many built-in functions that are always available. These functions perform common operations and are essential tools in your Python programming toolkit.

## Table of Contents
1. [What are Built-in Functions?](#what-are-built-in-functions)
2. [Type Conversion Functions](#type-conversion-functions)
3. [Mathematical Functions](#mathematical-functions)
4. [String Functions](#string-functions)
5. [Sequence Functions](#sequence-functions)
6. [Input/Output Functions](#inputoutput-functions)
7. [Object Functions](#object-functions)
8. [Other Useful Functions](#other-useful-functions)
9. [Best Practices](#best-practices)

---

## What are Built-in Functions?

**Built-in functions** are functions that come with Python and are always available. You don't need to import them - they're ready to use!

**Characteristics:**
- Always available (no import needed)
- Perform common operations
- Well-tested and optimized
- Part of Python's core functionality

**Examples:**
- `print()` - Display output
- `len()` - Get length
- `type()` - Get type
- `int()`, `str()`, `float()` - Type conversion

---

## Type Conversion Functions

Convert data from one type to another.

### `int()`, `float()`, `str()`, `bool()`

```python
# Convert to integer
int("42")        # 42
int(3.14)        # 3 (truncates)

# Convert to float
float("3.14")    # 3.14
float(5)         # 5.0

# Convert to string
str(42)          # "42"
str(True)        # "True"

# Convert to boolean
bool(1)          # True
bool(0)          # False
bool("")         # False
```

### `list()`, `tuple()`, `set()`, `dict()`

```python
# Convert to list
list("hello")    # ['h', 'e', 'l', 'l', 'o']
list((1, 2, 3))  # [1, 2, 3]

# Convert to tuple
tuple([1, 2, 3]) # (1, 2, 3)

# Convert to set
set([1, 2, 2, 3]) # {1, 2, 3}

# Convert to dictionary
dict([("a", 1), ("b", 2)])  # {'a': 1, 'b': 2}
```

---

## Mathematical Functions

Perform mathematical operations.

### `abs()`, `round()`, `min()`, `max()`, `sum()`

```python
# Absolute value
abs(-5)          # 5
abs(5)           # 5

# Round number
round(3.14159)   # 3
round(3.14159, 2) # 3.14

# Minimum and maximum
min(1, 2, 3)     # 1
max(1, 2, 3)     # 3
min([10, 20, 30]) # 10

# Sum
sum([1, 2, 3, 4]) # 10
```

### `pow()`, `divmod()`

```python
# Power
pow(2, 3)        # 8 (2 to the power of 3)
2 ** 3           # 8 (same thing)

# Division and modulo
divmod(10, 3)    # (3, 1) - quotient and remainder
```

---

## String Functions

Work with strings.

### `len()`, `ord()`, `chr()`

```python
# Length
len("hello")     # 5

# Character to ASCII
ord("A")         # 65

# ASCII to character
chr(65)          # "A"
```

---

## Sequence Functions

Work with sequences (lists, tuples, strings, etc.).

### `len()`, `sorted()`, `reversed()`, `enumerate()`, `zip()`

```python
# Length
len([1, 2, 3])   # 3
len("hello")     # 5

# Sort
sorted([3, 1, 2])        # [1, 2, 3]
sorted([3, 1, 2], reverse=True)  # [3, 2, 1]

# Reverse
list(reversed([1, 2, 3])) # [3, 2, 1]

# Enumerate (get index and value)
for i, item in enumerate(["a", "b", "c"]):
    print(i, item)  # 0 a, 1 b, 2 c

# Zip (combine sequences)
list(zip([1, 2, 3], ["a", "b", "c"]))  # [(1, 'a'), (2, 'b'), (3, 'c')]
```

### `any()`, `all()`

```python
# Any - True if any element is True
any([False, False, True])  # True
any([False, False, False]) # False

# All - True if all elements are True
all([True, True, True])    # True
all([True, False, True])   # False
```

---

## Input/Output Functions

Handle input and output.

### `print()`, `input()`

```python
# Print
print("Hello")           # Display text
print("Hello", "World")  # Multiple items
print("Hello", end=" ")  # Custom end

# Input
name = input("Enter name: ")  # Get user input
```

---

## Object Functions

Work with objects and types.

### `type()`, `isinstance()`, `id()`, `dir()`, `help()`

```python
# Get type
type(5)          # <class 'int'>
type("hello")    # <class 'str'>

# Check type
isinstance(5, int)      # True
isinstance(5, str)      # False

# Get object ID (memory address)
id(5)            # Unique identifier

# Get attributes/methods
dir("hello")     # List of string methods

# Get help
help(print)      # Documentation for print()
```

---

## Other Useful Functions

### `range()`, `open()`, `iter()`, `next()`

```python
# Range
range(5)         # 0, 1, 2, 3, 4
range(2, 5)      # 2, 3, 4
range(0, 10, 2)  # 0, 2, 4, 6, 8

# Open file
file = open("data.txt", "r")

# Iterator
iter([1, 2, 3])
next(iterator)
```

### `hash()`, `repr()`, `eval()`, `exec()`

```python
# Hash (for dictionaries and sets)
hash("hello")    # Hash value

# Representation
repr("hello")    # "'hello'" (string representation)

# Evaluate (use with caution!)
eval("2 + 3")    # 5

# Execute (use with caution!)
exec("x = 5")
```

---

## Best Practices

1. **Use built-in functions when available**
   ```python
   # Good
   total = sum(numbers)
   
   # Less preferred
   total = 0
   for num in numbers:
       total += num
   ```

2. **Know what functions are available**
   - Check Python documentation
   - Use `dir(__builtins__)` to see all built-ins
   - Use `help()` for documentation

3. **Use appropriate functions**
   ```python
   # Good
   if isinstance(x, int):
       pass
   
   # Less preferred
   if type(x) == int:
       pass
   ```

4. **Be careful with `eval()` and `exec()`**
   - Security risk if used with user input
   - Usually not needed
   - Use alternatives when possible

---

## Common Mistakes to Avoid

1. **Forgetting parentheses**
   ```python
   # Wrong
   len my_list
   
   # Correct
   len(my_list)
   ```

2. **Using wrong function**
   ```python
   # Wrong
   type(x) == int  # Works but not recommended
   
   # Better
   isinstance(x, int)
   ```

3. **Not handling errors**
   ```python
   # Problematic
   int("abc")  # ValueError!
   
   # Better
   try:
       value = int("abc")
   except ValueError:
       value = 0
   ```

---

## Summary

- **Built-in functions** are always available in Python
- **Type conversion**: `int()`, `float()`, `str()`, `bool()`, etc.
- **Mathematical**: `abs()`, `round()`, `min()`, `max()`, `sum()`
- **Sequences**: `len()`, `sorted()`, `enumerate()`, `zip()`
- **Objects**: `type()`, `isinstance()`, `dir()`, `help()`
- Use built-ins instead of writing custom code when possible
- Check documentation with `help()` function

**Remember**: Built-in functions are powerful tools. Learn them well to write efficient Python code!

---

## Next Steps

Now that you understand built-in functions:
1. Practice with the examples in this folder
2. Explore more built-in functions with `help()`
3. Use built-ins in your programs
4. Move on to **09-functions** to learn how to create your own functions

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_type_conversion.py`: Converting between data types - start here!
2. `02_math_functions.py`: Mathematical operations
3. `03_sequence_functions.py`: Working with sequences
4. `04_object_functions.py`: Object and type operations
5. `05_utility_functions.py`: Other useful built-in functions
6. `06_practical_examples.py`: Real-world examples using built-ins

Run these files in order to see built-in functions in action!

