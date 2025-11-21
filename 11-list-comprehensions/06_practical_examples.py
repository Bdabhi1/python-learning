"""
Practical List Comprehension Examples

This file demonstrates real-world examples of list comprehensions for
common programming tasks and problems.
"""

# ============================================================================
# 1. DATA PROCESSING
# ============================================================================
print("=" * 60)
print("1. DATA PROCESSING")
print("=" * 60)

# Process user data
users = ["alice", "bob", "charlie", "diana"]
formatted_users = [user.capitalize() for user in users]
print(f"  Users: {users}")
print(f"  Formatted: {formatted_users}")

# Extract and process
data = [("Alice", 25), ("Bob", 30), ("Charlie", 28)]
adults = [name for name, age in data if age >= 18]
print(f"  Data: {data}")
print(f"  Adults: {adults}")

# Calculate statistics
scores = [85, 92, 78, 96, 88]
passing = [score for score in scores if score >= 70]
print(f"  Scores: {scores}")
print(f"  Passing (>=70): {passing}")
print(f"  Average: {sum(scores) / len(scores):.2f}")

print()  # Empty line


# ============================================================================
# 2. TEXT PROCESSING
# ============================================================================
print("=" * 60)
print("2. TEXT PROCESSING")
print("=" * 60)

# Extract words from sentences
sentences = ["Hello world", "Python is great", "Learn programming"]
all_words = [word for sentence in sentences for word in sentence.split()]
print(f"  Sentences: {sentences}")
print(f"  All words: {all_words}")

# Filter and transform words
text = "Python is a great programming language"
long_words = [word.upper() for word in text.split() if len(word) > 5]
print(f"  Text: '{text}'")
print(f"  Long words (uppercase): {long_words}")

# Extract unique characters
text = "hello world"
unique_chars = list({char for char in text if char != " "})
print(f"  Text: '{text}'")
print(f"  Unique characters: {unique_chars}")

print()  # Empty line


# ============================================================================
# 3. FILTERING AND VALIDATION
# ============================================================================
print("=" * 60)
print("3. FILTERING AND VALIDATION")
print("=" * 60)

# Filter valid emails (simple)
emails = ["user@example.com", "invalid", "test@test.org", "notanemail"]
valid_emails = [email for email in emails if "@" in email and "." in email]
print(f"  Emails: {emails}")
print(f"  Valid emails: {valid_emails}")

# Filter numeric strings
strings = ["123", "abc", "45", "hello", "789"]
numeric = [s for s in strings if s.isdigit()]
print(f"  Strings: {strings}")
print(f"  Numeric strings: {numeric}")

# Validate and extract
data = [("Alice", 25, "Engineer"), ("Bob", 17, "Student"), ("Charlie", 30, "Doctor")]
adults = [f"{name} ({job})" for name, age, job in data if age >= 18]
print(f"  Data: {data}")
print(f"  Adults: {adults}")

print()  # Empty line


# ============================================================================
# 4. DATA TRANSFORMATION
# ============================================================================
print("=" * 60)
print("4. DATA TRANSFORMATION")
print("=" * 60)

# Transform prices
prices = [10.50, 20.75, 15.00, 30.25]
prices_with_tax = [price * 1.08 for price in prices]
print(f"  Original prices: {prices}")
print(f"  Prices with tax (8%): {prices_with_tax}")

# Convert units
temperatures_c = [0, 25, 37, 100]
temperatures_f = [(c * 9/5) + 32 for c in temperatures_c]
print(f"  Celsius: {temperatures_c}")
print(f"  Fahrenheit: {temperatures_f}")

# Format data
people = [("Alice", 25), ("Bob", 30), ("Charlie", 28)]
formatted = [f"{name} is {age} years old" for name, age in people]
print(f"  People: {people}")
print(f"  Formatted: {formatted}")

print()  # Empty line


# ============================================================================
# 5. MATHEMATICAL OPERATIONS
# ============================================================================
print("=" * 60)
print("5. MATHEMATICAL OPERATIONS")
print("=" * 60)

# Generate sequences
squares = [x ** 2 for x in range(1, 11)]
print(f"  Squares (1-10): {squares}")

# Calculate areas
radii = [1, 2, 3, 4, 5]
areas = [3.14159 * r ** 2 for r in radii]
print(f"  Radii: {radii}")
print(f"  Areas: {areas}")

# Filter and calculate
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
print(f"  Numbers: {numbers}")
print(f"  Even squares: {even_squares}")

print()  # Empty line


# ============================================================================
# 6. WORKING WITH NESTED DATA
# ============================================================================
print("=" * 60)
print("6. WORKING WITH NESTED DATA")
print("=" * 60)

# Flatten nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"  Matrix: {matrix}")
print(f"  Flattened: {flattened}")

# Extract from nested dictionaries
students = [
    {"name": "Alice", "scores": [95, 87, 92]},
    {"name": "Bob", "scores": [78, 85, 80]},
    {"name": "Charlie", "scores": [92, 94, 90]}
]
all_scores = [score for student in students for score in student["scores"]]
print(f"  Students: {students}")
print(f"  All scores: {all_scores}")

print()  # Empty line


# ============================================================================
# 7. CREATING LOOKUP TABLES
# ============================================================================
print("=" * 60)
print("7. CREATING LOOKUP TABLES")
print("=" * 60)

# Create square lookup
numbers = [1, 2, 3, 4, 5]
square_lookup = {num: num ** 2 for num in numbers}
print(f"  Numbers: {numbers}")
print(f"  Square lookup: {square_lookup}")

# Create grade mapping
scores = [85, 92, 78, 96, 88]
grade_map = {score: "A" if score >= 90 else "B" if score >= 80 else "C" 
             for score in scores}
print(f"  Scores: {scores}")
print(f"  Grade map: {grade_map}")

print()  # Empty line


# ============================================================================
# 8. DATA AGGREGATION
# ============================================================================
print("=" * 60)
print("8. DATA AGGREGATION")
print("=" * 60)

# Count word frequencies
text = "hello world hello python world"
words = text.split()
word_count = {word: words.count(word) for word in set(words)}
print(f"  Text: '{text}'")
print(f"  Word frequencies: {word_count}")

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

print()  # Empty line


# ============================================================================
# 9. COMBINING MULTIPLE OPERATIONS
# ============================================================================
print("=" * 60)
print("9. COMBINING MULTIPLE OPERATIONS")
print("=" * 60)

# Complex data processing
students = [
    {"name": "Alice", "age": 25, "scores": [95, 87, 92]},
    {"name": "Bob", "age": 30, "scores": [78, 85, 80]},
    {"name": "Charlie", "age": 28, "scores": [92, 94, 90]}
]
# Get names of students with average score >= 90
top_students = [
    student["name"] 
    for student in students 
    if sum(student["scores"]) / len(student["scores"]) >= 90
]
print(f"  Students: {students}")
print(f"  Top students (avg >= 90): {top_students}")

# Filter, transform, and format
products = [
    ("Apple", 1.50, 10),
    ("Banana", 0.75, 5),
    ("Orange", 2.00, 8)
]
# Get formatted names of affordable products with stock > 5
affordable = [
    f"{name} (${price:.2f})" 
    for name, price, stock in products 
    if price < 2.00 and stock > 5
]
print(f"  Products: {products}")
print(f"  Affordable with stock > 5: {affordable}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL LIST COMPREHENSION EXAMPLES SUMMARY:")
print("=" * 60)
print("Key Applications:")
print("  - Data processing: filtering, transforming, extracting")
print("  - Text processing: parsing, filtering, formatting")
print("  - Validation: checking conditions, filtering invalid data")
print("  - Mathematical operations: calculations, sequences")
print("  - Nested data: flattening, extracting, processing")
print("  - Lookup tables: creating dictionaries from data")
print("  - Data aggregation: counting, grouping, summarizing")
print("\nRemember:")
print("  - Comprehensions are concise and readable")
print("  - Combine filtering and transformation")
print("  - Use for data processing tasks")
print("  - Consider readability over complexity")
print("=" * 60)

