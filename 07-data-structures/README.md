# Data Structures in Python

Data structures are containers that organize and store data in different ways. Python provides several built-in data structures, each optimized for different use cases.

## Table of Contents
1. [What are Data Structures?](#what-are-data-structures)
2. [Lists](#lists)
3. [Tuples](#tuples)
4. [Dictionaries](#dictionaries)
5. [Sets](#sets)
6. [Choosing the Right Data Structure](#choosing-the-right-data-structure)
7. [Best Practices](#best-practices)

---

## What are Data Structures?

**Data structures** are ways of organizing and storing data in memory. Different structures have different properties:
- **Order**: Is the order of elements preserved?
- **Mutability**: Can elements be changed after creation?
- **Uniqueness**: Can elements be duplicated?
- **Indexing**: How do you access elements?

**Python's built-in data structures:**
1. **Lists**: Ordered, mutable, allows duplicates
2. **Tuples**: Ordered, immutable, allows duplicates
3. **Dictionaries**: Unordered (Python 3.7+ ordered), mutable, key-value pairs
4. **Sets**: Unordered, mutable, unique elements only

---

## Lists

Lists are ordered collections of items. They are **mutable** (can be changed).

### Creating Lists

```python
# Empty list
my_list = []

# List with items
fruits = ["apple", "banana", "orange"]

# Mixed types
mixed = [1, "hello", 3.14, True]

# Using list() constructor
numbers = list(range(5))  # [0, 1, 2, 3, 4]
```

### Accessing Elements

```python
fruits = ["apple", "banana", "orange"]

fruits[0]    # "apple" (first element)
fruits[1]    # "banana"
fruits[-1]   # "orange" (last element)
fruits[-2]   # "banana" (second from end)
```

### Modifying Lists

```python
fruits = ["apple", "banana"]

# Add item
fruits.append("orange")        # Add to end
fruits.insert(1, "grape")      # Insert at index
fruits.extend(["kiwi", "mango"])  # Add multiple

# Remove item
fruits.remove("banana")        # Remove by value
fruits.pop()                   # Remove last item
fruits.pop(0)                  # Remove by index
del fruits[0]                  # Delete by index

# Modify item
fruits[0] = "cherry"           # Change value
```

### List Operations

```python
# Length
len(fruits)

# Check membership
"apple" in fruits

# Concatenation
list1 + list2

# Repetition
list1 * 3

# Slicing
fruits[1:3]      # Elements from index 1 to 2
fruits[:2]        # First 2 elements
fruits[2:]        # From index 2 to end
```

### List Methods

```python
fruits = ["apple", "banana", "orange"]

fruits.append("grape")        # Add to end
fruits.insert(1, "kiwi")      # Insert at index
fruits.remove("banana")       # Remove first occurrence
fruits.pop()                   # Remove and return last
fruits.index("orange")        # Find index
fruits.count("apple")         # Count occurrences
fruits.sort()                  # Sort in place
fruits.reverse()               # Reverse in place
fruits.copy()                  # Create copy
```

---

## Tuples

Tuples are ordered collections like lists, but they are **immutable** (cannot be changed).

### Creating Tuples

```python
# Empty tuple
my_tuple = ()

# Tuple with items
coordinates = (10, 20)

# Single item tuple (note the comma!)
single = (5,)  # Not (5) - that's just a number!

# Without parentheses (tuple packing)
point = 10, 20

# Using tuple() constructor
numbers = tuple([1, 2, 3])
```

### Accessing Elements

```python
point = (10, 20)
point[0]    # 10
point[1]    # 20
point[-1]   # 20
```

### Tuple Operations

```python
# Length
len(point)

# Check membership
10 in point

# Concatenation
tuple1 + tuple2

# Repetition
tuple1 * 3

# Unpacking
x, y = point  # x = 10, y = 20
```

### Why Use Tuples?

- **Immutable**: Can't be accidentally modified
- **Faster**: Slightly faster than lists
- **Hashable**: Can be used as dictionary keys
- **Return multiple values**: Functions can return tuples

---

## Dictionaries

Dictionaries store key-value pairs. They are **mutable** and **unordered** (ordered in Python 3.7+).

### Creating Dictionaries

```python
# Empty dictionary
my_dict = {}

# Dictionary with items
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Using dict() constructor
person = dict(name="Alice", age=25)

# From list of tuples
person = dict([("name", "Alice"), ("age", 25)])
```

### Accessing Elements

```python
person = {"name": "Alice", "age": 25}

# Access by key
person["name"]           # "Alice"
person.get("name")       # "Alice"
person.get("email", "N/A")  # "N/A" (default if key doesn't exist)

# Check if key exists
"name" in person         # True
```

### Modifying Dictionaries

```python
person = {"name": "Alice"}

# Add/Update
person["age"] = 25
person.update({"city": "NYC", "email": "alice@example.com"})

# Remove
del person["age"]
person.pop("city")
person.popitem()         # Remove last item (Python 3.7+)
person.clear()           # Remove all items
```

### Dictionary Methods

```python
person = {"name": "Alice", "age": 25}

person.keys()            # Get all keys
person.values()          # Get all values
person.items()           # Get all key-value pairs
person.copy()            # Create copy
```

---

## Sets

Sets are unordered collections of **unique** elements. They are **mutable**.

### Creating Sets

```python
# Empty set
my_set = set()  # Not {} - that's a dictionary!

# Set with items
numbers = {1, 2, 3, 4, 5}

# From list (removes duplicates)
numbers = set([1, 2, 2, 3, 3])  # {1, 2, 3}

# Using set() constructor
numbers = set(range(5))
```

### Set Operations

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
set1 | set2          # {1, 2, 3, 4, 5}
set1.union(set2)

# Intersection
set1 & set2          # {3}
set1.intersection(set2)

# Difference
set1 - set2          # {1, 2}
set1.difference(set2)

# Symmetric difference
set1 ^ set2          # {1, 2, 4, 5}
set1.symmetric_difference(set2)
```

### Set Methods

```python
my_set = {1, 2, 3}

my_set.add(4)           # Add element
my_set.remove(2)        # Remove (error if not exists)
my_set.discard(2)       # Remove (no error if not exists)
my_set.pop()            # Remove and return arbitrary element
my_set.clear()          # Remove all elements
```

---

## Choosing the Right Data Structure

### Use Lists When:
- You need ordered collection
- You need to modify items
- You need duplicates
- You access by index

**Example:** Shopping cart, to-do list, scores

### Use Tuples When:
- You need ordered collection
- You don't need to modify items
- You need to use as dictionary key
- You return multiple values from function

**Example:** Coordinates, RGB colors, database records

### Use Dictionaries When:
- You need key-value pairs
- You access by key (not index)
- You need fast lookups

**Example:** User profiles, configuration, word counts

### Use Sets When:
- You need unique elements
- You need set operations (union, intersection)
- Order doesn't matter
- You need fast membership testing

**Example:** Unique tags, removing duplicates, set operations

---

## Best Practices

1. **Use list comprehensions for creating lists**
   ```python
   # Good
   squares = [x**2 for x in range(10)]
   
   # Less preferred
   squares = []
   for x in range(10):
       squares.append(x**2)
   ```

2. **Use tuples for immutable data**
   ```python
   # Good
   point = (10, 20)  # Can't be accidentally modified
   ```

3. **Use `.get()` for dictionary access**
   ```python
   # Good
   value = my_dict.get("key", "default")
   
   # Less safe
   value = my_dict["key"]  # KeyError if key doesn't exist
   ```

4. **Use sets to remove duplicates**
   ```python
   # Good
   unique = list(set(my_list))
   ```

5. **Choose the right structure for your use case**
   - Lists: Ordered, mutable, duplicates OK
   - Tuples: Ordered, immutable, duplicates OK
   - Dictionaries: Key-value pairs
   - Sets: Unique elements, set operations

---

## Common Mistakes to Avoid

1. **Confusing `{}` for empty set**
   ```python
   # Wrong
   my_set = {}  # This is a dictionary!
   
   # Correct
   my_set = set()
   ```

2. **Modifying tuple**
   ```python
   # Wrong
   point = (10, 20)
   point[0] = 5  # TypeError!
   
   # Correct - create new tuple
   point = (5, 20)
   ```

3. **Using list when set is better**
   ```python
   # Less efficient
   if item in my_list:  # O(n) - checks all items
   
   # More efficient
   if item in my_set:   # O(1) - hash lookup
   ```

4. **Forgetting dictionary keys must be immutable**
   ```python
   # Wrong
   my_dict = {[1, 2]: "value"}  # TypeError!
   
   # Correct
   my_dict = {(1, 2): "value"}  # Tuple is immutable
   ```

---

## Summary

- **Lists**: Ordered, mutable, allows duplicates - use for sequences you'll modify
- **Tuples**: Ordered, immutable, allows duplicates - use for fixed data
- **Dictionaries**: Key-value pairs - use for lookups and mappings
- **Sets**: Unordered, unique elements - use for uniqueness and set operations
- Choose the right structure based on your needs
- Each structure has specific methods and operations

**Remember**: Understanding data structures helps you write efficient, readable code!

---

## Next Steps

Now that you understand data structures:
1. Practice with the examples in this folder
2. Experiment with different operations
3. Learn when to use each structure
4. Move on to **08-built-in-functions** to learn about Python's built-in functions

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_lists.py`: Working with lists - start here!
2. `02_tuples.py`: Understanding tuples
3. `03_dictionaries.py`: Key-value pairs with dictionaries
4. `04_sets.py`: Unique elements with sets
5. `05_comparing_structures.py`: When to use which structure
6. `06_practical_examples.py`: Real-world data structure examples

Run these files in order to see data structures in action!

