"""
Encapsulation in Python

This file demonstrates encapsulation, access control, and properties.
"""

# ============================================================================
# 1. PUBLIC ATTRIBUTES
# ============================================================================
print("=" * 60)
print("1. PUBLIC ATTRIBUTES")
print("=" * 60)

class Person:
    def __init__(self, name):
        self.name = name  # Public attribute

person = Person("Alice")
print(f"  person.name: {person.name}")

person.name = "Bob"
print(f"  After change: {person.name}")

print()  # Empty line


# ============================================================================
# 2. PROTECTED ATTRIBUTES (CONVENTION)
# ============================================================================
print("=" * 60)
print("2. PROTECTED ATTRIBUTES (CONVENTION)")
print("=" * 60)

class Person:
    def __init__(self, name):
        self._name = name  # Protected (single underscore)
    
    def get_name(self):
        return self._name

person = Person("Alice")
print(f"  person._name: {person._name}")  # Still accessible
print(f"  person.get_name(): {person.get_name()}")

print("\n  Single underscore is a convention, not enforced")

print()  # Empty line


# ============================================================================
# 3. PRIVATE ATTRIBUTES (NAME MANGLING)
# ============================================================================
print("=" * 60)
print("3. PRIVATE ATTRIBUTES (NAME MANGLING)")
print("=" * 60)

class Person:
    def __init__(self, name):
        self.__name = name  # Private (double underscore)
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

person = Person("Alice")
print(f"  person.get_name(): {person.get_name()}")

# Direct access would fail (name mangling)
# print(person.__name)  # AttributeError

print("\n  Double underscore triggers name mangling")

print()  # Empty line


# ============================================================================
# 4. PROPERTIES FOR ENCAPSULATION
# ============================================================================
print("=" * 60)
print("4. PROPERTIES FOR ENCAPSULATION")
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
            raise ValueError("Temperature below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

temp = Temperature(25)
print(f"  Celsius: {temp.celsius}°C")
print(f"  Fahrenheit: {temp.fahrenheit}°F")

temp.celsius = 30
print(f"  After setting: {temp.celsius}°C")

print()  # Empty line


# ============================================================================
# 5. GETTERS AND SETTERS
# ============================================================================
print("=" * 60)
print("5. GETTERS AND SETTERS")
print("=" * 60)

class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    
    def get_balance(self):
        return self._balance
    
    def set_balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

account = BankAccount(1000)
print(f"  Balance: ${account.get_balance()}")

account.set_balance(1500)
print(f"  After set: ${account.get_balance()}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("ENCAPSULATION SUMMARY:")
print("=" * 60)
print("  - Public: no underscore (accessible anywhere)")
print("  - Protected: _single (convention, still accessible)")
print("  - Private: __double (name mangling)")
print("  - Use @property for controlled access")
print("  - Encapsulation bundles data and methods")
print("=" * 60)

