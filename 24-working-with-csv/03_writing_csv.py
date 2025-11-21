"""
Writing CSV Files

This file demonstrates different ways to write CSV files.
"""

import csv

# ============================================================================
# 1. BASIC WRITING
# ============================================================================
print("=" * 60)
print("1. BASIC WRITING")
print("=" * 60)

data = [
    ['name', 'age', 'city'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'London']
]

with open('output1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("  File written: output1.csv")
print("  Note: Always use newline='' when writing CSV files")

print()  # Empty line


# ============================================================================
# 2. WRITING ROW BY ROW
# ============================================================================
print("=" * 60)
print("2. WRITING ROW BY ROW")
print("=" * 60)

with open('output2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'city'])
    writer.writerow(['Alice', '30', 'New York'])
    writer.writerow(['Bob', '25', 'London'])

print("  File written row by row: output2.csv")

print()  # Empty line


# ============================================================================
# 3. APPENDING TO CSV
# ============================================================================
print("=" * 60)
print("3. APPENDING TO CSV")
print("=" * 60)

# First, create file with header
with open('output3.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'city'])

# Append data
with open('output3.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Charlie', '35', 'Paris'])
    writer.writerow(['Diana', '28', 'Berlin'])

print("  File created and appended to: output3.csv")

print()  # Empty line


# ============================================================================
# 4. WRITING WITH QUOTING
# ============================================================================
print("=" * 60)
print("4. WRITING WITH QUOTING")
print("=" * 60)

data = [
    ['name', 'description'],
    ['Alice', 'Likes "Python" programming'],
    ['Bob', 'Works in New York, NY']
]

with open('output4.csv', 'w', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerows(data)

print("  File written with quoting: output4.csv")

print()  # Empty line


# ============================================================================
# 5. CUSTOM DELIMITER
# ============================================================================
print("=" * 60)
print("5. CUSTOM DELIMITER")
print("=" * 60)

data = [
    ['name', 'age', 'city'],
    ['Alice', '30', 'New York']
]

# Tab-separated values
with open('output.tsv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(data)

print("  Tab-separated file written: output.tsv")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("WRITING CSV SUMMARY:")
print("=" * 60)
print("  - csv.writer(): Write CSV row by row")
print("  - writer.writerow(): Write single row")
print("  - writer.writerows(): Write multiple rows")
print("  - Always use newline='' when opening for writing")
print("  - Can customize delimiter and quoting")
print("=" * 60)

