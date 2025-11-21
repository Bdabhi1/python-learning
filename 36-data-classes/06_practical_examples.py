"""
Practical Data Class Examples

This file demonstrates real-world data class scenarios.
"""

from dataclasses import dataclass, field, asdict, astuple, replace
from typing import List, Optional
from datetime import datetime

# ============================================================================
# 1. USER MANAGEMENT
# ============================================================================
print("=" * 60)
print("1. USER MANAGEMENT")
print("=" * 60)

@dataclass
class User:
    username: str
    email: str
    age: int
    is_active: bool = True
    created_at: str = field(init=False)
    
    def __post_init__(self):
        self.created_at = datetime.now().isoformat()

user = User("alice", "alice@example.com", 30)
print(f"  User: {user}")
print(f"  Created: {user.created_at}")

print()  # Empty line


# ============================================================================
# 2. SHOPPING CART
# ============================================================================
print("=" * 60)
print("2. SHOPPING CART")
print("=" * 60)

@dataclass
class CartItem:
    product_id: int
    quantity: int
    price: float
    
    @property
    def total(self):
        return self.quantity * self.price

@dataclass
class ShoppingCart:
    items: List[CartItem] = field(default_factory=list)
    
    def add_item(self, item: CartItem):
        self.items.append(item)
    
    @property
    def total(self):
        return sum(item.total for item in self.items)

cart = ShoppingCart()
cart.add_item(CartItem(1, 2, 10.0))
cart.add_item(CartItem(2, 1, 25.0))
print(f"  Cart total: ${cart.total}")

print()  # Empty line


# ============================================================================
# 3. CONFIGURATION OBJECT
# ============================================================================
print("=" * 60)
print("3. CONFIGURATION OBJECT")
print("=" * 60)

@dataclass(frozen=True)
class DatabaseConfig:
    host: str
    port: int
    database: str
    username: str
    password: str = field(repr=False)  # Don't show password
    timeout: int = 30

config = DatabaseConfig(
    "localhost", 5432, "mydb", "user", "secret", 60
)
print(f"  Config: {config}")
print("  Config is immutable (frozen)")

print()  # Empty line


# ============================================================================
# 4. API RESPONSE
# ============================================================================
print("=" * 60)
print("4. API RESPONSE")
print("=" * 60)

@dataclass
class APIResponse:
    status_code: int
    data: dict
    message: Optional[str] = None
    timestamp: str = field(init=False)
    
    def __post_init__(self):
        self.timestamp = datetime.now().isoformat()
    
    def to_dict(self):
        return asdict(self)

response = APIResponse(200, {"user_id": 123}, "Success")
print(f"  Response: {response}")
print(f"  As dict: {response.to_dict()}")

print()  # Empty line


# ============================================================================
# 5. USING asdict() AND astuple()
# ============================================================================
print("=" * 60)
print("5. USING asdict() AND astuple()")
print("=" * 60)

@dataclass
class Point:
    x: int
    y: int

p = Point(1, 2)
print(f"  Point: {p}")
print(f"  As dict: {asdict(p)}")
print(f"  As tuple: {astuple(p)}")

print()  # Empty line


# ============================================================================
# 6. USING replace()
# ============================================================================
print("=" * 60)
print("6. USING replace()")
print("=" * 60)

@dataclass(frozen=True)
class Point:
    x: int
    y: int

p1 = Point(1, 2)
p2 = replace(p1, x=3)  # Create new instance with modified field
print(f"  Point 1: {p1}")
print(f"  Point 2: {p2}")

print()  # Empty line


# ============================================================================
# 7. VALIDATION IN __post_init__
# ============================================================================
print("=" * 60)
print("7. VALIDATION IN __post_init__")
print("=" * 60)

@dataclass
class Person:
    name: str
    age: int
    email: str = ""
    
    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")
        if self.email and "@" not in self.email:
            raise ValueError("Invalid email format")

try:
    person = Person("Alice", -5)  # Will raise ValueError
except ValueError as e:
    print(f"  Error: {e}")

person = Person("Bob", 25, "bob@example.com")
print(f"  Valid person: {person}")

print()  # Empty line


# ============================================================================
# 8. COMPUTED PROPERTIES
# ============================================================================
print("=" * 60)
print("8. COMPUTED PROPERTIES")
print("=" * 60)

@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)
    perimeter: float = field(init=False)
    
    def __post_init__(self):
        self.area = self.width * self.height
        self.perimeter = 2 * (self.width + self.height)

rect = Rectangle(10, 5)
print(f"  Rectangle: {rect}")
print(f"  Area: {rect.area}, Perimeter: {rect.perimeter}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL DATA CLASS EXAMPLES SUMMARY:")
print("=" * 60)
print("Real-world Patterns:")
print("  - User management systems")
print("  - Shopping carts")
print("  - Configuration objects")
print("  - API responses")
print("  - Using asdict() and astuple()")
print("  - Using replace() for immutable classes")
print("  - Validation in __post_init__")
print("  - Computed properties")
print("=" * 60)

