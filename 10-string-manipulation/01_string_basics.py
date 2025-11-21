"""
String Basics in Python

This file demonstrates how to create and work with strings - the fundamental
way to handle text data in Python.
"""

# ============================================================================
# 1. CREATING STRINGS
# ============================================================================
print("=" * 60)
print("1. CREATING STRINGS")
print("=" * 60)

# Single quotes
name1 = 'Alice'
print(f"  Single quotes: {name1}")

# Double quotes
name2 = "Bob"
print(f"  Double quotes: {name2}")

# Both work the same way
print(f"  name1 == name2: {name1 == name2}")

# Use double quotes when string contains single quotes
message1 = "It's a beautiful day"
print(f"  Contains apostrophe: {message1}")

# Use single quotes when string contains double quotes
message2 = 'He said "Hello"'
print(f"  Contains quotes: {message2}")

print()  # Empty line


# ============================================================================
# 2. TRIPLE QUOTES (MULTI-LINE STRINGS)
# ============================================================================
print("=" * 60)
print("2. TRIPLE QUOTES (MULTI-LINE STRINGS)")
print("=" * 60)

# Multi-line string with triple double quotes
poem = """Roses are red,
Violets are blue,
Python is awesome,
And so are you!"""
print("  Multi-line string:")
print(poem)

# Triple single quotes also work
quote = '''This is a
multi-line string
using single quotes'''
print("\n  Triple single quotes:")
print(quote)

print()  # Empty line


# ============================================================================
# 3. STRING CONCATENATION
# ============================================================================
print("=" * 60)
print("3. STRING CONCATENATION")
print("=" * 60)

# Using + operator
first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name
print(f"  Concatenation: {full_name}")

# Using += operator
greeting = "Hello"
greeting += " World"
print(f"  Using +=: {greeting}")

# Multiple concatenations
sentence = "Python" + " is" + " great"
print(f"  Multiple concatenations: {sentence}")

print()  # Empty line


# ============================================================================
# 4. STRING REPETITION
# ============================================================================
print("=" * 60)
print("4. STRING REPETITION")
print("=" * 60)

# Using * operator
line = "-" * 50
print(f"  Repeated dash: {line}")

# Repeat words
cheer = "Hip " * 3 + "Hooray!"
print(f"  Repeated word: {cheer}")

# Create patterns
pattern = "*" * 10
print(f"  Pattern: {pattern}")

print()  # Empty line


# ============================================================================
# 5. STRING LENGTH
# ============================================================================
print("=" * 60)
print("5. STRING LENGTH")
print("=" * 60)

text = "Python"
length = len(text)
print(f"  Length of '{text}': {length}")

# Empty string
empty = ""
print(f"  Length of empty string: {len(empty)}")

# Multi-line string
multi = """Line 1
Line 2
Line 3"""
print(f"  Length of multi-line string: {len(multi)} (includes newlines)")

print()  # Empty line


# ============================================================================
# 6. CHECKING STRING TYPE
# ============================================================================
print("=" * 60)
print("6. CHECKING STRING TYPE")
print("=" * 60)

text = "Hello"
print(f"  Type of 'Hello': {type(text)}")
print(f"  Is string? {isinstance(text, str)}")

# Different ways to check
number_str = "123"
print(f"  '123' is string: {isinstance(number_str, str)}")
print(f"  Note: '123' is a string, not a number!")

print()  # Empty line


# ============================================================================
# 7. STRING IMMUTABILITY
# ============================================================================
print("=" * 60)
print("7. STRING IMMUTABILITY")
print("=" * 60)

text = "Hello"
print(f"  Original: {text}")

# Strings are immutable - you can't change them directly
# text[0] = "h"  # This would cause TypeError!

# Instead, create a new string
new_text = "h" + text[1:]
print(f"  New string: {new_text}")
print(f"  Original unchanged: {text}")

# Operations create new strings
upper_text = text.upper()
print(f"  After .upper(): {upper_text}")
print(f"  Original still unchanged: {text}")

print()  # Empty line


# ============================================================================
# 8. MEMBERSHIP TESTING
# ============================================================================
print("=" * 60)
print("8. MEMBERSHIP TESTING")
print("=" * 60)

text = "Python Programming"

# Check if substring exists
print(f"  'Python' in '{text}': {'Python' in text}")
print(f"  'Java' in '{text}': {'Java' in text}")
print(f"  'python' in '{text}': {'python' in text}")  # Case-sensitive
print(f"  'python' in '{text.lower()}': {'python' in text.lower()}")

# Check if character exists
print(f"  'P' in '{text}': {'P' in text}")
print(f"  'z' in '{text}': {'z' in text}")

print()  # Empty line


# ============================================================================
# 9. STRING COMPARISON
# ============================================================================
print("=" * 60)
print("9. STRING COMPARISON")
print("=" * 60)

# Equality
str1 = "Hello"
str2 = "Hello"
str3 = "hello"
print(f"  '{str1}' == '{str2}': {str1 == str2}")
print(f"  '{str1}' == '{str3}': {str1 == str3}")

# Lexicographic comparison
print(f"  'apple' < 'banana': {'apple' < 'banana'}")
print(f"  'zebra' > 'apple': {'zebra' > 'apple'}")

# Case matters
print(f"  'A' < 'a': {'A' < 'a'}")  # Uppercase comes before lowercase in ASCII

print()  # Empty line


# ============================================================================
# 10. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("10. PRACTICAL EXAMPLES")
print("=" * 60)

# Building a formatted message
first = "John"
last = "Doe"
age = 30
message = f"{first} {last} is {age} years old"
print(f"  Formatted message: {message}")

# Creating a separator line
def create_separator(char, length):
    """Create a separator line."""
    return char * length

separator = create_separator("=", 40)
print(f"  Separator: {separator}")

# Repeating a pattern
def create_border(text, char="*", padding=2):
    """Create a border around text."""
    border_char = char * (len(text) + padding * 2)
    return f"{border_char}\n{char * padding}{text}{char * padding}\n{border_char}"

print("\n  Text border:")
print(create_border("Hello", "*", 2))

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("STRING BASICS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Strings are sequences of characters")
print("  - Use single, double, or triple quotes")
print("  - Strings are immutable (cannot be changed)")
print("  - Use + for concatenation, * for repetition")
print("  - Use len() to get string length")
print("  - Use 'in' to check membership")
print("\nCommon Operations:")
print("  - Concatenation: str1 + str2")
print("  - Repetition: str * n")
print("  - Length: len(str)")
print("  - Membership: 'sub' in str")
print("  - Comparison: str1 == str2, str1 < str2")
print("=" * 60)

