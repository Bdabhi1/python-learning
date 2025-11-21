"""
Basic Exceptions in Python

This file demonstrates what exceptions are and how to use basic
try-except blocks to handle them.
"""

# ============================================================================
# 1. WHAT ARE EXCEPTIONS?
# ============================================================================
print("=" * 60)
print("1. WHAT ARE EXCEPTIONS?")
print("=" * 60)

print("  Exceptions are errors that occur during program execution.")
print("  When an exception occurs, Python stops normal execution.")
print("  ")
print("  Example of unhandled exception:")
print("    result = 10 / 0  # ZeroDivisionError")

# This would raise an exception (commented to avoid crash)
# result = 10 / 0  # Uncomment to see the error

print("\n  Without exception handling, program crashes!")

print()  # Empty line


# ============================================================================
# 2. BASIC TRY-EXCEPT
# ============================================================================
print("=" * 60)
print("2. BASIC TRY-EXCEPT")
print("=" * 60)

# Basic try-except block
try:
    result = 10 / 0
except ZeroDivisionError:
    print("  Caught ZeroDivisionError: Cannot divide by zero!")

print("\n  Syntax:")
print("    try:")
print("        # Code that might raise exception")
print("    except ExceptionType:")
print("        # Handle the exception")

print()  # Empty line


# ============================================================================
# 3. HANDLING DIFFERENT EXCEPTIONS
# ============================================================================
print("=" * 60)
print("3. HANDLING DIFFERENT EXCEPTIONS")
print("=" * 60)

# ValueError
try:
    number = int("abc")
except ValueError:
    print("  ValueError: Cannot convert 'abc' to integer")

# TypeError
try:
    result = "hello" + 5
except TypeError:
    print("  TypeError: Cannot concatenate str and int")

# IndexError
try:
    items = [1, 2, 3]
    value = items[10]
except IndexError:
    print("  IndexError: Index 10 out of range")

# KeyError
try:
    data = {"name": "Alice"}
    value = data["age"]
except KeyError:
    print("  KeyError: Key 'age' not found in dictionary")

print()  # Empty line


# ============================================================================
# 4. GETTING EXCEPTION INFORMATION
# ============================================================================
print("=" * 60)
print("4. GETTING EXCEPTION INFORMATION")
print("=" * 60)

# Get exception message
try:
    result = int("abc")
except ValueError as e:
    print(f"  Exception message: {e}")
    print(f"  Exception type: {type(e).__name__}")

# Get exception details
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"  Exception: {e}")
    print(f"  Type: {type(e)}")

print("\n  Use 'as e' to capture exception object")

print()  # Empty line


# ============================================================================
# 5. EXCEPTION HIERARCHY
# ============================================================================
print("=" * 60)
print("5. EXCEPTION HIERARCHY")
print("=" * 60)

print("  All exceptions inherit from BaseException")
print("  ")
print("  BaseException")
print("    ├── Exception")
print("    │   ├── ValueError")
print("    │   ├── TypeError")
print("    │   ├── IndexError")
print("    │   ├── KeyError")
print("    │   └── ...")
print("    └── SystemExit, KeyboardInterrupt, ...")

print("\n  Most exceptions inherit from Exception class")

print()  # Empty line


# ============================================================================
# 6. CATCHING ALL EXCEPTIONS
# ============================================================================
print("=" * 60)
print("6. CATCHING ALL EXCEPTIONS")
print("=" * 60)

# Catch any exception (use with caution!)
try:
    result = int("abc")
except Exception as e:
    print(f"  Caught exception: {type(e).__name__}: {e}")

print("\n  Warning: Catching all exceptions can hide bugs!")
print("  Prefer catching specific exceptions when possible")

print()  # Empty line


# ============================================================================
# 7. EXCEPTION VS ERROR
# ============================================================================
print("=" * 60)
print("7. EXCEPTION VS ERROR")
print("=" * 60)

print("  In Python:")
print("    - Exceptions are objects representing errors")
print("    - All exceptions can be caught and handled")
print("    - Errors are a type of exception")
print("  ")
print("  Common terms:")
print("    - Exception: Can be caught and handled")
print("    - Error: Usually refers to exceptions")
print("    - Bug: Programming mistake (not an exception)")

print()  # Empty line


# ============================================================================
# 8. WHEN EXCEPTIONS OCCUR
# ============================================================================
print("=" * 60)
print("8. WHEN EXCEPTIONS OCCUR")
print("=" * 60)

print("  Exceptions occur when:")
print("    - Invalid operations (divide by zero)")
print("    - Type mismatches (str + int)")
print("    - Missing resources (file not found)")
print("    - Invalid input (wrong format)")
print("    - Index out of range")
print("    - Key not found in dictionary")
print("    - And many more...")

print("\n  Python raises exceptions automatically for these cases")

print()  # Empty line


# ============================================================================
# 9. EXCEPTION TRACEBACK
# ============================================================================
print("=" * 60)
print("9. EXCEPTION TRACEBACK")
print("=" * 60)

import traceback

# Get full traceback
try:
    def inner_function():
        result = 10 / 0
    
    inner_function()
except ZeroDivisionError as e:
    print("  Exception occurred!")
    print("  Full traceback:")
    traceback.print_exc()

print("\n  traceback.print_exc() shows full error trace")

print()  # Empty line


# ============================================================================
# 10. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("10. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Safe division
def safe_divide(a, b):
    """Divide two numbers safely."""
    try:
        return a / b
    except ZeroDivisionError:
        return None

result = safe_divide(10, 0)
print(f"  safe_divide(10, 0): {result}")

# Example 2: Safe conversion
def safe_int(value):
    """Convert to int safely."""
    try:
        return int(value)
    except ValueError:
        return None

result = safe_int("123")
print(f"  safe_int('123'): {result}")
result = safe_int("abc")
print(f"  safe_int('abc'): {result}")

# Example 3: Safe dictionary access
def safe_get(data, key, default=None):
    """Get value from dict safely."""
    try:
        return data[key]
    except KeyError:
        return default

data = {"name": "Alice"}
print(f"  safe_get(data, 'name'): {safe_get(data, 'name')}")
print(f"  safe_get(data, 'age'): {safe_get(data, 'age', 'Unknown')}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("BASIC EXCEPTIONS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Exceptions are errors during execution")
print("  - Use try-except to handle exceptions")
print("  - Unhandled exceptions crash the program")
print("  - Catch specific exceptions when possible")
print("  - Use 'as e' to get exception information")
print("\nBasic Syntax:")
print("  try:")
print("      # Risky code")
print("  except ExceptionType as e:")
print("      # Handle exception")
print("=" * 60)

