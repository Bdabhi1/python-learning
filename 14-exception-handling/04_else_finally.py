"""
Else and Finally Clauses in Exception Handling

This file demonstrates the else and finally clauses in try-except
blocks for additional control flow and cleanup operations.
"""

# ============================================================================
# 1. ELSE CLAUSE
# ============================================================================
print("=" * 60)
print("1. ELSE CLAUSE")
print("=" * 60)

# Else clause runs if no exception occurs
try:
    result = 10 / 2
except ZeroDivisionError:
    print("  Division by zero!")
else:
    print(f"  No exception! Result: {result}")

print("\n  else: Runs only if no exception occurs")

print()  # Empty line


# ============================================================================
# 2. ELSE WITH MULTIPLE OPERATIONS
# ============================================================================
print("=" * 60)
print("2. ELSE WITH MULTIPLE OPERATIONS")
print("=" * 60)

# Else can contain multiple statements
try:
    number = int("5")
    result = 10 / number
except (ValueError, ZeroDivisionError) as e:
    print(f"  Error: {e}")
else:
    print(f"  Success! Number: {number}")
    print(f"  Result: {result}")
    print("  All operations completed successfully")

print("\n  else block can contain any code")

print()  # Empty line


# ============================================================================
# 3. FINALLY CLAUSE
# ============================================================================
print("=" * 60)
print("3. FINALLY CLAUSE")
print("=" * 60)

# Finally always runs
try:
    result = 10 / 2
    print(f"  Result: {result}")
except ZeroDivisionError:
    print("  Division by zero!")
finally:
    print("  Finally: This always runs")

print("\n  finally: Always runs, regardless of exceptions")

print()  # Empty line


# ============================================================================
# 4. FINALLY WITH EXCEPTION
# ============================================================================
print("=" * 60)
print("4. FINALLY WITH EXCEPTION")
print("=" * 60)

# Finally runs even when exception occurs
try:
    result = 10 / 0
except ZeroDivisionError:
    print("  Caught ZeroDivisionError")
finally:
    print("  Finally: This still runs even with exception")

print()  # Empty line


# ============================================================================
# 5. FINALLY FOR CLEANUP
# ============================================================================
print("=" * 60)
print("5. FINALLY FOR CLEANUP")
print("=" * 60)

# Finally is perfect for cleanup
file_handle = None
try:
    file_handle = open("test_file.txt", "w")
    file_handle.write("Hello, World!")
except Exception as e:
    print(f"  Error: {e}")
finally:
    if file_handle:
        file_handle.close()
        print("  File closed in finally block")

# Better: use 'with' statement (automatic cleanup)
try:
    with open("test_file2.txt", "w") as file:
        file.write("Hello, World!")
except Exception as e:
    print(f"  Error: {e}")
# File automatically closed here

# Clean up
import os
for f in ["test_file.txt", "test_file2.txt"]:
    if os.path.exists(f):
        os.remove(f)

print("\n  finally ensures cleanup happens")

print()  # Empty line


# ============================================================================
# 6. ELSE AND FINALLY TOGETHER
# ============================================================================
print("=" * 60)
print("6. ELSE AND FINALLY TOGETHER")
print("=" * 60)

# Can use both else and finally
try:
    number = int("10")
    result = 100 / number
except (ValueError, ZeroDivisionError) as e:
    print(f"  Error: {e}")
else:
    print(f"  Success! Result: {result}")
finally:
    print("  Cleanup: This always runs")

print("\n  Order: try -> except -> else -> finally")

print()  # Empty line


# ============================================================================
# 7. FINALLY WITH RETURN
# ============================================================================
print("=" * 60)
print("7. FINALLY WITH RETURN")
print("=" * 60)

# Finally runs even with return
def test_function():
    try:
        return "Success"
    except Exception:
        return "Error"
    finally:
        print("  Finally: Runs even with return")

result = test_function()
print(f"  Function returned: {result}")

print("\n  finally executes before return")

print()  # Empty line


# ============================================================================
# 8. PRACTICAL EXAMPLE: FILE PROCESSING
# ============================================================================
print("=" * 60)
print("8. PRACTICAL EXAMPLE: FILE PROCESSING")
print("=" * 60)

def process_file(filename):
    """Process file with proper cleanup."""
    file_handle = None
    try:
        file_handle = open(filename, "r")
        content = file_handle.read()
        number = int(content.strip())
        result = 100 / number
        return result
    except FileNotFoundError:
        print(f"  File '{filename}' not found")
        return None
    except ValueError:
        print(f"  Invalid number in file")
        return None
    except ZeroDivisionError:
        print(f"  Cannot divide by zero")
        return None
    else:
        print("  File processed successfully")
    finally:
        if file_handle:
            file_handle.close()
            print("  File closed")

# Test with non-existent file
result = process_file("nonexistent.txt")
print(f"  Result: {result}")

print()  # Empty line


# ============================================================================
# 9. PRACTICAL EXAMPLE: DATABASE CONNECTION
# ============================================================================
print("=" * 60)
print("9. PRACTICAL EXAMPLE: DATABASE CONNECTION")
print("=" * 60)

# Simulated database connection
class DatabaseConnection:
    def __init__(self):
        self.connected = False
    
    def connect(self):
        self.connected = True
        print("  Connected to database")
    
    def close(self):
        self.connected = False
        print("  Database connection closed")

def query_database():
    """Query database with proper cleanup."""
    db = DatabaseConnection()
    try:
        db.connect()
        # Simulate query
        print("  Executing query...")
        return "Query results"
    except Exception as e:
        print(f"  Query error: {e}")
        return None
    finally:
        db.close()

result = query_database()
print(f"  Result: {result}")

print()  # Empty line


# ============================================================================
# 10. WHEN TO USE ELSE VS FINALLY
# ============================================================================
print("=" * 60)
print("10. WHEN TO USE ELSE VS FINALLY")
print("=" * 60)

print("  Use 'else' when:")
print("    - Code should run only if no exception")
print("    - Success case handling")
print("    - Additional processing after try succeeds")
print("  ")
print("  Use 'finally' when:")
print("    - Cleanup is required (close files, connections)")
print("    - Code must always run")
print("    - Resource management")
print("    - Logging completion")

print("\n  Example:")
print("    try:")
print("        # Risky operation")
print("    except Exception:")
print("        # Handle error")
print("    else:")
print("        # Success case")
print("    finally:")
print("        # Always cleanup")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("ELSE AND FINALLY SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - else: Runs only if no exception occurs")
print("  - finally: Always runs, regardless of exceptions")
print("  - Can use both else and finally together")
print("  - finally runs even with return statements")
print("  - finally is perfect for cleanup operations")
print("\nUse Cases:")
print("  - else: Success case handling")
print("  - finally: Resource cleanup, logging")
print("=" * 60)

