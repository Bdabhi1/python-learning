"""
Dictionaries in Python

This file demonstrates dictionaries - key-value pairs for storing
and retrieving data efficiently.
"""

# ============================================================================
# 1. CREATING DICTIONARIES
# ============================================================================
print("=" * 60)
print("1. CREATING DICTIONARIES")
print("=" * 60)

# Empty dictionary
empty_dict = {}
print(f"  Empty dict: {empty_dict}")

# Dictionary with items
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(f"  Person: {person}")

# Using dict() constructor
person2 = dict(name="Bob", age=30, city="London")
print(f"  Person2: {person2}")

# From list of tuples
person3 = dict([("name", "Charlie"), ("age", 35)])
print(f"  Person3: {person3}")

print()  # Empty line


# ============================================================================
# 2. ACCESSING ELEMENTS
# ============================================================================
print("=" * 60)
print("2. ACCESSING ELEMENTS")
print("=" * 60)

person = {"name": "Alice", "age": 25, "city": "New York"}

# Access by key
print(f"  person['name']: {person['name']}")
print(f"  person['age']: {person['age']}")

# Using get() (safer)
print(f"  person.get('name'): {person.get('name')}")
print(f"  person.get('email'): {person.get('email')}")  # Returns None
print(f"  person.get('email', 'N/A'): {person.get('email', 'N/A')}")  # Default

# Check if key exists
print(f"  'name' in person: {'name' in person}")
print(f"  'email' in person: {'email' in person}")

print()  # Empty line


# ============================================================================
# 3. MODIFYING DICTIONARIES
# ============================================================================
print("=" * 60)
print("3. MODIFYING DICTIONARIES")
print("=" * 60)

person = {"name": "Alice"}

# Add/Update
person["age"] = 25
print(f"  After person['age'] = 25: {person}")

person["city"] = "New York"
print(f"  After person['city'] = 'New York': {person}")

# Update multiple items
person.update({"email": "alice@example.com", "phone": "123-456-7890"})
print(f"  After update(): {person}")

# Modify existing
person["age"] = 26
print(f"  After person['age'] = 26: {person}")

print()  # Empty line


# ============================================================================
# 4. REMOVING ELEMENTS
# ============================================================================
print("=" * 60)
print("4. REMOVING ELEMENTS")
print("=" * 60)

person = {"name": "Alice", "age": 25, "city": "New York", "email": "alice@example.com"}
print(f"  Original: {person}")

# Remove by key
del person["email"]
print(f"  After del person['email']: {person}")

# Remove and return value
age = person.pop("age")
print(f"  After pop('age'): {person}, removed: {age}")

# Remove last item (Python 3.7+)
item = person.popitem()
print(f"  After popitem(): {person}, removed: {item}")

# Clear all
person.clear()
print(f"  After clear(): {person}")

print()  # Empty line


# ============================================================================
# 5. DICTIONARY METHODS
# ============================================================================
print("=" * 60)
print("5. DICTIONARY METHODS")
print("=" * 60)

person = {"name": "Alice", "age": 25, "city": "New York"}

# Get all keys
print(f"  person.keys(): {list(person.keys())}")

# Get all values
print(f"  person.values(): {list(person.values())}")

# Get all items (key-value pairs)
print(f"  person.items(): {list(person.items())}")

# Copy
person_copy = person.copy()
print(f"  Copy: {person_copy}")

# Get with default
print(f"  person.get('name', 'Unknown'): {person.get('name', 'Unknown')}")
print(f"  person.get('email', 'Unknown'): {person.get('email', 'Unknown')}")

print()  # Empty line


# ============================================================================
# 6. ITERATING OVER DICTIONARIES
# ============================================================================
print("=" * 60)
print("6. ITERATING OVER DICTIONARIES")
print("=" * 60)

person = {"name": "Alice", "age": 25, "city": "New York"}

# Iterate over keys (default)
print("  Iterating over keys:")
for key in person:
    print(f"    {key}: {person[key]}")

# Iterate over keys explicitly
print("\n  Iterating over keys():")
for key in person.keys():
    print(f"    {key}")

# Iterate over values
print("\n  Iterating over values():")
for value in person.values():
    print(f"    {value}")

# Iterate over items
print("\n  Iterating over items():")
for key, value in person.items():
    print(f"    {key}: {value}")

print()  # Empty line


# ============================================================================
# 7. NESTED DICTIONARIES
# ============================================================================
print("=" * 60)
print("7. NESTED DICTIONARIES")
print("=" * 60)

# Dictionary containing dictionaries
users = {
    "alice": {"age": 25, "city": "New York"},
    "bob": {"age": 30, "city": "London"},
    "charlie": {"age": 35, "city": "Paris"}
}

print("  Nested dictionary:")
for username, info in users.items():
    print(f"    {username}: {info}")

# Access nested values
print(f"\n  users['alice']['age']: {users['alice']['age']}")
print(f"  users['bob']['city']: {users['bob']['city']}")

# Modify nested
users["alice"]["age"] = 26
print(f"\n  After users['alice']['age'] = 26:")
print(f"    {users['alice']}")

print()  # Empty line


# ============================================================================
# 8. DICTIONARY COMPREHENSIONS (PREVIEW)
# ============================================================================
print("=" * 60)
print("8. DICTIONARY COMPREHENSIONS (PREVIEW)")
print("=" * 60)

# Create dictionary from range
squares = {x: x**2 for x in range(5)}
print(f"  Squares: {squares}")

# Create from two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
mapping = {k: v for k, v in zip(keys, values)}
print(f"  Mapping: {mapping}")

# Filter dictionary
numbers = {1: "one", 2: "two", 3: "three", 4: "four"}
even = {k: v for k, v in numbers.items() if k % 2 == 0}
print(f"  Even numbers: {even}")

print()  # Empty line


# ============================================================================
# 9. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("9. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: User profile
print("Example 1: User Profile")
user = {
    "username": "alice123",
    "email": "alice@example.com",
    "age": 25,
    "is_active": True
}
print(f"  User: {user}")
print(f"  Username: {user['username']}")
print(f"  Active: {user['is_active']}")

# Example 2: Word counter
print("\nExample 2: Word Counter")
text = "hello world hello python world"
words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(f"  Text: '{text}'")
print(f"  Word counts: {word_count}")

# Example 3: Configuration
print("\nExample 3: Configuration")
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True,
    "database": {
        "name": "mydb",
        "user": "admin"
    }
}
print(f"  Config: {config}")
print(f"  Host: {config['host']}")
print(f"  Database name: {config['database']['name']}")

# Example 4: Phone book
print("\nExample 4: Phone Book")
phonebook = {
    "Alice": "555-0101",
    "Bob": "555-0102",
    "Charlie": "555-0103"
}
print("  Phone book:")
for name, phone in phonebook.items():
    print(f"    {name}: {phone}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("DICTIONARIES SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Key-value pairs")
print("  - Mutable (can be modified)")
print("  - Keys must be immutable (strings, numbers, tuples)")
print("  - Fast lookups by key")
print("  - Unordered (ordered in Python 3.7+)")
print("\nCommon Operations:")
print("  - Access: dict[key] or dict.get(key)")
print("  - Add/Update: dict[key] = value")
print("  - Remove: del, pop(), popitem()")
print("  - Iterate: keys(), values(), items()")
print("  - Check: 'key' in dict")
print("=" * 60)

