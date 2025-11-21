"""
Logical Operators in Python

This file demonstrates logical operators (and, or, not) that work with
boolean values and are essential for conditional logic.
"""

# ============================================================================
# 1. LOGICAL AND (and)
# ============================================================================
print("=" * 60)
print("1. LOGICAL AND (and)")
print("=" * 60)

# AND returns True only if both operands are True
result1 = True and True
print(f"  True and True = {result1}")

result2 = True and False
print(f"  True and False = {result2}")

result3 = False and True
print(f"  False and True = {result3}")

result4 = False and False
print(f"  False and False = {result4}")

print("\nTruth Table for AND:")
print("  A     | B     | A and B")
print("  ------|-------|---------")
print(f"  True  | True  | {True and True}")
print(f"  True  | False | {True and False}")
print(f"  False | True  | {False and True}")
print(f"  False | False | {False and False}")

print()  # Empty line


# ============================================================================
# 2. LOGICAL OR (or)
# ============================================================================
print("=" * 60)
print("2. LOGICAL OR (or)")
print("=" * 60)

# OR returns True if at least one operand is True
result1 = True or True
print(f"  True or True = {result1}")

result2 = True or False
print(f"  True or False = {result2}")

result3 = False or True
print(f"  False or True = {result3}")

result4 = False or False
print(f"  False or False = {result4}")

print("\nTruth Table for OR:")
print("  A     | B     | A or B")
print("  ------|-------|--------")
print(f"  True  | True  | {True or True}")
print(f"  True  | False | {True or False}")
print(f"  False | True  | {False or True}")
print(f"  False | False | {False or False}")

print()  # Empty line


# ============================================================================
# 3. LOGICAL NOT (not)
# ============================================================================
print("=" * 60)
print("3. LOGICAL NOT (not)")
print("=" * 60)

# NOT returns the opposite boolean value
result1 = not True
print(f"  not True = {result1}")

result2 = not False
print(f"  not False = {result2}")

# Double negation
result3 = not not True
print(f"  not not True = {result3}")

print("\nTruth Table for NOT:")
print("  A     | not A")
print("  ------|------")
print(f"  True  | {not True}")
print(f"  False | {not False}")

print()  # Empty line


# ============================================================================
# 4. COMBINING LOGICAL OPERATORS
# ============================================================================
print("=" * 60)
print("4. COMBINING LOGICAL OPERATORS")
print("=" * 60)

# Multiple AND operations
result1 = True and True and True
print(f"  True and True and True = {result1}")

result2 = True and True and False
print(f"  True and True and False = {result2}")

# Multiple OR operations
result3 = False or False or True
print(f"  False or False or True = {result3}")

result4 = False or False or False
print(f"  False or False or False = {result4}")

# Combining AND and OR (use parentheses for clarity)
result5 = (True and False) or True
print(f"  (True and False) or True = {result5}")

result6 = True and (False or True)
print(f"  True and (False or True) = {result6}")

# NOT with AND/OR
result7 = not (True and False)
print(f"  not (True and False) = {result7}")

result8 = not True or not False
print(f"  not True or not False = {result8}")

print()  # Empty line


# ============================================================================
# 5. SHORT-CIRCUIT EVALUATION
# ============================================================================
print("=" * 60)
print("5. SHORT-CIRCUIT EVALUATION")
print("=" * 60)

# AND: If first is False, second is not evaluated
print("AND short-circuit:")
print("  False and (anything) = False (second not evaluated)")

# OR: If first is True, second is not evaluated
print("OR short-circuit:")
print("  True or (anything) = True (second not evaluated)")

# Practical example
def expensive_check():
    print("    (This function was called)")
    return True

# With AND - second part not evaluated if first is False
print("\n  False and expensive_check():")
if False and expensive_check():
    pass
else:
    print("    expensive_check() was NOT called (short-circuited)")

# With OR - second part not evaluated if first is True
print("\n  True or expensive_check():")
if True or expensive_check():
    print("    expensive_check() was NOT called (short-circuited)")

print()  # Empty line


# ============================================================================
# 6. TRUTHINESS - NON-BOOLEAN VALUES
# ============================================================================
print("=" * 60)
print("6. TRUTHINESS - NON-BOOLEAN VALUES")
print("=" * 60)

# Python evaluates non-boolean values as True/False
# Falsy values: False, 0, 0.0, "", None, [], {}
# Everything else is truthy

print("Falsy values (evaluate to False):")
print(f"  bool(False) = {bool(False)}")
print(f"  bool(0) = {bool(0)}")
print(f"  bool(0.0) = {bool(0.0)}")
print(f"  bool('') = {bool('')}")
print(f"  bool(None) = {bool(None)}")
print(f"  bool([]) = {bool([])}")

print("\nTruthy values (evaluate to True):")
print(f"  bool(True) = {bool(True)}")
print(f"  bool(1) = {bool(1)}")
print(f"  bool(-1) = {bool(-1)}")
print(f"  bool('hello') = {bool('hello')}")
print(f"  bool([1, 2]) = {bool([1, 2])}")

# Using with logical operators
result1 = 5 and 10  # Returns 10 (last truthy value)
print(f"\n  5 and 10 = {result1} (returns last truthy value)")

result2 = 0 and 10  # Returns 0 (first falsy value)
print(f"  0 and 10 = {result2} (returns first falsy value)")

result3 = 5 or 10  # Returns 5 (first truthy value)
print(f"  5 or 10 = {result3} (returns first truthy value)")

result4 = 0 or 10  # Returns 10 (first truthy value)
print(f"  0 or 10 = {result4} (returns first truthy value)")

print()  # Empty line


# ============================================================================
# 7. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("7. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Check if age is in valid range
age = 25
is_valid_age = age >= 18 and age <= 65
print(f"  Age: {age}, Is valid (18-65): {is_valid_age}")

# Example 2: Check if user has permission
has_read_permission = True
has_write_permission = False
can_edit = has_read_permission and has_write_permission
print(f"  Can edit: {can_edit}")

# Example 3: Check if user is admin or moderator
is_admin = False
is_moderator = True
has_privileges = is_admin or is_moderator
print(f"  Has privileges: {has_privileges}")

# Example 4: Check if number is NOT zero
number = 5
is_not_zero = not (number == 0)
print(f"  Number: {number}, Is not zero: {is_not_zero}")

# Example 5: Complex condition
score = 85
attendance = 0.95
passed = score >= 60 and attendance >= 0.8
print(f"  Score: {score}, Attendance: {attendance}, Passed: {passed}")

# Example 6: Using with strings
name = ""
default_name = "Guest"
display_name = name or default_name
print(f"  Display name: '{display_name}' (uses default if name is empty)")

print()  # Empty line


# ============================================================================
# 8. DE MORGAN'S LAWS
# ============================================================================
print("=" * 60)
print("8. DE MORGAN'S LAWS")
print("=" * 60)

# De Morgan's Law 1: not (A and B) = (not A) or (not B)
A = True
B = False
result1 = not (A and B)
result2 = (not A) or (not B)
print(f"  not (A and B) = {result1}")
print(f"  (not A) or (not B) = {result2}")
print(f"  They are equal: {result1 == result2}")

# De Morgan's Law 2: not (A or B) = (not A) and (not B)
result3 = not (A or B)
result4 = (not A) and (not B)
print(f"\n  not (A or B) = {result3}")
print(f"  (not A) and (not B) = {result4}")
print(f"  They are equal: {result3 == result4}")

print()  # Empty line


# ============================================================================
# 9. COMMON PATTERNS
# ============================================================================
print("=" * 60)
print("9. COMMON PATTERNS")
print("=" * 60)

# Pattern 1: Check if value exists and is valid
value = 10
is_valid = value is not None and value > 0
print(f"  Value: {value}, Is valid: {is_valid}")

# Pattern 2: Provide default value
user_input = ""
result = user_input or "default"
print(f"  Input: '{user_input}', Result: '{result}'")

# Pattern 3: Multiple conditions
x = 5
y = 10
condition = (x > 0 and y > 0) or (x < 0 and y < 0)
print(f"  x={x}, y={y}, Condition: {condition}")

# Pattern 4: Negation for clarity
is_empty = not bool([1, 2, 3])
print(f"  List is empty: {is_empty}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("LOGICAL OPERATORS SUMMARY:")
print("=" * 60)
print("Operator | Description                    | Example")
print("---------|--------------------------------|----------")
print("and      | Both must be True              | True and False = False")
print("or       | At least one must be True       | True or False = True")
print("not      | Returns opposite boolean        | not True = False")
print("=" * 60)
print("\nKey Points:")
print("  - AND: Returns True only if both are True")
print("  - OR: Returns True if at least one is True")
print("  - NOT: Returns opposite boolean value")
print("  - Short-circuit evaluation: second operand may not be evaluated")
print("  - Works with truthy/falsy values, not just booleans")
print("  - Use parentheses to clarify complex expressions")
print("=" * 60)

