"""
Basic Variables in Python

This file demonstrates the fundamentals of creating and using variables.
Variables are the building blocks of any program - they store data for later use.
"""

# ============================================================================
# 1. CREATING VARIABLES
# ============================================================================
print("=" * 60)
print("1. CREATING VARIABLES")
print("=" * 60)

# Assign a value to a variable using the = operator
name = "Alice"
age = 25
height = 5.6

# Print the variables
print("Name:", name)
print("Age:", age)
print("Height:", height)

print()  # Empty line for spacing


# ============================================================================
# 2. VARIABLE REASSIGNMENT
# ============================================================================
print("=" * 60)
print("2. VARIABLE REASSIGNMENT")
print("=" * 60)

# Variables can be reassigned with new values
x = 10
print("Initial value of x:", x)

x = 20
print("After reassignment, x:", x)

x = "Now I'm a string!"
print("After another reassignment, x:", x)
print("Type of x:", type(x))

print()  # Empty line


# ============================================================================
# 3. MULTIPLE ASSIGNMENT
# ============================================================================
print("=" * 60)
print("3. MULTIPLE ASSIGNMENT")
print("=" * 60)

# Assign multiple variables in one line
x, y, z = 1, 2, 3
print(f"x = {x}, y = {y}, z = {z}")

# Assign same value to multiple variables
a = b = c = 0
print(f"a = {a}, b = {b}, c = {c}")

# Swap two variables (elegant Python feature!)
first = "Hello"
second = "World"
print(f"Before swap: first = {first}, second = {second}")

first, second = second, first
print(f"After swap: first = {first}, second = {second}")

print()  # Empty line


# ============================================================================
# 4. USING VARIABLES IN EXPRESSIONS
# ============================================================================
print("=" * 60)
print("4. USING VARIABLES IN EXPRESSIONS")
print("=" * 60)

# Use variables in calculations
price = 19.99
quantity = 3
total = price * quantity

print(f"Price: ${price}")
print(f"Quantity: {quantity}")
print(f"Total: ${total}")

# Use variables in string operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

print()  # Empty line


# ============================================================================
# 5. VARIABLE NAMING EXAMPLES
# ============================================================================
print("=" * 60)
print("5. VARIABLE NAMING EXAMPLES")
print("=" * 60)

# Good variable names (descriptive and clear)
user_name = "alice123"
user_age = 25
is_active = True
total_items = 100

print("Good variable names:")
print(f"  user_name: {user_name}")
print(f"  user_age: {user_age}")
print(f"  is_active: {is_active}")
print(f"  total_items: {total_items}")

# Constants (convention: UPPER_CASE)
PI = 3.14159
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30

print("\nConstants:")
print(f"  PI: {PI}")
print(f"  MAX_CONNECTIONS: {MAX_CONNECTIONS}")
print(f"  DEFAULT_TIMEOUT: {DEFAULT_TIMEOUT}")

print()  # Empty line


# ============================================================================
# 6. VARIABLES IN DIFFERENT CONTEXTS
# ============================================================================
print("=" * 60)
print("6. VARIABLES IN DIFFERENT CONTEXTS")
print("=" * 60)

# Store calculation results
radius = 5
area = 3.14159 * radius ** 2
print(f"Circle with radius {radius} has area {area:.2f}")

# Store user information
user = {
    "name": "Alice",
    "email": "alice@example.com",
    "age": 25
}
print(f"User: {user['name']}, Email: {user['email']}")

# Store boolean flags
is_logged_in = True
has_permission = False
print(f"Logged in: {is_logged_in}, Has permission: {has_permission}")

print()  # Empty line


# ============================================================================
# 7. VARIABLE LIFETIME
# ============================================================================
print("=" * 60)
print("7. VARIABLE LIFETIME")
print("=" * 60)

# Variables exist from the point they're created
# They persist until the program ends or they're deleted

# Create a variable
counter = 0
print(f"Counter created: {counter}")

# Modify it
counter = counter + 1
print(f"Counter after increment: {counter}")

# Delete a variable (rarely needed)
del counter
# print(counter)  # This would cause NameError: name 'counter' is not defined
print("Counter deleted (commented out print to avoid error)")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("KEY TAKEAWAYS:")
print("=" * 60)
print("1. Variables store data using the = operator")
print("2. Variables can be reassigned with new values")
print("3. Use descriptive names for variables")
print("4. Variables can be used in expressions and calculations")
print("5. Python is dynamically typed (variables can change types)")
print("=" * 60)

