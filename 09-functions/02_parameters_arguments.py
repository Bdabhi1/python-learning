"""
Function Parameters and Arguments

This file demonstrates different ways to pass arguments to functions:
positional, keyword, and mixed arguments.
"""

# ============================================================================
# 1. POSITIONAL ARGUMENTS
# ============================================================================
print("=" * 60)
print("1. POSITIONAL ARGUMENTS")
print("=" * 60)

def greet(name, age, city):
    """Greet with name, age, and city."""
    print(f"  {name}, {age} years old, lives in {city}")

# Positional arguments (order matters)
print("  Positional arguments:")
greet("Alice", 25, "New York")
greet("Bob", 30, "London")

print("\n  Arguments are matched by position")

print()  # Empty line


# ============================================================================
# 2. KEYWORD ARGUMENTS
# ============================================================================
print("=" * 60)
print("2. KEYWORD ARGUMENTS")
print("=" * 60)

def greet(name, age, city):
    """Greet with name, age, and city."""
    print(f"  {name}, {age} years old, lives in {city}")

# Keyword arguments (order doesn't matter)
print("  Keyword arguments:")
greet(name="Alice", age=25, city="New York")
greet(city="London", name="Bob", age=30)

print("\n  Order doesn't matter with keyword arguments")

print()  # Empty line


# ============================================================================
# 3. MIXED ARGUMENTS
# ============================================================================
print("=" * 60)
print("3. MIXED ARGUMENTS")
print("=" * 60)

def greet(name, age, city):
    """Greet with name, age, and city."""
    print(f"  {name}, {age} years old, lives in {city}")

# Mix positional and keyword
print("  Mixed arguments:")
greet("Alice", age=25, city="New York")
greet("Bob", 30, city="London")

print("\n  Positional arguments must come before keyword arguments")

print()  # Empty line


# ============================================================================
# 4. PARAMETER ORDER
# ============================================================================
print("=" * 60)
print("4. PARAMETER ORDER")
print("=" * 60)

def calculate(price, quantity, discount=0, tax=0.08):
    """Calculate total with discount and tax."""
    subtotal = price * quantity
    after_discount = subtotal * (1 - discount)
    total = after_discount * (1 + tax)
    return total

# Different ways to call
result1 = calculate(10, 2)
print(f"  calculate(10, 2): ${result1:.2f}")

result2 = calculate(10, 2, discount=0.1)
print(f"  calculate(10, 2, discount=0.1): ${result2:.2f}")

result3 = calculate(10, 2, tax=0.1)
print(f"  calculate(10, 2, tax=0.1): ${result3:.2f}")

result4 = calculate(10, 2, discount=0.1, tax=0.1)
print(f"  calculate(10, 2, discount=0.1, tax=0.1): ${result4:.2f}")

print()  # Empty line


# ============================================================================
# 5. REQUIRED VS OPTIONAL PARAMETERS
# ============================================================================
print("=" * 60)
print("5. REQUIRED VS OPTIONAL PARAMETERS")
print("=" * 60)

def create_user(username, email, age=None, city=None):
    """Create user with required and optional parameters."""
    user = {"username": username, "email": email}
    if age is not None:
        user["age"] = age
    if city is not None:
        user["city"] = city
    return user

# Required parameters only
user1 = create_user("alice", "alice@example.com")
print(f"  User 1: {user1}")

# With optional parameters
user2 = create_user("bob", "bob@example.com", age=25, city="NYC")
print(f"  User 2: {user2}")

print()  # Empty line


# ============================================================================
# 6. PARAMETER VALIDATION
# ============================================================================
print("=" * 60)
print("6. PARAMETER VALIDATION")
print("=" * 60)

def divide(a, b):
    """Divide two numbers with validation."""
    if b == 0:
        return None  # Or raise ValueError
    return a / b

result1 = divide(10, 2)
print(f"  divide(10, 2) = {result1}")

result2 = divide(10, 0)
print(f"  divide(10, 0) = {result2}")

def calculate_age(birth_year, current_year=2024):
    """Calculate age with validation."""
    if birth_year > current_year:
        return None
    return current_year - birth_year

age = calculate_age(1999)
print(f"  calculate_age(1999) = {age}")

print()  # Empty line


# ============================================================================
# 7. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("7. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Format name
print("Example 1: Format Name")
def format_name(first, last, middle=None, title=""):
    """Format a person's name."""
    name_parts = []
    if title:
        name_parts.append(title)
    name_parts.append(first)
    if middle:
        name_parts.append(middle)
    name_parts.append(last)
    return " ".join(name_parts)

name1 = format_name("John", "Doe")
print(f"  format_name('John', 'Doe'): {name1}")

name2 = format_name("John", "Doe", middle="Michael", title="Dr.")
print(f"  format_name('John', 'Doe', middle='Michael', title='Dr.'): {name2}")

# Example 2: Send message
print("\nExample 2: Send Message")
def send_message(to, message, subject="No Subject", priority="normal"):
    """Send a message with optional parameters."""
    print(f"    To: {to}")
    print(f"    Subject: {subject}")
    print(f"    Priority: {priority}")
    print(f"    Message: {message}")

send_message("alice@example.com", "Hello!")
print()
send_message("bob@example.com", "Important!", subject="Urgent", priority="high")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PARAMETERS AND ARGUMENTS SUMMARY:")
print("=" * 60)
print("Argument Types:")
print("  - Positional: Arguments matched by position")
print("  - Keyword: Arguments matched by name")
print("  - Mixed: Positional then keyword")
print("\nRules:")
print("  - Positional arguments must come before keyword arguments")
print("  - Required parameters must come before optional")
print("  - Order matters for positional, not for keyword")
print("\nBest Practices:")
print("  - Use keyword arguments for clarity")
print("  - Use default parameters for optional values")
print("  - Validate parameters when needed")
print("=" * 60)

