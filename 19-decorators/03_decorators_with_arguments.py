"""
Decorators with Arguments

This file demonstrates how to create decorators that accept arguments.
"""

from functools import wraps
import time

# ============================================================================
# 1. DECORATOR FACTORY PATTERN
# ============================================================================
print("=" * 60)
print("1. DECORATOR FACTORY PATTERN")
print("=" * 60)

def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hello():
    print("Hello!")

say_hello()

print("\n  Decorator factory: function that returns a decorator")

print()  # Empty line


# ============================================================================
# 2. TIMER DECORATOR WITH UNIT
# ============================================================================
print("=" * 60)
print("2. TIMER DECORATOR WITH UNIT")
print("=" * 60)

def timer(unit='seconds'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            elapsed = end - start
            if unit == 'milliseconds':
                elapsed *= 1000
            print(f"{func.__name__} took {elapsed:.2f} {unit}")
            return result
        return wrapper
    return decorator

@timer(unit='milliseconds')
def slow_function():
    time.sleep(0.1)

slow_function()

print()  # Empty line


# ============================================================================
# 3. RETRY DECORATOR
# ============================================================================
print("=" * 60)
print("3. RETRY DECORATOR")
print("=" * 60)

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.1)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success!"

try:
    result = unreliable_function()
    print(f"  {result}")
except ValueError as e:
    print(f"  Failed after retries: {e}")

print()  # Empty line


# ============================================================================
# 4. VALIDATION DECORATOR
# ============================================================================
print("=" * 60)
print("4. VALIDATION DECORATOR")
print("=" * 60)

def validate_types(**types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Simple validation example
            param_names = list(types.keys())
            for i, arg in enumerate(args):
                if i < len(param_names):
                    param_name = param_names[i]
                    expected_type = types[param_name]
                    if not isinstance(arg, expected_type):
                        raise TypeError(f"{param_name} must be {expected_type.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(a=int, b=int)
def add(a, b):
    return a + b

try:
    result = add(5, 3)
    print(f"  add(5, 3) = {result}")
    add("5", 3)  # This will raise TypeError
except TypeError as e:
    print(f"  Validation error: {e}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("DECORATORS WITH ARGUMENTS SUMMARY:")
print("=" * 60)
print("  - Decorator factory: function that returns a decorator")
print("  - Pattern: def decorator_factory(args): return decorator")
print("  - Allows decorators to be configurable")
print("  - Common use cases: retry, timing, validation, caching")
print("=" * 60)

