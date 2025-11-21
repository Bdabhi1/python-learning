"""
Identity and Membership Operators in Python

This file demonstrates identity operators (is, is not) and membership
operators (in, not in) which are important for checking object identity
and membership in sequences.
"""

# ============================================================================
# 1. IDENTITY OPERATOR - IS
# ============================================================================
print("=" * 60)
print("1. IDENTITY OPERATOR - IS")
print("=" * 60)

# 'is' checks if two variables refer to the SAME object in memory
x = [1, 2, 3]
y = x  # y refers to the same object as x
print(f"  x = [1, 2, 3]")
print(f"  y = x (same object)")
print(f"  x is y: {x is y}")

# Different objects with same values
a = [1, 2, 3]
b = [1, 2, 3]
print(f"\n  a = [1, 2, 3]")
print(f"  b = [1, 2, 3] (different object, same values)")
print(f"  a is b: {a is b}")

# Integers (small integers are cached, so may be same)
x = 5
y = 5
print(f"\n  x = 5, y = 5")
print(f"  x is y: {x is y} (may be True due to integer caching)")

# But don't rely on this for integers - use == instead!
print("  Note: Use == for value comparison, is for identity")

print()  # Empty line


# ============================================================================
# 2. IDENTITY OPERATOR - IS NOT
# ============================================================================
print("=" * 60)
print("2. IDENTITY OPERATOR - IS NOT")
print("=" * 60)

# 'is not' checks if two variables refer to DIFFERENT objects
x = [1, 2, 3]
y = [1, 2, 3]
print(f"  x = [1, 2, 3]")
print(f"  y = [1, 2, 3]")
print(f"  x is not y: {x is not y}")

# Same object
x = [1, 2, 3]
y = x
print(f"\n  x = [1, 2, 3], y = x")
print(f"  x is not y: {x is not y}")

print()  # Empty line


# ============================================================================
# 3. IS VS == (IMPORTANT DISTINCTION)
# ============================================================================
print("=" * 60)
print("3. IS VS == (IMPORTANT DISTINCTION)")
print("=" * 60)

# == compares VALUES
# is compares IDENTITY (same object in memory)

x = [1, 2, 3]
y = [1, 2, 3]

print(f"  x = [1, 2, 3]")
print(f"  y = [1, 2, 3]")
print(f"  x == y: {x == y} (values are equal)")
print(f"  x is y: {x is y} (different objects)")

# Same object
x = [1, 2, 3]
y = x
print(f"\n  x = [1, 2, 3], y = x")
print(f"  x == y: {x == y} (values are equal)")
print(f"  x is y: {x is y} (same object)")

print("\n  Key Point:")
print("    - Use == to compare VALUES")
print("    - Use is to check IDENTITY (same object)")

print()  # Empty line


# ============================================================================
# 4. WHEN TO USE IS (COMMON CASES)
# ============================================================================
print("=" * 60)
print("4. WHEN TO USE IS (COMMON CASES)")
print("=" * 60)

# Case 1: Check for None (ALWAYS use 'is' for None)
value = None
print(f"  value = None")
print(f"  value is None: {value is None}")
print(f"  value == None: {value == None} (works but not recommended)")

value = 5
print(f"\n  value = 5")
print(f"  value is None: {value is None}")

# Case 2: Check for True/False (use 'is' for identity)
flag = True
print(f"\n  flag = True")
print(f"  flag is True: {flag is True}")
print(f"  flag == True: {flag == True} (also works)")

# Case 3: Check if variables refer to same object
list1 = [1, 2, 3]
list2 = list1
print(f"\n  list1 = [1, 2, 3], list2 = list1")
print(f"  list1 is list2: {list1 is list2}")

print()  # Empty line


# ============================================================================
# 5. MEMBERSHIP OPERATOR - IN
# ============================================================================
print("=" * 60)
print("5. MEMBERSHIP OPERATOR - IN")
print("=" * 60)

# Check if value exists in a sequence

# Strings
text = "Python"
print(f"  text = 'Python'")
print(f"  'P' in text: {'P' in text}")
print(f"  'p' in text: {'p' in text} (case-sensitive)")
print(f"  'th' in text: {'th' in text}")
print(f"  'xyz' in text: {'xyz' in text}")

# Lists
numbers = [1, 2, 3, 4, 5]
print(f"\n  numbers = [1, 2, 3, 4, 5]")
print(f"  3 in numbers: {3 in numbers}")
print(f"  10 in numbers: {10 in numbers}")

# Tuples
my_tuple = (1, 2, 3)
print(f"\n  my_tuple = (1, 2, 3)")
print(f"  2 in my_tuple: {2 in my_tuple}")

# Dictionaries (checks keys, not values)
my_dict = {"name": "Alice", "age": 25}
print(f"\n  my_dict = {{'name': 'Alice', 'age': 25}}")
print(f"  'name' in my_dict: {'name' in my_dict}")
print(f"  'Alice' in my_dict: {'Alice' in my_dict} (checks keys, not values)")

print()  # Empty line


# ============================================================================
# 6. MEMBERSHIP OPERATOR - NOT IN
# ============================================================================
print("=" * 60)
print("6. MEMBERSHIP OPERATOR - NOT IN")
print("=" * 60)

# Check if value does NOT exist in a sequence

# Strings
text = "Python"
print(f"  text = 'Python'")
print(f"  'x' not in text: {'x' not in text}")
print(f"  'P' not in text: {'P' not in text}")

# Lists
numbers = [1, 2, 3, 4, 5]
print(f"\n  numbers = [1, 2, 3, 4, 5]")
print(f"  10 not in numbers: {10 not in numbers}")
print(f"  3 not in numbers: {3 not in numbers}")

print()  # Empty line


# ============================================================================
# 7. PRACTICAL EXAMPLES - IDENTITY
# ============================================================================
print("=" * 60)
print("7. PRACTICAL EXAMPLES - IDENTITY")
print("=" * 60)

# Example 1: Check for None (most common use)
def process_data(data):
    if data is None:
        return "No data provided"
    return f"Processing: {data}"

result1 = process_data(None)
result2 = process_data("some data")
print(f"  process_data(None): {result1}")
print(f"  process_data('some data'): {result2}")

# Example 2: Check if two lists are the same object
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print(f"\n  list1 = [1, 2, 3]")
print(f"  list2 = list1")
print(f"  list3 = [1, 2, 3]")
print(f"  list1 is list2: {list1 is list2} (same object)")
print(f"  list1 is list3: {list1 is list3} (different objects)")

print()  # Empty line


# ============================================================================
# 8. PRACTICAL EXAMPLES - MEMBERSHIP
# ============================================================================
print("=" * 60)
print("8. PRACTICAL EXAMPLES - MEMBERSHIP")
print("=" * 60)

# Example 1: Check if character is vowel
char = 'a'
vowels = 'aeiou'
is_vowel = char.lower() in vowels
print(f"  '{char}' is vowel: {is_vowel}")

# Example 2: Check if item is in allowed list
user_role = "admin"
allowed_roles = ["admin", "moderator", "user"]
has_access = user_role in allowed_roles
print(f"\n  Role '{user_role}' has access: {has_access}")

# Example 3: Check if substring exists
email = "user@example.com"
is_valid = "@" in email and "." in email
print(f"\n  Email '{email}' is valid: {is_valid}")

# Example 4: Check if key exists in dictionary
user = {"name": "Alice", "age": 25}
has_name = "name" in user
has_email = "email" in user
print(f"\n  User dict has 'name': {has_name}")
print(f"  User dict has 'email': {has_email}")

# Example 5: Filter items
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [n for n in numbers if n % 2 == 0]
print(f"\n  Numbers: {numbers}")
print(f"  Even numbers: {even_numbers}")

print()  # Empty line


# ============================================================================
# 9. COMMON MISTAKES
# ============================================================================
print("=" * 60)
print("9. COMMON MISTAKES")
print("=" * 60)

# Mistake 1: Using == instead of is for None
value = None
# Good
print(f"  value is None: {value is None}")
# Bad (but works)
print(f"  value == None: {value == None} (not recommended)")

# Mistake 2: Using is instead of == for values
x = 5
y = 5
# Works for small integers (caching), but unreliable
print(f"\n  x = 5, y = 5")
print(f"  x is y: {x is y} (may work but don't rely on it)")
print(f"  x == y: {x == y} (correct way)")

# Mistake 3: Using in with wrong type
# "key" in {"key": "value"}  # ✅ Works (checks keys)
# "value" in {"key": "value"}  # ❌ False (doesn't check values)

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("IDENTITY AND MEMBERSHIP OPERATORS SUMMARY:")
print("=" * 60)
print("Identity Operators:")
print("  Operator | Description              | Example")
print("  ---------|--------------------------|-------------------")
print("  is       | Same object in memory    | x is y")
print("  is not   | Different objects        | x is not y")
print("\nMembership Operators:")
print("  Operator | Description              | Example")
print("  ---------|--------------------------|-------------------")
print("  in       | Value exists in sequence | 'a' in 'apple'")
print("  not in   | Value not in sequence    | 'x' not in 'apple'")
print("=" * 60)
print("\nKey Points:")
print("  - Use 'is' for None, True, False, and object identity")
print("  - Use '==' for value comparison")
print("  - Use 'in' to check membership in sequences")
print("  - 'in' with dict checks keys, not values")
print("  - 'is' checks identity, '==' checks equality")
print("=" * 60)

