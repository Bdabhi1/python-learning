"""
String Formatting in Python

This file demonstrates different ways to format strings for output.
String formatting makes it easy to create readable output with variables.
"""

# ============================================================================
# 1. F-STRINGS (RECOMMENDED - Python 3.6+)
# ============================================================================
print("=" * 60)
print("1. F-STRINGS (RECOMMENDED - Python 3.6+)")
print("=" * 60)

# Basic f-string
name = "Alice"
age = 25
message = f"My name is {name} and I'm {age} years old"
print(f"  {message}")

# F-string with expressions
x = 10
y = 20
print(f"  The sum of {x} and {y} is {x + y}")

# F-string with function calls
text = "hello"
print(f"  Uppercase: {text.upper()}")

# F-string with multiple variables
city = "New York"
print(f"  {name} is {age} years old and lives in {city}")

print("\n  Advantages:")
print("    - Most readable")
print("    - Fast performance")
print("    - Can include expressions")
print("    - Modern Python style")

print()  # Empty line


# ============================================================================
# 2. F-STRING FORMATTING OPTIONS
# ============================================================================
print("=" * 60)
print("2. F-STRING FORMATTING OPTIONS")
print("=" * 60)

# Number formatting
pi = 3.14159
print(f"  Pi: {pi:.2f}")  # 2 decimal places
print(f"  Pi: {pi:.4f}")  # 4 decimal places

# Integer formatting with padding
number = 42
print(f"  Number: {number:05d}")  # 5 digits with leading zeros
print(f"  Number: {number:10d}")  # 10 characters wide, right-aligned

# String formatting
text = "Hello"
print(f"  Text: '{text:10s}'")  # 10 characters wide
print(f"  Text: '{text:>10s}'")  # Right-aligned
print(f"  Text: '{text:<10s}'")  # Left-aligned
print(f"  Text: '{text:^10s}'")  # Center-aligned

# Percentage
ratio = 0.85
print(f"  Ratio: {ratio:.1%}")  # 85.0%

# Scientific notation
large_number = 1234567
print(f"  Large: {large_number:e}")  # Scientific notation

print()  # Empty line


# ============================================================================
# 3. .format() METHOD
# ============================================================================
print("=" * 60)
print("3. .format() METHOD")
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
message = "{name} is {age} years old".format(name="Alice", age=25)
print(f"  {message}")

# Mix positional and named
message = "{} is {} years old. {name} lives in {city}.".format(
    "Alice", 25, name="Alice", city="New York"
)
print(f"  {message}")

print()  # Empty line


# ============================================================================
# 4. .format() WITH FORMAT SPECIFIERS
# ============================================================================
print("=" * 60)
print("4. .format() WITH FORMAT SPECIFIERS")
print("=" * 60)

# Float formatting
pi = 3.14159
print(f"  Pi: {pi:.2f}".format(pi=pi))
print("  Format: {:.2f}".format(pi))

# Integer formatting
number = 42
print("  Number: {:05d}".format(number))
print("  Number: {:10d}".format(number))

# String formatting
text = "Hello"
print("  Text: '{:10s}'".format(text))
print("  Text: '{:>10s}'".format(text))

# Multiple format specifiers
print("  Price: ${:.2f}, Quantity: {:03d}".format(19.99, 5))

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
# %s - String
# %d - Integer
# %f - Float
# %x - Hexadecimal

pi = 3.14159
print("  Pi: %.2f" % pi)
print("  Number: %05d" % 42)

# Multiple values
print("  Name: %s, Age: %d, Score: %.2f" % ("Alice", 25, 95.5))

print("\n  Note: This style is older, use f-strings or .format() instead")

print()  # Empty line


# ============================================================================
# 6. STRING CONCATENATION
# ============================================================================
print("=" * 60)
print("6. STRING CONCATENATION")
print("=" * 60)

# Using + operator
name = "Alice"
age = 25
message = "My name is " + name + " and I'm " + str(age) + " years old"
print(f"  {message}")

# Note: Must convert numbers to strings
x = 10
y = 20
result = "Sum: " + str(x + y)
print(f"  {result}")

print("\n  Note: Less preferred - use f-strings instead")
print("  Can be slow and harder to read")

print()  # Empty line


# ============================================================================
# 7. MULTILINE STRINGS
# ============================================================================
print("=" * 60)
print("7. MULTILINE STRINGS")
print("=" * 60)

# Multiline f-string
name = "Alice"
age = 25
message = f"""
Name: {name}
Age: {age}
Status: Active
"""
print("  Multiline f-string:")
print(message)

# Multiline with .format()
message = """
Name: {}
Age: {}
Status: Active
""".format(name, age)
print("  Multiline with .format():")
print(message)

print()  # Empty line


# ============================================================================
# 8. FORMATTING IN LOOPS
# ============================================================================
print("=" * 60)
print("8. FORMATTING IN LOOPS")
print("=" * 60)

# Format in loop
print("  Numbered list:")
for i in range(1, 6):
    print(f"    {i}. Item {i}")

# Format table
print("\n  Table:")
print("    Name      Age     City")
print("    " + "-" * 30)
data = [
    ("Alice", 25, "New York"),
    ("Bob", 30, "London"),
    ("Charlie", 35, "Paris")
]
for name, age, city in data:
    print(f"    {name:10s} {age:3d}     {city}")

print()  # Empty line


# ============================================================================
# 9. CONDITIONAL FORMATTING
# ============================================================================
print("=" * 60)
print("9. CONDITIONAL FORMATTING")
print("=" * 60)

# Conditional expressions in f-strings
score = 85
print(f"  Score: {score} - {'Pass' if score >= 60 else 'Fail'}")

# Multiple conditions
temperature = 25
status = "Hot" if temperature > 30 else "Warm" if temperature > 20 else "Cold"
print(f"  Temperature: {temperature}°C - {status}")

print()  # Empty line


# ============================================================================
# 10. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("10. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Receipt
print("  Example 1: Receipt")
item = "Laptop"
price = 999.99
quantity = 2
tax_rate = 0.08

subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

print(f"\n    Item: {item}")
print(f"    Price: ${price:.2f}")
print(f"    Quantity: {quantity}")
print(f"    Subtotal: ${subtotal:.2f}")
print(f"    Tax ({tax_rate*100:.0f}%): ${tax:.2f}")
print(f"    Total: ${total:.2f}")

# Example 2: Progress bar
print("\n  Example 2: Progress")
progress = 75
bar_length = 20
filled = int(bar_length * progress / 100)
bar = "█" * filled + "░" * (bar_length - filled)
print(f"    Progress: [{bar}] {progress}%")

# Example 3: Formatted report
print("\n  Example 3: Report")
print("    " + "=" * 40)
print(f"    {'Report':^40}")
print("    " + "=" * 40)
print(f"    {'Name':<20} {'Age':>5} {'Score':>10}")
print("    " + "-" * 40)
print(f"    {'Alice':<20} {25:>5} {95.5:>10.1f}")
print(f"    {'Bob':<20} {30:>5} {87.0:>10.1f}")
print("    " + "=" * 40)

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("STRING FORMATTING SUMMARY:")
print("=" * 60)
print("Method          | Example")
print("----------------|----------------------------------------")
print("f-strings       | f'Hello {name}'")
print(".format()       | 'Hello {}'.format(name)")
print("% formatting   | 'Hello %s' % name")
print("Concatenation   | 'Hello ' + name")
print("=" * 60)
print("\nRecommendations:")
print("  ✅ Use f-strings (Python 3.6+) - most readable and fast")
print("  ✅ Use .format() for older Python versions")
print("  ⚠️  Avoid % formatting (old style)")
print("  ⚠️  Avoid concatenation for complex formatting")
print("\nFormat Specifiers:")
print("  {:.2f} - Float with 2 decimals")
print("  {:05d} - Integer with leading zeros")
print("  {:10s} - String 10 characters wide")
print("  {:>10} - Right-aligned")
print("  {:<10} - Left-aligned")
print("  {:^10} - Center-aligned")
print("=" * 60)

