"""
Encoding and Decoding JSON

This file demonstrates encoding Python objects to JSON and decoding JSON to Python.
"""

import json

# ============================================================================
# 1. ENCODING PYTHON TO JSON
# ============================================================================
print("=" * 60)
print("1. ENCODING PYTHON TO JSON")
print("=" * 60)

# Python dictionary
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "active": True,
    "hobbies": ["reading", "coding"]
}

# Encode to JSON
json_string = json.dumps(data)
print(f"  Python: {data}")
print(f"  JSON: {json_string}")

print()  # Empty line


# ============================================================================
# 2. DECODING JSON TO PYTHON
# ============================================================================
print("=" * 60)
print("2. DECODING JSON TO PYTHON")
print("=" * 60)

json_string = '{"name": "Bob", "age": 25, "city": "London"}'

# Decode from JSON
data = json.loads(json_string)
print(f"  JSON: {json_string}")
print(f"  Python: {data}")
print(f"  Type: {type(data)}")

print()  # Empty line


# ============================================================================
# 3. TYPE PRESERVATION
# ============================================================================
print("=" * 60)
print("3. TYPE PRESERVATION")
print("=" * 60)

json_string = '''
{
    "string": "text",
    "number": 42,
    "float": 3.14,
    "boolean": true,
    "null": null,
    "array": [1, 2, 3]
}
'''

data = json.loads(json_string)
print(f"  string type: {type(data['string'])}")
print(f"  number type: {type(data['number'])}")
print(f"  boolean type: {type(data['boolean'])}")
print(f"  null type: {type(data['null'])}")
print(f"  array type: {type(data['array'])}")

print()  # Empty line


# ============================================================================
# 4. NESTED STRUCTURES
# ============================================================================
print("=" * 60)
print("4. NESTED STRUCTURES")
print("=" * 60)

nested_data = {
    "user": {
        "name": "Alice",
        "address": {
            "street": "123 Main St",
            "city": "New York"
        }
    },
    "tags": ["python", "json", "data"]
}

json_string = json.dumps(nested_data)
print(f"  Nested JSON: {json_string}")

decoded = json.loads(json_string)
print(f"  Access nested: {decoded['user']['address']['city']}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("ENCODING/DECODING SUMMARY:")
print("=" * 60)
print("  - json.dumps(): Encode Python to JSON string")
print("  - json.loads(): Decode JSON string to Python")
print("  - Types are preserved during encoding/decoding")
print("  - Nested structures are supported")
print("=" * 60)

