"""
Higher-Order Functions

This file demonstrates functions that take or return other functions.
"""

from functools import reduce, partial

# ============================================================================
# 1. FUNCTIONS AS ARGUMENTS
# ============================================================================
print("=" * 60)
print("1. FUNCTIONS AS ARGUMENTS")
print("=" * 60)

def apply_twice(func, value):
    """Apply function twice to value"""
    return func(func(value))

def square(x):
    return x ** 2

result = apply_twice(square, 3)
print(f"  apply_twice(square, 3) = {result}")
print(f"  (3^2)^2 = {result}")

print()  # Empty line


# ============================================================================
# 2. FUNCTIONS AS RETURN VALUES
# ============================================================================
print("=" * 60)
print("2. FUNCTIONS AS RETURN VALUES")
print("=" * 60)

def make_multiplier(n):
    """Return a function that multiplies by n"""
    return lambda x: x * n

double = make_multiplier(2)
triple = make_multiplier(3)

print(f"  double(5) = {double(5)}")
print(f"  triple(5) = {triple(5)}")

print()  # Empty line


# ============================================================================
# 3. FUNCTION COMPOSITION
# ============================================================================
print("=" * 60)
print("3. FUNCTION COMPOSITION")
print("=" * 60)

def compose(f, g):
    """Compose two functions: f(g(x))"""
    return lambda x: f(g(x))

add_one = lambda x: x + 1
multiply_two = lambda x: x * 2

add_then_multiply = compose(multiply_two, add_one)
result = add_then_multiply(5)
print(f"  add_then_multiply(5) = {result}")
print(f"  (5 + 1) * 2 = {result}")

print()  # Empty line


# ============================================================================
# 4. PARTIAL APPLICATION
# ============================================================================
print("=" * 60)
print("4. PARTIAL APPLICATION")
print("=" * 60)

def multiply(x, y):
    return x * y

# Using functools.partial
double = partial(multiply, 2)
triple = partial(multiply, 3)

print(f"  double(5) = {double(5)}")
print(f"  triple(5) = {triple(5)}")

print()  # Empty line


# ============================================================================
# 5. DECORATORS AS HIGHER-ORDER FUNCTIONS
# ============================================================================
print("=" * 60)
print("5. DECORATORS AS HIGHER-ORDER FUNCTIONS")
print("=" * 60)

def timer(func):
    """Decorator that times function execution"""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"  {func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(0.1)
    return "Done"

result = slow_function()
print(f"  Result: {result}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("HIGHER-ORDER FUNCTIONS SUMMARY:")
print("=" * 60)
print("  - Functions that take functions as arguments")
print("  - Functions that return functions")
print("  - Function composition: combine functions")
print("  - Partial application: fix some arguments")
print("  - Decorators are higher-order functions")
print("=" * 60)

