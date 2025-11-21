"""
Basic Context Managers in Python

This file demonstrates the fundamental concepts of context managers
and the `with` statement.
"""

# ============================================================================
# 1. WHAT IS A CONTEXT MANAGER?
# ============================================================================
print("=" * 60)
print("1. WHAT IS A CONTEXT MANAGER?")
print("=" * 60)

print("  A context manager is an object that defines what happens")
print("  before and after a block of code runs.")
print("  ")
print("  Key features:")
print("    - Automatic setup and teardown")
print("    - Guaranteed cleanup even on exceptions")
print("    - Clean resource management")
print("    - Used with 'with' statement")

print()  # Empty line


# ============================================================================
# 2. THE 'with' STATEMENT
# ============================================================================
print("=" * 60)
print("2. THE 'with' STATEMENT")
print("=" * 60)

# Basic file handling with context manager
try:
    with open('sample.txt', 'w') as f:
        f.write("Hello, World!")
    print("  File written successfully")
    
    with open('sample.txt', 'r') as f:
        content = f.read()
        print(f"  File content: {content}")
except FileNotFoundError:
    print("  File not found")

print("\n  File is automatically closed when block exits")

print()  # Empty line


# ============================================================================
# 3. HOW 'with' WORKS
# ============================================================================
print("=" * 60)
print("3. HOW 'with' WORKS")
print("=" * 60)

print("  The 'with' statement:")
print("    1. Calls __enter__() method")
print("    2. Executes code block")
print("    3. Calls __exit__() method (even if exception occurs)")
print("  ")
print("  Syntax:")
print("    with expression as variable:")
print("        # code block")

print()  # Empty line


# ============================================================================
# 4. COMPARISON: WITH VS WITHOUT
# ============================================================================
print("=" * 60)
print("4. COMPARISON: WITH VS WITHOUT")
print("=" * 60)

print("  Without context manager (risky):")
print("    file = open('data.txt')")
print("    content = file.read()")
print("    file.close()  # Might not execute if exception occurs")
print("  ")
print("  With context manager (safe):")
print("    with open('data.txt') as file:")
print("        content = file.read()")
print("    # File always closed, even on exception")

print()  # Empty line


# ============================================================================
# 5. EXCEPTION SAFETY
# ============================================================================
print("=" * 60)
print("5. EXCEPTION SAFETY")
print("=" * 60)

print("  Context managers guarantee cleanup even if exceptions occur:")
print("  ")
print("    with open('file.txt') as f:")
print("        content = f.read()")
print("        raise ValueError('Error!')  # Exception occurs")
print("    # File still closed automatically")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("BASIC CONTEXT MANAGERS SUMMARY:")
print("=" * 60)
print("  - Context managers ensure proper resource management")
print("  - Use 'with' statement to enter context")
print("  - Automatic cleanup guaranteed")
print("  - Exception-safe")
print("  - Cleaner than try-finally blocks")
print("=" * 60)

