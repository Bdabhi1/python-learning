"""
Iterators in Python

This file demonstrates what iterators are and how they work.
"""

# ============================================================================
# 1. WHAT IS AN ITERATOR?
# ============================================================================
print("=" * 60)
print("1. WHAT IS AN ITERATOR?")
print("=" * 60)

print("  An iterator is an object that can be iterated (looped) upon.")
print("  It implements __iter__() and __next__() methods.")
print("  ")
print("  Iterable: Object that can return an iterator")
print("  Iterator: Object that implements iterator protocol")

print()  # Empty line


# ============================================================================
# 2. BUILT-IN ITERABLES
# ============================================================================
print("=" * 60)
print("2. BUILT-IN ITERABLES")
print("=" * 60)

# Lists, tuples, strings are iterable
my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_string = "abc"

print(f"  List: {my_list}")
print(f"  Tuple: {my_tuple}")
print(f"  String: {my_string}")

# Get iterator using iter()
list_iter = iter(my_list)
print(f"  Iterator: {list_iter}")

print()  # Empty line


# ============================================================================
# 3. USING next() FUNCTION
# ============================================================================
print("=" * 60)
print("3. USING next() FUNCTION")
print("=" * 60)

my_list = [1, 2, 3]
iterator = iter(my_list)

print(f"  next(iterator): {next(iterator)}")
print(f"  next(iterator): {next(iterator)}")
print(f"  next(iterator): {next(iterator)}")

try:
    print(f"  next(iterator): {next(iterator)}")
except StopIteration:
    print("  StopIteration raised - iterator exhausted")

print()  # Empty line


# ============================================================================
# 4. FOR LOOP AUTOMATICALLY HANDLES ITERATION
# ============================================================================
print("=" * 60)
print("4. FOR LOOP AUTOMATICALLY HANDLES ITERATION")
print("=" * 60)

print("  for loop automatically:")
print("    1. Calls iter() to get iterator")
print("    2. Calls next() repeatedly")
print("    3. Handles StopIteration")

for item in [1, 2, 3]:
    print(f"    {item}")

print()  # Empty line


# ============================================================================
# 5. CHECKING IF OBJECT IS ITERABLE
# ============================================================================
print("=" * 60)
print("5. CHECKING IF OBJECT IS ITERABLE")
print("=" * 60)

from collections.abc import Iterable, Iterator

print(f"  [1, 2, 3] is Iterable: {isinstance([1, 2, 3], Iterable)}")
print(f"  iter([1, 2, 3]) is Iterator: {isinstance(iter([1, 2, 3]), Iterator)}")
print(f"  5 is Iterable: {isinstance(5, Iterable)}")

print()  # Empty line


# ============================================================================
# 6. ITERATOR PROTOCOL
# ============================================================================
print("=" * 60)
print("6. ITERATOR PROTOCOL")
print("=" * 60)

print("  Iterator must implement:")
print("    - __iter__(): Returns self")
print("    - __next__(): Returns next item or raises StopIteration")
print("  ")
print("  Iterable must implement:")
print("    - __iter__(): Returns an iterator")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("ITERATORS SUMMARY:")
print("=" * 60)
print("  - Iterator implements __iter__() and __next__()")
print("  - Iterable implements __iter__()")
print("  - Use iter() to get iterator from iterable")
print("  - Use next() to get next value")
print("  - StopIteration signals end of iteration")
print("  - for loop handles iteration automatically")
print("=" * 60)

