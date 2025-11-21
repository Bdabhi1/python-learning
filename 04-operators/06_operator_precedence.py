"""
Operator Precedence in Python

This file demonstrates operator precedence - the order in which Python
evaluates operators when multiple operators are present in an expression.
Understanding precedence helps avoid bugs and write clearer code.
"""

# ============================================================================
# 1. WHAT IS OPERATOR PRECEDENCE?
# ============================================================================
print("=" * 60)
print("1. WHAT IS OPERATOR PRECEDENCE?")
print("=" * 60)

# When multiple operators are in an expression, Python evaluates them
# in a specific order based on precedence

# Example: What is the result?
result = 2 + 3 * 4
print(f"  2 + 3 * 4 = {result}")
print("  Multiplication (*) has higher precedence than addition (+)")
print("  So: 2 + (3 * 4) = 2 + 12 = 14")

# With parentheses (changes order)
result2 = (2 + 3) * 4
print(f"\n  (2 + 3) * 4 = {result2}")
print("  Parentheses override precedence")

print()  # Empty line


# ============================================================================
# 2. PRECEDENCE ORDER (HIGH TO LOW)
# ============================================================================
print("=" * 60)
print("2. PRECEDENCE ORDER (HIGH TO LOW)")
print("=" * 60)

print("1. Parentheses () - Highest precedence")
print("2. Exponentiation **")
print("3. Unary operators: +x, -x, ~x, not x")
print("4. Multiplication, Division, Floor Division, Modulo: *, /, //, %")
print("5. Addition, Subtraction: +, -")
print("6. Bitwise shifts: <<, >>")
print("7. Bitwise AND: &")
print("8. Bitwise XOR: ^")
print("9. Bitwise OR: |")
print("10. Comparison: ==, !=, <, >, <=, >=, is, is not, in, not in")
print("11. Logical NOT: not")
print("12. Logical AND: and")
print("13. Logical OR: or")
print("14. Assignment: =, +=, -=, etc. - Lowest precedence")

print()  # Empty line


# ============================================================================
# 3. ARITHMETIC PRECEDENCE
# ============================================================================
print("=" * 60)
print("3. ARITHMETIC PRECEDENCE")
print("=" * 60)

# Exponentiation first
result1 = 2 ** 3 * 2
print(f"  2 ** 3 * 2 = {result1}")
print("  (2 ** 3) * 2 = 8 * 2 = 16")

# Multiplication/Division before Addition/Subtraction
result2 = 2 + 3 * 4
print(f"\n  2 + 3 * 4 = {result2}")
print("  2 + (3 * 4) = 2 + 12 = 14")

# Multiple operations
result3 = 10 - 2 * 3 + 4
print(f"\n  10 - 2 * 3 + 4 = {result3}")
print("  Evaluated as: 10 - (2 * 3) + 4 = 10 - 6 + 4 = 8")

# Same precedence: left to right
result4 = 10 / 2 * 3
print(f"\n  10 / 2 * 3 = {result4}")
print("  Same precedence, left to right: (10 / 2) * 3 = 5 * 3 = 15")

print()  # Empty line


# ============================================================================
# 4. PARENTHESES OVERRIDE PRECEDENCE
# ============================================================================
print("=" * 60)
print("4. PARENTHESES OVERRIDE PRECEDENCE")
print("=" * 60)

# Without parentheses
result1 = 2 + 3 * 4
print(f"  2 + 3 * 4 = {result1}")

# With parentheses (changes order)
result2 = (2 + 3) * 4
print(f"  (2 + 3) * 4 = {result2}")

# Complex example
result3 = 2 + 3 * 4 ** 2
print(f"\n  2 + 3 * 4 ** 2 = {result3}")
print("  Evaluated as: 2 + (3 * (4 ** 2)) = 2 + (3 * 16) = 2 + 48 = 50")

result4 = (2 + 3) * 4 ** 2
print(f"  (2 + 3) * 4 ** 2 = {result4}")
print("  Evaluated as: (2 + 3) * (4 ** 2) = 5 * 16 = 80")

print("\n  Key Point: Use parentheses to make precedence clear!")

print()  # Empty line


# ============================================================================
# 5. LOGICAL OPERATOR PRECEDENCE
# ============================================================================
print("=" * 60)
print("5. LOGICAL OPERATOR PRECEDENCE")
print("=" * 60)

# NOT has higher precedence than AND/OR
result1 = not True and False
print(f"  not True and False = {result1}")
print("  Evaluated as: (not True) and False = False and False = False")

result2 = not (True and False)
print(f"  not (True and False) = {result2}")
print("  Evaluated as: not (False) = True")

# AND has higher precedence than OR
result3 = True or False and False
print(f"\n  True or False and False = {result3}")
print("  Evaluated as: True or (False and False) = True or False = True")

result4 = (True or False) and False
print(f"  (True or False) and False = {result4}")
print("  Evaluated as: True and False = False")

print()  # Empty line


# ============================================================================
# 6. COMPARISON OPERATOR PRECEDENCE
# ============================================================================
print("=" * 60)
print("6. COMPARISON OPERATOR PRECEDENCE")
print("=" * 60)

# Comparisons have lower precedence than arithmetic
result1 = 5 + 3 > 6
print(f"  5 + 3 > 6 = {result1}")
print("  Evaluated as: (5 + 3) > 6 = 8 > 6 = True")

# Multiple comparisons
result2 = 1 < 2 < 3
print(f"\n  1 < 2 < 3 = {result2}")
print("  Chained comparison: 1 < 2 and 2 < 3 = True")

# Comparison with arithmetic
result3 = 2 * 3 == 6
print(f"\n  2 * 3 == 6 = {result3}")
print("  Evaluated as: (2 * 3) == 6 = 6 == 6 = True")

print()  # Empty line


# ============================================================================
# 7. MIXED OPERATORS
# ============================================================================
print("=" * 60)
print("7. MIXED OPERATORS")
print("=" * 60)

# Arithmetic and comparison
result1 = 2 + 3 * 4 > 10
print(f"  2 + 3 * 4 > 10 = {result1}")
print("  Evaluated as: (2 + (3 * 4)) > 10 = 14 > 10 = True")

# Arithmetic, comparison, and logical
result2 = 5 + 3 > 6 and 2 * 2 == 4
print(f"\n  5 + 3 > 6 and 2 * 2 == 4 = {result2}")
print("  Evaluated as: ((5 + 3) > 6) and ((2 * 2) == 4)")
print("  = (8 > 6) and (4 == 4) = True and True = True")

# Complex expression
result3 = not 2 + 3 * 4 > 15
print(f"\n  not 2 + 3 * 4 > 15 = {result3}")
print("  Evaluated as: not ((2 + (3 * 4)) > 15)")
print("  = not (14 > 15) = not False = True")

print()  # Empty line


# ============================================================================
# 8. ASSIGNMENT OPERATOR PRECEDENCE
# ============================================================================
print("=" * 60)
print("8. ASSIGNMENT OPERATOR PRECEDENCE")
print("=" * 60)

# Assignment has lowest precedence
x = 2 + 3 * 4
print(f"  x = 2 + 3 * 4")
print(f"  x = {x}")
print("  Right side evaluated first, then assigned")

# Multiple assignments
a = b = c = 5
print(f"\n  a = b = c = 5")
print(f"  a = {a}, b = {b}, c = {c}")
print("  All assigned the same value (right to left)")

# Assignment with operation
x = 10
x += 2 * 3
print(f"\n  x = 10, then x += 2 * 3")
print(f"  x = {x}")
print("  Evaluated as: x = x + (2 * 3) = 10 + 6 = 16")

print()  # Empty line


# ============================================================================
# 9. BEST PRACTICES - USE PARENTHESES
# ============================================================================
print("=" * 60)
print("9. BEST PRACTICES - USE PARENTHESES")
print("=" * 60)

# Unclear (relies on precedence)
result1 = 2 + 3 * 4
print(f"  Unclear: 2 + 3 * 4 = {result1}")

# Clear (explicit parentheses)
result2 = 2 + (3 * 4)
print(f"  Clear: 2 + (3 * 4) = {result2}")

# Complex expression - unclear
result3 = not x > 5 and y < 10 or z == 0
print("\n  Unclear: not x > 5 and y < 10 or z == 0")
print("  Hard to understand precedence")

# Clear with parentheses
# result4 = ((not (x > 5)) and (y < 10)) or (z == 0)
print("  Clear: ((not (x > 5)) and (y < 10)) or (z == 0)")
print("  Much easier to understand!")

print("\n  Best Practice: Use parentheses even when not strictly necessary")
print("  It makes your code clearer and prevents bugs")

print()  # Empty line


# ============================================================================
# 10. COMMON PRECEDENCE MISTAKES
# ============================================================================
print("=" * 60)
print("10. COMMON PRECEDENCE MISTAKES")
print("=" * 60)

# Mistake 1: Assuming left-to-right for all operations
result1 = 2 ** 3 ** 2
print(f"  2 ** 3 ** 2 = {result1}")
print("  Exponentiation is right-associative: 2 ** (3 ** 2) = 2 ** 9 = 512")
print("  Not: (2 ** 3) ** 2 = 8 ** 2 = 64")

# Mistake 2: Forgetting that comparison has lower precedence
x = 5
result2 = x + 3 > 7
print(f"\n  x = 5, x + 3 > 7 = {result2}")
print("  Evaluated as: (x + 3) > 7 = 8 > 7 = True")

# Mistake 3: Logical operator precedence
result3 = True or False and False
print(f"\n  True or False and False = {result3}")
print("  AND has higher precedence: True or (False and False) = True")
print("  Not: (True or False) and False = True and False = False")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("OPERATOR PRECEDENCE SUMMARY:")
print("=" * 60)
print("Key Rules:")
print("  1. Parentheses () have highest precedence")
print("  2. Exponentiation **")
print("  3. Unary operators: +, -, ~, not")
print("  4. *, /, //, % (same precedence, left to right)")
print("  5. +, - (same precedence, left to right)")
print("  6. Comparison operators: ==, !=, <, >, <=, >=, is, in, etc.")
print("  7. Logical NOT: not")
print("  8. Logical AND: and")
print("  9. Logical OR: or")
print("  10. Assignment: =, +=, -=, etc. (lowest)")
print("\nBest Practices:")
print("  - Use parentheses to make precedence clear")
print("  - Don't rely on remembering precedence rules")
print("  - When in doubt, add parentheses")
print("  - Write code that's easy to read and understand")
print("=" * 60)

