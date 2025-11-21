"""
Common Scope Issues and Solutions

This file demonstrates common scope-related errors and how to fix them.
Understanding these issues will help you debug your code more effectively.
"""

# ============================================================================
# ISSUE 1: UNBOUNDLOCALERROR - Accessing Before Assignment
# ============================================================================
print("=" * 60)
print("ISSUE 1: UNBOUNDLOCALERROR - Accessing Before Assignment")
print("=" * 60)

x = 10

def problematic_function():
    """
    This causes UnboundLocalError!
    Python sees 'x = 20' and decides x is local,
    but we're trying to print it before assigning.
    """
    # Uncomment to see the error:
    # print(x)  # ❌ UnboundLocalError: local variable 'x' referenced before assignment
    # x = 20
    pass

def solution1():
    """Solution: Use 'global' keyword."""
    global x
    print(f"  Reading x: {x}")
    x = 20
    print(f"  Modified x: {x}")

def solution2():
    """Solution: Use different variable name."""
    local_x = 20
    print(f"  Local x: {local_x}")
    print(f"  Global x: {x}")

print(f"Initial x: {x}")
solution1()
print(f"After solution1: {x}")
solution2()
print(f"After solution2: {x}")

print("\nProblem: Python sees assignment and makes variable local")
print("Solution: Declare 'global' before using, or use different name")

print()  # Empty line


# ============================================================================
# ISSUE 2: Modifying Global Without 'global' Keyword
# ============================================================================
print("=" * 60)
print("ISSUE 2: Modifying Global Without 'global' Keyword")
print("=" * 60)

counter = 0

def problematic_increment():
    """This creates a LOCAL variable, not modifying global."""
    counter = counter + 1  # ❌ UnboundLocalError!
    # Uncomment to see error
    pass

def solution_increment():
    """Solution: Use 'global' keyword."""
    global counter
    counter += 1
    print(f"  Counter: {counter}")

print(f"Initial counter: {counter}")
for i in range(3):
    solution_increment()
print(f"Final counter: {counter}")

print("\nProblem: Assignment creates local variable")
print("Solution: Use 'global' keyword to modify global")

print()  # Empty line


# ============================================================================
# ISSUE 3: Confusing Local and Global Variables
# ============================================================================
print("=" * 60)
print("ISSUE 3: Confusing Local and Global Variables")
print("=" * 60)

value = 100

def confusing_function():
    """Local variable shadows global - easy to confuse."""
    value = 200  # Creates LOCAL variable
    print(f"  Inside function: {value}")

print(f"Before function: {value}")
confusing_function()
print(f"After function: {value} (unchanged!)")

def clear_function():
    """Clear: Explicitly modify global."""
    global value
    value = 200
    print(f"  Inside function: {value}")

print(f"\nBefore clear_function: {value}")
clear_function()
print(f"After clear_function: {value} (changed!)")

print("\nProblem: Local variables with same name hide global")
print("Solution: Be explicit - use 'global' if you want to modify global")

print()  # Empty line


# ============================================================================
# ISSUE 4: Modifying List/Dict Without 'global' (Works, But Confusing)
# ============================================================================
print("=" * 60)
print("ISSUE 4: Modifying List/Dict Without 'global' (Works, But Confusing)")
print("=" * 60)

my_list = [1, 2, 3]

def modify_list():
    """This works! But why?"""
    my_list.append(4)  # ✅ Works - modifying the list
    print(f"  Modified list: {my_list}")

def reassign_list():
    """This doesn't work the way you might expect."""
    my_list = [10, 20, 30]  # Creates LOCAL variable!
    print(f"  Local list: {my_list}")

print(f"Initial list: {my_list}")
modify_list()
print(f"After modify_list: {my_list}")

reassign_list()
print(f"After reassign_list: {my_list} (unchanged!)")

def reassign_list_correct():
    """Correct way to reassign."""
    global my_list
    my_list = [10, 20, 30]
    print(f"  Reassigned list: {my_list}")

reassign_list_correct()
print(f"After reassign_list_correct: {my_list}")

print("\nKey Point:")
print("  - Modifying (append, etc.) works without 'global'")
print("  - Reassigning (=) requires 'global' keyword")
print("  - This is because assignment creates a new local variable")

print()  # Empty line


# ============================================================================
# ISSUE 5: Nested Functions - Forgetting 'nonlocal'
# ============================================================================
print("=" * 60)
print("ISSUE 5: Nested Functions - Forgetting 'nonlocal'")
print("=" * 60)

def outer():
    count = 0
    
    def inner_problematic():
        count += 1  # ❌ UnboundLocalError!
        # Uncomment to see error
        pass
    
    def inner_solution():
        nonlocal count
        count += 1
        print(f"    Count: {count}")
    
    print(f"  Initial count: {count}")
    inner_solution()
    print(f"  After inner: {count}")

outer()

print("\nProblem: Assignment in nested function creates local variable")
print("Solution: Use 'nonlocal' keyword to modify enclosing variable")

print()  # Empty line


# ============================================================================
# ISSUE 6: Loop Variables in Functions
# ============================================================================
print("=" * 60)
print("ISSUE 6: Loop Variables in Functions")
print("=" * 60)

def create_functions_problematic():
    """Problem: All functions reference same variable."""
    functions = []
    for i in range(3):
        functions.append(lambda: print(f"  i = {i}"))  # All print 2!
    return functions

def create_functions_solution():
    """Solution: Capture loop variable in closure."""
    functions = []
    for i in range(3):
        # Capture i in a closure
        functions.append(lambda x=i: print(f"  x = {x}"))
    return functions

print("Problematic version:")
funcs = create_functions_problematic()
for f in funcs:
    f()

print("\nSolution version:")
funcs = create_functions_solution()
for f in funcs:
    f()

print("\nProblem: Loop variable changes, all lambdas see final value")
print("Solution: Capture loop variable as default parameter")

print()  # Empty line


# ============================================================================
# ISSUE 7: Default Parameters with Mutable Objects
# ============================================================================
print("=" * 60)
print("ISSUE 7: Default Parameters with Mutable Objects")
print("=" * 60)

def problematic_function(items=[]):
    """Problem: Default parameter is mutable."""
    items.append("new")
    return items

def solution_function(items=None):
    """Solution: Use None and create new list."""
    if items is None:
        items = []
    items.append("new")
    return items

print("Problematic version:")
result1 = problematic_function()
print(f"  First call: {result1}")
result2 = problematic_function()
print(f"  Second call: {result2}")  # Unexpected: has 'new' from first call!

print("\nSolution version:")
result1 = solution_function()
print(f"  First call: {result1}")
result2 = solution_function()
print(f"  Second call: {result2}")  # Correct: fresh list each time

print("\nProblem: Default parameters are evaluated once")
print("Solution: Use None and create new object inside function")

print()  # Empty line


# ============================================================================
# ISSUE 8: Importing and Global Variables
# ============================================================================
print("=" * 60)
print("ISSUE 8: Importing and Global Variables")
print("=" * 60)

# When you import a module, its global variables are shared
# This is usually fine, but can cause confusion

# Simulating module behavior
module_var = "I'm a module variable"

def use_module_var():
    """Can read module variable."""
    print(f"  Module var: {module_var}")

def modify_module_var():
    """Need 'global' to modify."""
    global module_var
    module_var = "Modified"
    print(f"  Modified module var: {module_var}")

use_module_var()
modify_module_var()
use_module_var()

print("\nModule-level variables are global to that module")
print("Importing a module gives access to its globals")

print()  # Empty line


# ============================================================================
# SUMMARY OF COMMON ISSUES
# ============================================================================
print("=" * 60)
print("SUMMARY OF COMMON ISSUES")
print("=" * 60)
print("1. UnboundLocalError:")
print("   - Accessing variable before assignment")
print("   - Solution: Use 'global' or 'nonlocal'")
print()
print("2. Modifying Global:")
print("   - Assignment creates local variable")
print("   - Solution: Use 'global' keyword")
print()
print("3. Confusing Local/Global:")
print("   - Same name in different scopes")
print("   - Solution: Be explicit with 'global'")
print()
print("4. Modifying vs Reassigning:")
print("   - Modifying (append) works without 'global'")
print("   - Reassigning (=) requires 'global'")
print()
print("5. Nested Functions:")
print("   - Need 'nonlocal' to modify outer variable")
print("   - Solution: Use 'nonlocal' keyword")
print()
print("6. Loop Variables:")
print("   - All closures see final value")
print("   - Solution: Capture as default parameter")
print()
print("7. Default Parameters:")
print("   - Mutable defaults are shared")
print("   - Solution: Use None and create new object")
print("=" * 60)

