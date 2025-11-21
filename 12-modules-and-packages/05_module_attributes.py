"""
Module Attributes in Python

This file demonstrates important attributes and features of modules,
including __name__, __file__, __doc__, and more.
"""

# ============================================================================
# 1. __name__ ATTRIBUTE
# ============================================================================
print("=" * 60)
print("1. __name__ ATTRIBUTE")
print("=" * 60)

# Current module's name
print(f"  Current __name__: {__name__}")

# When run directly, __name__ is '__main__'
# When imported, __name__ is the module name

import math
print(f"  math.__name__: {math.__name__}")

print("\n  Use case:")
print("    if __name__ == '__main__':")
print("        # Code runs only when executed directly")

print()  # Empty line


# ============================================================================
# 2. __file__ ATTRIBUTE
# ============================================================================
print("=" * 60)
print("2. __file__ ATTRIBUTE")
print("=" * 60)

# Current file path
print(f"  Current __file__: {__file__}")

# Module file path
import math
print(f"  math.__file__: {math.__file__}")

print("\n  __file__ contains the path to the module file")

print()  # Empty line


# ============================================================================
# 3. __doc__ ATTRIBUTE
# ============================================================================
print("=" * 60)
print("3. __doc__ ATTRIBUTE")
print("=" * 60)

# Module docstring
import math
print(f"  math.__doc__: {math.__doc__[:100]}...")

# Function docstring
print(f"  math.sqrt.__doc__: {math.sqrt.__doc__}")

print("\n  __doc__ contains the module/function docstring")

print()  # Empty line


# ============================================================================
# 4. __dict__ ATTRIBUTE
# ============================================================================
print("=" * 60)
print("4. __dict__ ATTRIBUTE")
print("=" * 60)

import math

# Module's namespace dictionary
print("  math.__dict__ keys (first 10):")
keys = list(math.__dict__.keys())[:10]
for key in keys:
    print(f"    {key}")

print("\n  __dict__ contains all module attributes")

print()  # Empty line


# ============================================================================
# 5. dir() FUNCTION
# ============================================================================
print("=" * 60)
print("5. dir() FUNCTION")
print("=" * 60)

import math

# Get all attributes of module
attributes = dir(math)
print(f"  dir(math) - first 10 items:")
for attr in attributes[:10]:
    print(f"    {attr}")

print(f"\n  Total attributes: {len(attributes)}")

print("\n  dir() returns list of names in module namespace")

print()  # Empty line


# ============================================================================
# 6. hasattr() FUNCTION
# ============================================================================
print("=" * 60)
print("6. hasattr() FUNCTION")
print("=" * 60)

import math

# Check if module has attribute
print(f"  hasattr(math, 'pi'): {hasattr(math, 'pi')}")
print(f"  hasattr(math, 'sqrt'): {hasattr(math, 'sqrt')}")
print(f"  hasattr(math, 'nonexistent'): {hasattr(math, 'nonexistent')}")

print("\n  hasattr() checks if object has attribute")

print()  # Empty line


# ============================================================================
# 7. getattr() FUNCTION
# ============================================================================
print("=" * 60)
print("7. getattr() FUNCTION")
print("=" * 60)

import math

# Get attribute value
pi_value = getattr(math, 'pi')
print(f"  getattr(math, 'pi'): {pi_value}")

# Get attribute with default
sqrt_func = getattr(math, 'sqrt', None)
print(f"  getattr(math, 'sqrt'): {sqrt_func}")

# Use the function
result = sqrt_func(16)
print(f"  sqrt_func(16): {result}")

print("\n  getattr() gets attribute value, with optional default")

print()  # Empty line


# ============================================================================
# 8. setattr() FUNCTION
# ============================================================================
print("=" * 60)
print("8. setattr() FUNCTION")
print("=" * 60)

# Create a simple object to demonstrate
class Example:
    pass

obj = Example()

# Set attribute dynamically
setattr(obj, 'name', 'Alice')
setattr(obj, 'age', 25)

print(f"  obj.name: {obj.name}")
print(f"  obj.age: {obj.age}")

print("\n  setattr() sets attribute value dynamically")

print()  # Empty line


# ============================================================================
# 9. __all__ ATTRIBUTE
# ============================================================================
print("=" * 60)
print("9. __all__ ATTRIBUTE")
print("=" * 60)

# Check if module has __all__
import math
has_all = hasattr(math, '__all__')
print(f"  hasattr(math, '__all__'): {has_all}")

if has_all:
    print(f"  math.__all__: {math.__all__}")

print("\n  __all__ defines what 'from module import *' imports")
print("  If not defined, imports all names not starting with _")

print()  # Empty line


# ============================================================================
# 10. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("10. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Check module info
import math
print("  Module information:")
print(f"    Name: {math.__name__}")
print(f"    File: {math.__file__}")
print(f"    Has pi: {hasattr(math, 'pi')}")
print(f"    Pi value: {getattr(math, 'pi')}")

# Example 2: Dynamic attribute access
function_name = 'sqrt'
if hasattr(math, function_name):
    func = getattr(math, function_name)
    result = func(16)
    print(f"  Dynamic call: {function_name}(16) = {result}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("MODULE ATTRIBUTES SUMMARY:")
print("=" * 60)
print("Key Attributes:")
print("  - __name__: Module name")
print("  - __file__: File path")
print("  - __doc__: Documentation string")
print("  - __dict__: Namespace dictionary")
print("  - __all__: Public exports list")
print("\nUseful Functions:")
print("  - dir(obj): List attributes")
print("  - hasattr(obj, name): Check if attribute exists")
print("  - getattr(obj, name): Get attribute value")
print("  - setattr(obj, name, value): Set attribute value")
print("=" * 60)

