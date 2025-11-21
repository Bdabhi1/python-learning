"""
Type Conversion Built-in Functions

This file demonstrates built-in functions for converting between
different data types in Python.
"""

# ============================================================================
# 1. INT() - CONVERT TO INTEGER
# ============================================================================
print("=" * 60)
print("1. INT() - CONVERT TO INTEGER")
print("=" * 60)

# From string
result1 = int("42")
print(f"  int('42'): {result1}, type: {type(result1).__name__}")

# From float (truncates)
result2 = int(3.14)
print(f"  int(3.14): {result2} (truncates decimal)")

result3 = int(3.99)
print(f"  int(3.99): {result3} (truncates, doesn't round)")

# From boolean
result4 = int(True)
print(f"  int(True): {result4}")

result5 = int(False)
print(f"  int(False): {result5}")

# With base (convert from different number systems)
result6 = int("1010", 2)  # Binary to decimal
print(f"  int('1010', 2): {result6} (binary to decimal)")

result7 = int("FF", 16)  # Hexadecimal to decimal
print(f"  int('FF', 16): {result7} (hex to decimal)")

print()  # Empty line


# ============================================================================
# 2. FLOAT() - CONVERT TO FLOAT
# ============================================================================
print("=" * 60)
print("2. FLOAT() - CONVERT TO FLOAT")
print("=" * 60)

# From integer
result1 = float(5)
print(f"  float(5): {result1}, type: {type(result1).__name__}")

# From string
result2 = float("3.14")
print(f"  float('3.14'): {result2}")

result3 = float("42")
print(f"  float('42'): {result3}")

# From boolean
result4 = float(True)
print(f"  float(True): {result4}")

print()  # Empty line


# ============================================================================
# 3. STR() - CONVERT TO STRING
# ============================================================================
print("=" * 60)
print("3. STR() - CONVERT TO STRING")
print("=" * 60)

# From integer
result1 = str(42)
print(f"  str(42): '{result1}', type: {type(result1).__name__}")

# From float
result2 = str(3.14)
print(f"  str(3.14): '{result2}'")

# From boolean
result3 = str(True)
print(f"  str(True): '{result3}'")

# From None
result4 = str(None)
print(f"  str(None): '{result4}'")

# From list
result5 = str([1, 2, 3])
print(f"  str([1, 2, 3]): '{result5}'")

print()  # Empty line


# ============================================================================
# 4. BOOL() - CONVERT TO BOOLEAN
# ============================================================================
print("=" * 60)
print("4. BOOL() - CONVERT TO BOOLEAN")
print("=" * 60)

# From numbers
print("  From numbers:")
print(f"    bool(1): {bool(1)}")
print(f"    bool(0): {bool(0)}")
print(f"    bool(-1): {bool(-1)}")
print(f"    bool(3.14): {bool(3.14)}")
print(f"    bool(0.0): {bool(0.0)}")

# From strings
print("\n  From strings:")
print(f"    bool('hello'): {bool('hello')}")
print(f"    bool(''): {bool('')}")

# From collections
print("\n  From collections:")
print(f"    bool([1, 2]): {bool([1, 2])}")
print(f"    bool([]): {bool([])}")
print(f"    bool({{'a': 1}}): {bool({'a': 1})}")
print(f"    bool({{}}): {bool({})}")

# From None
print("\n  From None:")
print(f"    bool(None): {bool(None)}")

print("\n  Rule: Falsy values are: False, 0, 0.0, '', None, [], {{}}")
print("        Everything else is truthy")

print()  # Empty line


# ============================================================================
# 5. LIST() - CONVERT TO LIST
# ============================================================================
print("=" * 60)
print("5. LIST() - CONVERT TO LIST")
print("=" * 60)

# From string
result1 = list("hello")
print(f"  list('hello'): {result1}")

# From tuple
result2 = list((1, 2, 3))
print(f"  list((1, 2, 3)): {result2}")

# From set
result3 = list({1, 2, 3})
print(f"  list({{1, 2, 3}}): {result3}")

# From range
result4 = list(range(5))
print(f"  list(range(5)): {result4}")

# From dictionary (gets keys)
result5 = list({"a": 1, "b": 2})
print(f"  list({{'a': 1, 'b': 2}}): {result5} (gets keys)")

print()  # Empty line


# ============================================================================
# 6. TUPLE() - CONVERT TO TUPLE
# ============================================================================
print("=" * 60)
print("6. TUPLE() - CONVERT TO TUPLE")
print("=" * 60)

# From list
result1 = tuple([1, 2, 3])
print(f"  tuple([1, 2, 3]): {result1}")

# From string
result2 = tuple("hello")
print(f"  tuple('hello'): {result2}")

# From set
result3 = tuple({1, 2, 3})
print(f"  tuple({{1, 2, 3}}): {result3}")

# From range
result4 = tuple(range(5))
print(f"  tuple(range(5)): {result4}")

print()  # Empty line


# ============================================================================
# 7. SET() - CONVERT TO SET
# ============================================================================
print("=" * 60)
print("7. SET() - CONVERT TO SET")
print("=" * 60)

# From list (removes duplicates)
result1 = set([1, 2, 2, 3, 3, 4])
print(f"  set([1, 2, 2, 3, 3, 4]): {result1} (duplicates removed)")

# From string
result2 = set("hello")
print(f"  set('hello'): {result2}")

# From tuple
result3 = set((1, 2, 3))
print(f"  set((1, 2, 3)): {result3}")

# From range
result4 = set(range(5))
print(f"  set(range(5)): {result4}")

print()  # Empty line


# ============================================================================
# 8. DICT() - CONVERT TO DICTIONARY
# ============================================================================
print("=" * 60)
print("8. DICT() - CONVERT TO DICTIONARY")
print("=" * 60)

# From list of tuples
result1 = dict([("a", 1), ("b", 2), ("c", 3)])
print(f"  dict([('a', 1), ('b', 2)]): {result1}")

# From keyword arguments
result2 = dict(name="Alice", age=25)
print(f"  dict(name='Alice', age=25): {result2}")

# From another dictionary (copy)
original = {"a": 1, "b": 2}
result3 = dict(original)
print(f"  dict({{'a': 1, 'b': 2}}): {result3}")

print()  # Empty line


# ============================================================================
# 9. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("9. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: User input conversion
print("Example 1: User Input Conversion")
user_input = "25"  # Simulated input
age = int(user_input)
print(f"  Input: '{user_input}' -> Age: {age}")

# Example 2: Remove duplicates
print("\nExample 2: Remove Duplicates")
numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique = list(set(numbers))
print(f"  Original: {numbers}")
print(f"  Unique: {unique}")

# Example 3: Convert coordinates
print("\nExample 3: Convert Coordinates")
coords_list = [10, 20]
coords_tuple = tuple(coords_list)
print(f"  List: {coords_list}")
print(f"  Tuple: {coords_tuple}")

# Example 4: Safe conversion
print("\nExample 4: Safe Conversion")
def safe_int(value, default=0):
    """Safely convert to int."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

print(f"  safe_int('42'): {safe_int('42')}")
print(f"  safe_int('abc'): {safe_int('abc')}")
print(f"  safe_int('abc', -1): {safe_int('abc', -1)}")

# Example 5: Type checking before conversion
print("\nExample 5: Type Checking")
values = [1, "2", 3.0, "4.5", True]
converted = []
for val in values:
    if isinstance(val, int):
        converted.append(val)
    elif isinstance(val, str):
        try:
            converted.append(int(val))
        except ValueError:
            converted.append(val)
    else:
        converted.append(int(val))

print(f"  Original: {values}")
print(f"  Converted: {converted}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("TYPE CONVERSION FUNCTIONS SUMMARY:")
print("=" * 60)
print("Function | Converts To | Example")
print("-" * 50)
print("int()    | Integer     | int('42') -> 42")
print("float()  | Float        | float('3.14') -> 3.14")
print("str()    | String       | str(42) -> '42'")
print("bool()   | Boolean      | bool(1) -> True")
print("list()   | List         | list('hello') -> ['h','e','l','l','o']")
print("tuple()  | Tuple        | tuple([1,2,3]) -> (1,2,3)")
print("set()    | Set          | set([1,2,2,3]) -> {1,2,3}")
print("dict()   | Dictionary   | dict([('a',1)]) -> {'a':1}")
print("=" * 60)
print("\nKey Points:")
print("  - Always returns new object (doesn't modify original)")
print("  - May raise ValueError if conversion not possible")
print("  - Use try-except for safe conversion")
print("  - Check type with isinstance() before converting")
print("=" * 60)

