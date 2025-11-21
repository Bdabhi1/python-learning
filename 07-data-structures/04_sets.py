"""
Sets in Python

This file demonstrates sets - unordered collections of unique elements.
Useful for membership testing, removing duplicates, and set operations.
"""

# ============================================================================
# 1. CREATING SETS
# ============================================================================
print("=" * 60)
print("1. CREATING SETS")
print("=" * 60)

# Empty set (note: use set(), not {})
empty_set = set()
print(f"  Empty set: {empty_set}")

# Set with items
numbers = {1, 2, 3, 4, 5}
print(f"  Numbers: {numbers}")

# From list (removes duplicates)
numbers = set([1, 2, 2, 3, 3, 4])
print(f"  From list [1,2,2,3,3,4]: {numbers}")

# From string
chars = set("hello")
print(f"  From string 'hello': {chars}")

# Using set() constructor
numbers = set(range(5))
print(f"  From range(5): {numbers}")

print("\n  Note: {} creates a dictionary, not a set!")

print()  # Empty line


# ============================================================================
# 2. SETS CONTAIN UNIQUE ELEMENTS
# ============================================================================
print("=" * 60)
print("2. SETS CONTAIN UNIQUE ELEMENTS")
print("=" * 60)

# Duplicates are automatically removed
numbers = {1, 2, 2, 3, 3, 3, 4}
print(f"  {1, 2, 2, 3, 3, 3, 4} becomes: {numbers}")

# Adding duplicate has no effect
numbers.add(2)
print(f"  After add(2): {numbers} (no change)")

# From list with duplicates
my_list = [1, 2, 2, 3, 3, 4]
unique = set(my_list)
print(f"  List {my_list} -> Set: {unique}")

print()  # Empty line


# ============================================================================
# 3. MODIFYING SETS
# ============================================================================
print("=" * 60)
print("3. MODIFYING SETS")
print("=" * 60)

my_set = {1, 2, 3}
print(f"  Original: {my_set}")

# Add element
my_set.add(4)
print(f"  After add(4): {my_set}")

# Add multiple
my_set.update([5, 6, 7])
print(f"  After update([5,6,7]): {my_set}")

# Remove element (error if not exists)
my_set.remove(7)
print(f"  After remove(7): {my_set}")

# Discard element (no error if not exists)
my_set.discard(10)  # No error
print(f"  After discard(10): {my_set} (no change)")

# Remove and return arbitrary element
removed = my_set.pop()
print(f"  After pop(): {my_set}, removed: {removed}")

# Clear all
my_set.clear()
print(f"  After clear(): {my_set}")

print()  # Empty line


# ============================================================================
# 4. SET OPERATIONS
# ============================================================================
print("=" * 60)
print("4. SET OPERATIONS")
print("=" * 60)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"  set1: {set1}")
print(f"  set2: {set2}")

# Union (all elements from both)
union = set1 | set2
print(f"  Union (set1 | set2): {union}")

# Intersection (common elements)
intersection = set1 & set2
print(f"  Intersection (set1 & set2): {intersection}")

# Difference (in set1 but not set2)
difference = set1 - set2
print(f"  Difference (set1 - set2): {difference}")

# Symmetric difference (in one but not both)
sym_diff = set1 ^ set2
print(f"  Symmetric difference (set1 ^ set2): {sym_diff}")

print()  # Empty line


# ============================================================================
# 5. SET METHODS
# ============================================================================
print("=" * 60)
print("5. SET METHODS")
print("=" * 60)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
print(f"  set1.union(set2): {set1.union(set2)}")

# Intersection
print(f"  set1.intersection(set2): {set1.intersection(set2)}")

# Difference
print(f"  set1.difference(set2): {set1.difference(set2)}")

# Symmetric difference
print(f"  set1.symmetric_difference(set2): {set1.symmetric_difference(set2)}")

# Subset check
print(f"  set1.issubset(set2): {set1.issubset(set2)}")
set3 = {1,2,3}
print(f"  set3.issubset(set1): {set3.issubset(set1)}")

# Superset check
print(f"  set1.issuperset({1,2,3}): {set1.issuperset({1,2,3})}")

# Disjoint check
print(f"  set1.isdisjoint({6,7,8}): {set1.isdisjoint({6,7,8})}")

print()  # Empty line


# ============================================================================
# 6. MEMBERSHIP TESTING
# ============================================================================
print("=" * 60)
print("6. MEMBERSHIP TESTING")
print("=" * 60)

my_set = {1, 2, 3, 4, 5}

# Check membership (very fast!)
print(f"  3 in {my_set}: {3 in my_set}")
print(f"  10 in {my_set}: {10 in my_set}")

# Length
print(f"  len({my_set}): {len(my_set)}")

# Check if empty
empty = set()
print(f"  bool(empty_set): {bool(empty)}")
print(f"  bool({my_set}): {bool(my_set)}")

print("\n  Sets are optimized for fast membership testing!")

print()  # Empty line


# ============================================================================
# 7. REMOVING DUPLICATES
# ============================================================================
print("=" * 60)
print("7. REMOVING DUPLICATES")
print("=" * 60)

# Remove duplicates from list
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 5]
print(f"  Original list: {my_list}")

# Method 1: Convert to set and back
unique_list = list(set(my_list))
print(f"  Unique (set method): {unique_list}")

# Note: Order may change with set method
# Method 2: Preserve order (Python 3.7+)
unique_ordered = list(dict.fromkeys(my_list))
print(f"  Unique (preserve order): {unique_ordered}")

print()  # Empty line


# ============================================================================
# 8. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("8. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Unique tags
print("Example 1: Unique Tags")
all_tags = ["python", "coding", "tutorial", "python", "coding", "beginner"]
unique_tags = set(all_tags)
print(f"  All tags: {all_tags}")
print(f"  Unique tags: {unique_tags}")

# Example 2: Find common elements
print("\nExample 2: Find Common Elements")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)
print(f"  List 1: {list1}")
print(f"  List 2: {list2}")
print(f"  Common: {list(common)}")

# Example 3: Valid characters
print("\nExample 3: Valid Characters")
valid_chars = set("abcdefghijklmnopqrstuvwxyz0123456789")
user_input = "hello123"
is_valid = set(user_input).issubset(valid_chars)
print(f"  Input: '{user_input}'")
print(f"  Valid: {is_valid}")

# Example 4: Set operations for data analysis
print("\nExample 4: Data Analysis")
students_math = {"Alice", "Bob", "Charlie", "David"}
students_science = {"Bob", "Charlie", "Eve", "Frank"}

both = students_math & students_science
only_math = students_math - students_science
only_science = students_science - students_math
all_students = students_math | students_science

print(f"  Math students: {students_math}")
print(f"  Science students: {students_science}")
print(f"  Both subjects: {both}")
print(f"  Only math: {only_math}")
print(f"  Only science: {only_science}")
print(f"  All students: {all_students}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("SETS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Unordered collection of unique elements")
print("  - Mutable (can be modified)")
print("  - No duplicates allowed")
print("  - Fast membership testing")
print("  - Set operations: union, intersection, difference")
print("\nCommon Uses:")
print("  - Removing duplicates")
print("  - Fast membership testing")
print("  - Set operations (union, intersection, etc.)")
print("  - Finding common/unique elements")
print("\nOperations:")
print("  - Union: | or union()")
print("  - Intersection: & or intersection()")
print("  - Difference: - or difference()")
print("  - Symmetric difference: ^ or symmetric_difference()")
print("=" * 60)

