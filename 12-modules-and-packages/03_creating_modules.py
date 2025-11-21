"""
Creating Your Own Modules in Python

This file demonstrates how to create and use your own modules.
Modules help organize code into reusable components.
"""

# ============================================================================
# 1. CREATING A SIMPLE MODULE
# ============================================================================
print("=" * 60)
print("1. CREATING A SIMPLE MODULE")
print("=" * 60)

# Create a simple calculator module (simulated)
# In practice, this would be in a separate file: calculator.py
print("  Example: calculator.py")
print("    def add(a, b):")
print("        return a + b")
print("    ")
print("    def subtract(a, b):")
print("        return a - b")

# Simulate using the module
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Use the functions
result1 = add(5, 3)
result2 = subtract(10, 4)
print(f"  add(5, 3) = {result1}")
print(f"  subtract(10, 4) = {result2}")

print("\n  To use: import calculator")
print("  Then: calculator.add(5, 3)")

print()  # Empty line


# ============================================================================
# 2. MODULE WITH VARIABLES
# ============================================================================
print("=" * 60)
print("2. MODULE WITH VARIABLES")
print("=" * 60)

# Module can contain variables (simulated)
# config.py example
APP_NAME = "My Application"
VERSION = "1.0.0"
DEBUG = True

print(f"  APP_NAME: {APP_NAME}")
print(f"  VERSION: {VERSION}")
print(f"  DEBUG: {DEBUG}")

print("\n  Access with: import config")
print("  Then: config.APP_NAME")

print()  # Empty line


# ============================================================================
# 3. MODULE WITH CLASSES
# ============================================================================
print("=" * 60)
print("3. MODULE WITH CLASSES")
print("=" * 60)

# Module can contain classes (simulated)
class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, value):
        self.result += value
        return self.result
    
    def reset(self):
        self.result = 0

# Use the class
calc = Calculator()
print(f"  calc.add(5): {calc.add(5)}")
print(f"  calc.add(3): {calc.add(3)}")
print(f"  calc.result: {calc.result}")

print("\n  Import and use: from my_module import Calculator")

print()  # Empty line


# ============================================================================
# 4. MODULE DOCUMENTATION
# ============================================================================
print("=" * 60)
print("4. MODULE DOCUMENTATION")
print("=" * 60)

# Module docstring (simulated)
"""
This module provides utility functions for calculations.

Functions:
    add: Add two numbers
    subtract: Subtract two numbers
    multiply: Multiply two numbers
"""

print("  Module docstring:")
print("    \"\"\"")
print("    This module provides utility functions.")
print("    \"\"\"")

print("\n  Access with: module_name.__doc__")

print()  # Empty line


# ============================================================================
# 5. __name__ AND __main__
# ============================================================================
print("=" * 60)
print("5. __name__ AND __main__")
print("=" * 60)

# Check __name__
print(f"  Current __name__: {__name__}")

# Example function
def greet(name):
    return f"Hello, {name}!"

# Code that runs only when module is executed directly
if __name__ == "__main__":
    print(f"  Running as main: {greet('World')}")
    print("  This code runs only when file is executed directly")
else:
    print("  Running as imported module")
    print("  This code runs when module is imported")

print("\n  Use: if __name__ == '__main__':")
print("  Allows module to be both imported and run directly")

print()  # Empty line


# ============================================================================
# 6. MODULE ATTRIBUTES
# ============================================================================
print("=" * 60)
print("6. MODULE ATTRIBUTES")
print("=" * 60)

import math

# Common module attributes
print(f"  math.__name__: {math.__name__}")
print(f"  math.__file__: {math.__file__}")
print(f"  math.__doc__: {math.__doc__[:50]}...")

print("\n  Every module has:")
print("    __name__: Module name")
print("    __file__: File path")
print("    __doc__: Documentation string")

print()  # Empty line


# ============================================================================
# 7. CONTROLLING EXPORTS
# ============================================================================
print("=" * 60)
print("7. CONTROLLING EXPORTS")
print("=" * 60)

# Define what gets imported with "from module import *"
# In module file:
__all__ = ['add', 'subtract', 'multiply']

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def _private_function():
    """Private function (starts with underscore)."""
    return "This is private"

print("  __all__ = ['add', 'subtract', 'multiply']")
print("  Controls what 'from module import *' imports")
print("  Functions starting with _ are considered private")

print()  # Empty line


# ============================================================================
# 8. RELOADING MODULES
# ============================================================================
print("=" * 60)
print("8. RELOADING MODULES")
print("=" * 60)

import importlib

# Reload a module (useful during development)
print("  import importlib")
print("  importlib.reload(module_name)")

print("\n  Note: Normally modules are imported once")
print("  Use reload() to reload during development")

print()  # Empty line


# ============================================================================
# 9. MODULE ORGANIZATION
# ============================================================================
print("=" * 60)
print("9. MODULE ORGANIZATION")
print("=" * 60)

print("  Good module structure:")
print("    1. Module docstring")
print("    2. Imports")
print("    3. Constants")
print("    4. Classes")
print("    5. Functions")
print("    6. if __name__ == '__main__':")

print("\n  Example structure:")
print("    \"\"\"Module docstring\"\"\"")
print("    ")
print("    import os")
print("    ")
print("    CONSTANT = 'value'")
print("    ")
print("    class MyClass:")
print("        pass")
print("    ")
print("    def my_function():")
print("        pass")
print("    ")
print("    if __name__ == '__main__':")
print("        pass")

print()  # Empty line


# ============================================================================
# 10. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("10. PRACTICAL EXAMPLES")
print("=" * 60)

# Example: Utility module
def format_currency(amount):
    """Format amount as currency."""
    return f"${amount:.2f}"

def calculate_tax(amount, rate=0.08):
    """Calculate tax on amount."""
    return amount * rate

# Use the functions
price = 100.50
tax = calculate_tax(price)
total = price + tax

print(f"  Price: {format_currency(price)}")
print(f"  Tax: {format_currency(tax)}")
print(f"  Total: {format_currency(total)}")

print("\n  This demonstrates a utility module pattern")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("CREATING MODULES SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - A module is just a .py file")
print("  - Can contain functions, classes, variables")
print("  - Use docstrings to document modules")
print("  - Use __name__ == '__main__' for test code")
print("  - Use __all__ to control exports")
print("  - Organize code logically")
print("\nBest Practices:")
print("  - Write clear docstrings")
print("  - Use descriptive names")
print("  - Keep modules focused (single responsibility)")
print("  - Use if __name__ == '__main__' for testing")
print("=" * 60)

