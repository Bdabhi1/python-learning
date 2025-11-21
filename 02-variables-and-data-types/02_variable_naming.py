"""
Variable Naming in Python - Examples and Best Practices

This file demonstrates proper variable naming conventions and common mistakes to avoid.
Good naming makes code readable and maintainable.
"""

# ============================================================================
# 1. VALID VARIABLE NAMES
# ============================================================================
print("=" * 60)
print("1. VALID VARIABLE NAMES")
print("=" * 60)

# Must start with letter or underscore
name = "Alice"          # ✅ Starts with letter
_name = "Bob"           # ✅ Starts with underscore
name1 = "Charlie"       # ✅ Contains number (not at start)

# Can contain letters, numbers, and underscores
user_name = "John"      # ✅ Contains underscore
user_name_2 = "Jane"    # ✅ Contains underscore and number
user2name = "Doe"       # ✅ Number in middle is OK

print("Valid variable names:")
print(f"  name = {name}")
print(f"  _name = {_name}")
print(f"  name1 = {name1}")
print(f"  user_name = {user_name}")

print()  # Empty line


# ============================================================================
# 2. INVALID VARIABLE NAMES (Commented out to avoid errors)
# ============================================================================
print("=" * 60)
print("2. INVALID VARIABLE NAMES")
print("=" * 60)

print("These would cause SyntaxError (commented out):")
print("  ❌ 2name = 'John'      # Cannot start with number")
print("  ❌ user-name = 'John'  # Cannot contain hyphens")
print("  ❌ user name = 'John'  # Cannot contain spaces")
print("  ❌ user@name = 'John'  # Cannot contain special characters")
print("  ❌ if = 5              # Cannot use Python keywords")

print()  # Empty line


# ============================================================================
# 3. CASE SENSITIVITY
# ============================================================================
print("=" * 60)
print("3. CASE SENSITIVITY")
print("=" * 60)

# Python is case-sensitive
name = "Alice"
Name = "Bob"
NAME = "Charlie"

print("Case-sensitive examples:")
print(f"  name = {name}")
print(f"  Name = {Name}")
print(f"  NAME = {NAME}")
print("  These are three different variables!")

print()  # Empty line


# ============================================================================
# 4. NAMING CONVENTIONS - GOOD PRACTICES
# ============================================================================
print("=" * 60)
print("4. NAMING CONVENTIONS - GOOD PRACTICES")
print("=" * 60)

# Use descriptive names
print("✅ Good: Descriptive names")
user_age = 25
total_price = 100.50
is_active = True
user_email = "user@example.com"

print(f"  user_age = {user_age}")
print(f"  total_price = {total_price}")
print(f"  is_active = {is_active}")

print("\n❌ Bad: Non-descriptive names")
a = 25
x = 100.50
flag = True

print(f"  a = {a}  (What does 'a' represent?)")
print(f"  x = {x}  (What does 'x' represent?)")

print()  # Empty line


# ============================================================================
# 5. SNAKE_CASE (Python Convention)
# ============================================================================
print("=" * 60)
print("5. SNAKE_CASE (Python Convention)")
print("=" * 60)

# Python convention: use snake_case for variables
print("✅ Python convention: snake_case")
user_name = "Alice"
total_items = 10
is_logged_in = True
max_retry_count = 3

print(f"  user_name = {user_name}")
print(f"  total_items = {total_items}")
print(f"  is_logged_in = {is_logged_in}")
print(f"  max_retry_count = {max_retry_count}")

print("\nNote: Other languages use camelCase, but Python prefers snake_case")

print()  # Empty line


# ============================================================================
# 6. CONSTANTS (UPPER_CASE)
# ============================================================================
print("=" * 60)
print("6. CONSTANTS (UPPER_CASE)")
print("=" * 60)

# Constants: values that don't change (convention: UPPER_CASE)
PI = 3.14159
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30
API_BASE_URL = "https://api.example.com"

print("Constants (values that don't change):")
print(f"  PI = {PI}")
print(f"  MAX_CONNECTIONS = {MAX_CONNECTIONS}")
print(f"  DEFAULT_TIMEOUT = {DEFAULT_TIMEOUT}")
print(f"  API_BASE_URL = {API_BASE_URL}")

print()  # Empty line


# ============================================================================
# 7. BOOLEAN VARIABLES (is_, has_, should_)
# ============================================================================
print("=" * 60)
print("7. BOOLEAN VARIABLES (is_, has_, should_)")
print("=" * 60)

# Boolean variables often start with is_, has_, should_, etc.
print("✅ Good: Clear boolean names")
is_active = True
has_permission = False
should_retry = True
can_edit = False
is_valid = True

print(f"  is_active = {is_active}")
print(f"  has_permission = {has_permission}")
print(f"  should_retry = {should_retry}")
print(f"  can_edit = {can_edit}")
print(f"  is_valid = {is_valid}")

print("\n❌ Bad: Unclear boolean names")
active = True
permission = False

print(f"  active = {active}  (Is this a boolean or something else?)")

print()  # Empty line


# ============================================================================
# 8. SINGLE LETTER VARIABLES (When OK)
# ============================================================================
print("=" * 60)
print("8. SINGLE LETTER VARIABLES (When OK)")
print("=" * 60)

# Single letters are OK for loop counters and mathematical variables
print("✅ OK: Loop counters and math variables")
for i in range(5):
    print(f"  Loop iteration {i}")

# Mathematical formulas
x = 10
y = 20
result = x * y
print(f"\n  x = {x}, y = {y}, result = {result}")

print("\n❌ Bad: Single letters for meaningful data")
n = "Alice"  # Should be 'name'
a = 25       # Should be 'age'

print()  # Empty line


# ============================================================================
# 9. AVOIDING PYTHON KEYWORDS
# ============================================================================
print("=" * 60)
print("9. AVOIDING PYTHON KEYWORDS")
print("=" * 60)

# Python keywords cannot be used as variable names
print("Python keywords (cannot use as variable names):")
keywords = [
    "and", "as", "assert", "break", "class", "continue", "def", "del",
    "elif", "else", "except", "exec", "finally", "for", "from", "global",
    "if", "import", "in", "is", "lambda", "not", "or", "pass", "print",
    "raise", "return", "try", "while", "with", "yield"
]

print(f"  Total keywords: {len(keywords)}")
print(f"  Examples: {', '.join(keywords[:10])}...")

# Workaround: add underscore or use different name
print("\nWorkarounds if you need similar names:")
class_name = "Python 101"      # Instead of 'class'
def_timeout = 30                # Instead of 'def'
is_valid = True                 # Instead of 'is' (though 'is' is rarely needed)

print(f"  class_name = {class_name}")
print(f"  def_timeout = {def_timeout}")
print(f"  is_valid = {is_valid}")

print()  # Empty line


# ============================================================================
# 10. REAL-WORLD EXAMPLES
# ============================================================================
print("=" * 60)
print("10. REAL-WORLD EXAMPLES")
print("=" * 60)

# Example 1: User information
print("Example 1: User information")
user_first_name = "John"
user_last_name = "Doe"
user_email = "john.doe@example.com"
user_age = 30
is_email_verified = True

print(f"  Name: {user_first_name} {user_last_name}")
print(f"  Email: {user_email}")
print(f"  Age: {user_age}")
print(f"  Verified: {is_email_verified}")

# Example 2: Shopping cart
print("\nExample 2: Shopping cart")
item_name = "Laptop"
item_price = 999.99
item_quantity = 2
total_cost = item_price * item_quantity
has_discount = False

print(f"  Item: {item_name}")
print(f"  Price: ${item_price}")
print(f"  Quantity: {item_quantity}")
print(f"  Total: ${total_cost}")
print(f"  Discount: {has_discount}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("VARIABLE NAMING SUMMARY:")
print("=" * 60)
print("Rules:")
print("  ✅ Start with letter or underscore")
print("  ✅ Can contain letters, numbers, underscores")
print("  ✅ Case-sensitive")
print("  ❌ Cannot start with number")
print("  ❌ Cannot use Python keywords")
print("  ❌ Cannot contain spaces or special characters")
print("\nConventions:")
print("  - Use snake_case for variables (user_name)")
print("  - Use UPPER_CASE for constants (MAX_SIZE)")
print("  - Use descriptive names (age, not a)")
print("  - Boolean variables: is_, has_, should_ prefix")
print("  - Single letters OK for loops/math (i, x, y)")
print("=" * 60)

