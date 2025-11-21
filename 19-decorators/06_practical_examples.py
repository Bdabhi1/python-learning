"""
Practical Decorator Examples

This file demonstrates real-world decorator patterns and use cases.
"""

from functools import wraps
import time
import logging

# ============================================================================
# 1. TIMING DECORATOR
# ============================================================================
print("=" * 60)
print("1. TIMING DECORATOR")
print("=" * 60)

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.1)
    return "Done"

result = slow_function()
print(f"  Result: {result}")

print()  # Empty line


# ============================================================================
# 2. LOGGING DECORATOR
# ============================================================================
print("=" * 60)
print("2. LOGGING DECORATOR")
print("=" * 60)

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

result = add(5, 3)
print(f"  Result: {result}")

print()  # Empty line


# ============================================================================
# 3. CACHING DECORATOR
# ============================================================================
print("=" * 60)
print("3. CACHING DECORATOR")
print("=" * 60)

def cache(func):
    cache_dict = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache_dict:
            cache_dict[key] = func(*args, **kwargs)
        return cache_dict[key]
    return wrapper

@cache
def expensive_function(n):
    time.sleep(0.1)  # Simulate expensive operation
    return n * 2

start = time.time()
result1 = expensive_function(5)
time1 = time.time() - start

start = time.time()
result2 = expensive_function(5)  # Cached
time2 = time.time() - start

print(f"  First call: {time1:.4f}s, Result: {result1}")
print(f"  Cached call: {time2:.4f}s, Result: {result2}")

print()  # Empty line


# ============================================================================
# 4. RATE LIMITING DECORATOR
# ============================================================================
print("=" * 60)
print("4. RATE LIMITING DECORATOR")
print("=" * 60)

def rate_limit(max_calls=3, period=1):
    def decorator(func):
        calls = []
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            calls[:] = [call_time for call_time in calls if now - call_time < period]
            if len(calls) >= max_calls:
                raise Exception(f"Rate limit exceeded: {max_calls} calls per {period}s")
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(max_calls=2, period=1)
def api_call():
    return "API response"

try:
    print(f"  {api_call()}")
    print(f"  {api_call()}")
    print(f"  {api_call()}")  # Should fail
except Exception as e:
    print(f"  Error: {e}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL EXAMPLES SUMMARY:")
print("=" * 60)
print("Decorators are useful for:")
print("  - Timing and profiling")
print("  - Logging and debugging")
print("  - Caching and memoization")
print("  - Rate limiting and throttling")
print("  - Validation and error handling")
print("=" * 60)

