"""
Nonlocal Scope in Python

This file demonstrates the 'nonlocal' keyword used in nested functions
to modify variables from enclosing (outer) functions.
"""

# ============================================================================
# 1. BASIC NONLOCAL
# ============================================================================
print("=" * 60)
print("1. BASIC NONLOCAL")
print("=" * 60)

def outer_function():
    """Outer function with a variable."""
    outer_var = "I'm in outer function"
    
    def inner_function():
        """Inner function that modifies outer variable."""
        nonlocal outer_var  # Refers to outer_var in outer_function
        outer_var = "Modified by inner function"
        print(f"    Inside inner: {outer_var}")
    
    print(f"  Before inner: {outer_var}")
    inner_function()
    print(f"  After inner: {outer_var}")

outer_function()

print("\n'nonlocal' allows inner function to modify outer function's variable")

print()  # Empty line


# ============================================================================
# 2. WITHOUT NONLOCAL (CREATES LOCAL VARIABLE)
# ============================================================================
print("=" * 60)
print("2. WITHOUT NONLOCAL (CREATES LOCAL VARIABLE)")
print("=" * 60)

def outer_function():
    """Outer function with a variable."""
    outer_var = "I'm in outer function"
    
    def inner_function():
        """Without 'nonlocal', this creates a LOCAL variable."""
        outer_var = "New local variable"  # Creates LOCAL variable!
        print(f"    Inside inner: {outer_var}")
    
    print(f"  Before inner: {outer_var}")
    inner_function()
    print(f"  After inner: {outer_var} (unchanged!)")

outer_function()

print("\nWithout 'nonlocal', assignment creates a LOCAL variable")
print("The outer variable remains unchanged")

print()  # Empty line


# ============================================================================
# 3. READING WITHOUT NONLOCAL
# ============================================================================
print("=" * 60)
print("3. READING WITHOUT NONLOCAL")
print("=" * 60)

def outer_function():
    """Outer function with a variable."""
    outer_var = "I'm in outer function"
    
    def inner_function():
        """Can READ outer variable without 'nonlocal'."""
        print(f"    Reading outer_var: {outer_var}")  # ✅ Works!
        # No 'nonlocal' needed for reading
    
    inner_function()

outer_function()

print("\nYou can READ outer variables without 'nonlocal'")
print("'nonlocal' is only needed for MODIFYING")

print()  # Empty line


# ============================================================================
# 4. MULTIPLE LEVELS OF NESTING
# ============================================================================
print("=" * 60)
print("4. MULTIPLE LEVELS OF NESTING")
print("=" * 60)

def level1():
    """First level."""
    var = "Level 1"
    
    def level2():
        """Second level."""
        var = "Level 2"
        
        def level3():
            """Third level - modifies level2's var."""
            nonlocal var  # Modifies var in level2 (nearest enclosing)
            var = "Modified in Level 3"
            print(f"        Level 3: {var}")
        
        print(f"      Before level3: {var}")
        level3()
        print(f"      After level3: {var}")
    
    print(f"    Before level2: {var}")
    level2()
    print(f"    After level2: {var}")

level1()

print("\n'nonlocal' modifies the variable in the nearest enclosing scope")
print("In this case, it modifies level2's 'var', not level1's")

print()  # Empty line


# ============================================================================
# 5. COUNTER EXAMPLE WITH NONLOCAL
# ============================================================================
print("=" * 60)
print("5. COUNTER EXAMPLE WITH NONLOCAL")
print("=" * 60)

def create_counter():
    """Factory function that creates a counter."""
    count = 0  # Variable in outer function
    
    def increment():
        """Increment the counter."""
        nonlocal count
        count += 1
        return count
    
    def decrement():
        """Decrement the counter."""
        nonlocal count
        count -= 1
        return count
    
    def get_count():
        """Get current count."""
        return count  # Can read without nonlocal
    
    # Return functions that can access 'count'
    return increment, decrement, get_count

# Create a counter
inc, dec, get = create_counter()

print("Using counter:")
print(f"  Initial count: {get()}")
print(f"  After increment: {inc()}")
print(f"  After increment: {inc()}")
print(f"  After increment: {inc()}")
print(f"  After decrement: {dec()}")
print(f"  Final count: {get()}")

print("\nThis is a 'closure' - inner functions 'remember' outer variables")
print("Useful for creating stateful functions")

print()  # Empty line


# ============================================================================
# 6. NONLOCAL VS GLOBAL
# ============================================================================
print("=" * 60)
print("6. NONLOCAL VS GLOBAL")
print("=" * 60)

# Global variable
global_var = "I'm global"

def outer_function():
    """Outer function with local variable."""
    local_var = "I'm local to outer"
    
    def inner_function():
        """Inner function accessing different scopes."""
        # Can read global without any keyword
        print(f"    Reading global: {global_var}")
        
        # Can read local (outer) without nonlocal
        print(f"    Reading local (outer): {local_var}")
        
        # To modify global, use 'global'
        global global_var
        global_var = "Modified global"
        
        # To modify outer's local, use 'nonlocal'
        nonlocal local_var
        local_var = "Modified local (outer)"
        
        print(f"    After modifications:")
        print(f"      global_var: {global_var}")
        print(f"      local_var: {local_var}")
    
    print(f"  Before inner:")
    print(f"    global_var: {global_var}")
    print(f"    local_var: {local_var}")
    
    inner_function()
    
    print(f"  After inner:")
    print(f"    global_var: {global_var}")
    print(f"    local_var: {local_var}")

print(f"Before outer:")
print(f"  global_var: {global_var}")

outer_function()

print(f"\nAfter outer:")
print(f"  global_var: {global_var}")

print("\n'global' modifies module-level variables")
print("'nonlocal' modifies enclosing function's variables")

print()  # Empty line


# ============================================================================
# 7. PRACTICAL EXAMPLE - ACCUMULATOR
# ============================================================================
print("=" * 60)
print("7. PRACTICAL EXAMPLE - ACCUMULATOR")
print("=" * 60)

def create_accumulator(initial_value=0):
    """Create an accumulator that keeps a running total."""
    total = initial_value
    
    def add(value):
        """Add value to total."""
        nonlocal total
        total += value
        return total
    
    def subtract(value):
        """Subtract value from total."""
        nonlocal total
        total -= value
        return total
    
    def reset():
        """Reset total to initial value."""
        nonlocal total
        total = initial_value
        return total
    
    def get_total():
        """Get current total."""
        return total
    
    return add, subtract, reset, get_total

# Create an accumulator starting at 10
add, subtract, reset, get_total = create_accumulator(10)

print("Using accumulator:")
print(f"  Initial total: {get_total()}")
print(f"  Add 5: {add(5)}")
print(f"  Add 3: {add(3)}")
print(f"  Subtract 2: {subtract(2)}")
print(f"  Current total: {get_total()}")
print(f"  Reset: {reset()}")
print(f"  After reset: {get_total()}")

print("\nThis pattern is useful for maintaining state in closures")

print()  # Empty line


# ============================================================================
# 8. WHEN TO USE NONLOCAL
# ============================================================================
print("=" * 60)
print("8. WHEN TO USE NONLOCAL")
print("=" * 60)

print("Use 'nonlocal' when:")
print("  ✅ You have nested functions")
print("  ✅ Inner function needs to modify outer function's variable")
print("  ✅ Creating closures (functions that remember state)")
print("  ✅ Factory functions that create stateful functions")
print("\nAvoid 'nonlocal' when:")
print("  ❌ You can pass values as parameters instead")
print("  ❌ You can return values instead")
print("  ❌ The code becomes hard to understand")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("NONLOCAL SCOPE SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  1. 'nonlocal' is used in nested functions")
print("  2. Allows inner function to MODIFY outer function's variable")
print("  3. Not needed for READING outer variables")
print("  4. Without 'nonlocal', assignment creates LOCAL variable")
print("  5. Modifies variable in nearest enclosing scope")
print("  6. Useful for closures and factory functions")
print("  7. Use sparingly - prefer parameters/return values when possible")
print("=" * 60)

