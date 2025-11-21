"""
Object Built-in Functions

This file demonstrates built-in functions for working with objects,
types, and introspection.
"""

# ============================================================================
# 1. TYPE() - GET TYPE
# ============================================================================
print("=" * 60)
print("1. TYPE() - GET TYPE")
print("=" * 60)

# Get type of object
result1 = type(5)
print(f"  type(5): {result1}")

result2 = type("hello")
print(f"  type('hello'): {result2}")

result3 = type([1, 2, 3])
print(f"  type([1,2,3]): {result3}")

result4 = type(True)
print(f"  type(True): {result4}")

# Compare types
x = 5
print(f"\n  type(x) == int: {type(x) == int}")

print()  # Empty line


# ============================================================================
# 2. ISINSTANCE() - TYPE CHECKING
# ============================================================================
print("=" * 60)
print("2. ISINSTANCE() - TYPE CHECKING")
print("=" * 60)

# Check if object is instance of type
result1 = isinstance(5, int)
print(f"  isinstance(5, int): {result1}")

result2 = isinstance("hello", str)
print(f"  isinstance('hello', str): {result2}")

result3 = isinstance([1, 2], list)
print(f"  isinstance([1,2], list): {result3}")

# Check multiple types
result4 = isinstance(5, (int, float))
print(f"  isinstance(5, (int, float)): {result4}")

result5 = isinstance(3.14, (int, float))
print(f"  isinstance(3.14, (int, float)): {result5}")

print("\n  Preferred over type() == for type checking")

print()  # Empty line


# ============================================================================
# 3. ID() - GET OBJECT ID
# ============================================================================
print("=" * 60)
print("3. ID() - GET OBJECT ID")
print("=" * 60)

# Get unique identifier (memory address)
x = 5
y = 5
z = [1, 2, 3]
w = [1, 2, 3]

print(f"  x = 5, id(x): {id(x)}")
print(f"  y = 5, id(y): {id(y)}")
print(f"  Same id: {id(x) == id(y)} (small integers are cached)")

print(f"\n  z = [1,2,3], id(z): {id(z)}")
print(f"  w = [1,2,3], id(w): {id(w)}")
print(f"  Same id: {id(z) == id(w)} (different objects)")

# Check if same object
print(f"\n  z is w: {z is w} (different objects)")
print(f"  x is y: {x is y} (same object for small integers)")

print()  # Empty line


# ============================================================================
# 4. DIR() - GET ATTRIBUTES
# ============================================================================
print("=" * 60)
print("4. DIR() - GET ATTRIBUTES")
print("=" * 60)

# Get attributes and methods of object
string_attrs = dir("hello")
print(f"  dir('hello') returns {len(string_attrs)} attributes/methods")
print(f"  First 10: {string_attrs[:10]}")

# Filter methods
methods = [attr for attr in dir("hello") if not attr.startswith("_")]
print(f"\n  Public methods (first 10): {methods[:10]}")

# Check if attribute exists
has_upper = "upper" in dir("hello")
print(f"\n  'upper' in dir('hello'): {has_upper}")

print()  # Empty line


# ============================================================================
# 5. HELP() - GET DOCUMENTATION
# ============================================================================
print("=" * 60)
print("5. HELP() - GET DOCUMENTATION")
print("=" * 60)

# Get help for function
print("  help(print) - Shows documentation for print()")
print("  (Output would be too long to display here)")
print("\n  Try in interactive Python:")
print("    >>> help(print)")
print("    >>> help(str.upper)")
print("    >>> help(len)")

# Get help for object
print("\n  help([1,2,3]) - Shows documentation for list methods")

print()  # Empty line


# ============================================================================
# 6. HASATTR() - CHECK ATTRIBUTE
# ============================================================================
print("=" * 60)
print("6. HASATTR() - CHECK ATTRIBUTE")
print("=" * 60)

# Check if object has attribute
result1 = hasattr("hello", "upper")
print(f"  hasattr('hello', 'upper'): {result1}")

result2 = hasattr("hello", "append")
print(f"  hasattr('hello', 'append'): {result2}")

result3 = hasattr([1, 2, 3], "append")
print(f"  hasattr([1,2,3], 'append'): {result3}")

# Get attribute if exists
if hasattr("hello", "upper"):
    method = getattr("hello", "upper")
    result = method()
    print(f"\n  getattr('hello', 'upper')(): {result}")

print()  # Empty line


# ============================================================================
# 7. GETATTR() AND SETATTR()
# ============================================================================
print("=" * 60)
print("7. GETATTR() AND SETATTR()")
print("=" * 60)

# Get attribute
text = "hello"
upper_method = getattr(text, "upper")
result1 = upper_method()
print(f"  getattr('hello', 'upper')(): {result1}")

# With default
result2 = getattr(text, "lower", "default")
print(f"  getattr('hello', 'lower', 'default'): {result2}")

# Set attribute (works with objects)
class Person:
    pass

person = Person()
setattr(person, "name", "Alice")
print(f"\n  After setattr(person, 'name', 'Alice'):")
print(f"    person.name: {person.name}")

# Get attribute
name = getattr(person, "name")
print(f"    getattr(person, 'name'): {name}")

print()  # Empty line


# ============================================================================
# 8. REPR() - STRING REPRESENTATION
# ============================================================================
print("=" * 60)
print("8. REPR() - STRING REPRESENTATION")
print("=" * 60)

# Get string representation
result1 = repr("hello")
print(f"  repr('hello'): {result1} (includes quotes)")

result2 = str("hello")
print(f"  str('hello'): {result2} (no quotes)")

# For debugging
x = [1, 2, 3]
print(f"\n  repr([1,2,3]): {repr(x)}")
print(f"  str([1,2,3]): {str(x)}")

# repr() is what you'd type to recreate the object
print("\n  repr() shows how to recreate the object")

print()  # Empty line


# ============================================================================
# 9. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("9. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Type checking function
print("Example 1: Type Checking Function")
def process_data(data):
    if isinstance(data, int):
        return f"Integer: {data}"
    elif isinstance(data, str):
        return f"String: {data}"
    elif isinstance(data, list):
        return f"List with {len(data)} items"
    else:
        return f"Unknown type: {type(data)}"

print(f"  process_data(5): {process_data(5)}")
print(f"  process_data('hello'): {process_data('hello')}")
print(f"  process_data([1,2,3]): {process_data([1,2,3])}")

# Example 2: Dynamic method calling
print("\nExample 2: Dynamic Method Calling")
text = "hello"
method_name = "upper"
if hasattr(text, method_name):
    method = getattr(text, method_name)
    result = method()
    print(f"  Called {method_name}(): {result}")

# Example 3: Check object capabilities
print("\nExample 3: Check Object Capabilities")
def can_append(obj):
    return hasattr(obj, "append") and callable(getattr(obj, "append", None))

print(f"  can_append([1,2,3]): {can_append([1,2,3])}")
print(f"  can_append('hello'): {can_append('hello')}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("OBJECT FUNCTIONS SUMMARY:")
print("=" * 60)
print("Function     | Description              | Example")
print("-" * 55)
print("type()       | Get type                 | type(5) -> <class 'int'>")
print("isinstance() | Type check               | isinstance(5, int) -> True")
print("id()         | Get object ID            | id(x)")
print("dir()        | Get attributes          | dir('hello')")
print("help()       | Get documentation        | help(print)")
print("hasattr()    | Check attribute          | hasattr(obj, 'attr')")
print("getattr()    | Get attribute            | getattr(obj, 'attr')")
print("setattr()    | Set attribute            | setattr(obj, 'attr', val)")
print("repr()       | String representation    | repr('hello') -> \"'hello'\"")
print("=" * 60)
print("\nKey Points:")
print("  - Use isinstance() instead of type() == for type checking")
print("  - id() returns unique identifier (memory address)")
print("  - dir() shows all attributes and methods")
print("  - help() provides documentation")
print("  - hasattr()/getattr()/setattr() for dynamic attribute access")
print("=" * 60)

