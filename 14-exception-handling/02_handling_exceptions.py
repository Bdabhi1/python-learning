"""
Handling Different Types of Exceptions

This file demonstrates how to handle various built-in exceptions
that commonly occur in Python programs.
"""

# ============================================================================
# 1. VALUEERROR
# ============================================================================
print("=" * 60)
print("1. VALUEERROR")
print("=" * 60)

# ValueError occurs when value is wrong type or format
try:
    number = int("abc")
except ValueError as e:
    print(f"  ValueError: {e}")

try:
    number = float("not a number")
except ValueError as e:
    print(f"  ValueError: {e}")

print("\n  ValueError: Invalid value for operation")

print()  # Empty line


# ============================================================================
# 2. TYPEERROR
# ============================================================================
print("=" * 60)
print("2. TYPEERROR")
print("=" * 60)

# TypeError occurs when operation on wrong type
try:
    result = "hello" + 5
except TypeError as e:
    print(f"  TypeError: {e}")

try:
    result = len(5)  # int has no length
except TypeError as e:
    print(f"  TypeError: {e}")

print("\n  TypeError: Operation on incompatible type")

print()  # Empty line


# ============================================================================
# 3. INDEXERROR
# ============================================================================
print("=" * 60)
print("3. INDEXERROR")
print("=" * 60)

# IndexError occurs when index is out of range
try:
    items = [1, 2, 3]
    value = items[10]
except IndexError as e:
    print(f"  IndexError: {e}")

try:
    text = "hello"
    char = text[10]
except IndexError as e:
    print(f"  IndexError: {e}")

print("\n  IndexError: Index out of range")

print()  # Empty line


# ============================================================================
# 4. KEYERROR
# ============================================================================
print("=" * 60)
print("4. KEYERROR")
print("=" * 60)

# KeyError occurs when dictionary key not found
try:
    data = {"name": "Alice", "age": 25}
    value = data["email"]
except KeyError as e:
    print(f"  KeyError: {e}")

print("\n  KeyError: Dictionary key not found")
print("  Alternative: Use .get() method to avoid KeyError")

# Better approach
value = data.get("email", "Not found")
print(f"  Using .get(): {value}")

print()  # Empty line


# ============================================================================
# 5. ZERODIVISIONERROR
# ============================================================================
print("=" * 60)
print("5. ZERODIVISIONERROR")
print("=" * 60)

# ZeroDivisionError occurs when dividing by zero
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"  ZeroDivisionError: {e}")

try:
    result = 10 // 0
except ZeroDivisionError as e:
    print(f"  ZeroDivisionError: {e}")

print("\n  ZeroDivisionError: Division by zero")

print()  # Empty line


# ============================================================================
# 6. ATTRIBUTEERROR
# ============================================================================
print("=" * 60)
print("6. ATTRIBUTEERROR")
print("=" * 60)

# AttributeError occurs when attribute doesn't exist
try:
    text = "hello"
    result = text.upper_case()  # Method doesn't exist
except AttributeError as e:
    print(f"  AttributeError: {e}")

try:
    obj = None
    result = obj.some_method()
except AttributeError as e:
    print(f"  AttributeError: {e}")

print("\n  AttributeError: Attribute or method not found")

print()  # Empty line


# ============================================================================
# 7. FILENOTFOUNDERROR
# ============================================================================
print("=" * 60)
print("7. FILENOTFOUNDERROR")
print("=" * 60)

# FileNotFoundError occurs when file doesn't exist
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"  FileNotFoundError: {e}")

print("\n  FileNotFoundError: File or directory not found")

print()  # Empty line


# ============================================================================
# 8. PERMISSIONERROR
# ============================================================================
print("=" * 60)
print("8. PERMISSIONERROR")
print("=" * 60)

# PermissionError occurs when access denied
try:
    # This might fail on some systems
    with open("/root/protected.txt", "w") as file:
        file.write("Hello")
except PermissionError as e:
    print(f"  PermissionError: {e}")
except FileNotFoundError:
    print("  FileNotFoundError: Directory does not exist")

print("\n  PermissionError: Access denied")

print()  # Empty line


# ============================================================================
# 9. KEYBOARDINTERRUPT
# ============================================================================
print("=" * 60)
print("9. KEYBOARDINTERRUPT")
print("=" * 60)

# KeyboardInterrupt occurs when user presses Ctrl+C
print("  KeyboardInterrupt: User interrupted program (Ctrl+C)")
print("  Try running code and pressing Ctrl+C to see it")

# Example handler
try:
    # Simulate long operation
    import time
    print("  Press Ctrl+C to interrupt (waiting 2 seconds)...")
    time.sleep(2)
except KeyboardInterrupt:
    print("  Program interrupted by user!")

print()  # Empty line


# ============================================================================
# 10. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("10. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Safe number input
def get_number(prompt):
    """Get number from user safely."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  Invalid input! Please enter a number.")

# Simulated (not actually asking for input)
print("  get_number() function handles ValueError")

# Example 2: Safe list access
def safe_get_item(items, index, default=None):
    """Get item from list safely."""
    try:
        return items[index]
    except IndexError:
        return default

items = [1, 2, 3]
print(f"  safe_get_item(items, 1): {safe_get_item(items, 1)}")
print(f"  safe_get_item(items, 10): {safe_get_item(items, 10)}")

# Example 3: Safe dictionary access
def safe_dict_get(data, key, default=None):
    """Get value from dict safely."""
    try:
        return data[key]
    except KeyError:
        return default

data = {"name": "Alice"}
print(f"  safe_dict_get(data, 'name'): {safe_dict_get(data, 'name')}")
print(f"  safe_dict_get(data, 'age'): {safe_dict_get(data, 'age', 'Unknown')}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("HANDLING EXCEPTIONS SUMMARY:")
print("=" * 60)
print("Common Exceptions:")
print("  - ValueError: Invalid value")
print("  - TypeError: Wrong type")
print("  - IndexError: Index out of range")
print("  - KeyError: Dictionary key not found")
print("  - ZeroDivisionError: Division by zero")
print("  - AttributeError: Attribute not found")
print("  - FileNotFoundError: File doesn't exist")
print("  - PermissionError: Access denied")
print("\nBest Practices:")
print("  - Handle specific exceptions")
print("  - Provide helpful error messages")
print("  - Use alternative methods when possible (.get() for dicts)")
print("=" * 60)

