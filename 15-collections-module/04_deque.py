"""
deque (Double-Ended Queue) in Python Collections Module

This file demonstrates how to use deque for fast append and pop operations
from both ends of a sequence.
"""

from collections import deque

# ============================================================================
# 1. CREATING A DEQUE
# ============================================================================
print("=" * 60)
print("1. CREATING A DEQUE")
print("=" * 60)

# Empty deque
d1 = deque()
print(f"  Empty deque: {list(d1)}")

# From iterable
d2 = deque([1, 2, 3, 4, 5])
print(f"  From list: {list(d2)}")

# From string
d3 = deque('hello')
print(f"  From string: {list(d3)}")

# With maxlen (bounded deque)
d4 = deque([1, 2, 3], maxlen=5)
print(f"  With maxlen=5: {list(d4)}")

print()  # Empty line


# ============================================================================
# 2. APPEND OPERATIONS
# ============================================================================
print("=" * 60)
print("2. APPEND OPERATIONS")
print("=" * 60)

d = deque([1, 2, 3])
print(f"  Initial: {list(d)}")

# Append to right (end)
d.append(4)
print(f"  After append(4): {list(d)}")

# Append to left (beginning)
d.appendleft(0)
print(f"  After appendleft(0): {list(d)}")

print()  # Empty line


# ============================================================================
# 3. POP OPERATIONS
# ============================================================================
print("=" * 60)
print("3. POP OPERATIONS")
print("=" * 60)

d = deque([1, 2, 3, 4, 5])
print(f"  Initial: {list(d)}")

# Pop from right (end)
item = d.pop()
print(f"  pop(): {item}, Remaining: {list(d)}")

# Pop from left (beginning)
item = d.popleft()
print(f"  popleft(): {item}, Remaining: {list(d)}")

print()  # Empty line


# ============================================================================
# 4. EXTEND OPERATIONS
# ============================================================================
print("=" * 60)
print("4. EXTEND OPERATIONS")
print("=" * 60)

d = deque([1, 2, 3])
print(f"  Initial: {list(d)}")

# Extend right
d.extend([4, 5])
print(f"  After extend([4, 5]): {list(d)}")

# Extend left (note: items are added in reverse order!)
d.extendleft([0, -1])
print(f"  After extendleft([0, -1]): {list(d)}")

print()  # Empty line


# ============================================================================
# 5. ROTATE OPERATION
# ============================================================================
print("=" * 60)
print("5. ROTATE OPERATION")
print("=" * 60)

d = deque([1, 2, 3, 4, 5])
print(f"  Initial: {list(d)}")

# Rotate right by 1
d.rotate(1)
print(f"  After rotate(1): {list(d)}")

# Rotate left by 2
d.rotate(-2)
print(f"  After rotate(-2): {list(d)}")

print()  # Empty line


# ============================================================================
# 6. BOUNDED DEQUE (MAXLEN)
# ============================================================================
print("=" * 60)
print("6. BOUNDED DEQUE (MAXLEN)")
print("=" * 60)

# Bounded deque (removes from opposite end when full)
d = deque([1, 2, 3], maxlen=3)
print(f"  Initial (maxlen=3): {list(d)}")

# Adding to right removes from left
d.append(4)
print(f"  After append(4): {list(d)}")

# Adding to left removes from right
d.appendleft(0)
print(f"  After appendleft(0): {list(d)}")

print()  # Empty line


# ============================================================================
# 7. ACCESSING ELEMENTS
# ============================================================================
print("=" * 60)
print("7. ACCESSING ELEMENTS")
print("=" * 60)

d = deque([10, 20, 30, 40, 50])
print(f"  Deque: {list(d)}")

# Index access
print(f"  d[0]: {d[0]}")
print(f"  d[-1]: {d[-1]}")
print(f"  d[2]: {d[2]}")

# Slicing (returns a list, not a deque)
print(f"  d[1:4]: {list(d)[1:4]}")

# Length
print(f"  len(d): {len(d)}")

print()  # Empty line


# ============================================================================
# 8. QUEUE OPERATIONS (FIFO)
# ============================================================================
print("=" * 60)
print("8. QUEUE OPERATIONS (FIFO)")
print("=" * 60)

# Queue: First In, First Out
queue = deque()

# Enqueue (add to end)
queue.append('first')
queue.append('second')
queue.append('third')
print(f"  After enqueue: {list(queue)}")

# Dequeue (remove from front)
item = queue.popleft()
print(f"  Dequeued: {item}, Remaining: {list(queue)}")

print()  # Empty line


# ============================================================================
# 9. STACK OPERATIONS (LIFO)
# ============================================================================
print("=" * 60)
print("9. STACK OPERATIONS (LIFO)")
print("=" * 60)

# Stack: Last In, First Out
stack = deque()

# Push (add to end)
stack.append('first')
stack.append('second')
stack.append('third')
print(f"  After push: {list(stack)}")

# Pop (remove from end)
item = stack.pop()
print(f"  Popped: {item}, Remaining: {list(stack)}")

print()  # Empty line


# ============================================================================
# 10. PERFORMANCE COMPARISON
# ============================================================================
print("=" * 60)
print("10. PERFORMANCE COMPARISON")
print("=" * 60)

import time

# List operations (slow at beginning)
n = 100000
lst = list(range(n))
start = time.time()
lst.insert(0, 0)
list_time = time.time() - start

# Deque operations (fast at both ends)
d = deque(range(n))
start = time.time()
d.appendleft(0)
deque_time = time.time() - start

print(f"  List insert(0): {list_time:.6f} seconds")
print(f"  Deque appendleft: {deque_time:.6f} seconds")
print(f"  Deque is {list_time/deque_time:.1f}x faster!")

print()  # Empty line


# ============================================================================
# 11. PRACTICAL EXAMPLE: SLIDING WINDOW
# ============================================================================
print("=" * 60)
print("11. PRACTICAL EXAMPLE: SLIDING WINDOW")
print("=" * 60)

def sliding_window_max(nums, k):
    """Find maximum in each sliding window of size k"""
    dq = deque()  # Store indices
    result = []
    
    for i, num in enumerate(nums):
        # Remove indices outside current window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove indices with smaller values
        while dq and nums[dq[-1]] <= num:
            dq.pop()
        
        dq.append(i)
        
        # Add to result when window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
result = sliding_window_max(nums, k)
print(f"  Input: {nums}, k={k}")
print(f"  Max in each window: {result}")

print()  # Empty line


# ============================================================================
# 12. PRACTICAL EXAMPLE: BFS
# ============================================================================
print("=" * 60)
print("12. PRACTICAL EXAMPLE: BFS")
print("=" * 60)

def bfs(graph, start):
    """Breadth-First Search using deque"""
    queue = deque([start])
    visited = {start}
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print(f"  Graph: {graph}")
print(f"  BFS from 'A': {bfs(graph, 'A')}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("DEQUE SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - deque is optimized for operations at both ends")
print("  - O(1) append/pop from both ends")
print("  - O(n) for operations in the middle")
print("  - Can be used as queue (FIFO) or stack (LIFO)")
print("  - rotate() rotates elements")
print("  - maxlen creates bounded deque")
print("  - Much faster than list for queue operations")
print("=" * 60)

