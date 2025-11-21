"""
Practical Control Flow Examples

This file demonstrates real-world examples combining conditionals,
loops, break, continue, and other control flow concepts.
"""

# ============================================================================
# 1. NUMBER GUESSING GAME (SIMULATED)
# ============================================================================
print("=" * 60)
print("1. NUMBER GUESSING GAME (SIMULATED)")
print("=" * 60)

def number_guessing_game():
    """Simulated number guessing game."""
    secret_number = 42
    max_attempts = 5
    attempts = 0
    
    print("  Guess the number (1-100)!")
    print(f"  (Secret number is {secret_number} for demo)")
    
    while attempts < max_attempts:
        attempts += 1
        # Simulated guesses
        if attempts == 1:
            guess = 50
        elif attempts == 2:
            guess = 30
        elif attempts == 3:
            guess = 45
        elif attempts == 4:
            guess = 42
        
        print(f"\n  Attempt {attempts}: Guessed {guess}")
        
        if guess == secret_number:
            print(f"  🎉 Correct! You guessed it in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("  Too low! Try again.")
        else:
            print("  Too high! Try again.")
    else:
        print(f"\n  Game over! The number was {secret_number}")

number_guessing_game()

print()  # Empty line


# ============================================================================
# 2. STUDENT GRADE CALCULATOR
# ============================================================================
print("=" * 60)
print("2. STUDENT GRADE CALCULATOR")
print("=" * 60)

def calculate_grades():
    """Calculate and display student grades."""
    students = [
        {"name": "Alice", "scores": [85, 90, 88, 92]},
        {"name": "Bob", "scores": [75, 80, 78, 82]},
        {"name": "Charlie", "scores": [95, 98, 92, 96]}
    ]
    
    print("  Student Grade Report")
    print("  " + "=" * 50)
    print(f"  {'Name':<15} {'Average':>10} {'Grade':>8}")
    print("  " + "-" * 50)
    
    for student in students:
        name = student["name"]
        scores = student["scores"]
        average = sum(scores) / len(scores)
        
        # Determine grade
        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        else:
            grade = "F"
        
        print(f"  {name:<15} {average:>10.2f} {grade:>8}")
    
    print("  " + "=" * 50)

calculate_grades()

print()  # Empty line


# ============================================================================
# 3. PASSWORD VALIDATOR
# ============================================================================
print("=" * 60)
print("3. PASSWORD VALIDATOR")
print("=" * 60)

def validate_password(password):
    """Validate password strength."""
    errors = []
    
    # Check length
    if len(password) < 8:
        errors.append("Password must be at least 8 characters")
    
    # Check for uppercase
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if not has_upper:
        errors.append("Password must contain uppercase letter")
    
    # Check for lowercase
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
    if not has_lower:
        errors.append("Password must contain lowercase letter")
    
    # Check for digit
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit:
        errors.append("Password must contain a digit")
    
    # Return result
    if errors:
        print(f"  Password: '{password}'")
        print("  Validation failed:")
        for error in errors:
            print(f"    - {error}")
        return False
    else:
        print(f"  Password: '{password}'")
        print("  ✅ Password is valid!")
        return True

# Test passwords
passwords = ["weak", "Weak123", "StrongPass123"]
for pwd in passwords:
    validate_password(pwd)
    print()

print()  # Empty line


# ============================================================================
# 4. SHOPPING CART CALCULATOR
# ============================================================================
print("=" * 60)
print("4. SHOPPING CART CALCULATOR")
print("=" * 60)

def shopping_cart():
    """Calculate shopping cart total."""
    items = [
        {"name": "Laptop", "price": 999.99, "quantity": 1},
        {"name": "Mouse", "price": 29.99, "quantity": 2},
        {"name": "Keyboard", "price": 79.99, "quantity": 1}
    ]
    
    tax_rate = 0.08
    discount_threshold = 1000
    discount_rate = 0.10
    
    print("  Shopping Cart")
    print("  " + "=" * 50)
    print(f"  {'Item':<15} {'Price':>10} {'Qty':>5} {'Total':>10}")
    print("  " + "-" * 50)
    
    subtotal = 0
    for item in items:
        item_total = item["price"] * item["quantity"]
        subtotal += item_total
        print(f"  {item['name']:<15} ${item['price']:>9.2f} {item['quantity']:>5} ${item_total:>9.2f}")
    
    print("  " + "-" * 50)
    print(f"  {'Subtotal':<15} ${subtotal:>29.2f}")
    
    # Apply discount
    discount = 0
    if subtotal >= discount_threshold:
        discount = subtotal * discount_rate
        print(f"  {'Discount (10%)':<15} ${discount:>29.2f}")
    
    after_discount = subtotal - discount
    tax = after_discount * tax_rate
    total = after_discount + tax
    
    print(f"  {'Tax (8%)':<15} ${tax:>29.2f}")
    print("  " + "=" * 50)
    print(f"  {'TOTAL':<15} ${total:>29.2f}")

shopping_cart()

print()  # Empty line


# ============================================================================
# 5. PRIME NUMBER FINDER
# ============================================================================
print("=" * 60)
print("5. PRIME NUMBER FINDER")
print("=" * 60)

def is_prime(n):
    """Check if number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(limit):
    """Find all prime numbers up to limit."""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

print("  Prime numbers up to 50:")
primes = find_primes(50)
for i, prime in enumerate(primes, 1):
    print(f"    {prime:3}", end=" ")
    if i % 10 == 0:
        print()
print()

print()  # Empty line


# ============================================================================
# 6. MENU SYSTEM
# ============================================================================
print("=" * 60)
print("6. MENU SYSTEM")
print("=" * 60)

def menu_system():
    """Simple menu system (simulated)."""
    print("  Main Menu")
    print("  " + "=" * 30)
    print("  1. View Profile")
    print("  2. Edit Settings")
    print("  3. View Reports")
    print("  4. Exit")
    print("  " + "=" * 30)
    
    # Simulated menu selections
    choices = [1, 2, 3, 4]
    
    for choice in choices:
        print(f"\n  Selected option: {choice}")
        if choice == 1:
            print("    Displaying profile...")
        elif choice == 2:
            print("    Opening settings...")
        elif choice == 3:
            print("    Generating reports...")
        elif choice == 4:
            print("    Exiting...")
            break
        else:
            print("    Invalid choice!")

menu_system()

print()  # Empty line


# ============================================================================
# 7. DATA PROCESSING PIPELINE
# ============================================================================
print("=" * 60)
print("7. DATA PROCESSING PIPELINE")
print("=" * 60)

def process_data():
    """Process and filter data."""
    raw_data = [10, None, 20, -5, 30, None, 40, -10, 50]
    
    print("  Raw data:", raw_data)
    
    # Step 1: Remove None values
    step1 = []
    for item in raw_data:
        if item is not None:
            step1.append(item)
    print("  After removing None:", step1)
    
    # Step 2: Remove negative values
    step2 = []
    for item in step1:
        if item >= 0:
            step2.append(item)
    print("  After removing negatives:", step2)
    
    # Step 3: Calculate statistics
    if step2:
        total = sum(step2)
        average = total / len(step2)
        maximum = max(step2)
        minimum = min(step2)
        
        print("\n  Statistics:")
        print(f"    Count: {len(step2)}")
        print(f"    Sum: {total}")
        print(f"    Average: {average:.2f}")
        print(f"    Max: {maximum}")
        print(f"    Min: {minimum}")

process_data()

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL EXAMPLES SUMMARY:")
print("=" * 60)
print("These examples demonstrate:")
print("  - Combining conditionals and loops")
print("  - Using break and continue effectively")
print("  - Processing data with loops")
print("  - Creating interactive programs")
print("  - Real-world problem solving")
print("\nKey Patterns:")
print("  - Input validation with while loops")
print("  - Searching with break")
print("  - Filtering with continue")
print("  - Nested loops for 2D data")
print("  - Menu systems with loops")
print("=" * 60)

