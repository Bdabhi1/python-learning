"""
List Comprehensions

This file demonstrates list comprehensions and generator expressions.
"""

# ============================================================================
# 1. BASIC LIST COMPREHENSION
# ============================================================================
print("=" * 60)
print("1. BASIC LIST COMPREHENSION")
print("=" * 60)

# Traditional approach
squares_traditional = []
for x in range(10):
    squares_traditional.append(x ** 2)

# List comprehension
squares_comprehension = [x ** 2 for x in range(10)]

print(f"  Traditional: {squares_traditional}")
print(f"  Comprehension: {squares_comprehension}")
print(f"  Same result, more concise!")

print()  # Empty line


# ============================================================================
# 2. LIST COMPREHENSION WITH CONDITION
# ============================================================================
print("=" * 60)
print("2. LIST COMPREHENSION WITH CONDITION")
print("=" * 60)

# Even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(f"  Evens: {evens}")

# Squares of even numbers
squares_of_evens = [x ** 2 for x in range(10) if x % 2 == 0]
print(f"  Squares of evens: {squares_of_evens}")

print()  # Empty line


# ============================================================================
# 3. NESTED LIST COMPREHENSIONS
# ============================================================================
print("=" * 60)
print("3. NESTED LIST COMPREHENSIONS")
print("=" * 60)

# Matrix
matrix = [[i * j for j in range(3)] for i in range(3)]
print(f"  Matrix:")
for row in matrix:
    print(f"    {row}")

# Flatten matrix
flattened = [item for row in matrix for item in row]
print(f"  Flattened: {flattened}")

print()  # Empty line


# ============================================================================
# 4. DICTIONARY AND SET COMPREHENSIONS
# ============================================================================
print("=" * 60)
print("4. DICTIONARY AND SET COMPREHENSIONS")
print("=" * 60)

# Dictionary comprehension
squares_dict = {x: x ** 2 for x in range(5)}
print(f"  Dictionary: {squares_dict}")

# Set comprehension
squares_set = {x ** 2 for x in range(5)}
print(f"  Set: {squares_set}")

print()  # Empty line


# ============================================================================
# 5. GENERATOR EXPRESSIONS
# ============================================================================
print("=" * 60)
print("5. GENERATOR EXPRESSIONS")
print("=" * 60)

# List comprehension (creates list)
squares_list = [x ** 2 for x in range(10)]

# Generator expression (creates generator)
squares_gen = (x ** 2 for x in range(10))

print(f"  List type: {type(squares_list)}")
print(f"  Generator type: {type(squares_gen)}")
print(f"  Generator is memory efficient!")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("LIST COMPREHENSIONS SUMMARY:")
print("=" * 60)
print("  - [expr for item in iterable]: Basic comprehension")
print("  - [expr for item in iterable if condition]: With condition")
print("  - Nested comprehensions for matrices")
print("  - Dictionary/set comprehensions available")
print("  - Generator expressions for memory efficiency")
print("=" * 60)

