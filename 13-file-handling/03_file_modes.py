"""
File Modes in Python

This file demonstrates different file modes for opening files.
Understanding file modes is crucial for proper file operations.
"""

# ============================================================================
# 1. READ MODE ('r')
# ============================================================================
print("=" * 60)
print("1. READ MODE ('r')")
print("=" * 60)

# Create a file first
filename = "test.txt"
with open(filename, "w") as f:
    f.write("Hello, World!\n")

# Read mode (default for text files)
with open(filename, "r") as file:
    content = file.read()
    print(f"  Read content: {content.strip()}")

print("\n  'r' mode:")
print("    - Opens file for reading")
print("    - File must exist")
print("    - Default mode for text files")

print()  # Empty line


# ============================================================================
# 2. WRITE MODE ('w')
# ============================================================================
print("=" * 60)
print("2. WRITE MODE ('w')")
print("=" * 60)

# Write mode (overwrites existing file)
with open("write_test.txt", "w") as file:
    file.write("This overwrites the file.\n")
    file.write("Previous content is lost.\n")

print("  Written with 'w' mode")

# Read to verify
with open("write_test.txt", "r") as file:
    print("  Content:")
    for line in file:
        print(f"    {line.strip()}")

print("\n  'w' mode:")
print("    - Opens file for writing")
print("    - Creates file if doesn't exist")
print("    - Overwrites existing file")

print()  # Empty line


# ============================================================================
# 3. APPEND MODE ('a')
# ============================================================================
print("=" * 60)
print("3. APPEND MODE ('a')")
print("=" * 60)

# Append mode (adds to end)
with open("append_test.txt", "w") as file:
    file.write("First line.\n")

with open("append_test.txt", "a") as file:
    file.write("Second line (appended).\n")
    file.write("Third line (appended).\n")

print("  Appended to file")

# Read to verify
with open("append_test.txt", "r") as file:
    print("  Content:")
    for line in file:
        print(f"    {line.strip()}")

print("\n  'a' mode:")
print("    - Opens file for appending")
print("    - Creates file if doesn't exist")
print("    - Adds to end of file")

print()  # Empty line


# ============================================================================
# 4. EXCLUSIVE CREATION ('x')
# ============================================================================
print("=" * 60)
print("4. EXCLUSIVE CREATION ('x')")
print("=" * 60)

# Exclusive creation (fails if file exists)
try:
    with open("exclusive.txt", "x") as file:
        file.write("This file is created exclusively.\n")
    print("  File created with 'x' mode")
except FileExistsError:
    print("  File already exists (expected on second run)")

print("\n  'x' mode:")
print("    - Creates file exclusively")
print("    - Fails if file already exists")
print("    - Prevents accidental overwriting")

print()  # Empty line


# ============================================================================
# 5. BINARY MODES
# ============================================================================
print("=" * 60)
print("5. BINARY MODES")
print("=" * 60)

# Binary read mode
binary_data = b"Hello, Binary World!\n"
with open("binary_file.bin", "wb") as file:
    file.write(binary_data)

print("  Written binary data")

# Binary read mode
with open("binary_file.bin", "rb") as file:
    data = file.read()
    print(f"  Read binary data: {data}")

print("\n  Binary modes:")
print("    - 'rb' - Read binary")
print("    - 'wb' - Write binary")
print("    - 'ab' - Append binary")

print()  # Empty line


# ============================================================================
# 6. READ AND WRITE MODES ('r+', 'w+', 'a+')
# ============================================================================
print("=" * 60)
print("6. READ AND WRITE MODES ('r+', 'w+', 'a+')")
print("=" * 60)

# Read and write mode
with open("rw_test.txt", "w") as file:
    file.write("Line 1\nLine 2\nLine 3\n")

with open("rw_test.txt", "r+") as file:
    content = file.read()
    print(f"  Read: {content.strip()}")
    
    file.write("Line 4 (added)\n")
    file.seek(0)  # Go back to beginning
    new_content = file.read()
    print(f"  After write: {new_content.strip()}")

print("\n  Read+Write modes:")
print("    - 'r+' - Read and write (file must exist)")
print("    - 'w+' - Write and read (overwrites)")
print("    - 'a+' - Append and read")

print()  # Empty line


# ============================================================================
# 7. TEXT MODE ('t')
# ============================================================================
print("=" * 60)
print("7. TEXT MODE ('t')")
print("=" * 60)

# Text mode (default)
with open("text_test.txt", "wt") as file:
    file.write("Text mode file.\n")

with open("text_test.txt", "rt") as file:
    content = file.read()
    print(f"  Read: {content.strip()}")

print("\n  't' mode:")
print("    - Text mode (default)")
print("    - Handles newlines automatically")
print("    - Works with strings")

print()  # Empty line


# ============================================================================
# 8. MODE COMBINATIONS
# ============================================================================
print("=" * 60)
print("8. MODE COMBINATIONS")
print("=" * 60)

print("  Common mode combinations:")
print("    'r'  or 'rt'  - Read text (default)")
print("    'w'  or 'wt'  - Write text")
print("    'a'  or 'at'  - Append text")
print("    'rb'          - Read binary")
print("    'wb'          - Write binary")
print("    'ab'          - Append binary")
print("    'r+'          - Read and write")
print("    'w+'          - Write and read")
print("    'a+'          - Append and read")

print()  # Empty line


# ============================================================================
# 9. CHOOSING THE RIGHT MODE
# ============================================================================
print("=" * 60)
print("9. CHOOSING THE RIGHT MODE")
print("=" * 60)

print("  When to use each mode:")
print("    'r'  - Reading existing files")
print("    'w'  - Creating new file or overwriting")
print("    'a'  - Adding to end of file (logs, etc.)")
print("    'x'  - Creating file only if it doesn't exist")
print("    'rb' - Reading binary files (images, etc.)")
print("    'wb' - Writing binary files")
print("    'r+' - Reading and modifying existing file")

print()  # Empty line


# ============================================================================
# 10. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("10. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Log file (append mode)
with open("app.log", "a") as log:
    log.write("2024-01-15 10:00:00 - Application started\n")
    log.write("2024-01-15 10:01:00 - Processing data\n")

print("  Log file written (append mode)")

# Example 2: Configuration file (write mode)
with open("config.txt", "w") as config:
    config.write("host=localhost\n")
    config.write("port=8080\n")
    config.write("debug=True\n")

print("  Config file written (write mode)")

# Example 3: Read existing file
if os.path.exists("app.log"):
    with open("app.log", "r") as log:
        print("  Log file content:")
        for line in log:
            print(f"    {line.strip()}")

# Clean up
import os
for f in [filename, "write_test.txt", "append_test.txt", "exclusive.txt",
          "binary_file.bin", "rw_test.txt", "text_test.txt", 
          "app.log", "config.txt"]:
    if os.path.exists(f):
        os.remove(f)

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("FILE MODES SUMMARY:")
print("=" * 60)
print("Key Modes:")
print("  - 'r' - Read (file must exist)")
print("  - 'w' - Write (overwrites)")
print("  - 'a' - Append (adds to end)")
print("  - 'x' - Exclusive creation")
print("  - 'b' - Binary mode")
print("  - 't' - Text mode (default)")
print("  - '+' - Read and write")
print("\nRemember:")
print("  - Choose mode based on operation")
print("  - 'w' overwrites, 'a' appends")
print("  - Use 'b' for binary files")
print("  - Default is text mode")
print("=" * 60)

