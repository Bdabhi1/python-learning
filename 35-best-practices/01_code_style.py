"""
Code Style and PEP 8

This file demonstrates Python code style guidelines and PEP 8 conventions.
"""

# ============================================================================
# 1. WHAT IS PEP 8?
# ============================================================================
print("=" * 60)
print("1. WHAT IS PEP 8?")
print("=" * 60)

print("  PEP 8 is Python's official style guide.")
print("  It provides conventions for writing readable Python code.")
print("  ")
print("  Key principles:")
print("    - Readability counts")
print("    - Consistency is important")
print("    - Follow community standards")

print()  # Empty line


# ============================================================================
# 2. INDENTATION
# ============================================================================
print("=" * 60)
print("2. INDENTATION")
print("=" * 60)

print("  Indentation rules:")
print("    - Use 4 spaces (not tabs)")
print("    - Be consistent")
print("    - Don't mix tabs and spaces")
print("  ")
print("  Good:")
print("    def function():")
print("        if condition:")
print("            do_something()")
print("  ")
print("  Bad:")
print("    def function():")
print("      if condition:  # 2 spaces")
print("            do_something()  # 8 spaces")

print()  # Empty line


# ============================================================================
# 3. LINE LENGTH
# ============================================================================
print("=" * 60)
print("3. LINE LENGTH")
print("=" * 60)

print("  Line length guidelines:")
print("    - Maximum 79 characters for code")
print("    - Maximum 72 characters for comments")
print("    - Break long lines appropriately")
print("  ")
print("  Breaking long lines:")
print("    ")
print("    # Good")
print("    result = function_name(")
print("        argument1,")
print("        argument2,")
print("        argument3")
print("    )")

print()  # Empty line


# ============================================================================
# 4. BLANK LINES
# ============================================================================
print("=" * 60)
print("4. BLANK LINES")
print("=" * 60)

print("  Blank line rules:")
print("    - Two blank lines between top-level functions/classes")
print("    - One blank line between methods")
print("    - Use blank lines to separate logical sections")
print("  ")
print("  Example:")
print("    ")
print("    def function1():")
print("        pass")
print("    ")
print("    ")
print("    def function2():")
print("        pass")

print()  # Empty line


# ============================================================================
# 5. IMPORTS
# ============================================================================
print("=" * 60)
print("5. IMPORTS")
print("=" * 60)

print("  Import order:")
print("    1. Standard library imports")
print("    2. Third-party imports")
print("    3. Local application imports")
print("  ")
print("  Example:")
print("    ")
print("    # Standard library")
print("    import os")
print("    import sys")
print("    ")
print("    # Third-party")
print("    import requests")
print("    import numpy")
print("    ")
print("    # Local")
print("    from my_package import module")

print()  # Empty line


# ============================================================================
# 6. WHITESPACE
# ============================================================================
print("=" * 60)
print("6. WHITESPACE")
print("=" * 60)

print("  Whitespace rules:")
print("    - Use spaces around operators")
print("    - No spaces inside parentheses/brackets")
print("    - Use spaces after commas")
print("  ")
print("  Good:")
print("    x = 1 + 2")
print("    if x == 5:")
print("        items = [1, 2, 3]")
print("  ")
print("  Bad:")
print("    x=1+2")
print("    if x==5:")
print("        items = [1,2,3]")

print()  # Empty line


# ============================================================================
# 7. NAMING CONVENTIONS
# ============================================================================
print("=" * 60)
print("7. NAMING CONVENTIONS")
print("=" * 60)

print("  Naming conventions:")
print("    - Variables/functions: lowercase_with_underscores")
print("    - Constants: UPPERCASE_WITH_UNDERSCORES")
print("    - Classes: PascalCase")
print("    - Private: _single_underscore")
print("    - Name mangling: __double_underscore")
print("  ")
print("  Examples:")
print("    user_name = \"John\"")
print("    MAX_SIZE = 100")
print("    class UserAccount:")
print("        _internal = 10")

print()  # Empty line


# ============================================================================
# 8. CODE FORMATTING TOOLS
# ============================================================================
print("=" * 60)
print("8. CODE FORMATTING TOOLS")
print("=" * 60)

print("  Tools to help with code style:")
print("    ")
print("    - black: Auto-formatter")
print("      black my_file.py")
print("    ")
print("    - autopep8: Auto-formats to PEP 8")
print("      autopep8 --in-place my_file.py")
print("    ")
print("    - flake8: Linter")
print("      flake8 my_file.py")
print("    ")
print("    - pylint: Advanced linter")
print("      pylint my_file.py")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("CODE STYLE SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Follow PEP 8 style guide")
print("  - Use 4 spaces for indentation")
print("  - Maximum 79 characters per line")
print("  - Use proper blank lines")
print("  - Follow import order")
print("  - Use consistent naming conventions")
print("  - Use formatting tools (black, flake8)")
print("=" * 60)

