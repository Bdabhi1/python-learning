"""
Type Conversion in Python

This file demonstrates how to convert between different data types in Python.
Type conversion is essential when you need to work with different types together.
"""

# ============================================================================
# 1. IMPLICIT CONVERSION (Automatic)
# ============================================================================
print("=" * 60)
print("1. IMPLICIT CONVERSION (Automatic)")
print("=" * 60)

# Python automatically converts types in some cases
print("Automatic type conversion examples:")

# int + float = float
result = 5 + 3.14
print(f"  5 + 3.14 = {result} (type: {type(result).__name__})")

# int * float = float
result = 2 * 1.5
print(f"  2 * 1.5 = {result} (type: {type(result).__name__})")

# int / int = float (in Python 3)
result = 10 / 2
print(f"  10 / 2 = {result} (type: {type(result).__name__})")

print()  # Empty line


# ============================================================================
# 2. EXPLICIT CONVERSION - int()
# ============================================================================
print("=" * 60)
print("2. EXPLICIT CONVERSION - int()")
print("=" * 60)

# Convert to integer
print("Converting to int:")

# From float (truncates decimal part)
print(f"  int(3.14) = {int(3.14)}")
print(f"  int(3.99) = {int(3.99)}")  # Truncates, doesn't round
print(f"  int(-3.14) = {int(-3.14)}")

# From string (must be a valid integer representation)
print(f"  int('42') = {int('42')}")
print(f"  int('100') = {int('100')}")
# int('3.14')  # This would cause ValueError!

# From boolean
print(f"  int(True) = {int(True)}")
print(f"  int(False) = {int(False)}")

# Rounding before converting
print(f"\nRounding then converting:")
print(f"  int(round(3.7)) = {int(round(3.7))}")

print()  # Empty line


# ============================================================================
# 3. EXPLICIT CONVERSION - float()
# ============================================================================
print("=" * 60)
print("3. EXPLICIT CONVERSION - float()")
print("=" * 60)

# Convert to float
print("Converting to float:")

# From int
print(f"  float(5) = {float(5)}")
print(f"  float(42) = {float(42)}")

# From string
print(f"  float('3.14') = {float('3.14')}")
print(f"  float('42') = {float('42')}")
print(f"  float('3.14159') = {float('3.14159')}")

# From boolean
print(f"  float(True) = {float(True)}")
print(f"  float(False) = {float(False)}")

print()  # Empty line


# ============================================================================
# 4. EXPLICIT CONVERSION - str()
# ============================================================================
print("=" * 60)
print("4. EXPLICIT CONVERSION - str()")
print("=" * 60)

# Convert to string
print("Converting to str:")

# From int
print(f"  str(42) = '{str(42)}'")
print(f"  str(-10) = '{str(-10)}'")

# From float
print(f"  str(3.14) = '{str(3.14)}'")
print(f"  str(19.99) = '{str(19.99)}'")

# From boolean
print(f"  str(True) = '{str(True)}'")
print(f"  str(False) = '{str(False)}'")

# From None
print(f"  str(None) = '{str(None)}'")

# Practical example: concatenating numbers with strings
age = 25
# print("I am " + age + " years old")  # This would cause TypeError!
print(f"  Correct way: 'I am ' + str({age}) + ' years old' = 'I am {str(age)} years old'")

print()  # Empty line


# ============================================================================
# 5. EXPLICIT CONVERSION - bool()
# ============================================================================
print("=" * 60)
print("5. EXPLICIT CONVERSION - bool()")
print("=" * 60)

# Convert to boolean
print("Converting to bool:")

# From numbers
print(f"  bool(1) = {bool(1)}")
print(f"  bool(0) = {bool(0)}")
print(f"  bool(42) = {bool(42)}")
print(f"  bool(-1) = {bool(-1)}")  # Any non-zero number is True
print(f"  bool(0.0) = {bool(0.0)}")
print(f"  bool(3.14) = {bool(3.14)}")

# From strings
print(f"  bool('Hello') = {bool('Hello')}")  # Non-empty string
print(f"  bool('') = {bool('')}")            # Empty string is False
print(f"  bool('False') = {bool('False')}")  # Non-empty string is True!

# From None
print(f"  bool(None) = {bool(None)}")

# From collections (we'll learn these later)
print(f"  bool([]) = {bool([])}")           # Empty list
print(f"  bool([1, 2]) = {bool([1, 2])}")   # Non-empty list

print()  # Empty line


# ============================================================================
# 6. COMMON CONVERSION PATTERNS
# ============================================================================
print("=" * 60)
print("6. COMMON CONVERSION PATTERNS")
print("=" * 60)

# Pattern 1: User input (always comes as string)
print("Pattern 1: Converting user input")
user_input = "25"  # Simulating input("Enter age: ")
age = int(user_input)
print(f"  Input: '{user_input}' -> Converted to int: {age}")

# Pattern 2: Building strings with numbers
print("\nPattern 2: Building strings with numbers")
price = 19.99
quantity = 3
total = price * quantity
message = f"Total: ${total:.2f}"  # Using f-string (best way)
print(f"  {message}")

# Alternative: Using str()
message2 = "Total: $" + str(round(total, 2))
print(f"  {message2}")

# Pattern 3: Safe conversion with error handling
print("\nPattern 3: Safe conversion")
def safe_int(value):
    """Safely convert to int, return None if conversion fails."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

print(f"  safe_int('42') = {safe_int('42')}")
print(f"  safe_int('abc') = {safe_int('abc')}")
print(f"  safe_int(3.14) = {safe_int(3.14)}")

print()  # Empty line


# ============================================================================
# 7. TYPE CONVERSION ERRORS
# ============================================================================
print("=" * 60)
print("7. TYPE CONVERSION ERRORS")
print("=" * 60)

print("Common conversion errors to avoid:")

# Error 1: Converting invalid string to int
# int("3.14")  # ValueError: invalid literal for int()
print("  ❌ int('3.14') -> ValueError")
print("  ✅ Solution: int(float('3.14')) =", int(float('3.14')))

# Error 2: Converting non-numeric string to number
# int("abc")  # ValueError: invalid literal for int()
print("  ❌ int('abc') -> ValueError")
print("  ✅ Solution: Use try-except or validation")

# Error 3: Concatenating string with number
# "Age: " + 25  # TypeError: can only concatenate str to str
print("  ❌ 'Age: ' + 25 -> TypeError")
print("  ✅ Solution: 'Age: ' + str(25) = 'Age: ' + str(25)")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("TYPE CONVERSION SUMMARY:")
print("=" * 60)
print("Conversion Functions:")
print("  - int():   Convert to integer (truncates floats)")
print("  - float(): Convert to floating-point number")
print("  - str():   Convert to string")
print("  - bool():  Convert to boolean")
print("\nKey Points:")
print("  - Python automatically converts int + float -> float")
print("  - Use explicit conversion when needed")
print("  - Be careful with invalid conversions (use try-except)")
print("  - str() is useful for concatenating numbers with strings")
print("  - bool() follows truthiness rules (empty = False, else = True)")
print("=" * 60)

