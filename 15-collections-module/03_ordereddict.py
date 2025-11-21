"""
OrderedDict in Python Collections Module

This file demonstrates how to use OrderedDict, a dictionary that remembers
insertion order. Note: Regular dicts in Python 3.7+ also maintain order,
but OrderedDict has additional features.
"""

from collections import OrderedDict

# ============================================================================
# 1. CREATING AN ORDEREDDICT
# ============================================================================
print("=" * 60)
print("1. CREATING AN ORDEREDDICT")
print("=" * 60)

# Empty OrderedDict
od1 = OrderedDict()
od1['first'] = 1
od1['second'] = 2
od1['third'] = 3
print(f"  OrderedDict: {dict(od1)}")
print(f"  Order preserved: {list(od1.keys())}")

# From a list of tuples
od2 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(f"\n  From tuples: {dict(od2)}")

# From keyword arguments (Python 3.6+)
od3 = OrderedDict(first=1, second=2, third=3)
print(f"\n  From kwargs: {dict(od3)}")

print()  # Empty line


# ============================================================================
# 2. INSERTION ORDER PRESERVATION
# ============================================================================
print("=" * 60)
print("2. INSERTION ORDER PRESERVATION")
print("=" * 60)

od = OrderedDict()
od['z'] = 26
od['a'] = 1
od['m'] = 13

print(f"  Insertion order: {list(od.keys())}")
print(f"  Values in order: {list(od.values())}")
print(f"  Items in order: {list(od.items())}")

# Re-inserting changes position
od['a'] = 1  # 'a' moves to end
print(f"\n  After re-inserting 'a': {list(od.keys())}")

print()  # Empty line


# ============================================================================
# 3. MOVE_TO_END METHOD
# ============================================================================
print("=" * 60)
print("3. MOVE_TO_END METHOD")
print("=" * 60)

od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
print(f"  Initial: {list(od.keys())}")

# Move to end (default)
od.move_to_end('a')
print(f"  After move_to_end('a'): {list(od.keys())}")

# Move to beginning
od.move_to_end('c', last=False)
print(f"  After move_to_end('c', last=False): {list(od.keys())}")

print()  # Empty line


# ============================================================================
# 4. POPITEM METHOD
# ============================================================================
print("=" * 60)
print("4. POPITEM METHOD")
print("=" * 60)

od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
print(f"  Initial: {list(od.keys())}")

# Pop last item (default)
item = od.popitem()
print(f"  popitem(): {item}, Remaining: {list(od.keys())}")

# Pop first item
item = od.popitem(last=False)
print(f"  popitem(last=False): {item}, Remaining: {list(od.keys())}")

print()  # Empty line


# ============================================================================
# 5. REVERSING ORDER
# ============================================================================
print("=" * 60)
print("5. REVERSING ORDER")
print("=" * 60)

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(f"  Original: {list(od.keys())}")

# Reverse using reversed()
reversed_od = OrderedDict(reversed(od.items()))
print(f"  Reversed: {list(reversed_od.keys())}")

print()  # Empty line


# ============================================================================
# 6. LRU CACHE IMPLEMENTATION
# ============================================================================
print("=" * 60)
print("6. LRU CACHE IMPLEMENTATION")
print("=" * 60)

class LRUCache:
    """Least Recently Used Cache using OrderedDict"""
    
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        if key in self.cache:
            # Move to end (most recently used)
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            # Update existing key
            self.cache.move_to_end(key)
        else:
            # Check capacity
            if len(self.cache) >= self.capacity:
                # Remove least recently used (first item)
                self.cache.popitem(last=False)
        self.cache[key] = value

# Example usage
cache = LRUCache(3)
cache.put(1, 'one')
cache.put(2, 'two')
cache.put(3, 'three')
print(f"  After putting 1, 2, 3: {dict(cache.cache)}")

cache.get(1)  # Access 1 (moves to end)
print(f"  After get(1): {dict(cache.cache)}")

cache.put(4, 'four')  # Evicts 2 (least recently used)
print(f"  After put(4): {dict(cache.cache)}")

print()  # Empty line


# ============================================================================
# 7. SORTING ORDEREDDICT
# ============================================================================
print("=" * 60)
print("7. SORTING ORDEREDDICT")
print("=" * 60)

od = OrderedDict([('z', 26), ('a', 1), ('m', 13), ('b', 2)])
print(f"  Original: {dict(od)}")

# Sort by key
sorted_by_key = OrderedDict(sorted(od.items(), key=lambda x: x[0]))
print(f"  Sorted by key: {dict(sorted_by_key)}")

# Sort by value
sorted_by_value = OrderedDict(sorted(od.items(), key=lambda x: x[1]))
print(f"  Sorted by value: {dict(sorted_by_value)}")

print()  # Empty line


# ============================================================================
# 8. COMPARING WITH REGULAR DICT
# ============================================================================
print("=" * 60)
print("8. COMPARING WITH REGULAR DICT")
print("=" * 60)

# Python 3.7+ dicts also maintain order
regular_dict = {'a': 1, 'b': 2, 'c': 3}
ordered_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

print(f"  Regular dict (Python 3.7+): {list(regular_dict.keys())}")
print(f"  OrderedDict: {list(ordered_dict.keys())}")

print("\n  Differences:")
print("    - OrderedDict has move_to_end() method")
print("    - OrderedDict has popitem(last=False) for first item")
print("    - OrderedDict equality considers order (Python < 3.8)")
print("    - OrderedDict is more explicit about ordering")

print()  # Empty line


# ============================================================================
# 9. PRACTICAL EXAMPLE: CONFIGURATION ORDER
# ============================================================================
print("=" * 60)
print("9. PRACTICAL EXAMPLE: CONFIGURATION ORDER")
print("=" * 60)

# Configuration that needs to be processed in order
config = OrderedDict()
config['database'] = 'localhost'
config['port'] = 5432
config['username'] = 'admin'
config['password'] = 'secret'

print(f"  Configuration order: {list(config.keys())}")

# Process in insertion order
for key, value in config.items():
    print(f"    {key}: {value}")

print()  # Empty line


# ============================================================================
# 10. EQUALITY COMPARISON
# ============================================================================
print("=" * 60)
print("10. EQUALITY COMPARISON")
print("=" * 60)

od1 = OrderedDict([('a', 1), ('b', 2)])
od2 = OrderedDict([('b', 2), ('a', 1)])

print(f"  od1: {dict(od1)}")
print(f"  od2: {dict(od2)}")
print(f"  od1 == od2: {od1 == od2}")  # False (different order)

od3 = OrderedDict([('a', 1), ('b', 2)])
print(f"\n  od1 == od3: {od1 == od3}")  # True (same order and values)

# Compare with regular dict
regular = {'a': 1, 'b': 2}
print(f"  od1 == regular dict: {od1 == regular}")  # True (Python 3.8+)

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("ORDEREDDICT SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - OrderedDict remembers insertion order")
print("  - move_to_end() moves items to end or beginning")
print("  - popitem() can pop from either end")
print("  - Useful for LRU caches")
print("  - Equality considers order (Python < 3.8)")
print("  - Regular dicts also maintain order (Python 3.7+)")
print("  - OrderedDict has additional ordering methods")
print("=" * 60)

