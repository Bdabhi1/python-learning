"""
Package Structure in Python

This file demonstrates how to organize code into a proper package structure.
"""

import os

# ============================================================================
# 1. WHAT IS A PACKAGE?
# ============================================================================
print("=" * 60)
print("1. WHAT IS A PACKAGE?")
print("=" * 60)

print("  A package is a directory containing Python modules.")
print("  It allows you to organize code into logical units.")
print("  ")
print("  Key components:")
print("    - __init__.py file (makes directory a package)")
print("    - Python modules (.py files)")
print("    - Subpackages (nested directories)")

print()  # Empty line


# ============================================================================
# 2. BASIC PACKAGE STRUCTURE
# ============================================================================
print("=" * 60)
print("2. BASIC PACKAGE STRUCTURE")
print("=" * 60)

print("  Basic package structure:")
print("    ")
print("    my_package/")
print("    ├── __init__.py")
print("    ├── module1.py")
print("    └── module2.py")
print("  ")
print("  The __init__.py file can be empty or contain initialization code.")

print()  # Empty line


# ============================================================================
# 3. PACKAGE WITH SUBPACKAGES
# ============================================================================
print("=" * 60)
print("3. PACKAGE WITH SUBPACKAGES")
print("=" * 60)

print("  Package with subpackages:")
print("    ")
print("    my_package/")
print("    ├── __init__.py")
print("    ├── module1.py")
print("    ├── subpackage/")
print("    │   ├── __init__.py")
print("    │   └── module3.py")
print("    └── utils/")
print("        ├── __init__.py")
print("        └── helpers.py")
print("  ")
print("  Subpackages are nested packages within a package.")

print()  # Empty line


# ============================================================================
# 4. COMPLETE PROJECT STRUCTURE
# ============================================================================
print("=" * 60)
print("4. COMPLETE PROJECT STRUCTURE")
print("=" * 60)

print("  Complete project structure:")
print("    ")
print("    my_project/")
print("    ├── my_package/")
print("    │   ├── __init__.py")
print("    │   ├── module1.py")
print("    │   └── module2.py")
print("    ├── tests/")
print("    │   ├── __init__.py")
print("    │   └── test_module1.py")
print("    ├── docs/")
print("    │   └── README.md")
print("    ├── setup.py")
print("    ├── README.md")
print("    ├── LICENSE")
print("    └── requirements.txt")
print("  ")
print("  This structure includes:")
print("    - Source code (my_package/)")
print("    - Tests (tests/)")
print("    - Documentation (docs/)")
print("    - Configuration files (setup.py, requirements.txt)")

print()  # Empty line


# ============================================================================
# 5. __init__.py FILE
# ============================================================================
print("=" * 60)
print("5. __init__.py FILE")
print("=" * 60)

print("  The __init__.py file:")
print("    - Makes a directory a Python package")
print("    - Can be empty")
print("    - Can contain initialization code")
print("    - Can control what's imported with 'from package import *'")
print("  ")
print("  Example __init__.py:")
print("    ")
print("    # Empty __init__.py")
print("    # (just makes directory a package)")
print("    ")
print("    # Or with imports:")
print("    from .module1 import function1")
print("    from .module2 import Class1")
print("    ")
print("    __all__ = ['function1', 'Class1']")

print()  # Empty line


# ============================================================================
# 6. IMPORTING FROM PACKAGES
# ============================================================================
print("=" * 60)
print("6. IMPORTING FROM PACKAGES")
print("=" * 60)

print("  Importing from packages:")
print("    ")
print("    # Import entire package")
print("    import my_package")
print("    ")
print("    # Import specific module")
print("    from my_package import module1")
print("    ")
print("    # Import from subpackage")
print("    from my_package.subpackage import module3")
print("    ")
print("    # Import specific function/class")
print("    from my_package.module1 import function1")

print()  # Empty line


# ============================================================================
# 7. RELATIVE IMPORTS
# ============================================================================
print("=" * 60)
print("7. RELATIVE IMPORTS")
print("=" * 60)

print("  Relative imports (within package):")
print("    ")
print("    # In module1.py, import from same package")
print("    from . import module2")
print("    from .module2 import function1")
print("    ")
print("    # Import from parent package")
print("    from .. import parent_module")
print("    ")
print("    # Import from sibling subpackage")
print("    from ..subpackage import module3")
print("  ")
print("  Use relative imports within packages.")

print()  # Empty line


# ============================================================================
# 8. PACKAGE METADATA
# ============================================================================
print("=" * 60)
print("8. PACKAGE METADATA")
print("=" * 60)

print("  Package metadata in __init__.py:")
print("    ")
print("    __version__ = '0.1.0'")
print("    __author__ = 'Your Name'")
print("    __email__ = 'your.email@example.com'")
print("    ")
print("    # Access metadata")
print("    import my_package")
print("    print(my_package.__version__)")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PACKAGE STRUCTURE SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Packages are directories with __init__.py")
print("  - Organize code into logical units")
print("  - Use subpackages for nested organization")
print("  - Include tests, docs, and config files")
print("  - Use relative imports within packages")
print("  - Define metadata in __init__.py")
print("=" * 60)

