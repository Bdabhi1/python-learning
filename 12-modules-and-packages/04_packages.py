"""
Packages in Python

This file demonstrates how to create and use packages - collections of
modules organized in directories.
"""

# ============================================================================
# 1. WHAT IS A PACKAGE?
# ============================================================================
print("=" * 60)
print("1. WHAT IS A PACKAGE?")
print("=" * 60)

print("  A package is a collection of modules organized in directories.")
print("  ")
print("  Package structure:")
print("    my_package/")
print("        __init__.py")
print("        module1.py")
print("        module2.py")
print("        subpackage/")
print("            __init__.py")
print("            module3.py")

print("\n  Key points:")
print("    - Directory containing __init__.py is a package")
print("    - Can contain multiple modules")
print("    - Can have subpackages")
print("    - Helps organize related code")

print()  # Empty line


# ============================================================================
# 2. CREATING A PACKAGE
# ============================================================================
print("=" * 60)
print("2. CREATING A PACKAGE")
print("=" * 60)

print("  Steps to create a package:")
print("    1. Create a directory")
print("    2. Add __init__.py file (can be empty)")
print("    3. Add module files (.py)")
print("    4. Optionally create subpackages")

print("\n  Example structure:")
print("    my_package/")
print("        __init__.py      # Makes it a package")
print("        utils.py         # Module 1")
print("        helpers.py       # Module 2")

print()  # Empty line


# ============================================================================
# 3. __init__.py FILE
# ============================================================================
print("=" * 60)
print("3. __init__.py FILE")
print("=" * 60)

print("  __init__.py makes a directory a Python package.")
print("  ")
print("  Can be empty:")
print("    # Empty file is fine")
print("  ")
print("  Or can contain initialization code:")
print("    from .module1 import function1")
print("    from .module2 import function2")
print("    ")
print("    __all__ = ['function1', 'function2']")

print("\n  Note: Python 3.3+ allows namespace packages without __init__.py")
print("  But it's still recommended to include it")

print()  # Empty line


# ============================================================================
# 4. IMPORTING FROM PACKAGES
# ============================================================================
print("=" * 60)
print("4. IMPORTING FROM PACKAGES")
print("=" * 60)

print("  Import entire module from package:")
print("    import my_package.module1")
print("    my_package.module1.function()")
print("  ")
print("  Import module from package:")
print("    from my_package import module1")
print("    module1.function()")
print("  ")
print("  Import specific item:")
print("    from my_package.module1 import function1")
print("    function1()")
print("  ")
print("  Import from subpackage:")
print("    from my_package.subpackage import module3")
print("    module3.function()")

print()  # Empty line


# ============================================================================
# 5. RELATIVE IMPORTS
# ============================================================================
print("=" * 60)
print("5. RELATIVE IMPORTS")
print("=" * 60)

print("  Use relative imports within packages:")
print("  ")
print("    from .module1 import function1  # Same package")
print("    from ..parent import something  # Parent package")
print("    from .subpackage.module import func  # Subpackage")
print("  ")
print("  . means current package")
print("  .. means parent package")

print("\n  Example in my_package/__init__.py:")
print("    from .utils import helper_function")
print("    from .helpers import utility_function")

print()  # Empty line


# ============================================================================
# 6. PACKAGE INITIALIZATION
# ============================================================================
print("=" * 60)
print("6. PACKAGE INITIALIZATION")
print("=" * 60)

print("  __init__.py can initialize the package:")
print("  ")
print("    # my_package/__init__.py")
print("    \"\"\"Package documentation\"\"\"")
print("    ")
print("    from .module1 import Class1")
print("    from .module2 import function2")
print("    ")
print("    __version__ = '1.0.0'")
print("    __all__ = ['Class1', 'function2']")

print("\n  This allows:")
print("    from my_package import Class1, function2")
print("    Instead of: from my_package.module1 import Class1")

print()  # Empty line


# ============================================================================
# 7. SUBPACKAGES
# ============================================================================
print("=" * 60)
print("7. SUBPACKAGES")
print("=" * 60)

print("  Packages can contain subpackages:")
print("  ")
print("    my_package/")
print("        __init__.py")
print("        module1.py")
print("        subpackage/")
print("            __init__.py")
print("            module2.py")
print("  ")
print("  Import from subpackage:")
print("    from my_package.subpackage import module2")
print("    from my_package.subpackage.module2 import function")

print()  # Empty line


# ============================================================================
# 8. PACKAGE VS MODULE
# ============================================================================
print("=" * 60)
print("8. PACKAGE VS MODULE")
print("=" * 60)

print("  Module:")
print("    - Single .py file")
print("    - Contains functions, classes, variables")
print("    - Example: math.py")
print("  ")
print("  Package:")
print("    - Directory with __init__.py")
print("    - Contains multiple modules")
print("    - Can have subpackages")
print("    - Example: os/ (directory)")

print("\n  Use packages to organize related modules")

print()  # Empty line


# ============================================================================
# 9. NAMESPACE PACKAGES
# ============================================================================
print("=" * 60)
print("9. NAMESPACE PACKAGES")
print("=" * 60)

print("  Python 3.3+ supports namespace packages")
print("  (packages without __init__.py)")
print("  ")
print("  But it's still recommended to use __init__.py:")
print("    - Makes intent clear")
print("    - Allows package initialization")
print("    - Better compatibility")

print()  # Empty line


# ============================================================================
# 10. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("10. PRACTICAL EXAMPLES")
print("=" * 60)

print("  Example package structure:")
print("    ")
print("    myapp/")
print("        __init__.py")
print("        config.py          # Configuration")
print("        utils.py            # Utility functions")
print("        models/             # Subpackage")
print("            __init__.py")
print("            user.py")
print("            product.py")
print("        views/              # Subpackage")
print("            __init__.py")
print("            home.py")
print("            admin.py")
print("  ")
print("  Usage:")
print("    from myapp import config")
print("    from myapp.models import user")
print("    from myapp.views import home")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PACKAGES SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Package = directory with __init__.py")
print("  - Contains multiple related modules")
print("  - Can have subpackages")
print("  - Use __init__.py for initialization")
print("  - Use relative imports within packages")
print("\nBest Practices:")
print("  - Organize related modules in packages")
print("  - Use clear, descriptive names")
print("  - Keep packages focused")
print("  - Document in __init__.py")
print("  - Use __all__ to control exports")
print("=" * 60)

