"""
Regex Metacharacters

This file demonstrates special characters in regular expressions.
"""

import re

# ============================================================================
# 1. DOT (.) - ANY CHARACTER
# ============================================================================
print("=" * 60)
print("1. DOT (.) - ANY CHARACTER")
print("=" * 60)

text = "cat bat rat"
pattern = r".at"  # Matches any character followed by "at"

matches = re.findall(pattern, text)
print(f"  Pattern: {pattern}")
print(f"  Matches: {matches}")

print()  # Empty line


# ============================================================================
# 2. CARET (^) - START OF STRING
# ============================================================================
print("=" * 60)
print("2. CARET (^) - START OF STRING")
print("=" * 60)

text1 = "Hello, World!"
text2 = "World, Hello!"

pattern = r"^Hello"

match1 = re.search(pattern, text1)
match2 = re.search(pattern, text2)

print(f"  Pattern: {pattern}")
print(f"  '{text1}': {'Match' if match1 else 'No match'}")
print(f"  '{text2}': {'Match' if match2 else 'No match'}")

print()  # Empty line


# ============================================================================
# 3. DOLLAR ($) - END OF STRING
# ============================================================================
print("=" * 60)
print("3. DOLLAR ($) - END OF STRING")
print("=" * 60)

text1 = "Hello, World!"
text2 = "Hello, World! Hi"

pattern = r"World!$"

match1 = re.search(pattern, text1)
match2 = re.search(pattern, text2)

print(f"  Pattern: {pattern}")
print(f"  '{text1}': {'Match' if match1 else 'No match'}")
print(f"  '{text2}': {'Match' if match2 else 'No match'}")

print()  # Empty line


# ============================================================================
# 4. ESCAPE (\) - LITERAL CHARACTERS
# ============================================================================
print("=" * 60)
print("4. ESCAPE (\\) - LITERAL CHARACTERS")
print("=" * 60)

text = "Price: $100.50"
pattern1 = r"\$"  # Match literal dollar sign
pattern2 = r"\."  # Match literal dot

matches1 = re.findall(pattern1, text)
matches2 = re.findall(pattern2, text)

print(f"  Pattern: {pattern1}, Matches: {matches1}")
print(f"  Pattern: {pattern2}, Matches: {matches2}")

print()  # Empty line


# ============================================================================
# 5. PIPE (|) - OR OPERATOR
# ============================================================================
print("=" * 60)
print("5. PIPE (|) - OR OPERATOR")
print("=" * 60)

text = "I like cats and dogs"
pattern = r"cat|dog"

matches = re.findall(pattern, text)
print(f"  Pattern: {pattern}")
print(f"  Matches: {matches}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("METACHARACTERS SUMMARY:")
print("=" * 60)
print("  - . (dot): Any character except newline")
print("  - ^: Start of string")
print("  - $: End of string")
print("  - \\: Escape special characters")
print("  - |: OR operator")
print("  - *: Zero or more")
print("  - +: One or more")
print("  - ?: Zero or one")
print("=" * 60)

