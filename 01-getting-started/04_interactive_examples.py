"""
Interactive Python Examples

These examples are perfect for trying in the Python interactive shell (REPL).
Open a terminal and type 'python' or 'python3' to start the interactive shell,
then copy and paste these examples one at a time to see how they work.
"""

# ============================================================================
# BASIC ARITHMETIC
# ============================================================================
# Try these in the interactive shell:

# Addition
2 + 3

# Subtraction
10 - 4

# Multiplication
5 * 6

# Division (always returns float)
10 / 3

# Floor division (returns integer)
10 // 3

# Modulo (remainder)
10 % 3

# Exponentiation (power)
2 ** 8

# Order of operations
2 + 3 * 4  # Multiplication happens first
(2 + 3) * 4  # Parentheses change the order


# ============================================================================
# VARIABLES (Preview - we'll learn more in next lesson)
# ============================================================================
# Try these:

# Assign a value to a variable
x = 10
y = 5

# Use variables in expressions
x + y
x * y

# Reassign variables
x = 20
x + y  # Now x is 20, so result is 25


# ============================================================================
# STRING OPERATIONS
# ============================================================================
# Try these:

# Create strings
"Hello"
'World'

# Concatenate strings
"Hello" + " " + "World"

# Repeat strings
"Python " * 3

# String length (we'll learn len() function later)
len("Python")


# ============================================================================
# TYPE CHECKING
# ============================================================================
# Try these to see data types:

type(42)        # <class 'int'>
type(3.14)      # <class 'float'>
type("Hello")   # <class 'str'>
type(True)      # <class 'bool'>


# ============================================================================
# BUILT-IN FUNCTIONS
# ============================================================================
# Try these:

# Print (we've seen this)
print("Hello, World!")

# Get user input (we'll learn more later)
# name = input("What's your name? ")

# Convert types
int("42")
float("3.14")
str(123)

# Get help on any function
help(print)


# ============================================================================
# INTERACTIVE SHELL TIPS
# ============================================================================
"""
USEFUL INTERACTIVE SHELL COMMANDS:

1. _ (underscore): Stores the last result
   >>> 2 + 3
   5
   >>> _ * 2
   10

2. exit() or quit(): Exit the shell
   >>> exit()

3. Ctrl+D (Unix/Mac) or Ctrl+Z (Windows): Exit the shell

4. Up/Down arrows: Navigate command history

5. Tab completion: Auto-complete variable/function names

6. help(): Get help on any topic
   >>> help(print)
   >>> help('if')

7. dir(): See available methods/attributes
   >>> dir(str)

8. Clear screen: Ctrl+L (Unix/Mac)
"""


# ============================================================================
# PRACTICE EXERCISES FOR INTERACTIVE SHELL
# ============================================================================
"""
Try these exercises in the interactive shell:

1. Calculate your age in days (assume 365 days per year)

2. Calculate the area of a circle with radius 5
   (Formula: π × r², use 3.14159 for π)

3. Create a variable with your name and print a greeting

4. Calculate how many seconds are in a day

5. Try different arithmetic operations and see the results

6. Use the _ variable to reference previous results

7. Get help on the print function using help(print)
"""


# ============================================================================
# EXAMPLE INTERACTIVE SESSION
# ============================================================================
"""
Here's what a typical interactive session might look like:

$ python3
Python 3.11.0 (default, ...)
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello, Python!")
Hello, Python!
>>> 2 + 2
4
>>> result = 2 + 2
>>> result
4
>>> result * 3
12
>>> _ * 2
24
>>> exit()
"""

