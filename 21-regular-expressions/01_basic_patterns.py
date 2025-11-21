"""
Basic Regular Expression Patterns

This file demonstrates basic pattern matching with Python's re module.
"""

import re

# ============================================================================
# 1. SIMPLE SEARCH
# ============================================================================
print("=" * 60)
print("1. SIMPLE SEARCH")
print("=" * 60)

text = "Hello, World!"
pattern = "World"

match = re.search(pattern, text)
if match:
    print(f"  Found: '{match.group()}' at position {match.start()}-{match.end()}")

print()  # Empty line


# ============================================================================
# 2. re.match() - MATCH AT START
# ============================================================================
print("=" * 60)
print("2. re.match() - MATCH AT START")
print("=" * 60)

text = "Hello, World!"
pattern = "Hello"

match = re.match(pattern, text)  # Only matches at start
if match:
    print(f"  Matched: '{match.group()}'")

# This won't match
match = re.match("World", text)
if not match:
    print("  'World' doesn't match at start")

print()  # Empty line


# ============================================================================
# 3. re.findall() - FIND ALL MATCHES
# ============================================================================
print("=" * 60)
print("3. re.findall() - FIND ALL MATCHES")
print("=" * 60)

text = "The cat sat on the mat"
pattern = "the"

matches = re.findall(pattern, text, re.IGNORECASE)
print(f"  Found {len(matches)} matches: {matches}")

print()  # Empty line


# ============================================================================
# 4. re.sub() - REPLACE MATCHES
# ============================================================================
print("=" * 60)
print("4. re.sub() - REPLACE MATCHES")
print("=" * 60)

text = "Hello, World!"
pattern = "World"
replacement = "Python"

result = re.sub(pattern, replacement, text)
print(f"  Original: {text}")
print(f"  Replaced: {result}")

print()  # Empty line


# ============================================================================
# 5. USING RAW STRINGS
# ============================================================================
print("=" * 60)
print("5. USING RAW STRINGS")
print("=" * 60)

# Raw strings (r"...") are recommended for regex
pattern1 = r"\d+"  # Matches digits
pattern2 = "\\d+"  # Same, but more verbose

text = "I have 5 apples and 10 oranges"
matches = re.findall(pattern1, text)
print(f"  Pattern: {pattern1}")
print(f"  Matches: {matches}")

print("\n  Always use raw strings (r'...') for regex patterns!")

print()  # Empty line


# ============================================================================
# 6. COMPILING PATTERNS
# ============================================================================
print("=" * 60)
print("6. COMPILING PATTERNS")
print("=" * 60)

# Compile pattern for reuse
pattern = re.compile(r'\d+')

text1 = "I have 5 apples"
text2 = "There are 10 oranges"

matches1 = pattern.findall(text1)
matches2 = pattern.findall(text2)

print(f"  Text1 matches: {matches1}")
print(f"  Text2 matches: {matches2}")

print("\n  Compile patterns when reusing them!")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("BASIC PATTERNS SUMMARY:")
print("=" * 60)
print("  - re.search(): Find first match anywhere")
print("  - re.match(): Match only at start")
print("  - re.findall(): Find all matches")
print("  - re.sub(): Replace matches")
print("  - Use raw strings (r'...') for patterns")
print("  - Compile patterns for reuse")
print("=" * 60)

