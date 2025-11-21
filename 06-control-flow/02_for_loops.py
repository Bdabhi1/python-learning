"""
For Loops in Python

This file demonstrates for loops - how to iterate over sequences
and repeat code for each item.
"""

# ============================================================================
# 1. BASIC FOR LOOP
# ============================================================================
print("=" * 60)
print("1. BASIC FOR LOOP")
print("=" * 60)

# Iterate over a range
print("  Counting from 0 to 4:")
for i in range(5):
    print(f"    {i}")

print("\n  Structure:")
print("    for variable in sequence:")
print("        # Code to execute for each item")

print()  # Empty line


# ============================================================================
# 2. ITERATING OVER LISTS
# ============================================================================
print("=" * 60)
print("2. ITERATING OVER LISTS")
print("=" * 60)

# Iterate over list items
fruits = ["apple", "banana", "orange"]
print("  Fruits:")
for fruit in fruits:
    print(f"    - {fruit}")

# Iterate with index
print("\n  Fruits with index:")
for i in range(len(fruits)):
    print(f"    {i}: {fruits[i]}")

# Better: Use enumerate
print("\n  Fruits with enumerate:")
for index, fruit in enumerate(fruits):
    print(f"    {index}: {fruit}")

print()  # Empty line


# ============================================================================
# 3. ITERATING OVER STRINGS
# ============================================================================
print("=" * 60)
print("3. ITERATING OVER STRINGS")
print("=" * 60)

# Iterate over characters
word = "Python"
print(f"  Characters in '{word}':")
for char in word:
    print(f"    {char}")

# Count characters
count = 0
for char in word:
    count += 1
print(f"\n  Total characters: {count}")

print()  # Empty line


# ============================================================================
# 4. THE range() FUNCTION
# ============================================================================
print("=" * 60)
print("4. THE range() FUNCTION")
print("=" * 60)

# range(stop) - 0 to stop-1
print("  range(5):")
for i in range(5):
    print(f"    {i}")

# range(start, stop) - start to stop-1
print("\n  range(2, 5):")
for i in range(2, 5):
    print(f"    {i}")

# range(start, stop, step) - with step
print("\n  range(0, 10, 2):")
for i in range(0, 10, 2):
    print(f"    {i}")

# Countdown
print("\n  range(10, 0, -1) (countdown):")
for i in range(10, 0, -1):
    print(f"    {i}")

print()  # Empty line


# ============================================================================
# 5. ITERATING OVER DICTIONARIES
# ============================================================================
print("=" * 60)
print("5. ITERATING OVER DICTIONARIES")
print("=" * 60)

# Iterate over keys
person = {"name": "Alice", "age": 25, "city": "New York"}
print("  Dictionary keys:")
for key in person:
    print(f"    {key}")

# Iterate over values
print("\n  Dictionary values:")
for value in person.values():
    print(f"    {value}")

# Iterate over key-value pairs
print("\n  Dictionary items:")
for key, value in person.items():
    print(f"    {key}: {value}")

print()  # Empty line


# ============================================================================
# 6. NESTED FOR LOOPS
# ============================================================================
print("=" * 60)
print("6. NESTED FOR LOOPS")
print("=" * 60)

# Multiplication table
print("  Multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"    {i} x {j} = {i * j}")

# Grid pattern
print("\n  Grid pattern:")
for row in range(3):
    for col in range(3):
        print(f"    ({row}, {col})", end=" ")
    print()  # New line after each row

print()  # Empty line


# ============================================================================
# 7. FOR LOOP WITH ELSE
# ============================================================================
print("=" * 60)
print("7. FOR LOOP WITH ELSE")
print("=" * 60)

# else executes if loop completes normally (no break)
print("  Loop without break:")
for i in range(3):
    print(f"    {i}")
else:
    print("    Loop completed normally")

# else does NOT execute if break is used
print("\n  Loop with break:")
for i in range(5):
    if i == 3:
        break
    print(f"    {i}")
else:
    print("    This won't print (break was used)")

print()  # Empty line


# ============================================================================
# 8. ITERATING OVER MULTIPLE SEQUENCES
# ============================================================================
print("=" * 60)
print("8. ITERATING OVER MULTIPLE SEQUENCES")
print("=" * 60)

# zip() combines multiple sequences
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

print("  Using zip():")
for name, age in zip(names, ages):
    print(f"    {name} is {age} years old")

# Different length sequences
list1 = [1, 2, 3]
list2 = ["a", "b"]
print("\n  zip() with different lengths (stops at shortest):")
for item1, item2 in zip(list1, list2):
    print(f"    {item1}, {item2}")

print()  # Empty line


# ============================================================================
# 9. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("9. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Sum numbers
print("Example 1: Sum numbers")
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"  Numbers: {numbers}")
print(f"  Sum: {total}")

# Example 2: Find maximum
print("\nExample 2: Find maximum")
numbers = [5, 12, 8, 3, 15]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"  Numbers: {numbers}")
print(f"  Maximum: {max_num}")

# Example 3: Count occurrences
print("\nExample 3: Count occurrences")
text = "hello"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(f"  Text: '{text}'")
print(f"  Character counts: {char_count}")

# Example 4: Filter items
print("\nExample 4: Filter even numbers")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"  All numbers: {numbers}")
print(f"  Even numbers: {even_numbers}")

# Example 5: Process list of dictionaries
print("\nExample 5: Process list of dictionaries")
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]
print("  Student scores:")
for student in students:
    print(f"    {student['name']}: {student['score']}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("FOR LOOPS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Iterates over a sequence (list, string, range, etc.)")
print("  - Syntax: for variable in sequence:")
print("  - range() generates number sequences")
print("  - enumerate() provides index and value")
print("  - Can iterate over lists, strings, dictionaries, etc.")
print("  - Nested loops iterate within loops")
print("  - else clause executes if loop completes normally")
print("  - Use zip() to iterate over multiple sequences")
print("=" * 60)

