"""
Code Organization in Python

This file demonstrates how to organize Python code effectively.
"""

# ============================================================================
# 1. MODULE STRUCTURE
# ============================================================================
print("=" * 60)
print("1. MODULE STRUCTURE")
print("=" * 60)

print("  Standard module structure:")
print("    ")
print("    1. Module docstring")
print("    2. Imports")
print("    3. Constants")
print("    4. Classes")
print("    5. Functions")
print("    6. Main execution")
print("  ")
print("  Example:")
print("    ")
print("    \"\"\"Module docstring.\"\"\"")
print("    ")
print("    import os")
print("    import sys")
print("    ")
print("    DEFAULT_VALUE = 10")
print("    ")
print("    class MyClass:")
print("        pass")
print("    ")
print("    def my_function():")
print("        pass")
print("    ")
print("    if __name__ == '__main__':")
print("        main()")

print()  # Empty line


# ============================================================================
# 2. FUNCTION DESIGN
# ============================================================================
print("=" * 60)
print("2. FUNCTION DESIGN")
print("=" * 60)

print("  Function design principles:")
print("    - Single responsibility")
print("    - Keep functions small")
print("    - Do one thing well")
print("    - Use descriptive names")
print("  ")
print("  Good:")
print("    def calculate_total(items):")
print("        return sum(item.price for item in items)")
print("  ")
print("  Bad:")
print("    def process_order(order):")
print("        validate_order(order)")
print("        calculate_total(order.items)")
print("        send_email(order.customer)")
print("        update_inventory(order.items)")

print()  # Empty line


# ============================================================================
# 3. AVOID DEEP NESTING
# ============================================================================
print("=" * 60)
print("3. AVOID DEEP NESTING")
print("=" * 60)

print("  Avoid deep nesting:")
print("    ")
print("    # Bad - too nested")
print("    if condition1:")
print("        if condition2:")
print("            if condition3:")
print("                do_something()")
print("    ")
print("    # Good - early returns")
print("    if not condition1:")
print("        return")
print("    if not condition2:")
print("        return")
print("    if not condition3:")
print("        return")
print("    do_something()")

print()  # Empty line


# ============================================================================
# 4. PACKAGE ORGANIZATION
# ============================================================================
print("=" * 60)
print("4. PACKAGE ORGANIZATION")
print("=" * 60)

print("  Package structure:")
print("    ")
print("    my_package/")
print("    ├── __init__.py")
print("    ├── core/")
print("    │   ├── __init__.py")
print("    │   └── main.py")
print("    ├── utils/")
print("    │   ├── __init__.py")
print("    │   └── helpers.py")
print("    └── tests/")
print("        └── test_main.py")
print("  ")
print("  Organize by functionality")

print()  # Empty line


# ============================================================================
# 5. SEPARATION OF CONCERNS
# ============================================================================
print("=" * 60)
print("5. SEPARATION OF CONCERNS")
print("=" * 60)

print("  Separate concerns:")
print("    - Data access layer")
print("    - Business logic")
print("    - Presentation layer")
print("  ")
print("  Example:")
print("    ")
print("    # data.py - Data access")
print("    def get_user(id):")
print("        return database.query(User).filter_by(id=id).first()")
print("    ")
print("    # logic.py - Business logic")
print("    def validate_user(user):")
print("        return user.age >= 18")
print("    ")
print("    # presentation.py - UI")
print("    def display_user(user):")
print("        print(f\"{user.name} ({user.age})\")")

print()  # Empty line


# ============================================================================
# 6. DRY PRINCIPLE
# ============================================================================
print("=" * 60)
print("6. DRY PRINCIPLE")
print("=" * 60)

print("  DRY: Don't Repeat Yourself")
print("    ")
print("    # Bad - repeated code")
print("    def process_user1(user):")
print("        validate(user)")
print("        save(user)")
print("        send_email(user)")
print("    ")
print("    def process_user2(user):")
print("        validate(user)")
print("        save(user)")
print("        send_email(user)")
print("    ")
print("    # Good - reusable")
print("    def process_user(user):")
print("        validate(user)")
print("        save(user)")
print("        send_email(user)")

print()  # Empty line


# ============================================================================
# 7. KEEP IT SIMPLE
# ============================================================================
print("=" * 60)
print("7. KEEP IT SIMPLE")
print("=" * 60)

print("  Simplicity principles:")
print("    - Simple is better than complex")
print("    - Complex is better than complicated")
print("    - Readability counts")
print("  ")
print("  Good:")
print("    result = sum(numbers)")
print("  ")
print("  Less preferred:")
print("    result = reduce(lambda x, y: x + y, numbers)")

print()  # Empty line


# ============================================================================
# 8. CODE COMMENTS
# ============================================================================
print("=" * 60)
print("8. CODE COMMENTS")
print("=" * 60)

print("  Comment guidelines:")
print("    - Explain why, not what")
print("    - Keep comments up to date")
print("    - Use docstrings for functions/classes")
print("  ")
print("  Good:")
print("    # Use binary search for O(log n) performance")
print("    result = binary_search(items, target)")
print("  ")
print("  Bad:")
print("    # Increment counter")
print("    counter += 1")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("CODE ORGANIZATION SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Follow standard module structure")
print("  - Keep functions small and focused")
print("  - Avoid deep nesting")
print("  - Organize packages by functionality")
print("  - Separate concerns")
print("  - Follow DRY principle")
print("  - Keep code simple")
print("=" * 60)

