"""
Lists in Python

This file demonstrates lists - ordered, mutable collections of items.
Lists are one of the most commonly used data structures in Python.
"""

# ============================================================================
# 1. CREATING LISTS
# ============================================================================
print("=" * 60)
print("1. CREATING LISTS")
print("=" * 60)

# Empty list
empty_list = []
print(f"  Empty list: {empty_list}")

# List with items
fruits = ["apple", "banana", "orange"]
print(f"  Fruits: {fruits}")

# Mixed types
mixed = [1, "hello", 3.14, True]
print(f"  Mixed types: {mixed}")

# Using list() constructor
numbers = list(range(5))
print(f"  Numbers from range: {numbers}")

# List from string
chars = list("Python")
print(f"  Characters: {chars}")

print()  # Empty line


# ============================================================================
# 2. ACCESSING ELEMENTS
# ============================================================================
print("=" * 60)
print("2. ACCESSING ELEMENTS")
print("=" * 60)

fruits = ["apple", "banana", "orange", "grape", "kiwi"]

# Access by index (0-based)
print(f"  fruits[0]: {fruits[0]}")
print(f"  fruits[1]: {fruits[1]}")
print(f"  fruits[2]: {fruits[2]}")

# Negative indexing (from end)
print(f"\n  fruits[-1]: {fruits[-1]} (last)")
print(f"  fruits[-2]: {fruits[-2]} (second from end)")

# Slicing
print(f"\n  fruits[1:3]: {fruits[1:3]}")
print(f"  fruits[:3]: {fruits[:3]} (first 3)")
print(f"  fruits[2:]: {fruits[2:]} (from index 2)")
print(f"  fruits[:]: {fruits[:]} (all elements)")

# Step in slicing
print(f"\n  fruits[::2]: {fruits[::2]} (every 2nd element)")
print(f"  fruits[::-1]: {fruits[::-1]} (reversed)")

print()  # Empty line


# ============================================================================
# 3. MODIFYING LISTS
# ============================================================================
print("=" * 60)
print("3. MODIFYING LISTS")
print("=" * 60)

# Change element
fruits = ["apple", "banana", "orange"]
print(f"  Original: {fruits}")
fruits[0] = "cherry"
print(f"  After fruits[0] = 'cherry': {fruits}")

# Add to end
fruits.append("grape")
print(f"  After append('grape'): {fruits}")

# Insert at position
fruits.insert(1, "kiwi")
print(f"  After insert(1, 'kiwi'): {fruits}")

# Extend with another list
fruits.extend(["mango", "pineapple"])
print(f"  After extend(['mango', 'pineapple']): {fruits}")

print()  # Empty line


# ============================================================================
# 4. REMOVING ELEMENTS
# ============================================================================
print("=" * 60)
print("4. REMOVING ELEMENTS")
print("=" * 60)

fruits = ["apple", "banana", "orange", "grape", "kiwi"]
print(f"  Original: {fruits}")

# Remove by value
fruits.remove("banana")
print(f"  After remove('banana'): {fruits}")

# Remove by index (pop)
removed = fruits.pop(1)
print(f"  After pop(1): {fruits}, removed: '{removed}'")

# Remove last element
removed = fruits.pop()
print(f"  After pop(): {fruits}, removed: '{removed}'")

# Delete by index
del fruits[0]
print(f"  After del fruits[0]: {fruits}")

# Clear all
fruits.clear()
print(f"  After clear(): {fruits}")

print()  # Empty line


# ============================================================================
# 5. LIST OPERATIONS
# ============================================================================
print("=" * 60)
print("5. LIST OPERATIONS")
print("=" * 60)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Length
print(f"  len([1, 2, 3]): {len(list1)}")

# Membership
print(f"  2 in [1, 2, 3]: {2 in list1}")
print(f"  5 in [1, 2, 3]: {5 in list1}")

# Concatenation
combined = list1 + list2
print(f"  [1,2,3] + [4,5,6]: {combined}")

# Repetition
repeated = list1 * 3
print(f"  [1,2,3] * 3: {repeated}")

# Minimum and maximum
numbers = [5, 2, 8, 1, 9]
print(f"  min([5,2,8,1,9]): {min(numbers)}")
print(f"  max([5,2,8,1,9]): {max(numbers)}")
print(f"  sum([5,2,8,1,9]): {sum(numbers)}")

print()  # Empty line


# ============================================================================
# 6. LIST METHODS
# ============================================================================
print("=" * 60)
print("6. LIST METHODS")
print("=" * 60)

# Count occurrences
numbers = [1, 2, 2, 3, 2, 4]
print(f"  numbers.count(2): {numbers.count(2)}")

# Find index
fruits = ["apple", "banana", "orange"]
print(f"  fruits.index('banana'): {fruits.index('banana')}")

# Sort (modifies list)
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"  Original: {numbers}")
numbers.sort()
print(f"  After sort(): {numbers}")

# Reverse (modifies list)
numbers.reverse()
print(f"  After reverse(): {numbers}")

# Copy
original = [1, 2, 3]
copied = original.copy()
copied.append(4)
print(f"  Original: {original}")
print(f"  Copied: {copied}")

print()  # Empty line


# ============================================================================
# 7. LIST COMPREHENSIONS (PREVIEW)
# ============================================================================
print("=" * 60)
print("7. LIST COMPREHENSIONS (PREVIEW)")
print("=" * 60)

# Create list from range
squares = [x**2 for x in range(5)]
print(f"  Squares: {squares}")

# Filter with comprehension
even = [x for x in range(10) if x % 2 == 0]
print(f"  Even numbers: {even}")

# Transform elements
words = ["hello", "world", "python"]
lengths = [len(word) for word in words]
print(f"  Word lengths: {lengths}")

print("\n  Note: We'll learn more about comprehensions later!")

print()  # Empty line


# ============================================================================
# 8. NESTED LISTS
# ============================================================================
print("=" * 60)
print("8. NESTED LISTS")
print("=" * 60)

# 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("  Matrix:")
for row in matrix:
    print(f"    {row}")

# Access nested elements
print(f"\n  matrix[0][1]: {matrix[0][1]}")
print(f"  matrix[2][2]: {matrix[2][2]}")

# Modify nested element
matrix[0][0] = 10
print(f"  After matrix[0][0] = 10:")
for row in matrix:
    print(f"    {row}")

print()  # Empty line


# ============================================================================
# 9. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("9. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Shopping cart
print("Example 1: Shopping Cart")
cart = []
cart.append("Apple")
cart.append("Banana")
cart.append("Orange")
print(f"  Cart: {cart}")
cart.remove("Banana")
print(f"  After removing Banana: {cart}")

# Example 2: Score tracking
print("\nExample 2: Score Tracking")
scores = [85, 90, 78, 92, 88]
print(f"  Scores: {scores}")
print(f"  Average: {sum(scores) / len(scores):.2f}")
print(f"  Highest: {max(scores)}")
print(f"  Lowest: {min(scores)}")

# Example 3: To-do list
print("\nExample 3: To-Do List")
todos = ["Learn Python", "Write code", "Test program"]
print("  To-dos:")
for i, todo in enumerate(todos, 1):
    print(f"    {i}. {todo}")

# Example 4: Filtering
print("\nExample 4: Filtering Numbers")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [n for n in numbers if n % 2 == 0]
print(f"  All: {numbers}")
print(f"  Even: {even_numbers}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("LISTS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Ordered collection of items")
print("  - Mutable (can be modified)")
print("  - Allows duplicates")
print("  - Indexed (0-based)")
print("  - Supports slicing")
print("\nCommon Operations:")
print("  - Access: list[index]")
print("  - Add: append(), insert(), extend()")
print("  - Remove: remove(), pop(), del")
print("  - Modify: list[index] = value")
print("  - Search: in, index(), count()")
print("  - Sort: sort(), reverse()")
print("=" * 60)

