"""
Advanced String Operations in Python

This file demonstrates advanced string operations including escape sequences,
raw strings, and more complex manipulations.
"""

# ============================================================================
# 1. ESCAPE SEQUENCES
# ============================================================================
print("=" * 60)
print("1. ESCAPE SEQUENCES")
print("=" * 60)

# Newline
print("  Line 1\nLine 2")

# Tab
print("  Column1\tColumn2\tColumn3")

# Quotes
print('  He said "Hello"')
print("  It's a beautiful day")

# Backslash
print("  Path: C:\\Users\\Documents")

# Carriage return
print("  Hello\rWorld")  # Overwrites beginning

# Backspace
print("  Hello\bWorld")  # Removes 'o'

print()  # Empty line


# ============================================================================
# 2. RAW STRINGS
# ============================================================================
print("=" * 60)
print("2. RAW STRINGS")
print("=" * 60)

# Regular string (escape sequences processed)
path1 = "C:\\Users\\Documents"
print(f"  Regular: {path1}")

# Raw string (escape sequences ignored)
path2 = r"C:\Users\Documents"
print(f"  Raw: {path2}")

# Useful for regex patterns
pattern = r"\d+\.\d+"  # Matches numbers like "3.14"
print(f"  Regex pattern: {pattern}")

# Useful for Windows paths
windows_path = r"C:\Program Files\Python"
print(f"  Windows path: {windows_path}")

print()  # Empty line


# ============================================================================
# 3. STRING ITERATION PATTERNS
# ============================================================================
print("=" * 60)
print("3. STRING ITERATION PATTERNS")
print("=" * 60)

text = "Python"

# Iterate through characters
print("  Characters:")
for char in text:
    print(f"    {char}")

# Iterate with index
print("\n  With index:")
for i, char in enumerate(text):
    print(f"    [{i}] = '{char}'")

# Iterate in reverse
print("\n  Reverse:")
for char in reversed(text):
    print(f"    {char}")

# Iterate with step
print("\n  Every 2nd character:")
for char in text[::2]:
    print(f"    {char}")

print()  # Empty line


# ============================================================================
# 4. STRING COMPARISONS
# ============================================================================
print("=" * 60)
print("4. STRING COMPARISONS")
print("=" * 60)

# Equality
str1 = "Hello"
str2 = "Hello"
str3 = "hello"
print(f"  '{str1}' == '{str2}': {str1 == str2}")
print(f"  '{str1}' == '{str3}': {str1 == str3}")

# Case-insensitive comparison
print(f"  Case-insensitive: {str1.lower() == str3.lower()}")

# Lexicographic order
print(f"  'apple' < 'banana': {'apple' < 'banana'}")
print(f"  'zebra' > 'apple': {'zebra' > 'apple'}")

print()  # Empty line


# ============================================================================
# 5. STRING VALIDATION
# ============================================================================
print("=" * 60)
print("5. STRING VALIDATION")
print("=" * 60)

# Check if all characters are digits
def is_numeric(text):
    """Check if string contains only digits."""
    return text.isdigit()

print(f"  '123'.isdigit(): {is_numeric('123')}")
print(f"  '12.3'.isdigit(): {is_numeric('12.3')}")

# Check if all characters are letters
def is_alphabetic(text):
    """Check if string contains only letters."""
    return text.isalpha()

print(f"  'Hello'.isalpha(): {is_alphabetic('Hello')}")
print(f"  'Hello123'.isalpha(): {is_alphabetic('Hello123')}")

# Validate email (simple)
def is_valid_email(email):
    """Simple email validation."""
    return "@" in email and "." in email and email.count("@") == 1

print(f"  'user@example.com' is valid: {is_valid_email('user@example.com')}")
print(f"  'invalid' is valid: {is_valid_email('invalid')}")

print()  # Empty line


# ============================================================================
# 6. STRING TRANSFORMATIONS
# ============================================================================
print("=" * 60)
print("6. STRING TRANSFORMATIONS")
print("=" * 60)

# Reverse string
text = "Python"
reversed_text = text[::-1]
print(f"  Original: '{text}'")
print(f"  Reversed: '{reversed_text}'")

# Swap case
text = "Hello World"
swapped = text.swapcase()
print(f"  Original: '{text}'")
print(f"  Swapped: '{swapped}'")

# Title case
text = "hello world python"
titled = text.title()
print(f"  Original: '{text}'")
print(f"  Title: '{titled}'")

# Remove whitespace
text = "  Hello World  "
stripped = text.strip()
print(f"  Original: '{text}'")
print(f"  Stripped: '{stripped}'")

print()  # Empty line


# ============================================================================
# 7. STRING SEARCHING AND REPLACING
# ============================================================================
print("=" * 60)
print("7. STRING SEARCHING AND REPLACING")
print("=" * 60)

text = "Hello World Hello"

# Find substring
index = text.find("World")
print(f"  'World' found at index: {index}")

# Replace all occurrences
replaced = text.replace("Hello", "Hi")
print(f"  Original: '{text}'")
print(f"  Replaced: '{replaced}'")

# Replace first occurrence only
replaced_first = text.replace("Hello", "Hi", 1)
print(f"  Replace first: '{replaced_first}'")

print()  # Empty line


# ============================================================================
# 8. STRING SPLITTING AND JOINING
# ============================================================================
print("=" * 60)
print("8. STRING SPLITTING AND JOINING")
print("=" * 60)

# Split by delimiter
text = "apple,banana,orange"
fruits = text.split(",")
print(f"  Original: '{text}'")
print(f"  Split: {fruits}")

# Split by whitespace
sentence = "Hello World Python"
words = sentence.split()
print(f"  Original: '{sentence}'")
print(f"  Words: {words}")

# Join list into string
words = ["Hello", "World", "Python"]
joined = " ".join(words)
print(f"  Words: {words}")
print(f"  Joined: '{joined}'")

# Join with different separator
joined = "-".join(words)
print(f"  Joined with '-': '{joined}'")

print()  # Empty line


# ============================================================================
# 9. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("9. PRACTICAL EXAMPLES")
print("=" * 60)

# Palindrome checker
def is_palindrome(text):
    """Check if string is palindrome."""
    cleaned = text.lower().replace(" ", "").replace(",", "").replace(".", "")
    return cleaned == cleaned[::-1]

test1 = "racecar"
test2 = "A man a plan a canal Panama"
print(f"  '{test1}' is palindrome: {is_palindrome(test1)}")
print(f"  '{test2}' is palindrome: {is_palindrome(test2)}")

# Word count
def count_words(text):
    """Count words in text."""
    return len(text.split())

sentence = "Python is a great programming language"
print(f"  Sentence: '{sentence}'")
print(f"  Word count: {count_words(sentence)}")

# Extract initials
def get_initials(name):
    """Get initials from full name."""
    return "".join(word[0].upper() for word in name.split())

name = "John Doe Smith"
print(f"  Name: '{name}'")
print(f"  Initials: {get_initials(name)}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("ADVANCED STRING OPERATIONS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Escape sequences: \\n (newline), \\t (tab), \\\\ (backslash)")
print("  - Raw strings: r'text' - ignore escape sequences")
print("  - String iteration: for char in text")
print("  - String comparison: ==, <, > (lexicographic)")
print("  - Validation: isdigit(), isalpha(), isalnum()")
print("  - Transformations: reverse, swapcase, title")
print("  - Search/Replace: find(), replace()")
print("  - Split/Join: split(), join()")
print("=" * 60)

