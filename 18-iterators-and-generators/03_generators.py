"""
Generators in Python

This file demonstrates generator functions using the yield keyword.
"""

# ============================================================================
# 1. BASIC GENERATOR FUNCTION
# ============================================================================
print("=" * 60)
print("1. BASIC GENERATOR FUNCTION")
print("=" * 60)

def countdown(n):
    while n > 0:
        yield n
        n -= 1

print("  Countdown from 5:")
for num in countdown(5):
    print(f"    {num}")

print()  # Empty line


# ============================================================================
# 2. GENERATOR VS REGULAR FUNCTION
# ============================================================================
print("=" * 60)
print("2. GENERATOR VS REGULAR FUNCTION")
print("=" * 60)

# Regular function - returns all at once
def squares_list(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

# Generator function - yields one at a time
def squares_gen(n):
    for i in range(n):
        yield i ** 2

print(f"  Regular function (first 5): {squares_list(5)}")
print(f"  Generator (first 5): {list(squares_gen(5))}")

print("\n  Generator is memory efficient for large datasets!")

print()  # Empty line


# ============================================================================
# 3. FIBONACCI GENERATOR
# ============================================================================
print("=" * 60)
print("3. FIBONACCI GENERATOR")
print("=" * 60)

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print("  First 10 Fibonacci numbers:")
for _ in range(10):
    print(f"    {next(fib)}")

print()  # Empty line


# ============================================================================
# 4. GENERATOR WITH PARAMETERS
# ============================================================================
print("=" * 60)
print("4. GENERATOR WITH PARAMETERS")
print("=" * 60)

def range_generator(start, stop, step=1):
    current = start
    while current < stop:
        yield current
        current += step

print("  Range generator(0, 10, 2):")
for num in range_generator(0, 10, 2):
    print(f"    {num}")

print()  # Empty line


# ============================================================================
# 5. GENERATOR WITH send()
# ============================================================================
print("=" * 60)
print("5. GENERATOR WITH send()")
print("=" * 60)

def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

acc = accumulator()
next(acc)  # Start generator
print(f"  acc.send(10): {acc.send(10)}")
print(f"  acc.send(20): {acc.send(20)}")
print(f"  acc.send(5): {acc.send(5)}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("GENERATORS SUMMARY:")
print("=" * 60)
print("  - Use yield instead of return")
print("  - Automatically implement iterator protocol")
print("  - Memory efficient - generates on demand")
print("  - Can use send() to send values to generator")
print("  - Simpler than custom iterator classes")
print("=" * 60)

