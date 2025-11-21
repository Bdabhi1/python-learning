"""
Assignment Operators in Python

This file demonstrates assignment operators that assign values to variables,
including compound assignment operators that perform an operation and assign.
"""

# ============================================================================
# 1. BASIC ASSIGNMENT (=)
# ============================================================================
print("=" * 60)
print("1. BASIC ASSIGNMENT (=)")
print("=" * 60)

# Simple assignment
x = 5
print(f"  x = 5, x is now: {x}")

# Assign multiple variables
a = b = c = 0
print(f"  a = b = c = 0, a={a}, b={b}, c={c}")

# Multiple assignment (unpacking)
x, y, z = 1, 2, 3
print(f"  x, y, z = 1, 2, 3, x={x}, y={y}, z={z}")

# Reassignment
x = 10
print(f"  x = 10, x is now: {x}")

print()  # Empty line


# ============================================================================
# 2. ADDITION ASSIGNMENT (+=)
# ============================================================================
print("=" * 60)
print("2. ADDITION ASSIGNMENT (+=)")
print("=" * 60)

# += adds and assigns
x = 5
print(f"  Initial: x = {x}")
x += 3  # Equivalent to: x = x + 3
print(f"  After x += 3: x = {x}")

# With floats
y = 10.5
y += 2.5
print(f"  y = 10.5, after y += 2.5: y = {y}")

# With strings (concatenation)
text = "Hello"
text += " World"
print(f"  text = 'Hello', after text += ' World': text = '{text}'")

# With lists
my_list = [1, 2]
my_list += [3, 4]  # Extends the list
print(f"  my_list = [1, 2], after my_list += [3, 4]: {my_list}")

print()  # Empty line


# ============================================================================
# 3. SUBTRACTION ASSIGNMENT (-=)
# ============================================================================
print("=" * 60)
print("3. SUBTRACTION ASSIGNMENT (-=)")
print("=" * 60)

# -= subtracts and assigns
x = 10
print(f"  Initial: x = {x}")
x -= 4  # Equivalent to: x = x - 4
print(f"  After x -= 4: x = {x}")

# With floats
y = 15.5
y -= 3.2
print(f"  y = 15.5, after y -= 3.2: y = {y}")

print()  # Empty line


# ============================================================================
# 4. MULTIPLICATION ASSIGNMENT (*=)
# ============================================================================
print("=" * 60)
print("4. MULTIPLICATION ASSIGNMENT (*=)")
print("=" * 60)

# *= multiplies and assigns
x = 5
print(f"  Initial: x = {x}")
x *= 3  # Equivalent to: x = x * 3
print(f"  After x *= 3: x = {x}")

# With floats
y = 2.5
y *= 4
print(f"  y = 2.5, after y *= 4: y = {y}")

# With strings (repetition)
text = "Hi"
text *= 3
print(f"  text = 'Hi', after text *= 3: text = '{text}'")

print()  # Empty line


# ============================================================================
# 5. DIVISION ASSIGNMENT (/=)
# ============================================================================
print("=" * 60)
print("5. DIVISION ASSIGNMENT (/=)")
print("=" * 60)

# /= divides and assigns (always returns float)
x = 10
print(f"  Initial: x = {x} (type: {type(x).__name__})")
x /= 2  # Equivalent to: x = x / 2
print(f"  After x /= 2: x = {x} (type: {type(x).__name__})")

# With floats
y = 15.0
y /= 3
print(f"  y = 15.0, after y /= 3: y = {y}")

print()  # Empty line


# ============================================================================
# 6. FLOOR DIVISION ASSIGNMENT (//=)
# ============================================================================
print("=" * 60)
print("6. FLOOR DIVISION ASSIGNMENT (//=)")
print("=" * 60)

# //= performs floor division and assigns
x = 10
print(f"  Initial: x = {x}")
x //= 3  # Equivalent to: x = x // 3
print(f"  After x //= 3: x = {x}")

# With floats (still rounds down)
y = 15.5
y //= 2.5
print(f"  y = 15.5, after y //= 2.5: y = {y}")

print()  # Empty line


# ============================================================================
# 7. MODULO ASSIGNMENT (%=)
# ============================================================================
print("=" * 60)
print("7. MODULO ASSIGNMENT (%=)")
print("=" * 60)

# %= performs modulo and assigns
x = 10
print(f"  Initial: x = {x}")
x %= 3  # Equivalent to: x = x % 3
print(f"  After x %= 3: x = {x}")

# Practical: Keep number in range
number = 25
number %= 10  # Keeps number between 0 and 9
print(f"  number = 25, after number %= 10: {number}")

print()  # Empty line


# ============================================================================
# 8. EXPONENTIATION ASSIGNMENT (**=)
# ============================================================================
print("=" * 60)
print("8. EXPONENTIATION ASSIGNMENT (**=)")
print("=" * 60)

# **= performs exponentiation and assigns
x = 2
print(f"  Initial: x = {x}")
x **= 3  # Equivalent to: x = x ** 3
print(f"  After x **= 3: x = {x}")

# Square a number
y = 5
y **= 2
print(f"  y = 5, after y **= 2: y = {y}")

print()  # Empty line


# ============================================================================
# 9. COMPARING WITH REGULAR ASSIGNMENT
# ============================================================================
print("=" * 60)
print("9. COMPARING WITH REGULAR ASSIGNMENT")
print("=" * 60)

# Method 1: Using compound assignment (shorter)
x = 10
x += 5
print(f"  Using +=: x = 10, x += 5, x = {x}")

# Method 2: Using regular assignment (longer, but clearer for beginners)
y = 10
y = y + 5
print(f"  Using =: y = 10, y = y + 5, y = {y}")

print("\n  Both methods produce the same result!")
print("  Compound assignment is shorter and more Pythonic")

print()  # Empty line


# ============================================================================
# 10. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("10. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Counter
counter = 0
print(f"  Counter: {counter}")
counter += 1
print(f"  After increment: {counter}")
counter += 1
print(f"  After another increment: {counter}")

# Example 2: Accumulator
total = 0
numbers = [10, 20, 30]
for num in numbers:
    total += num
    print(f"  Added {num}, total = {total}")

# Example 3: String building
message = "Hello"
message += ", "
message += "World"
message += "!"
print(f"\n  Built message: '{message}'")

# Example 4: Price calculation
price = 100
price *= 1.08  # Add 8% tax
print(f"\n  Price with tax: ${price:.2f}")

# Example 5: Power of 2
power = 2
for i in range(4):
    power **= 2
    print(f"  Power of 2, iteration {i+1}: {power}")

print()  # Empty line


# ============================================================================
# 11. CHAINING ASSIGNMENTS (NOT POSSIBLE WITH COMPOUND)
# ============================================================================
print("=" * 60)
print("11. CHAINING ASSIGNMENTS")
print("=" * 60)

# Regular assignment can be chained
a = b = c = 10
print(f"  a = b = c = 10: a={a}, b={b}, c={c}")

# Compound assignment cannot be chained
x = 5
x += 3
# y = x += 3  # ❌ SyntaxError! Cannot chain compound assignment
print("  Note: Compound assignment cannot be chained")
print("  Use separate statements instead")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("ASSIGNMENT OPERATORS SUMMARY:")
print("=" * 60)
print("Operator | Description              | Equivalent To")
print("---------|---------------------------|-------------------")
print("=        | Assignment                | x = value")
print("+=       | Add and assign            | x = x + value")
print("-=       | Subtract and assign       | x = x - value")
print("*=       | Multiply and assign       | x = x * value")
print("/=       | Divide and assign         | x = x / value")
print("//=      | Floor divide and assign   | x = x // value")
print("%=       | Modulo and assign         | x = x % value")
print("**=      | Exponentiate and assign   | x = x ** value")
print("=" * 60)
print("\nKey Points:")
print("  - Compound assignment is shorter: x += 1 vs x = x + 1")
print("  - Both methods produce the same result")
print("  - Compound assignment is more Pythonic")
print("  - Cannot chain compound assignments")
print("  - Works with numbers, strings, and other types")
print("=" * 60)

