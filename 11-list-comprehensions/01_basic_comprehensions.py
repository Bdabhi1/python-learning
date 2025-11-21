"""
Basic List Comprehensions in Python

This file demonstrates the basic syntax and usage of list comprehensions -
a concise and Pythonic way to create lists.
"""

# ============================================================================
# 1. BASIC LIST COMPREHENSION SYNTAX
# ============================================================================
print("=" * 60)
print("1. BASIC LIST COMPREHENSION SYNTAX")
print("=" * 60)

# Traditional approach (loop)
squares_loop = []
for x in range(10):
    squares_loop.append(x ** 2)

# List comprehension (concise)
squares_comp = [x ** 2 for x in range(10)]

print(f"  Using loop: {squares_loop}")
print(f"  Using comprehension: {squares_comp}")
print(f"  Same result: {squares_loop == squares_comp}")

print("\n  Syntax: [expression for item in iterable]")

print()  # Empty line


# ============================================================================
# 2. SIMPLE TRANSFORMATIONS
# ============================================================================
print("=" * 60)
print("2. SIMPLE TRANSFORMATIONS")
print("=" * 60)

# Square numbers
squares = [x ** 2 for x in range(10)]
print(f"  Squares: {squares}")

# Double numbers
doubles = [x * 2 for x in range(10)]
print(f"  Doubles: {doubles}")

# Convert to string
numbers = [1, 2, 3, 4, 5]
strings = [str(x) for x in numbers]
print(f"  Numbers: {numbers}")
print(f"  As strings: {strings}")

# Calculate lengths
words = ["hello", "world", "python"]
lengths = [len(word) for word in words]
print(f"  Words: {words}")
print(f"  Lengths: {lengths}")

print()  # Empty line


# ============================================================================
# 3. WORKING WITH DIFFERENT ITERABLES
# ============================================================================
print("=" * 60)
print("3. WORKING WITH DIFFERENT ITERABLES")
print("=" * 60)

# From range
numbers = [x for x in range(5)]
print(f"  From range(5): {numbers}")

# From string
chars = [char for char in "Python"]
print(f"  From 'Python': {chars}")

# From existing list
original = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in original]
print(f"  Original: {original}")
print(f"  Doubled: {doubled}")

# From tuple
coordinates = [(1, 2), (3, 4), (5, 6)]
x_coords = [x for x, y in coordinates]
print(f"  Coordinates: {coordinates}")
print(f"  X coordinates: {x_coords}")

print()  # Empty line


# ============================================================================
# 4. USING FUNCTIONS IN COMPREHENSIONS
# ============================================================================
print("=" * 60)
print("4. USING FUNCTIONS IN COMPREHENSIONS")
print("=" * 60)

# Apply function to each element
numbers = [1, 2, 3, 4, 5]
squared = [pow(x, 2) for x in numbers]
print(f"  Numbers: {numbers}")
print(f"  Squared: {squared}")

# Using built-in functions
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"  Words: {words}")
print(f"  Uppercase: {upper_words}")

# Using abs() function
numbers = [-2, -1, 0, 1, 2]
abs_values = [abs(x) for x in numbers]
print(f"  Numbers: {numbers}")
print(f"  Absolute values: {abs_values}")

print()  # Empty line


# ============================================================================
# 5. COMPLEX EXPRESSIONS
# ============================================================================
print("=" * 60)
print("5. COMPLEX EXPRESSIONS")
print("=" * 60)

# Mathematical expressions
numbers = [1, 2, 3, 4, 5]
results = [x ** 2 + 2 * x + 1 for x in numbers]
print(f"  Numbers: {numbers}")
print(f"  x² + 2x + 1: {results}")

# String operations
words = ["hello", "world", "python"]
modified = [word.upper() + "!" for word in words]
print(f"  Words: {words}")
print(f"  Modified: {modified}")

print()  # Empty line


# ============================================================================
# 6. COMPARISON WITH TRADITIONAL LOOPS
# ============================================================================
print("=" * 60)
print("6. COMPARISON WITH TRADITIONAL LOOPS")
print("=" * 60)

# Example 1: Squares
print("  Example 1: Squares")
# Loop
squares_loop = []
for x in range(5):
    squares_loop.append(x ** 2)
print(f"    Loop: {squares_loop}")

# Comprehension
squares_comp = [x ** 2 for x in range(5)]
print(f"    Comprehension: {squares_comp}")

# Example 2: Uppercase words
print("\n  Example 2: Uppercase words")
words = ["hello", "world", "python"]
# Loop
upper_loop = []
for word in words:
    upper_loop.append(word.upper())
print(f"    Loop: {upper_loop}")

# Comprehension
upper_comp = [word.upper() for word in words]
print(f"    Comprehension: {upper_comp}")

print()  # Empty line


# ============================================================================
# 7. WORKING WITH STRINGS
# ============================================================================
print("=" * 60)
print("7. WORKING WITH STRINGS")
print("=" * 60)

# Extract characters
text = "Python"
chars = [char for char in text]
print(f"  Text: '{text}'")
print(f"  Characters: {chars}")

# Split and process
sentence = "hello world python"
words = [word.capitalize() for word in sentence.split()]
print(f"  Sentence: '{sentence}'")
print(f"  Capitalized words: {words}")

print()  # Empty line


# ============================================================================
# 8. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("8. PRACTICAL EXAMPLES")
print("=" * 60)

# Generate sequence
sequence = [x * 2 for x in range(1, 11)]
print(f"  Sequence (2, 4, 6, ...): {sequence}")

# Process user data
users = ["alice", "bob", "charlie"]
formatted_users = [user.capitalize() for user in users]
print(f"  Users: {users}")
print(f"  Formatted: {formatted_users}")

# Calculate areas
radii = [1, 2, 3, 4, 5]
areas = [3.14159 * r ** 2 for r in radii]
print(f"  Radii: {radii}")
print(f"  Areas: {areas}")

# Extract data from tuples
people = [("Alice", 25), ("Bob", 30), ("Charlie", 28)]
names = [name for name, age in people]
ages = [age for name, age in people]
print(f"  People: {people}")
print(f"  Names: {names}")
print(f"  Ages: {ages}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("BASIC LIST COMPREHENSIONS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Syntax: [expression for item in iterable]")
print("  - More concise than traditional loops")
print("  - More readable and Pythonic")
print("  - Can work with any iterable (list, range, string, tuple)")
print("  - Can use functions in expressions")
print("\nBenefits:")
print("  - Less code to write")
print("  - More readable")
print("  - Often faster than loops")
print("  - Pythonic way to create lists")
print("=" * 60)

