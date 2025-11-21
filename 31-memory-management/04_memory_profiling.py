"""
Memory Profiling in Python

This file demonstrates tools and techniques for profiling memory usage.
"""

import sys
import tracemalloc

# ============================================================================
# 1. BASIC MEMORY SIZING
# ============================================================================
print("=" * 60)
print("1. BASIC MEMORY SIZING")
print("=" * 60)

# Get size of individual objects
print("  Object sizes:")
print(f"    Integer 42: {sys.getsizeof(42)} bytes")
print(f"    String 'Hello': {sys.getsizeof('Hello')} bytes")
print(f"    Empty list: {sys.getsizeof([])} bytes")
print(f"    List [1, 2, 3]: {sys.getsizeof([1, 2, 3])} bytes")
print(f"    Empty dict: {sys.getsizeof({})} bytes")
print(f"    Dict {{'a': 1}}: {sys.getsizeof({'a': 1})} bytes")

# Size of larger structures
large_list = list(range(1000))
print(f"    List with 1000 items: {sys.getsizeof(large_list)} bytes")

print()  # Empty line


# ============================================================================
# 2. USING TRACEMALLOC
# ============================================================================
print("=" * 60)
print("2. USING TRACEMALLOC")
print("=" * 60)

# Start tracking memory
tracemalloc.start()

# Create some data
data1 = [i for i in range(10000)]
data2 = "x" * 10000
data3 = {i: i**2 for i in range(1000)}

# Get current memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"  Current memory usage: {current / 1024:.2f} KB")
print(f"  Peak memory usage: {peak / 1024:.2f} KB")

# Stop tracking
tracemalloc.stop()

print()  # Empty line


# ============================================================================
# 3. MEMORY SNAPSHOTS
# ============================================================================
print("=" * 60)
print("3. MEMORY SNAPSHOTS")
print("=" * 60)

# Start tracking
tracemalloc.start()

# Take initial snapshot
snapshot1 = tracemalloc.take_snapshot()
print("  Taken initial snapshot")

# Create some objects
data = [i**2 for i in range(5000)]
text = "Hello" * 1000

# Take second snapshot
snapshot2 = tracemalloc.take_snapshot()
print("  Taken second snapshot after creating objects")

# Compare snapshots
top_stats = snapshot2.compare_to(snapshot1, 'lineno')
print("  Top 5 memory allocations:")
for index, stat in enumerate(top_stats[:5], 1):
    print(f"    {index}. {stat}")

tracemalloc.stop()

print()  # Empty line


# ============================================================================
# 4. TRACKING MEMORY BY FILENAME
# ============================================================================
print("=" * 60)
print("4. TRACKING MEMORY BY FILENAME")
print("=" * 60)

tracemalloc.start()

# Create objects
data1 = list(range(10000))
data2 = [i**2 for i in range(5000)]

# Take snapshot
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('filename')

print("  Memory usage by filename:")
for stat in top_stats[:5]:
    print(f"    {stat.filename}: {stat.size / 1024:.2f} KB")

tracemalloc.stop()

print()  # Empty line


# ============================================================================
# 5. MEMORY TRACKING IN FUNCTIONS
# ============================================================================
print("=" * 60)
print("5. MEMORY TRACKING IN FUNCTIONS")
print("=" * 60)

def create_large_data(size):
    """Function that creates large data structures"""
    return [i for i in range(size)]

tracemalloc.start()

# Before function call
snapshot_before = tracemalloc.take_snapshot()
current_before, _ = tracemalloc.get_traced_memory()

# Call function
result = create_large_data(10000)

# After function call
snapshot_after = tracemalloc.take_snapshot()
current_after, _ = tracemalloc.get_traced_memory()

# Compare
print(f"  Memory before: {current_before / 1024:.2f} KB")
print(f"  Memory after: {current_after / 1024:.2f} KB")
print(f"  Memory increase: {(current_after - current_before) / 1024:.2f} KB")

tracemalloc.stop()

print()  # Empty line


# ============================================================================
# 6. FINDING MEMORY LEAKS
# ============================================================================
print("=" * 60)
print("6. FINDING MEMORY LEAKS")
print("=" * 60)

# Simulate a memory leak
cache = {}

def process_data(data):
    """Function that leaks memory by caching everything"""
    cache[id(data)] = data  # Never cleared!
    return len(data)

tracemalloc.start()

# Initial state
snapshot1 = tracemalloc.take_snapshot()

# Process multiple items (memory leak)
for i in range(100):
    data = list(range(1000))
    process_data(data)

# Final state
snapshot2 = tracemalloc.take_snapshot()

# Compare
top_stats = snapshot2.compare_to(snapshot1, 'lineno')
print("  Top memory increases (potential leaks):")
for stat in top_stats[:3]:
    print(f"    {stat}")

print(f"  Cache size: {len(cache)} items")
print("  Note: Cache never cleared = memory leak")

tracemalloc.stop()

print()  # Empty line


# ============================================================================
# 7. MEMORY USAGE OF DIFFERENT DATA STRUCTURES
# ============================================================================
print("=" * 60)
print("7. MEMORY USAGE OF DIFFERENT DATA STRUCTURES")
print("=" * 60)

size = 1000

# List
list_data = list(range(size))
list_size = sys.getsizeof(list_data)

# Tuple
tuple_data = tuple(range(size))
tuple_size = sys.getsizeof(tuple_data)

# Set
set_data = set(range(size))
set_size = sys.getsizeof(set_data)

# Dict
dict_data = {i: i for i in range(size)}
dict_size = sys.getsizeof(dict_data)

print(f"  Memory usage for {size} items:")
print(f"    List: {list_size} bytes")
print(f"    Tuple: {tuple_size} bytes")
print(f"    Set: {set_size} bytes")
print(f"    Dict: {dict_size} bytes")

print()  # Empty line


# ============================================================================
# 8. MEMORY PROFILING BEST PRACTICES
# ============================================================================
print("=" * 60)
print("8. MEMORY PROFILING BEST PRACTICES")
print("=" * 60)

print("  Best practices:")
print("    1. Use tracemalloc for detailed tracking")
print("    2. Take snapshots before and after operations")
print("    3. Compare snapshots to find memory increases")
print("    4. Profile in realistic scenarios")
print("    5. Look for unexpected memory growth")
print("    6. Check for memory leaks in long-running code")
print("    7. Use external tools (memory_profiler) for detailed analysis")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("MEMORY PROFILING SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Use sys.getsizeof() for individual object sizes")
print("  - Use tracemalloc for detailed memory tracking")
print("  - Take snapshots to compare memory usage")
print("  - Compare snapshots to find memory leaks")
print("  - Track memory by filename or line number")
print("  - Profile in realistic scenarios")
print("  - Different data structures use different amounts of memory")
print("=" * 60)

