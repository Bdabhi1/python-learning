"""
Conditional List Comprehensions in Python

This file demonstrates how to add conditions to list comprehensions for
filtering and conditional transformations.
"""

# ============================================================================
# 1. BASIC FILTERING WITH IF
# ============================================================================
print("=" * 60)
print("1. BASIC FILTERING WITH IF")
print("=" * 60)

# Filter even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(f"  Even numbers: {evens}")

# Filter odd numbers
odds = [x for x in range(10) if x % 2 != 0]
print(f"  Odd numbers: {odds}")

# Filter positive numbers
numbers = [-2, -1, 0, 1, 2, 3]
positives = [x for x in numbers if x > 0]
print(f"  Numbers: {numbers}")
print(f"  Positives: {positives}")

# Filter words by length
words = ["hello", "world", "python", "hi", "programming"]
long_words = [word for word in words if len(word) > 5]
print(f"  Words: {words}")
print(f"  Long words (>5 chars): {long_words}")

print()  # Empty line


# ============================================================================
# 2. CONDITIONAL EXPRESSIONS (TERNARY OPERATOR)
# ============================================================================
print("=" * 60)
print("2. CONDITIONAL EXPRESSIONS (TERNARY OPERATOR)")
print("=" * 60)

# Mark even/odd
numbers = [1, 2, 3, 4, 5]
labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(f"  Numbers: {numbers}")
print(f"  Labels: {labels}")

# Absolute values
numbers = [-2, -1, 0, 1, 2]
abs_values = [x if x >= 0 else -x for x in numbers]
print(f"  Numbers: {numbers}")
print(f"  Absolute values: {abs_values}")

# Or simply use abs()
abs_values2 = [abs(x) for x in numbers]
print(f"  Using abs(): {abs_values2}")

# Grade assignment
scores = [85, 92, 78, 96, 88]
grades = ["A" if score >= 90 else "B" if score >= 80 else "C" for score in scores]
print(f"  Scores: {scores}")
print(f"  Grades: {grades}")

print()  # Empty line


# ============================================================================
# 3. MULTIPLE CONDITIONS
# ============================================================================
print("=" * 60)
print("3. MULTIPLE CONDITIONS")
print("=" * 60)

# Multiple if conditions (AND)
numbers = list(range(20))
filtered = [x for x in numbers if x % 2 == 0 if x % 3 == 0]
print(f"  Numbers divisible by 2 AND 3: {filtered}")

# Using and operator
filtered2 = [x for x in numbers if x % 2 == 0 and x % 3 == 0]
print(f"  Using 'and': {filtered2}")

# Complex conditions
ages = [15, 18, 20, 25, 30, 35, 65, 70]
adults = [age for age in ages if age >= 18 and age < 65]
print(f"  Ages: {ages}")
print(f"  Adults (18-64): {adults}")

# Multiple conditions with or
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = [x for x in numbers if x < 3 or x > 7]
print(f"  Numbers: {numbers}")
print(f"  Numbers < 3 OR > 7: {filtered}")

print()  # Empty line


# ============================================================================
# 4. COMBINING FILTERING AND TRANSFORMATION
# ============================================================================
print("=" * 60)
print("4. COMBINING FILTERING AND TRANSFORMATION")
print("=" * 60)

# Square only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
print(f"  Numbers: {numbers}")
print(f"  Even squares: {even_squares}")

# Uppercase only long words
words = ["hello", "world", "python", "hi", "programming"]
long_upper = [word.upper() for word in words if len(word) > 5]
print(f"  Words: {words}")
print(f"  Long words (uppercase): {long_upper}")

# Extract and process
people = [("Alice", 25), ("Bob", 17), ("Charlie", 30), ("Diana", 16)]
adult_names = [name.upper() for name, age in people if age >= 18]
print(f"  People: {people}")
print(f"  Adult names (uppercase): {adult_names}")

print()  # Empty line


# ============================================================================
# 5. FILTERING WITH MEMBERSHIP
# ============================================================================
print("=" * 60)
print("5. FILTERING WITH MEMBERSHIP")
print("=" * 60)

# Filter vowels
text = "Hello World Python"
vowels = [char for char in text if char.lower() in "aeiou"]
print(f"  Text: '{text}'")
print(f"  Vowels: {vowels}")

# Filter words containing specific letters
words = ["hello", "world", "python", "java", "javascript"]
filtered = [word for word in words if "a" in word]
print(f"  Words: {words}")
print(f"  Words with 'a': {filtered}")

# Filter numbers in range
numbers = [1, 5, 10, 15, 20, 25, 30]
in_range = [x for x in numbers if 10 <= x <= 20]
print(f"  Numbers: {numbers}")
print(f"  In range [10, 20]: {in_range}")

print()  # Empty line


# ============================================================================
# 6. FILTERING WITH STRING METHODS
# ============================================================================
print("=" * 60)
print("6. FILTERING WITH STRING METHODS")
print("=" * 60)

# Filter numeric strings
strings = ["123", "abc", "45", "hello", "789"]
numeric = [s for s in strings if s.isdigit()]
print(f"  Strings: {strings}")
print(f"  Numeric strings: {numeric}")

# Filter uppercase words
words = ["HELLO", "world", "PYTHON", "Java"]
uppercase = [word for word in words if word.isupper()]
print(f"  Words: {words}")
print(f"  Uppercase words: {uppercase}")

# Filter words starting with letter
words = ["hello", "123abc", "world", "456", "python"]
starts_letter = [word for word in words if word[0].isalpha()]
print(f"  Words: {words}")
print(f"  Starting with letter: {starts_letter}")

print()  # Empty line


# ============================================================================
# 7. COMPLEX CONDITIONAL LOGIC
# ============================================================================
print("=" * 60)
print("7. COMPLEX CONDITIONAL LOGIC")
print("=" * 60)

# Multiple transformations based on conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [
    "small even" if x < 5 and x % 2 == 0 
    else "small odd" if x < 5 
    else "large even" if x % 2 == 0 
    else "large odd" 
    for x in numbers
]
print(f"  Numbers: {numbers}")
print(f"  Categorized: {result}")

# Process based on type
mixed = [1, "hello", 2.5, "world", 3, "python"]
numbers_only = [x for x in mixed if isinstance(x, (int, float))]
strings_only = [x for x in mixed if isinstance(x, str)]
print(f"  Mixed: {mixed}")
print(f"  Numbers: {numbers_only}")
print(f"  Strings: {strings_only}")

print()  # Empty line


# ============================================================================
# 8. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("8. PRACTICAL EXAMPLES")
print("=" * 60)

# Filter valid email addresses (simple)
emails = ["user@example.com", "invalid", "test@test.org", "notanemail"]
valid_emails = [email for email in emails if "@" in email and "." in email]
print(f"  Emails: {emails}")
print(f"  Valid emails: {valid_emails}")

# Process scores
scores = [85, 92, 78, 96, 88, 65, 72]
passing = [score for score in scores if score >= 70]
print(f"  Scores: {scores}")
print(f"  Passing (>=70): {passing}")

# Extract and format
people = [("Alice", 25, "Engineer"), ("Bob", 17, "Student"), ("Charlie", 30, "Doctor")]
adults = [f"{name} ({age})" for name, age, job in people if age >= 18]
print(f"  People: {people}")
print(f"  Adult descriptions: {adults}")

# Price filtering
products = [("Apple", 1.50), ("Banana", 0.75), ("Orange", 2.00), ("Grape", 3.50)]
affordable = [name for name, price in products if price < 2.00]
print(f"  Products: {products}")
print(f"  Affordable (<$2.00): {affordable}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("CONDITIONAL LIST COMPREHENSIONS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Filtering: [x for x in iterable if condition]")
print("  - Conditional expression: [value1 if condition else value2 for x in iterable]")
print("  - Multiple conditions: use 'and', 'or' operators")
print("  - Combine filtering and transformation")
print("\nCommon Patterns:")
print("  - Filter: [x for x in items if x > 0]")
print("  - Transform conditionally: [x*2 if x%2==0 else x for x in items]")
print("  - Multiple conditions: [x for x in items if condition1 and condition2]")
print("=" * 60)

