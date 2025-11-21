"""
File Operations in Python

This file demonstrates how to read from and write to files.
File I/O is essential for storing and retrieving data.
"""

# ============================================================================
# 1. WRITING TO A FILE
# ============================================================================
print("=" * 60)
print("1. WRITING TO A FILE")
print("=" * 60)

# Write to file using 'with' statement (recommended)
filename = "example.txt"

with open(filename, "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2.\n")
    file.write("This is line 3.\n")

print(f"  Written to {filename}")
print("  File is automatically closed when exiting 'with' block")

# Read it back to verify
with open(filename, "r") as file:
    content = file.read()
    print(f"\n  Content of {filename}:")
    print("  " + content.replace("\n", "\n  "))

print()  # Empty line


# ============================================================================
# 2. FILE MODES
# ============================================================================
print("=" * 60)
print("2. FILE MODES")
print("=" * 60)

print("Common file modes:")
print("  'r'  - Read (default, file must exist)")
print("  'w'  - Write (overwrites existing file)")
print("  'a'  - Append (adds to end of file)")
print("  'x'  - Exclusive creation (fails if file exists)")
print("  'b'  - Binary mode (e.g., 'rb', 'wb')")
print("  't'  - Text mode (default)")
print("  '+'  - Read and write (e.g., 'r+', 'w+')")

print()  # Empty line


# ============================================================================
# 3. READING FROM A FILE
# ============================================================================
print("=" * 60)
print("3. READING FROM A FILE")
print("=" * 60)

# Read entire file
with open(filename, "r") as file:
    content = file.read()
    print("  Entire file content:")
    print("  " + repr(content))

# Read line by line
print("\n  Line by line:")
with open(filename, "r") as file:
    for line in file:
        print(f"    {line.strip()}")  # strip() removes newline

print()  # Empty line


# ============================================================================
# 4. READING ALL LINES
# ============================================================================
print("=" * 60)
print("4. READING ALL LINES")
print("=" * 60)

# readlines() returns a list of lines
with open(filename, "r") as file:
    lines = file.readlines()
    print(f"  Total lines: {len(lines)}")
    for i, line in enumerate(lines, 1):
        print(f"    Line {i}: {line.strip()}")

print()  # Empty line


# ============================================================================
# 5. APPENDING TO A FILE
# ============================================================================
print("=" * 60)
print("5. APPENDING TO A FILE")
print("=" * 60)

# Append mode adds to end of file
with open(filename, "a") as file:
    file.write("This is appended line.\n")
    file.write("Another appended line.\n")

print(f"  Appended to {filename}")

# Read to see appended content
with open(filename, "r") as file:
    print("\n  Updated content:")
    for line in file:
        print(f"    {line.strip()}")

print()  # Empty line


# ============================================================================
# 6. THE 'WITH' STATEMENT (BEST PRACTICE)
# ============================================================================
print("=" * 60)
print("6. THE 'WITH' STATEMENT (BEST PRACTICE)")
print("=" * 60)

# ✅ Good: Using 'with' (automatically closes file)
print("  ✅ Good: Using 'with' statement")
with open(filename, "r") as file:
    content = file.read()
# File is automatically closed here

# ❌ Less preferred: Manual file closing
print("\n  ⚠️  Less preferred: Manual closing")
file = open(filename, "r")
content = file.read()
file.close()  # Must remember to close!

print("\n  Advantages of 'with' statement:")
print("    - Automatically closes file")
print("    - Handles errors gracefully")
print("    - More Pythonic")
print("    - Prevents resource leaks")

print()  # Empty line


# ============================================================================
# 7. HANDLING FILE ERRORS
# ============================================================================
print("=" * 60)
print("7. HANDLING FILE ERRORS")
print("=" * 60)

# FileNotFoundError when file doesn't exist
# try:
#     with open("nonexistent.txt", "r") as file:
#         content = file.read()
# except FileNotFoundError:
#     print("  File not found! Creating it...")
#     with open("nonexistent.txt", "w") as file:
#         file.write("New file created!\n")

# # PermissionError when no permission
# try:
#     with open("/root/restricted.txt", "w") as file:
#         file.write("test")
# except PermissionError:
#     print("  Permission denied!")

# print("\n  Always handle file errors in production code")

print()  # Empty line


# ============================================================================
# 8. READING LINE BY LINE (MEMORY EFFICIENT)
# ============================================================================
print("=" * 60)
print("8. READING LINE BY LINE (MEMORY EFFICIENT)")
print("=" * 60)

# For large files, read line by line instead of entire file
print("  Reading line by line (memory efficient):")
with open(filename, "r") as file:
    line_count = 0
    for line in file:
        line_count += 1
        print(f"    Line {line_count}: {line.strip()}")

print("\n  This is better for large files - doesn't load entire file into memory")

print()  # Empty line


# ============================================================================
# 9. WRITING MULTIPLE LINES
# ============================================================================
print("=" * 60)
print("9. WRITING MULTIPLE LINES")
print("=" * 60)

# Write multiple lines at once
data = [
    "Line 1",
    "Line 2",
    "Line 3",
    "Line 4"
]

output_file = "multi_line.txt"
with open(output_file, "w") as file:
    for line in data:
        file.write(line + "\n")

print(f"  Wrote {len(data)} lines to {output_file}")

# Or use writelines() with newlines
with open(output_file, "w") as file:
    file.writelines([line + "\n" for line in data])

print(f"  Updated {output_file} using writelines()")

print()  # Empty line


# ============================================================================
# 10. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("10. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Save user data
print("  Example 1: Save user data")
user_data = {
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com"
}

data_file = "user_data.txt"
with open(data_file, "w") as file:
    for key, value in user_data.items():
        file.write(f"{key}: {value}\n")

print(f"    Saved user data to {data_file}")

# Example 2: Read configuration
print("\n  Example 2: Read configuration")
config_file = "config.txt"
with open(config_file, "w") as file:
    file.write("host=localhost\n")
    file.write("port=8080\n")
    file.write("debug=True\n")

config = {}
with open(config_file, "r") as file:
    for line in file:
        if "=" in line:
            key, value = line.strip().split("=", 1)
            config[key] = value

print(f"    Config: {config}")

# Example 3: Log file
print("\n  Example 3: Log file")
log_file = "app.log"
with open(log_file, "a") as file:
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"[{timestamp}] Application started\n")
    file.write(f"[{timestamp}] User logged in\n")

print(f"    Logged to {log_file}")

print()  # Empty line


# ============================================================================
# 11. CLEANUP - REMOVE TEST FILES
# ============================================================================
print("=" * 60)
print("11. CLEANUP")
print("=" * 60)

import os

# Remove test files (optional - comment out if you want to keep them)
test_files = [filename, output_file, data_file, config_file, log_file]
print("  Test files created:")
for file in test_files:
    if os.path.exists(file):
        print(f"    - {file}")
        # Uncomment to delete:
        # os.remove(file)

print("\n  Note: Files are kept for inspection")
print("  Uncomment os.remove() to clean up")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("FILE OPERATIONS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Use 'with' statement for file operations (auto-closes)")
print("  - 'r' mode: Read (file must exist)")
print("  - 'w' mode: Write (overwrites existing file)")
print("  - 'a' mode: Append (adds to end)")
print("  - file.read() - Read entire file")
print("  - file.readline() - Read one line")
print("  - file.readlines() - Read all lines as list")
print("  - file.write() - Write string to file")
print("  - Always handle FileNotFoundError")
print("  - Read line by line for large files")
print("=" * 60)

