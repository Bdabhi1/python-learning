# Input and Output in Python

Input and output (I/O) operations allow your programs to interact with users and display information. This guide covers how to get input from users and display output in Python.

## Table of Contents
1. [What is Input/Output?](#what-is-inputoutput)
2. [Output with `print()`](#output-with-print)
3. [Input with `input()`](#input-with-input)
4. [String Formatting](#string-formatting)
5. [File Input/Output Basics](#file-inputoutput-basics)
6. [Best Practices](#best-practices)

---

## What is Input/Output?

**Input/Output (I/O)** refers to how programs communicate with the outside world:
- **Input**: Getting data from users, files, or other sources
- **Output**: Displaying or saving data to users, files, or other destinations

**Common I/O operations:**
- Displaying text on screen (`print()`)
- Getting user input (`input()`)
- Reading from files
- Writing to files
- Displaying formatted output

---

## Output with `print()`

The `print()` function displays output to the console (terminal/screen).

### Basic `print()`

```python
print("Hello, World!")
# Output: Hello, World!
```

### Printing Multiple Items

```python
print("Hello", "World", "!")
# Output: Hello World !
```

**Note:** Multiple items are separated by spaces by default.

### Custom Separator

```python
print("Hello", "World", sep="-")
# Output: Hello-World
```

### Custom End Character

```python
print("Hello", end=" ")
print("World")
# Output: Hello World (on same line)
```

By default, `print()` ends with a newline (`\n`). You can change this with the `end` parameter.

### Printing Variables

```python
name = "Alice"
age = 25
print("Name:", name, "Age:", age)
# Output: Name: Alice Age: 25
```

### Printing Empty Lines

```python
print()  # Prints a blank line
print("After blank line")
```

---

## Input with `input()`

The `input()` function gets text input from the user.

### Basic `input()`

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

**How it works:**
1. Displays the prompt message
2. Waits for user to type and press Enter
3. Returns the entered text as a string

### Important: `input()` Always Returns a String

```python
age = input("Enter your age: ")
# age is a STRING, not a number!
# If user enters "25", age = "25" (string)

# To convert to integer:
age = int(input("Enter your age: "))
```

### Converting Input Types

```python
# Get integer
age = int(input("Enter age: "))

# Get float
price = float(input("Enter price: "))

# Get boolean (indirectly)
response = input("Yes or No? ").lower()
is_yes = response == "yes"
```

### Multiple Inputs

```python
name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")

print(f"{name} is {age} years old and lives in {city}")
```

---

## String Formatting

Python offers several ways to format strings for output.

### 1. f-strings (Python 3.6+) - Recommended

```python
name = "Alice"
age = 25
print(f"My name is {name} and I'm {age} years old")
# Output: My name is Alice and I'm 25 years old
```

**Advantages:**
- Most readable
- Fast
- Can include expressions

```python
x = 10
y = 20
print(f"The sum of {x} and {y} is {x + y}")
# Output: The sum of 10 and 20 is 30
```

### 2. `.format()` Method

```python
name = "Alice"
age = 25
print("My name is {} and I'm {} years old".format(name, age))
# Output: My name is Alice and I'm 25 years old
```

**With positional arguments:**
```python
print("{0} is {1} years old. {0} likes Python.".format(name, age))
```

**With named arguments:**
```python
print("{name} is {age} years old".format(name="Alice", age=25))
```

### 3. % Formatting (Old Style)

```python
name = "Alice"
age = 25
print("My name is %s and I'm %d years old" % (name, age))
# Output: My name is Alice and I'm 25 years old
```

**Format specifiers:**
- `%s` - String
- `%d` - Integer
- `%f` - Float
- `%.2f` - Float with 2 decimal places

### 4. String Concatenation

```python
name = "Alice"
age = 25
print("My name is " + name + " and I'm " + str(age) + " years old")
# Output: My name is Alice and I'm 25 years old
```

**Note:** Less preferred - use f-strings instead.

### Formatting Numbers

```python
# Float formatting
pi = 3.14159
print(f"Pi is approximately {pi:.2f}")  # 2 decimal places
# Output: Pi is approximately 3.14

# Integer formatting with padding
number = 42
print(f"Number: {number:05d}")  # 5 digits with leading zeros
# Output: Number: 00042
```

---

## File Input/Output Basics

Reading from and writing to files.

### Writing to a File

```python
# Open file for writing
with open("data.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a second line.\n")

# File is automatically closed when exiting 'with' block
```

**File modes:**
- `"w"` - Write (overwrites existing file)
- `"a"` - Append (adds to end of file)
- `"r"` - Read (default)

### Reading from a File

```python
# Read entire file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes newline
```

### Reading All Lines

```python
with open("data.txt", "r") as file:
    lines = file.readlines()  # Returns list of lines
    for line in lines:
        print(line.strip())
```

---

## Best Practices

### 1. Use f-strings for Formatting

```python
# Good
name = "Alice"
print(f"Hello, {name}!")

# Less preferred
print("Hello, " + name + "!")
```

### 2. Always Convert `input()` When Needed

```python
# Good
age = int(input("Enter age: "))

# Bad (will cause errors in calculations)
age = input("Enter age: ")  # age is a string!
```

### 3. Use `with` Statement for Files

```python
# Good - automatically closes file
with open("file.txt", "r") as file:
    content = file.read()

# Less preferred - must manually close
file = open("file.txt", "r")
content = file.read()
file.close()
```

### 4. Provide Clear Prompts

```python
# Good
name = input("Enter your name: ")

# Less clear
name = input("Name: ")
```

### 5. Handle Input Errors

```python
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Invalid input! Please enter a number.")
    age = 0
```

### 6. Use Descriptive Variable Names

```python
# Good
user_name = input("Enter your name: ")

# Less clear
n = input("Enter your name: ")
```

---

## Common Mistakes to Avoid

1. **Forgetting `input()` returns a string**
   ```python
   # Wrong
   age = input("Enter age: ")
   next_year = age + 1  # TypeError!
   
   # Correct
   age = int(input("Enter age: "))
   next_year = age + 1
   ```

2. **Not handling invalid input**
   ```python
   # Problematic
   age = int(input("Enter age: "))  # Crashes if user enters text
   
   # Better
   try:
       age = int(input("Enter age: "))
   except ValueError:
       print("Invalid input!")
   ```

3. **Forgetting to close files**
   ```python
   # Problematic
   file = open("data.txt", "w")
   file.write("Hello")
   # Forgot to close!
   
   # Better
   with open("data.txt", "w") as file:
       file.write("Hello")
   ```

4. **Using wrong file mode**
   ```python
   # Wrong - tries to read non-existent file
   with open("newfile.txt", "r") as file:
       content = file.read()
   
   # Correct - creates file for writing
   with open("newfile.txt", "w") as file:
       file.write("Hello")
   ```

---

## Summary

- **`print()`** displays output to the console
- **`input()`** gets text input from users (always returns string)
- **f-strings** are the best way to format strings
- Always **convert `input()`** to the correct type (int, float, etc.)
- Use **`with` statement** for file operations
- **Handle errors** when getting user input
- Provide **clear prompts** for better user experience

**Remember**: I/O operations make your programs interactive and useful. Master these basics to create programs that communicate with users!

---

## Next Steps

Now that you understand input and output:
1. Practice with the examples in this folder
2. Create interactive programs that get user input
3. Experiment with different formatting options
4. Move on to **06-control-flow** to learn about conditional statements and loops

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_print_basics.py`: Basic output with print() - start here!
2. `02_input_basics.py`: Getting user input with input()
3. `03_string_formatting.py`: Different ways to format strings
4. `04_file_operations.py`: Reading from and writing to files
5. `05_practical_examples.py`: Real-world I/O examples

Run these files in order to see input and output in action!

