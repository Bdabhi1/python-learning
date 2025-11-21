"""
Practical JSON Examples

This file demonstrates real-world JSON use cases.
"""

import json
import os

# ============================================================================
# 1. CONFIGURATION FILE
# ============================================================================
print("=" * 60)
print("1. CONFIGURATION FILE")
print("=" * 60)

config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "mydb"
    },
    "api": {
        "key": "secret_key",
        "timeout": 30
    }
}

# Save config
with open('config.json', 'w') as f:
    json.dump(config, f, indent=2)

# Load config
with open('config.json', 'r') as f:
    loaded_config = json.load(f)

print(f"  Config loaded: {loaded_config['database']['host']}")

print()  # Empty line


# ============================================================================
# 2. API RESPONSE HANDLING
# ============================================================================
print("=" * 60)
print("2. API RESPONSE HANDLING")
print("=" * 60)

# Simulated API response
api_response = '''
{
    "status": "success",
    "data": {
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ]
    }
}
'''

response = json.loads(api_response)
print(f"  Status: {response['status']}")
print(f"  Users: {len(response['data']['users'])}")

print()  # Empty line


# ============================================================================
# 3. DATA VALIDATION
# ============================================================================
print("=" * 60)
print("3. DATA VALIDATION")
print("=" * 60)

def is_valid_json(json_string):
    try:
        json.loads(json_string)
        return True
    except json.JSONDecodeError:
        return False

test_strings = [
    '{"valid": true}',
    'invalid json',
    '{"missing": quote}'
]

for test in test_strings:
    valid = is_valid_json(test)
    print(f"  '{test[:20]}...': {'Valid' if valid else 'Invalid'}")

print()  # Empty line


# ============================================================================
# 4. MERGING JSON DATA
# ============================================================================
print("=" * 60)
print("4. MERGING JSON DATA")
print("=" * 60)

data1 = {"name": "Alice", "age": 30}
data2 = {"city": "New York", "age": 31}

# Merge (data2 overwrites data1)
merged = {**data1, **data2}
print(f"  Merged: {merged}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL EXAMPLES SUMMARY:")
print("=" * 60)
print("JSON is useful for:")
print("  - Configuration files")
print("  - API responses")
print("  - Data storage")
print("  - Data exchange between systems")
print("=" * 60)

