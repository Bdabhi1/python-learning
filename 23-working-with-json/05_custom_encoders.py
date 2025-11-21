"""
Custom JSON Encoders

This file demonstrates handling complex objects with custom encoders.
"""

import json
from datetime import datetime

# ============================================================================
# 1. PROBLEM: DATETIME NOT JSON SERIALIZABLE
# ============================================================================
print("=" * 60)
print("1. PROBLEM: DATETIME NOT JSON SERIALIZABLE")
print("=" * 60)

data = {
    "name": "Alice",
    "created": datetime.now()
}

try:
    json_string = json.dumps(data)
except TypeError as e:
    print(f"  Error: {e}")
    print("  datetime objects are not JSON serializable by default")

print()  # Empty line


# ============================================================================
# 2. CUSTOM ENCODER
# ============================================================================
print("=" * 60)
print("2. CUSTOM ENCODER")
print("=" * 60)

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data = {
    "name": "Alice",
    "created": datetime.now()
}

json_string = json.dumps(data, cls=CustomEncoder)
print(f"  Encoded: {json_string}")

print()  # Empty line


# ============================================================================
# 3. DECODING WITH CUSTOM DECODER
# ============================================================================
print("=" * 60)
print("3. DECODING WITH CUSTOM DECODER")
print("=" * 60)

def decode_datetime(dct):
    if 'created' in dct:
        dct['created'] = datetime.fromisoformat(dct['created'])
    return dct

json_string = '{"name": "Alice", "created": "2024-01-15T14:30:00"}'
data = json.loads(json_string, object_hook=decode_datetime)

print(f"  Decoded: {data}")
print(f"  Created type: {type(data['created'])}")

print()  # Empty line


# ============================================================================
# 4. HANDLING MULTIPLE TYPES
# ============================================================================
print("=" * 60)
print("4. HANDLING MULTIPLE TYPES")
print("=" * 60)

class ExtendedEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, set):
            return list(obj)
        return super().default(obj)

data = {
    "name": "Alice",
    "created": datetime.now(),
    "tags": {"python", "json", "data"}
}

json_string = json.dumps(data, cls=ExtendedEncoder)
print(f"  Encoded: {json_string}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("CUSTOM ENCODERS SUMMARY:")
print("=" * 60)
print("  - Create custom encoder class inheriting from JSONEncoder")
print("  - Override default() method")
print("  - Handle non-serializable types")
print("  - Use object_hook for custom decoding")
print("=" * 60)

