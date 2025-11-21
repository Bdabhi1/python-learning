"""
Error Handling in Python

This file demonstrates best practices for error handling.
"""

# ============================================================================
# 1. WHAT IS ERROR HANDLING?
# ============================================================================
print("=" * 60)
print("1. WHAT IS ERROR HANDLING?")
print("=" * 60)

print("  Error handling deals with exceptions and errors.")
print("  Good error handling:")
print("    - Prevents crashes")
print("    - Provides useful error messages")
print("    - Handles edge cases")
print("    - Logs errors appropriately")

print()  # Empty line


# ============================================================================
# 2. USE SPECIFIC EXCEPTIONS
# ============================================================================
print("=" * 60)
print("2. USE SPECIFIC EXCEPTIONS")
print("=" * 60)

print("  Catch specific exceptions:")
print("    ")
print("    # Good")
print("    try:")
print("        value = int(user_input)")
print("    except ValueError:")
print("        print(\"Invalid number\")")
print("    ")
print("    # Bad")
print("    try:")
print("        value = int(user_input)")
print("    except Exception:")
print("        print(\"Error\")")

print()  # Empty line


# ============================================================================
# 3. DON'T SUPPRESS EXCEPTIONS
# ============================================================================
print("=" * 60)
print("3. DON'T SUPPRESS EXCEPTIONS")
print("=" * 60)

print("  Don't silently ignore errors:")
print("    ")
print("    # Bad")
print("    try:")
print("        risky_operation()")
print("    except:")
print("        pass  # Silent failure")
print("    ")
print("    # Good")
print("    try:")
print("        risky_operation()")
print("    except SpecificError as e:")
print("        logger.error(f\"Operation failed: {e}\")")
print("        handle_error(e)")

print()  # Empty line


# ============================================================================
# 4. USE CONTEXT MANAGERS
# ============================================================================
print("=" * 60)
print("4. USE CONTEXT MANAGERS")
print("=" * 60)

print("  Use context managers for resources:")
print("    ")
print("    # Good")
print("    with open('file.txt') as f:")
print("        content = f.read()")
print("    # File automatically closed")
print("    ")
print("    # Bad")
print("    f = open('file.txt')")
print("    content = f.read()")
print("    f.close()  # Might not execute if exception occurs")

print()  # Empty line


# ============================================================================
# 5. RAISE MEANINGFUL ERRORS
# ============================================================================
print("=" * 60)
print("5. RAISE MEANINGFUL ERRORS")
print("=" * 60)

print("  Raise exceptions with clear messages:")
print("    ")
print("    # Good")
print("    if age < 0:")
print("        raise ValueError(f\"Age cannot be negative: {age}\")")
print("    ")
print("    # Less helpful")
print("    if age < 0:")
print("        raise ValueError(\"Invalid age\")")

print()  # Empty line


# ============================================================================
# 6. HANDLE MULTIPLE EXCEPTIONS
# ============================================================================
print("=" * 60)
print("6. HANDLE MULTIPLE EXCEPTIONS")
print("=" * 60)

print("  Handle different exceptions appropriately:")
print("    ")
print("    try:")
print("        result = process_data(data)")
print("    except ValueError as e:")
print("        print(f\"Invalid data: {e}\")")
print("    except FileNotFoundError as e:")
print("        print(f\"File not found: {e}\")")
print("    except Exception as e:")
print("        print(f\"Unexpected error: {e}\")")
print("        raise  # Re-raise if unexpected")

print()  # Empty line


# ============================================================================
# 7. FINALLY BLOCKS
# ============================================================================
print("=" * 60)
print("7. FINALLY BLOCKS")
print("=" * 60)

print("  Use finally for cleanup:")
print("    ")
print("    try:")
print("        process_data()")
print("    except Exception as e:")
print("        handle_error(e)")
print("    finally:")
print("        cleanup_resources()  # Always executes")
print("  ")
print("  Finally block always executes, even if exception occurs")

print()  # Empty line


# ============================================================================
# 8. CUSTOM EXCEPTIONS
# ============================================================================
print("=" * 60)
print("8. CUSTOM EXCEPTIONS")
print("=" * 60)

print("  Create custom exceptions for your domain:")
print("    ")
print("    class ValidationError(Exception):")
print("        \"\"\"Raised when validation fails.\"\"\"")
print("        pass")
print("    ")
print("    class InsufficientFundsError(Exception):")
print("        \"\"\"Raised when account has insufficient funds.\"\"\"")
print("        pass")
print("  ")
print("  Use custom exceptions for domain-specific errors")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("ERROR HANDLING SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Catch specific exceptions")
print("  - Don't suppress exceptions silently")
print("  - Use context managers for resources")
print("  - Raise meaningful error messages")
print("  - Handle multiple exception types")
print("  - Use finally for cleanup")
print("  - Create custom exceptions when needed")
print("=" * 60)

