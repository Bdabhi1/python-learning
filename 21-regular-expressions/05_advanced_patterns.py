"""
Advanced Regular Expression Patterns

This file demonstrates lookahead, lookbehind, and other advanced features.
"""

import re

# ============================================================================
# 1. POSITIVE LOOKAHEAD
# ============================================================================
print("=" * 60)
print("1. POSITIVE LOOKAHEAD")
print("=" * 60)

text = "email@example.com"
pattern = r"\w+(?=@)"  # Word before @

match = re.search(pattern, text)
if match:
    print(f"  Pattern: \\w+(?=@)")
    print(f"  Match: {match.group()}")

print()  # Empty line


# ============================================================================
# 2. NEGATIVE LOOKAHEAD
# ============================================================================
print("=" * 60)
print("2. NEGATIVE LOOKAHEAD")
print("=" * 60)

text = "100px 200em 300"
pattern = r"\d+(?!px)"  # Number not followed by "px"

matches = re.findall(pattern, text)
print(f"  Pattern: \\d+(?!px)")
print(f"  Matches: {matches}")

print()  # Empty line


# ============================================================================
# 3. POSITIVE LOOKBEHIND
# ============================================================================
print("=" * 60)
print("3. POSITIVE LOOKBEHIND")
print("=" * 60)

text = "Price: $100"
pattern = r"(?<=\$)\d+"  # Number after $

match = re.search(pattern, text)
if match:
    print(f"  Pattern: (?<=\\$)\\d+")
    print(f"  Match: {match.group()}")

print()  # Empty line


# ============================================================================
# 4. REGEX FLAGS
# ============================================================================
print("=" * 60)
print("4. REGEX FLAGS")
print("=" * 60)

text = "Hello\nWorld"

# re.IGNORECASE
matches1 = re.findall(r"hello", text, re.IGNORECASE)
print(f"  IGNORECASE: {matches1}")

# re.MULTILINE
matches2 = re.findall(r"^World", text, re.MULTILINE)
print(f"  MULTILINE: {matches2}")

# re.DOTALL
matches3 = re.findall(r".*", text, re.DOTALL)
print(f"  DOTALL: {matches3[0][:20]}...")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("ADVANCED PATTERNS SUMMARY:")
print("=" * 60)
print("  - (?=...): Positive lookahead")
print("  - (?!...): Negative lookahead")
print("  - (?<=...): Positive lookbehind")
print("  - (?<!...): Negative lookbehind")
print("  - re.IGNORECASE: Case insensitive")
print("  - re.MULTILINE: ^ and $ match line boundaries")
print("  - re.DOTALL: . matches newline")
print("=" * 60)

