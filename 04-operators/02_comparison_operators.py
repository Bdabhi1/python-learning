"""
Comparison Operators in Python

This file demonstrates comparison operators that compare values and return
True or False. These are essential for conditional statements and loops.
"""

# ============================================================================
# 1. EQUAL (==)
# ============================================================================
print("=" * 60)
print("1. EQUAL (==)")
print("=" * 60)

# Compare numbers
result1 = 5 == 5
print(f"  5 == 5: {result1}")

result2 = 5 == 3
print(f"  5 == 3: {result2}")

# Compare strings
result3 = "hello" == "hello"
print(f"  'hello' == 'hello': {result3}")

result4 = "hello" == "world"
print(f"  'hello' == 'world': {result4}")

# Compare different types
result5 = 5 == 5.0
print(f"  5 == 5.0: {result5} (value comparison)")

result6 = "5" == 5
print(f"  '5' == 5: {result6} (different types)")

print()  # Empty line


# ============================================================================
# 2. NOT EQUAL (!=)
# ============================================================================
print("=" * 60)
print("2. NOT EQUAL (!=)")
print("=" * 60)

# Compare numbers
result1 = 5 != 3
print(f"  5 != 3: {result1}")

result2 = 5 != 5
print(f"  5 != 5: {result2}")

# Compare strings
result3 = "hello" != "world"
print(f"  'hello' != 'world': {result3}")

result4 = "hello" != "hello"
print(f"  'hello' != 'hello': {result4}")

print()  # Empty line


# ============================================================================
# 3. LESS THAN (<)
# ============================================================================
print("=" * 60)
print("3. LESS THAN (<)")
print("=" * 60)

# Compare numbers
result1 = 3 < 5
print(f"  3 < 5: {result1}")

result2 = 10 < 5
print(f"  10 < 5: {result2}")

result3 = 5 < 5
print(f"  5 < 5: {result3}")

# Compare strings (lexicographic order)
result4 = "apple" < "banana"
print(f"  'apple' < 'banana': {result4}")

result5 = "zebra" < "apple"
print(f"  'zebra' < 'apple': {result5}")

print()  # Empty line


# ============================================================================
# 4. GREATER THAN (>)
# ============================================================================
print("=" * 60)
print("4. GREATER THAN (>)")
print("=" * 60)

# Compare numbers
result1 = 5 > 3
print(f"  5 > 3: {result1}")

result2 = 3 > 5
print(f"  3 > 5: {result2}")

result3 = 5 > 5
print(f"  5 > 5: {result3}")

# Compare strings
result4 = "banana" > "apple"
print(f"  'banana' > 'apple': {result4}")

print()  # Empty line


# ============================================================================
# 5. LESS THAN OR EQUAL (<=)
# ============================================================================
print("=" * 60)
print("5. LESS THAN OR EQUAL (<=)")
print("=" * 60)

# Compare numbers
result1 = 5 <= 5
print(f"  5 <= 5: {result1}")

result2 = 3 <= 5
print(f"  3 <= 5: {result2}")

result3 = 6 <= 5
print(f"  6 <= 5: {result3}")

print()  # Empty line


# ============================================================================
# 6. GREATER THAN OR EQUAL (>=)
# ============================================================================
print("=" * 60)
print("6. GREATER THAN OR EQUAL (>=)")
print("=" * 60)

# Compare numbers
result1 = 5 >= 5
print(f"  5 >= 5: {result1}")

result2 = 6 >= 5
print(f"  6 >= 5: {result1}")

result3 = 4 >= 5
print(f"  4 >= 5: {result3}")

print()  # Empty line


# ============================================================================
# 7. CHAINED COMPARISONS
# ============================================================================
print("=" * 60)
print("7. CHAINED COMPARISONS")
print("=" * 60)

# Python allows chaining comparisons
result1 = 1 < 2 < 3
print(f"  1 < 2 < 3: {result1} (equivalent to: 1 < 2 and 2 < 3)")

result2 = 5 < 10 < 15
print(f"  5 < 10 < 15: {result2}")

result3 = 1 < 2 < 1
print(f"  1 < 2 < 1: {result3}")

# Multiple chains
result4 = 1 < 2 < 3 < 4
print(f"  1 < 2 < 3 < 4: {result4}")

# Mixed operators
result5 = 5 <= 10 < 15
print(f"  5 <= 10 < 15: {result5}")

print()  # Empty line


# ============================================================================
# 8. COMPARING DIFFERENT TYPES
# ============================================================================
print("=" * 60)
print("8. COMPARING DIFFERENT TYPES")
print("=" * 60)

# Numbers
print("Numbers:")
print(f"  5 == 5.0: {5 == 5.0}")
print(f"  5 < 5.5: {5 < 5.5}")

# Strings (case-sensitive)
print("\nStrings (case-sensitive):")
print(f"  'Hello' == 'hello': {'Hello' == 'hello'}")
print(f"  'A' < 'a': {'A' < 'a'}")

# Lists (element-wise comparison)
print("\nLists:")
print(f"  [1, 2] == [1, 2]: {[1, 2] == [1, 2]}")
print(f"  [1, 2] < [1, 3]: {[1, 2] < [1, 3]}")

print()  # Empty line


# ============================================================================
# 9. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("9. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Check if user is old enough
age = 18
min_age = 18
can_vote = age >= min_age
print(f"  Age: {age}, Can vote: {can_vote}")

# Example 2: Check if score is passing
score = 85
passing_score = 60
is_passing = score >= passing_score
print(f"  Score: {score}, Is passing: {is_passing}")

# Example 3: Check if number is in range
number = 15
in_range = 10 <= number <= 20
print(f"  Number: {number}, In range [10, 20]: {in_range}")

# Example 4: Compare strings alphabetically
name1 = "Alice"
name2 = "Bob"
comes_first = name1 < name2
print(f"  '{name1}' < '{name2}': {comes_first}")

# Example 5: Check if values are equal
x = 5
y = 5
are_equal = x == y
print(f"  x = {x}, y = {y}, Are equal: {are_equal}")

print()  # Empty line


# ============================================================================
# 10. COMPARISON WITH VARIABLES
# ============================================================================
print("=" * 60)
print("10. COMPARISON WITH VARIABLES")
print("=" * 60)

# Store values in variables
a = 10
b = 5
c = 10

# Compare variables
print(f"  a = {a}, b = {b}, c = {c}")
print(f"  a == b: {a == b}")
print(f"  a == c: {a == c}")
print(f"  a < b: {a < b}")
print(f"  a > b: {a > b}")
print(f"  a <= c: {a <= c}")
print(f"  a >= b: {a >= b}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("COMPARISON OPERATORS SUMMARY:")
print("=" * 60)
print("Operator | Description              | Example      | Result")
print("---------|---------------------------|--------------|--------")
print("==       | Equal to                  | 5 == 5       | True")
print("!=       | Not equal to              | 5 != 3       | True")
print("<        | Less than                 | 3 < 5        | True")
print(">        | Greater than              | 5 > 3        | True")
print("<=       | Less than or equal        | 5 <= 5       | True")
print(">=       | Greater than or equal     | 5 >= 3       | True")
print("=" * 60)
print("\nKey Points:")
print("  - All comparison operators return True or False")
print("  - Can chain comparisons: 1 < 2 < 3")
print("  - Works with numbers, strings, and other types")
print("  - String comparison is lexicographic (alphabetical)")
print("  - Use == for equality, not = (which is assignment)")
print("=" * 60)

