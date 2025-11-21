"""
Name Binding and Scopes in Python

This file demonstrates how Python binds names to objects and resolves scopes.
"""

# ============================================================================
# 1. NAMES ARE REFERENCES
# ============================================================================
print("=" * 60)
print("1. NAMES ARE REFERENCES")
print("=" * 60)

print("  Names in Python are references to objects:")
print("    ")
x = [1, 2, 3]
y = x
print(f"  x = {x}")
print(f"  y = x")
print(f"  id(x) == id(y): {id(x) == id(y)}")

y.append(4)
print(f"  After y.append(4):")
print(f"  x = {x}")  # Also changed!
print(f"  y = {y}")

print()  # Empty line


# ============================================================================
# 2. SCOPE RESOLUTION (LEGB)
# ============================================================================
print("=" * 60)
print("2. SCOPE RESOLUTION (LEGB)")
print("=" * 60)

print("  Python resolves names in this order:")
print("    1. Local (L)")
print("    2. Enclosing (E)")
print("    3. Global (G)")
print("    4. Built-in (B)")

x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(f"    Inner sees: {x}")
    
    inner()
    print(f"  Outer sees: {x}")

outer()
print(f"  Global sees: {x}")

print()  # Empty line


# ============================================================================
# 3. GLOBAL KEYWORD
# ============================================================================
print("=" * 60)
print("3. GLOBAL KEYWORD")
print("=" * 60)

x = "global"

def func():
    global x
    x = "modified"
    print(f"  Inside func: {x}")

print(f"  Before func: {x}")
func()
print(f"  After func: {x}")

print()  # Empty line


# ============================================================================
# 4. NONLOCAL KEYWORD
# ============================================================================
print("=" * 60)
print("4. NONLOCAL KEYWORD")
print("=" * 60)

def outer():
    x = "outer"
    
    def inner():
        nonlocal x
        x = "modified"
        print(f"    Inside inner: {x}")
    
    print(f"  Before inner: {x}")
    inner()
    print(f"  After inner: {x}")

outer()

print()  # Empty line


# ============================================================================
# 5. NAMESPACES
# ============================================================================
print("=" * 60)
print("5. NAMESPACES")
print("=" * 60)

print("  Each scope has its own namespace:")
print("    ")
x = "global"

def func():
    y = "local"
    print(f"    Local namespace: {locals()}")
    print(f"    Global namespace: {globals().get('x')}")

func()
print(f"  Global namespace has x: {'x' in globals()}")

print()  # Empty line


# ============================================================================
# 6. NAME BINDING RULES
# ============================================================================
print("=" * 60)
print("6. NAME BINDING RULES")
print("=" * 60)

print("  Assignment creates binding:")
print("    x = 42  # Binds name 'x' to integer 42")
print("  ")
print("  Import creates binding:")
print("    import os  # Binds name 'os' to module")
print("  ")
print("  Function definition creates binding:")
print("    def func():  # Binds name 'func' to function")

x = 42
print(f"  x is bound to: {x}")

def func():
    return "test"

print(f"  func is bound to: {func}")

print()  # Empty line


# ============================================================================
# 7. CLOSURES
# ============================================================================
print("=" * 60)
print("7. CLOSURES")
print("=" * 60)

def outer(x):
    def inner():
        return x  # Captures x from enclosing scope
    return inner

closure = outer(42)
print(f"  Closure result: {closure()}")
print("  Inner function remembers outer's variable")

print()  # Empty line


# ============================================================================
# 8. DEL STATEMENT
# ============================================================================
print("=" * 60)
print("8. DEL STATEMENT")
print("=" * 60)

x = 42
print(f"  x exists: {'x' in globals()}")

del x
print(f"  After del x, x exists: {'x' in globals()}")
# print(x)  # Would raise NameError

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("NAME BINDING SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Names are references to objects")
print("  - LEGB rule for scope resolution")
print("  - Use 'global' to modify global variables")
print("  - Use 'nonlocal' to modify enclosing variables")
print("  - Each scope has its own namespace")
print("  - Closures capture enclosing variables")
print("  - 'del' removes name bindings")
print("=" * 60)

