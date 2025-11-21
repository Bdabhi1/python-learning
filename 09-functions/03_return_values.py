"""
Return Values in Functions

This file demonstrates how functions return values and how to use
those return values in your code.
"""

# ============================================================================
# 1. SINGLE RETURN VALUE
# ============================================================================
print("=" * 60)
print("1. SINGLE RETURN VALUE")
print("=" * 60)

def square(x):
    """Return the square of a number."""
    return x * x

# Use return value
result = square(5)
print(f"  square(5) = {result}")

# Use in expression
total = square(3) + square(4)
print(f"  square(3) + square(4) = {total}")

# Use directly
print(f"  square(6) = {square(6)}")

print()  # Empty line


# ============================================================================
# 2. MULTIPLE RETURN VALUES
# ============================================================================
print("=" * 60)
print("2. MULTIPLE RETURN VALUES")
print("=" * 60)

def divide_with_remainder(a, b):
    """Divide and return quotient and remainder."""
    quotient = a // b
    remainder = a % b
    return quotient, remainder

# Unpack return values
q, r = divide_with_remainder(17, 5)
print(f"  divide_with_remainder(17, 5)")
print(f"    Quotient: {q}, Remainder: {r}")

# Receive as tuple
result = divide_with_remainder(20, 3)
print(f"\n  divide_with_remainder(20, 3) = {result} (tuple)")

print()  # Empty line


# ============================================================================
# 3. CONDITIONAL RETURN
# ============================================================================
print("=" * 60)
print("3. CONDITIONAL RETURN")
print("=" * 60)

def get_grade(score):
    """Return grade based on score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

scores = [95, 85, 75, 65, 55]
print("  Grades:")
for score in scores:
    grade = get_grade(score)
    print(f"    Score {score}: {grade}")

print()  # Empty line


# ============================================================================
# 4. EARLY RETURN
# ============================================================================
print("=" * 60)
print("4. EARLY RETURN")
print("=" * 60)

def is_positive(n):
    """Check if number is positive."""
    if n <= 0:
        return False
    return True  # Only reached if n > 0

print(f"  is_positive(5): {is_positive(5)}")
print(f"  is_positive(-3): {is_positive(-3)}")
print(f"  is_positive(0): {is_positive(0)}")

def find_first_even(numbers):
    """Find first even number."""
    for num in numbers:
        if num % 2 == 0:
            return num  # Return immediately
    return None  # No even number found

result1 = find_first_even([1, 3, 5, 8, 9])
print(f"\n  find_first_even([1,3,5,8,9]): {result1}")

result2 = find_first_even([1, 3, 5, 7])
print(f"  find_first_even([1,3,5,7]): {result2}")

print()  # Empty line


# ============================================================================
# 5. NO RETURN VALUE (RETURNS NONE)
# ============================================================================
print("=" * 60)
print("5. NO RETURN VALUE (RETURNS NONE)")
print("=" * 60)

def print_message(msg):
    """Print message (no return)."""
    print(f"  {msg}")

# Function returns None
result = print_message("Hello")
print(f"  Return value: {result}")

# Explicitly return None
def do_nothing():
    """Function that does nothing."""
    return None

result = do_nothing()
print(f"  do_nothing() returns: {result}")

print()  # Empty line


# ============================================================================
# 6. RETURNING DIFFERENT TYPES
# ============================================================================
print("=" * 60)
print("6. RETURNING DIFFERENT TYPES")
print("=" * 60)

def process_value(value):
    """Process value and return appropriate type."""
    if isinstance(value, str):
        return value.upper()
    elif isinstance(value, int):
        return value * 2
    elif isinstance(value, list):
        return len(value)
    else:
        return None

print(f"  process_value('hello'): {process_value('hello')}")
print(f"  process_value(5): {process_value(5)}")
print(f"  process_value([1,2,3]): {process_value([1,2,3])}")

print()  # Empty line


# ============================================================================
# 7. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("7. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Calculate statistics
print("Example 1: Calculate Statistics")
def calculate_stats(numbers):
    """Calculate min, max, and average."""
    if not numbers:
        return None, None, None
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

numbers = [10, 20, 30, 40, 50]
min_val, max_val, avg = calculate_stats(numbers)
print(f"  Numbers: {numbers}")
print(f"  Min: {min_val}, Max: {max_val}, Avg: {avg:.2f}")

# Example 2: Validate and convert
print("\nExample 2: Validate and Convert")
def safe_divide(a, b):
    """Safely divide two numbers."""
    if b == 0:
        return None, "Division by zero"
    return a / b, None

result, error = safe_divide(10, 2)
print(f"  safe_divide(10, 2): result={result}, error={error}")

result, error = safe_divide(10, 0)
print(f"  safe_divide(10, 0): result={result}, error={error}")

# Example 3: Search function
print("\nExample 3: Search Function")
def find_item(items, target):
    """Find item in list, return index or None."""
    for i, item in enumerate(items):
        if item == target:
            return i
    return None

items = ["apple", "banana", "orange"]
index = find_item(items, "banana")
print(f"  find_item({items}, 'banana'): {index}")

index = find_item(items, "grape")
print(f"  find_item({items}, 'grape'): {index}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("RETURN VALUES SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Use 'return' to send value back")
print("  - Can return single value")
print("  - Can return multiple values (as tuple)")
print("  - Functions without return return None")
print("  - Can return early with conditional return")
print("  - Return value can be used in expressions")
print("\nBest Practices:")
print("  - Return early for clarity")
print("  - Return consistent types when possible")
print("  - Use None to indicate 'no value'")
print("  - Unpack multiple return values")
print("=" * 60)

