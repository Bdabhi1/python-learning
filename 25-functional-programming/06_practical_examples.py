"""
Practical Functional Programming Examples

This file demonstrates real-world functional programming patterns.
"""

from functools import reduce

# ============================================================================
# 1. DATA TRANSFORMATION PIPELINE
# ============================================================================
print("=" * 60)
print("1. DATA TRANSFORMATION PIPELINE")
print("=" * 60)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Pipeline: filter evens → square → sum
result = sum(x ** 2 for x in numbers if x % 2 == 0)
print(f"  Numbers: {numbers}")
print(f"  Sum of squares of evens: {result}")

print()  # Empty line


# ============================================================================
# 2. PROCESSING DATA WITH MAP
# ============================================================================
print("=" * 60)
print("2. PROCESSING DATA WITH MAP")
print("=" * 60)

names = ["alice", "bob", "charlie"]

# Capitalize names
capitalized = list(map(str.capitalize, names))
print(f"  Original: {names}")
print(f"  Capitalized: {capitalized}")

print()  # Empty line


# ============================================================================
# 3. FILTERING DATA
# ============================================================================
print("=" * 60)
print("3. FILTERING DATA")
print("=" * 60)

data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

# Filter by age
adults = list(filter(lambda x: x['age'] >= 30, data))
print(f"  Adults (age >= 30): {adults}")

print()  # Empty line


# ============================================================================
# 4. REDUCING DATA
# ============================================================================
print("=" * 60)
print("4. REDUCING DATA")
print("=" * 60)

numbers = [1, 2, 3, 4, 5]

# Calculate product
product = reduce(lambda x, y: x * y, numbers)
print(f"  Numbers: {numbers}")
print(f"  Product: {product}")

# Find maximum
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(f"  Maximum: {maximum}")

print()  # Empty line


# ============================================================================
# 5. FUNCTIONAL STYLE VS IMPERATIVE
# ============================================================================
print("=" * 60)
print("5. FUNCTIONAL STYLE VS IMPERATIVE")
print("=" * 60)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Imperative style
squares_of_evens_imperative = []
for n in numbers:
    if n % 2 == 0:
        squares_of_evens_imperative.append(n ** 2)

# Functional style
squares_of_evens_functional = [n ** 2 for n in numbers if n % 2 == 0]

print(f"  Imperative: {squares_of_evens_imperative}")
print(f"  Functional: {squares_of_evens_functional}")
print(f"  Functional is more concise and readable!")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL EXAMPLES SUMMARY:")
print("=" * 60)
print("Functional programming is useful for:")
print("  - Data transformation pipelines")
print("  - Filtering and processing data")
print("  - Creating reusable function combinations")
print("  - Writing concise, readable code")
print("=" * 60)

