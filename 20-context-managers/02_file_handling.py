"""
File Handling with Context Managers

This file demonstrates using context managers for file operations.
"""

# ============================================================================
# 1. READING FILES
# ============================================================================
print("=" * 60)
print("1. READING FILES")
print("=" * 60)

# Create sample file
with open('sample.txt', 'w') as f:
    f.write("Line 1\nLine 2\nLine 3\n")

# Read file
with open('sample.txt', 'r') as f:
    content = f.read()
    print(f"  Content:\n{content}")

print()  # Empty line


# ============================================================================
# 2. WRITING FILES
# ============================================================================
print("=" * 60)
print("2. WRITING FILES")
print("=" * 60)

with open('output.txt', 'w') as f:
    f.write("Hello, World!\n")
    f.write("This is a test file.\n")

print("  File written successfully")

# Verify
with open('output.txt', 'r') as f:
    print(f"  Content: {f.read()}")

print()  # Empty line


# ============================================================================
# 3. READING LINE BY LINE
# ============================================================================
print("=" * 60)
print("3. READING LINE BY LINE")
print("=" * 60)

with open('sample.txt', 'r') as f:
    print("  Lines:")
    for i, line in enumerate(f, 1):
        print(f"    {i}: {line.strip()}")

print()  # Empty line


# ============================================================================
# 4. MULTIPLE FILES
# ============================================================================
print("=" * 60)
print("4. MULTIPLE FILES")
print("=" * 60)

# Nested context managers
with open('input.txt', 'w') as infile:
    infile.write("Input data")

with open('input.txt', 'r') as infile:
    with open('output.txt', 'w') as outfile:
        data = infile.read()
        outfile.write(data.upper())

print("  Data copied and transformed")

print()  # Empty line


# ============================================================================
# 5. MULTIPLE FILES WITH COMMAS
# ============================================================================
print("=" * 60)
print("5. MULTIPLE FILES WITH COMMAS")
print("=" * 60)

with open('input.txt', 'r') as infile, open('output2.txt', 'w') as outfile:
    data = infile.read()
    outfile.write(data.lower())

print("  Data copied using comma syntax")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("FILE HANDLING SUMMARY:")
print("=" * 60)
print("  - Always use 'with' for file operations")
print("  - Files are automatically closed")
print("  - Can nest multiple context managers")
print("  - Can use comma syntax for multiple files")
print("=" * 60)

