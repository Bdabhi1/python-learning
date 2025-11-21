"""
Conditional Statements in Python

This file demonstrates if/else/elif statements - how to make decisions
in your Python programs based on conditions.
"""

# ============================================================================
# 1. BASIC IF STATEMENT
# ============================================================================
print("=" * 60)
print("1. BASIC IF STATEMENT")
print("=" * 60)

# Simple if statement
age = 18
if age >= 18:
    print("  You are an adult")

# Condition is False - nothing happens
age = 15
if age >= 18:
    print("  This won't print")

print("\n  Key Points:")
print("    - if keyword followed by condition")
print("    - Colon (:) is required")
print("    - Indented code executes if condition is True")
print("    - If False, the block is skipped")

print()  # Empty line


# ============================================================================
# 2. IF-ELSE STATEMENT
# ============================================================================
print("=" * 60)
print("2. IF-ELSE STATEMENT")
print("=" * 60)

# If-else provides alternative execution
age = 20
if age >= 18:
    print(f"  Age {age}: You are an adult")
else:
    print(f"  Age {age}: You are a minor")

age = 15
if age >= 18:
    print(f"  Age {age}: You are an adult")
else:
    print(f"  Age {age}: You are a minor")

print("\n  Structure:")
print("    if condition:")
print("        # Execute if True")
print("    else:")
print("        # Execute if False")

print()  # Empty line


# ============================================================================
# 3. ELIF STATEMENT (ELSE-IF)
# ============================================================================
print("=" * 60)
print("3. ELIF STATEMENT (ELSE-IF)")
print("=" * 60)

# elif allows multiple conditions
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"  Score: {score}, Grade: {grade}")

# Test different scores
scores = [95, 85, 75, 65, 55]
for score in scores:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"  Score: {score}, Grade: {grade}")

print("\n  Key Points:")
print("    - Checks conditions in order")
print("    - Only first True condition executes")
print("    - else is optional but recommended")

print()  # Empty line


# ============================================================================
# 4. COMPARISON OPERATORS IN CONDITIONS
# ============================================================================
print("=" * 60)
print("4. COMPARISON OPERATORS IN CONDITIONS")
print("=" * 60)

x = 10

# Greater than
if x > 5:
    print(f"  {x} > 5: True")

# Less than
if x < 20:
    print(f"  {x} < 20: True")

# Equal to
if x == 10:
    print(f"  {x} == 10: True")

# Not equal to
if x != 5:
    print(f"  {x} != 5: True")

# Greater than or equal
if x >= 10:
    print(f"  {x} >= 10: True")

# Less than or equal
if x <= 10:
    print(f"  {x} <= 10: True")

print()  # Empty line


# ============================================================================
# 5. LOGICAL OPERATORS IN CONDITIONS
# ============================================================================
print("=" * 60)
print("5. LOGICAL OPERATORS IN CONDITIONS")
print("=" * 60)

age = 25
has_license = True

# AND - both must be True
if age >= 18 and has_license:
    print("  Can drive (age >= 18 AND has license)")

# OR - at least one must be True
if age < 18 or not has_license:
    print("  Cannot drive (age < 18 OR no license)")

# NOT
is_weekend = False
if not is_weekend:
    print("  It's a weekday")

# Complex condition
temperature = 25
is_sunny = True
if temperature > 20 and is_sunny:
    print("  Great weather for outdoor activities!")

print()  # Empty line


# ============================================================================
# 6. NESTED CONDITIONALS
# ============================================================================
print("=" * 60)
print("6. NESTED CONDITIONALS")
print("=" * 60)

# If statement inside another if statement
age = 25
has_license = True
has_car = True

if age >= 18:
    if has_license:
        if has_car:
            print("  Can drive (age >= 18, has license, has car)")
        else:
            print("  Need a car to drive")
    else:
        print("  Need a license to drive")
else:
    print("  Too young to drive")

# Better: Use logical operators instead
if age >= 18 and has_license and has_car:
    print("  Can drive (using logical operators - cleaner!)")

print("\n  Best Practice: Use 'and'/'or' instead of deep nesting")

print()  # Empty line


# ============================================================================
# 7. CONDITIONAL EXPRESSIONS (TERNARY OPERATOR)
# ============================================================================
print("=" * 60)
print("7. CONDITIONAL EXPRESSIONS (TERNARY OPERATOR)")
print("=" * 60)

# Short form: value_if_true if condition else value_if_false
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"  Age {age}: {status}")

# Equivalent to:
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# More examples
score = 85
result = "Pass" if score >= 60 else "Fail"
print(f"  Score {score}: {result}")

x = 10
y = 20
max_value = x if x > y else y
print(f"  Max of {x} and {y}: {max_value}")

print("\n  Use for simple assignments, not complex logic")

print()  # Empty line


# ============================================================================
# 8. CHECKING MULTIPLE VALUES
# ============================================================================
print("=" * 60)
print("8. CHECKING MULTIPLE VALUES")
print("=" * 60)

# Check if value is in a list
fruits = ["apple", "banana", "orange"]
fruit = "apple"

if fruit in fruits:
    print(f"  {fruit} is in the list")

# Check if value is NOT in a list
if "grape" not in fruits:
    print("  grape is not in the list")

# Check multiple conditions with 'in'
day = "Monday"
if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print("  It's a weekday")
elif day in ["Saturday", "Sunday"]:
    print("  It's a weekend")

print()  # Empty line


# ============================================================================
# 9. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("9. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Age verification
print("Example 1: Age Verification")
age = 20
if age < 13:
    print("  Child")
elif age < 20:
    print("  Teenager")
elif age < 65:
    print("  Adult")
else:
    print("  Senior")

# Example 2: Password strength
print("\nExample 2: Password Strength")
password = "MyP@ssw0rd"
if len(password) < 8:
    strength = "Weak"
elif len(password) < 12:
    strength = "Medium"
else:
    strength = "Strong"
print(f"  Password length: {len(password)}, Strength: {strength}")

# Example 3: Temperature advice
print("\nExample 3: Temperature Advice")
temperature = 25
if temperature > 30:
    advice = "It's hot! Stay hydrated."
elif temperature > 20:
    advice = "Nice weather!"
elif temperature > 10:
    advice = "A bit cool, bring a jacket."
else:
    advice = "It's cold! Dress warmly."
print(f"  Temperature: {temperature}°C - {advice}")

# Example 4: User permissions
print("\nExample 4: User Permissions")
user_role = "admin"
if user_role == "admin":
    can_edit = True
    can_delete = True
elif user_role == "moderator":
    can_edit = True
    can_delete = False
else:
    can_edit = False
    can_delete = False
print(f"  Role: {user_role}, Can edit: {can_edit}, Can delete: {can_delete}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("CONDITIONAL STATEMENTS SUMMARY:")
print("=" * 60)
print("Statements:")
print("  - if: Execute if condition is True")
print("  - else: Execute if condition is False")
print("  - elif: Check another condition if previous was False")
print("\nKey Points:")
print("  - Colon (:) is required after condition")
print("  - Indentation defines the code block")
print("  - Conditions use comparison operators (==, !=, <, >, etc.)")
print("  - Can use logical operators (and, or, not)")
print("  - Only first True condition executes")
print("  - Use 'and'/'or' instead of deep nesting when possible")
print("=" * 60)

