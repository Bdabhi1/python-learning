"""
Documentation in Python

This file demonstrates how to write good documentation in Python.
"""

# ============================================================================
# 1. WHAT IS DOCUMENTATION?
# ============================================================================
print("=" * 60)
print("1. WHAT IS DOCUMENTATION?")
print("=" * 60)

print("  Documentation helps others understand your code.")
print("  Types of documentation:")
print("    - Docstrings (function/class documentation)")
print("    - Comments (inline explanations)")
print("    - README files (project documentation)")
print("    - Type hints (type information)")

print()  # Empty line


# ============================================================================
# 2. DOCSTRINGS
# ============================================================================
print("=" * 60)
print("2. DOCSTRINGS")
print("=" * 60)

print("  Function docstring example:")
print("    ")
print("    def calculate_total(items):")
print("        \"\"\"")
print("        Calculate total price of items.")
print("        ")
print("        Args:")
print("            items: List of items with price attribute")
print("        ")
print("        Returns:")
print("            Total price as float")
print("        ")
print("        Raises:")
print("            ValueError: If items list is empty")
print("        \"\"\"")
print("        return sum(item.price for item in items)")

print()  # Empty line


# ============================================================================
# 3. CLASS DOCSTRINGS
# ============================================================================
print("=" * 60)
print("3. CLASS DOCSTRINGS")
print("=" * 60)

print("  Class docstring example:")
print("    ")
print("    class UserAccount:")
print("        \"\"\"")
print("        Represents a user account.")
print("        ")
print("        Attributes:")
print("            name: User's name")
print("            email: User's email address")
print("            age: User's age")
print("        \"\"\"")
print("        ")
print("        def __init__(self, name, email, age):")
print("            self.name = name")
print("            self.email = email")
print("            self.age = age")

print()  # Empty line


# ============================================================================
# 4. MODULE DOCSTRINGS
# ============================================================================
print("=" * 60)
print("4. MODULE DOCSTRINGS")
print("=" * 60)

print("  Module docstring (at top of file):")
print("    ")
print("    \"\"\"")
print("    User management module.")
print("    ")
print("    This module provides classes and functions")
print("    for managing user accounts.")
print("    \"\"\"")
print("    ")
print("    import os")
print("    import sys")

print()  # Empty line


# ============================================================================
# 5. COMMENTS
# ============================================================================
print("=" * 60)
print("5. COMMENTS")
print("=" * 60)

print("  Comment guidelines:")
print("    - Explain why, not what")
print("    - Keep comments up to date")
print("    - Don't state the obvious")
print("  ")
print("  Good:")
print("    # Use binary search for O(log n) performance")
print("    result = binary_search(items, target)")
print("  ")
print("  Bad:")
print("    # Increment counter")
print("    counter += 1")

print()  # Empty line


# ============================================================================
# 6. TYPE HINTS
# ============================================================================
print("=" * 60)
print("6. TYPE HINTS")
print("=" * 60)

print("  Type hints provide type information:")
print("    ")
print("    from typing import List, Optional")
print("    ")
print("    def process_items(items: List[str]) -> Optional[int]:")
print("        \"\"\"Process list of items.\"\"\"")
print("        if not items:")
print("            return None")
print("        return len(items)")
print("  ")
print("  Benefits:")
print("    - Better IDE support")
print("    - Type checking with mypy")
print("    - Self-documenting code")

print()  # Empty line


# ============================================================================
# 7. README FILES
# ============================================================================
print("=" * 60)
print("7. README FILES")
print("=" * 60)

print("  README.md should include:")
print("    - Project description")
print("    - Installation instructions")
print("    - Usage examples")
print("    - API documentation")
print("    - Contributing guidelines")
print("    - License information")
print("  ")
print("  Keep README up to date!")

print()  # Empty line


# ============================================================================
# 8. DOCUMENTATION TOOLS
# ============================================================================
print("=" * 60)
print("8. DOCUMENTATION TOOLS")
print("=" * 60)

print("  Documentation generation tools:")
print("    ")
print("    - Sphinx: Generate HTML/PDF docs")
print("      sphinx-quickstart")
print("    ")
print("    - pydoc: Built-in documentation")
print("      pydoc my_module")
print("    ")
print("    - help(): Built-in help")
print("      help(my_function)")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("DOCUMENTATION SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Write docstrings for functions/classes")
print("  - Use comments to explain why")
print("  - Add type hints for clarity")
print("  - Keep README files updated")
print("  - Use documentation tools")
print("  - Keep documentation in sync with code")
print("=" * 60)

