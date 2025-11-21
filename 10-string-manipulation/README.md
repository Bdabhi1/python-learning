# String Manipulation in Python

Strings are one of the most commonly used data types in Python. This guide covers everything you need to know about working with strings, from basic operations to advanced manipulation techniques.

## Table of Contents
1. [What are Strings?](#what-are-strings)
2. [Creating Strings](#creating-strings)
3. [String Indexing and Slicing](#string-indexing-and-slicing)
4. [String Methods](#string-methods)
5. [String Formatting](#string-formatting)
6. [String Operations](#string-operations)
7. [Escape Sequences](#escape-sequences)
8. [Raw Strings](#raw-strings)
9. [Best Practices](#best-practices)

---

## What are Strings?

A **string** is a sequence of characters (letters, numbers, symbols, spaces). In Python, strings are:
- **Immutable**: Once created, they cannot be changed (you create new strings instead)
- **Ordered**: Characters have a specific position (index)
- **Iterable**: You can loop through each character

**Key characteristics:**
- Enclosed in quotes: `'single'`, `"double"`, or `"""triple"""` quotes
- Can contain any Unicode character
- Support many built-in methods for manipulation

**Example:**
```python
name = "Python"
print(name)  # Output: Python
print(type(name))  # Output: <class 'str'>
```

---

## Creating Strings

### Single and Double Quotes

```python
# Both work the same way
name1 = "Alice"
name2 = 'Bob'
print(name1)  # Alice
print(name2)  # Bob
```

**When to use which:**
- Use double quotes when your string contains single quotes
- Use single quotes when your string contains double quotes

```python
message1 = "It's a beautiful day"
message2 = 'He said "Hello"'
```

### Triple Quotes (Multi-line Strings)

```python
# Multi-line string
poem = """Roses are red,
Violets are blue,
Python is awesome,
And so are you!"""

# Also works with single quotes
poem = '''Roses are red,
Violets are blue'''
```

### String Concatenation

```python
# Using + operator
first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name
print(full_name)  # Output: Alice Smith

# Using += operator
greeting = "Hello"
greeting += " World"
print(greeting)  # Output: Hello World
```

### String Repetition

```python
# Using * operator
line = "-" * 50
print(line)  # Output: --------------------------------------------------

cheer = "Hip " * 3 + "Hooray!"
print(cheer)  # Output: Hip Hip Hip Hooray!
```

---

## String Indexing and Slicing

### Indexing

Strings are indexed starting from 0:

```python
text = "Python"
print(text[0])   # P (first character)
print(text[1])   # y
print(text[5])   # n (last character)
print(text[-1])  # n (last character, negative indexing)
print(text[-2])  # o (second from end)
```

**Negative indexing:**
- `-1` = last character
- `-2` = second from last
- And so on...

### Slicing

Extract a portion of a string using slicing:

```python
text = "Python Programming"

# Basic slicing: [start:end]
print(text[0:6])    # Python (characters 0 to 5)
print(text[7:18])   # Programming

# Omitting start (starts from beginning)
print(text[:6])     # Python

# Omitting end (goes to end)
print(text[7:])     # Programming

# Negative indices
print(text[-11:])   # Programming

# Step size
print(text[::2])    # Pto rgamn (every 2nd character)
print(text[::-1])   # gnimmargorP nohtyP (reversed)
```

**Slicing syntax:** `[start:end:step]`
- `start`: Index to start from (inclusive)
- `end`: Index to stop before (exclusive)
- `step`: How many characters to skip (default: 1)

---

## String Methods

Python provides many built-in methods for string manipulation.

### Case Conversion

```python
text = "Hello World"

text.upper()        # "HELLO WORLD"
text.lower()        # "hello world"
text.capitalize()   # "Hello world"
text.title()        # "Hello World"
text.swapcase()     # "hELLO wORLD"
```

### Checking String Content

```python
text = "Python123"

text.isalpha()      # False (contains numbers)
text.isdigit()      # False (contains letters)
text.isalnum()      # True (letters and numbers only)
text.islower()      # False (has uppercase)
text.isupper()      # False (has lowercase)
text.isspace()      # False (not just spaces)
text.startswith("Py")  # True
text.endswith("123")   # True
```

### Finding and Replacing

```python
text = "Hello World"

# Finding
text.find("World")      # 6 (index of first occurrence)
text.find("Python")     # -1 (not found)
text.index("World")     # 6 (raises error if not found)
text.count("l")         # 3 (count occurrences)

# Replacing
text.replace("World", "Python")  # "Hello Python"
text.replace("l", "L", 1)        # "HeLlo World" (replace first occurrence only)
```

### Splitting and Joining

```python
# Splitting
text = "apple,banana,orange"
fruits = text.split(",")  # ["apple", "banana", "orange"]

sentence = "Hello World Python"
words = sentence.split()  # ["Hello", "World", "Python"] (splits on whitespace)

# Joining
words = ["Hello", "World", "Python"]
sentence = " ".join(words)  # "Hello World Python"
comma_separated = ",".join(words)  # "Hello,World,Python"
```

### Stripping Whitespace

```python
text = "  Hello World  "

text.strip()    # "Hello World" (removes from both ends)
text.lstrip()   # "Hello World  " (removes from left)
text.rstrip()   # "  Hello World" (removes from right)

# Strip specific characters
text = "!!!Hello!!!"
text.strip("!")  # "Hello"
```

### Padding and Alignment

```python
text = "Hello"

text.center(11)     # "   Hello   " (centers in 11 characters)
text.ljust(10)      # "Hello     " (left-aligned)
text.rjust(10)      # "     Hello" (right-aligned)
text.zfill(8)       # "000Hello" (pads with zeros)
```

### Other Useful Methods

```python
text = "hello world"

text.capitalize()   # "Hello world"
text.title()        # "Hello World"
len(text)           # 11 (length of string)
"Python" in text    # False (membership check)
```

---

## String Formatting

Python offers multiple ways to format strings.

### f-strings (Python 3.6+) - Recommended

```python
name = "Alice"
age = 25
print(f"My name is {name} and I'm {age} years old")
# Output: My name is Alice and I'm 25 years old

# With expressions
x, y = 10, 20
print(f"The sum is {x + y}")  # Output: The sum is 30

# With formatting
pi = 3.14159
print(f"Pi is {pi:.2f}")  # Output: Pi is 3.14
```

### `.format()` Method

```python
name = "Alice"
age = 25
print("My name is {} and I'm {} years old".format(name, age))

# With positional arguments
print("{0} is {1} years old. {0} likes Python.".format(name, age))

# With named arguments
print("{name} is {age} years old".format(name="Alice", age=25))
```

### % Formatting (Old Style)

```python
name = "Alice"
age = 25
print("My name is %s and I'm %d years old" % (name, age))

# Format specifiers:
# %s - String
# %d - Integer
# %f - Float
# %.2f - Float with 2 decimal places
```

### Format Specifiers

```python
# Numbers
number = 42
print(f"{number:05d}")  # 00042 (5 digits, zero-padded)

# Floats
pi = 3.14159
print(f"{pi:.2f}")      # 3.14 (2 decimal places)
print(f"{pi:10.2f}")    # "      3.14" (10 width, 2 decimals)

# Strings
text = "Hello"
print(f"{text:>10}")    # "     Hello" (right-aligned, 10 width)
print(f"{text:<10}")    # "Hello     " (left-aligned)
print(f"{text:^10}")    # "  Hello   " (centered)
```

---

## String Operations

### Membership Testing

```python
text = "Python Programming"

"Python" in text      # True
"Java" in text        # False
"python" in text      # False (case-sensitive)
"python" in text.lower()  # True
```

### Comparison

```python
"apple" < "banana"    # True (lexicographic order)
"apple" == "Apple"    # False (case-sensitive)
"apple" != "banana"   # True
```

### Iteration

```python
# Loop through characters
text = "Hello"
for char in text:
    print(char)

# With index
for i, char in enumerate(text):
    print(f"{i}: {char}")
```

---

## Escape Sequences

Special characters in strings using backslash:

```python
# Common escape sequences
print("Hello\nWorld")      # Newline
print("Hello\tWorld")      # Tab
print("He said \"Hello\"")  # Double quote
print("It's a book")       # Single quote (or use different quotes)
print("Path: C:\\Users")   # Backslash
print("Hello\rWorld")      # Carriage return
print("Hello\bWorld")      # Backspace
```

**Common escape sequences:**
- `\n` - Newline
- `\t` - Tab
- `\"` - Double quote
- `\'` - Single quote
- `\\` - Backslash
- `\r` - Carriage return
- `\b` - Backspace

---

## Raw Strings

Raw strings ignore escape sequences (useful for file paths, regex):

```python
# Regular string
path = "C:\Users\Documents"  # Error! \U is invalid

# Raw string (prefix with r)
path = r"C:\Users\Documents"  # Correct!

# Useful for regex
pattern = r"\d+\.\d+"  # Matches numbers like "3.14"
```

---

## Best Practices

### 1. Use f-strings for Formatting

```python
# Good
name = "Alice"
age = 25
message = f"My name is {name} and I'm {age} years old"

# Less preferred
message = "My name is " + name + " and I'm " + str(age) + " years old"
```

### 2. Use `.join()` for Concatenating Many Strings

```python
# Good (efficient)
words = ["Hello", "World", "Python"]
sentence = " ".join(words)

# Less efficient
sentence = ""
for word in words:
    sentence += word + " "
```

### 3. Use String Methods Instead of Manual Checks

```python
# Good
if text.isdigit():
    number = int(text)

# Less preferred
if all(char.isdigit() for char in text):
    number = int(text)
```

### 4. Be Careful with String Immutability

```python
# Strings are immutable - operations create new strings
text = "Hello"
text.upper()  # Returns new string, doesn't modify text
print(text)   # Still "Hello"

# To change, reassign
text = text.upper()  # Now text is "HELLO"
```

### 5. Use Triple Quotes for Multi-line Strings

```python
# Good
message = """This is a
multi-line
string"""

# Less preferred
message = "This is a\nmulti-line\nstring"
```

### 6. Handle Case Sensitivity

```python
# When comparing, consider case
user_input = "YES"
if user_input.lower() == "yes":  # Case-insensitive
    print("Confirmed")
```

---

## Common Mistakes to Avoid

1. **Forgetting strings are immutable**
   ```python
   # Wrong
   text = "Hello"
   text[0] = "h"  # TypeError!
   
   # Correct - create new string
   text = "h" + text[1:]  # "hello"
   ```

2. **Using wrong quotes**
   ```python
   # Wrong
   message = "He said "Hello""  # SyntaxError
   
   # Correct
   message = "He said \"Hello\""
   # Or
   message = 'He said "Hello"'
   ```

3. **Confusing `find()` and `index()`**
   ```python
   text = "Hello"
   text.find("x")    # Returns -1 (safe)
   text.index("x")   # Raises ValueError (use with caution)
   ```

4. **Not handling empty strings**
   ```python
   # Problematic
   text = ""
   first_char = text[0]  # IndexError!
   
   # Better
   if text:
       first_char = text[0]
   ```

5. **Inefficient string concatenation in loops**
   ```python
   # Inefficient
   result = ""
   for i in range(1000):
       result += str(i)
   
   # Efficient
   result = "".join(str(i) for i in range(1000))
   ```

---

## Summary

- **Strings** are sequences of characters, immutable and ordered
- Use **indexing** `[0]` and **slicing** `[start:end]` to access parts
- Many **built-in methods** available: `upper()`, `lower()`, `split()`, `join()`, etc.
- **f-strings** are the best way to format strings (Python 3.6+)
- Strings are **immutable** - operations create new strings
- Use **raw strings** (`r""`) for paths and regex patterns
- **Escape sequences** allow special characters in strings
- Use `.join()` for efficient string concatenation

**Remember**: String manipulation is fundamental to Python programming. Master these techniques to work effectively with text data!

---

## Next Steps

Now that you understand string manipulation:
1. Practice with the examples in this folder
2. Experiment with different string methods
3. Try building text processing programs
4. Move on to **11-list-comprehensions** to learn concise ways to create lists

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_string_basics.py`: Creating and basic string operations - start here!
2. `02_string_indexing_slicing.py`: Accessing characters and substrings
3. `03_string_methods.py`: Built-in string methods
4. `04_string_formatting.py`: Formatting strings with f-strings and more
5. `05_string_operations.py`: Advanced string operations
6. `06_practical_examples.py`: Real-world string manipulation examples

Run these files in order to see string manipulation in action!

