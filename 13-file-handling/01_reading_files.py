"""
Reading Files in Python

This file demonstrates different ways to read data from files.
Reading files is essential for loading data into your programs.
"""

# ============================================================================
# 1. READING ENTIRE FILE
# ============================================================================
print("=" * 60)
print("1. READING ENTIRE FILE")
print("=" * 60)

# Create a sample file first
filename = "sample.txt"
with open(filename, "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")

# Read entire file
with open(filename, "r") as file:
    content = file.read()
    print("  File content:")
    print(f"  {repr(content)}")

print("\n  file.read() reads entire file as string")

print()  # Empty line


# ============================================================================
# 2. READING LINE BY LINE
# ============================================================================
print("=" * 60)
print("2. READING LINE BY LINE")
print("=" * 60)

# Read line by line (memory efficient)
print("  Reading line by line:")
with open(filename, "r") as file:
    for i, line in enumerate(file, 1):
        print(f"    Line {i}: {line.strip()}")

print("\n  Iterating over file object reads line by line")

print()  # Empty line


# ============================================================================
# 3. READLINE() METHOD
# ============================================================================
print("=" * 60)
print("3. READLINE() METHOD")
print("=" * 60)

# Read single line
with open(filename, "r") as file:
    first_line = file.readline()
    second_line = file.readline()
    print(f"  First line: {repr(first_line)}")
    print(f"  Second line: {repr(second_line)}")

print("\n  readline() reads one line at a time")

print()  # Empty line


# ============================================================================
# 4. READLINES() METHOD
# ============================================================================
print("=" * 60)
print("4. READLINES() METHOD")
print("=" * 60)

# Read all lines into list
with open(filename, "r") as file:
    lines = file.readlines()
    print(f"  All lines: {lines}")
    print(f"  Number of lines: {len(lines)}")

print("\n  readlines() returns list of all lines")

print()  # Empty line


# ============================================================================
# 5. READING WITH SIZE LIMIT
# ============================================================================
print("=" * 60)
print("5. READING WITH SIZE LIMIT")
print("=" * 60)

# Read specific number of characters
with open(filename, "r") as file:
    chunk = file.read(10)  # Read first 10 characters
    print(f"  First 10 characters: {repr(chunk)}")
    
    chunk2 = file.read(10)  # Read next 10 characters
    print(f"  Next 10 characters: {repr(chunk2)}")

print("\n  read(size) reads specified number of characters")

print()  # Empty line


# ============================================================================
# 6. READING WITH ENCODING
# ============================================================================
print("=" * 60)
print("6. READING WITH ENCODING")
print("=" * 60)

# Specify encoding (important for text files)
with open(filename, "r", encoding="utf-8") as file:
    content = file.read()
    print(f"  Read with UTF-8 encoding: {len(content)} characters")

print("\n  Always specify encoding for text files")
print("  Default encoding varies by system")

print()  # Empty line


# ============================================================================
# 7. PROCESSING FILE CONTENT
# ============================================================================
print("=" * 60)
print("7. PROCESSING FILE CONTENT")
print("=" * 60)

# Process each line
with open(filename, "r") as file:
    for line in file:
        # Remove newline and process
        processed = line.strip().upper()
        print(f"  Processed: {processed}")

print("\n  Process lines as you read them")

print()  # Empty line


# ============================================================================
# 8. READING INTO DATA STRUCTURES
# ============================================================================
print("=" * 60)
print("8. READING INTO DATA STRUCTURES")
print("=" * 60)

# Read into list
with open(filename, "r") as file:
    lines = [line.strip() for line in file]
    print(f"  Lines as list: {lines}")

# Read into dictionary (if structured)
data = {}
with open(filename, "r") as file:
    for i, line in enumerate(file, 1):
        data[f"line_{i}"] = line.strip()
    print(f"  Lines as dict: {data}")

print()  # Empty line


# ============================================================================
# 9. CHECKING FILE BEFORE READING
# ============================================================================
print("=" * 60)
print("9. CHECKING FILE BEFORE READING")
print("=" * 60)

import os

# Check if file exists
if os.path.exists(filename):
    with open(filename, "r") as file:
        content = file.read()
        print(f"  File exists, read {len(content)} characters")
else:
    print("  File does not exist")

# Check file size
if os.path.exists(filename):
    size = os.path.getsize(filename)
    print(f"  File size: {size} bytes")

print()  # Empty line


# ============================================================================
# 10. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("10. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Count lines
with open(filename, "r") as file:
    line_count = sum(1 for line in file)
    print(f"  Total lines: {line_count}")

# Example 2: Find longest line
with open(filename, "r") as file:
    longest = max((line.strip() for line in file), key=len)
    print(f"  Longest line: {longest}")

# Example 3: Search for text
search_term = "Line"
with open(filename, "r") as file:
    matching_lines = [line.strip() for line in file if search_term in line]
    print(f"  Lines containing '{search_term}': {matching_lines}")

# Clean up
import os
if os.path.exists(filename):
    os.remove(filename)

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("READING FILES SUMMARY:")
print("=" * 60)
print("Key Methods:")
print("  - file.read() - Read entire file")
print("  - file.readline() - Read one line")
print("  - file.readlines() - Read all lines as list")
print("  - for line in file - Iterate line by line")
print("  - file.read(size) - Read specific number of characters")
print("\nBest Practices:")
print("  - Use 'with' statement for automatic closing")
print("  - Specify encoding for text files")
print("  - Check if file exists before reading")
print("  - Process lines as you read (memory efficient)")
print("=" * 60)

