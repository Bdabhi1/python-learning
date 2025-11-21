"""
Nested List Comprehensions in Python

This file demonstrates nested list comprehensions for working with
nested structures and creating multi-dimensional lists.
"""

# ============================================================================
# 1. FLATTENING NESTED LISTS
# ============================================================================
print("=" * 60)
print("1. FLATTENING NESTED LISTS")
print("=" * 60)

# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"  Matrix: {matrix}")
print(f"  Flattened: {flattened}")

# Equivalent loop
flattened_loop = []
for row in matrix:
    for num in row:
        flattened_loop.append(num)
print(f"  Using loop: {flattened_loop}")
print(f"  Same result: {flattened == flattened_loop}")

# Flatten with filtering
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
evens = [num for row in matrix for num in row if num % 2 == 0]
print(f"  Matrix: {matrix}")
print(f"  Even numbers: {evens}")

print()  # Empty line


# ============================================================================
# 2. CREATING 2D LISTS
# ============================================================================
print("=" * 60)
print("2. CREATING 2D LISTS")
print("=" * 60)

# Create a 3x3 matrix
matrix = [[i * 3 + j for j in range(3)] for i in range(3)]
print(f"  3x3 matrix: {matrix}")

# Create multiplication table
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print(f"  5x5 multiplication table:")
for row in table:
    print(f"    {row}")

# Create identity matrix
size = 4
identity = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
print(f"  {size}x{size} identity matrix:")
for row in identity:
    print(f"    {row}")

print()  # Empty line


# ============================================================================
# 3. CARTESIAN PRODUCT
# ============================================================================
print("=" * 60)
print("3. CARTESIAN PRODUCT")
print("=" * 60)

# Cartesian product of two lists
colors = ["red", "green", "blue"]
sizes = ["S", "M", "L"]
combinations = [(color, size) for color in colors for size in sizes]
print(f"  Colors: {colors}")
print(f"  Sizes: {sizes}")
print(f"  Combinations: {combinations}")

# Cartesian product of three lists
numbers = [1, 2]
letters = ["a", "b"]
symbols = ["!", "@"]
all_combinations = [(n, l, s) for n in numbers for l in letters for s in symbols]
print(f"  All combinations: {all_combinations}")

print()  # Empty line


# ============================================================================
# 4. NESTED COMPREHENSIONS WITH CONDITIONS
# ============================================================================
print("=" * 60)
print("4. NESTED COMPREHENSIONS WITH CONDITIONS")
print("=" * 60)

# Flatten and filter
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
evens = [num for row in matrix for num in row if num % 2 == 0]
print(f"  Matrix: {matrix}")
print(f"  Even numbers: {evens}")

# Filter rows first, then elements
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Get numbers from rows that have sum > 10
filtered = [num for row in matrix for num in row if sum(row) > 10]
print(f"  Numbers from rows with sum > 10: {filtered}")

print()  # Empty line


# ============================================================================
# 5. WORKING WITH STRINGS
# ============================================================================
print("=" * 60)
print("5. WORKING WITH STRINGS")
print("=" * 60)

# Split sentences into words
sentences = ["Hello world", "Python is great", "Learn programming"]
all_words = [word for sentence in sentences for word in sentence.split()]
print(f"  Sentences: {sentences}")
print(f"  All words: {all_words}")

# Extract characters from words
words = ["hello", "world", "python"]
all_chars = [char for word in words for char in word]
print(f"  Words: {words}")
print(f"  All characters: {all_chars}")

# Extract vowels from multiple words
words = ["hello", "world", "python"]
vowels = [char for word in words for char in word if char.lower() in "aeiou"]
print(f"  Words: {words}")
print(f"  Vowels: {vowels}")

print()  # Empty line


# ============================================================================
# 6. CREATING NESTED STRUCTURES
# ============================================================================
print("=" * 60)
print("6. CREATING NESTED STRUCTURES")
print("=" * 60)

# Create list of lists with patterns
pattern = [[i + j for j in range(3)] for i in range(0, 9, 3)]
print(f"  Pattern: {pattern}")

# Create triangular numbers
triangular = [[j for j in range(1, i + 1)] for i in range(1, 6)]
print(f"  Triangular numbers: {triangular}")

# Create coordinate pairs
coordinates = [(x, y) for x in range(3) for y in range(3)]
print(f"  Coordinates: {coordinates}")

print()  # Empty line


# ============================================================================
# 7. PROCESSING NESTED DATA
# ============================================================================
print("=" * 60)
print("7. PROCESSING NESTED DATA")
print("=" * 60)

# Process nested tuples
people = [
    [("Alice", 25), ("Bob", 30)],
    [("Charlie", 28), ("Diana", 22)]
]
all_ages = [age for group in people for name, age in group]
print(f"  People: {people}")
print(f"  All ages: {all_ages}")

# Extract specific fields
students = [
    [{"name": "Alice", "score": 95}, {"name": "Bob", "score": 87}],
    [{"name": "Charlie", "score": 92}, {"name": "Diana", "score": 88}]
]
all_scores = [student["score"] for group in students for student in group]
print(f"  Students: {students}")
print(f"  All scores: {all_scores}")

print()  # Empty line


# ============================================================================
# 8. COMPLEX NESTED OPERATIONS
# ============================================================================
print("=" * 60)
print("8. COMPLEX NESTED OPERATIONS")
print("=" * 60)

# Transpose a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(f"  Original: {matrix}")
print(f"  Transposed: {transposed}")

# Sum of each row
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row_sums = [sum(row) for row in matrix]
print(f"  Matrix: {matrix}")
print(f"  Row sums: {row_sums}")

# Maximum in each row
matrix = [[1, 5, 3], [9, 2, 7], [4, 8, 6]]
row_maxes = [max(row) for row in matrix]
print(f"  Matrix: {matrix}")
print(f"  Row maximums: {row_maxes}")

print()  # Empty line


# ============================================================================
# 9. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("9. PRACTICAL EXAMPLES")
print("=" * 60)

# Flatten list of lists with different lengths
nested = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10]]
flattened = [item for sublist in nested for item in sublist]
print(f"  Nested: {nested}")
print(f"  Flattened: {flattened}")

# Create grid coordinates
rows = 3
cols = 4
grid = [(i, j) for i in range(rows) for j in range(cols)]
print(f"  Grid coordinates ({rows}x{cols}): {grid[:6]}...")  # Show first 6

# Process nested JSON-like data
data = [
    {"items": [("apple", 1.50), ("banana", 0.75)]},
    {"items": [("orange", 2.00), ("grape", 3.50)]}
]
all_prices = [price for group in data for item, price in group["items"]]
print(f"  Data: {data}")
print(f"  All prices: {all_prices}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("NESTED LIST COMPREHENSIONS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Flatten nested lists: [item for sublist in nested for item in sublist]")
print("  - Create 2D lists: [[expr for j in range(n)] for i in range(m)]")
print("  - Cartesian product: [(x, y) for x in list1 for y in list2]")
print("  - Can combine with conditions for filtering")
print("\nCommon Patterns:")
print("  - Flatten: [num for row in matrix for num in row]")
print("  - Create matrix: [[i*j for j in range(n)] for i in range(m)]")
print("  - Filter nested: [x for row in matrix for x in row if condition]")
print("=" * 60)

