"""
Sequence Built-in Functions

This file demonstrates built-in functions for working with sequences
(lists, tuples, strings, etc.).
"""

# ============================================================================
# 1. LEN() - LENGTH
# ============================================================================
print("=" * 60)
print("1. LEN() - LENGTH")
print("=" * 60)

# Length of string
result1 = len("hello")
print(f"  len('hello'): {result1}")

# Length of list
result2 = len([1, 2, 3, 4, 5])
print(f"  len([1, 2, 3, 4, 5]): {result2}")

# Length of tuple
result3 = len((1, 2, 3))
print(f"  len((1, 2, 3)): {result3}")

# Length of dictionary (number of keys)
result4 = len({"a": 1, "b": 2, "c": 3})
print(f"  len({{'a':1, 'b':2, 'c':3}}): {result4}")

# Length of set
result5 = len({1, 2, 3, 4})
print(f"  len({{1, 2, 3, 4}}): {result5}")

print()  # Empty line


# ============================================================================
# 2. SORTED() - SORT SEQUENCE
# ============================================================================
print("=" * 60)
print("2. SORTED() - SORT SEQUENCE")
print("=" * 60)

# Sort list (returns new list)
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result1 = sorted(numbers)
print(f"  Original: {numbers}")
print(f"  sorted([3,1,4,1,5,9,2,6]): {result1}")

# Sort in reverse
result2 = sorted(numbers, reverse=True)
print(f"  sorted(..., reverse=True): {result2}")

# Sort strings
words = ["banana", "apple", "cherry"]
result3 = sorted(words)
print(f"  sorted(['banana', 'apple', 'cherry']): {result3}")

# Sort with key function
students = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
result4 = sorted(students, key=lambda x: x[1])
print(f"  sorted by age: {result4}")

print("\n  Note: sorted() returns new list, doesn't modify original")

print()  # Empty line


# ============================================================================
# 3. REVERSED() - REVERSE SEQUENCE
# ============================================================================
print("=" * 60)
print("3. REVERSED() - REVERSE SEQUENCE")
print("=" * 60)

# Reverse list (returns iterator)
numbers = [1, 2, 3, 4, 5]
result1 = list(reversed(numbers))
print(f"  Original: {numbers}")
print(f"  list(reversed([1,2,3,4,5])): {result1}")

# Reverse string
text = "hello"
result2 = "".join(reversed(text))
print(f"  ''.join(reversed('hello')): {result2}")

# Reverse tuple
my_tuple = (1, 2, 3, 4)
result3 = tuple(reversed(my_tuple))
print(f"  tuple(reversed((1,2,3,4))): {result3}")

print("\n  Note: reversed() returns iterator, convert to list/tuple/string")

print()  # Empty line


# ============================================================================
# 4. ENUMERATE() - ADD INDEX
# ============================================================================
print("=" * 60)
print("4. ENUMERATE() - ADD INDEX")
print("=" * 60)

# Enumerate list
fruits = ["apple", "banana", "orange"]
print("  enumerate(['apple', 'banana', 'orange']):")
for index, fruit in enumerate(fruits):
    print(f"    {index}: {fruit}")

# Enumerate with start
print("\n  enumerate(..., start=1):")
for index, fruit in enumerate(fruits, start=1):
    print(f"    {index}: {fruit}")

# Convert to list
result = list(enumerate(fruits))
print(f"\n  list(enumerate(...)): {result}")

print()  # Empty line


# ============================================================================
# 5. ZIP() - COMBINE SEQUENCES
# ============================================================================
print("=" * 60)
print("5. ZIP() - COMBINE SEQUENCES")
print("=" * 60)

# Zip two lists
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
result1 = list(zip(list1, list2))
print(f"  zip([1,2,3], ['a','b','c']): {result1}")

# Zip multiple sequences
list3 = ["x", "y", "z"]
result2 = list(zip(list1, list2, list3))
print(f"  zip(3 sequences): {result2}")

# Unzip (unpack)
pairs = [(1, "a"), (2, "b"), (3, "c")]
unzipped = zip(*pairs)
numbers, letters = list(unzipped)
print(f"\n  Unzip: {pairs}")
print(f"    Numbers: {list(numbers)}")
print(f"    Letters: {list(letters)}")

# Different lengths (stops at shortest)
short = [1, 2]
long_list = ["a", "b", "c", "d"]
result3 = list(zip(short, long_list))
print(f"\n  zip([1,2], ['a','b','c','d']): {result3} (stops at shortest)")

print()  # Empty line


# ============================================================================
# 6. ANY() - ANY ELEMENT TRUE
# ============================================================================
print("=" * 60)
print("6. ANY() - ANY ELEMENT TRUE")
print("=" * 60)

# Check if any element is True
result1 = any([False, False, True])
print(f"  any([False, False, True]): {result1}")

result2 = any([False, False, False])
print(f"  any([False, False, False]): {result2}")

# With numbers (non-zero is True)
result3 = any([0, 0, 1])
print(f"  any([0, 0, 1]): {result3}")

# With strings (non-empty is True)
result4 = any(["", "", "hello"])
print(f"  any(['', '', 'hello']): {result4}")

# Practical: Check if any number is positive
numbers = [-1, -2, 0, 3, -4]
result5 = any(n > 0 for n in numbers)
print(f"  any(n > 0 for n in [-1,-2,0,3,-4]): {result5}")

print()  # Empty line


# ============================================================================
# 7. ALL() - ALL ELEMENTS TRUE
# ============================================================================
print("=" * 60)
print("7. ALL() - ALL ELEMENTS TRUE")
print("=" * 60)

# Check if all elements are True
result1 = all([True, True, True])
print(f"  all([True, True, True]): {result1}")

result2 = all([True, False, True])
print(f"  all([True, False, True]): {result2}")

# With numbers
result3 = all([1, 2, 3])
print(f"  all([1, 2, 3]): {result3}")

result4 = all([1, 2, 0])
print(f"  all([1, 2, 0]): {result4}")

# Practical: Check if all numbers are positive
numbers = [1, 2, 3, 4, 5]
result5 = all(n > 0 for n in numbers)
print(f"  all(n > 0 for n in [1,2,3,4,5]): {result5}")

numbers2 = [1, 2, -3, 4, 5]
result6 = all(n > 0 for n in numbers2)
print(f"  all(n > 0 for n in [1,2,-3,4,5]): {result6}")

print()  # Empty line


# ============================================================================
# 8. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("8. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Process with index
print("Example 1: Process with Index")
items = ["apple", "banana", "orange"]
print("  Items with numbers:")
for i, item in enumerate(items, 1):
    print(f"    {i}. {item}")

# Example 2: Combine data
print("\nExample 2: Combine Data")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
people = list(zip(names, ages))
print(f"  Names: {names}")
print(f"  Ages: {ages}")
print(f"  Combined: {people}")

# Example 3: Validation
print("\nExample 3: Validation")
scores = [85, 90, 78, 92, 88]
all_passing = all(score >= 60 for score in scores)
any_excellent = any(score >= 90 for score in scores)
print(f"  Scores: {scores}")
print(f"  All passing (>=60): {all_passing}")
print(f"  Any excellent (>=90): {any_excellent}")

# Example 4: Sort and reverse
print("\nExample 4: Sort and Reverse")
numbers = [5, 2, 8, 1, 9, 3]
sorted_asc = sorted(numbers)
sorted_desc = sorted(numbers, reverse=True)
print(f"  Original: {numbers}")
print(f"  Sorted (asc): {sorted_asc}")
print(f"  Sorted (desc): {sorted_desc}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("SEQUENCE FUNCTIONS SUMMARY:")
print("=" * 60)
print("Function    | Description              | Example")
print("-" * 55)
print("len()       | Get length               | len([1,2,3]) -> 3")
print("sorted()    | Sort sequence            | sorted([3,1,2]) -> [1,2,3]")
print("reversed()  | Reverse sequence          | list(reversed([1,2,3]))")
print("enumerate() | Add index                 | enumerate(['a','b'])")
print("zip()       | Combine sequences         | zip([1,2],['a','b'])")
print("any()       | Any element True          | any([False,True]) -> True")
print("all()       | All elements True         | all([True,True]) -> True")
print("=" * 60)
print("\nKey Points:")
print("  - len() works with any sequence/collection")
print("  - sorted() returns new list, doesn't modify original")
print("  - reversed() returns iterator, convert to list/string")
print("  - enumerate() adds index to iteration")
print("  - zip() combines sequences, stops at shortest")
print("  - any()/all() check truthiness of elements")
print("=" * 60)

