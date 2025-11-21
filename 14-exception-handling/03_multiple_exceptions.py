"""
Handling Multiple Exceptions

This file demonstrates how to handle multiple different exceptions
in a single try-except block.
"""

# ============================================================================
# 1. MULTIPLE EXCEPT CLAUSES
# ============================================================================
print("=" * 60)
print("1. MULTIPLE EXCEPT CLAUSES")
print("=" * 60)

# Handle different exceptions separately
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"  Result: {result}")
except ValueError:
    print("  ValueError: Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("  ZeroDivisionError: Cannot divide by zero!")

# Simulated example
print("\n  Example with simulated input:")
try:
    number = int("5")  # Simulated: user enters "5"
    result = 10 / number
    print(f"  Result: {result}")
except ValueError:
    print("  ValueError: Invalid input!")
except ZeroDivisionError:
    print("  ZeroDivisionError: Cannot divide by zero!")

print()  # Empty line


# ============================================================================
# 2. CATCHING MULTIPLE IN ONE HANDLER
# ============================================================================
print("=" * 60)
print("2. CATCHING MULTIPLE IN ONE HANDLER")
print("=" * 60)

# Catch multiple exceptions in one except clause
try:
    # Code that might raise different exceptions
    value = int("abc")
except (ValueError, TypeError) as e:
    print(f"  Caught ValueError or TypeError: {e}")

try:
    items = [1, 2, 3]
    value = items[10]
except (IndexError, KeyError) as e:
    print(f"  Caught IndexError or KeyError: {e}")

print("\n  Syntax: except (Exception1, Exception2) as e:")

print()  # Empty line


# ============================================================================
# 3. ORDER OF EXCEPT HANDLERS
# ============================================================================
print("=" * 60)
print("3. ORDER OF EXCEPT HANDLERS")
print("=" * 60)

# More specific exceptions first
try:
    result = int("abc") / 0
except ValueError:
    print("  ValueError: Invalid number")
except ZeroDivisionError:
    print("  ZeroDivisionError: Division by zero")
except Exception:
    print("  Other exception")

print("\n  Order matters: More specific exceptions first")
print("  General Exception should be last")

print()  # Empty line


# ============================================================================
# 4. HANDLING FILE OPERATIONS
# ============================================================================
print("=" * 60)
print("4. HANDLING FILE OPERATIONS")
print("=" * 60)

# Multiple exceptions for file operations
try:
    with open("data.txt", "r") as file:
        number = int(file.read())
        result = 10 / number
except FileNotFoundError:
    print("  FileNotFoundError: File not found!")
except ValueError:
    print("  ValueError: Invalid number in file!")
except ZeroDivisionError:
    print("  ZeroDivisionError: Cannot divide by zero!")
except PermissionError:
    print("  PermissionError: Access denied!")

print("\n  File operations can raise multiple exception types")

print()  # Empty line


# ============================================================================
# 5. NESTED TRY-EXCEPT
# ============================================================================
print("=" * 60)
print("5. NESTED TRY-EXCEPT")
print("=" * 60)

# Nested try-except blocks
try:
    try:
        number = int("abc")
    except ValueError:
        print("  Inner: ValueError caught")
        number = 0
    
    result = 10 / number
except ZeroDivisionError:
    print("  Outer: ZeroDivisionError caught")

print("\n  Can nest try-except blocks for fine-grained control")

print()  # Empty line


# ============================================================================
# 6. EXCEPTION CHAINING
# ============================================================================
print("=" * 60)
print("6. EXCEPTION CHAINING")
print("=" * 60)

# Handle exception and raise another
try:
    try:
        number = int("abc")
    except ValueError as e:
        raise TypeError("Invalid type") from e
except TypeError as e:
    print(f"  TypeError: {e}")
    print(f"  Caused by: {e.__cause__}")

print("\n  Can chain exceptions to show cause")

print()  # Empty line


# ============================================================================
# 7. HANDLING WITH GENERAL EXCEPTION
# ============================================================================
print("=" * 60)
print("7. HANDLING WITH GENERAL EXCEPTION")
print("=" * 60)

# Specific exceptions first, then general
try:
    # Risky operation
    result = int("5") / 0
except ValueError:
    print("  ValueError: Invalid number")
except ZeroDivisionError:
    print("  ZeroDivisionError: Division by zero")
except Exception as e:
    print(f"  Unexpected error: {type(e).__name__}: {e}")

print("\n  General Exception catches anything not handled above")

print()  # Empty line


# ============================================================================
# 8. COMPLEX ERROR HANDLING
# ============================================================================
print("=" * 60)
print("8. COMPLEX ERROR HANDLING")
print("=" * 60)

def process_data(data):
    """Process data with comprehensive error handling."""
    try:
        # Try to get value
        value = data["number"]
        
        # Try to convert
        number = int(value)
        
        # Try to calculate
        result = 100 / number
        
        return result
    except KeyError:
        return "Error: 'number' key not found"
    except ValueError:
        return "Error: Invalid number format"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except Exception as e:
        return f"Error: {type(e).__name__}: {e}"

# Test different scenarios
test_cases = [
    {"number": "10"},
    {"number": "abc"},
    {"number": "0"},
    {"other": "value"}
]

for i, test in enumerate(test_cases, 1):
    result = process_data(test)
    print(f"  Test {i}: {result}")

print()  # Empty line


# ============================================================================
# 9. PRACTICAL EXAMPLE: CALCULATOR
# ============================================================================
print("=" * 60)
print("9. PRACTICAL EXAMPLE: CALCULATOR")
print("=" * 60)

def calculate(operation, a, b):
    """Perform calculation with error handling."""
    try:
        a = float(a)
        b = float(b)
        
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            return a / b
        else:
            raise ValueError(f"Unknown operation: {operation}")
    except ValueError as e:
        return f"ValueError: {e}"
    except ZeroDivisionError:
        return "ZeroDivisionError: Cannot divide by zero"
    except Exception as e:
        return f"Error: {e}"

# Test calculator
print("  calculate('+', '5', '3'):", calculate("+", "5", "3"))
print("  calculate('/', '10', '0'):", calculate("/", "10", "0"))
print("  calculate('*', 'abc', '2'):", calculate("*", "abc", "2"))

print()  # Empty line


# ============================================================================
# 10. BEST PRACTICES
# ============================================================================
print("=" * 60)
print("10. BEST PRACTICES")
print("=" * 60)

print("  When handling multiple exceptions:")
print("    1. Handle specific exceptions first")
print("    2. Put general Exception last")
print("    3. Use tuple to catch multiple in one handler")
print("    4. Provide helpful error messages")
print("    5. Don't suppress exceptions silently")
print("    6. Log exceptions for debugging")

print("\n  Example structure:")
print("    try:")
print("        # Code")
print("    except SpecificError1:")
print("        # Handle specific error")
print("    except SpecificError2:")
print("        # Handle another specific error")
print("    except (Error3, Error4):")
print("        # Handle multiple errors")
print("    except Exception:")
print("        # Handle any other error")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("MULTIPLE EXCEPTIONS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Can have multiple except clauses")
print("  - Handle specific exceptions first")
print("  - Use tuple to catch multiple: except (E1, E2)")
print("  - General Exception should be last")
print("  - Can nest try-except blocks")
print("  - Order of handlers matters")
print("\nBest Practices:")
print("  - Specific before general")
print("  - Group related exceptions")
print("  - Provide clear error messages")
print("=" * 60)

