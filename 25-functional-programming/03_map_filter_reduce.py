"""
Map, Filter, and Reduce

This file demonstrates the map, filter, and reduce functions.
"""

from functools import reduce

# ============================================================================
# 1. MAP - APPLY FUNCTION TO EACH ELEMENT
# ============================================================================
print("=" * 60)
print("1. MAP - APPLY FUNCTION TO EACH ELEMENT")
print("=" * 60)

numbers = [1, 2, 3, 4, 5]

# Using map with lambda
squared = list(map(lambda x: x ** 2, numbers))
print(f"  Numbers: {numbers}")
print(f"  Squared: {squared}")

# Using map with regular function
def double(x):
    return x * 2

doubled = list(map(double, numbers))
print(f"  Doubled: {doubled}")

print()  # Empty line


# ============================================================================
# 2. FILTER - FILTER ELEMENTS BY CONDITION
# ============================================================================
print("=" * 60)
print("2. FILTER - FILTER ELEMENTS BY CONDITION")
print("=" * 60)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"  Numbers: {numbers}")
print(f"  Evens: {evens}")

# Filter numbers greater than 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"  Greater than 5: {greater_than_5}")

print()  # Empty line


# ============================================================================
# 3. REDUCE - CUMULATIVE OPERATION
# ============================================================================
print("=" * 60)
print("3. REDUCE - CUMULATIVE OPERATION")
print("=" * 60)

numbers = [1, 2, 3, 4, 5]

# Sum using reduce
total = reduce(lambda x, y: x + y, numbers)
print(f"  Numbers: {numbers}")
print(f"  Sum: {total}")

# Product using reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"  Product: {product}")

# Maximum using reduce
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(f"  Maximum: {maximum}")

print()  # Empty line


# ============================================================================
# 4. COMBINING MAP, FILTER, REDUCE
# ============================================================================
print("=" * 60)
print("4. COMBINING MAP, FILTER, REDUCE")
print("=" * 60)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Square even numbers, then sum
result = reduce(
    lambda x, y: x + y,
    map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
)
print(f"  Numbers: {numbers}")
print(f"  Sum of squares of evens: {result}")

print()  # Empty line


# ============================================================================
# 5. LIST COMPREHENSIONS VS MAP/FILTER
# ============================================================================
print("=" * 60)
print("5. LIST COMPREHENSIONS VS MAP/FILTER")
print("=" * 60)

numbers = [1, 2, 3, 4, 5]

# Using map
squared_map = list(map(lambda x: x ** 2, numbers))

# Using list comprehension
squared_comp = [x ** 2 for x in numbers]

print(f"  Using map: {squared_map}")
print(f"  Using comprehension: {squared_comp}")
print(f"  Same result, but comprehensions are more Pythonic")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("MAP, FILTER, REDUCE SUMMARY:")
print("=" * 60)
print("  - map(func, iterable): Apply function to each element")
print("  - filter(func, iterable): Filter elements by condition")
print("  - reduce(func, iterable): Cumulative operation")
print("  - Can be chained together")
print("  - List comprehensions often more Pythonic")
print("=" * 60)

