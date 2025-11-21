"""
Basic Functions in Python

This file demonstrates how to define and call functions - the building
blocks of organized Python programs.
"""

# ============================================================================
# 1. DEFINING A FUNCTION
# ============================================================================
print("=" * 60)
print("1. DEFINING A FUNCTION")
print("=" * 60)

# Basic function definition
def greet():
    """Simple function that prints a greeting."""
    print("  Hello, World!")

# Call the function
print("  Calling greet():")
greet()

print("\n  Structure:")
print("    def function_name():")
print("        # Function body")
print("        pass")

print()  # Empty line


# ============================================================================
# 2. FUNCTION WITH PARAMETERS
# ============================================================================
print("=" * 60)
print("2. FUNCTION WITH PARAMETERS")
print("=" * 60)

# Function that takes a parameter
def greet_person(name):
    """Greet a specific person."""
    print(f"  Hello, {name}!")

# Call with argument
print("  Calling greet_person('Alice'):")
greet_person("Alice")

print("  Calling greet_person('Bob'):")
greet_person("Bob")

print("\n  Parameters receive values when function is called")

print()  # Empty line


# ============================================================================
# 3. FUNCTION WITH MULTIPLE PARAMETERS
# ============================================================================
print("=" * 60)
print("3. FUNCTION WITH MULTIPLE PARAMETERS")
print("=" * 60)

# Function with multiple parameters
def introduce(name, age, city):
    """Introduce a person with their details."""
    print(f"  {name} is {age} years old and lives in {city}")

# Call with multiple arguments
print("  Calling introduce('Alice', 25, 'New York'):")
introduce("Alice", 25, "New York")

print("\n  Arguments are passed in order (positional)")

print()  # Empty line


# ============================================================================
# 4. FUNCTION WITH RETURN VALUE
# ============================================================================
print("=" * 60)
print("4. FUNCTION WITH RETURN VALUE")
print("=" * 60)

# Function that returns a value
def add(a, b):
    """Add two numbers and return the result."""
    return a + b

# Call and use return value
result = add(3, 5)
print(f"  add(3, 5) = {result}")

result2 = add(10, 20)
print(f"  add(10, 20) = {result2}")

# Use in expression
total = add(5, 3) * 2
print(f"  add(5, 3) * 2 = {total}")

print("\n  Use 'return' to send a value back")

print()  # Empty line


# ============================================================================
# 5. FUNCTION DOCSTRINGS
# ============================================================================
print("=" * 60)
print("5. FUNCTION DOCSTRINGS")
print("=" * 60)

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle
        width: The width of the rectangle
    
    Returns:
        The area of the rectangle
    """
    return length * width

# Access docstring
print("  Docstring:")
print(f"    {calculate_area.__doc__}")

# Use function
area = calculate_area(5, 3)
print(f"\n  calculate_area(5, 3) = {area}")

print("\n  Docstrings document what the function does")

print()  # Empty line


# ============================================================================
# 6. CALLING FUNCTIONS
# ============================================================================
print("=" * 60)
print("6. CALLING FUNCTIONS")
print("=" * 60)

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

# Call and store result
result = multiply(4, 5)
print(f"  multiply(4, 5) = {result}")

# Call in expression
total = multiply(2, 3) + multiply(4, 5)
print(f"  multiply(2, 3) + multiply(4, 5) = {total}")

# Call and print directly
print(f"  multiply(6, 7) = {multiply(6, 7)}")

print()  # Empty line


# ============================================================================
# 7. FUNCTIONS WITHOUT RETURN
# ============================================================================
print("=" * 60)
print("7. FUNCTIONS WITHOUT RETURN")
print("=" * 60)

def print_info(name, age):
    """Print information (no return value)."""
    print(f"  Name: {name}, Age: {age}")

# Call function
print("  Calling print_info('Alice', 25):")
print_info("Alice", 25)

# Functions without return return None
result = print_info("Bob", 30)
print(f"  Return value: {result}")

print("\n  Functions without 'return' return None")

print()  # Empty line


# ============================================================================
# 8. REUSING FUNCTIONS
# ============================================================================
print("=" * 60)
print("8. REUSING FUNCTIONS")
print("=" * 60)

def square(x):
    """Calculate square of a number."""
    return x * x

# Use multiple times with different values
print("  Calculating squares:")
print(f"    square(2) = {square(2)}")
print(f"    square(5) = {square(5)}")
print(f"    square(10) = {square(10)}")

# Use in loop
print("\n  Squares of 1-5:")
for i in range(1, 6):
    print(f"    square({i}) = {square(i)}")

print("\n  Functions can be called multiple times!")

print()  # Empty line


# ============================================================================
# 9. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("9. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Temperature converter
print("Example 1: Temperature Converter")
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"  {temp_c}°C = {temp_f}°F")

# Example 2: Calculate total
print("\nExample 2: Calculate Total")
def calculate_total(price, quantity, tax_rate=0.08):
    """Calculate total with tax."""
    subtotal = price * quantity
    tax = subtotal * tax_rate
    return subtotal + tax

total = calculate_total(19.99, 3)
print(f"  Total for 3 items at $19.99: ${total:.2f}")

# Example 3: Check eligibility
print("\nExample 3: Check Eligibility")
def is_eligible(age, min_age=18):
    """Check if person is eligible."""
    return age >= min_age

print(f"  Age 20 eligible: {is_eligible(20)}")
print(f"  Age 15 eligible: {is_eligible(15)}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("BASIC FUNCTIONS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Use 'def' keyword to define functions")
print("  - Function name followed by parentheses")
print("  - Parameters go inside parentheses")
print("  - Function body is indented")
print("  - Use 'return' to send value back")
print("  - Call function with function_name()")
print("  - Functions can be called multiple times")
print("  - Use docstrings to document functions")
print("\nBenefits:")
print("  - Reusability: Write once, use many times")
print("  - Modularity: Break code into logical pieces")
print("  - Readability: Code is easier to understand")
print("=" * 60)

