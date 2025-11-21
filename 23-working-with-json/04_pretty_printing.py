"""
Pretty Printing JSON

This file demonstrates formatting JSON for readability.
"""

import json

# ============================================================================
# 1. BASIC PRETTY PRINTING
# ============================================================================
print("=" * 60)
print("1. BASIC PRETTY PRINTING")
print("=" * 60)

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "coding", "traveling"]
}

# Compact (default)
compact = json.dumps(data)
print("  Compact:")
print(f"    {compact}")

# Pretty printed
pretty = json.dumps(data, indent=4)
print("\n  Pretty printed (indent=4):")
print(pretty)

print()  # Empty line


# ============================================================================
# 2. SORTING KEYS
# ============================================================================
print("=" * 60)
print("2. SORTING KEYS")
print("=" * 60)

data = {"z": 3, "a": 1, "b": 2, "m": 4}

# Unsorted
unsorted = json.dumps(data, indent=2)
print("  Unsorted:")
print(unsorted)

# Sorted
sorted_json = json.dumps(data, sort_keys=True, indent=2)
print("\n  Sorted:")
print(sorted_json)

print()  # Empty line


# ============================================================================
# 3. CUSTOM INDENTATION
# ============================================================================
print("=" * 60)
print("3. CUSTOM INDENTATION")
print("=" * 60)

data = {"name": "Alice", "age": 30}

# Different indent values
for indent in [0, 2, 4]:
    formatted = json.dumps(data, indent=indent)
    print(f"  Indent {indent}:")
    print(f"    {formatted}")

print()  # Empty line


# ============================================================================
# 4. SEPARATORS
# ============================================================================
print("=" * 60)
print("4. SEPARATORS")
print("=" * 60)

data = {"name": "Alice", "age": 30}

# Default separators
default = json.dumps(data)
print(f"  Default: {default}")

# Custom separators (more compact)
compact = json.dumps(data, separators=(',', ':'))
print(f"  Compact: {compact}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRETTY PRINTING SUMMARY:")
print("=" * 60)
print("  - indent parameter: Add indentation for readability")
print("  - sort_keys=True: Sort keys alphabetically")
print("  - separators: Customize separators")
print("  - Use for debugging and human-readable output")
print("=" * 60)

