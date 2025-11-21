"""
String Formatting in Python

This file demonstrates different ways to format strings in Python, including
f-strings, .format() method, and % formatting.
"""

# ============================================================================
# 1. F-STRINGS (PYTHON 3.6+) - RECOMMENDED
# ============================================================================
print("=" * 60)
print("1. F-STRINGS (PYTHON 3.6+) - RECOMMENDED")
print("=" * 60)

# Basic f-string
name = "Alice"
age = 25
message = f"My name is {name} and I'm {age} years old"
print(f"  {message}")

# With expressions
x, y = 10, 20
result = f"The sum of {x} and {y} is {x + y}"
print(f"  {result}")

# With function calls
text = "python"
formatted = f"Uppercase: {text.upper()}"
print(f"  {formatted}")

# Multiple variables
first = "John"
last = "Doe"
full = f"{first} {last}"
print(f"  Full name: {full}")

print()  # Empty line


# ============================================================================
# 2. F-STRING FORMATTING SPECIFIERS
# ============================================================================
print("=" * 60)
print("2. F-STRING FORMATTING SPECIFIERS")
print("=" * 60)

# Float formatting
pi = 3.14159
print(f"  Pi: {pi:.2f}")  # 2 decimal places
print(f"  Pi: {pi:.4f}")  # 4 decimal places
print(f"  Pi: {pi:10.2f}")  # 10 width, 2 decimals

# Integer formatting
number = 42
print(f"  Number: {number:05d}")  # 5 digits with leading zeros
print(f"  Number: {number:10d}")  # Right-aligned in 10 spaces

# String formatting
text = "Hello"
print(f"  Text: {text:>10}")  # Right-aligned, 10 width
print(f"  Text: {text:<10}")  # Left-aligned, 10 width
print(f"  Text: {text:^10}")  # Centered, 10 width
print(f"  Text: {text:*^10}")  # Centered with * padding

# Percentage
ratio = 0.85
print(f"  Ratio: {ratio:.1%}")  # 85.0%

print()  # Empty line


# ============================================================================
# 3. .FORMAT() METHOD
# ============================================================================
print("=" * 60)
print("3. .FORMAT() METHOD")
print("=" * 60)

# Basic .format()
name = "Alice"
age = 25
message = "My name is {} and I'm {} years old".format(name, age)
print(f"  {message}")

# Positional arguments
message = "{0} is {1} years old. {0} likes Python.".format(name, age)
print(f"  {message}")

# Named arguments
message = "{name} is {age} years old".format(name="Bob", age=30)
print(f"  {message}")

print()  # Empty line


# ============================================================================
# 4. .FORMAT() WITH FORMAT SPECIFIERS
# ============================================================================
print("=" * 60)
print("4. .FORMAT() WITH FORMAT SPECIFIERS")
print("=" * 60)

# Float formatting
pi = 3.14159
print("  Pi: {:.2f}".format(pi))
print("  Pi: {:10.2f}".format(pi))

# Integer formatting
number = 42
print("  Number: {:05d}".format(number))
print("  Number: {:10d}".format(number))

# String formatting
text = "Hello"
print("  Text: {:>10}".format(text))
print("  Text: {:<10}".format(text))
print("  Text: {:^10}".format(text))

print()  # Empty line


# ============================================================================
# 5. % FORMATTING (OLD STYLE)
# ============================================================================
print("=" * 60)
print("5. % FORMATTING (OLD STYLE)")
print("=" * 60)

# Basic % formatting
name = "Alice"
age = 25
message = "My name is %s and I'm %d years old" % (name, age)
print(f"  {message}")

# Format specifiers
print("  String: %s" % "Hello")
print("  Integer: %d" % 42)
print("  Float: %f" % 3.14)
print("  Float (2 decimals): %.2f" % 3.14159)

# Multiple values
print("  Name: %s, Age: %d, Score: %.2f" % ("Alice", 25, 95.5))

print()  # Empty line


# ============================================================================
# 6. STRING CONCATENATION (LESS PREFERRED)
# ============================================================================
print("=" * 60)
print("6. STRING CONCATENATION (LESS PREFERRED)")
print("=" * 60)

# Using + operator
name = "Alice"
age = 25
message = "My name is " + name + " and I'm " + str(age) + " years old"
print(f"  {message}")

# Note: Requires converting non-strings to strings
number = 42
text = "The number is " + str(number)
print(f"  {text}")

print()  # Empty line


# ============================================================================
# 7. FORMATTING NUMBERS
# ============================================================================
print("=" * 60)
print("7. FORMATTING NUMBERS")
print("=" * 60)

# Thousands separator
large_number = 1234567
print(f"  With commas: {large_number:,}")

# Currency
price = 19.99
print(f"  Price: ${price:.2f}")

# Percentage
ratio = 0.85
print(f"  Ratio: {ratio:.1%}")

# Padding numbers
num = 42
print(f"  Padded: {num:05d}")
print(f"  Padded: {num:10d}")

print()  # Empty line


# ============================================================================
# 8. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("8. PRACTICAL EXAMPLES")
print("=" * 60)

# Formatting a receipt
def format_receipt(items):
    """Format a simple receipt."""
    total = sum(price for _, price in items)
    receipt = "RECEIPT\n" + "=" * 30 + "\n"
    for item, price in items:
        receipt += f"{item:20s} ${price:6.2f}\n"
    receipt += "-" * 30 + "\n"
    receipt += f"{'Total':20s} ${total:6.2f}\n"
    return receipt

items = [("Apple", 1.50), ("Banana", 0.75), ("Orange", 2.00)]
print(format_receipt(items))

# Formatting a table
def format_table(data):
    """Format data as a table."""
    header = f"{'Name':<15} {'Age':>5} {'Score':>8}\n"
    header += "-" * 30 + "\n"
    rows = "\n".join(f"{name:<15} {age:>5} {score:>8.2f}" 
                     for name, age, score in data)
    return header + rows

data = [("Alice", 25, 95.5), ("Bob", 30, 87.3), ("Charlie", 28, 92.1)]
print("\n  Table:")
print(format_table(data))

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("STRING FORMATTING SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - f-strings (Python 3.6+) are recommended: f'Text {variable}'")
print("  - .format() method: 'Text {}'.format(variable)")
print("  - % formatting (old style): 'Text %s' % variable")
print("  - String concatenation: 'Text ' + variable (less preferred)")
print("\nFormat Specifiers:")
print("  - Float: {value:.2f} - 2 decimal places")
print("  - Integer: {value:05d} - 5 digits with zeros")
print("  - String: {value:>10} - right-aligned, 10 width")
print("  - Percentage: {value:.1%} - as percentage")
print("=" * 60)

