"""
Basic Decorators in Python

This file demonstrates the fundamental concepts of decorators.
"""

# ============================================================================
# 1. WHAT IS A DECORATOR?
# ============================================================================
print("=" * 60)
print("1. WHAT IS A DECORATOR?")
print("=" * 60)

print("  A decorator is a function that modifies another function.")
print("  It wraps the original function, adding functionality.")
print("  ")
print("  Decorators follow the decorator pattern:")
print("    - Take a function as input")
print("    - Return a modified function")
print("    - Can add behavior before, after, or around the function")

print()  # Empty line


# ============================================================================
# 2. BASIC DECORATOR FUNCTION
# ============================================================================
print("=" * 60)
print("2. BASIC DECORATOR FUNCTION")
print("=" * 60)

def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

def say_hello():
    print("Hello!")

# Manual decoration
say_hello = my_decorator(say_hello)
say_hello()

print()  # Empty line


# ============================================================================
# 3. USING @ SYNTAX
# ============================================================================
print("=" * 60)
print("3. USING @ SYNTAX")
print("=" * 60)

def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

print("\n  @decorator is syntactic sugar for:")
print("    function = decorator(function)")

print()  # Empty line


# ============================================================================
# 4. DECORATOR WITH ARGUMENTS
# ============================================================================
print("=" * 60)
print("4. DECORATOR WITH ARGUMENTS")
print("=" * 60)

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

result = add(5, 3)
print(f"  Result: {result}")

print()  # Empty line


# ============================================================================
# 5. DECORATOR THAT MODIFIES BEHAVIOR
# ============================================================================
print("=" * 60)
print("5. DECORATOR THAT MODIFIES BEHAVIOR")
print("=" * 60)

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet(name):
    return f"Hello, {name}!"

print(f"  {greet('Alice')}")

print()  # Empty line


# ============================================================================
# 6. MULTIPLE DECORATORS
# ============================================================================
print("=" * 60)
print("6. MULTIPLE DECORATORS")
print("=" * 60)

def bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic
def greet(name):
    return f"Hello, {name}!"

print(f"  {greet('Alice')}")

print("\n  Decorators are applied from bottom to top")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("BASIC DECORATORS SUMMARY:")
print("=" * 60)
print("  - Decorator is a function that takes a function")
print("  - Returns a modified/wrapped function")
print("  - Use @decorator syntax for convenience")
print("  - Can handle function arguments with *args, **kwargs")
print("  - Can chain multiple decorators")
print("=" * 60)

