"""
Character Classes in Regular Expressions

This file demonstrates character classes and predefined character sets.
"""

import re

# ============================================================================
# 1. BASIC CHARACTER CLASSES
# ============================================================================
print("=" * 60)
print("1. BASIC CHARACTER CLASSES")
print("=" * 60)

text = "apple"
pattern = r"[aeiou]"  # Match any vowel

matches = re.findall(pattern, text)
print(f"  Pattern: {pattern}")
print(f"  Text: {text}")
print(f"  Matches: {matches}")

print()  # Empty line


# ============================================================================
# 2. RANGES IN CHARACTER CLASSES
# ============================================================================
print("=" * 60)
print("2. RANGES IN CHARACTER CLASSES")
print("=" * 60)

text = "Hello123"
pattern1 = r"[a-z]"  # Lowercase letters
pattern2 = r"[A-Z]"  # Uppercase letters
pattern3 = r"[0-9]"  # Digits

matches1 = re.findall(pattern1, text)
matches2 = re.findall(pattern2, text)
matches3 = re.findall(pattern3, text)

print(f"  [a-z]: {matches1}")
print(f"  [A-Z]: {matches2}")
print(f"  [0-9]: {matches3}")

print()  # Empty line


# ============================================================================
# 3. NEGATED CHARACTER CLASSES
# ============================================================================
print("=" * 60)
print("3. NEGATED CHARACTER CLASSES")
print("=" * 60)

text = "abc123"
pattern = r"[^0-9]"  # Anything except digits

matches = re.findall(pattern, text)
print(f"  Pattern: [^0-9] (non-digits)")
print(f"  Matches: {matches}")

print()  # Empty line


# ============================================================================
# 4. PREDEFINED CHARACTER CLASSES
# ============================================================================
print("=" * 60)
print("4. PREDEFINED CHARACTER CLASSES")
print("=" * 60)

text = "Hello 123 World!"

# \d - digits
digits = re.findall(r"\d", text)
print(f"  \\d (digits): {digits}")

# \D - non-digits
non_digits = re.findall(r"\D", text)
print(f"  \\D (non-digits): {''.join(non_digits[:10])}...")

# \w - word characters
words = re.findall(r"\w+", text)
print(f"  \\w+ (words): {words}")

# \s - whitespace
whitespace = re.findall(r"\s", text)
print(f"  \\s (whitespace): {len(whitespace)} spaces")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("CHARACTER CLASSES SUMMARY:")
print("=" * 60)
print("  - [abc]: Match a, b, or c")
print("  - [a-z]: Match lowercase letters")
print("  - [^abc]: Match anything except a, b, c")
print("  - \\d: Digit [0-9]")
print("  - \\D: Non-digit")
print("  - \\w: Word character [a-zA-Z0-9_]")
print("  - \\W: Non-word character")
print("  - \\s: Whitespace")
print("  - \\S: Non-whitespace")
print("=" * 60)

