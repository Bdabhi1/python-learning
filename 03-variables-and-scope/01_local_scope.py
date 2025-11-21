"""
Local Scope in Python

This file demonstrates how local scope works - variables defined inside functions
that can only be accessed within those functions.
"""

# ============================================================================
# 1. BASIC LOCAL SCOPE
# ============================================================================
print("=" * 60)
print("1. BASIC LOCAL SCOPE")
print("=" * 60)

def my_function():
    # This variable is LOCAL to my_function
    local_var = "I'm a local variable"
    print(f"Inside function: {local_var}")

# Call the function
my_function()

# Try to access local_var outside the function
# print(local_var)  # ❌ This would cause NameError!
print("local_var cannot be accessed outside the function")

print()  # Empty line


# ============================================================================
# 2. MULTIPLE LOCAL VARIABLES
# ============================================================================
print("=" * 60)
print("2. MULTIPLE LOCAL VARIABLES")
print("=" * 60)

def calculate_total(price, quantity):
    """
    Calculate total with tax.
    All variables here are LOCAL to this function.
    """
    # Local variables
    tax_rate = 0.08
    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax
    
    print(f"  Price per item: ${price}")
    print(f"  Quantity: {quantity}")
    print(f"  Tax rate: {tax_rate * 100}%")
    print(f"  Subtotal: ${subtotal:.2f}")
    print(f"  Tax: ${tax:.2f}")
    print(f"  Total: ${total:.2f}")
    
    return total

# Call the function
result = calculate_total(10, 2)

# These variables don't exist outside the function:
# print(tax_rate)  # ❌ NameError
# print(subtotal)  # ❌ NameError
print(f"\nResult returned: ${result:.2f}")
print("Local variables (tax_rate, subtotal, etc.) are not accessible outside")

print()  # Empty line


# ============================================================================
# 3. LOCAL VARIABLES ARE CREATED EACH TIME
# ============================================================================
print("=" * 60)
print("3. LOCAL VARIABLES ARE CREATED EACH TIME")
print("=" * 60)

def counter_function():
    """Each call creates a new local variable."""
    count = 0  # New local variable each time
    count += 1
    return count

# Call multiple times
print("Calling counter_function() multiple times:")
for i in range(5):
    result = counter_function()
    print(f"  Call {i+1}: {result}")

print("\nNote: Each call creates a fresh 'count' variable")
print("The variable doesn't persist between calls")

print()  # Empty line


# ============================================================================
# 4. PARAMETERS ARE LOCAL VARIABLES
# ============================================================================
print("=" * 60)
print("4. PARAMETERS ARE LOCAL VARIABLES")
print("=" * 60)

def greet(name, age):
    """
    Function parameters are also local variables.
    They exist only within the function.
    """
    # 'name' and 'age' are local to this function
    message = f"Hello, {name}! You are {age} years old."
    print(f"  {message}")
    return message

# Call the function
greet("Alice", 25)

# Parameters don't exist outside:
# print(name)  # ❌ NameError: name 'name' is not defined
# print(age)   # ❌ NameError: name 'age' is not defined

print("Parameters are local variables - not accessible outside the function")

print()  # Empty line


# ============================================================================
# 5. SAME NAME, DIFFERENT SCOPES
# ============================================================================
print("=" * 60)
print("5. SAME NAME, DIFFERENT SCOPES")
print("=" * 60)

# Global variable
x = "I'm global"

def function1():
    # Local variable with same name (shadows global)
    x = "I'm local in function1"
    print(f"  Inside function1: {x}")

def function2():
    # Different local variable with same name
    x = "I'm local in function2"
    print(f"  Inside function2: {x}")

print(f"Global x: {x}")
function1()
function2()
print(f"Global x (unchanged): {x}")

print("\nEach function has its own local 'x' variable")
print("They don't interfere with each other or the global 'x'")

print()  # Empty line


# ============================================================================
# 6. LOCAL VARIABLES IN CONDITIONAL BLOCKS
# ============================================================================
print("=" * 60)
print("6. LOCAL VARIABLES IN CONDITIONAL BLOCKS")
print("=" * 60)

def process_number(num):
    """Variables in if/else blocks are still local to the function."""
    if num > 0:
        result = "positive"
        message = f"The number is {result}"
    elif num < 0:
        result = "negative"
        message = f"The number is {result}"
    else:
        result = "zero"
        message = f"The number is {result}"
    
    # All these variables are accessible here (function scope)
    print(f"  Number: {num}")
    print(f"  Result: {result}")
    print(f"  Message: {message}")
    
    return result

process_number(5)
process_number(-3)
process_number(0)

print("\nVariables in if/else blocks are still local to the function")
print("They're accessible throughout the entire function")

print()  # Empty line


# ============================================================================
# 7. LOCAL VARIABLES IN LOOPS
# ============================================================================
print("=" * 60)
print("7. LOCAL VARIABLES IN LOOPS")
print("=" * 60)

def sum_numbers(numbers):
    """Loop variables are local to the function."""
    total = 0  # Local variable
    
    for num in numbers:  # 'num' is local to the loop, but accessible in function
        total += num
    
    # 'num' still exists here (last value from loop)
    print(f"  Numbers: {numbers}")
    print(f"  Total: {total}")
    print(f"  Last number processed: {num}")
    
    return total

result = sum_numbers([1, 2, 3, 4, 5])
print(f"  Returned: {result}")

print("\nNote: Loop variables persist after the loop in Python")
print("They're still local to the function, not the loop")

print()  # Empty line


# ============================================================================
# 8. NESTED FUNCTIONS - LOCAL TO OUTER FUNCTION
# ============================================================================
print("=" * 60)
print("8. NESTED FUNCTIONS - LOCAL TO OUTER FUNCTION")
print("=" * 60)

def outer_function():
    """Outer function with nested inner function."""
    outer_var = "I'm in outer function"
    
    def inner_function():
        """Inner function - also has local scope."""
        inner_var = "I'm in inner function"
        print(f"    Inner function sees: {outer_var}")
        print(f"    Inner function has: {inner_var}")
        # inner_var is local to inner_function
        # outer_var is from enclosing scope (we'll learn about this)
    
    print(f"  Outer function has: {outer_var}")
    inner_function()
    # print(inner_var)  # ❌ Would cause NameError - inner_var is local to inner_function

outer_function()

print("\nInner functions have their own local scope")
print("They can see outer function's variables, but outer can't see inner's")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("LOCAL SCOPE SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  1. Variables defined inside functions are LOCAL")
print("  2. Local variables exist only within the function")
print("  3. Local variables are created when function is called")
print("  4. Local variables are destroyed when function returns")
print("  5. Each function call creates new local variables")
print("  6. Parameters are also local variables")
print("  7. Variables in if/else/loops are still local to the function")
print("  8. Local variables cannot be accessed from outside the function")
print("=" * 60)

