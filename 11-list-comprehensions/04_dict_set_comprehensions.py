"""
Dictionary and Set Comprehensions in Python

This file demonstrates comprehensions for dictionaries and sets, similar
to list comprehensions but for other data structures.
"""

# ============================================================================
# 1. DICTIONARY COMPREHENSIONS
# ============================================================================
print("=" * 60)
print("1. DICTIONARY COMPREHENSIONS")
print("=" * 60)

# Basic dictionary comprehension
squares = {x: x ** 2 for x in range(5)}
print(f"  Squares: {squares}")

# From list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
my_dict = {key: value for key, value in pairs}
print(f"  From pairs: {my_dict}")

# With conditions
numbers = [1, 2, 3, 4, 5, 6]
even_squares = {x: x ** 2 for x in numbers if x % 2 == 0}
print(f"  Numbers: {numbers}")
print(f"  Even squares: {even_squares}")

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {value: key for key, value in original.items()}
print(f"  Original: {original}")
print(f"  Swapped: {swapped}")

print()  # Empty line


# ============================================================================
# 2. SET COMPREHENSIONS
# ============================================================================
print("=" * 60)
print("2. SET COMPREHENSIONS")
print("=" * 60)

# Basic set comprehension
squares = {x ** 2 for x in range(5)}
print(f"  Squares: {squares} (note: set, so unordered)")

# Remove duplicates
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = {x for x in numbers}
print(f"  Numbers: {numbers}")
print(f"  Unique: {unique}")

# With conditions
evens = {x for x in range(10) if x % 2 == 0}
print(f"  Even numbers: {evens}")

print()  # Empty line


# ============================================================================
# 3. DICTIONARY FROM TWO LISTS
# ============================================================================
print("=" * 60)
print("3. DICTIONARY FROM TWO LISTS")
print("=" * 60)

# Create dictionary from two lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
person = {keys[i]: values[i] for i in range(len(keys))}
print(f"  Keys: {keys}")
print(f"  Values: {values}")
print(f"  Dictionary: {person}")

# Using zip (more Pythonic)
person2 = {k: v for k, v in zip(keys, values)}
print(f"  Using zip: {person2}")

print()  # Empty line


# ============================================================================
# 4. DICTIONARY WITH CONDITIONAL VALUES
# ============================================================================
print("=" * 60)
print("4. DICTIONARY WITH CONDITIONAL VALUES")
print("=" * 60)

# Conditional values
numbers = [1, 2, 3, 4, 5]
labels = {x: "even" if x % 2 == 0 else "odd" for x in numbers}
print(f"  Numbers: {numbers}")
print(f"  Labels: {labels}")

# Grade mapping
scores = [85, 92, 78, 96, 88]
grades = {score: "A" if score >= 90 else "B" if score >= 80 else "C" 
          for score in scores}
print(f"  Scores: {scores}")
print(f"  Grades: {grades}")

print()  # Empty line


# ============================================================================
# 5. FILTERING DICTIONARIES
# ============================================================================
print("=" * 60)
print("5. FILTERING DICTIONARIES")
print("=" * 60)

# Filter dictionary by value
scores = {"Alice": 95, "Bob": 87, "Charlie": 92, "Diana": 78}
high_scores = {name: score for name, score in scores.items() if score >= 90}
print(f"  All scores: {scores}")
print(f"  High scores (>=90): {high_scores}")

# Filter by key
data = {"name": "Alice", "age": 25, "email": "alice@example.com", "phone": "123-456-7890"}
personal = {k: v for k, v in data.items() if k in ["name", "age"]}
print(f"  All data: {data}")
print(f"  Personal info: {personal}")

print()  # Empty line


# ============================================================================
# 6. TRANSFORMING DICTIONARY VALUES
# ============================================================================
print("=" * 60)
print("6. TRANSFORMING DICTIONARY VALUES")
print("=" * 60)

# Transform values
prices = {"apple": 1.50, "banana": 0.75, "orange": 2.00}
prices_with_tax = {item: price * 1.08 for item, price in prices.items()}
print(f"  Original prices: {prices}")
print(f"  Prices with tax (8%): {prices_with_tax}")

# Transform keys
data = {"first_name": "Alice", "last_name": "Smith", "age": 25}
snake_case = {k.replace("_", ""): v for k, v in data.items()}
print(f"  Original: {data}")
print(f"  Transformed keys: {snake_case}")

print()  # Empty line


# ============================================================================
# 7. SET OPERATIONS WITH COMPREHENSIONS
# ============================================================================
print("=" * 60)
print("7. SET OPERATIONS WITH COMPREHENSIONS")
print("=" * 60)

# Create set from string
text = "hello world"
unique_chars = {char for char in text if char != " "}
print(f"  Text: '{text}'")
print(f"  Unique characters: {unique_chars}")

# Extract unique words
sentences = ["hello world", "world python", "python is great"]
all_words = {word for sentence in sentences for word in sentence.split()}
print(f"  Sentences: {sentences}")
print(f"  All unique words: {all_words}")

print()  # Empty line


# ============================================================================
# 8. NESTED DICTIONARY COMPREHENSIONS
# ============================================================================
print("=" * 60)
print("8. NESTED DICTIONARY COMPREHENSIONS")
print("=" * 60)

# Create nested dictionary
matrix_dict = {i: {j: i * j for j in range(1, 4)} for i in range(1, 4)}
print(f"  Matrix dictionary: {matrix_dict}")

# Flatten nested dictionary
nested = {
    "group1": {"Alice": 25, "Bob": 30},
    "group2": {"Charlie": 28, "Diana": 22}
}
flattened = {name: age for group in nested.values() for name, age in group.items()}
print(f"  Nested: {nested}")
print(f"  Flattened: {flattened}")

print()  # Empty line


# ============================================================================
# 9. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("9. PRACTICAL EXAMPLES")
print("=" * 60)

# Count word frequencies
text = "hello world hello python world"
words = text.split()
word_count = {word: words.count(word) for word in set(words)}
print(f"  Text: '{text}'")
print(f"  Word frequencies: {word_count}")

# Create lookup dictionary
items = [("apple", 1.50), ("banana", 0.75), ("orange", 2.00)]
price_lookup = {item: price for item, price in items}
print(f"  Items: {items}")
print(f"  Price lookup: {price_lookup}")

# Filter and transform
students = {"Alice": 95, "Bob": 87, "Charlie": 92, "Diana": 78}
honor_roll = {name: "A" if score >= 90 else "B" 
              for name, score in students.items() if score >= 85}
print(f"  Students: {students}")
print(f"  Honor roll (>=85): {honor_roll}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("DICTIONARY AND SET COMPREHENSIONS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Dictionary: {key: value for item in iterable}")
print("  - Set: {expression for item in iterable}")
print("  - Can add conditions: {k: v for k, v in items if condition}")
print("  - Can transform keys and values")
print("  - Sets automatically remove duplicates")
print("\nCommon Patterns:")
print("  - Dict from pairs: {k: v for k, v in pairs}")
print("  - Dict from lists: {k: v for k, v in zip(keys, values)}")
print("  - Unique items: {x for x in items}")
print("  - Filter dict: {k: v for k, v in d.items() if condition}")
print("=" * 60)

