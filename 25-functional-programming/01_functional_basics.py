"""
Functional Programming Basics

This file demonstrates the fundamental concepts of functional programming.
"""

# ============================================================================
# 1. WHAT IS FUNCTIONAL PROGRAMMING?
# ============================================================================
print("=" * 60)
print("1. WHAT IS FUNCTIONAL PROGRAMMING?")
print("=" * 60)

print("  Functional Programming is a paradigm that:")
print("    - Emphasizes functions as first-class citizens")
print("    - Avoids side effects and mutations")
print("    - Uses immutable data")
print("    - Focuses on 'what' not 'how'")
print("  ")
print("  Key Concepts:")
print("    - Pure functions: Same input → same output")
print("    - Higher-order functions: Functions that take/return functions")
print("    - Immutability: Data doesn't change")
print("    - Function composition: Build complex from simple")

print()  # Empty line


# ============================================================================
# 2. PURE FUNCTIONS
# ============================================================================
print("=" * 60)
print("2. PURE FUNCTIONS")
print("=" * 60)

# Pure function (no side effects)
def add(a, b):
    return a + b

result1 = add(5, 3)
result2 = add(5, 3)
print(f"  add(5, 3) = {result1}")
print(f"  Always returns same result: {result1 == result2}")

# Impure function (has side effects)
counter = 0
def impure_add(a, b):
    global counter
    counter += 1
    return a + b

print(f"\n  Pure functions are predictable and testable")
print(f"  Impure functions have side effects (like modifying counter)")

print()  # Empty line


# ============================================================================
# 3. IMMUTABILITY
# ============================================================================
print("=" * 60)
print("3. IMMUTABILITY")
print("=" * 60)

# Immutable: Tuple
point = (3, 4)
print(f"  Original point: {point}")
# point[0] = 5  # Error! Tuple is immutable

# Create new tuple instead
new_point = (5, point[1])
print(f"  New point: {new_point}")
print(f"  Original unchanged: {point}")

print("\n  Immutability prevents accidental modifications")

print()  # Empty line


# ============================================================================
# 4. FUNCTIONS AS FIRST-CLASS CITIZENS
# ============================================================================
print("=" * 60)
print("4. FUNCTIONS AS FIRST-CLASS CITIZENS")
print("=" * 60)

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

# Functions can be assigned to variables
func = square
print(f"  func(5) = {func(5)}")

# Functions can be stored in lists
functions = [square, cube]
print(f"  functions[0](3) = {functions[0](3)}")
print(f"  functions[1](3) = {functions[1](3)}")

print("\n  Functions are first-class: can be assigned, passed, returned")

print()  # Empty line


# ============================================================================
# 5. DECLARATIVE VS IMPERATIVE
# ============================================================================
print("=" * 60)
print("5. DECLARATIVE VS IMPERATIVE")
print("=" * 60)

numbers = [1, 2, 3, 4, 5]

# Imperative (how)
squares_imperative = []
for n in numbers:
    squares_imperative.append(n ** 2)

# Declarative (what)
squares_declarative = [n ** 2 for n in numbers]

print(f"  Imperative: {squares_imperative}")
print(f"  Declarative: {squares_declarative}")
print(f"  Same result, different approach")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("FUNCTIONAL PROGRAMMING BASICS SUMMARY:")
print("=" * 60)
print("  - Pure functions: No side effects")
print("  - Immutability: Data doesn't change")
print("  - Functions as first-class: Can be passed around")
print("  - Declarative: Focus on 'what' not 'how'")
print("  - Easier to test and reason about")
print("=" * 60)

