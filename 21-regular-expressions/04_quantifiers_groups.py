"""
Quantifiers and Groups in Regular Expressions

This file demonstrates quantifiers and capturing groups.
"""

import re

# ============================================================================
# 1. BASIC QUANTIFIERS
# ============================================================================
print("=" * 60)
print("1. BASIC QUANTIFIERS")
print("=" * 60)

text = "aa aaa aaaa"

# * - zero or more
matches1 = re.findall(r"a*", text)
print(f"  a* (zero or more): {matches1[:5]}...")

# + - one or more
matches2 = re.findall(r"a+", text)
print(f"  a+ (one or more): {matches2}")

# ? - zero or one
matches3 = re.findall(r"a?", text)
print(f"  a? (zero or one): {matches3[:5]}...")

# {n} - exactly n
matches4 = re.findall(r"a{3}", text)
print(f"  a{{3}} (exactly 3): {matches4}")

# {n,m} - between n and m
matches5 = re.findall(r"a{2,4}", text)
print(f"  a{{2,4}} (2 to 4): {matches5}")

print()  # Empty line


# ============================================================================
# 2. CAPTURING GROUPS
# ============================================================================
print("=" * 60)
print("2. CAPTURING GROUPS")
print("=" * 60)

text = "John Doe, Jane Smith"
pattern = r"(\w+) (\w+)"  # Two groups

matches = re.findall(pattern, text)
print(f"  Pattern: {pattern}")
print(f"  All matches: {matches}")

# Using search to get groups
match = re.search(pattern, text)
if match:
    print(f"  Full match: {match.group(0)}")
    print(f"  Group 1: {match.group(1)}")
    print(f"  Group 2: {match.group(2)}")

print()  # Empty line


# ============================================================================
# 3. NAMED GROUPS
# ============================================================================
print("=" * 60)
print("3. NAMED GROUPS")
print("=" * 60)

text = "John Doe"
pattern = r"(?P<first>\w+) (?P<last>\w+)"

match = re.search(pattern, text)
if match:
    print(f"  First name: {match.group('first')}")
    print(f"  Last name: {match.group('last')}")

print()  # Empty line


# ============================================================================
# 4. GREEDY VS NON-GREEDY
# ============================================================================
print("=" * 60)
print("4. GREEDY VS NON-GREEDY")
print("=" * 60)

text = "<div>content</div>"

# Greedy (default)
greedy = re.search(r"<.*>", text)
print(f"  Greedy: {greedy.group()}")

# Non-greedy
non_greedy = re.search(r"<.*?>", text)
print(f"  Non-greedy: {non_greedy.group()}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("QUANTIFIERS AND GROUPS SUMMARY:")
print("=" * 60)
print("  - *: Zero or more (greedy)")
print("  - +: One or more (greedy)")
print("  - ?: Zero or one")
print("  - {{n}}: Exactly n times")
print("  - {{n,m}}: Between n and m times")
print("  - (): Capturing group")
print("  - (?P<name>...): Named group")
print("  - *? +? ??: Non-greedy quantifiers")
print("=" * 60)

