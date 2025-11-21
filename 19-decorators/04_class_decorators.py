"""
Class Decorators in Python

This file demonstrates decorating classes and creating class-based decorators.
"""

from functools import wraps

# ============================================================================
# 1. DECORATING A CLASS
# ============================================================================
print("=" * 60)
print("1. DECORATING A CLASS")
print("=" * 60)

def add_method(cls):
    def new_method(self):
        return "New method added!"
    cls.new_method = new_method
    return cls

@add_method
class MyClass:
    def existing_method(self):
        return "Existing method"

obj = MyClass()
print(f"  {obj.existing_method()}")
print(f"  {obj.new_method()}")

print()  # Empty line


# ============================================================================
# 2. CLASS-BASED DECORATOR
# ============================================================================
print("=" * 60)
print("2. CLASS-BASED DECORATOR")
print("=" * 60)

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} called {self.count} times")
        return self.func(*args, **kwargs)

@CountCalls
def greet(name):
    return f"Hello, {name}!"

print(f"  {greet('Alice')}")
print(f"  {greet('Bob')}")

print()  # Empty line


# ============================================================================
# 3. CLASS-BASED DECORATOR WITH STATE
# ============================================================================
print("=" * 60)
print("3. CLASS-BASED DECORATOR WITH STATE")
print("=" * 60)

class Timer:
    def __init__(self, func):
        self.func = func
        self.total_time = 0
        self.call_count = 0
    
    def __call__(self, *args, **kwargs):
        import time
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        self.total_time += elapsed
        self.call_count += 1
        print(f"{self.func.__name__} call {self.call_count}: {elapsed:.4f}s")
        return result
    
    def stats(self):
        avg = self.total_time / self.call_count if self.call_count > 0 else 0
        return f"Total: {self.total_time:.4f}s, Calls: {self.call_count}, Avg: {avg:.4f}s"

@Timer
def slow_function():
    import time
    time.sleep(0.1)

slow_function()
slow_function()
print(f"  {slow_function.stats()}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("CLASS DECORATORS SUMMARY:")
print("=" * 60)
print("  - Can decorate classes to add methods/attributes")
print("  - Class-based decorators use __init__ and __call__")
print("  - Useful for maintaining state across calls")
print("  - Can track statistics, caching, etc.")
print("=" * 60)

