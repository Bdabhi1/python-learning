"""
Utility Built-in Functions

This file demonstrates other useful built-in functions including
range(), open(), iter(), next(), hash(), and more.
"""

# ============================================================================
# 1. RANGE() - GENERATE NUMBER SEQUENCE
# ============================================================================
print("=" * 60)
print("1. RANGE() - GENERATE NUMBER SEQUENCE")
print("=" * 60)

# range(stop) - 0 to stop-1
result1 = list(range(5))
print(f"  list(range(5)): {result1}")

# range(start, stop) - start to stop-1
result2 = list(range(2, 5))
print(f"  list(range(2, 5)): {result2}")

# range(start, stop, step) - with step
result3 = list(range(0, 10, 2))
print(f"  list(range(0, 10, 2)): {result3}")

# Negative step
result4 = list(range(10, 0, -1))
print(f"  list(range(10, 0, -1)): {result4}")

# In loops
print("\n  Using in for loop:")
for i in range(3):
    print(f"    {i}")

print()  # Empty line


# ============================================================================
# 2. OPEN() - OPEN FILE
# ============================================================================
print("=" * 60)
print("2. OPEN() - OPEN FILE")
print("=" * 60)

# Open file for reading
print("  Opening file (example):")
print("    file = open('data.txt', 'r')")
print("    content = file.read()")
print("    file.close()")

# Better: Use with statement
print("\n  Better: Use 'with' statement")
print("    with open('data.txt', 'r') as file:")
print("        content = file.read()")

print("\n  File modes:")
print("    'r' - Read")
print("    'w' - Write")
print("    'a' - Append")
print("    'x' - Exclusive creation")

print()  # Empty line


# ============================================================================
# 3. ITER() AND NEXT() - ITERATORS
# ============================================================================
print("=" * 60)
print("3. ITER() AND NEXT() - ITERATORS")
print("=" * 60)

# Create iterator
my_list = [1, 2, 3, 4, 5]
iterator = iter(my_list)

# Get next item
print(f"  iterator = iter([1,2,3,4,5])")
print(f"  next(iterator): {next(iterator)}")
print(f"  next(iterator): {next(iterator)}")
print(f"  next(iterator): {next(iterator)}")

# With default (no StopIteration error)
iterator2 = iter([1, 2])
print(f"\n  next(iterator, 'end'): {next(iterator2, 'end')}")
print(f"  next(iterator, 'end'): {next(iterator2, 'end')}")
print(f"  next(iterator, 'end'): {next(iterator2, 'end')}")

print()  # Empty line


# ============================================================================
# 4. HASH() - GET HASH VALUE
# ============================================================================
print("=" * 60)
print("4. HASH() - GET HASH VALUE")
print("=" * 60)

# Hash immutable objects
result1 = hash("hello")
print(f"  hash('hello'): {result1}")

result2 = hash(42)
print(f"  hash(42): {result2}")

result3 = hash((1, 2, 3))
print(f"  hash((1,2,3)): {result3}")

# Mutable objects cannot be hashed
# hash([1,2,3])  # TypeError!

print("\n  Note: Only immutable objects can be hashed")
print("  Used internally by dictionaries and sets")

print()  # Empty line


# ============================================================================
# 5. CALLABLE() - CHECK IF CALLABLE
# ============================================================================
print("=" * 60)
print("5. CALLABLE() - CHECK IF CALLABLE")
print("=" * 60)

# Check if object is callable
result1 = callable(print)
print(f"  callable(print): {result1}")

result2 = callable(len)
print(f"  callable(len): {result2}")

result3 = callable(5)
print(f"  callable(5): {result3}")

# Function
def my_function():
    pass

result4 = callable(my_function)
print(f"  callable(my_function): {result4}")

# Class
class MyClass:
    pass

result5 = callable(MyClass)
print(f"  callable(MyClass): {result5}")

print()  # Empty line


# ============================================================================
# 6. GLOBALS() AND LOCALS() - NAMESPACE
# ============================================================================
print("=" * 60)
print("6. GLOBALS() AND LOCALS() - NAMESPACE")
print("=" * 60)

# Get global variables
x = 10
y = 20
globals_dict = globals()
print(f"  'x' in globals(): {'x' in globals_dict}")
print(f"  globals()['x']: {globals_dict['x']}")

# Get local variables
def my_function():
    local_var = 5
    locals_dict = locals()
    print(f"    Local variables: {list(locals_dict.keys())}")

print("  Local variables in function:")
my_function()

print("\n  Note: Usually not needed, but useful for introspection")

print()  # Empty line


# ============================================================================
# 7. VARS() - GET OBJECT DICTIONARY
# ============================================================================
print("=" * 60)
print("7. VARS() - GET OBJECT DICTIONARY")
print("=" * 60)

# Get object's __dict__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)
person_dict = vars(person)
print(f"  person = Person('Alice', 25)")
print(f"  vars(person): {person_dict}")

# Same as __dict__
print(f"  person.__dict__: {person.__dict__}")

print()  # Empty line


# ============================================================================
# 8. EVAL() AND EXEC() - EVALUATE CODE
# ============================================================================
print("=" * 60)
print("8. EVAL() AND EXEC() - EVALUATE CODE")
print("=" * 60)

# eval() - Evaluate expression
result1 = eval("2 + 3")
print(f"  eval('2 + 3'): {result1}")

result2 = eval("'hello' + 'world'")
print(f"  eval(\"'hello' + 'world'\"): {result2}")

# exec() - Execute statement
x = 0
exec("x = 5")
print(f"\n  After exec('x = 5'): x = {x}")

print("\n  ⚠️  WARNING: eval() and exec() can be dangerous!")
print("     Never use with user input - security risk!")
print("     Usually not needed - find alternatives")

print()  # Empty line


# ============================================================================
# 9. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("9. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Generate number sequence
print("Example 1: Generate Number Sequence")
even_numbers = list(range(0, 20, 2))
print(f"  Even numbers 0-18: {even_numbers}")

# Example 2: Countdown
print("\nExample 2: Countdown")
countdown = list(range(10, 0, -1))
print(f"  Countdown: {countdown}")

# Example 3: Check if callable before calling
print("\nExample 3: Safe Function Call")
def safe_call(func, *args):
    if callable(func):
        return func(*args)
    else:
        return f"{func} is not callable"

result = safe_call(len, [1, 2, 3])
print(f"  safe_call(len, [1,2,3]): {result}")

# Example 4: Iterator with default
print("\nExample 4: Iterator with Default")
data = [1, 2, 3]
it = iter(data)
for _ in range(5):
    value = next(it, None)
    if value is None:
        print("    End of iterator")
        break
    print(f"    {value}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("UTILITY FUNCTIONS SUMMARY:")
print("=" * 60)
print("Function     | Description              | Example")
print("-" * 55)
print("range()      | Generate number sequence | range(5) -> 0,1,2,3,4")
print("open()       | Open file                | open('file.txt', 'r')")
print("iter()       | Create iterator          | iter([1,2,3])")
print("next()       | Get next item            | next(iterator)")
print("hash()       | Get hash value           | hash('hello')")
print("callable()   | Check if callable        | callable(print)")
print("globals()    | Get global namespace     | globals()")
print("locals()     | Get local namespace      | locals()")
print("vars()       | Get object dictionary    | vars(obj)")
print("eval()       | Evaluate expression      | eval('2+3')")
print("exec()       | Execute statement        | exec('x=5')")
print("=" * 60)
print("\nKey Points:")
print("  - range() generates number sequences efficiently")
print("  - open() is used for file operations")
print("  - iter()/next() for manual iteration")
print("  - hash() only works with immutable objects")
print("  - ⚠️  Avoid eval()/exec() with user input (security risk)")
print("=" * 60)

