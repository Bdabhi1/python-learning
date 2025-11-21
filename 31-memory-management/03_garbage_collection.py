"""
Garbage Collection in Python

This file demonstrates Python's garbage collection mechanism.
"""

import gc
import sys

# ============================================================================
# 1. WHAT IS GARBAGE COLLECTION?
# ============================================================================
print("=" * 60)
print("1. WHAT IS GARBAGE COLLECTION?")
print("=" * 60)

print("  Garbage collection:")
print("    - Handles objects that reference counting can't free")
print("    - Primarily handles circular references")
print("    - Runs automatically in the background")
print("    - Can be controlled and monitored")

print()  # Empty line


# ============================================================================
# 2. GARBAGE COLLECTION GENERATIONS
# ============================================================================
print("=" * 60)
print("2. GARBAGE COLLECTION GENERATIONS")
print("=" * 60)

# Python uses generational garbage collection
# Objects are placed in one of three generations
print("  Python uses 3 generations:")
print("    - Generation 0: New objects")
print("    - Generation 1: Objects that survived one collection")
print("    - Generation 2: Objects that survived multiple collections")

# Get current generation counts
counts = gc.get_count()
print(f"  Current generation counts: {counts}")
print("    Format: (generation_0, generation_1, generation_2)")

print()  # Empty line


# ============================================================================
# 3. AUTOMATIC GARBAGE COLLECTION
# ============================================================================
print("=" * 60)
print("3. AUTOMATIC GARBAGE COLLECTION")
print("=" * 60)

# Garbage collection happens automatically
print("  Garbage collection runs automatically")
print("  Thresholds determine when collection occurs")

# Get collection thresholds
thresholds = gc.get_threshold()
print(f"  Collection thresholds: {thresholds}")
print("    Format: (gen0_threshold, gen1_threshold, gen2_threshold)")
print("    Collection occurs when generation exceeds its threshold")

print()  # Empty line


# ============================================================================
# 4. MANUAL GARBAGE COLLECTION
# ============================================================================
print("=" * 60)
print("4. MANUAL GARBAGE COLLECTION")
print("=" * 60)

# Force garbage collection
print("  Forcing garbage collection...")
collected = gc.collect()
print(f"  Objects collected: {collected}")

# Collect specific generation
print("  Collecting generation 0...")
collected = gc.collect(0)
print(f"  Objects collected: {collected}")

print()  # Empty line


# ============================================================================
# 5. CIRCULAR REFERENCES AND GARBAGE COLLECTION
# ============================================================================
print("=" * 60)
print("5. CIRCULAR REFERENCES AND GARBAGE COLLECTION")
print("=" * 60)

class Node:
    """Node class for circular reference example"""
    def __init__(self, value):
        self.value = value
        self.next = None
        print(f"    Created Node({value})")
    
    def __del__(self):
        print(f"    Deleted Node({self.value})")

# Create circular reference
print("  Creating circular reference:")
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node2.next = node1  # Circular reference!

print(f"  node1 reference count: {sys.getrefcount(node1)}")
print(f"  node2 reference count: {sys.getrefcount(node2)}")
print("  Reference counting alone cannot free these")

# Delete references
print("  Deleting references:")
del node1
del node2

# Force garbage collection
print("  Forcing garbage collection:")
collected = gc.collect()
print(f"  Objects collected: {collected}")

print()  # Empty line


# ============================================================================
# 6. GARBAGE COLLECTION STATISTICS
# ============================================================================
print("=" * 60)
print("6. GARBAGE COLLECTION STATISTICS")
print("=" * 60)

# Get garbage collection statistics
stats = gc.get_stats()
print("  Garbage collection statistics:")
for i, stat in enumerate(stats):
    print(f"    Generation {i}:")
    print(f"      Collections: {stat['collections']}")
    print(f"      Collected: {stat['collected']}")
    print(f"      Uncollectable: {stat['uncollectable']}")

print()  # Empty line


# ============================================================================
# 7. ENABLING AND DISABLING GARBAGE COLLECTION
# ============================================================================
print("=" * 60)
print("7. ENABLING AND DISABLING GARBAGE COLLECTION")
print("=" * 60)

# Check if garbage collection is enabled
print(f"  Garbage collection enabled: {gc.isenabled()}")

# Disable garbage collection (rarely needed)
print("  Disabling garbage collection...")
gc.disable()
print(f"  Garbage collection enabled: {gc.isenabled()}")

# Re-enable
print("  Re-enabling garbage collection...")
gc.enable()
print(f"  Garbage collection enabled: {gc.isenabled()}")

print()  # Empty line


# ============================================================================
# 8. DEBUGGING GARBAGE COLLECTION
# ============================================================================
print("=" * 60)
print("8. DEBUGGING GARBAGE COLLECTION")
print("=" * 60)

# Enable debug flags
print("  Garbage collection debug flags:")
print("    - DEBUG_STATS: Print statistics during collection")
print("    - DEBUG_COLLECTABLE: Print collectable objects")
print("    - DEBUG_UNCOLLECTABLE: Print uncollectable objects")
print("    - DEBUG_SAVEALL: Save all objects in gc.garbage")

# Set debug flags (commented out to avoid verbose output)
# gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_COLLECTABLE)

print()  # Empty line


# ============================================================================
# 9. UNCOLLECTABLE OBJECTS
# ============================================================================
print("=" * 60)
print("9. UNCOLLECTABLE OBJECTS")
print("=" * 60)

# Objects with __del__ methods in circular references can't be collected
class Uncollectable:
    def __init__(self, name):
        self.name = name
        self.ref = None
    
    def __del__(self):
        print(f"    Deleting {self.name}")

print("  Creating uncollectable circular reference:")
obj1 = Uncollectable("obj1")
obj2 = Uncollectable("obj2")
obj1.ref = obj2
obj2.ref = obj1

print("  Deleting references:")
del obj1
del obj2

print("  Forcing garbage collection:")
collected = gc.collect()
print(f"  Objects collected: {collected}")
print(f"  Uncollectable objects in gc.garbage: {len(gc.garbage)}")
print("  Note: Objects with __del__ in circular refs can't be collected")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("GARBAGE COLLECTION SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Handles objects reference counting can't free")
print("  - Uses generational collection (3 generations)")
print("  - Runs automatically based on thresholds")
print("  - Can be manually triggered with gc.collect()")
print("  - Handles circular references")
print("  - Can be enabled/disabled with gc.enable()/disable()")
print("  - Statistics available with gc.get_stats()")
print("  - Objects with __del__ in circular refs are uncollectable")
print("=" * 60)

