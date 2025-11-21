"""
Practical Function Examples

This file demonstrates real-world examples combining all function
concepts to solve common programming problems.
"""

# ============================================================================
# 1. CALCULATOR FUNCTIONS
# ============================================================================
print("=" * 60)
print("1. CALCULATOR FUNCTIONS")
print("=" * 60)

def calculate(operation, *numbers, precision=2):
    """Perform calculation with variable arguments."""
    if not numbers:
        return None
    
    if operation == "add":
        result = sum(numbers)
    elif operation == "multiply":
        result = 1
        for num in numbers:
            result *= num
    elif operation == "average":
        result = sum(numbers) / len(numbers)
    else:
        return None
    
    return round(result, precision)

print(f"  calculate('add', 1, 2, 3, 4): {calculate('add', 1, 2, 3, 4)}")
print(f"  calculate('multiply', 2, 3, 4): {calculate('multiply', 2, 3, 4)}")
print(f"  calculate('average', 10, 20, 30): {calculate('average', 10, 20, 30)}")

print()  # Empty line


# ============================================================================
# 2. DATA VALIDATION FUNCTIONS
# ============================================================================
print("=" * 60)
print("2. DATA VALIDATION FUNCTIONS")
print("=" * 60)

def validate_user(username, email, age=None, min_age=13):
    """Validate user data."""
    errors = []
    
    if not username or len(username) < 3:
        errors.append("Username must be at least 3 characters")
    
    if "@" not in email:
        errors.append("Invalid email format")
    
    if age is not None:
        if age < min_age:
            errors.append(f"Age must be at least {min_age}")
    
    return len(errors) == 0, errors

valid, errors = validate_user("alice", "alice@example.com", age=25)
print(f"  validate_user('alice', 'alice@example.com', age=25):")
print(f"    Valid: {valid}, Errors: {errors}")

valid, errors = validate_user("ab", "invalid", age=10)
print(f"\n  validate_user('ab', 'invalid', age=10):")
print(f"    Valid: {valid}, Errors: {errors}")

print()  # Empty line


# ============================================================================
# 3. DATA PROCESSING FUNCTIONS
# ============================================================================
print("=" * 60)
print("3. DATA PROCESSING FUNCTIONS")
print("=" * 60)

def process_numbers(numbers, operation="sum", filter_func=None):
    """Process list of numbers with optional filtering."""
    if filter_func:
        numbers = [n for n in numbers if filter_func(n)]
    
    if not numbers:
        return None
    
    if operation == "sum":
        return sum(numbers)
    elif operation == "average":
        return sum(numbers) / len(numbers)
    elif operation == "max":
        return max(numbers)
    elif operation == "min":
        return min(numbers)
    else:
        return None

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"  Numbers: {numbers}")

result1 = process_numbers(numbers, "sum")
print(f"  Sum: {result1}")

result2 = process_numbers(numbers, "average", filter_func=lambda x: x % 2 == 0)
print(f"  Average of evens: {result2}")

print()  # Empty line


# ============================================================================
# 4. FORMATTING FUNCTIONS
# ============================================================================
print("=" * 60)
print("4. FORMATTING FUNCTIONS")
print("=" * 60)

def format_person(name, **details):
    """Format person information."""
    info = f"Name: {name}"
    if details:
        info += "\nDetails:"
        for key, value in details.items():
            info += f"\n  {key}: {value}"
    return info

person1 = format_person("Alice")
print(f"  {person1}")

person2 = format_person("Bob", age=30, city="NYC", email="bob@example.com")
print(f"\n  {person2}")

print()  # Empty line


# ============================================================================
# 5. UTILITY FUNCTIONS
# ============================================================================
print("=" * 60)
print("5. UTILITY FUNCTIONS")
print("=" * 60)

def safe_divide(a, b, default=None):
    """Safely divide two numbers."""
    try:
        return a / b
    except ZeroDivisionError:
        return default

def find_item(items, target, default=None):
    """Find item in list, return index or default."""
    try:
        return items.index(target)
    except ValueError:
        return default

def get_nested_value(data, *keys, default=None):
    """Get nested dictionary value safely."""
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

# Test functions
result1 = safe_divide(10, 2)
print(f"  safe_divide(10, 2): {result1}")

result2 = safe_divide(10, 0, default=0)
print(f"  safe_divide(10, 0, default=0): {result2}")

items = ["apple", "banana", "orange"]
index = find_item(items, "banana")
print(f"  find_item({items}, 'banana'): {index}")

data = {"user": {"profile": {"name": "Alice"}}}
name = get_nested_value(data, "user", "profile", "name")
print(f"  get_nested_value(data, 'user', 'profile', 'name'): {name}")

print()  # Empty line


# ============================================================================
# 6. COMPREHENSIVE EXAMPLE
# ============================================================================
print("=" * 60)
print("6. COMPREHENSIVE EXAMPLE")
print("=" * 60)

def process_student_data(name, *scores, **info):
    """Process student data with scores and additional info."""
    student = {
        "name": name,
        "scores": list(scores),
        "average": sum(scores) / len(scores) if scores else 0,
        "min": min(scores) if scores else None,
        "max": max(scores) if scores else None
    }
    student.update(info)
    return student

student = process_student_data(
    "Alice",
    85, 90, 88, 92,
    age=20,
    major="Computer Science",
    email="alice@example.com"
)

print("  Student data:")
for key, value in student.items():
    print(f"    {key}: {value}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL EXAMPLES SUMMARY:")
print("=" * 60)
print("These examples demonstrate:")
print("  - Combining all function concepts")
print("  - Real-world problem solving")
print("  - Flexible function design")
print("  - Error handling in functions")
print("  - Data processing patterns")
print("\nKey Patterns:")
print("  - Use default parameters for optional behavior")
print("  - Use *args for variable positional arguments")
print("  - Use **kwargs for flexible keyword arguments")
print("  - Return tuples for multiple values")
print("  - Validate inputs and handle errors")
print("=" * 60)

