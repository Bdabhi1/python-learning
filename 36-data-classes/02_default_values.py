"""
Default Values in Data Classes

This file demonstrates how to use default values in data classes.
"""

from dataclasses import dataclass, field
from typing import List

# ============================================================================
# 1. SIMPLE DEFAULT VALUES
# ============================================================================
print("=" * 60)
print("1. SIMPLE DEFAULT VALUES")
print("=" * 60)

@dataclass
class Person:
    name: str
    age: int = 0
    email: str = ""

p1 = Person("Alice")
p2 = Person("Bob", 25)
p3 = Person("Charlie", 30, "charlie@example.com")

print(f"  Person 1: {p1}")
print(f"  Person 2: {p2}")
print(f"  Person 3: {p3}")

print()  # Empty line


# ============================================================================
# 2. DEFAULT FACTORY
# ============================================================================
print("=" * 60)
print("2. DEFAULT FACTORY")
print("=" * 60)

@dataclass
class ShoppingCart:
    items: List[str] = field(default_factory=list)
    total: float = 0.0

cart1 = ShoppingCart()
cart2 = ShoppingCart()

cart1.items.append("apple")
cart2.items.append("banana")

print(f"  Cart 1: {cart1}")
print(f"  Cart 2: {cart2}")
print("  Each cart has its own list (not shared)")

print()  # Empty line


# ============================================================================
# 3. MUTABLE DEFAULT VALUES
# ============================================================================
print("=" * 60)
print("3. MUTABLE DEFAULT VALUES")
print("=" * 60)

print("  Wrong - mutable default:")
print("    ")
print("    @dataclass")
print("    class BadExample:")
print("        items: List[str] = []  # Don't do this!")
print("  ")
print("  Correct - use default_factory:")
print("    ")
print("    @dataclass")
print("    class GoodExample:")
print("        items: List[str] = field(default_factory=list)")

print()  # Empty line


# ============================================================================
# 4. COMPLEX DEFAULT VALUES
# ============================================================================
print("=" * 60)
print("4. COMPLEX DEFAULT VALUES")
print("=" * 60)

@dataclass
class Configuration:
    host: str = "localhost"
    port: int = 8080
    timeout: int = 30
    debug: bool = False

config1 = Configuration()
config2 = Configuration(host="example.com", port=443)

print(f"  Config 1: {config1}")
print(f"  Config 2: {config2}")

print()  # Empty line


# ============================================================================
# 5. FIELD ORDERING
# ============================================================================
print("=" * 60)
print("5. FIELD ORDERING")
print("=" * 60)

print("  Fields without defaults must come first:")
print("    ")
print("    @dataclass")
print("    class Example:")
print("        required: str  # No default - must be first")
print("        optional: int = 0  # Has default - comes after")
print("  ")
print("  This is required for __init__() generation")

print()  # Empty line


# ============================================================================
# 6. DEFAULT WITH FACTORY FUNCTION
# ============================================================================
print("=" * 60)
print("6. DEFAULT WITH FACTORY FUNCTION")
print("=" * 60)

def create_default_tags():
    """Factory function for default tags"""
    return ["untagged"]

@dataclass
class Article:
    title: str
    content: str
    tags: List[str] = field(default_factory=create_default_tags)

article1 = Article("Title 1", "Content 1")
article2 = Article("Title 2", "Content 2", ["python", "tutorial"])

print(f"  Article 1: {article1}")
print(f"  Article 2: {article2}")

print()  # Empty line


# ============================================================================
# 7. OPTIONAL FIELDS
# ============================================================================
print("=" * 60)
print("7. OPTIONAL FIELDS")
print("=" * 60)

from typing import Optional

@dataclass
class User:
    username: str
    email: str
    phone: Optional[str] = None
    bio: Optional[str] = None

user1 = User("alice", "alice@example.com")
user2 = User("bob", "bob@example.com", phone="123-456-7890")

print(f"  User 1: {user1}")
print(f"  User 2: {user2}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("DEFAULT VALUES SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Use = for simple defaults")
print("  - Use field(default_factory=...) for mutable defaults")
print("  - Fields without defaults must come first")
print("  - Use Optional for optional fields")
print("  - Never use mutable defaults directly")
print("=" * 60)

