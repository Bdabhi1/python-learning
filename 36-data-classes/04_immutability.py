"""
Immutability in Data Classes

This file demonstrates frozen (immutable) data classes.
"""

from dataclasses import dataclass

# ============================================================================
# 1. FROZEN DATA CLASSES
# ============================================================================
print("=" * 60)
print("1. FROZEN DATA CLASSES")
print("=" * 60)

@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(1, 2)
print(f"  Point: {p}")

# p.x = 3  # This would raise FrozenInstanceError
print("  Point is immutable (frozen=True)")

print()  # Empty line


# ============================================================================
# 2. HASHABLE DATA CLASSES
# ============================================================================
print("=" * 60)
print("2. HASHABLE DATA CLASSES")
print("=" * 60)

@dataclass(frozen=True)
class Point:
    x: int
    y: int

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

# Frozen data classes are hashable
point_set = {p1, p2, p3}
print(f"  Points: {point_set}")
print(f"  Number of unique points: {len(point_set)}")  # 2 (p1 and p2 are equal)

print()  # Empty line


# ============================================================================
# 3. WHEN TO USE FROZEN
# ============================================================================
print("=" * 60)
print("3. WHEN TO USE FROZEN")
print("=" * 60)

print("  Use frozen=True for:")
print("    - Constants")
print("    - Configuration objects")
print("    - Hashable objects (for sets/dicts)")
print("    - Immutable data structures")
print("  ")
print("  Example:")
print("    ")
print("    @dataclass(frozen=True)")
print("    class Configuration:")
print("        host: str")
print("        port: int")
print("        timeout: int")

print()  # Empty line


# ============================================================================
# 4. FROZEN WITH COMPUTED FIELDS
# ============================================================================
print("=" * 60)
print("4. FROZEN WITH COMPUTED FIELDS")
print("=" * 60)

@dataclass(frozen=True)
class Rectangle:
    width: float
    height: float
    area: float = 0.0
    
    def __post_init__(self):
        # Use object.__setattr__ for frozen classes
        object.__setattr__(self, 'area', self.width * self.height)

r = Rectangle(10, 5)
print(f"  Rectangle: {r}")
print(f"  Area: {r.area}")

print()  # Empty line


# ============================================================================
# 5. MUTABLE VS IMMUTABLE
# ============================================================================
print("=" * 60)
print("5. MUTABLE VS IMMUTABLE")
print("=" * 60)

# Mutable
@dataclass
class MutablePoint:
    x: int
    y: int

# Immutable
@dataclass(frozen=True)
class ImmutablePoint:
    x: int
    y: int

mp = MutablePoint(1, 2)
mp.x = 3  # OK
print(f"  Mutable point: {mp}")

ip = ImmutablePoint(1, 2)
# ip.x = 3  # FrozenInstanceError
print(f"  Immutable point: {ip}")

print()  # Empty line


# ============================================================================
# 6. FROZEN IN DICTIONARIES
# ============================================================================
print("=" * 60)
print("6. FROZEN IN DICTIONARIES")
print("=" * 60)

@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int

# Can use as dictionary key
coords = {
    Coordinate(0, 0): "origin",
    Coordinate(1, 1): "diagonal",
    Coordinate(0, 1): "up"
}

print(f"  Coordinates dict: {coords}")
print(f"  Value at (0, 0): {coords[Coordinate(0, 0)]}")

print()  # Empty line


# ============================================================================
# 7. PARTIAL IMMUTABILITY
# ============================================================================
print("=" * 60)
print("7. PARTIAL IMMUTABILITY")
print("=" * 60)

print("  Note: frozen=True applies to all fields")
print("  For partial immutability, use regular class")
print("  or make specific fields read-only with properties")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("IMMUTABILITY SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Use frozen=True for immutable data classes")
print("  - Frozen classes are hashable")
print("  - Good for constants and configurations")
print("  - Can use as dictionary keys")
print("  - Use object.__setattr__ in __post_init__ for frozen")
print("=" * 60)

