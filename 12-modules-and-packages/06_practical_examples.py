"""
Practical Module and Package Examples

This file demonstrates real-world examples of using modules and packages
to organize and structure Python code.
"""

# ============================================================================
# 1. UTILITY MODULE EXAMPLE
# ============================================================================
print("=" * 60)
print("1. UTILITY MODULE EXAMPLE")
print("=" * 60)

# Simulated utility module functions
def format_currency(amount):
    """Format amount as currency."""
    return f"${amount:.2f}"

def calculate_percentage(value, total):
    """Calculate percentage."""
    if total == 0:
        return 0
    return (value / total) * 100

def validate_email(email):
    """Simple email validation."""
    return "@" in email and "." in email

# Use the utilities
price = 99.99
print(f"  Price: {format_currency(price)}")

score = 85
total = 100
percentage = calculate_percentage(score, total)
print(f"  Score: {score}/{total} = {percentage:.1f}%")

email = "user@example.com"
print(f"  Email valid: {validate_email(email)}")

print("\n  This demonstrates a utility module pattern")

print()  # Empty line


# ============================================================================
# 2. CONFIGURATION MODULE
# ============================================================================
print("=" * 60)
print("2. CONFIGURATION MODULE")
print("=" * 60)

# Simulated config module
APP_NAME = "My Application"
VERSION = "1.0.0"
DEBUG = True
DATABASE_URL = "sqlite:///app.db"
MAX_CONNECTIONS = 100

print(f"  APP_NAME: {APP_NAME}")
print(f"  VERSION: {VERSION}")
print(f"  DEBUG: {DEBUG}")
print(f"  DATABASE_URL: {DATABASE_URL}")
print(f"  MAX_CONNECTIONS: {MAX_CONNECTIONS}")

print("\n  Configuration modules store app settings")

print()  # Empty line


# ============================================================================
# 3. DATA PROCESSING MODULE
# ============================================================================
print("=" * 60)
print("3. DATA PROCESSING MODULE")
print("=" * 60)

# Simulated data processing functions
def process_numbers(numbers):
    """Process list of numbers."""
    return {
        'sum': sum(numbers),
        'average': sum(numbers) / len(numbers) if numbers else 0,
        'max': max(numbers) if numbers else None,
        'min': min(numbers) if numbers else None
    }

def filter_even(numbers):
    """Filter even numbers."""
    return [n for n in numbers if n % 2 == 0]

# Use the functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stats = process_numbers(numbers)
print(f"  Numbers: {numbers}")
print(f"  Statistics: {stats}")

evens = filter_even(numbers)
print(f"  Even numbers: {evens}")

print()  # Empty line


# ============================================================================
# 4. USING STANDARD LIBRARY MODULES
# ============================================================================
print("=" * 60)
print("4. USING STANDARD LIBRARY MODULES")
print("=" * 60)

import json
from datetime import datetime
import os

# JSON processing
data = {"name": "Alice", "age": 25, "timestamp": str(datetime.now())}
json_str = json.dumps(data, indent=2)
print("  JSON data:")
print(json_str)

# File operations
current_dir = os.getcwd()
print(f"  Current directory: {current_dir}")

print()  # Empty line


# ============================================================================
# 5. MODULE WITH CLASSES
# ============================================================================
print("=" * 60)
print("5. MODULE WITH CLASSES")
print("=" * 60)

# Simulated module with classes
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def __str__(self):
        return f"User(name={self.name}, email={self.email})"

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"Product(name={self.name}, price=${self.price:.2f})"

# Use the classes
user = User("Alice", "alice@example.com")
product = Product("Laptop", 999.99)

print(f"  {user}")
print(f"  {product}")

print("\n  Modules can contain classes for object-oriented code")

print()  # Empty line


# ============================================================================
# 6. PACKAGE STRUCTURE EXAMPLE
# ============================================================================
print("=" * 60)
print("6. PACKAGE STRUCTURE EXAMPLE")
print("=" * 60)

print("  Example package structure:")
print("    ")
print("    myapp/")
print("        __init__.py")
print("        config.py          # Configuration")
print("        utils.py            # Utilities")
print("        models/             # Data models")
print("            __init__.py")
print("            user.py")
print("            product.py")
print("        services/           # Business logic")
print("            __init__.py")
print("            auth.py")
print("            payment.py")
print("  ")
print("  Usage:")
print("    from myapp import config")
print("    from myapp.models import user")
print("    from myapp.services import auth")

print()  # Empty line


# ============================================================================
# 7. MODULE WITH __main__ BLOCK
# ============================================================================
print("=" * 60)
print("7. MODULE WITH __main__ BLOCK")
print("=" * 60)

def calculate_area(radius):
    """Calculate circle area."""
    import math
    return math.pi * radius ** 2

# This runs only when module is executed directly
if __name__ == "__main__":
    print("  Running as main script")
    area = calculate_area(5)
    print(f"  Circle area (r=5): {area:.2f}")
else:
    print("  Imported as module")

print("\n  Allows module to be both imported and run directly")

print()  # Empty line


# ============================================================================
# 8. ERROR HANDLING WITH MODULES
# ============================================================================
print("=" * 60)
print("8. ERROR HANDLING WITH MODULES")
print("=" * 60)

# Try importing optional module
try:
    import optional_module
    print("  Optional module imported")
except ImportError:
    print("  Optional module not available, using fallback")
    # Define fallback
    class OptionalModule:
        @staticmethod
        def function():
            return "Fallback implementation"
    optional_module = OptionalModule()

result = optional_module.function()
print(f"  Result: {result}")

print("\n  Always handle ImportError for optional dependencies")

print()  # Empty line


# ============================================================================
# 9. MODULE DOCUMENTATION
# ============================================================================
print("=" * 60)
print("9. MODULE DOCUMENTATION")
print("=" * 60)

"""
Example module documentation.

This module provides utility functions for common tasks.

Functions:
    format_currency: Format number as currency
    calculate_percentage: Calculate percentage
    validate_email: Validate email format

Classes:
    User: Represents a user
    Product: Represents a product

Example:
    >>> from my_module import format_currency
    >>> format_currency(99.99)
    '$99.99'
"""

print("  Module docstring example shown above")
print("  Access with: module_name.__doc__")

print()  # Empty line


# ============================================================================
# 10. BEST PRACTICES SUMMARY
# ============================================================================
print("=" * 60)
print("10. BEST PRACTICES SUMMARY")
print("=" * 60)

print("  Module Best Practices:")
print("    1. Use descriptive names")
print("    2. Write docstrings")
print("    3. Use __all__ to control exports")
print("    4. Use if __name__ == '__main__' for testing")
print("    5. Keep modules focused (single responsibility)")
print("    6. Organize imports: stdlib, third-party, local")
print("    7. Handle ImportError for optional modules")
print("    8. Use packages to organize related modules")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL MODULE EXAMPLES SUMMARY:")
print("=" * 60)
print("Key Applications:")
print("  - Utility modules: Common functions")
print("  - Configuration modules: App settings")
print("  - Data processing: Transform and analyze data")
print("  - Class modules: Object-oriented code")
print("  - Package organization: Structure large projects")
print("\nRemember:")
print("  - Modules organize code logically")
print("  - Packages organize multiple modules")
print("  - Use standard library modules when possible")
print("  - Document your modules")
print("  - Follow best practices")
print("=" * 60)

