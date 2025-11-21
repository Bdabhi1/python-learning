"""
CSV Dialects and Custom Formats

This file demonstrates working with different CSV formats and dialects.
"""

import csv

# ============================================================================
# 1. CUSTOM DELIMITER
# ============================================================================
print("=" * 60)
print("1. CUSTOM DELIMITER")
print("=" * 60)

# Tab-separated values
data = [
    ['name', 'age', 'city'],
    ['Alice', '30', 'New York']
]

# Write TSV
with open('data.tsv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(data)

# Read TSV
with open('data.tsv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        print(f"  {row}")

print()  # Empty line


# ============================================================================
# 2. CUSTOM QUOTE CHARACTER
# ============================================================================
print("=" * 60)
print("2. CUSTOM QUOTE CHARACTER")
print("=" * 60)

data = [
    ['name', 'description'],
    ['Alice', 'Likes "Python" programming']
]

with open('data_quoted.csv', 'w', newline='') as f:
    writer = csv.writer(f, quotechar="'", quoting=csv.QUOTE_ALL)
    writer.writerows(data)

print("  File written with custom quote character")

print()  # Empty line


# ============================================================================
# 3. QUOTING OPTIONS
# ============================================================================
print("=" * 60)
print("3. QUOTING OPTIONS")
print("=" * 60)

data = [
    ['name', 'value'],
    ['Alice', '30'],
    ['Bob', '25,000']  # Contains comma
]

# QUOTE_MINIMAL (default)
with open('quote_minimal.csv', 'w', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerows(data)

# QUOTE_ALL
with open('quote_all.csv', 'w', newline='') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerows(data)

print("  Files written with different quoting options")

print()  # Empty line


# ============================================================================
# 4. BUILT-IN DIALECTS
# ============================================================================
print("=" * 60)
print("4. BUILT-IN DIALECTS")
print("=" * 60)

print("  Available dialects:")
print("    - excel: Excel CSV format (default)")
print("    - excel-tab: Excel tab-delimited")
print("    - unix: Unix-style CSV")

# Using Excel dialect
data = [['name', 'age'], ['Alice', '30']]
with open('excel_format.csv', 'w', newline='') as f:
    writer = csv.writer(f, dialect='excel')
    writer.writerows(data)

print("  File written using Excel dialect")

print()  # Empty line


# ============================================================================
# 5. REGISTERING CUSTOM DIALECT
# ============================================================================
print("=" * 60)
print("5. REGISTERING CUSTOM DIALECT")
print("=" * 60)

# Register custom dialect
csv.register_dialect('pipes', delimiter='|', quoting=csv.QUOTE_MINIMAL)

data = [['name', 'age'], ['Alice', '30']]
with open('pipes.csv', 'w', newline='') as f:
    writer = csv.writer(f, dialect='pipes')
    writer.writerows(data)

print("  Custom dialect 'pipes' registered and used")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("CSV DIALECTS SUMMARY:")
print("=" * 60)
print("  - delimiter: Character separating values (default: ',')")
print("  - quotechar: Character for quoting (default: '\"')")
print("  - quoting: When to quote (QUOTE_MINIMAL, QUOTE_ALL, etc.)")
print("  - Built-in dialects: excel, excel-tab, unix")
print("  - Can register custom dialects")
print("=" * 60)

