"""
Practical Input/Output Examples

This file demonstrates real-world examples combining input, output,
formatting, and file operations.
"""

# ============================================================================
# 1. INTERACTIVE GREETING PROGRAM
# ============================================================================
print("=" * 60)
print("1. INTERACTIVE GREETING PROGRAM")
print("=" * 60)

def greeting_program():
    """Interactive greeting program."""
    print("Welcome to the Greeting Program!")
    print("-" * 40)
    
    # Get user input
    # Uncomment to make interactive:
    # name = input("Enter your name: ").strip()
    # age = input("Enter your age: ").strip()
    
    # Simulated for demonstration
    name = "Alice"
    age = "25"
    
    # Validate and convert
    try:
        age_int = int(age)
        print(f"\nHello, {name}!")
        print(f"You are {age_int} years old.")
        print(f"In 10 years, you'll be {age_int + 10} years old.")
    except ValueError:
        print("Invalid age entered!")

# greeting_program()  # Uncomment to run

print("  This program:")
print("    - Gets user name and age")
print("    - Validates input")
print("    - Displays formatted greeting")
print("    - Performs calculations")

print()  # Empty line


# ============================================================================
# 2. SIMPLE CALCULATOR
# ============================================================================
print("=" * 60)
print("2. SIMPLE CALCULATOR")
print("=" * 60)

def calculator():
    """Simple calculator program."""
    print("Simple Calculator")
    print("=" * 30)
    
    # Get inputs (simulated)
    num1 = 10
    num2 = 5
    operation = "+"
    
    # Uncomment for interactive:
    # try:
    #     num1 = float(input("Enter first number: "))
    #     operation = input("Enter operation (+, -, *, /): ")
    #     num2 = float(input("Enter second number: "))
    # except ValueError:
    #     print("Invalid input!")
    #     return
    
    # Perform calculation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Error: Division by zero!")
            return
        result = num1 / num2
    else:
        print("Invalid operation!")
        return
    
    # Display result
    print(f"\n{num1} {operation} {num2} = {result}")

# calculator()  # Uncomment to run

print()  # Empty line


# ============================================================================
# 3. STUDENT GRADE TRACKER
# ============================================================================
print("=" * 60)
print("3. STUDENT GRADE TRACKER")
print("=" * 60)

def grade_tracker():
    """Track and display student grades."""
    # Simulated data
    students = [
        {"name": "Alice", "grades": [85, 90, 88]},
        {"name": "Bob", "grades": [75, 80, 78]},
        {"name": "Charlie", "grades": [95, 92, 98]}
    ]
    
    print("Student Grade Report")
    print("=" * 50)
    print(f"{'Name':<15} {'Grades':<20} {'Average':>10}")
    print("-" * 50)
    
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = sum(grades) / len(grades)
        grades_str = ", ".join(map(str, grades))
        print(f"{name:<15} {grades_str:<20} {average:>10.2f}")
    
    print("=" * 50)

grade_tracker()

print()  # Empty line


# ============================================================================
# 4. FILE-BASED TODO LIST
# ============================================================================
print("=" * 60)
print("4. FILE-BASED TODO LIST")
print("=" * 60)

def todo_list_manager():
    """Simple todo list with file storage."""
    todo_file = "todos.txt"
    
    # Create sample todos
    todos = [
        "Learn Python",
        "Write documentation",
        "Test code"
    ]
    
    # Write todos to file
    with open(todo_file, "w") as file:
        for todo in todos:
            file.write(f"- {todo}\n")
    
    print(f"Saved {len(todos)} todos to {todo_file}")
    
    # Read todos from file
    print("\nCurrent todos:")
    with open(todo_file, "r") as file:
        for i, line in enumerate(file, 1):
            print(f"  {i}. {line.strip()}")

todo_list_manager()

print()  # Empty line


# ============================================================================
# 5. USER REGISTRATION FORM
# ============================================================================
print("=" * 60)
print("5. USER REGISTRATION FORM")
print("=" * 60)

def registration_form():
    """User registration with validation."""
    print("User Registration")
    print("=" * 40)
    
    # Simulated inputs
    username = "alice123"
    email = "alice@example.com"
    age = "25"
    password = "secret123"
    
    # Uncomment for interactive:
    # username = input("Username: ").strip()
    # email = input("Email: ").strip()
    # age = input("Age: ").strip()
    # password = input("Password: ").strip()
    
    # Validate
    errors = []
    if not username:
        errors.append("Username is required")
    if "@" not in email:
        errors.append("Invalid email")
    try:
        age_int = int(age)
        if age_int < 13:
            errors.append("Must be 13 or older")
    except ValueError:
        errors.append("Invalid age")
    if len(password) < 8:
        errors.append("Password must be at least 8 characters")
    
    # Display results
    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("\nRegistration successful!")
        print(f"  Username: {username}")
        print(f"  Email: {email}")
        print(f"  Age: {age_int}")

registration_form()

print()  # Empty line


# ============================================================================
# 6. EXPENSE TRACKER
# ============================================================================
print("=" * 60)
print("6. EXPENSE TRACKER")
print("=" * 60)

def expense_tracker():
    """Track expenses and generate report."""
    expenses = [
        {"item": "Groceries", "amount": 150.50, "category": "Food"},
        {"item": "Gas", "amount": 45.00, "category": "Transport"},
        {"item": "Movie", "amount": 12.50, "category": "Entertainment"},
        {"item": "Restaurant", "amount": 35.75, "category": "Food"},
    ]
    
    # Calculate totals
    total = sum(exp["amount"] for exp in expenses)
    by_category = {}
    for exp in expenses:
        cat = exp["category"]
        by_category[cat] = by_category.get(cat, 0) + exp["amount"]
    
    # Display report
    print("Expense Report")
    print("=" * 50)
    print(f"{'Item':<20} {'Category':<15} {'Amount':>10}")
    print("-" * 50)
    for exp in expenses:
        print(f"{exp['item']:<20} {exp['category']:<15} ${exp['amount']:>9.2f}")
    print("-" * 50)
    print(f"{'Total':<36} ${total:>9.2f}")
    print("=" * 50)
    
    print("\nBy Category:")
    for cat, amount in by_category.items():
        print(f"  {cat}: ${amount:.2f}")

expense_tracker()

print()  # Empty line


# ============================================================================
# 7. CONFIGURATION FILE HANDLER
# ============================================================================
print("=" * 60)
print("7. CONFIGURATION FILE HANDLER")
print("=" * 60)

def config_handler():
    """Read and write configuration files."""
    config_file = "app_config.txt"
    
    # Write configuration
    config = {
        "app_name": "MyApp",
        "version": "1.0.0",
        "debug": "True",
        "max_users": "100"
    }
    
    with open(config_file, "w") as file:
        for key, value in config.items():
            file.write(f"{key}={value}\n")
    
    print(f"Configuration saved to {config_file}")
    
    # Read configuration
    loaded_config = {}
    with open(config_file, "r") as file:
        for line in file:
            line = line.strip()
            if "=" in line:
                key, value = line.split("=", 1)
                loaded_config[key] = value
    
    print("\nLoaded configuration:")
    for key, value in loaded_config.items():
        print(f"  {key}: {value}")

config_handler()

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL EXAMPLES SUMMARY:")
print("=" * 60)
print("These examples demonstrate:")
print("  - Getting and validating user input")
print("  - Formatting output for readability")
print("  - Reading from and writing to files")
print("  - Error handling")
print("  - Real-world program patterns")
print("\nKey Patterns:")
print("  - Always validate user input")
print("  - Use try-except for error handling")
print("  - Format output for clarity")
print("  - Use files for data persistence")
print("  - Combine input, processing, and output")
print("=" * 60)

