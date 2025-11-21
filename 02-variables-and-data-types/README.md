# Variables and Data Types in Python

Understanding variables and data types is fundamental to programming. This guide will teach you everything you need to know about storing and working with different types of data in Python.

## Table of Contents
1. [What are Variables?](#what-are-variables)
2. [Variable Naming Rules](#variable-naming-rules)
3. [Assigning Values to Variables](#assigning-values-to-variables)
4. [Data Types in Python](#data-types-in-python)
5. [Type Checking](#type-checking)
6. [Type Conversion](#type-conversion)
7. [Dynamic Typing](#dynamic-typing)
8. [Common Operations by Type](#common-operations-by-type)
9. [Best Practices](#best-practices)

---

## What are Variables?

A **variable** is like a labeled container that stores data. Think of it as a box with a name tag where you can put different things.

**Real-world analogy:**
- Imagine a storage box labeled "books" - you can put books in it
- In programming, a variable named `age` can store the number 25
- You can change what's in the box, but the label (variable name) stays the same

**Key concepts:**
- Variables store data (numbers, text, etc.)
- Variables have names (identifiers)
- You can change the value stored in a variable
- Variables make code reusable and readable

**Example:**
```python
name = "Alice"
age = 25
print(name)  # Output: Alice
print(age)   # Output: 25
```

---

## Variable Naming Rules

Python has specific rules for naming variables. Following these rules is essential!

### ✅ Valid Variable Names

1. **Must start with a letter or underscore**
   ```python
   name = "John"      # ✅ Valid
   _name = "John"     # ✅ Valid
   name1 = "John"     # ✅ Valid
   ```

2. **Can contain letters, numbers, and underscores**
   ```python
   user_name = "John"     # ✅ Valid
   user_name_2 = "John"   # ✅ Valid
   user2name = "John"     # ✅ Valid
   ```

3. **Case-sensitive**
   ```python
   name = "John"
   Name = "Jane"      # Different variable!
   NAME = "Bob"       # Different variable!
   ```

### ❌ Invalid Variable Names

1. **Cannot start with a number**
   ```python
   2name = "John"     # ❌ SyntaxError
   ```

2. **Cannot use Python keywords**
   ```python
   if = 5              # ❌ SyntaxError (if is a keyword)
   def = "function"    # ❌ SyntaxError (def is a keyword)
   ```

3. **Cannot contain spaces or special characters**
   ```python
   user name = "John"  # ❌ SyntaxError
   user-name = "John"  # ❌ SyntaxError
   user@name = "John"  # ❌ SyntaxError
   ```

### Python Keywords (Cannot be used as variable names)
```
and, as, assert, break, class, continue, def, del, elif, else, except,
exec, finally, for, from, global, if, import, in, is, lambda, not, or,
pass, print, raise, return, try, while, with, yield
```

### Naming Conventions (Best Practices)

1. **Use descriptive names**
   ```python
   # Good
   user_age = 25
   total_price = 100.50
   
   # Bad
   a = 25
   x = 100.50
   ```

2. **Use snake_case (recommended for Python)**
   ```python
   user_name = "John"
   total_items = 10
   is_active = True
   ```

3. **Use UPPER_CASE for constants**
   ```python
   PI = 3.14159
   MAX_CONNECTIONS = 100
   ```

4. **Avoid single letters (except for loop counters)**
   ```python
   # Good for loops
   for i in range(10):
       print(i)
   
   # Bad for variables
   x = get_user_name()  # What is x?
   ```

---

## Assigning Values to Variables

### Basic Assignment

Use the `=` operator to assign values:

```python
# Assign a single value
name = "Alice"
age = 25
price = 19.99

# Assign multiple variables (unpacking)
x, y, z = 1, 2, 3
name, age = "Alice", 25

# Assign same value to multiple variables
x = y = z = 0
```

### Reassigning Variables

Variables can be reassigned with new values:

```python
age = 25
print(age)  # Output: 25

age = 26    # Reassign
print(age)  # Output: 26
```

### Multiple Assignment

Python allows elegant multiple assignments:

```python
# Swap two variables (no temporary variable needed!)
a, b = 10, 20
a, b = b, a  # Now a=20, b=10
```

---

## Data Types in Python

Python has several built-in data types. Understanding each is crucial!

### 1. Integers (int)

Whole numbers (positive, negative, or zero).

```python
age = 25
temperature = -10
count = 0
big_number = 1000000
```

**Characteristics:**
- No decimal point
- Can be arbitrarily large (unlike some languages)
- Supports all basic arithmetic operations

### 2. Floating-Point Numbers (float)

Numbers with decimal points.

```python
price = 19.99
temperature = 98.6
pi = 3.14159
scientific = 1.5e3  # 1500.0 (scientific notation)
```

**Characteristics:**
- Always have a decimal point (or use scientific notation)
- Have limited precision
- Used for measurements, calculations requiring decimals

### 3. Strings (str)

Text data - sequences of characters.

```python
name = "Alice"
greeting = 'Hello'
message = """Multi-line
string"""
```

**Characteristics:**
- Enclosed in single `'`, double `"`, or triple `"""` quotes
- Immutable (cannot be changed once created)
- Support many operations (concatenation, slicing, etc.)

**Common operations:**
```python
name = "Python"
len(name)              # Length: 6
name.upper()           # "PYTHON"
name.lower()           # "python"
"Py" in name           # True
name + " is cool"      # "Python is cool"
```

### 4. Booleans (bool)

Represents truth values: `True` or `False`.

```python
is_active = True
is_complete = False
is_raining = True
```

**Characteristics:**
- Only two values: `True` and `False`
- Used in conditional statements and logic
- Case-sensitive (must be `True`/`False`, not `true`/`false`)

**Boolean operations:**
```python
True and False    # False
True or False     # True
not True          # False
```

### 5. None Type

Represents the absence of a value.

```python
result = None
data = None
```

**Characteristics:**
- Only one value: `None`
- Similar to `null` in other languages
- Used to indicate "no value" or "not set"
- `None` is falsy (evaluates to `False` in boolean context)

---

## Type Checking

You can check the type of a variable using the `type()` function or `isinstance()`.

### Using `type()`

```python
age = 25
print(type(age))        # <class 'int'>

price = 19.99
print(type(price))      # <class 'float'>

name = "Alice"
print(type(name))       # <class 'str'>

is_active = True
print(type(is_active))  # <class 'bool'>

result = None
print(type(result))     # <class 'NoneType'>
```

### Using `isinstance()`

```python
age = 25
print(isinstance(age, int))      # True
print(isinstance(age, str))      # False
```

**Why use `isinstance()`?**
- More Pythonic
- Handles inheritance better
- Preferred in production code

---

## Type Conversion

Sometimes you need to convert data from one type to another.

### Implicit Conversion (Automatic)

Python automatically converts types in some cases:

```python
# int + float = float
result = 5 + 3.14  # Result is 8.14 (float)

# int * float = float
result = 2 * 1.5   # Result is 3.0 (float)
```

### Explicit Conversion (Manual)

Use built-in functions to convert types:

#### `int()` - Convert to Integer
```python
int(3.14)        # 3 (truncates decimal)
int("42")        # 42
int(True)        # 1
int(False)       # 0
```

#### `float()` - Convert to Float
```python
float(5)         # 5.0
float("3.14")    # 3.14
float(True)      # 1.0
```

#### `str()` - Convert to String
```python
str(42)          # "42"
str(3.14)        # "3.14"
str(True)        # "True"
str(None)        # "None"
```

#### `bool()` - Convert to Boolean
```python
bool(1)          # True
bool(0)          # False
bool("")         # False (empty string)
bool("Hello")    # True (non-empty string)
bool(None)       # False
```

**Important conversion rules:**
- Empty strings, `0`, `None`, empty containers → `False`
- Everything else → `True`

---

## Dynamic Typing

Python is **dynamically typed**, meaning:
- You don't declare variable types
- Types are determined at runtime
- Variables can change types

```python
# Same variable, different types
x = 5           # x is an int
x = "Hello"     # Now x is a str
x = 3.14        # Now x is a float
x = True        # Now x is a bool
```

**Advantages:**
- Flexible and easy to use
- Less code to write
- Great for rapid development

**Disadvantages:**
- Can lead to type-related errors
- Need to be careful about types
- Type hints (Python 3.5+) help with this

---

## Common Operations by Type

### Integer Operations
```python
x, y = 10, 3

x + y    # 13 (addition)
x - y    # 7 (subtraction)
x * y    # 30 (multiplication)
x / y    # 3.333... (division, returns float)
x // y   # 3 (floor division, returns int)
x % y    # 1 (modulo, remainder)
x ** y   # 1000 (exponentiation)
```

### Float Operations
```python
x, y = 10.5, 3.2

x + y    # 13.7
x - y    # 7.3
x * y    # 33.6
x / y    # 3.28125
x // y   # 3.0 (floor division)
x % y    # 0.8999999999999995
x ** y   # Exponentiation
```

### String Operations
```python
s1, s2 = "Hello", "World"

s1 + s2           # "HelloWorld" (concatenation)
s1 * 3            # "HelloHelloHello" (repetition)
len(s1)           # 5 (length)
s1[0]             # "H" (indexing)
s1[1:4]           # "ell" (slicing)
"lo" in s1        # True (membership)
s1.upper()        # "HELLO" (methods)
```

### Boolean Operations
```python
x, y = True, False

x and y    # False
x or y     # True
not x      # False
```

---

## Best Practices

1. **Use descriptive variable names**
   ```python
   # Good
   user_age = 25
   
   # Bad
   ua = 25
   ```

2. **Choose appropriate data types**
   ```python
   # Use int for whole numbers
   count = 10
   
   # Use float for decimals
   price = 19.99
   
   # Use str for text
   name = "Alice"
   ```

3. **Be aware of type conversions**
   ```python
   # Explicit is better than implicit
   age = int(input("Enter age: "))
   ```

4. **Use type hints (Python 3.5+)**
   ```python
   def greet(name: str) -> str:
       return f"Hello, {name}!"
   ```

5. **Check types when necessary**
   ```python
   if isinstance(value, int):
       # Process integer
   ```

6. **Understand truthiness**
   ```python
   # These are all False:
   bool(0)
   bool("")
   bool(None)
   bool([])
   ```

---

## Common Mistakes to Avoid

1. **Using wrong quotes**
   ```python
   name = "Alice"  # ✅ Correct
   name = 'Alice'  # ✅ Also correct
   name = Alice    # ❌ Wrong (no quotes = variable name)
   ```

2. **Confusing = and ==**
   ```python
   x = 5    # Assignment
   x == 5   # Comparison (returns True/False)
   ```

3. **Type errors**
   ```python
   # This will cause an error:
   "5" + 3  # TypeError: can only concatenate str to str
   
   # Fix:
   "5" + str(3)  # "53"
   int("5") + 3  # 8
   ```

4. **Forgetting Python is case-sensitive**
   ```python
   Name = "Alice"
   print(name)  # NameError: name not defined
   ```

---

## Summary

- **Variables** are containers that store data
- Python has **5 main data types**: int, float, str, bool, None
- Variables are **dynamically typed** (types determined at runtime)
- Use **descriptive names** following naming conventions
- **Type conversion** allows changing between types
- **Type checking** helps ensure correct data types
- Follow **best practices** for clean, maintainable code

**Remember**: Understanding variables and data types is the foundation of programming. Master these concepts before moving forward!

---

## Next Steps

Now that you understand variables and data types:
1. Practice creating variables of different types
2. Experiment with type conversions
3. Try the examples in this folder
4. Move on to **03-variables-and-scope** to learn about variable scope and lifetime

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_basic_variables.py`: Basic variable creation and usage - start here!
2. `02_variable_naming.py`: Examples of good and bad variable names
3. `03_data_types_demo.py`: Comprehensive examples of all data types
4. `04_type_conversion.py`: Examples of converting between types
5. `05_operations_by_type.py`: Common operations for each data type

Run these files in order to see variables and data types in action!

