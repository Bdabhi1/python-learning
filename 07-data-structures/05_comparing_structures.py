"""
Comparing Data Structures

This file demonstrates when to use each data structure and compares
their characteristics, use cases, and performance.
"""

# ============================================================================
# 1. QUICK COMPARISON TABLE
# ============================================================================
print("=" * 60)
print("1. QUICK COMPARISON TABLE")
print("=" * 60)

print("Structure | Ordered | Mutable | Duplicates | Indexed | Use Case")
print("-" * 70)
print("List      |   Yes   |   Yes   |    Yes     |  Yes    | Sequences")
print("Tuple     |   Yes   |   No    |    Yes     |  Yes    | Fixed data")
print("Dict      |   Yes*  |   Yes   | Keys: No   |  No     | Key-value")
print("Set       |   No    |   Yes   |    No      |  No     | Unique items")
print("\n* Dictionaries are ordered in Python 3.7+")

print()  # Empty line


# ============================================================================
# 2. WHEN TO USE LISTS
# ============================================================================
print("=" * 60)
print("2. WHEN TO USE LISTS")
print("=" * 60)

print("Use lists when:")
print("  ✅ You need ordered collection")
print("  ✅ You need to modify items")
print("  ✅ You need duplicates")
print("  ✅ You access by index")
print("  ✅ Order matters")

print("\nExamples:")
print("  - Shopping cart: ['apple', 'banana', 'apple']")
print("  - To-do list: ['task1', 'task2', 'task3']")
print("  - Scores: [85, 90, 78, 92]")
print("  - Any sequence you'll modify")

# Example
shopping_cart = ["apple", "banana", "apple", "orange"]
print(f"\n  Shopping cart: {shopping_cart}")
shopping_cart.append("milk")
print(f"  After adding milk: {shopping_cart}")

print()  # Empty line


# ============================================================================
# 3. WHEN TO USE TUPLES
# ============================================================================
print("=" * 60)
print("3. WHEN TO USE TUPLES")
print("=" * 60)

print("Use tuples when:")
print("  ✅ You need ordered collection")
print("  ✅ You DON'T need to modify items")
print("  ✅ You need to use as dictionary key")
print("  ✅ You return multiple values from function")
print("  ✅ Data should be immutable")

print("\nExamples:")
print("  - Coordinates: (10, 20)")
print("  - RGB colors: (255, 0, 0)")
print("  - Database records: (name, age, email)")
print("  - Dictionary keys")

# Example
coordinates = (10, 20)
rgb_red = (255, 0, 0)
print(f"\n  Coordinates: {coordinates}")
print(f"  RGB Red: {rgb_red}")

# As dictionary key
locations = {(0, 0): "Origin", (10, 20): "Point A"}
print(f"  Locations dict: {locations}")

print()  # Empty line


# ============================================================================
# 4. WHEN TO USE DICTIONARIES
# ============================================================================
print("=" * 60)
print("4. WHEN TO USE DICTIONARIES")
print("=" * 60)

print("Use dictionaries when:")
print("  ✅ You need key-value pairs")
print("  ✅ You access by key (not index)")
print("  ✅ You need fast lookups")
print("  ✅ Keys are unique")
print("  ✅ You need mappings/associations")

print("\nExamples:")
print("  - User profiles: {'name': 'Alice', 'age': 25}")
print("  - Phone book: {'Alice': '555-0101'}")
print("  - Configuration: {'host': 'localhost', 'port': 8080}")
print("  - Word counts: {'hello': 3, 'world': 2}")

# Example
user = {"name": "Alice", "age": 25, "email": "alice@example.com"}
print(f"\n  User profile: {user}")
print(f"  User name: {user['name']}")

print()  # Empty line


# ============================================================================
# 5. WHEN TO USE SETS
# ============================================================================
print("=" * 60)
print("5. WHEN TO USE SETS")
print("=" * 60)

print("Use sets when:")
print("  ✅ You need unique elements")
print("  ✅ You need set operations (union, intersection)")
print("  ✅ Order doesn't matter")
print("  ✅ You need fast membership testing")
print("  ✅ You need to remove duplicates")

print("\nExamples:")
print("  - Unique tags: {'python', 'coding', 'tutorial'}")
print("  - Valid characters: set('abcdefghijklmnopqrstuvwxyz')")
print("  - Removing duplicates from list")
print("  - Finding common elements")

# Example
tags = {"python", "coding", "tutorial", "python", "coding"}
print(f"\n  Tags (duplicates removed): {tags}")

# Remove duplicates
numbers = [1, 2, 2, 3, 3, 4]
unique = list(set(numbers))
print(f"  Remove duplicates: {numbers} -> {unique}")

print()  # Empty line


# ============================================================================
# 6. PERFORMANCE COMPARISON
# ============================================================================
print("=" * 60)
print("6. PERFORMANCE COMPARISON")
print("=" * 60)

print("Operation          | List | Tuple | Dict | Set")
print("-" * 50)
print("Access by index    | O(1) | O(1)  | N/A  | N/A")
print("Access by key      | N/A  | N/A   | O(1) | N/A")
print("Membership test    | O(n) | O(n)  | O(1) | O(1)")
print("Add element        | O(1) | N/A   | O(1) | O(1)")
print("Remove element     | O(n) | N/A   | O(1) | O(1)")
print("Iteration          | O(n) | O(n)  | O(n) | O(n)")

print("\nKey Points:")
print("  - Lists/Tuples: Fast indexed access")
print("  - Dicts/Sets: Fast membership testing")
print("  - Sets: Fastest for unique element operations")
print("  - Tuples: Slightly faster than lists (immutable)")

print()  # Empty line


# ============================================================================
# 7. CONVERSION BETWEEN STRUCTURES
# ============================================================================
print("=" * 60)
print("7. CONVERSION BETWEEN STRUCTURES")
print("=" * 60)

# List to other structures
my_list = [1, 2, 3, 2, 4]
print(f"  Original list: {my_list}")

# List to tuple
my_tuple = tuple(my_list)
print(f"  To tuple: {my_tuple}")

# List to set (removes duplicates)
my_set = set(my_list)
print(f"  To set: {my_set} (duplicates removed)")

# List to dict (need key-value pairs)
my_dict = dict(enumerate(my_list))
print(f"  To dict: {my_dict}")

# Set to list
back_to_list = list(my_set)
print(f"  Set back to list: {back_to_list}")

print()  # Empty line


# ============================================================================
# 8. COMMON PATTERNS
# ============================================================================
print("=" * 60)
print("8. COMMON PATTERNS")
print("=" * 60)

# Pattern 1: Remove duplicates
print("Pattern 1: Remove Duplicates")
numbers = [1, 2, 2, 3, 3, 4]
unique = list(set(numbers))
print(f"  {numbers} -> {unique}")

# Pattern 2: Count occurrences
print("\nPattern 2: Count Occurrences")
words = ["apple", "banana", "apple", "orange", "banana"]
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(f"  Words: {words}")
print(f"  Counts: {counts}")

# Pattern 3: Group data
print("\nPattern 3: Group Data")
students = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Charlie", "Math"),
    ("David", "Science")
]
groups = {}
for name, subject in students:
    if subject not in groups:
        groups[subject] = []
    groups[subject].append(name)
print(f"  Groups: {groups}")

# Pattern 4: Find common elements
print("\nPattern 4: Find Common Elements")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))
print(f"  List1: {list1}")
print(f"  List2: {list2}")
print(f"  Common: {common}")

print()  # Empty line


# ============================================================================
# 9. DECISION GUIDE
# ============================================================================
print("=" * 60)
print("9. DECISION GUIDE")
print("=" * 60)

print("Ask yourself:")
print("  1. Do I need to modify items?")
print("     - Yes → List or Dict or Set")
print("     - No → Tuple")
print()
print("  2. Do I need key-value pairs?")
print("     - Yes → Dictionary")
print("     - No → Continue to question 3")
print()
print("  3. Do I need unique elements?")
print("     - Yes → Set")
print("     - No → Continue to question 4")
print()
print("  4. Do I need order preserved?")
print("     - Yes → List")
print("     - No → Set")
print()
print("  5. Do I need to modify after creation?")
print("     - Yes → List")
print("     - No → Tuple")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("COMPARING STRUCTURES SUMMARY:")
print("=" * 60)
print("Lists:")
print("  - Use for: Sequences you'll modify, ordered data")
print("  - Strengths: Flexible, indexed access")
print("\nTuples:")
print("  - Use for: Fixed data, dictionary keys, return values")
print("  - Strengths: Immutable, faster, hashable")
print("\nDictionaries:")
print("  - Use for: Key-value mappings, lookups")
print("  - Strengths: Fast lookups, flexible keys")
print("\nSets:")
print("  - Use for: Unique elements, set operations")
print("  - Strengths: Fast membership, removes duplicates")
print("\nChoose based on your specific needs!")
print("=" * 60)

