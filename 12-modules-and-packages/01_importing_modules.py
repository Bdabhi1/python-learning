"""
Importing Modules in Python

This file demonstrates how to import and use modules - both from Python's
standard library and custom modules.
"""

# ============================================================================
# 1. BASIC IMPORT
# ============================================================================
print("=" * 60)
print("1. BASIC IMPORT")
print("=" * 60)

# Import entire module
import math

# Use module with dot notation
print(f"  math.pi: {math.pi}")
print(f"  math.sqrt(16): {math.sqrt(16)}")
print(f"  math.pow(2, 3): {math.pow(2, 3)}")

print("\n  Syntax: import module_name")
print("  Access with: module_name.function_name")

print()  # Empty line


# ============================================================================
# 2. IMPORT WITH ALIAS
# ============================================================================
print("=" * 60)
print("2. IMPORT WITH ALIAS")
print("=" * 60)

# Import with shorter name
import math as m

print(f"  m.pi: {m.pi}")
print(f"  m.sqrt(16): {m.sqrt(16)}")

# Another example
import datetime as dt
now = dt.datetime.now()
print(f"  Current time: {now}")

print("\n  Syntax: import module_name as alias")
print("  Useful for long module names")

print()  # Empty line


# ============================================================================
# 3. IMPORT SPECIFIC ITEMS
# ============================================================================
print("=" * 60)
print("3. IMPORT SPECIFIC ITEMS")
print("=" * 60)

# Import specific functions/constants
from math import pi, sqrt, pow

print(f"  pi: {pi}")
print(f"  sqrt(16): {sqrt(16)}")
print(f"  pow(2, 3): {pow(2, 3)}")

# No need for module name prefix
print("\n  Syntax: from module_name import item1, item2")
print("  Access directly without module name")

print()  # Empty line


# ============================================================================
# 4. IMPORT ALL (NOT RECOMMENDED)
# ============================================================================
print("=" * 60)
print("4. IMPORT ALL (NOT RECOMMENDED)")
print("=" * 60)

# Import all from module
from math import *

print(f"  pi: {pi}")
print(f"  sqrt(16): {sqrt(16)}")
print(f"  pow(2, 3): {pow(2, 3)}")

print("\n  Syntax: from module_name import *")
print("  Warning: Can cause naming conflicts!")
print("  Generally discouraged in production code")

print()  # Empty line


# ============================================================================
# 5. MULTIPLE IMPORTS
# ============================================================================
print("=" * 60)
print("5. MULTIPLE IMPORTS")
print("=" * 60)

# Import multiple modules
import math
import random
import os

print(f"  math.pi: {math.pi}")
print(f"  random.randint(1, 10): {random.randint(1, 10)}")
print(f"  os.getcwd(): {os.getcwd()}")

# Import multiple items from one module
from math import pi, e, sqrt, pow
print(f"  pi: {pi}, e: {e}")

print()  # Empty line


# ============================================================================
# 6. CHECKING MODULE ATTRIBUTES
# ============================================================================
print("=" * 60)
print("6. CHECKING MODULE ATTRIBUTES")
print("=" * 60)

import math

# Check what's in a module
print("  Available in math module:")
print(f"    dir(math): {dir(math)[:10]}...")  # First 10 items

# Check if attribute exists
print(f"    hasattr(math, 'pi'): {hasattr(math, 'pi')}")
print(f"    hasattr(math, 'sqrt'): {hasattr(math, 'sqrt')}")

# Get attribute value
print(f"    getattr(math, 'pi'): {getattr(math, 'pi')}")

print()  # Empty line


# ============================================================================
# 7. MODULE DOCUMENTATION
# ============================================================================
print("=" * 60)
print("7. MODULE DOCUMENTATION")
print("=" * 60)

import math

# Access module docstring
print("  math.__doc__:")
print(f"    {math.__doc__[:100]}...")  # First 100 chars

# Access function docstring
print("\n  math.sqrt.__doc__:")
print(f"    {math.sqrt.__doc__}")

print()  # Empty line


# ============================================================================
# 8. IMPORTING FROM DIFFERENT LOCATIONS
# ============================================================================
print("=" * 60)
print("8. IMPORTING FROM DIFFERENT LOCATIONS")
print("=" * 60)

import sys

# See module search path
print("  Python searches for modules in:")
for i, path in enumerate(sys.path[:5], 1):  # First 5 paths
    print(f"    {i}. {path}")

print("\n  Modules are searched in this order:")
print("    1. Current directory")
print("    2. PYTHONPATH directories")
print("    3. Standard library")
print("    4. Site-packages")

print()  # Empty line


# ============================================================================
# 9. HANDLING IMPORT ERRORS
# ============================================================================
print("=" * 60)
print("9. HANDLING IMPORT ERRORS")
print("=" * 60)

# Try to import a module
try:
    import nonexistent_module
except ModuleNotFoundError:
    print("  ModuleNotFoundError: Module not found!")

# Try to import optional module
try:
    import optional_module
    print("  Optional module imported successfully")
except ImportError:
    print("  Optional module not available, using fallback")
    optional_module = None

print("\n  Always handle ImportError for optional modules")

print()  # Empty line


# ============================================================================
# 10. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("10. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Using math module
import math

radius = 5
area = math.pi * radius ** 2
print(f"  Circle with radius {radius}:")
print(f"    Area: {area:.2f}")

# Example 2: Using random module
import random

dice_roll = random.randint(1, 6)
print(f"  Dice roll: {dice_roll}")

# Example 3: Using datetime module
from datetime import datetime
now = datetime.now()
print(f"  Current date/time: {now}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("IMPORTING MODULES SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - import module_name - import entire module")
print("  - import module_name as alias - import with alias")
print("  - from module_name import item - import specific items")
print("  - from module_name import * - import all (not recommended)")
print("  - Use dot notation to access: module.function()")
print("  - Handle ImportError for optional modules")
print("\nBest Practices:")
print("  - Use specific imports when possible")
print("  - Avoid 'import *' to prevent naming conflicts")
print("  - Use aliases for long module names")
print("  - Organize imports: stdlib, third-party, local")
print("=" * 60)

