"""
String Indexing and Slicing in Python

This file demonstrates how to access individual characters and extract
substrings from strings using indexing and slicing.
"""

# ============================================================================
# 1. STRING INDEXING (POSITIVE INDICES)
# ============================================================================
print("=" * 60)
print("1. STRING INDEXING (POSITIVE INDICES)")
print("=" * 60)

text = "Python"
print(f"  String: '{text}'")
print(f"  Length: {len(text)}")

# Access individual characters (0-based indexing)
print(f"  text[0] = '{text[0]}'  (first character)")
print(f"  text[1] = '{text[1]}'  (second character)")
print(f"  text[2] = '{text[2]}'  (third character)")
print(f"  text[5] = '{text[5]}'  (last character)")

# Index out of range
try:
    print(f"  text[10] = '{text[10]}'")  # This will cause IndexError
except IndexError:
    print("  text[10] causes IndexError (index out of range)")

print()  # Empty line


# ============================================================================
# 2. NEGATIVE INDEXING
# ============================================================================
print("=" * 60)
print("2. NEGATIVE INDEXING")
print("=" * 60)

text = "Python"
print(f"  String: '{text}'")

# Negative indices count from the end
print(f"  text[-1] = '{text[-1]}'  (last character)")
print(f"  text[-2] = '{text[-2]}'  (second from last)")
print(f"  text[-3] = '{text[-3]}'  (third from last)")
print(f"  text[-6] = '{text[-6]}'  (first character)")

# Visual representation
print("\n  Index mapping:")
print("    P  y  t  h  o  n")
print("    0  1  2  3  4  5  (positive indices)")
print("   -6 -5 -4 -3 -2 -1  (negative indices)")

print()  # Empty line


# ============================================================================
# 3. BASIC SLICING
# ============================================================================
print("=" * 60)
print("3. BASIC SLICING")
print("=" * 60)

text = "Python Programming"
print(f"  String: '{text}'")

# Syntax: [start:end] (end is exclusive)
print(f"  text[0:6] = '{text[0:6]}'  (characters 0 to 5)")
print(f"  text[7:18] = '{text[7:18]}'  (characters 7 to 17)")

# Omitting start (starts from beginning)
print(f"  text[:6] = '{text[:6]}'  (from start to index 5)")

# Omitting end (goes to end)
print(f"  text[7:] = '{text[7:]}'  (from index 7 to end)")

# Omitting both (entire string)
print(f"  text[:] = '{text[:]}'  (entire string, creates copy)")

print()  # Empty line


# ============================================================================
# 4. SLICING WITH NEGATIVE INDICES
# ============================================================================
print("=" * 60)
print("4. SLICING WITH NEGATIVE INDICES")
print("=" * 60)

text = "Python Programming"
print(f"  String: '{text}'")

# Using negative indices
print(f"  text[-11:] = '{text[-11:]}'  (last 11 characters)")
print(f"  text[:-11] = '{text[:-11]}'  (all except last 11)")
print(f"  text[-11:-1] = '{text[-11:-1]}'  (from -11 to -2)")

# Mix positive and negative
print(f"  text[0:-11] = '{text[0:-11]}'  (from start to -11)")

print()  # Empty line


# ============================================================================
# 5. SLICING WITH STEP SIZE
# ============================================================================
print("=" * 60)
print("5. SLICING WITH STEP SIZE")
print("=" * 60)

text = "Python Programming"
print(f"  String: '{text}'")

# Syntax: [start:end:step]
print(f"  text[::2] = '{text[::2]}'  (every 2nd character)")
print(f"  text[::3] = '{text[::3]}'  (every 3rd character)")

# Start from specific index with step
print(f"  text[1::2] = '{text[1::2]}'  (every 2nd from index 1)")

# Reverse string
print(f"  text[::-1] = '{text[::-1]}'  (reversed string)")

# Every 2nd character in reverse
print(f"  text[::-2] = '{text[::-2]}'  (every 2nd in reverse)")

print()  # Empty line


# ============================================================================
# 6. COMMON SLICING PATTERNS
# ============================================================================
print("=" * 60)
print("6. COMMON SLICING PATTERNS")
print("=" * 60)

text = "Python"
print(f"  String: '{text}'")

# Get first character
print(f"  First char: text[0] = '{text[0]}'")
print(f"  First char: text[:1] = '{text[:1]}'")

# Get last character
print(f"  Last char: text[-1] = '{text[-1]}'")
print(f"  Last char: text[len(text)-1] = '{text[len(text)-1]}'")

# Get first n characters
print(f"  First 3: text[:3] = '{text[:3]}'")

# Get last n characters
print(f"  Last 3: text[-3:] = '{text[-3:]}'")

# Remove first character
print(f"  Without first: text[1:] = '{text[1:]}'")

# Remove last character
print(f"  Without last: text[:-1] = '{text[:-1]}'")

# Remove first and last
print(f"  Without both: text[1:-1] = '{text[1:-1]}'")

print()  # Empty line


# ============================================================================
# 7. ITERATING THROUGH STRINGS
# ============================================================================
print("=" * 60)
print("7. ITERATING THROUGH STRINGS")
print("=" * 60)

text = "Python"
print(f"  String: '{text}'")

# Iterate through characters
print("  Characters:")
for char in text:
    print(f"    {char}")

# Iterate with index
print("\n  Characters with index:")
for i, char in enumerate(text):
    print(f"    [{i}] = '{char}'")

# Iterate in reverse
print("\n  Characters in reverse:")
for char in reversed(text):
    print(f"    {char}")

# Iterate with slicing
print("\n  Every 2nd character:")
for char in text[::2]:
    print(f"    {char}")

print()  # Empty line


# ============================================================================
# 8. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("8. PRACTICAL EXAMPLES")
print("=" * 60)

# Extract file extension
filename = "document.pdf"
extension = filename[-3:]  # Last 3 characters
print(f"  Filename: '{filename}'")
print(f"  Extension: '{extension}'")

# Better approach (handles variable length)
filename2 = "image.jpeg"
if "." in filename2:
    extension = filename2[filename2.rfind(".")+1:]
    print(f"  Filename: '{filename2}'")
    print(f"  Extension: '{extension}'")

# Extract domain from email
email = "user@example.com"
if "@" in email:
    domain = email[email.find("@")+1:]
    print(f"  Email: '{email}'")
    print(f"  Domain: '{domain}'")

# Get middle characters
text = "Programming"
middle = text[len(text)//2-1:len(text)//2+2]
print(f"  String: '{text}'")
print(f"  Middle 3 chars: '{middle}'")

# Reverse words in a string
sentence = "Hello World Python"
words = sentence.split()
reversed_sentence = " ".join(word[::-1] for word in words)
print(f"  Original: '{sentence}'")
print(f"  Reversed words: '{reversed_sentence}'")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("STRING INDEXING AND SLICING SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Indexing: str[index] - access single character")
print("  - Positive indices: 0 to len(str)-1 (left to right)")
print("  - Negative indices: -1 to -len(str) (right to left)")
print("  - Slicing: str[start:end] - extract substring")
print("  - End index is exclusive (not included)")
print("  - Step: str[start:end:step] - skip characters")
print("\nCommon Patterns:")
print("  - First char: str[0] or str[:1]")
print("  - Last char: str[-1]")
print("  - First n: str[:n]")
print("  - Last n: str[-n:]")
print("  - Reverse: str[::-1]")
print("=" * 60)

