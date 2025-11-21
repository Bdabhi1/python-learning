"""
Using DictReader and DictWriter

This file demonstrates reading and writing CSV files using dictionaries.
"""

import csv

# ============================================================================
# 1. DictReader - READING AS DICTIONARIES
# ============================================================================
print("=" * 60)
print("1. DictReader - READING AS DICTIONARIES")
print("=" * 60)

with open('sample.csv', 'r') as f:
    reader = csv.DictReader(f)
    print("  Reading as dictionaries:")
    for row in reader:
        print(f"    {row}")
        print(f"      Name: {row['name']}, Age: {row['age']}, City: {row['city']}")

print()  # Empty line


# ============================================================================
# 2. DictReader - ACCESSING HEADERS
# ============================================================================
print("=" * 60)
print("2. DictReader - ACCESSING HEADERS")
print("=" * 60)

with open('sample.csv', 'r') as f:
    reader = csv.DictReader(f)
    headers = reader.fieldnames
    print(f"  Headers: {headers}")
    
    for row in reader:
        print(f"    {row['name']} is {row['age']} years old")

print()  # Empty line


# ============================================================================
# 3. DictWriter - WRITING FROM DICTIONARIES
# ============================================================================
print("=" * 60)
print("3. DictWriter - WRITING FROM DICTIONARIES")
print("=" * 60)

data = [
    {'name': 'Alice', 'age': '30', 'city': 'New York'},
    {'name': 'Bob', 'age': '25', 'city': 'London'},
    {'name': 'Charlie', 'age': '35', 'city': 'Paris'}
]

with open('output_dict.csv', 'w', newline='') as f:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print("  File written using DictWriter: output_dict.csv")

print()  # Empty line


# ============================================================================
# 4. DictWriter - WRITING SINGLE ROW
# ============================================================================
print("=" * 60)
print("4. DictWriter - WRITING SINGLE ROW")
print("=" * 60)

with open('output_dict2.csv', 'w', newline='') as f:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'Diana', 'age': '28', 'city': 'Berlin'})

print("  Single row written: output_dict2.csv")

print()  # Empty line


# ============================================================================
# 5. ADVANTAGES OF DictReader/DictWriter
# ============================================================================
print("=" * 60)
print("5. ADVANTAGES OF DictReader/DictWriter")
print("=" * 60)

print("  DictReader advantages:")
print("    - Access columns by name (not index)")
print("    - More readable code")
print("    - Less error-prone")
print("  ")
print("  DictWriter advantages:")
print("    - Write from dictionary objects")
print("    - Automatic header writing")
print("    - Column order doesn't matter")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("DICT READER/WRITER SUMMARY:")
print("=" * 60)
print("  - csv.DictReader(): Read CSV as dictionaries")
print("  - csv.DictWriter(): Write CSV from dictionaries")
print("  - Access columns by name (more readable)")
print("  - writer.writeheader(): Write header row")
print("  - reader.fieldnames: Get column names")
print("=" * 60)

