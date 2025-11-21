"""
Writing Files in Python

This file demonstrates different ways to write data to files.
Writing files allows your programs to save data persistently.
"""

# ============================================================================
# 1. WRITING TO A FILE
# ============================================================================
print("=" * 60)
print("1. WRITING TO A FILE")
print("=" * 60)

filename = "output.txt"

# Write to file (creates or overwrites)
with open(filename, "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2.\n")
    file.write("This is line 3.\n")

print(f"  Written to {filename}")

# Read it back to verify
with open(filename, "r") as file:
    content = file.read()
    print("  Content:")
    print("  " + content.replace("\n", "\n  "))

print()  # Empty line


# ============================================================================
# 2. APPENDING TO A FILE
# ============================================================================
print("=" * 60)
print("2. APPENDING TO A FILE")
print("=" * 60)

# Append to existing file
with open(filename, "a") as file:
    file.write("This line is appended.\n")
    file.write("Another appended line.\n")

print("  Appended to file")

# Read to verify
with open(filename, "r") as file:
    lines = file.readlines()
    print(f"  Total lines: {len(lines)}")

print()  # Empty line


# ============================================================================
# 3. WRITING MULTIPLE LINES
# ============================================================================
print("=" * 60)
print("3. WRITING MULTIPLE LINES")
print("=" * 60)

# Write list of lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("multiple.txt", "w") as file:
    file.writelines(lines)

print("  Written multiple lines using writelines()")

# Read back
with open("multiple.txt", "r") as file:
    content = file.read()
    print("  Content:")
    print("  " + content.replace("\n", "\n  "))

print()  # Empty line


# ============================================================================
# 4. WRITING WITH FORMATTING
# ============================================================================
print("=" * 60)
print("4. WRITING WITH FORMATTING")
print("=" * 60)

# Write formatted data
with open("formatted.txt", "w") as file:
    name = "Alice"
    age = 25
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Next year: {age + 1}\n")

print("  Written formatted data")

# Read back
with open("formatted.txt", "r") as file:
    print("  Content:")
    for line in file:
        print(f"    {line.strip()}")

print()  # Empty line


# ============================================================================
# 5. WRITING WITH ENCODING
# ============================================================================
print("=" * 60)
print("5. WRITING WITH ENCODING")
print("=" * 60)

# Specify encoding
with open("encoded.txt", "w", encoding="utf-8") as file:
    file.write("Hello, World! 🌍\n")
    file.write("Special characters: café, résumé\n")

print("  Written with UTF-8 encoding")

# Read back
with open("encoded.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(f"  Content: {content.strip()}")

print()  # Empty line


# ============================================================================
# 6. WRITING BINARY DATA
# ============================================================================
print("=" * 60)
print("6. WRITING BINARY DATA")
print("=" * 60)

# Write binary data
binary_data = b"Hello, Binary World!\n"
with open("binary.bin", "wb") as file:
    file.write(binary_data)

print("  Written binary data")

# Read binary data
with open("binary.bin", "rb") as file:
    data = file.read()
    print(f"  Read: {data}")

print()  # Empty line


# ============================================================================
# 7. WRITING STRUCTURED DATA
# ============================================================================
print("=" * 60)
print("7. WRITING STRUCTURED DATA")
print("=" * 60)

# Write structured data (CSV-like)
data = [
    ("Alice", 25, "Engineer"),
    ("Bob", 30, "Doctor"),
    ("Charlie", 28, "Teacher")
]

with open("data.txt", "w") as file:
    file.write("Name,Age,Job\n")
    for name, age, job in data:
        file.write(f"{name},{age},{job}\n")

print("  Written structured data")

# Read back
with open("data.txt", "r") as file:
    print("  Content:")
    for line in file:
        print(f"    {line.strip()}")

print()  # Empty line


# ============================================================================
# 8. WRITING JSON DATA
# ============================================================================
print("=" * 60)
print("8. WRITING JSON DATA")
print("=" * 60)

import json

# Write JSON data
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "coding", "traveling"]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=2)

print("  Written JSON data")

# Read back
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(f"  Loaded: {loaded_data}")

print()  # Empty line


# ============================================================================
# 9. WRITING WITH ERROR HANDLING
# ============================================================================
print("=" * 60)
print("9. WRITING WITH ERROR HANDLING")
print("=" * 60)

# Handle write errors
try:
    with open("protected.txt", "w") as file:
        file.write("Hello\n")
    print("  Written successfully")
except PermissionError:
    print("  Permission denied!")
except Exception as e:
    print(f"  Error: {e}")

print()  # Empty line


# ============================================================================
# 10. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("10. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Write log file
import datetime
log_file = "app.log"
with open(log_file, "a") as file:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"[{timestamp}] Application started\n")
    file.write(f"[{timestamp}] Processing data\n")

print(f"  Written log entries to {log_file}")

# Example 2: Write configuration
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}

with open("config.txt", "w") as file:
    for key, value in config.items():
        file.write(f"{key}={value}\n")

print("  Written configuration file")

# Clean up
import os
for f in [filename, "multiple.txt", "formatted.txt", "encoded.txt", 
          "binary.bin", "data.txt", "data.json", log_file, "config.txt"]:
    if os.path.exists(f):
        os.remove(f)

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("WRITING FILES SUMMARY:")
print("=" * 60)
print("Key Methods:")
print("  - file.write(text) - Write string to file")
print("  - file.writelines(lines) - Write list of lines")
print("  - Use 'w' mode to overwrite")
print("  - Use 'a' mode to append")
print("  - Use 'wb' mode for binary data")
print("\nBest Practices:")
print("  - Use 'with' statement for automatic closing")
print("  - Specify encoding for text files")
print("  - Handle write errors")
print("  - Use appropriate file mode")
print("=" * 60)

