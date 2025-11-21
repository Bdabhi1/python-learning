"""
Comments in Python - Examples and Best Practices

This file demonstrates how to write effective comments in Python.
Comments are essential for explaining your code to others (and yourself later!).
"""

# ============================================================================
# SINGLE-LINE COMMENTS
# ============================================================================

# This is a single-line comment
# Comments start with a hash symbol (#)
# Everything after # on that line is ignored by Python

print("Hello")  # This is an inline comment

# You can comment out code to disable it temporarily
# print("This won't run")


# ============================================================================
# MULTI-LINE COMMENTS
# ============================================================================

"""
This is a multi-line comment using triple double quotes.
It can span multiple lines.
Python treats this as a string, but if it's not assigned to a variable,
it's effectively a comment.

This is commonly used for:
- Module documentation
- Function documentation (docstrings)
- Long explanations
"""

'''
This is also a multi-line comment using triple single quotes.
Both triple single quotes and triple double quotes work the same way.
'''


# ============================================================================
# DOCSTRINGS (SPECIAL TYPE OF COMMENT)
# ============================================================================

def example_function():
    """
    This is a docstring - a special comment that documents a function.
    
    Docstrings are used to explain:
    - What the function does
    - What parameters it takes
    - What it returns
    
    They can be accessed using help() or .__doc__
    """
    return "This function does something"


# ============================================================================
# GOOD COMMENT PRACTICES
# ============================================================================

# GOOD: Explains WHY, not WHAT
# We use a list here because we need to modify the collection
items = []

# BAD: States the obvious (code already shows this)
# items = []  # This creates an empty list

# GOOD: Explains complex logic
# Calculate compound interest using the formula: A = P(1 + r/n)^(nt)
principal = 1000
rate = 0.05
time = 5
amount = principal * (1 + rate) ** time

# GOOD: Warns about potential issues
# WARNING: This function modifies the original list
def add_item(lst, item):
    lst.append(item)


# ============================================================================
# COMMENTING OUT CODE
# ============================================================================

# Sometimes you want to temporarily disable code
# old_code = "This won't run"
new_code = "This will run"

# Or comment out multiple lines
# if condition:
#     do_something()
#     do_something_else()


# ============================================================================
# SECTION HEADERS (ORGANIZING CODE)
# ============================================================================

# ============================================================================
# SECTION 1: VARIABLE DECLARATIONS
# ============================================================================
name = "Python"
version = 3.11

# ============================================================================
# SECTION 2: FUNCTION DEFINITIONS
# ============================================================================
def greet(name):
    """Greets a person by name."""
    return f"Hello, {name}!"


# ============================================================================
# PRACTICAL EXAMPLE: WELL-COMMENTED CODE
# ============================================================================

def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI).
    
    Formula: BMI = weight (kg) / height (m)²
    
    Args:
        weight_kg: Weight in kilograms
        height_m: Height in meters
    
    Returns:
        BMI value as a float
    """
    # Validate inputs to prevent division by zero or negative values
    if height_m <= 0:
        raise ValueError("Height must be positive")
    if weight_kg < 0:
        raise ValueError("Weight cannot be negative")
    
    # Calculate and return BMI
    bmi = weight_kg / (height_m ** 2)
    return bmi


# Example usage
if __name__ == "__main__":
    # Test the function
    my_weight = 70  # kg
    my_height = 1.75  # meters
    
    my_bmi = calculate_bmi(my_weight, my_height)
    print(f"BMI: {my_bmi:.2f}")


# ============================================================================
# SUMMARY
# ============================================================================
"""
COMMENT BEST PRACTICES:

1. Write comments that explain WHY, not WHAT
2. Keep comments up-to-date with code changes
3. Use docstrings for functions and classes
4. Don't over-comment obvious code
5. Use comments to organize code into sections
6. Comment complex algorithms or business logic
7. Use clear, concise language
8. Remove commented-out code before committing (use version control instead)
"""

