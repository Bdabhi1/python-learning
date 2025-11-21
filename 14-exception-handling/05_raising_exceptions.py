"""
Raising Exceptions in Python

This file demonstrates how to raise exceptions, re-raise exceptions,
and create custom exception messages.
"""

# ============================================================================
# 1. BASIC RAISE
# ============================================================================
print("=" * 60)
print("1. BASIC RAISE")
print("=" * 60)

# Raise an exception
def check_positive(number):
    """Check if number is positive."""
    if number < 0:
        raise ValueError("Number must be positive")
    return number

try:
    result = check_positive(-5)
except ValueError as e:
    print(f"  Caught: {e}")

print("\n  raise ExceptionType('message')")

print()  # Empty line


# ============================================================================
# 2. RAISING WITH MESSAGE
# ============================================================================
print("=" * 60)
print("2. RAISING WITH MESSAGE")
print("=" * 60)

# Raise with custom message
def validate_age(age):
    """Validate age."""
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age cannot be greater than 150")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(f"  Error: {e}")

try:
    validate_age(200)
except ValueError as e:
    print(f"  Error: {e}")

print()  # Empty line


# ============================================================================
# 3. RE-RAISING EXCEPTIONS
# ============================================================================
print("=" * 60)
print("3. RE-RAISING EXCEPTIONS")
print("=" * 60)

# Re-raise the same exception
def process_data(data):
    """Process data and re-raise if error."""
    try:
        number = int(data)
        return number * 2
    except ValueError:
        print("  Logging error...")
        raise  # Re-raise the same exception

try:
    result = process_data("abc")
except ValueError as e:
    print(f"  Re-raised: {e}")

print("\n  Use 'raise' to re-raise the same exception")

print()  # Empty line


# ============================================================================
# 4. RAISING DIFFERENT EXCEPTION
# ============================================================================
print("=" * 60)
print("4. RAISING DIFFERENT EXCEPTION")
print("=" * 60)

# Catch one exception, raise another
def convert_to_int(value):
    """Convert to int, raise TypeError if fails."""
    try:
        return int(value)
    except ValueError:
        raise TypeError(f"Cannot convert '{value}' to int")

try:
    result = convert_to_int("abc")
except TypeError as e:
    print(f"  TypeError: {e}")

print("\n  Can catch one exception and raise another")

print()  # Empty line


# ============================================================================
# 5. RAISING WITH EXCEPTION CHAINING
# ============================================================================
print("=" * 60)
print("5. RAISING WITH EXCEPTION CHAINING")
print("=" * 60)

# Chain exceptions to show cause
try:
    try:
        number = int("abc")
    except ValueError as e:
        raise TypeError("Invalid type") from e
except TypeError as e:
    print(f"  TypeError: {e}")
    print(f"  Caused by: {e.__cause__}")

print("\n  raise NewException from old_exception")

print()  # Empty line


# ============================================================================
# 6. CONDITIONAL RAISING
# ============================================================================
print("=" * 60)
print("6. CONDITIONAL RAISING")
print("=" * 60)

# Raise based on conditions
def divide(a, b):
    """Divide with validation."""
    if not isinstance(a, (int, float)):
        raise TypeError("First argument must be a number")
    if not isinstance(b, (int, float)):
        raise TypeError("Second argument must be a number")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# Test different cases
test_cases = [
    (10, 2),
    (10, 0),
    ("10", 2),
    (10, "2")
]

for a, b in test_cases:
    try:
        result = divide(a, b)
        print(f"  divide({a}, {b}) = {result}")
    except (TypeError, ZeroDivisionError) as e:
        print(f"  divide({a}, {b}): {e}")

print()  # Empty line


# ============================================================================
# 7. ASSERT STATEMENTS
# ============================================================================
print("=" * 60)
print("7. ASSERT STATEMENTS")
print("=" * 60)

# Assert raises AssertionError if condition is False
def calculate_area(length, width):
    """Calculate area with assertion."""
    assert length > 0, "Length must be positive"
    assert width > 0, "Width must be positive"
    return length * width

try:
    result = calculate_area(5, 3)
    print(f"  Area: {result}")
except AssertionError as e:
    print(f"  AssertionError: {e}")

try:
    result = calculate_area(-5, 3)
except AssertionError as e:
    print(f"  AssertionError: {e}")

print("\n  assert condition, 'message'")

print()  # Empty line


# ============================================================================
# 8. RAISING IN NESTED FUNCTIONS
# ============================================================================
print("=" * 60)
print("8. RAISING IN NESTED FUNCTIONS")
print("=" * 60)

# Exception propagates up the call stack
def inner_function():
    """Inner function that raises exception."""
    raise ValueError("Error in inner function")

def outer_function():
    """Outer function that calls inner."""
    inner_function()

try:
    outer_function()
except ValueError as e:
    print(f"  Caught in outer scope: {e}")

print("\n  Exceptions propagate up the call stack")

print()  # Empty line


# ============================================================================
# 9. PRACTICAL EXAMPLE: VALIDATION
# ============================================================================
print("=" * 60)
print("9. PRACTICAL EXAMPLE: VALIDATION")
print("=" * 60)

def validate_user(username, email, age):
    """Validate user data."""
    errors = []
    
    if not username or len(username) < 3:
        raise ValueError("Username must be at least 3 characters")
    
    if "@" not in email:
        raise ValueError("Invalid email format")
    
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age < 13:
        raise ValueError("Age must be at least 13")
    
    return True

# Test validation
test_users = [
    ("alice", "alice@example.com", 25),
    ("ab", "alice@example.com", 25),  # Short username
    ("alice", "invalid", 25),  # Invalid email
    ("alice", "alice@example.com", -5),  # Negative age
]

for username, email, age in test_users:
    try:
        validate_user(username, email, age)
        print(f"  Valid: {username}")
    except ValueError as e:
        print(f"  Invalid: {e}")

print()  # Empty line


# ============================================================================
# 10. BEST PRACTICES
# ============================================================================
print("=" * 60)
print("10. BEST PRACTICES")
print("=" * 60)

print("  When raising exceptions:")
print("    1. Use appropriate exception type")
print("    2. Provide clear, helpful messages")
print("    3. Raise early, catch late")
print("    4. Don't raise generic Exception")
print("    5. Document exceptions in docstrings")
print("    6. Use exception chaining when appropriate")

print("\n  Example:")
print("    def function():")
print("        \"\"\"")
print("        Raises:")
print("            ValueError: If input is invalid")
print("            TypeError: If wrong type")
print("        \"\"\"")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("RAISING EXCEPTIONS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - raise ExceptionType('message') - Raise exception")
print("  - raise - Re-raise current exception")
print("  - raise NewException from old - Chain exceptions")
print("  - assert condition, 'message' - Assert with message")
print("  - Exceptions propagate up call stack")
print("\nBest Practices:")
print("  - Use appropriate exception types")
print("  - Provide clear error messages")
print("  - Raise early for validation")
print("  - Document exceptions in docstrings")
print("=" * 60)

