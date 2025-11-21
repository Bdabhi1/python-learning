"""
Custom Iterators in Python

This file demonstrates how to create custom iterator classes.
"""

# ============================================================================
# 1. BASIC CUSTOM ITERATOR
# ============================================================================
print("=" * 60)
print("1. BASIC CUSTOM ITERATOR")
print("=" * 60)

class CountDown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

print("  CountDown from 5:")
for num in CountDown(5):
    print(f"    {num}")

print()  # Empty line


# ============================================================================
# 2. SEPARATE ITERATOR CLASS
# ============================================================================
print("=" * 60)
print("2. SEPARATE ITERATOR CLASS")
print("=" * 60)

class Range:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
    def __iter__(self):
        return RangeIterator(self.start, self.stop)

class RangeIterator:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        self.current += 1
        return self.current - 1

print("  Custom Range(0, 5):")
for num in Range(0, 5):
    print(f"    {num}")

print()  # Empty line


# ============================================================================
# 3. ITERATOR WITH CUSTOM LOGIC
# ============================================================================
print("=" * 60)
print("3. ITERATOR WITH CUSTOM LOGIC")
print("=" * 60)

class Fibonacci:
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        self.count += 1
        self.a, self.b = self.b, self.a + self.b
        return self.a

print("  First 10 Fibonacci numbers:")
for fib in Fibonacci(10):
    print(f"    {fib}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("CUSTOM ITERATORS SUMMARY:")
print("=" * 60)
print("  - Implement __iter__() and __next__()")
print("  - __iter__() returns self (or separate iterator)")
print("  - __next__() returns next value or raises StopIteration")
print("  - Can have separate iterator class")
print("=" * 60)

