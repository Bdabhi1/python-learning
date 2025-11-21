"""
Decorator Syntax and Metadata Preservation

This file demonstrates the @ syntax and how to preserve function metadata.
"""

from functools import wraps

# ============================================================================
# 1. @ SYNTAX IS SYNTHACTIC SUGAR
# ============================================================================
print("=" * 60)
print("1. @ SYNTAX IS SYNTHACTIC SUGAR")
print("=" * 60)

def my_decorator(func):
    def wrapper():
        return func()
    return wrapper

# These are equivalent:
@my_decorator
def function1():
    pass

def function2():
    pass
function2 = my_decorator(function2)

print("  @decorator syntax is equivalent to manual decoration")

print()  # Empty line


# ============================================================================
# 2. PROBLEM: LOST METADATA
# ============================================================================
print("=" * 60)
print("2. PROBLEM: LOST METADATA")
print("=" * 60)

def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def my_function():
    """This is my function"""
    pass

print(f"  Function name: {my_function.__name__}")  # 'wrapper' (wrong!)
print(f"  Function doc: {my_function.__doc__}")    # None (lost!)

print("\n  Without @wraps, metadata is lost!")

print()  # Empty line


# ============================================================================
# 3. SOLUTION: USING @wraps
# ============================================================================
print("=" * 60)
print("3. SOLUTION: USING @wraps")
print("=" * 60)

def my_decorator(func):
    @wraps(func)  # Preserves metadata
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def my_function():
    """This is my function"""
    pass

print(f"  Function name: {my_function.__name__}")  # 'my_function' (correct!)
print(f"  Function doc: {my_function.__doc__}")     # 'This is my function' (preserved!)

print("\n  Always use @wraps to preserve function metadata!")

print()  # Empty line


# ============================================================================
# 4. PRESERVING ALL METADATA
# ============================================================================
print("=" * 60)
print("4. PRESERVING ALL METADATA")
print("=" * 60)

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

print(f"  __name__: {add.__name__}")
print(f"  __doc__: {add.__doc__}")
print(f"  __annotations__: {add.__annotations__}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("DECORATOR SYNTAX SUMMARY:")
print("=" * 60)
print("  - @decorator is syntactic sugar")
print("  - Always use @wraps to preserve metadata")
print("  - Without @wraps, function name becomes 'wrapper'")
print("  - @wraps preserves __name__, __doc__, __annotations__, etc.")
print("=" * 60)

