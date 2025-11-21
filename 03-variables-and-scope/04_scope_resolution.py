"""
Scope Resolution in Python - LEGB Rule

This file demonstrates how Python searches for variables using the LEGB rule:
Local → Enclosing → Global → Built-in
"""

# ============================================================================
# 1. THE LEGB RULE
# ============================================================================
print("=" * 60)
print("1. THE LEGB RULE")
print("=" * 60)

print("Python searches for variables in this order:")
print("  L - Local:      Current function's namespace")
print("  E - Enclosing:  Enclosing functions' namespaces")
print("  G - Global:     Module's namespace")
print("  B - Built-in:   Python's built-in names")
print()

# Built-in (B)
# 'print' is a built-in function

# Global (G)
x = "I'm global"

def outer():
    # Enclosing (E)
    x = "I'm enclosing"
    
    def inner():
        # Local (L)
        x = "I'm local"
        print(f"    Local scope: {x}")
    
    print(f"  Enclosing scope: {x}")
    inner()

print(f"Global scope: {x}")
outer()
print(f"Global scope (unchanged): {x}")

print("\nPython finds the first match in LEGB order")

print()  # Empty line


# ============================================================================
# 2. LOCAL SCOPE FIRST
# ============================================================================
print("=" * 60)
print("2. LOCAL SCOPE FIRST")
print("=" * 60)

# Global variable
name = "Global Name"

def my_function():
    # Local variable (found first, shadows global)
    name = "Local Name"
    print(f"  Inside function: {name}")

print(f"Global: {name}")
my_function()
print(f"Global (unchanged): {name}")

print("\nLocal variables are found first, so they 'shadow' (hide) global ones")

print()  # Empty line


# ============================================================================
# 3. ENCLOSING SCOPE
# ============================================================================
print("=" * 60)
print("3. ENCLOSING SCOPE")
print("=" * 60)

def outer():
    # Enclosing scope
    outer_var = "I'm in enclosing scope"
    
    def inner():
        # No local 'outer_var', so Python looks in enclosing scope
        print(f"    Found in enclosing: {outer_var}")
    
    inner()

outer()

print("\nIf not found locally, Python searches enclosing functions")

print()  # Empty line


# ============================================================================
# 4. GLOBAL SCOPE
# ============================================================================
print("=" * 60)
print("4. GLOBAL SCOPE")
print("=" * 60)

# Global variable
global_var = "I'm global"

def my_function():
    # No local or enclosing, so Python looks in global scope
    print(f"  Found in global: {global_var}")

my_function()

print("\nIf not found locally or in enclosing, Python searches global scope")

print()  # Empty line


# ============================================================================
# 5. BUILT-IN SCOPE
# ============================================================================
print("=" * 60)
print("5. BUILT-IN SCOPE")
print("=" * 60)

# 'len' is a built-in function
def my_function():
    # No local 'len', so Python uses built-in
    result = len("Hello")
    print(f"  Using built-in len(): {result}")

my_function()

# But you can shadow built-ins (not recommended!)
def my_function():
    len = 5  # Shadows built-in 'len'
    print(f"  Local len: {len}")
    # len("Hello")  # ❌ Would cause TypeError - len is now an int!

my_function()

print("\nBuilt-ins are found last, but can be shadowed (avoid this!)")

print()  # Empty line


# ============================================================================
# 6. COMPLETE LEGB EXAMPLE
# ============================================================================
print("=" * 60)
print("6. COMPLETE LEGB EXAMPLE")
print("=" * 60)

# Built-in (B): print, len, etc.

# Global (G)
x = "global x"
y = "global y"

def outer():
    # Enclosing (E)
    x = "enclosing x"
    z = "enclosing z"
    
    def inner():
        # Local (L)
        x = "local x"
        w = "local w"
        
        print("Inside inner():")
        print(f"  x = {x} (found in Local)")
        print(f"  y = {y} (found in Global - not in Local or Enclosing)")
        print(f"  z = {z} (found in Enclosing)")
        print(f"  w = {w} (found in Local)")
        print(f"  len('test') = {len('test')} (found in Built-in)")
    
    print("Inside outer():")
    print(f"  x = {x} (found in Enclosing)")
    print(f"  y = {y} (found in Global)")
    inner()

print("At module level:")
print(f"  x = {x} (found in Global)")
print(f"  y = {y} (found in Global)")

outer()

print()  # Empty line


# ============================================================================
# 7. SHADOWING EXAMPLES
# ============================================================================
print("=" * 60)
print("7. SHADOWING EXAMPLES")
print("=" * 60)

# Global
name = "Global"

def level1():
    # Enclosing
    name = "Level 1"
    
    def level2():
        # Local
        name = "Level 2"
        print(f"      Level 2 sees: {name} (Local)")
    
    print(f"    Level 1 sees: {name} (Enclosing)")
    level2()

print(f"Global sees: {name} (Global)")
level1()

print("\nEach level can have its own 'name' variable")
print("Inner scopes shadow outer scopes")

print()  # Empty line


# ============================================================================
# 8. ACCESSING OUTER SCOPES EXPLICITLY
# ============================================================================
print("=" * 60)
print("8. ACCESSING OUTER SCOPES EXPLICITLY")
print("=" * 60)

# Global
counter = 0

def outer():
    # Enclosing
    counter = 10
    
    def inner():
        # Local
        counter = 20
        print(f"    Local counter: {counter}")
        
        # Can't directly access enclosing or global with same name
        # But we can use nonlocal or global to modify them
        
        # To modify enclosing:
        nonlocal counter  # Now refers to enclosing
        counter = 30
        print(f"    After nonlocal: {counter} (enclosing)")
        
        # To modify global (need to use different approach or rename)
        # global counter  # Would refer to global, not enclosing
    
    print(f"  Before inner: {counter} (enclosing)")
    inner()
    print(f"  After inner: {counter} (enclosing)")

print(f"Before outer: {counter} (global)")
outer()
print(f"After outer: {counter} (global)")

print("\n'nonlocal' and 'global' keywords let you explicitly choose scope")

print()  # Empty line


# ============================================================================
# 9. PRACTICAL EXAMPLE - CONFIGURATION
# ============================================================================
print("=" * 60)
print("9. PRACTICAL EXAMPLE - CONFIGURATION")
print("=" * 60)

# Global configuration
DEBUG = False
LOG_LEVEL = "INFO"

def process_data():
    """Process data with configuration."""
    # Uses global DEBUG and LOG_LEVEL
    if DEBUG:
        print(f"  Debug mode: Processing with log level {LOG_LEVEL}")
    else:
        print(f"  Production mode: Log level {LOG_LEVEL}")

def debug_mode():
    """Enable debug mode."""
    global DEBUG
    DEBUG = True
    print(f"  Debug mode enabled")

print("Initial configuration:")
print(f"  DEBUG: {DEBUG}")
print(f"  LOG_LEVEL: {LOG_LEVEL}")

process_data()
debug_mode()
process_data()

print("\nFunctions can read globals and modify them with 'global' keyword")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("SCOPE RESOLUTION (LEGB) SUMMARY:")
print("=" * 60)
print("Search Order:")
print("  1. Local (L):      Current function")
print("  2. Enclosing (E):  Outer functions")
print("  3. Global (G):     Module level")
print("  4. Built-in (B):   Python built-ins")
print("\nKey Points:")
print("  - Python searches in LEGB order")
print("  - First match wins (inner shadows outer)")
print("  - Use 'global' to modify global variables")
print("  - Use 'nonlocal' to modify enclosing variables")
print("  - Can read from outer scopes without keywords")
print("  - Be careful not to shadow built-ins")
print("=" * 60)

