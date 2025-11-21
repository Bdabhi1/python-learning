"""
Built-in Decorators in Python

This file demonstrates built-in decorators like @property, @staticmethod,
@classmethod, and @functools decorators.
"""

from functools import lru_cache, wraps
import time

# ============================================================================
# 1. @property DECORATOR
# ============================================================================
print("=" * 60)
print("1. @property DECORATOR")
print("=" * 60)

class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2

circle = Circle(5)
print(f"  Radius: {circle.radius}")
print(f"  Area: {circle.area:.2f}")

circle.radius = 10
print(f"  New radius: {circle.radius}")
print(f"  New area: {circle.area:.2f}")

print()  # Empty line


# ============================================================================
# 2. @staticmethod AND @classmethod
# ============================================================================
print("=" * 60)
print("2. @staticmethod AND @classmethod")
print("=" * 60)

class MathUtils:
    pi = 3.14159
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def from_string(cls, value):
        return cls(int(value))
    
    @classmethod
    def get_pi(cls):
        return cls.pi

print(f"  MathUtils.add(5, 3): {MathUtils.add(5, 3)}")
print(f"  MathUtils.get_pi(): {MathUtils.get_pi()}")

print()  # Empty line


# ============================================================================
# 3. @functools.lru_cache
# ============================================================================
print("=" * 60)
print("3. @functools.lru_cache")
print("=" * 60)

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# First call (computes)
start = time.time()
result1 = fibonacci(30)
time1 = time.time() - start

# Second call (uses cache)
start = time.time()
result2 = fibonacci(30)
time2 = time.time() - start

print(f"  fibonacci(30) = {result1}")
print(f"  First call: {time1:.6f}s")
print(f"  Cached call: {time2:.6f}s")
print(f"  Speedup: {time1/time2:.1f}x faster!")

print()  # Empty line


# ============================================================================
# 4. @functools.wraps
# ============================================================================
print("=" * 60)
print("4. @functools.wraps")
print("=" * 60)

def my_decorator(func):
    @wraps(func)  # Preserves function metadata
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def my_function():
    """This is my function"""
    pass

print(f"  Function name: {my_function.__name__}")
print(f"  Function doc: {my_function.__doc__}")

print("\n  @wraps preserves function metadata")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("BUILT-IN DECORATORS SUMMARY:")
print("=" * 60)
print("  - @property: Create computed attributes")
print("  - @staticmethod: Methods that don't need self/cls")
print("  - @classmethod: Methods that work with the class")
print("  - @lru_cache: Cache function results")
print("  - @wraps: Preserve function metadata")
print("=" * 60)

