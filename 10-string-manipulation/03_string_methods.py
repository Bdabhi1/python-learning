"""
String Methods in Python

This file demonstrates Python's built-in string methods for manipulating
and working with strings.
"""

# ============================================================================
# 1. CASE CONVERSION METHODS
# ============================================================================
print("=" * 60)
print("1. CASE CONVERSION METHODS")
print("=" * 60)

text = "Hello World Python"
print(f"  Original: '{text}'")

# Convert to uppercase
print(f"  .upper(): '{text.upper()}'")

# Convert to lowercase
print(f"  .lower(): '{text.lower()}'")

# Capitalize first letter
print(f"  .capitalize(): '{text.capitalize()}'")

# Title case (first letter of each word)
print(f"  .title(): '{text.title()}'")

# Swap case
print(f"  .swapcase(): '{text.swapcase()}'")

print()  # Empty line


# ============================================================================
# 2. CHECKING STRING CONTENT
# ============================================================================
print("=" * 60)
print("2. CHECKING STRING CONTENT")
print("=" * 60)

# isalpha() - only letters
print(f"  'Python'.isalpha(): {'Python'.isalpha()}")
print(f"  'Python123'.isalpha(): {'Python123'.isalpha()}")

# isdigit() - only digits
print(f"  '123'.isdigit(): {'123'.isdigit()}")
print(f"  '12.3'.isdigit(): {'12.3'.isdigit()}")

# isalnum() - letters and/or digits
print(f"  'Python123'.isalnum(): {'Python123'.isalnum()}")
print(f"  'Python 123'.isalnum(): {'Python 123'.isalnum()}")

# isspace() - only whitespace
print(f"  '   '.isspace(): {'   '.isspace()}")
print(f"  'Hello'.isspace(): {'Hello'.isspace()}")

# islower() - all lowercase
print(f"  'python'.islower(): {'python'.islower()}")
print(f"  'Python'.islower(): {'Python'.islower()}")

# isupper() - all uppercase
print(f"  'PYTHON'.isupper(): {'PYTHON'.isupper()}")
print(f"  'Python'.isupper(): {'Python'.isupper()}")

print()  # Empty line


# ============================================================================
# 3. FINDING AND SEARCHING
# ============================================================================
print("=" * 60)
print("3. FINDING AND SEARCHING")
print("=" * 60)

text = "Hello World Hello"

# find() - returns index or -1 if not found
print(f"  text.find('World'): {text.find('World')}")
print(f"  text.find('Python'): {text.find('Python')}")  # Returns -1
print(f"  text.find('Hello'): {text.find('Hello')}")  # First occurrence
print(f"  text.find('Hello', 1): {text.find('Hello', 1)}")  # Start from index 1

# rfind() - find from right
print(f"  text.rfind('Hello'): {text.rfind('Hello')}")

# index() - like find() but raises ValueError if not found
print(f"  text.index('World'): {text.index('World')}")
try:
    text.index('Python')
except ValueError:
    print("  text.index('Python'): ValueError (not found)")

# count() - count occurrences
print(f"  text.count('Hello'): {text.count('Hello')}")
print(f"  text.count('l'): {text.count('l')}")

# startswith() - check if starts with
print(f"  text.startswith('Hello'): {text.startswith('Hello')}")
print(f"  text.startswith('World'): {text.startswith('World')}")

# endswith() - check if ends with
print(f"  text.endswith('Hello'): {text.endswith('Hello')}")
print(f"  text.endswith('World'): {text.endswith('World')}")

print()  # Empty line


# ============================================================================
# 4. REPLACING AND MODIFYING
# ============================================================================
print("=" * 60)
print("4. REPLACING AND MODIFYING")
print("=" * 60)

text = "Hello World Hello"

# replace() - replace substring
print(f"  Original: '{text}'")
print(f"  .replace('Hello', 'Hi'): '{text.replace('Hello', 'Hi')}'")
print(f"  .replace('Hello', 'Hi', 1): '{text.replace('Hello', 'Hi', 1)}'")  # Replace first occurrence only

# Note: strings are immutable, so replace returns a new string
print(f"  Original unchanged: '{text}'")

print()  # Empty line


# ============================================================================
# 5. SPLITTING AND JOINING
# ============================================================================
print("=" * 60)
print("5. SPLITTING AND JOINING")
print("=" * 60)

# split() - split into list
text = "apple,banana,orange"
fruits = text.split(",")
print(f"  '{text}'.split(','): {fruits}")

# split() without argument (splits on whitespace)
sentence = "Hello World Python"
words = sentence.split()
print(f"  '{sentence}'.split(): {words}")

# join() - join list into string
words = ["Hello", "World", "Python"]
joined = " ".join(words)
print(f"  ' '.join({words}): '{joined}'")

# join() with different separator
joined = "-".join(words)
print(f"  '-'.join({words}): '{joined}'")

print()  # Empty line


# ============================================================================
# 6. STRIPPING WHITESPACE
# ============================================================================
print("=" * 60)
print("6. STRIPPING WHITESPACE")
print("=" * 60)

text = "  Hello World  "
print(f"  Original: '{text}'")

# strip() - remove from both ends
print(f"  .strip(): '{text.strip()}'")

# lstrip() - remove from left
print(f"  .lstrip(): '{text.lstrip()}'")

# rstrip() - remove from right
print(f"  .rstrip(): '{text.rstrip()}'")

# strip() with specific characters
text2 = "!!!Hello!!!"
print(f"  Original: '{text2}'")
print(f"  .strip('!'): '{text2.strip('!')}'")

print()  # Empty line


# ============================================================================
# 7. PADDING AND ALIGNMENT
# ============================================================================
print("=" * 60)
print("7. PADDING AND ALIGNMENT")
print("=" * 60)

text = "Hello"
print(f"  Original: '{text}'")

# center() - center in width
print(f"  .center(11): '{text.center(11)}'")
print(f"  .center(11, '-'): '{text.center(11, '-')}'")

# ljust() - left align
print(f"  .ljust(10): '{text.ljust(10)}'")
print(f"  .ljust(10, '-'): '{text.ljust(10, '-')}'")

# rjust() - right align
print(f"  .rjust(10): '{text.rjust(10)}'")
print(f"  .rjust(10, '-'): '{text.rjust(10, '-')}'")

# zfill() - zero fill (pad with zeros)
number = "42"
print(f"  '{number}'.zfill(5): '{number.zfill(5)}'")

print()  # Empty line


# ============================================================================
# 8. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("8. PRACTICAL EXAMPLES")
print("=" * 60)

# Validate email format (simple)
def is_valid_email(email):
    """Simple email validation."""
    return "@" in email and "." in email and email.count("@") == 1

email = "user@example.com"
print(f"  Email '{email}' is valid: {is_valid_email(email)}")

# Extract words from sentence
sentence = "Python is a great programming language"
words = sentence.split()
print(f"  Sentence: '{sentence}'")
print(f"  Words: {words}")
print(f"  Word count: {len(words)}")

# Format phone number
phone = "1234567890"
formatted = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
print(f"  Phone: '{phone}'")
print(f"  Formatted: '{formatted}'")

# Capitalize names
names = "john doe jane smith"
capitalized = " ".join(name.capitalize() for name in names.split())
print(f"  Original: '{names}'")
print(f"  Capitalized: '{capitalized}'")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("STRING METHODS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Strings have many built-in methods")
print("  - Methods return new strings (strings are immutable)")
print("  - Case methods: upper(), lower(), title(), capitalize()")
print("  - Check methods: isalpha(), isdigit(), isalnum(), etc.")
print("  - Search methods: find(), index(), count(), startswith(), endswith()")
print("  - Modify methods: replace(), strip(), split(), join()")
print("\nCommon Methods:")
print("  - text.upper() - convert to uppercase")
print("  - text.lower() - convert to lowercase")
print("  - text.split() - split into list")
print("  - ' '.join(list) - join list into string")
print("  - text.replace(old, new) - replace substring")
print("  - text.strip() - remove whitespace")
print("=" * 60)

