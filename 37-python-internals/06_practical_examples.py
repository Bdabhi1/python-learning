"""
Practical Python Internals Examples

This file demonstrates real-world scenarios using Python internals knowledge.
"""

import sys
import gc
import dis
from functools import lru_cache

# ============================================================================
# 1. OBJECT IDENTITY VS EQUALITY
# ============================================================================
print("=" * 60)
print("1. OBJECT IDENTITY VS EQUALITY")
print("=" * 60)

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(f"  x = {x}")
print(f"  y = {y}")
print(f"  z = x")
print(f"  ")
print(f"  x == y: {x == y}")  # True (same values)
print(f"  x is y: {x is y}")  # False (different objects)
print(f"  x is z: {x is z}")  # True (same object)
print(f"  ")
print(f"  id(x): {id(x)}")
print(f"  id(y): {id(y)}")
print(f"  id(z): {id(z)}")

print()  # Empty line


# ============================================================================
# 2. REFERENCE COUNTING
# ============================================================================
print("=" * 60)
print("2. REFERENCE COUNTING")
print("=" * 60)

x = [1, 2, 3]
print(f"  Reference count of x: {sys.getrefcount(x)}")
print("  (Note: getrefcount includes its own reference)")

y = x
print(f"  After y = x: {sys.getrefcount(x)}")

del y
print(f"  After del y: {sys.getrefcount(x)}")

print()  # Empty line


# ============================================================================
# 3. INTEGER CACHING
# ============================================================================
print("=" * 60)
print("3. INTEGER CACHING")
print("=" * 60)

# Small integers are cached
a = 256
b = 256
print(f"  a = 256, b = 256")
print(f"  a is b: {a is b}")  # True (cached)

# Large integers are not cached
c = 257
d = 257
print(f"  c = 257, d = 257")
print(f"  c is d: {c is d}")  # May be False (not cached)

print()  # Empty line


# ============================================================================
# 4. MEMORY EFFICIENCY WITH __slots__
# ============================================================================
print("=" * 60)
print("4. MEMORY EFFICIENCY WITH __slots__")
print("=" * 60)

class RegularClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SlotsClass:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

print("  Creating 1000 instances:")
regular_instances = [RegularClass(i, i+1) for i in range(1000)]
slots_instances = [SlotsClass(i, i+1) for i in range(1000)]

print(f"    Regular class size: ~{sys.getsizeof(regular_instances)} bytes")
print(f"    Slots class size: ~{sys.getsizeof(slots_instances)} bytes")
print("    __slots__ saves memory with many instances")

print()  # Empty line


# ============================================================================
# 5. GARBAGE COLLECTION
# ============================================================================
print("=" * 60)
print("5. GARBAGE COLLECTION")
print("=" * 60)

print("  Garbage collection statistics:")
stats = gc.get_stats()
for i, stat in enumerate(stats):
    print(f"    Generation {i}: {stat}")

print(f"  ")
print(f"  Collection counts: {gc.get_count()}")
print(f"  ")
print("  Forcing garbage collection:")
collected = gc.collect()
print(f"    Collected {collected} objects")

print()  # Empty line


# ============================================================================
# 6. BYTECODE OPTIMIZATION
# ============================================================================
print("=" * 60)
print("6. BYTECODE OPTIMIZATION")
print("=" * 60)

def slow_version():
    result = 0
    for i in range(100):
        result += i
    return result

@lru_cache(maxsize=128)
def cached_function(n):
    return sum(range(n))

print("  Slow version bytecode:")
dis.dis(slow_version)
print("  ")
print("  Using caching for optimization:")
print(f"    cached_function(100): {cached_function(100)}")
print(f"    cached_function(100): {cached_function(100)} (cached)")

print()  # Empty line


# ============================================================================
# 7. FRAME INSPECTION
# ============================================================================
print("=" * 60)
print("7. FRAME INSPECTION")
print("=" * 60)

def inspect_frame():
    frame = sys._getframe()
    print(f"    Current function: {frame.f_code.co_name}")
    print(f"    File: {frame.f_code.co_filename}")
    print(f"    Line number: {frame.f_lineno}")
    print(f"    Local variables: {list(frame.f_locals.keys())}")

print("  Frame inspection:")
inspect_frame()

print()  # Empty line


# ============================================================================
# 8. CODE OBJECT INSPECTION
# ============================================================================
print("=" * 60)
print("8. CODE OBJECT INSPECTION")
print("=" * 60)

def example_function(x, y, z=10):
    local_var = x + y + z
    return local_var

code = example_function.__code__

print("  Code object inspection:")
print(f"    Function name: {code.co_name}")
print(f"    Argument count: {code.co_argcount}")
print(f"    Variable names: {code.co_varnames}")
print(f"    Constants: {code.co_consts}")
print(f"    Names: {code.co_names}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL INTERNALS EXAMPLES SUMMARY:")
print("=" * 60)
print("Real-world Applications:")
print("  - Understanding object identity vs equality")
print("  - Reference counting and memory management")
print("  - Integer caching behavior")
print("  - Memory optimization with __slots__")
print("  - Garbage collection monitoring")
print("  - Bytecode analysis for optimization")
print("  - Frame and code object inspection")
print("=" * 60)

