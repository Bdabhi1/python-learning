"""
Error Handling in File Operations

This file demonstrates how to handle errors when working with files.
Proper error handling makes file operations robust and reliable.
"""

# ============================================================================
# 1. FILE NOT FOUND ERROR
# ============================================================================
print("=" * 60)
print("1. FILE NOT FOUND ERROR")
print("=" * 60)

# Handle FileNotFoundError
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("  FileNotFoundError: File does not exist!")

print("\n  Always handle FileNotFoundError when reading files")

print()  # Empty line


# ============================================================================
# 2. PERMISSION ERROR
# ============================================================================
print("=" * 60)
print("2. PERMISSION ERROR")
print("=" * 60)

# Handle PermissionError
try:
    # This might fail on some systems
    with open("/root/protected.txt", "w") as file:
        file.write("Hello")
except PermissionError:
    print("  PermissionError: Permission denied!")
except FileNotFoundError:
    print("  FileNotFoundError: Directory does not exist!")

print("\n  Handle PermissionError for protected files/directories")

print()  # Empty line


# ============================================================================
# 3. MULTIPLE EXCEPTIONS
# ============================================================================
print("=" * 60)
print("3. MULTIPLE EXCEPTIONS")
print("=" * 60)

# Handle multiple exceptions
try:
    with open("test_file.txt", "r") as file:
        content = file.read()
        # Simulate other potential errors
        result = int(content)  # Might raise ValueError
except FileNotFoundError:
    print("  FileNotFoundError: File not found!")
except ValueError:
    print("  ValueError: Cannot convert to integer!")
except Exception as e:
    print(f"  Other error: {e}")

print("\n  Handle specific exceptions, then general Exception")

print()  # Empty line


# ============================================================================
# 4. CHECKING BEFORE OPERATIONS
# ============================================================================
print("=" * 60)
print("4. CHECKING BEFORE OPERATIONS")
print("=" * 60)

import os

# Check before reading
filename = "data.txt"
if os.path.exists(filename):
    with open(filename, "r") as file:
        content = file.read()
        print(f"  Read {len(content)} characters")
else:
    print(f"  File '{filename}' does not exist")

print("\n  Check file existence before operations")

print()  # Empty line


# ============================================================================
# 5. SAFE FILE WRITING
# ============================================================================
print("=" * 60)
print("5. SAFE FILE WRITING")
print("=" * 60)

# Safe file writing with error handling
def safe_write(filename, content):
    """Safely write to file."""
    try:
        with open(filename, "w") as file:
            file.write(content)
        return True
    except PermissionError:
        print(f"  Permission denied: {filename}")
        return False
    except Exception as e:
        print(f"  Error writing {filename}: {e}")
        return False

result = safe_write("safe_test.txt", "Hello, World!")
print(f"  Write successful: {result}")

# Clean up
if os.path.exists("safe_test.txt"):
    os.remove("safe_test.txt")

print()  # Empty line


# ============================================================================
# 6. SAFE FILE READING
# ============================================================================
print("=" * 60)
print("6. SAFE FILE READING")
print("=" * 60)

# Safe file reading
def safe_read(filename):
    """Safely read from file."""
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"  File not found: {filename}")
        return None
    except PermissionError:
        print(f"  Permission denied: {filename}")
        return None
    except Exception as e:
        print(f"  Error reading {filename}: {e}")
        return None

# Test with non-existent file
content = safe_read("nonexistent.txt")
print(f"  Content: {content}")

print()  # Empty line


# ============================================================================
# 7. HANDLING ENCODING ERRORS
# ============================================================================
print("=" * 60)
print("7. HANDLING ENCODING ERRORS")
print("=" * 60)

# Handle encoding errors
try:
    with open("test_encoding.txt", "w", encoding="utf-8") as file:
        file.write("Hello, World! 🌍\n")
    
    # Try reading with wrong encoding
    with open("test_encoding.txt", "r", encoding="ascii") as file:
        content = file.read()
except UnicodeDecodeError:
    print("  UnicodeDecodeError: Cannot decode with ASCII")
    # Read with correct encoding
    with open("test_encoding.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(f"  Read with UTF-8: {content.strip()}")

# Clean up
if os.path.exists("test_encoding.txt"):
    os.remove("test_encoding.txt")

print()  # Empty line


# ============================================================================
# 8. TRY-EXCEPT-FINALLY
# ============================================================================
print("=" * 60)
print("8. TRY-EXCEPT-FINALLY")
print("=" * 60)

# Using finally for cleanup
file_handle = None
try:
    file_handle = open("finally_test.txt", "w")
    file_handle.write("Test content\n")
except Exception as e:
    print(f"  Error: {e}")
finally:
    if file_handle:
        file_handle.close()
        print("  File closed in finally block")

# Better: use 'with' statement (automatic cleanup)
try:
    with open("finally_test2.txt", "w") as file:
        file.write("Test content\n")
except Exception as e:
    print(f"  Error: {e}")
# File automatically closed here

# Clean up
for f in ["finally_test.txt", "finally_test2.txt"]:
    if os.path.exists(f):
        os.remove(f)

print()  # Empty line


# ============================================================================
# 9. CUSTOM ERROR MESSAGES
# ============================================================================
print("=" * 60)
print("9. CUSTOM ERROR MESSAGES")
print("=" * 60)

# Provide helpful error messages
filename = "important_data.txt"
try:
    with open(filename, "r") as file:
        content = file.read()
except FileNotFoundError:
    print(f"  Error: Cannot find file '{filename}'")
    print("  Please ensure the file exists in the current directory.")
    print(f"  Current directory: {os.getcwd()}")
except PermissionError:
    print(f"  Error: Permission denied for '{filename}'")
    print("  Please check file permissions.")
except Exception as e:
    print(f"  Unexpected error: {e}")
    print("  Please contact support.")

print()  # Empty line


# ============================================================================
# 10. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("10. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Robust file reader
def read_file_safe(filename):
    """Read file with comprehensive error handling."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except PermissionError:
        return f"Error: Permission denied for '{filename}'"
    except UnicodeDecodeError:
        return f"Error: Cannot decode '{filename}' as UTF-8"
    except Exception as e:
        return f"Error: {type(e).__name__}: {e}"

result = read_file_safe("nonexistent.txt")
print(f"  Result: {result}")

# Example 2: Safe file writer
def write_file_safe(filename, content):
    """Write file with error handling."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        return True, "Success"
    except PermissionError:
        return False, "Permission denied"
    except Exception as e:
        return False, str(e)

success, message = write_file_safe("test_safe.txt", "Hello")
print(f"  Write result: {success}, Message: {message}")

# Clean up
if os.path.exists("test_safe.txt"):
    os.remove("test_safe.txt")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("ERROR HANDLING SUMMARY:")
print("=" * 60)
print("Key Exceptions:")
print("  - FileNotFoundError: File doesn't exist")
print("  - PermissionError: Access denied")
print("  - UnicodeDecodeError: Encoding issues")
print("  - IOError: General I/O errors")
print("\nBest Practices:")
print("  - Always use try-except for file operations")
print("  - Handle specific exceptions first")
print("  - Use 'with' statement for automatic cleanup")
print("  - Check file existence when appropriate")
print("  - Provide helpful error messages")
print("  - Specify encoding for text files")
print("=" * 60)

