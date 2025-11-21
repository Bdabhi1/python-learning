"""
itertools Module in Python

This file demonstrates useful functions from the itertools module.
"""

import itertools

# ============================================================================
# 1. INFINITE ITERATORS
# ============================================================================
print("=" * 60)
print("1. INFINITE ITERATORS")
print("=" * 60)

# Count
counter = itertools.count(10, 2)
print(f"  count(10, 2): {[next(counter) for _ in range(5)]}")

# Cycle
cycle = itertools.cycle(['A', 'B', 'C'])
print(f"  cycle(['A', 'B', 'C']): {[next(cycle) for _ in range(5)]}")

# Repeat
repeat = itertools.repeat(5, 3)
print(f"  repeat(5, 3): {list(repeat)}")

print()  # Empty line


# ============================================================================
# 2. COMBINATORIC ITERATORS
# ============================================================================
print("=" * 60)
print("2. COMBINATORIC ITERATORS")
print("=" * 60)

# Permutations
perms = itertools.permutations([1, 2, 3], 2)
print(f"  permutations([1,2,3], 2): {list(perms)}")

# Combinations
combs = itertools.combinations([1, 2, 3, 4], 2)
print(f"  combinations([1,2,3,4], 2): {list(combs)}")

print()  # Empty line


# ============================================================================
# 3. ITERATOR TOOLS
# ============================================================================
print("=" * 60)
print("3. ITERATOR TOOLS")
print("=" * 60)

# Chain
chain = itertools.chain([1, 2], [3, 4])
print(f"  chain([1,2], [3,4]): {list(chain)}")

# Groupby
data = [1, 1, 2, 2, 2, 3]
grouped = itertools.groupby(data)
print("  groupby([1,1,2,2,2,3]):")
for key, group in grouped:
    print(f"    {key}: {list(group)}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("ITERTOOLS SUMMARY:")
print("=" * 60)
print("  - itertools provides useful iterator tools")
print("  - Infinite iterators: count, cycle, repeat")
print("  - Combinatoric: permutations, combinations")
print("  - Tools: chain, groupby, tee, etc.")
print("=" * 60)

