"""
Nested Context Managers

This file demonstrates working with multiple context managers.
"""

# ============================================================================
# 1. NESTED CONTEXT MANAGERS
# ============================================================================
print("=" * 60)
print("1. NESTED CONTEXT MANAGERS")
print("=" * 60)

# Create input file
with open('input.txt', 'w') as f:
    f.write("Hello, World!")

# Nested context managers
with open('input.txt', 'r') as infile:
    with open('output.txt', 'w') as outfile:
        data = infile.read()
        outfile.write(data.upper())

print("  Data processed with nested contexts")

print()  # Empty line


# ============================================================================
# 2. MULTIPLE CONTEXTS WITH COMMAS
# ============================================================================
print("=" * 60)
print("2. MULTIPLE CONTEXTS WITH COMMAS")
print("=" * 60)

with open('input.txt', 'r') as infile, open('output2.txt', 'w') as outfile:
    data = infile.read()
    outfile.write(data.lower())

print("  Data processed using comma syntax")

print()  # Empty line


# ============================================================================
# 3. THREE OR MORE CONTEXTS
# ============================================================================
print("=" * 60)
print("3. THREE OR MORE CONTEXTS")
print("=" * 60)

with open('file1.txt', 'w') as f1, open('file2.txt', 'w') as f2, open('file3.txt', 'w') as f3:
    f1.write("File 1")
    f2.write("File 2")
    f3.write("File 3")

print("  Multiple files created simultaneously")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("NESTED CONTEXTS SUMMARY:")
print("=" * 60)
print("  - Can nest context managers")
print("  - Can use comma syntax for multiple contexts")
print("  - All contexts are properly managed")
print("  - Cleanup happens in reverse order")
print("=" * 60)

