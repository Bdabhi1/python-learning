"""
Practical CSV Examples

This file demonstrates real-world CSV use cases.
"""

import csv

# ============================================================================
# 1. PROCESSING CSV DATA
# ============================================================================
print("=" * 60)
print("1. PROCESSING CSV DATA")
print("=" * 60)

# Calculate average age
with open('sample.csv', 'r') as f:
    reader = csv.DictReader(f)
    ages = []
    for row in reader:
        ages.append(int(row['age']))
    
    if ages:
        avg_age = sum(ages) / len(ages)
        print(f"  Average age: {avg_age:.1f}")

print()  # Empty line


# ============================================================================
# 2. FILTERING CSV DATA
# ============================================================================
print("=" * 60)
print("2. FILTERING CSV DATA")
print("=" * 60)

# Filter by age
with open('sample.csv', 'r') as f:
    reader = csv.DictReader(f)
    print("  People over 30:")
    for row in reader:
        if int(row['age']) > 30:
            print(f"    {row['name']}: {row['age']} years old")

print()  # Empty line


# ============================================================================
# 3. CONVERTING CSV TO DICTIONARY
# ============================================================================
print("=" * 60)
print("3. CONVERTING CSV TO DICTIONARY")
print("=" * 60)

# Convert to list of dictionaries
with open('sample.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = list(reader)

print(f"  Loaded {len(data)} records")
for record in data:
    print(f"    {record}")

print()  # Empty line


# ============================================================================
# 4. MERGING CSV FILES
# ============================================================================
print("=" * 60)
print("4. MERGING CSV FILES")
print("=" * 60)

# Create second CSV
data2 = [
    ['name', 'age', 'city'],
    ['Diana', '28', 'Berlin'],
    ['Eve', '32', 'Tokyo']
]

with open('sample2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data2)

# Merge files
with open('merged.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    
    # Write header once
    with open('sample.csv', 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        writer.writerow(header)
        writer.writerows(reader)
    
    # Append data from second file
    with open('sample2.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        writer.writerows(reader)

print("  Files merged: merged.csv")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL EXAMPLES SUMMARY:")
print("=" * 60)
print("CSV is useful for:")
print("  - Data processing and analysis")
print("  - Filtering and transforming data")
print("  - Merging multiple data sources")
print("  - Exporting data from applications")
print("  - Importing data into spreadsheets")
print("=" * 60)

