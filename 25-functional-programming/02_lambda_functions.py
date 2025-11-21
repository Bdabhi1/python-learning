"""
Lambda Functions in Python

This file demonstrates anonymous functions using lambda.
"""

# ============================================================================
# 1. BASIC LAMBDA
# ============================================================================
print("=" * 60)
print("1. BASIC LAMBDA")
print("=" * 60)

# Regular function
def add(x, y):
    return x + y

# Lambda equivalent
add_lambda = lambda x, y: x + y

print(f"  Regular function: add(5, 3) = {add(5, 3)}")
print(f"  Lambda function: add_lambda(5, 3) = {add_lambda(5, 3)}")

print()  # Empty line


# ============================================================================
# 2. LAMBDA WITH SINGLE EXPRESSION
# ============================================================================
print("=" * 60)
print("2. LAMBDA WITH SINGLE EXPRESSION")
print("=" * 60)

# Square function
square = lambda x: x ** 2
print(f"  square(5) = {square(5)}")

# Is even
is_even = lambda x: x % 2 == 0
print(f"  is_even(4) = {is_even(4)}")
print(f"  is_even(5) = {is_even(5)}")

print()  # Empty line


# ============================================================================
# 3. LAMBDA WITH BUILT-IN FUNCTIONS
# ============================================================================
print("=" * 60)
print("3. LAMBDA WITH BUILT-IN FUNCTIONS")
print("=" * 60)

# Sorting
items = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
sorted_by_age = sorted(items, key=lambda x: x['age'])
print(f"  Sorted by age: {sorted_by_age}")

# Filtering
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"  Even numbers: {evens}")

print()  # Empty line


# ============================================================================
# 4. LAMBDA LIMITATIONS
# ============================================================================
print("=" * 60)
print("4. LAMBDA LIMITATIONS")
print("=" * 60)

print("  Lambda can only contain expressions, not statements:")
print("    - No print, return, if, for, while, etc.")
print("    - Only single expression")
print("  ")
print("  Use regular function for complex logic:")

def complex_function(x):
    if x > 0:
        return x ** 2
    elif x < 0:
        return x * 2
    return 0

print(f"  complex_function(5) = {complex_function(5)}")
print(f"  complex_function(-3) = {complex_function(-3)}")

print()  # Empty line


# ============================================================================
# 5. WHEN TO USE LAMBDA
# ============================================================================
print("=" * 60)
print("5. WHEN TO USE LAMBDA")
print("=" * 60)

print("  Good uses:")
print("    - Simple one-line functions")
print("    - Functions passed as arguments")
print("    - Sorting/filtering with key functions")
print("  ")
print("  Avoid:")
print("    - Complex logic (use def instead)")
print("    - Functions used multiple times (assign to variable)")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("LAMBDA FUNCTIONS SUMMARY:")
print("=" * 60)
print("  - Lambda: Anonymous function")
print("  - Syntax: lambda args: expression")
print("  - Single expression only")
print("  - Good for simple operations")
print("  - Use def for complex logic")
print("=" * 60)

