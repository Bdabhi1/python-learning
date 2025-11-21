"""
Advanced List Comprehension Examples

This file demonstrates advanced patterns and techniques with list
comprehensions for complex real-world scenarios.
"""

# ============================================================================
# 1. MULTIPLE ITERABLES
# ============================================================================
print("=" * 60)
print("1. MULTIPLE ITERABLES")
print("=" * 60)

# Combine two lists
list1 = [1, 2, 3]
list2 = [10, 20, 30]
combined = [x + y for x in list1 for y in list2]
print(f"  List1: {list1}")
print(f"  List2: {list2}")
print(f"  Combined (all pairs): {combined}")

# Pairwise combination
pairs = [(x, y) for x in list1 for y in list2]
print(f"  Pairs: {pairs}")

# Using zip for parallel iteration
sums = [x + y for x, y in zip(list1, list2)]
print(f"  Sums (parallel): {sums}")

print()  # Empty line


# ============================================================================
# 2. NESTED COMPREHENSIONS WITH CONDITIONS
# ============================================================================
print("=" * 60)
print("2. NESTED COMPREHENSIONS WITH CONDITIONS")
print("=" * 60)

# Filter nested structure
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Get numbers > 5 from rows where sum > 10
result = [num for row in matrix if sum(row) > 10 for num in row if num > 5]
print(f"  Matrix: {matrix}")
print(f"  Numbers > 5 from rows with sum > 10: {result}")

# Complex filtering
data = [
    [("Alice", 25, "Engineer"), ("Bob", 30, "Doctor")],
    [("Charlie", 20, "Student"), ("Diana", 28, "Engineer")]
]
# Get names of engineers over 25
engineers = [name for group in data 
             for name, age, job in group 
             if job == "Engineer" and age > 25]
print(f"  Data: {data}")
print(f"  Engineers over 25: {engineers}")

print()  # Empty line


# ============================================================================
# 3. COMPREHENSIONS WITH FUNCTIONS
# ============================================================================
print("=" * 60)
print("3. COMPREHENSIONS WITH FUNCTIONS")
print("=" * 60)

# Using map-like operations
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared = [square(x) for x in numbers]
print(f"  Numbers: {numbers}")
print(f"  Squared: {squared}")

# Using filter-like operations
def is_even(x):
    return x % 2 == 0

evens = [x for x in range(10) if is_even(x)]
print(f"  Even numbers: {evens}")

# Combining functions
def process_number(x):
    return x ** 2 if x % 2 == 0 else x * 3

numbers = [1, 2, 3, 4, 5]
processed = [process_number(x) for x in numbers]
print(f"  Numbers: {numbers}")
print(f"  Processed: {processed}")

print()  # Empty line


# ============================================================================
# 4. COMPREHENSIONS WITH LAMBDA
# ============================================================================
print("=" * 60)
print("4. COMPREHENSIONS WITH LAMBDA")
print("=" * 60)

# Using lambda in comprehension
numbers = [1, 2, 3, 4, 5]
squared = [(lambda x: x ** 2)(x) for x in numbers]
print(f"  Numbers: {numbers}")
print(f"  Squared: {squared}")

# More complex lambda
process = lambda x: x * 2 if x > 3 else x + 1
numbers = [1, 2, 3, 4, 5]
result = [process(x) for x in numbers]
print(f"  Numbers: {numbers}")
print(f"  Processed: {result}")

print()  # Empty line


# ============================================================================
# 5. COMPREHENSIONS FOR DATA TRANSFORMATION
# ============================================================================
print("=" * 60)
print("5. COMPREHENSIONS FOR DATA TRANSFORMATION")
print("=" * 60)

# Transform list of tuples
people = [("Alice", 25), ("Bob", 30), ("Charlie", 28)]
formatted = [f"{name} is {age} years old" for name, age in people]
print(f"  People: {people}")
print(f"  Formatted: {formatted}")

# Extract and transform
data = [
    {"name": "Alice", "score": 95},
    {"name": "Bob", "score": 87},
    {"name": "Charlie", "score": 92}
]
high_scorers = [item["name"] for item in data if item["score"] >= 90]
print(f"  Data: {data}")
print(f"  High scorers (>=90): {high_scorers}")

print()  # Empty line


# ============================================================================
# 6. COMPREHENSIONS WITH ENUMERATE
# ============================================================================
print("=" * 60)
print("6. COMPREHENSIONS WITH ENUMERATE")
print("=" * 60)

# Using enumerate for indexed operations
words = ["hello", "world", "python"]
indexed = [(i, word.upper()) for i, word in enumerate(words)]
print(f"  Words: {words}")
print(f"  Indexed and uppercased: {indexed}")

# Filter by index
numbers = [10, 20, 30, 40, 50]
even_indices = [num for i, num in enumerate(numbers) if i % 2 == 0]
print(f"  Numbers: {numbers}")
print(f"  At even indices: {even_indices}")

print()  # Empty line


# ============================================================================
# 7. COMPREHENSIONS FOR GROUPING
# ============================================================================
print("=" * 60)
print("7. COMPREHENSIONS FOR GROUPING")
print("=" * 60)

# Group by category
items = [
    ("apple", "fruit", 1.50),
    ("banana", "fruit", 0.75),
    ("carrot", "vegetable", 0.50),
    ("orange", "fruit", 2.00)
]
fruits = [item for item in items if item[1] == "fruit"]
print(f"  All items: {items}")
print(f"  Fruits only: {fruits}")

# Extract categories
categories = {item[1] for item in items}
print(f"  Categories: {categories}")

print()  # Empty line


# ============================================================================
# 8. PERFORMANCE CONSIDERATIONS
# ============================================================================
print("=" * 60)
print("8. PERFORMANCE CONSIDERATIONS")
print("=" * 60)

# List comprehension vs generator expression
import sys

# List comprehension (creates full list)
list_comp = [x ** 2 for x in range(1000)]
print(f"  List comprehension size: {sys.getsizeof(list_comp)} bytes")

# Generator expression (lazy evaluation)
gen_expr = (x ** 2 for x in range(1000))
print(f"  Generator expression size: {sys.getsizeof(gen_expr)} bytes")
print("  Note: Generator is more memory-efficient for large datasets")

print()  # Empty line


# ============================================================================
# 9. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("9. PRACTICAL EXAMPLES")
print("=" * 60)

# Process CSV-like data
csv_data = [
    "Alice,25,Engineer",
    "Bob,30,Doctor",
    "Charlie,28,Teacher"
]
parsed = [line.split(",") for line in csv_data]
print(f"  CSV data: {csv_data}")
print(f"  Parsed: {parsed}")

# Create lookup tables
numbers = [1, 2, 3, 4, 5]
lookup = {num: num ** 2 for num in numbers}
print(f"  Numbers: {numbers}")
print(f"  Square lookup: {lookup}")

# Filter and transform complex data
students = [
    {"name": "Alice", "scores": [95, 87, 92]},
    {"name": "Bob", "scores": [78, 85, 80]},
    {"name": "Charlie", "scores": [92, 94, 90]}
]
top_students = [
    student["name"] 
    for student in students 
    if sum(student["scores"]) / len(student["scores"]) >= 90
]
print(f"  Students: {students}")
print(f"  Top students (avg >= 90): {top_students}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("ADVANCED COMPREHENSIONS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Can use multiple iterables")
print("  - Can combine with functions and lambdas")
print("  - Can use enumerate for indexed operations")
print("  - Useful for data transformation and filtering")
print("  - Consider generator expressions for large datasets")
print("\nAdvanced Patterns:")
print("  - Multiple iterables: [x+y for x in list1 for y in list2]")
print("  - With enumerate: [(i, x) for i, x in enumerate(items)]")
print("  - Complex filtering: [x for x in items if complex_condition(x)]")
print("  - Data transformation: [process(x) for x in data]")
print("=" * 60)

