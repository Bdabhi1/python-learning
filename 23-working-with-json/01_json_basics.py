"""
JSON Basics in Python

This file demonstrates the fundamental concepts of JSON and the json module.
"""

import json

# ============================================================================
# 1. WHAT IS JSON?
# ============================================================================
print("=" * 60)
print("1. WHAT IS JSON?")
print("=" * 60)

print("  JSON (JavaScript Object Notation) is:")
print("    - A lightweight data interchange format")
print("    - Human-readable and easy to parse")
print("    - Language-independent")
print("    - Commonly used for APIs and configuration")
print("  ")
print("  JSON Data Types:")
print("    - String: \"text\"")
print("    - Number: 123 or 12.34")
print("    - Boolean: true or false")
print("    - Null: null")
print("    - Array: [1, 2, 3]")
print("    - Object: {\"key\": \"value\"}")

print()  # Empty line


# ============================================================================
# 2. THE json MODULE
# ============================================================================
print("=" * 60)
print("2. THE json MODULE")
print("=" * 60)

print("  Main functions:")
print("    - json.dumps(): Python object → JSON string")
print("    - json.loads(): JSON string → Python object")
print("    - json.dump(): Python object → JSON file")
print("    - json.load(): JSON file → Python object")

print()  # Empty line


# ============================================================================
# 3. BASIC JSON STRING
# ============================================================================
print("=" * 60)
print("3. BASIC JSON STRING")
print("=" * 60)

# Example JSON string
json_string = '{"name": "Alice", "age": 30, "city": "New York"}'
print(f"  JSON string: {json_string}")

# Parse to Python
data = json.loads(json_string)
print(f"  Python dict: {data}")
print(f"  Type: {type(data)}")

print()  # Empty line


# ============================================================================
# 4. PYTHON TO JSON
# ============================================================================
print("=" * 60)
print("4. PYTHON TO JSON")
print("=" * 60)

# Python dictionary
python_data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Convert to JSON
json_string = json.dumps(python_data)
print(f"  Python dict: {python_data}")
print(f"  JSON string: {json_string}")

print()  # Empty line


# ============================================================================
# 5. TYPE MAPPING
# ============================================================================
print("=" * 60)
print("5. TYPE MAPPING")
print("=" * 60)

print("  Python → JSON:")
print("    dict → object")
print("    list → array")
print("    str → string")
print("    int/float → number")
print("    True → true")
print("    False → false")
print("    None → null")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("JSON BASICS SUMMARY:")
print("=" * 60)
print("  - JSON is a data interchange format")
print("  - json.dumps(): Python → JSON string")
print("  - json.loads(): JSON string → Python")
print("  - Types map between Python and JSON")
print("  - JSON is human-readable and widely used")
print("=" * 60)

