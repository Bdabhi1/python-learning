"""
Nested Loops in Python

This file demonstrates nested loops - loops inside other loops.
Useful for working with 2D data, grids, and combinations.
"""

# ============================================================================
# 1. BASIC NESTED FOR LOOPS
# ============================================================================
print("=" * 60)
print("1. BASIC NESTED FOR LOOPS")
print("=" * 60)

# Simple nested loop
print("  Nested loop pattern:")
for i in range(3):
    for j in range(3):
        print(f"    ({i}, {j})", end=" ")
    print()  # New line after inner loop

print("\n  Structure:")
print("    for outer in sequence:")
print("        for inner in sequence:")
print("            # Code executes outer * inner times")

print()  # Empty line


# ============================================================================
# 2. MULTIPLICATION TABLE
# ============================================================================
print("=" * 60)
print("2. MULTIPLICATION TABLE")
print("=" * 60)

# Create multiplication table
print("  Multiplication table (5x5):")
print("    ", end="")
for i in range(1, 6):
    print(f"{i:4}", end="")
print()  # New line
print("    " + "-" * 20)

for i in range(1, 6):
    print(f"  {i}|", end="")
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()  # New line

print()  # Empty line


# ============================================================================
# 3. PATTERN PRINTING
# ============================================================================
print("=" * 60)
print("3. PATTERN PRINTING")
print("=" * 60)

# Right triangle
print("  Right triangle:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Square
print("\n  Square (5x5):")
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

# Hollow square
print("\n  Hollow square (5x5):")
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()  # Empty line


# ============================================================================
# 4. ITERATING OVER 2D DATA
# ============================================================================
print("=" * 60)
print("4. ITERATING OVER 2D DATA")
print("=" * 60)

# 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("  Matrix:")
for row in matrix:
    for element in row:
        print(f"{element:3}", end=" ")
    print()

# Access by index
print("\n  Matrix with indices:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"    matrix[{i}][{j}] = {matrix[i][j]}")

print()  # Empty line


# ============================================================================
# 5. COMBINATIONS AND PERMUTATIONS
# ============================================================================
print("=" * 60)
print("5. COMBINATIONS AND PERMUTATIONS")
print("=" * 60)

# Generate pairs
print("  All pairs from two lists:")
list1 = ["A", "B", "C"]
list2 = [1, 2]

for item1 in list1:
    for item2 in list2:
        print(f"    ({item1}, {item2})")

# Cartesian product
print("\n  Cartesian product:")
colors = ["red", "blue"]
sizes = ["S", "M", "L"]

for color in colors:
    for size in sizes:
        print(f"    {color} {size}")

print()  # Empty line


# ============================================================================
# 6. NESTED WHILE LOOPS
# ============================================================================
print("=" * 60)
print("6. NESTED WHILE LOOPS")
print("=" * 60)

# Nested while loops
print("  Nested while loops:")
i = 0
while i < 3:
    j = 0
    while j < 3:
        print(f"    ({i}, {j})", end=" ")
        j += 1
    print()
    i += 1

print()  # Empty line


# ============================================================================
# 7. BREAK AND CONTINUE IN NESTED LOOPS
# ============================================================================
print("=" * 60)
print("7. BREAK AND CONTINUE IN NESTED LOOPS")
print("=" * 60)

# break in nested loop (exits inner loop only)
print("  Break in inner loop (exits inner only):")
for i in range(3):
    print(f"    Outer: {i}")
    for j in range(5):
        if j == 2:
            break  # Exits inner loop
        print(f"      Inner: {j}")

# continue in nested loop
print("\n  Continue in inner loop:")
for i in range(3):
    print(f"    Outer: {i}")
    for j in range(5):
        if j == 2:
            continue  # Skips to next inner iteration
        print(f"      Inner: {j}")

print()  # Empty line


# ============================================================================
# 8. SEARCHING IN 2D STRUCTURES
# ============================================================================
print("=" * 60)
print("8. SEARCHING IN 2D STRUCTURES")
print("=" * 60)

# Search for value in matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
target = 5
found = False

print(f"  Searching for {target} in matrix:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == target:
            print(f"    Found at position ({i}, {j})")
            found = True
            break
    if found:
        break  # Exit outer loop too

if not found:
    print(f"    {target} not found")

print()  # Empty line


# ============================================================================
# 9. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("9. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Sum of matrix
print("Example 1: Sum of matrix")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
total = 0
for row in matrix:
    for element in row:
        total += element
print(f"  Matrix sum: {total}")

# Example 2: Transpose matrix
print("\nExample 2: Transpose matrix")
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print("  Original:")
for row in matrix:
    print(f"    {row}")

transposed = []
for j in range(len(matrix[0])):
    new_row = []
    for i in range(len(matrix)):
        new_row.append(matrix[i][j])
    transposed.append(new_row)

print("  Transposed:")
for row in transposed:
    print(f"    {row}")

# Example 3: Compare two lists
print("\nExample 3: Find common elements")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = []

for item1 in list1:
    for item2 in list2:
        if item1 == item2:
            common.append(item1)
            break

print(f"  List 1: {list1}")
print(f"  List 2: {list2}")
print(f"  Common: {common}")

# Example 4: Grid coordinates
print("\nExample 4: Grid coordinates")
rows = 3
cols = 4
print(f"  Grid ({rows}x{cols}):")
for i in range(rows):
    for j in range(cols):
        print(f"    ({i}, {j})", end=" ")
    print()

print()  # Empty line


# ============================================================================
# 10. PERFORMANCE CONSIDERATIONS
# ============================================================================
print("=" * 60)
print("10. PERFORMANCE CONSIDERATIONS")
print("=" * 60)

print("  Nested loops can be slow:")
print("    - Outer loop: n iterations")
print("    - Inner loop: m iterations")
print("    - Total: n * m operations")

print("\n  Example:")
print("    for i in range(1000):")
print("        for j in range(1000):")
print("            # This executes 1,000,000 times!")

print("\n  Tips:")
print("    - Use nested loops only when necessary")
print("    - Consider if there's a better algorithm")
print("    - Break early when possible")
print("    - Use list comprehensions when appropriate")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("NESTED LOOPS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Loop inside another loop")
print("  - Inner loop completes for each outer iteration")
print("  - Total iterations: outer * inner")
print("  - Useful for 2D data, grids, combinations")
print("  - break/continue affect current loop only")
print("  - Can be slow for large iterations")
print("\nCommon Uses:")
print("  - Multiplication tables")
print("  - Pattern printing")
print("  - Matrix operations")
print("  - Generating combinations")
print("  - Searching 2D structures")
print("=" * 60)

