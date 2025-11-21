"""
Reading and Writing JSON Files

This file demonstrates working with JSON files.
"""

import json
import os

# ============================================================================
# 1. WRITING JSON TO FILE
# ============================================================================
print("=" * 60)
print("1. WRITING JSON TO FILE")
print("=" * 60)

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "coding"]
}

# Write to file
with open('data.json', 'w') as f:
    json.dump(data, f)

print("  Data written to data.json")

# Verify
if os.path.exists('data.json'):
    print("  File created successfully")

print()  # Empty line


# ============================================================================
# 2. READING JSON FROM FILE
# ============================================================================
print("=" * 60)
print("2. READING JSON FROM FILE")
print("=" * 60)

# Read from file
with open('data.json', 'r') as f:
    loaded_data = json.load(f)

print(f"  Loaded data: {loaded_data}")

print()  # Empty line


# ============================================================================
# 3. ERROR HANDLING
# ============================================================================
print("=" * 60)
print("3. ERROR HANDLING")
print("=" * 60)

# File not found
try:
    with open('nonexistent.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    print("  File not found - handled gracefully")

# Invalid JSON
try:
    with open('data.json', 'w') as f:
        f.write('invalid json')
    
    with open('data.json', 'r') as f:
        data = json.load(f)
except json.JSONDecodeError as e:
    print(f"  Invalid JSON: {e}")

print()  # Empty line


# ============================================================================
# 4. UPDATING JSON FILE
# ============================================================================
print("=" * 60)
print("4. UPDATING JSON FILE")
print("=" * 60)

# Read existing data
with open('data.json', 'r') as f:
    data = json.load(f)

# Update data
data['age'] = 31
data['hobbies'].append('traveling')

# Write back
with open('data.json', 'w') as f:
    json.dump(data, f)

print("  Data updated in file")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("JSON FILES SUMMARY:")
print("=" * 60)
print("  - json.dump(): Write Python object to JSON file")
print("  - json.load(): Read JSON file to Python object")
print("  - Always use context managers (with statement)")
print("  - Handle FileNotFoundError and JSONDecodeError")
print("=" * 60)

