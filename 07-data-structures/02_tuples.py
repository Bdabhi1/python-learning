"""
Tuples in Python

This file demonstrates tuples - ordered, immutable collections.
Tuples are like lists but cannot be modified after creation.
"""

# ============================================================================
# 1. CREATING TUPLES
# ============================================================================
print("=" * 60)
print("1. CREATING TUPLES")
print("=" * 60)

# Empty tuple
empty_tuple = ()
print(f"  Empty tuple: {empty_tuple}")

# Tuple with items
coordinates = (10, 20)
print(f"  Coordinates: {coordinates}")

# Single item tuple (note the comma!)
single = (5,)
print(f"  Single item: {single}, type: {type(single)}")
not_tuple = (5)  # This is just an integer!
print(f"  (5) without comma: {not_tuple}, type: {type(not_tuple)}")

# Without parentheses (tuple packing)
point = 10, 20, 30
print(f"  Without parentheses: {point}")

# Using tuple() constructor
numbers = tuple([1, 2, 3])
print(f"  From list: {numbers}")

print()  # Empty line


# ============================================================================
# 2. ACCESSING ELEMENTS
# ============================================================================
print("=" * 60)
print("2. ACCESSING ELEMENTS")
print("=" * 60)

point = (10, 20, 30, 40, 50)

# Access by index
print(f"  point[0]: {point[0]}")
print(f"  point[1]: {point[1]}")

# Negative indexing
print(f"  point[-1]: {point[-1]} (last)")
print(f"  point[-2]: {point[-2]} (second from end)")

# Slicing
print(f"  point[1:3]: {point[1:3]}")
print(f"  point[:3]: {point[:3]}")
print(f"  point[2:]: {point[2:]}")

print()  # Empty line


# ============================================================================
# 3. TUPLES ARE IMMUTABLE
# ============================================================================
print("=" * 60)
print("3. TUPLES ARE IMMUTABLE")
print("=" * 60)

point = (10, 20)
print(f"  Original: {point}")

# Cannot modify
# point[0] = 5  # TypeError!

# Cannot add
# point.append(30)  # AttributeError!

# Cannot remove
# point.remove(10)  # AttributeError!

print("  Tuples cannot be modified after creation")
print("  To change, create a new tuple:")

# Create new tuple
point = (5, 20)  # New tuple
print(f"  New tuple: {point}")

print()  # Empty line


# ============================================================================
# 4. TUPLE OPERATIONS
# ============================================================================
print("=" * 60)
print("4. TUPLE OPERATIONS")
print("=" * 60)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Length
print(f"  len((1, 2, 3)): {len(tuple1)}")

# Membership
print(f"  2 in (1, 2, 3): {2 in tuple1}")

# Concatenation
combined = tuple1 + tuple2
print(f"  (1,2,3) + (4,5,6): {combined}")

# Repetition
repeated = tuple1 * 3
print(f"  (1,2,3) * 3: {repeated}")

# Count
numbers = (1, 2, 2, 3, 2, 4)
print(f"  (1,2,2,3,2,4).count(2): {numbers.count(2)}")

# Index
fruits = ("apple", "banana", "orange")
print(f"  ('apple','banana','orange').index('banana'): {fruits.index('banana')}")

print()  # Empty line


# ============================================================================
# 5. TUPLE UNPACKING
# ============================================================================
print("=" * 60)
print("5. TUPLE UNPACKING")
print("=" * 60)

# Unpack into variables
point = (10, 20)
x, y = point
print(f"  point = (10, 20)")
print(f"  x, y = point")
print(f"  x = {x}, y = {y}")

# Multiple values
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"\n  coordinates = (10, 20, 30)")
print(f"  x, y, z = coordinates")
print(f"  x = {x}, y = {y}, z = {z}")

# Swap variables (elegant!)
a, b = 5, 10
print(f"\n  Before swap: a = {a}, b = {b}")
a, b = b, a
print(f"  After swap: a = {a}, b = {b}")

print()  # Empty line


# ============================================================================
# 6. RETURNING MULTIPLE VALUES
# ============================================================================
print("=" * 60)
print("6. RETURNING MULTIPLE VALUES")
print("=" * 60)

# Functions can return tuples
def get_name_age():
    return "Alice", 25

name, age = get_name_age()
print(f"  Function returned: name = {name}, age = {age}")

# Or receive as tuple
result = get_name_age()
print(f"  As tuple: {result}")

# Calculate and return multiple values
def divide_with_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide_with_remainder(17, 5)
print(f"  17 / 5: quotient = {q}, remainder = {r}")

print()  # Empty line


# ============================================================================
# 7. TUPLES AS DICTIONARY KEYS
# ============================================================================
print("=" * 60)
print("7. TUPLES AS DICTIONARY KEYS")
print("=" * 60)

# Tuples are hashable (can be dictionary keys)
# Lists cannot be dictionary keys!

locations = {
    (0, 0): "Origin",
    (10, 20): "Point A",
    (30, 40): "Point B"
}

print("  Dictionary with tuple keys:")
for key, value in locations.items():
    print(f"    {key}: {value}")

# Access by tuple key
print(f"\n  locations[(10, 20)]: {locations[(10, 20)]}")

print("\n  Note: Lists cannot be dictionary keys (they're mutable)")

print()  # Empty line


# ============================================================================
# 8. NESTED TUPLES
# ============================================================================
print("=" * 60)
print("8. NESTED TUPLES")
print("=" * 60)

# Tuples can contain other tuples
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print("  Nested tuple (matrix):")
for row in matrix:
    print(f"    {row}")

# Access nested elements
print(f"\n  matrix[0][1]: {matrix[0][1]}")
print(f"  matrix[2][2]: {matrix[2][2]}")

print()  # Empty line


# ============================================================================
# 9. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("9. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: RGB colors
print("Example 1: RGB Colors")
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
print(f"  Red: {red}")
print(f"  Green: {green}")
print(f"  Blue: {blue}")

# Example 2: Coordinates
print("\nExample 2: Coordinates")
points = [(0, 0), (10, 20), (30, 40)]
print("  Points:")
for i, (x, y) in enumerate(points, 1):
    print(f"    Point {i}: ({x}, {y})")

# Example 3: Database records
print("\nExample 3: Database Records")
users = [
    ("Alice", 25, "alice@example.com"),
    ("Bob", 30, "bob@example.com"),
    ("Charlie", 35, "charlie@example.com")
]
print("  Users:")
for name, age, email in users:
    print(f"    {name}, {age}, {email}")

# Example 4: Multiple return values
print("\nExample 4: Function Returning Multiple Values")
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

numbers = [10, 20, 30, 40, 50]
min_val, max_val, avg = get_stats(numbers)
print(f"  Numbers: {numbers}")
print(f"  Min: {min_val}, Max: {max_val}, Avg: {avg:.2f}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("TUPLES SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Ordered collection of items")
print("  - IMMUTABLE (cannot be modified)")
print("  - Allows duplicates")
print("  - Indexed (0-based)")
print("  - Faster than lists")
print("  - Can be dictionary keys")
print("\nCommon Uses:")
print("  - Returning multiple values from functions")
print("  - Unpacking multiple values")
print("  - Fixed data that shouldn't change")
print("  - Dictionary keys")
print("  - Coordinates, RGB colors, etc.")
print("=" * 60)

