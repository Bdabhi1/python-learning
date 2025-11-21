"""
Print Basics in Python

This file demonstrates the print() function - the primary way to display
output in Python. Understanding print() is essential for all Python programs.
"""

# ============================================================================
# 1. BASIC PRINT
# ============================================================================
print("=" * 60)
print("1. BASIC PRINT")
print("=" * 60)

# Simplest form - print a string
print("Hello, World!")

# Print multiple strings
print("Hello", "World", "!")

# Print numbers
print(42)
print(3.14)

# Print variables
name = "Alice"
print(name)

print()  # Empty line


# ============================================================================
# 2. PRINTING MULTIPLE ITEMS
# ============================================================================
print("=" * 60)
print("2. PRINTING MULTIPLE ITEMS")
print("=" * 60)

# Multiple items are separated by space by default
print("Hello", "World")
print("Python", "is", "awesome")

# Mix different types
print("Number:", 42)
print("Name:", "Alice", "Age:", 25)

# Print variables
x = 10
y = 20
print("x =", x, "y =", y)

print()  # Empty line


# ============================================================================
# 3. CUSTOM SEPARATOR (sep parameter)
# ============================================================================
print("=" * 60)
print("3. CUSTOM SEPARATOR (sep parameter)")
print("=" * 60)

# Default separator is space
print("Hello", "World")  # Space between

# Custom separator
print("Hello", "World", sep="-")
print("2024", "01", "15", sep="/")  # Date format
print("Python", "is", "great", sep="...")

# No separator
print("Hello", "World", sep="")

# Special characters as separator
print("Item1", "Item2", "Item3", sep=" | ")

print()  # Empty line


# ============================================================================
# 4. CUSTOM END CHARACTER (end parameter)
# ============================================================================
print("=" * 60)
print("4. CUSTOM END CHARACTER (end parameter)")
print("=" * 60)

# Default end is newline (\n)
print("Line 1")
print("Line 2")

# Custom end character
print("Hello", end=" ")
print("World")  # Prints on same line

# No newline
print("Loading", end="")
print("...", end="")
print("Done!")

# Custom end
print("Question:", end="? ")
print("Answer")

# Multiple prints on same line
for i in range(5):
    print(i, end=" ")
print()  # New line after loop

print()  # Empty line


# ============================================================================
# 5. PRINTING VARIABLES
# ============================================================================
print("=" * 60)
print("5. PRINTING VARIABLES")
print("=" * 60)

# Print single variable
name = "Alice"
print(name)

# Print multiple variables
age = 25
city = "New York"
print("Name:", name, "Age:", age, "City:", city)

# Print with expressions
x = 10
y = 20
print("Sum:", x + y)
print("Product:", x * y)

# Print boolean values
is_active = True
print("Status:", is_active)

print()  # Empty line


# ============================================================================
# 6. PRINTING EMPTY LINES
# ============================================================================
print("=" * 60)
print("6. PRINTING EMPTY LINES")
print("=" * 60)

print("First line")
print()  # Empty line
print("Third line")

# Multiple empty lines
print("Before")
print()
print()
print("After")

print()  # Empty line


# ============================================================================
# 7. ESCAPE SEQUENCES
# ============================================================================
print("=" * 60)
print("7. ESCAPE SEQUENCES")
print("=" * 60)

# Newline
print("Line 1\nLine 2")

# Tab
print("Column1\tColumn2\tColumn3")

# Quotes
print("He said, \"Hello!\"")
print('She said, \'Hi!\'')

# Backslash
print("Path: C:\\Users\\Documents")

# Raw string (no escape sequences)
print(r"C:\Users\Documents")  # Note the 'r' prefix

print()  # Empty line


# ============================================================================
# 8. PRINTING SPECIAL CHARACTERS
# ============================================================================
print("=" * 60)
print("8. PRINTING SPECIAL CHARACTERS")
print("=" * 60)

# Unicode characters
print("Hello 🌍")
print("Math: π ≈ 3.14159")
print("Check: ✓")

# Special formatting
print("=" * 50)  # Print 50 equal signs
print("-" * 30)  # Print 30 dashes

print()  # Empty line


# ============================================================================
# 9. PRINTING LISTS AND OTHER TYPES
# ============================================================================
print("=" * 60)
print("9. PRINTING LISTS AND OTHER TYPES")
print("=" * 60)

# Print list
numbers = [1, 2, 3, 4, 5]
print("Numbers:", numbers)

# Print dictionary
person = {"name": "Alice", "age": 25}
print("Person:", person)

# Print tuple
coordinates = (10, 20)
print("Coordinates:", coordinates)

print()  # Empty line


# ============================================================================
# 10. FORMATTED OUTPUT (Preview - detailed in next file)
# ============================================================================
print("=" * 60)
print("10. FORMATTED OUTPUT (Preview)")
print("=" * 60)

# Using f-strings (we'll learn more in next file)
name = "Alice"
age = 25
print(f"My name is {name} and I'm {age} years old")

# Simple concatenation
print("My name is " + name + " and I'm " + str(age) + " years old")

print()  # Empty line


# ============================================================================
# 11. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("11. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Display menu
print("=" * 30)
print("MENU")
print("=" * 30)
print("1. Option 1")
print("2. Option 2")
print("3. Option 3")
print("=" * 30)

# Example 2: Display table
print("\nName\t\tAge\tCity")
print("-" * 30)
print("Alice\t\t25\tNew York")
print("Bob\t\t30\tLondon")

# Example 3: Progress indicator
print("\nProgress:")
for i in range(5):
    print(f"Step {i+1}...", end=" ")
print("Done!")

# Example 4: Display calculation results
x = 10
y = 5
print(f"\nCalculation:")
print(f"  {x} + {y} = {x + y}")
print(f"  {x} - {y} = {x - y}")
print(f"  {x} * {y} = {x * y}")
print(f"  {x} / {y} = {x / y}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRINT BASICS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - print() displays output to console")
print("  - Can print strings, numbers, variables, expressions")
print("  - Multiple items separated by space (default)")
print("  - Use sep parameter to change separator")
print("  - Use end parameter to change end character (default: newline)")
print("  - print() with no arguments prints empty line")
print("  - Escape sequences: \\n (newline), \\t (tab), etc.")
print("=" * 60)

