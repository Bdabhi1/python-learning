"""
Metaclasses in Python

This file demonstrates metaclasses, which are classes of classes.
"""

# ============================================================================
# 1. BASIC METACLASS
# ============================================================================
print("=" * 60)
print("1. BASIC METACLASS")
print("=" * 60)

class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['created_by'] = 'Meta'
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

print(f"  MyClass.created_by: {MyClass.created_by}")

print()  # Empty line


# ============================================================================
# 2. METACLASS FOR VALIDATION
# ============================================================================
print("=" * 60)
print("2. METACLASS FOR VALIDATION")
print("=" * 60)

class ValidateMeta(type):
    def __new__(cls, name, bases, dct):
        if 'required_method' not in dct:
            raise TypeError(f"{name} must define 'required_method'")
        return super().__new__(cls, name, bases, dct)

class ValidClass(metaclass=ValidateMeta):
    def required_method(self):
        pass

print("  ValidClass created successfully")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("METACLASSES SUMMARY:")
print("=" * 60)
print("  - Metaclasses are classes of classes")
print("  - Control class creation")
print("  - Use __new__ to modify class creation")
print("  - Advanced feature, use sparingly")
print("=" * 60)

