"""
Basic Python Syntax Examples

This file demonstrates fundamental Python syntax rules that every beginner must understand.
"""

# ============================================================================
# 1. PRINT STATEMENTS
# ============================================================================
print("=" * 50)
print("1. PRINT STATEMENTS")
print("=" * 50)

# Basic print
print("Hello from Python!")

# Print multiple items (separated by space by default)
print("Python", "is", "awesome")

# Print with custom separator
print("Python", "is", "awesome", sep="-")

# Print without newline (end parameter)
print("This", end=" ")
print("will", end=" ")
print("be", end=" ")
print("on", end=" ")
print("one line")

print()  # Empty line for spacing


# ============================================================================
# 2. INDENTATION (VERY IMPORTANT!)
# ============================================================================
print("=" * 50)
print("2. INDENTATION")
print("=" * 50)

# Python uses indentation to define code blocks
# This is different from languages like Java or C++ that use braces {}

# Correct indentation (4 spaces recommended)
if True:
    print("This is indented correctly")
    print("This too - same level of indentation")

# Nested indentation
if True:
    print("Outer block")
    if True:
        print("Inner block - more indented")
        print("Still in inner block")
    print("Back to outer block")

print()  # Empty line


# ============================================================================
# 3. CASE SENSITIVITY
# ============================================================================
print("=" * 50)
print("3. CASE SENSITIVITY")
print("=" * 50)

# Python is case-sensitive
name = "Alice"
Name = "Bob"
NAME = "Charlie"

print(name)  # Output: Alice
print(Name)  # Output: Bob
print(NAME)  # Output: Charlie

# print() is different from Print() or PRINT()
# print("Hello")  # Correct
# Print("Hello")  # Would cause NameError
# PRINT("Hello")  # Would cause NameError

print()  # Empty line


# ============================================================================
# 4. COLONS ARE REQUIRED
# ============================================================================
print("=" * 50)
print("4. COLONS AFTER CONTROL STRUCTURES")
print("=" * 50)

# Colons are required after if, for, while, def, class, etc.
if True:
    print("Colon is required after 'if'")

# This would cause a syntax error:
# if True
#     print("Missing colon!")

print()  # Empty line


# ============================================================================
# 5. QUOTES (SINGLE OR DOUBLE)
# ============================================================================
print("=" * 50)
print("5. QUOTES")
print("=" * 50)

# Both single and double quotes work for strings
single_quotes = 'This is a string'
double_quotes = "This is also a string"

print(single_quotes)
print(double_quotes)

# Use the opposite quote inside if needed
message1 = "He said, 'Hello!'"
message2 = 'She said, "Hi there!"'

print(message1)
print(message2)

# Or escape quotes
message3 = "He said, \"Hello!\""
print(message3)

print()  # Empty line


# ============================================================================
# 6. MULTI-LINE STATEMENTS
# ============================================================================
print("=" * 50)
print("6. MULTI-LINE STATEMENTS")
print("=" * 50)

# Use backslash for line continuation
total = 1 + \
        2 + \
        3

print("Total:", total)

# Or use parentheses (preferred)
total = (1 +
         2 +
         3)

print("Total:", total)

print()  # Empty line


# ============================================================================
# 7. MULTIPLE STATEMENTS ON ONE LINE
# ============================================================================
print("=" * 50)
print("7. MULTIPLE STATEMENTS")
print("=" * 50)

# Use semicolon to separate statements (not recommended, but possible)
x = 5; y = 10; print("x =", x, "y =", y)

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 50)
print("KEY TAKEAWAYS:")
print("=" * 50)
print("1. Indentation defines code blocks (use 4 spaces)")
print("2. Python is case-sensitive")
print("3. Colons are required after if, for, def, etc.")
print("4. Single and double quotes both work for strings")
print("5. Be consistent with your style")
print("=" * 50)

