"""
Arithmetic Operators in Python

This file demonstrates all arithmetic operators used for mathematical operations.
Arithmetic operators work with numbers (integers and floats).
"""

# ============================================================================
# 1. ADDITION (+)
# ============================================================================
print("=" * 60)
print("1. ADDITION (+)")
print("=" * 60)

# Addition with integers
result1 = 5 + 3
print(f"  5 + 3 = {result1}")

# Addition with floats
result2 = 10.5 + 2.3
print(f"  10.5 + 2.3 = {result2}")

# Addition with mixed types (int + float = float)
result3 = 5 + 3.5
print(f"  5 + 3.5 = {result3} (type: {type(result3).__name__})")

# String concatenation (also uses +)
greeting = "Hello" + " " + "World"
print(f"  'Hello' + ' ' + 'World' = '{greeting}'")

# Multiple additions
total = 10 + 20 + 30
print(f"  10 + 20 + 30 = {total}")

print()  # Empty line


# ============================================================================
# 2. SUBTRACTION (-)
# ============================================================================
print("=" * 60)
print("2. SUBTRACTION (-)")
print("=" * 60)

# Subtraction with integers
result1 = 10 - 4
print(f"  10 - 4 = {result1}")

# Subtraction with floats
result2 = 15.5 - 3.2
print(f"  15.5 - 3.2 = {result2}")

# Negative result
result3 = 5 - 10
print(f"  5 - 10 = {result3}")

# Multiple subtractions
result4 = 100 - 20 - 10
print(f"  100 - 20 - 10 = {result4}")

print()  # Empty line


# ============================================================================
# 3. MULTIPLICATION (*)
# ============================================================================
print("=" * 60)
print("3. MULTIPLICATION (*)")
print("=" * 60)

# Multiplication with integers
result1 = 4 * 5
print(f"  4 * 5 = {result1}")

# Multiplication with floats
result2 = 3.5 * 2
print(f"  3.5 * 2 = {result2}")

# Mixed types
result3 = 5 * 2.5
print(f"  5 * 2.5 = {result3}")

# String repetition (also uses *)
repeated = "Hi" * 3
print(f"  'Hi' * 3 = '{repeated}'")

# Multiple multiplications
result4 = 2 * 3 * 4
print(f"  2 * 3 * 4 = {result4}")

print()  # Empty line


# ============================================================================
# 4. DIVISION (/)
# ============================================================================
print("=" * 60)
print("4. DIVISION (/)")
print("=" * 60)

# Division always returns a float (even if result is whole number)
result1 = 10 / 2
print(f"  10 / 2 = {result1} (type: {type(result1).__name__})")

result2 = 15 / 4
print(f"  15 / 4 = {result2}")

# Division with floats
result3 = 10.5 / 2.5
print(f"  10.5 / 2.5 = {result3}")

# Division by zero (causes error)
# result4 = 10 / 0  # ZeroDivisionError!
print("  Note: Division by zero causes ZeroDivisionError")

print()  # Empty line


# ============================================================================
# 5. FLOOR DIVISION (//)
# ============================================================================
print("=" * 60)
print("5. FLOOR DIVISION (//)")
print("=" * 60)

# Floor division returns integer (rounds down)
result1 = 10 // 3
print(f"  10 // 3 = {result1} (type: {type(result1).__name__})")

result2 = 15 // 4
print(f"  15 // 4 = {result2}")

# With floats (still rounds down)
result3 = 10.5 // 2.5
print(f"  10.5 // 2.5 = {result3}")

# Negative numbers (rounds toward negative infinity)
result4 = -10 // 3
print(f"  -10 // 3 = {result4} (note: rounds toward negative infinity)")

result5 = 10 // -3
print(f"  10 // -3 = {result5}")

print()  # Empty line


# ============================================================================
# 6. MODULO (%)
# ============================================================================
print("=" * 60)
print("6. MODULO (%) - Remainder")
print("=" * 60)

# Modulo returns the remainder after division
result1 = 10 % 3
print(f"  10 % 3 = {result1} (10 divided by 3 = 3 remainder 1)")

result2 = 15 % 4
print(f"  15 % 4 = {result2}")

# When divisible, remainder is 0
result3 = 20 % 5
print(f"  20 % 5 = {result3} (no remainder)")

# With floats
result4 = 10.5 % 3.2
print(f"  10.5 % 3.2 = {result4}")

# Common use: Check if number is even or odd
number = 7
if number % 2 == 0:
    print(f"  {number} is even")
else:
    print(f"  {number} is odd")

print()  # Empty line


# ============================================================================
# 7. EXPONENTIATION (**)
# ============================================================================
print("=" * 60)
print("7. EXPONENTIATION (**)")
print("=" * 60)

# Exponentiation (power)
result1 = 2 ** 3
print(f"  2 ** 3 = {result1} (2 to the power of 3)")

result2 = 5 ** 2
print(f"  5 ** 2 = {result2} (5 squared)")

result3 = 2 ** 8
print(f"  2 ** 8 = {result3}")

# Square root (using fractional exponent)
result4 = 16 ** 0.5
print(f"  16 ** 0.5 = {result4} (square root of 16)")

result5 = 27 ** (1/3)
print(f"  27 ** (1/3) = {result5} (cube root of 27)")

# Large numbers
result6 = 10 ** 3
print(f"  10 ** 3 = {result6}")

print()  # Empty line


# ============================================================================
# 8. COMBINING OPERATORS
# ============================================================================
print("=" * 60)
print("8. COMBINING OPERATORS")
print("=" * 60)

# Multiple operations (follows operator precedence)
result1 = 2 + 3 * 4
print(f"  2 + 3 * 4 = {result1} (multiplication first)")

result2 = (2 + 3) * 4
print(f"  (2 + 3) * 4 = {result2} (parentheses change order)")

# Complex expression
result3 = 10 + 5 * 2 - 3
print(f"  10 + 5 * 2 - 3 = {result3}")

# Using variables
a = 10
b = 3
c = 2
result4 = a * b + c
print(f"  a * b + c = {a} * {b} + {c} = {result4}")

print()  # Empty line


# ============================================================================
# 9. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("9. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Calculate area of a rectangle
length = 10
width = 5
area = length * width
print(f"  Rectangle area: {length} * {width} = {area}")

# Example 2: Calculate total with tax
price = 100
tax_rate = 0.08
tax = price * tax_rate
total = price + tax
print(f"  Price: ${price}, Tax: ${tax}, Total: ${total:.2f}")

# Example 3: Check if number is divisible
number = 15
divisor = 3
if number % divisor == 0:
    print(f"  {number} is divisible by {divisor}")
else:
    print(f"  {number} is NOT divisible by {divisor}")

# Example 4: Convert seconds to minutes and seconds
total_seconds = 125
minutes = total_seconds // 60
seconds = total_seconds % 60
print(f"  {total_seconds} seconds = {minutes} minutes and {seconds} seconds")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("ARITHMETIC OPERATORS SUMMARY:")
print("=" * 60)
print("Operator | Description                    | Example")
print("---------|--------------------------------|----------")
print("+        | Addition                      | 5 + 3 = 8")
print("-        | Subtraction                   | 10 - 4 = 6")
print("*        | Multiplication                 | 4 * 5 = 20")
print("/        | Division (returns float)       | 10 / 2 = 5.0")
print("//       | Floor division (returns int)  | 10 // 3 = 3")
print("%        | Modulo (remainder)            | 10 % 3 = 1")
print("**       | Exponentiation (power)        | 2 ** 3 = 8")
print("=" * 60)
print("\nKey Points:")
print("  - Division (/) always returns float")
print("  - Floor division (//) returns integer (rounds down)")
print("  - Modulo (%) returns remainder")
print("  - Exponentiation (**) raises to power")
print("  - Operators follow precedence rules (use parentheses)")
print("=" * 60)

