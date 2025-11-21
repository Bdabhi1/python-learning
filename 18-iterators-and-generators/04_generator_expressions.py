"""
Generator Expressions in Python

This file demonstrates generator expressions, which are like list
comprehensions but create generators.
"""

# ============================================================================
# 1. BASIC GENERATOR EXPRESSION
# ============================================================================
print("=" * 60)
print("1. BASIC GENERATOR EXPRESSION")
print("=" * 60)

# List comprehension (creates list)
squares_list = [x**2 for x in range(10)]
print(f"  List comprehension: {squares_list}")

# Generator expression (creates generator)
squares_gen = (x**2 for x in range(10))
print(f"  Generator expression: {squares_gen}")
print(f"  Converted to list: {list(squares_gen)}")

print()  # Empty line


# ============================================================================
# 2. MEMORY EFFICIENCY
# ============================================================================
print("=" * 60)
print("2. MEMORY EFFICIENCY")
print("=" * 60)

import sys

# List comprehension - stores all in memory
big_list = [x**2 for x in range(1000)]
print(f"  List size: {sys.getsizeof(big_list)} bytes")

# Generator expression - generates on demand
big_gen = (x**2 for x in range(1000))
print(f"  Generator size: {sys.getsizeof(big_gen)} bytes")

print("\n  Generator is much more memory efficient!")

print()  # Empty line


# ============================================================================
# 3. FILTERING WITH GENERATOR EXPRESSIONS
# ============================================================================
print("=" * 60)
print("3. FILTERING WITH GENERATOR EXPRESSIONS")
print("=" * 60)

# Generator with condition
evens = (x for x in range(20) if x % 2 == 0)
print(f"  Even numbers: {list(evens)}")

# Multiple conditions
filtered = (x for x in range(20) if x % 2 == 0 and x > 5)
print(f"  Filtered: {list(filtered)}")

print()  # Empty line


# ============================================================================
# 4. NESTED GENERATOR EXPRESSIONS
# ============================================================================
print("=" * 60)
print("4. NESTED GENERATOR EXPRESSIONS")
print("=" * 60)

# Nested generator
matrix = ((i * j for j in range(3)) for i in range(3))
print("  Matrix (3x3):")
for row in matrix:
    print(f"    {list(row)}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("GENERATOR EXPRESSIONS SUMMARY:")
print("=" * 60)
print("  - Syntax: (expression for item in iterable)")
print("  - Like list comprehensions but create generators")
print("  - Memory efficient - generates on demand")
print("  - Can include conditions and nested loops")
print("  - Perfect for large datasets")
print("=" * 60)

