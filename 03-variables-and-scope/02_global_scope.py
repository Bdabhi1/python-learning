"""
Global Scope in Python

This file demonstrates global scope - variables defined at module level
that can be accessed from anywhere in the module.
"""

# ============================================================================
# 1. BASIC GLOBAL SCOPE
# ============================================================================
print("=" * 60)
print("1. BASIC GLOBAL SCOPE")
print("=" * 60)

# Global variable (defined at module level)
global_var = "I'm a global variable"

def read_global():
    """Functions can READ global variables without any keyword."""
    print(f"  Inside function: {global_var}")

# Access from module level
print(f"Module level: {global_var}")

# Access from function
read_global()

print("\nGlobal variables can be accessed from anywhere in the module")

print()  # Empty line


# ============================================================================
# 2. READING VS MODIFYING GLOBAL VARIABLES
# ============================================================================
print("=" * 60)
print("2. READING VS MODIFYING GLOBAL VARIABLES")
print("=" * 60)

# Global variable
counter = 0

def read_counter():
    """Can read global without 'global' keyword."""
    print(f"  Counter value: {counter}")

def try_modify_without_global():
    """Trying to modify without 'global' keyword creates LOCAL variable."""
    counter = 10  # This creates a LOCAL variable, not modifying global!
    print(f"  Local counter: {counter}")

def modify_with_global():
    """Need 'global' keyword to modify global variable."""
    global counter
    counter = 20
    print(f"  Modified global counter: {counter}")

print(f"Initial counter: {counter}")
read_counter()
try_modify_without_global()
print(f"Counter after try_modify (unchanged): {counter}")
modify_with_global()
print(f"Counter after modify_with_global: {counter}")

print("\nKey Point: Reading is easy, modifying requires 'global' keyword")

print()  # Empty line


# ============================================================================
# 3. THE GLOBAL KEYWORD
# ============================================================================
print("=" * 60)
print("3. THE GLOBAL KEYWORD")
print("=" * 60)

# Global variables
x = 1
y = 2
z = 3

def modify_global():
    """Use 'global' keyword to modify global variables."""
    global x, y, z
    x = 10
    y = 20
    z = 30
    print(f"  Modified: x={x}, y={y}, z={z}")

print(f"Before: x={x}, y={y}, z={z}")
modify_global()
print(f"After: x={x}, y={y}, z={z}")

print()  # Empty line


# ============================================================================
# 4. CREATING GLOBAL VARIABLES FROM FUNCTIONS
# ============================================================================
print("=" * 60)
print("4. CREATING GLOBAL VARIABLES FROM FUNCTIONS")
print("=" * 60)

def create_global():
    """Can create global variables from inside functions."""
    global new_global_var
    new_global_var = "I was created in a function!"

# Variable doesn't exist yet
# print(new_global_var)  # ❌ Would cause NameError

# Create it
create_global()

# Now it exists
print(f"New global variable: {new_global_var}")

print("\nYou can create global variables from functions using 'global' keyword")

print()  # Empty line


# ============================================================================
# 5. GLOBAL VARIABLES PERSIST BETWEEN FUNCTION CALLS
# ============================================================================
print("=" * 60)
print("5. GLOBAL VARIABLES PERSIST BETWEEN FUNCTION CALLS")
print("=" * 60)

# Global counter
call_count = 0

def increment_counter():
    """Increment global counter each time function is called."""
    global call_count
    call_count += 1
    print(f"  Function called {call_count} time(s)")

print("Calling increment_counter() multiple times:")
for i in range(5):
    increment_counter()

print(f"\nFinal counter value: {call_count}")
print("Global variables persist and can be modified across function calls")

print()  # Empty line


# ============================================================================
# 6. SHADOWING - LOCAL VS GLOBAL WITH SAME NAME
# ============================================================================
print("=" * 60)
print("6. SHADOWING - LOCAL VS GLOBAL WITH SAME NAME")
print("=" * 60)

# Global variable
name = "Global Name"

def function_with_local():
    """Local variable shadows (hides) global variable."""
    name = "Local Name"  # Creates LOCAL variable
    print(f"  Inside function: {name}")

def function_with_global():
    """Using 'global' to modify global variable."""
    global name
    name = "Modified Global Name"
    print(f"  Inside function: {name}")

print(f"Initial global name: {name}")
function_with_local()
print(f"After function_with_local (unchanged): {name}")
function_with_global()
print(f"After function_with_global (changed): {name}")

print("\nLocal variables with same name 'shadow' (hide) global variables")
print("Use 'global' keyword to modify the global instead")

print()  # Empty line


# ============================================================================
# 7. COMMON MISTAKE - UNBOUNDLOCALERROR
# ============================================================================
print("=" * 60)
print("7. COMMON MISTAKE - UNBOUNDLOCALERROR")
print("=" * 60)

x = 10

def problematic_function():
    """
    This would cause UnboundLocalError!
    Python sees 'x = 20' and decides x is local,
    but we're trying to print it before assigning.
    """
    # print(x)  # ❌ UnboundLocalError!
    # x = 20
    
    # Uncomment above to see the error
    pass

def correct_function():
    """Correct way: declare 'global' first."""
    global x
    print(f"  Reading x: {x}")
    x = 20
    print(f"  Modified x: {x}")

print(f"Initial x: {x}")
correct_function()
print(f"Final x: {x}")

print("\nAlways declare 'global' before using the variable")

print()  # Empty line


# ============================================================================
# 8. WHEN TO USE GLOBAL VARIABLES
# ============================================================================
print("=" * 60)
print("8. WHEN TO USE GLOBAL VARIABLES")
print("=" * 60)

# Example: Configuration settings (sometimes acceptable)
MAX_RETRIES = 3
TIMEOUT = 30
DEBUG_MODE = True

def check_config():
    """Read configuration (no 'global' needed for reading)."""
    print(f"  Max retries: {MAX_RETRIES}")
    print(f"  Timeout: {TIMEOUT}")
    print(f"  Debug mode: {DEBUG_MODE}")

check_config()

print("\nGood use: Configuration constants")
print("Bad use: Frequently modified state (use parameters/return values instead)")

print()  # Empty line


# ============================================================================
# 9. BETTER ALTERNATIVE - PASSING VALUES
# ============================================================================
print("=" * 60)
print("9. BETTER ALTERNATIVE - PASSING VALUES")
print("=" * 60)

# Instead of using global variables, pass values as parameters

# ❌ Bad: Using global
# counter = 0
# def increment():
#     global counter
#     counter += 1

# ✅ Good: Using parameters and return values
def increment(counter):
    """Increment and return new value."""
    return counter + 1

counter = 0
print(f"Initial counter: {counter}")
counter = increment(counter)
print(f"After increment: {counter}")
counter = increment(counter)
print(f"After another increment: {counter}")

print("\nBest Practice: Use parameters and return values instead of globals")
print("This makes code more predictable and testable")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("GLOBAL SCOPE SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  1. Global variables are defined at module level")
print("  2. Can be READ from functions without 'global' keyword")
print("  3. Need 'global' keyword to MODIFY global variables")
print("  4. Global variables persist for entire program execution")
print("  5. Local variables with same name 'shadow' global variables")
print("  6. Use 'global' before modifying (not after)")
print("  7. Minimize global variables - prefer parameters/return values")
print("=" * 60)

