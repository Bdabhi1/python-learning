"""
namedtuple and ChainMap in Python Collections Module

This file demonstrates namedtuple (tuples with named fields) and
ChainMap (multiple dictionaries as single mapping).
"""

from collections import namedtuple, ChainMap

# ============================================================================
# 1. CREATING NAMEDTUPLES
# ============================================================================
print("=" * 60)
print("1. CREATING NAMEDTUPLES")
print("=" * 60)

# Define a Point namedtuple
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(11, y=22)
print(f"  Point(11, y=22): {p1}")
print(f"  p1.x: {p1.x}, p1.y: {p1.y}")

# Access by index or name
print(f"  p1[0]: {p1[0]}, p1[1]: {p1[1]}")

# Define a Person namedtuple
Person = namedtuple('Person', ['name', 'age', 'city'])
person = Person('Alice', 30, 'NYC')
print(f"\n  Person: {person}")
print(f"  {person.name} is {person.age} years old, lives in {person.city}")

print()  # Empty line


# ============================================================================
# 2. NAMEDTUPLE METHODS
# ============================================================================
print("=" * 60)
print("2. NAMEDTUPLE METHODS")
print("=" * 60)

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, 22)

# Convert to dictionary
print(f"  Point: {p}")
print(f"  _asdict(): {p._asdict()}")

# Replace fields (creates new instance)
p_new = p._replace(x=33)
print(f"  Original: {p}")
print(f"  _replace(x=33): {p_new}")

# Get all fields
print(f"  _fields: {Point._fields}")

# Get field defaults (if any)
Point2 = namedtuple('Point2', ['x', 'y', 'z'], defaults=[0])
print(f"  Point2._fields: {Point2._fields}")
print(f"  Point2._field_defaults: {Point2._field_defaults}")

print()  # Empty line


# ============================================================================
# 3. NAMEDTUPLE WITH DEFAULTS
# ============================================================================
print("=" * 60)
print("3. NAMEDTUPLE WITH DEFAULTS")
print("=" * 60)

# Namedtuple with defaults (Python 3.7+)
Person = namedtuple('Person', ['name', 'age', 'city'], defaults=['Unknown'])
person1 = Person('Alice', 30)
print(f"  Person('Alice', 30): {person1}")
print(f"  city defaults to: {person1.city}")

person2 = Person('Bob', 25, 'LA')
print(f"  Person('Bob', 25, 'LA'): {person2}")

print()  # Empty line


# ============================================================================
# 4. PRACTICAL EXAMPLES: NAMEDTUPLE
# ============================================================================
print("=" * 60)
print("4. PRACTICAL EXAMPLES: NAMEDTUPLE")
print("=" * 60)

# Represent coordinates
Coordinate = namedtuple('Coordinate', ['latitude', 'longitude'])
nyc = Coordinate(40.7128, -74.0060)
print(f"  NYC coordinates: {nyc.latitude}, {nyc.longitude}")

# Represent RGB color
Color = namedtuple('Color', ['red', 'green', 'blue'])
red = Color(255, 0, 0)
print(f"  Red color: RGB{red}")

# Represent a card
Card = namedtuple('Card', ['rank', 'suit'])
ace_spades = Card('A', 'Spades')
print(f"  Card: {ace_spades.rank} of {ace_spades.suit}")

print()  # Empty line


# ============================================================================
# 5. CREATING CHAINMAP
# ============================================================================
print("=" * 60)
print("5. CREATING CHAINMAP")
print("=" * 60)

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain = ChainMap(dict1, dict2)

print(f"  dict1: {dict1}")
print(f"  dict2: {dict2}")
print(f"  ChainMap: {dict(chain)}")

# Lookup order: searches dict1 first, then dict2
print(f"  chain['a']: {chain['a']} (from dict1)")
print(f"  chain['b']: {chain['b']} (from dict1, first match)")
print(f"  chain['c']: {chain['c']} (from dict2)")

print()  # Empty line


# ============================================================================
# 6. CHAINMAP OPERATIONS
# ============================================================================
print("=" * 60)
print("6. CHAINMAP OPERATIONS")
print("=" * 60)

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3}
chain = ChainMap(dict1, dict2)

# Get all keys (may have duplicates)
print(f"  Keys: {list(chain.keys())}")

# Get all values
print(f"  Values: {list(chain.values())}")

# Get all items
print(f"  Items: {list(chain.items())}")

# Check membership
print(f"  'a' in chain: {'a' in chain}")
print(f"  'd' in chain: {'d' in chain}")

print()  # Empty line


# ============================================================================
# 7. CHAINMAP MODIFICATIONS
# ============================================================================
print("=" * 60)
print("7. CHAINMAP MODIFICATIONS")
print("=" * 60)

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3}
chain = ChainMap(dict1, dict2)

print(f"  Initial: {dict(chain)}")

# Modifications affect first mapping
chain['a'] = 10
chain['d'] = 4
print(f"  After modifications: {dict(chain)}")
print(f"  dict1: {dict1} (modified)")
print(f"  dict2: {dict2} (unchanged)")

print()  # Empty line


# ============================================================================
# 8. CHAINMAP NEW_CHILD AND PARENTS
# ============================================================================
print("=" * 60)
print("8. CHAINMAP NEW_CHILD AND PARENTS")
print("=" * 60)

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3}
chain = ChainMap(dict1, dict2)

print(f"  Initial: {dict(chain)}")

# Add new child (new mapping at beginning)
new_dict = {'d': 4}
chain = chain.new_child(new_dict)
print(f"  After new_child: {dict(chain)}")

# Get parents (all mappings except first)
parents = chain.parents
print(f"  Parents: {dict(parents)}")

print()  # Empty line


# ============================================================================
# 9. PRACTICAL EXAMPLE: CONFIGURATION WITH DEFAULTS
# ============================================================================
print("=" * 60)
print("9. PRACTICAL EXAMPLE: CONFIGURATION WITH DEFAULTS")
print("=" * 60)

# Default configuration
defaults = {
    'theme': 'dark',
    'language': 'en',
    'font_size': 12,
    'notifications': True
}

# User preferences (override defaults)
user_prefs = {
    'theme': 'light',
    'font_size': 14
}

# Command-line arguments (highest priority)
cli_args = {
    'notifications': False
}

# Create ChainMap (first dict has highest priority)
config = ChainMap(cli_args, user_prefs, defaults)

print(f"  Defaults: {defaults}")
print(f"  User prefs: {user_prefs}")
print(f"  CLI args: {cli_args}")
print(f"\n  Final config:")
for key in ['theme', 'language', 'font_size', 'notifications']:
    print(f"    {key}: {config[key]}")

print()  # Empty line


# ============================================================================
# 10. PRACTICAL EXAMPLE: ENVIRONMENT VARIABLES
# ============================================================================
print("=" * 60)
print("10. PRACTICAL EXAMPLE: ENVIRONMENT VARIABLES")
print("=" * 60)

# Simulate environment variables
import os

# Default settings
default_settings = {
    'HOST': 'localhost',
    'PORT': 8080,
    'DEBUG': False
}

# Environment overrides (simulated)
env_vars = {
    'PORT': 9000,
    'DEBUG': True
}

# Create ChainMap
settings = ChainMap(env_vars, default_settings)

print(f"  Default settings: {default_settings}")
print(f"  Environment vars: {env_vars}")
print(f"\n  Final settings:")
for key in ['HOST', 'PORT', 'DEBUG']:
    print(f"    {key}: {settings[key]}")

print()  # Empty line


# ============================================================================
# 11. NAMEDTUPLE VS REGULAR TUPLE
# ============================================================================
print("=" * 60)
print("11. NAMEDTUPLE VS REGULAR TUPLE")
print("=" * 60)

# Regular tuple (less readable)
point_tuple = (11, 22)
print(f"  Regular tuple: {point_tuple}")
print(f"  Access: point_tuple[0] = {point_tuple[0]}")

# Namedtuple (more readable)
Point = namedtuple('Point', ['x', 'y'])
point_named = Point(11, 22)
print(f"  Namedtuple: {point_named}")
print(f"  Access: point_named.x = {point_named.x}")

print("\n  Namedtuple advantages:")
print("    - More readable code")
print("    - Self-documenting")
print("    - Can access by name or index")
print("    - Still immutable like tuple")

print()  # Empty line


# ============================================================================
# 12. CHAINMAP VS DICT.UPDATE
# ============================================================================
print("=" * 60)
print("12. CHAINMAP VS DICT.UPDATE")
print("=" * 60)

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Using ChainMap (doesn't modify original dicts)
chain = ChainMap(dict1, dict2)
print(f"  ChainMap: {dict(chain)}")
print(f"  dict1 unchanged: {dict1}")

# Using update (modifies first dict)
dict1_copy = dict1.copy()
dict1_copy.update(dict2)
print(f"  dict.update: {dict1_copy}")
print(f"  Original dict1 would be modified")

print("\n  ChainMap advantages:")
print("    - Doesn't modify original dictionaries")
print("    - Dynamic (changes in original dicts are reflected)")
print("    - Can have multiple layers")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("NAMEDTUPLE AND CHAINMAP SUMMARY:")
print("=" * 60)
print("namedtuple:")
print("  - Tuple with named fields")
print("  - More readable than regular tuples")
print("  - Immutable like tuples")
print("  - Access by name or index")
print("  - Methods: _asdict(), _replace(), _fields")
print("\nChainMap:")
print("  - Multiple dictionaries as single mapping")
print("  - Searches mappings in order")
print("  - Doesn't modify original dictionaries")
print("  - Useful for configuration with defaults")
print("  - Methods: new_child(), parents")
print("=" * 60)

