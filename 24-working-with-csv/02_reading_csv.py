"""
Reading CSV Files

This file demonstrates different ways to read CSV files.
"""

import csv

# ============================================================================
# 1. BASIC READING
# ============================================================================
print("=" * 60)
print("1. BASIC READING")
print("=" * 60)

with open('sample.csv', 'r') as f:
    reader = csv.reader(f)
    print("  All rows:")
    for row in reader:
        print(f"    {row}")

print()  # Empty line


# ============================================================================
# 2. READING WITH HEADERS
# ============================================================================
print("=" * 60)
print("2. READING WITH HEADERS")
print("=" * 60)

with open('sample.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)  # Get header row
    print(f"  Headers: {headers}")
    print("  Data rows:")
    for row in reader:
        print(f"    {row}")

print()  # Empty line


# ============================================================================
# 3. READING ALL ROWS AT ONCE
# ============================================================================
print("=" * 60)
print("3. READING ALL ROWS AT ONCE")
print("=" * 60)

with open('sample.csv', 'r') as f:
    reader = csv.reader(f)
    rows = list(reader)
    print(f"  Total rows: {len(rows)}")
    print(f"  First row (headers): {rows[0]}")
    print(f"  Data rows: {rows[1:]}")

print()  # Empty line


# ============================================================================
# 4. PROCESSING ROWS
# ============================================================================
print("=" * 60)
print("4. PROCESSING ROWS")
print("=" * 60)

with open('sample.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    print(f"  Processing {len(headers)} columns: {headers}")
    for i, row in enumerate(reader, 1):
        print(f"    Row {i}: {row[0]} is {row[1]} years old, lives in {row[2]}")

print()  # Empty line


# ============================================================================
# 5. ACCESSING SPECIFIC COLUMNS
# ============================================================================
print("=" * 60)
print("5. ACCESSING SPECIFIC COLUMNS")
print("=" * 60)

with open('sample.csv', 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    name_index = headers.index('name')
    age_index = headers.index('age')
    
    print("  Names and ages:")
    for row in reader:
        print(f"    {row[name_index]}: {row[age_index]} years old")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("READING CSV SUMMARY:")
print("=" * 60)
print("  - csv.reader(): Read CSV row by row")
print("  - next(reader): Skip/get header row")
print("  - list(reader): Read all rows at once")
print("  - Each row is a list of values")
print("  - Access columns by index")
print("=" * 60)

