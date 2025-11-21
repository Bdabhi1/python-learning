"""
CSV Basics in Python

This file demonstrates the fundamental concepts of CSV and the csv module.
"""

import csv

# ============================================================================
# 1. WHAT IS CSV?
# ============================================================================
print("=" * 60)
print("1. WHAT IS CSV?")
print("=" * 60)

print("  CSV (Comma-Separated Values) is:")
print("    - A simple text format for tabular data")
print("    - Each line is a row")
print("    - Values separated by commas (or other delimiters)")
print("    - First row often contains column names (headers)")
print("    - Widely used in spreadsheets and data analysis")
print("  ")
print("  Example CSV:")
print("    name,age,city")
print("    Alice,30,New York")
print("    Bob,25,London")

print()  # Empty line


# ============================================================================
# 2. THE csv MODULE
# ============================================================================
print("=" * 60)
print("2. THE csv MODULE")
print("=" * 60)

print("  Main functions:")
print("    - csv.reader(): Read CSV file row by row")
print("    - csv.writer(): Write CSV file row by row")
print("    - csv.DictReader(): Read CSV as dictionary")
print("    - csv.DictWriter(): Write CSV from dictionary")

print()  # Empty line


# ============================================================================
# 3. CREATING SAMPLE CSV
# ============================================================================
print("=" * 60)
print("3. CREATING SAMPLE CSV")
print("=" * 60)

# Create sample CSV file
data = [
    ['name', 'age', 'city'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'London'],
    ['Charlie', '35', 'Paris']
]

with open('sample.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("  Sample CSV file created: sample.csv")

print()  # Empty line


# ============================================================================
# 4. READING CSV BASICS
# ============================================================================
print("=" * 60)
print("4. READING CSV BASICS")
print("=" * 60)

with open('sample.csv', 'r') as f:
    reader = csv.reader(f)
    print("  CSV content:")
    for row in reader:
        print(f"    {row}")

print()  # Empty line


# ============================================================================
# 5. CSV STRUCTURE
# ============================================================================
print("=" * 60)
print("5. CSV STRUCTURE")
print("=" * 60)

print("  CSV file structure:")
print("    - Header row: Column names")
print("    - Data rows: Actual data")
print("    - Delimiter: Comma (,) by default")
print("    - Quote character: Double quotes (\") for values with commas")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("CSV BASICS SUMMARY:")
print("=" * 60)
print("  - CSV is a simple format for tabular data")
print("  - csv module provides reader and writer functions")
print("  - Each row is a list of values")
print("  - First row often contains headers")
print("  - Use newline='' when writing CSV files")
print("=" * 60)

