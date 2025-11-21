"""
Field Customization in Data Classes

This file demonstrates how to customize fields in data classes.
"""

from dataclasses import dataclass, field

# ============================================================================
# 1. FIELD OPTIONS
# ============================================================================
print("=" * 60)
print("1. FIELD OPTIONS")
print("=" * 60)

@dataclass
class Person:
    name: str
    age: int = field(default=0)
    email: str = field(default="", repr=False)  # Don't show in repr
    _id: int = field(init=False)  # Not in __init__
    
    def __post_init__(self):
        self._id = hash(self.name)

p = Person("Alice", 30, "alice@example.com")
print(f"  Person: {p}")  # email not shown (repr=False)
print(f"  ID: {p._id}")  # Set in __post_init__

print()  # Empty line


# ============================================================================
# 2. COMPARING FIELDS
# ============================================================================
print("=" * 60)
print("2. COMPARING FIELDS")
print("=" * 60)

@dataclass
class Person:
    name: str
    age: int
    email: str = field(compare=False)  # Not used in comparison

p1 = Person("Alice", 30, "alice@example.com")
p2 = Person("Alice", 30, "different@example.com")

print(f"  Person 1: {p1}")
print(f"  Person 2: {p2}")
print(f"  Equal: {p1 == p2}")  # True (email not compared)

print()  # Empty line


# ============================================================================
# 3. REPR CONTROL
# ============================================================================
print("=" * 60)
print("3. REPR CONTROL")
print("=" * 60)

@dataclass
class Account:
    username: str
    password: str = field(repr=False)  # Don't show password in repr
    balance: float = 0.0

account = Account("alice", "secret123", 1000.0)
print(f"  Account: {account}")  # Password not shown

print()  # Empty line


# ============================================================================
# 4. INIT CONTROL
# ============================================================================
print("=" * 60)
print("4. INIT CONTROL")
print("=" * 60)

@dataclass
class Product:
    name: str
    price: float
    discount: float = field(init=False, default=0.0)  # Not in __init__
    final_price: float = field(init=False)  # Computed in __post_init__
    
    def __post_init__(self):
        self.final_price = self.price * (1 - self.discount)

product = Product("Laptop", 1000.0)
print(f"  Product: {product}")
print(f"  Final price: ${product.final_price}")

print()  # Empty line


# ============================================================================
# 5. MULTIPLE FIELD OPTIONS
# ============================================================================
print("=" * 60)
print("5. MULTIPLE FIELD OPTIONS")
print("=" * 60)

@dataclass
class User:
    username: str
    email: str = field(
        default="",
        repr=False,  # Don't show in repr
        compare=False  # Don't use in comparison
    )
    created_at: str = field(init=False)  # Set in __post_init__
    
    def __post_init__(self):
        from datetime import datetime
        self.created_at = datetime.now().isoformat()

user = User("alice", "alice@example.com")
print(f"  User: {user}")  # email not shown
print(f"  Created: {user.created_at}")

print()  # Empty line


# ============================================================================
# 6. FIELD METADATA
# ============================================================================
print("=" * 60)
print("6. FIELD METADATA")
print("=" * 60)

@dataclass
class Person:
    name: str = field(metadata={"description": "Person's full name"})
    age: int = field(metadata={"description": "Person's age", "min": 0, "max": 150})

p = Person("Alice", 30)
print(f"  Person: {p}")
print("  Field metadata can store additional information")

print()  # Empty line


# ============================================================================
# 7. ACCESSING FIELD INFO
# ============================================================================
print("=" * 60)
print("7. ACCESSING FIELD INFO")
print("=" * 60)

from dataclasses import fields

@dataclass
class Example:
    name: str
    age: int = 0
    email: str = field(default="", repr=False)

print("  Field information:")
for f in fields(Example):
    print(f"    {f.name}: default={f.default}, repr={f.repr}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("FIELD CUSTOMIZATION SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Use field() for customization")
print("  - repr=False: Hide from __repr__")
print("  - compare=False: Exclude from comparison")
print("  - init=False: Not in __init__")
print("  - Use metadata for additional info")
print("  - Access field info with fields()")
print("=" * 60)

