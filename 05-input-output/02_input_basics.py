"""
Input Basics in Python

This file demonstrates the input() function - how to get user input
and interact with users in your Python programs.
"""

# ============================================================================
# 1. BASIC INPUT
# ============================================================================
print("=" * 60)
print("1. BASIC INPUT")
print("=" * 60)

# Basic input with prompt
# Uncomment to try:
# name = input("Enter your name: ")
# print(f"Hello, {name}!")

print("Note: Uncomment the code above to try interactive input")
print("input() displays the prompt and waits for user to press Enter")

print()  # Empty line


# ============================================================================
# 2. INPUT ALWAYS RETURNS A STRING
# ============================================================================
print("=" * 60)
print("2. INPUT ALWAYS RETURNS A STRING")
print("=" * 60)

# Important: input() always returns a string, even if user enters a number
# Uncomment to try:
# age = input("Enter your age: ")
# print(f"Type of age: {type(age)}")
# print(f"age = '{age}' (it's a string!)")

# This would cause an error:
# next_year = age + 1  # TypeError: can't add int to string!

print("Key Point: input() always returns a string")
print("You must convert it to the type you need")

print()  # Empty line


# ============================================================================
# 3. CONVERTING INPUT TO INTEGER
# ============================================================================
print("=" * 60)
print("3. CONVERTING INPUT TO INTEGER")
print("=" * 60)

# Convert string to integer
# Uncomment to try:
# age = int(input("Enter your age: "))
# print(f"Age: {age}, Type: {type(age)}")
# next_year = age + 1
# print(f"Next year you'll be {next_year}")

print("Method: int(input('prompt'))")
print("Converts the input string to an integer")

# Example with calculation
print("\nExample (simulated):")
age = 25  # Simulating user input
print(f"  User entered: {age}")
print(f"  Type: {type(age)}")
next_year = age + 1
print(f"  Next year: {next_year}")

print()  # Empty line


# ============================================================================
# 4. CONVERTING INPUT TO FLOAT
# ============================================================================
print("=" * 60)
print("4. CONVERTING INPUT TO FLOAT")
print("=" * 60)

# Convert string to float
# Uncomment to try:
# price = float(input("Enter price: $"))
# print(f"Price: ${price:.2f}")

print("Method: float(input('prompt'))")
print("Converts the input string to a float")

# Example
print("\nExample (simulated):")
price = 19.99  # Simulating user input
print(f"  User entered: {price}")
print(f"  Type: {type(price)}")
total = price * 1.08  # Add 8% tax
print(f"  Price with tax: ${total:.2f}")

print()  # Empty line


# ============================================================================
# 5. GETTING MULTIPLE INPUTS
# ============================================================================
print("=" * 60)
print("5. GETTING MULTIPLE INPUTS")
print("=" * 60)

# Get multiple inputs one by one
# Uncomment to try:
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# city = input("Enter your city: ")
# print(f"{name} is {age} years old and lives in {city}")

print("You can get multiple inputs by calling input() multiple times")
print("Each call waits for user to enter a value and press Enter")

# Simulated example
print("\nExample (simulated):")
name = "Alice"
age = 25
city = "New York"
print(f"  Name: {name}")
print(f"  Age: {age}")
print(f"  City: {city}")
print(f"  Result: {name} is {age} years old and lives in {city}")

print()  # Empty line


# ============================================================================
# 6. HANDLING INVALID INPUT
# ============================================================================
print("=" * 60)
print("6. HANDLING INVALID INPUT")
print("=" * 60)

# Problem: What if user enters text when expecting a number?
# int(input("Enter age: "))  # ValueError if user enters "abc"

# Solution: Use try-except
print("Use try-except to handle invalid input:")

# Example function
def get_age():
    """Get age from user with error handling."""
    while True:
        try:
            age = int(input("Enter your age: "))
            return age
        except ValueError:
            print("Invalid input! Please enter a number.")

# Uncomment to try:
# age = get_age()
# print(f"Age: {age}")

print("Code structure:")
print("  try:")
print("    age = int(input('Enter age: '))")
print("  except ValueError:")
print("    print('Invalid input!')")

print()  # Empty line


# ============================================================================
# 7. INPUT WITH VALIDATION
# ============================================================================
print("=" * 60)
print("7. INPUT WITH VALIDATION")
print("=" * 60)

# Validate input range
def get_valid_age():
    """Get age between 0 and 120."""
    while True:
        try:
            age = int(input("Enter age (0-120): "))
            if 0 <= age <= 120:
                return age
            else:
                print("Age must be between 0 and 120!")
        except ValueError:
            print("Invalid input! Please enter a number.")

# Uncomment to try:
# age = get_valid_age()
# print(f"Valid age: {age}")

print("Validation ensures input meets your requirements")
print("Keep asking until valid input is provided")

print()  # Empty line


# ============================================================================
# 8. YES/NO INPUT
# ============================================================================
print("=" * 60)
print("8. YES/NO INPUT")
print("=" * 60)

# Get yes/no answer
# Uncomment to try:
# response = input("Do you like Python? (yes/no): ").lower()
# if response == "yes":
#     print("Great!")
# elif response == "no":
#     print("Maybe you'll change your mind!")
# else:
#     print("Please answer yes or no")

print("Use .lower() to make input case-insensitive")
print("Compare with 'yes' or 'no'")

# Simulated example
print("\nExample (simulated):")
response = "yes"
if response.lower() == "yes":
    print(f"  User said: {response}")
    print("  Response: Great!")

print()  # Empty line


# ============================================================================
# 9. INPUT WITH DEFAULT VALUES
# ============================================================================
print("=" * 60)
print("9. INPUT WITH DEFAULT VALUES")
print("=" * 60)

# Provide default if user enters nothing
def get_name_with_default():
    """Get name with default value."""
    name = input("Enter your name (press Enter for 'Guest'): ").strip()
    if name == "":
        return "Guest"
    return name

# Uncomment to try:
# name = get_name_with_default()
# print(f"Hello, {name}!")

print("Use .strip() to remove leading/trailing spaces")
print("Check if input is empty to use default")

print()  # Empty line


# ============================================================================
# 10. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("10. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Simple calculator
print("Example 1: Simple Calculator (simulated)")
num1 = 10  # Simulated input
num2 = 5   # Simulated input
operation = "+"  # Simulated input

print(f"  Number 1: {num1}")
print(f"  Number 2: {num2}")
print(f"  Operation: {operation}")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Invalid operation"

print(f"  Result: {result}")

# Example 2: User registration
print("\nExample 2: User Registration (simulated)")
username = "alice123"  # Simulated
email = "alice@example.com"  # Simulated
age = 25  # Simulated

print(f"  Username: {username}")
print(f"  Email: {email}")
print(f"  Age: {age}")
print("  Registration successful!")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("INPUT BASICS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - input('prompt') gets text input from user")
print("  - Always returns a STRING (even for numbers)")
print("  - Convert with int() or float() when needed")
print("  - Use try-except to handle invalid input")
print("  - Validate input to ensure it meets requirements")
print("  - Use .strip() to remove extra spaces")
print("  - Use .lower() for case-insensitive comparison")
print("\nCommon Patterns:")
print("  - age = int(input('Enter age: '))")
print("  - price = float(input('Enter price: '))")
print("  - name = input('Enter name: ').strip()")
print("  - Use while loop with try-except for validation")
print("=" * 60)

