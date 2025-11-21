# Collections Module in Python

The `collections` module provides specialized container datatypes that extend Python's built-in data structures. These collections offer enhanced functionality and performance for specific use cases.

## Table of Contents
1. [What is the Collections Module?](#what-is-the-collections-module)
2. [Counter](#counter)
3. [defaultdict](#defaultdict)
4. [OrderedDict](#ordereddict)
5. [deque](#deque)
6. [namedtuple](#namedtuple)
7. [ChainMap](#chainmap)
8. [Best Practices](#best-practices)

---

## What is the Collections Module?

The `collections` module provides alternative implementations of built-in containers and additional specialized data structures.

**Key collections:**
- `Counter`: Count hashable objects
- `defaultdict`: Dictionary with default values
- `OrderedDict`: Dictionary that remembers insertion order
- `deque`: Double-ended queue
- `namedtuple`: Tuple with named fields
- `ChainMap`: Multiple dictionaries as single mapping

**Why use collections?**
- **Performance**: Optimized for specific operations
- **Convenience**: Built-in methods for common tasks
- **Clarity**: More readable code for specific use cases

---

## Counter

`Counter` is a dictionary subclass for counting hashable objects. It's a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.

### Creating a Counter

```python
from collections import Counter

# From a list
counter = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
# Counter({'apple': 3, 'banana': 2, 'orange': 1})

# From a string
counter = Counter('hello')
# Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

# From a dictionary
counter = Counter({'red': 4, 'blue': 2})
```

### Common Operations

```python
from collections import Counter

counter = Counter(['apple', 'banana', 'apple', 'orange'])

# Access count
counter['apple']  # 2
counter['grape']  # 0 (doesn't raise KeyError)

# Update counter
counter.update(['apple', 'grape'])
# Counter({'apple': 3, 'banana': 1, 'orange': 1, 'grape': 1})

# Most common elements
counter.most_common(2)  # [('apple', 3), ('banana', 1)]

# Subtract counts
counter.subtract(['apple', 'banana'])
# Counter({'apple': 2, 'banana': 0, 'orange': 1, 'grape': 1})
```

### Practical Uses

```python
from collections import Counter

# Count word frequencies
text = "the quick brown fox jumps over the lazy dog"
word_count = Counter(text.split())
print(word_count.most_common(3))
# [('the', 2), ('quick', 1), ('brown', 1)]

# Find most common characters
text = "mississippi"
char_count = Counter(text)
print(char_count.most_common(3))
# [('i', 4), ('s', 4), ('p', 2)]
```

---

## defaultdict

`defaultdict` is a dictionary subclass that provides a default value for missing keys. It eliminates the need to check if a key exists before accessing it.

### Creating a defaultdict

```python
from collections import defaultdict

# Default factory function
dd = defaultdict(int)  # Default value is 0
dd['a'] = 1
print(dd['b'])  # 0 (not KeyError)

# Default factory for lists
dd = defaultdict(list)
dd['fruits'].append('apple')
dd['fruits'].append('banana')
# defaultdict(<class 'list'>, {'fruits': ['apple', 'banana']})

# Default factory for sets
dd = defaultdict(set)
dd['colors'].add('red')
dd['colors'].add('blue')
```

### Common Use Cases

```python
from collections import defaultdict

# Group items by category
items = [('fruit', 'apple'), ('fruit', 'banana'), ('vegetable', 'carrot')]
grouped = defaultdict(list)
for category, item in items:
    grouped[category].append(item)
# defaultdict(<class 'list'>, {'fruit': ['apple', 'banana'], 'vegetable': ['carrot']})

# Count occurrences
counter = defaultdict(int)
for word in ['apple', 'banana', 'apple']:
    counter[word] += 1
# defaultdict(<class 'int'>, {'apple': 2, 'banana': 1})
```

### Custom Default Factory

```python
from collections import defaultdict

# Custom default value
def default_value():
    return "Not Found"

dd = defaultdict(default_value)
print(dd['missing'])  # "Not Found"
```

---

## OrderedDict

`OrderedDict` is a dictionary subclass that remembers the order in which items were inserted. (Note: Regular dicts in Python 3.7+ also maintain insertion order, but OrderedDict has additional features.)

### Creating an OrderedDict

```python
from collections import OrderedDict

# Preserves insertion order
od = OrderedDict()
od['first'] = 1
od['second'] = 2
od['third'] = 3
# OrderedDict([('first', 1), ('second', 2), ('third', 3)])

# From a list of tuples
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```

### Special Methods

```python
from collections import OrderedDict

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Move to end
od.move_to_end('a')
# OrderedDict([('b', 2), ('c', 3), ('a', 1)])

# Move to beginning
od.move_to_end('a', last=False)
# OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Pop last item
od.popitem()  # ('c', 3)
od.popitem(last=False)  # ('a', 1) - pop first item
```

### Use Cases

```python
from collections import OrderedDict

# LRU Cache implementation
class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

---

## deque

`deque` (double-ended queue) is a list-like container with fast appends and pops from both ends. It's optimized for operations at both ends.

### Creating a deque

```python
from collections import deque

# Empty deque
d = deque()

# From iterable
d = deque([1, 2, 3, 4, 5])

# With maxlen (bounded deque)
d = deque([1, 2, 3], maxlen=5)
```

### Operations

```python
from collections import deque

d = deque([1, 2, 3])

# Append operations
d.append(4)        # Add to right: deque([1, 2, 3, 4])
d.appendleft(0)    # Add to left: deque([0, 1, 2, 3, 4])

# Pop operations
d.pop()            # Remove from right: 4
d.popleft()        # Remove from left: 0

# Extend operations
d.extend([5, 6])   # Extend right: deque([1, 2, 3, 5, 6])
d.extendleft([0])  # Extend left: deque([0, 1, 2, 3, 5, 6])

# Rotate
d.rotate(1)        # Rotate right by 1
d.rotate(-1)       # Rotate left by 1
```

### Performance Benefits

```python
from collections import deque
import time

# List operations (slow at beginning)
lst = list(range(1000000))
start = time.time()
lst.insert(0, 0)  # Slow!
print(f"List insert: {time.time() - start}")

# Deque operations (fast at both ends)
d = deque(range(1000000))
start = time.time()
d.appendleft(0)  # Fast!
print(f"Deque appendleft: {time.time() - start}")
```

### Use Cases

```python
from collections import deque

# Sliding window
def sliding_window_max(nums, k):
    dq = deque()
    result = []
    for i, num in enumerate(nums):
        while dq and nums[dq[-1]] <= num:
            dq.pop()
        dq.append(i)
        if dq[0] == i - k:
            dq.popleft()
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

# BFS (Breadth-First Search)
def bfs(graph, start):
    queue = deque([start])
    visited = {start}
    while queue:
        node = queue.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

---

## namedtuple

`namedtuple` creates tuple subclasses with named fields. It's like a lightweight class without methods.

### Creating a namedtuple

```python
from collections import namedtuple

# Define a namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(p.x, p.y)  # 11 22

# Access by index or name
print(p[0])      # 11
print(p.x)       # 11

# Immutable
# p.x = 5  # AttributeError: can't set attribute
```

### Common Use Cases

```python
from collections import namedtuple

# Represent a person
Person = namedtuple('Person', ['name', 'age', 'city'])
person = Person('Alice', 30, 'NYC')
print(f"{person.name} is {person.age} years old")

# Represent coordinates
Coordinate = namedtuple('Coordinate', ['latitude', 'longitude'])
location = Coordinate(40.7128, -74.0060)
print(f"Lat: {location.latitude}, Long: {location.longitude}")

# With default values (Python 3.7+)
Person = namedtuple('Person', ['name', 'age', 'city'], defaults=['Unknown'])
person = Person('Bob', 25)
print(person.city)  # 'Unknown'
```

### Methods

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, 22)

# Convert to dictionary
p._asdict()  # {'x': 11, 'y': 22}

# Replace fields
p._replace(x=33)  # Point(x=33, y=22)

# Get all fields
Point._fields  # ('x', 'y')
```

---

## ChainMap

`ChainMap` groups multiple dictionaries into a single mapping. Lookups search the underlying mappings successively until a key is found.

### Creating a ChainMap

```python
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain = ChainMap(dict1, dict2)

print(chain['a'])  # 1 (from dict1)
print(chain['b'])  # 2 (from dict1, first match)
print(chain['c'])  # 4 (from dict2)
```

### Common Use Cases

```python
from collections import ChainMap

# Configuration with defaults
defaults = {'theme': 'dark', 'language': 'en'}
user_prefs = {'theme': 'light'}
config = ChainMap(user_prefs, defaults)
print(config['theme'])    # 'light' (from user_prefs)
print(config['language']) # 'en' (from defaults)

# Command-line arguments with defaults
import argparse
args = {'verbose': True}
defaults = {'verbose': False, 'debug': False}
settings = ChainMap(args, defaults)
```

### Operations

```python
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3}
chain = ChainMap(dict1, dict2)

# Get all keys (may have duplicates)
list(chain.keys())  # ['a', 'b', 'c']

# Get all values
list(chain.values())  # [1, 2, 3]

# Add new mapping
chain = chain.new_child({'d': 4})

# Get parents
chain.parents  # ChainMap({'a': 1, 'b': 2}, {'c': 3})
```

---

## Best Practices

### 1. Choose the Right Collection

```python
# Use Counter for counting
from collections import Counter
counts = Counter(['a', 'b', 'a', 'c'])

# Use defaultdict for grouping
from collections import defaultdict
groups = defaultdict(list)

# Use deque for queue operations
from collections import deque
queue = deque()
```

### 2. Understand Performance

```python
# deque is faster for queue operations
from collections import deque
queue = deque()  # O(1) append/pop from both ends

# Counter is optimized for counting
from collections import Counter
counter = Counter()  # Fast counting operations
```

### 3. Use namedtuple for Simple Data Structures

```python
# Good for simple data structures
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)

# Consider dataclasses for more complex cases (Python 3.7+)
```

### 4. ChainMap for Configuration

```python
# Useful for layered configuration
from collections import ChainMap
config = ChainMap(user_settings, default_settings)
```

---

## Common Mistakes to Avoid

1. **Using regular dict instead of Counter**
   ```python
   # Less efficient
   counts = {}
   for item in items:
       counts[item] = counts.get(item, 0) + 1
   
   # Better
   from collections import Counter
   counts = Counter(items)
   ```

2. **Not using defaultdict for grouping**
   ```python
   # Verbose
   groups = {}
   for key, value in items:
       if key not in groups:
           groups[key] = []
       groups[key].append(value)
   
   # Better
   from collections import defaultdict
   groups = defaultdict(list)
   for key, value in items:
       groups[key].append(value)
   ```

3. **Using list for queue operations**
   ```python
   # Slow for queue operations
   queue = []
   queue.insert(0, item)  # O(n)
   item = queue.pop()     # O(1)
   
   # Better
   from collections import deque
   queue = deque()
   queue.appendleft(item)  # O(1)
   item = queue.pop()      # O(1)
   ```

---

## Summary

- **Counter**: Count hashable objects efficiently
- **defaultdict**: Dictionary with default values
- **OrderedDict**: Dictionary that remembers order (with extra features)
- **deque**: Fast double-ended queue
- **namedtuple**: Tuple with named fields
- **ChainMap**: Multiple dictionaries as single mapping
- Choose the right collection for your use case
- Understand performance characteristics

**Remember**: The collections module provides optimized data structures for specific use cases. Use them to write more efficient and readable code!

---

## Next Steps

Now that you understand the collections module:
1. Practice with the examples in this folder
2. Use appropriate collections in your projects
3. Understand when to use each collection type
4. Move on to **16-object-oriented-programming** to learn about classes and objects

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_counter.py`: Using Counter for counting objects - start here!
2. `02_defaultdict.py`: Dictionary with default values
3. `03_ordereddict.py`: Dictionary that remembers order
4. `04_deque.py`: Double-ended queue operations
5. `05_namedtuple_chainmap.py`: Named tuples and ChainMap
6. `06_practical_examples.py`: Real-world collections examples

Run these files in order to see the collections module in action!

