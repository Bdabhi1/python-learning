"""
Default Parameters in Functions

This file demonstrates how to use default parameter values to make
functions more flexible and easier to use.
"""

# ============================================================================
# 1. BASIC DEFAULT PARAMETERS
# ============================================================================
print("=" * 60)
print("1. BASIC DEFAULT PARAMETERS")
print("=" * 60)

def greet(name, greeting="Hello"):
    """Greet with optional custom greeting."""
    print(f"  {greeting}, {name}!")

# Use default
print("  Using default greeting:")
greet("Alice")

# Override default
print("\n  Overriding default:")
greet("Bob", "Hi")

print()  # Empty line


# ============================================================================
# 2. MULTIPLE DEFAULT PARAMETERS
# ============================================================================
print("=" * 60)
print("2. MULTIPLE DEFAULT PARAMETERS")
print("=" * 60)

def create_profile(name, age=18, city="Unknown", email=None):
    """Create user profile with defaults."""
    profile = {"name": name, "age": age, "city": city}
    if email:
        profile["email"] = email
    return profile

# Use all defaults
profile1 = create_profile("Alice")
print(f"  create_profile('Alice'): {profile1}")

# Override some defaults
profile2 = create_profile("Bob", age=25)
print(f"  create_profile('Bob', age=25): {profile2}")

# Override all defaults
profile3 = create_profile("Charlie", age=30, city="NYC", email="charlie@example.com")
print(f"  create_profile('Charlie', ...): {profile3}")

print()  # Empty line


# ============================================================================
# 3. DEFAULT PARAMETER ORDER
# ============================================================================
print("=" * 60)
print("3. DEFAULT PARAMETER ORDER")
print("=" * 60)

# Required parameters must come before defaults
def calculate(price, quantity, discount=0, tax=0.08):
    """Calculate total with optional discount and tax."""
    subtotal = price * quantity
    after_discount = subtotal * (1 - discount)
    total = after_discount * (1 + tax)
    return total

# Can skip defaults at the end
result1 = calculate(10, 2)
print(f"  calculate(10, 2): ${result1:.2f}")

# Can override later defaults
result2 = calculate(10, 2, tax=0.1)
print(f"  calculate(10, 2, tax=0.1): ${result2:.2f}")

# Must use keyword for skipping middle defaults
result3 = calculate(10, 2, discount=0.1)
print(f"  calculate(10, 2, discount=0.1): ${result3:.2f}")

print()  # Empty line


# ============================================================================
# 4. MUTABLE DEFAULT PARAMETERS (COMMON MISTAKE)
# ============================================================================
print("=" * 60)
print("4. MUTABLE DEFAULT PARAMETERS (COMMON MISTAKE)")
print("=" * 60)

# Problematic: Mutable default
def add_item_bad(item, items=[]):
    """Add item to list (PROBLEMATIC - don't do this!)."""
    items.append(item)
    return items

# This causes unexpected behavior
list1 = add_item_bad("apple")
list2 = add_item_bad("banana")
print(f"  ❌ Bad: list1 = {list1}")
print(f"  ❌ Bad: list2 = {list2} (unexpected!)")

# Correct: Use None
def add_item_good(item, items=None):
    """Add item to list (CORRECT)."""
    if items is None:
        items = []
    items.append(item)
    return items

list1 = add_item_good("apple")
list2 = add_item_good("banana")
print(f"\n  ✅ Good: list1 = {list1}")
print(f"  ✅ Good: list2 = {list2}")

print("\n  Rule: Use None for mutable defaults, create new object inside")

print()  # Empty line


# ============================================================================
# 5. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("5. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Format text
print("Example 1: Format Text")
def format_text(text, width=80, indent=0, prefix=""):
    """Format text with optional parameters."""
    lines = []
    for line in text.split('\n'):
        formatted = " " * indent + prefix + line
        lines.append(formatted)
    return '\n'.join(lines)

text = "Hello\nWorld"
formatted = format_text(text, indent=2, prefix="> ")
print(f"  Formatted text:\n{formatted}")

# Example 2: Calculate price
print("\nExample 2: Calculate Price")
def calculate_price(base_price, quantity=1, discount=0, tax_rate=0.08):
    """Calculate final price."""
    subtotal = base_price * quantity
    after_discount = subtotal * (1 - discount)
    total = after_discount * (1 + tax_rate)
    return total

price1 = calculate_price(100)
print(f"  calculate_price(100): ${price1:.2f}")

price2 = calculate_price(100, quantity=2, discount=0.1)
print(f"  calculate_price(100, quantity=2, discount=0.1): ${price2:.2f}")

# Example 3: Log message
print("\nExample 3: Log Message")
def log(message, level="INFO", timestamp=True):
    """Log message with optional parameters."""
    if timestamp:
        from datetime import datetime
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"    [{ts}] [{level}] {message}")
    else:
        print(f"    [{level}] {message}")

log("Application started")
log("Error occurred", level="ERROR")
log("Debug info", level="DEBUG", timestamp=False)

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("DEFAULT PARAMETERS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Provide default values in function definition")
print("  - Defaults make parameters optional")
print("  - Required parameters must come before defaults")
print("  - Can override defaults when calling function")
print("  - Use keyword arguments to skip some defaults")
print("\nImportant:")
print("  - ⚠️  Don't use mutable defaults (lists, dicts)")
print("  - ✅ Use None and create new object inside function")
print("  - Defaults are evaluated once when function is defined")
print("=" * 60)

