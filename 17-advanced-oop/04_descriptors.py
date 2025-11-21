"""
Descriptors in Python

This file demonstrates descriptors for controlled attribute access.
"""

# ============================================================================
# 1. PROPERTY AS DESCRIPTOR
# ============================================================================
print("=" * 60)
print("1. PROPERTY AS DESCRIPTOR")
print("=" * 60)

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Too cold")
        self._celsius = value

temp = Temperature(25)
print(f"  temp.celsius: {temp.celsius}")

print()  # Empty line


# ============================================================================
# 2. CUSTOM DESCRIPTOR
# ============================================================================
print("=" * 60)
print("2. CUSTOM DESCRIPTOR")
print("=" * 60)

class ValidatedAttribute:
    def __init__(self, validator):
        self.validator = validator
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if self.validator(value):
            instance.__dict__[self.name] = value
        else:
            raise ValueError(f"Invalid value for {self.name}")

class Person:
    age = ValidatedAttribute(lambda x: 0 <= x <= 150)
    
    def __init__(self, age):
        self.age = age

person = Person(30)
print(f"  person.age: {person.age}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("DESCRIPTORS SUMMARY:")
print("=" * 60)
print("  - Descriptors control attribute access")
print("  - Implement __get__, __set__, __delete__")
print("  - Properties are descriptors")
print("  - Useful for validation and computed attributes")
print("=" * 60)

