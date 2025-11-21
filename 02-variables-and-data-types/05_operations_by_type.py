"""
Operations by Data Type

This file demonstrates common operations available for each data type in Python.
Different data types support different operations.
"""

# ============================================================================
# INTEGER OPERATIONS
# ============================================================================
print("=" * 60)
print("INTEGER OPERATIONS")
print("=" * 60)

x, y = 10, 3

print(f"With x = {x} and y = {y}:\n")

# Arithmetic operations
print("Arithmetic Operations:")
print(f"  Addition:        {x} + {y} = {x + y}")
print(f"  Subtraction:     {x} - {y} = {x - y}")
print(f"  Multiplication:  {x} * {y} = {x * y}")
print(f"  Division:        {x} / {y} = {x / y} (returns float)")
print(f"  Floor Division:  {x} // {y} = {x // y} (returns int)")
print(f"  Modulo:          {x} % {y} = {x % y} (remainder)")
print(f"  Exponentiation:  {x} ** {y} = {x ** y}")

# Comparison operations
print("\nComparison Operations:")
print(f"  {x} > {y}  = {x > y}")
print(f"  {x} < {y}  = {x < y}")
print(f"  {x} == {y} = {x == y}")
print(f"  {x} != {y} = {x != y}")
print(f"  {x} >= {y} = {x >= y}")
print(f"  {x} <= {y} = {x <= y}")

# Built-in functions
print("\nBuilt-in Functions:")
print(f"  abs(-{x}) = {abs(-x)}")
print(f"  pow({x}, {y}) = {pow(x, y)}")
print(f"  max({x}, {y}) = {max(x, y)}")
print(f"  min({x}, {y}) = {min(x, y)}")

print()  # Empty line


# ============================================================================
# FLOAT OPERATIONS
# ============================================================================
print("=" * 60)
print("FLOAT OPERATIONS")
print("=" * 60)

a, b = 10.5, 3.2

print(f"With a = {a} and b = {b}:\n")

# Arithmetic operations (same as integers)
print("Arithmetic Operations:")
print(f"  Addition:        {a} + {b} = {a + b}")
print(f"  Subtraction:     {a} - {b} = {a - b}")
print(f"  Multiplication:  {a} * {b} = {a * b}")
print(f"  Division:        {a} / {b} = {a / b}")
print(f"  Floor Division:  {a} // {b} = {a // b}")
print(f"  Modulo:          {a} % {b} = {a % b}")
print(f"  Exponentiation:  {a} ** {b} = {a ** b}")

# Rounding
print("\nRounding Operations:")
import math
print(f"  round({a}) = {round(a)}")
print(f"  round({a}, 1) = {round(a, 1)}")
print(f"  math.floor({a}) = {math.floor(a)}")
print(f"  math.ceil({a}) = {math.ceil(a)}")

# Math functions
print("\nMath Functions:")
print(f"  abs(-{a}) = {abs(-a)}")
print(f"  math.sqrt({x}) = {math.sqrt(x):.2f}")
print(f"  math.pow({a}, 2) = {math.pow(a, 2)}")

print()  # Empty line


# ============================================================================
# STRING OPERATIONS
# ============================================================================
print("=" * 60)
print("STRING OPERATIONS")
print("=" * 60)

s1, s2 = "Hello", "World"
s = "Python Programming"

print(f"With s1 = '{s1}', s2 = '{s2}', s = '{s}':\n")

# Concatenation
print("Concatenation:")
print(f"  '{s1}' + ' ' + '{s2}' = '{s1 + ' ' + s2}'")

# Repetition
print("\nRepetition:")
print(f"  '{s1}' * 3 = '{s1 * 3}'")

# Length
print("\nLength:")
print(f"  len('{s1}') = {len(s1)}")
print(f"  len('{s}') = {len(s)}")

# Indexing (access individual characters)
print("\nIndexing (access characters):")
print(f"  '{s1}[0]' = '{s1[0]}'")
print(f"  '{s1}[1]' = '{s1[1]}'")
print(f"  '{s1}[-1]' = '{s1[-1]}' (last character)")

# Slicing (extract substrings)
print("\nSlicing (extract substrings):")
print(f"  '{s1}[1:4]' = '{s1[1:4]}'")
print(f"  '{s1}[:3]' = '{s1[:3]}' (first 3 characters)")
print(f"  '{s1}[2:]' = '{s1[2:]}' (from index 2 to end)")

# Membership (check if substring exists)
print("\nMembership (in operator):")
print(f"  'lo' in '{s1}' = {'lo' in s1}")
print(f"  'xyz' in '{s1}' = {'xyz' in s1}")

# String methods
print("\nString Methods:")
print(f"  '{s1}'.upper() = '{s1.upper()}'")
print(f"  '{s1}'.lower() = '{s1.lower()}'")
print(f"  '{s1}'.capitalize() = '{s1.capitalize()}'")
print(f"  '{s}'.replace('Python', 'Java') = '{s.replace('Python', 'Java')}'")
print(f"  '{s}'.split(' ') = {s.split(' ')}")
print(f"  '{s1}'.startswith('He') = {s1.startswith('He')}")
print(f"  '{s1}'.endswith('lo') = {s1.endswith('lo')}")

# String formatting
print("\nString Formatting:")
name, age = "Alice", 25
print(f"  f-string: f'Name: {name}, Age: {age}' = 'Name: {name}, Age: {age}'")
print(f"  .format(): 'Name: {{}}, Age: {{}}'.format('{name}', {age}) = 'Name: {name}, Age: {age}'")

print()  # Empty line


# ============================================================================
# BOOLEAN OPERATIONS
# ============================================================================
print("=" * 60)
print("BOOLEAN OPERATIONS")
print("=" * 60)

x, y = True, False

print(f"With x = {x} and y = {y}:\n")

# Logical operations
print("Logical Operations:")
print(f"  {x} and {y} = {x and y}")
print(f"  {x} or {y} = {x or y}")
print(f"  not {x} = {not x}")
print(f"  not {y} = {not y}")

# Truth tables
print("\nTruth Tables:")
print("  AND:")
print(f"    True and True  = {True and True}")
print(f"    True and False = {True and False}")
print(f"    False and True = {False and True}")
print(f"    False and False = {False and False}")

print("\n  OR:")
print(f"    True or True  = {True or True}")
print(f"    True or False = {True or False}")
print(f"    False or True = {False or True}")
print(f"    False or False = {False or False}")

# Comparison results (return booleans)
print("\nComparison Operations (return booleans):")
print(f"  5 > 3  = {5 > 3}")
print(f"  5 < 3  = {5 < 3}")
print(f"  5 == 5 = {5 == 5}")
print(f"  5 != 3 = {5 != 3}")
print(f"  5 >= 5 = {5 >= 5}")
print(f"  5 <= 3 = {5 <= 3}")

# Truthiness
print("\nTruthiness (values that evaluate to True/False):")
print(f"  bool(1) = {bool(1)}")
print(f"  bool(0) = {bool(0)}")
print(f"  bool('Hello') = {bool('Hello')}")
print(f"  bool('') = {bool('')}")
print(f"  bool([]) = {bool([])}")
print(f"  bool([1, 2]) = {bool([1, 2])}")
print(f"  bool(None) = {bool(None)}")

print()  # Empty line


# ============================================================================
# TYPE-SPECIFIC OPERATIONS SUMMARY
# ============================================================================
print("=" * 60)
print("OPERATIONS SUMMARY BY TYPE")
print("=" * 60)
print("Integers & Floats:")
print("  - Arithmetic: +, -, *, /, //, %, **")
print("  - Comparison: >, <, ==, !=, >=, <=")
print("  - Math functions: abs(), pow(), round(), etc.")
print("\nStrings:")
print("  - Concatenation: +")
print("  - Repetition: *")
print("  - Indexing: [index]")
print("  - Slicing: [start:end]")
print("  - Membership: in, not in")
print("  - Methods: .upper(), .lower(), .split(), etc.")
print("\nBooleans:")
print("  - Logical: and, or, not")
print("  - Comparison: >, <, ==, !=, >=, <=")
print("  - Truthiness: bool()")
print("=" * 60)

