"""
Multiple Inheritance and MRO in Python

This file demonstrates multiple inheritance and Method Resolution Order (MRO).
"""

# ============================================================================
# 1. BASIC MULTIPLE INHERITANCE
# ============================================================================
print("=" * 60)
print("1. BASIC MULTIPLE INHERITANCE")
print("=" * 60)

class A:
    def method(self):
        return "A"

class B:
    def method(self):
        return "B"

class C(A, B):
    pass

c = C()
print(f"  c.method(): {c.method()}")
print(f"  MRO: {C.__mro__}")

print()  # Empty line


# ============================================================================
# 2. DIAMOND PROBLEM
# ============================================================================
print("=" * 60)
print("2. DIAMOND PROBLEM")
print("=" * 60)

class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

d = D()
print(f"  d.method(): {d.method()}")
print(f"  MRO: {D.__mro__}")

print()  # Empty line


# ============================================================================
# 3. USING super()
# ============================================================================
print("=" * 60)
print("3. USING super()")
print("=" * 60)

class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return f"B -> {super().method()}"

class C(A):
    def method(self):
        return f"C -> {super().method()}"

class D(B, C):
    def method(self):
        return f"D -> {super().method()}"

d = D()
print(f"  d.method(): {d.method()}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("MULTIPLE INHERITANCE SUMMARY:")
print("=" * 60)
print("  - Python supports multiple inheritance")
print("  - MRO determines method resolution order")
print("  - Use __mro__ to see resolution order")
print("  - super() follows MRO")
print("=" * 60)

