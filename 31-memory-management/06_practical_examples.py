"""
Practical Memory Management Examples

This file demonstrates real-world memory management scenarios.
"""

import sys
import gc
import weakref
import tracemalloc

# ============================================================================
# 1. MEMORY-EFFICIENT DATA PROCESSING
# ============================================================================
print("=" * 60)
print("1. MEMORY-EFFICIENT DATA PROCESSING")
print("=" * 60)

def process_large_file_efficiently(filename, chunk_size=1024):
    """Process large file in chunks to avoid loading entire file"""
    print(f"  Processing {filename} in chunks of {chunk_size} bytes")
    
    # Generator function - processes one chunk at a time
    with open(filename, 'r') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk.upper()  # Process chunk

# Simulate processing
print("  Using generator for memory-efficient processing")
print("  Each chunk is processed and then freed")

print()  # Empty line


# ============================================================================
# 2. MEMORY-EFFICIENT CACHING
# ============================================================================
print("=" * 60)
print("2. MEMORY-EFFICIENT CACHING")
print("=" * 60)

# Weak reference cache - objects can be garbage collected
class WeakCache:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()
    
    def get(self, key):
        return self._cache.get(key)
    
    def set(self, key, value):
        self._cache[key] = value
    
    def size(self):
        return len(self._cache)

cache = WeakCache()

# Add items
for i in range(10):
    cache.set(i, f"value_{i}")

print(f"  Cache size: {cache.size()}")

# Items can be garbage collected if no other references
print("  Cache uses weak references - items can be collected")

print()  # Empty line


# ============================================================================
# 3. MEMORY PROFILING A FUNCTION
# ============================================================================
print("=" * 60)
print("3. MEMORY PROFILING A FUNCTION")
print("=" * 60)

def process_data(data_size):
    """Function that processes data"""
    tracemalloc.start()
    
    # Before processing
    snapshot_before = tracemalloc.take_snapshot()
    current_before, _ = tracemalloc.get_traced_memory()
    
    # Process data
    data = [i**2 for i in range(data_size)]
    result = sum(data)
    
    # After processing
    snapshot_after = tracemalloc.take_snapshot()
    current_after, _ = tracemalloc.get_traced_memory()
    
    # Report
    print(f"  Processing {data_size} items:")
    print(f"    Memory before: {current_before / 1024:.2f} KB")
    print(f"    Memory after: {current_after / 1024:.2f} KB")
    print(f"    Memory increase: {(current_after - current_before) / 1024:.2f} KB")
    
    tracemalloc.stop()
    return result

process_data(10000)

print()  # Empty line


# ============================================================================
# 4. MEMORY-EFFICIENT CLASS WITH __SLOTS__
# ============================================================================
print("=" * 60)
print("4. MEMORY-EFFICIENT CLASS WITH __SLOTS__")
print("=" * 60)

# Regular class
class RegularPerson:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

# Slots class
class SlotsPerson:
    __slots__ = ['name', 'age', 'email']
    
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

# Create many instances
print("  Creating 1000 instances:")
regular_people = [RegularPerson(f"Person{i}", 20+i, f"person{i}@email.com") for i in range(1000)]
slots_people = [SlotsPerson(f"Person{i}", 20+i, f"person{i}@email.com") for i in range(1000)]

print(f"    Regular class: ~{sys.getsizeof(regular_people)} bytes")
print(f"    Slots class: ~{sys.getsizeof(slots_people)} bytes")
print("    __slots__ saves memory with many instances")

print()  # Empty line


# ============================================================================
# 5. DETECTING MEMORY LEAKS
# ============================================================================
print("=" * 60)
print("5. DETECTING MEMORY LEAKS")
print("=" * 60)

# Simulate memory leak
class LeakyCache:
    def __init__(self):
        self.cache = {}
    
    def add(self, key, value):
        self.cache[key] = value
    
    def clear(self):
        self.cache.clear()

cache = LeakyCache()

tracemalloc.start()
snapshot1 = tracemalloc.take_snapshot()

# Add items without clearing
for i in range(100):
    data = list(range(1000))
    cache.add(i, data)

snapshot2 = tracemalloc.take_snapshot()

# Compare
top_stats = snapshot2.compare_to(snapshot1, 'lineno')
print("  Memory leak detection:")
print(f"    Cache size: {len(cache.cache)} items")
print("    Top memory increases:")
for stat in top_stats[:2]:
    print(f"      {stat}")

tracemalloc.stop()

# Fix: Clear cache periodically
cache.clear()
print("    Cache cleared - memory leak fixed")

print()  # Empty line


# ============================================================================
# 6. MEMORY-EFFICIENT ITERATION
# ============================================================================
print("=" * 60)
print("6. MEMORY-EFFICIENT ITERATION")
print("=" * 60)

# Inefficient - creates entire list
def squares_list(n):
    return [i**2 for i in range(n)]

# Efficient - generator
def squares_gen(n):
    for i in range(n):
        yield i**2

n = 100000
print(f"  Processing {n} items:")

# List approach
list_result = squares_list(n)
print(f"    List size: {sys.getsizeof(list_result)} bytes")

# Generator approach
gen_result = squares_gen(n)
print(f"    Generator size: {sys.getsizeof(gen_result)} bytes")
print("    Generator uses minimal memory")

# Process generator
total = sum(gen_result)
print(f"    Sum: {total}")

print()  # Empty line


# ============================================================================
# 7. MANAGING CIRCULAR REFERENCES
# ============================================================================
print("=" * 60)
print("7. MANAGING CIRCULAR REFERENCES")
print("=" * 60)

class TreeNode:
    """Tree node with parent reference"""
    def __init__(self, value):
        self.value = value
        self.children = []
        self._parent = None
    
    def set_parent(self, parent):
        """Set parent using weak reference"""
        self._parent = weakref.ref(parent) if parent else None
    
    def get_parent(self):
        """Get parent from weak reference"""
        return self._parent() if self._parent else None

# Create tree structure
root = TreeNode("root")
child1 = TreeNode("child1")
child2 = TreeNode("child2")

# Use weak references to avoid circular references
child1.set_parent(root)
child2.set_parent(root)
root.children = [child1, child2]

print("  Tree structure created with weak references")
print(f"    Root children: {len(root.children)}")
print(f"    Child1 parent: {child1.get_parent().value if child1.get_parent() else None}")
print("    Weak references prevent circular reference issues")

print()  # Empty line


# ============================================================================
# 8. MEMORY CLEANUP PATTERN
# ============================================================================
print("=" * 60)
print("8. MEMORY CLEANUP PATTERN")
print("=" * 60)

class DataProcessor:
    """Class that processes data and cleans up"""
    def __init__(self):
        self.large_data = None
    
    def load_data(self, size):
        """Load large dataset"""
        self.large_data = [i for i in range(size)]
        print(f"    Loaded {size} items")
    
    def process(self):
        """Process data"""
        if self.large_data:
            return sum(self.large_data)
        return 0
    
    def cleanup(self):
        """Clean up resources"""
        if self.large_data:
            del self.large_data
            self.large_data = None
            print("    Cleaned up large_data")
    
    def __del__(self):
        """Cleanup on deletion"""
        self.cleanup()

# Use processor
processor = DataProcessor()
processor.load_data(100000)
result = processor.process()
print(f"    Result: {result}")
processor.cleanup()
print("    Memory cleaned up")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL MEMORY MANAGEMENT SUMMARY:")
print("=" * 60)
print("Key Patterns:")
print("  - Use generators for large data processing")
print("  - Use weak references for caching")
print("  - Profile memory usage in functions")
print("  - Use __slots__ for classes with many instances")
print("  - Detect and fix memory leaks")
print("  - Use generators for memory-efficient iteration")
print("  - Manage circular references with weak references")
print("  - Clean up resources explicitly")
print("=" * 60)

