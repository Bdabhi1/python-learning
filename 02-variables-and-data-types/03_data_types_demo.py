"""
Data Types in Python - Comprehensive Demonstration

This file shows all the fundamental data types in Python with detailed examples.
Understanding data types is crucial for writing correct Python programs.
"""

# ============================================================================
# 1. INTEGERS (int)
# ============================================================================
print("=" * 60)
print("1. INTEGERS (int)")
print("=" * 60)

# Whole numbers (positive, negative, or zero)
age = 25
temperature = -10
count = 0
big_number = 1000000
negative_number = -42

print(f"age = {age}, type: {type(age)}")
print(f"temperature = {temperature}, type: {type(temperature)}")
print(f"count = {count}, type: {type(count)}")
print(f"big_number = {big_number}, type: {type(big_number)}")

# Integer operations
x, y = 10, 3
print(f"\nInteger operations with x={x}, y={y}:")
print(f"  Addition: {x} + {y} = {x + y}")
print(f"  Subtraction: {x} - {y} = {x - y}")
print(f"  Multiplication: {x} * {y} = {x * y}")
print(f"  Division: {x} / {y} = {x / y} (returns float!)")
print(f"  Floor division: {x} // {y} = {x // y}")
print(f"  Modulo: {x} % {y} = {x % y}")
print(f"  Exponentiation: {x} ** {y} = {x ** y}")

print()  # Empty line


# ============================================================================
# 2. FLOATING-POINT NUMBERS (float)
# ============================================================================
print("=" * 60)
print("2. FLOATING-POINT NUMBERS (float)")
print("=" * 60)

# Numbers with decimal points
price = 19.99
temperature = 98.6
pi = 3.14159
small_number = 0.001
scientific = 1.5e3  # 1500.0 (scientific notation)
negative_float = -3.14

print(f"price = {price}, type: {type(price)}")
print(f"temperature = {temperature}, type: {type(temperature)}")
print(f"pi = {pi}, type: {type(pi)}")
print(f"scientific notation: 1.5e3 = {scientific}, type: {type(scientific)}")

# Float operations
a, b = 10.5, 3.2
print(f"\nFloat operations with a={a}, b={b}:")
print(f"  Addition: {a} + {b} = {a + b}")
print(f"  Subtraction: {a} - {b} = {a - b}")
print(f"  Multiplication: {a} * {b} = {a * b}")
print(f"  Division: {a} / {b} = {a / b}")

# Be aware of floating-point precision issues
print(f"\nFloating-point precision example:")
print(f"  0.1 + 0.2 = {0.1 + 0.2}")  # Might not be exactly 0.3!
print(f"  (This is normal in floating-point arithmetic)")

print()  # Empty line


# ============================================================================
# 3. STRINGS (str)
# ============================================================================
print("=" * 60)
print("3. STRINGS (str)")
print("=" * 60)

# Text data - sequences of characters
name = "Alice"
greeting = 'Hello'
message = "Python is awesome!"
multiline = """This is a
multi-line
string"""

print(f"name = {name}, type: {type(name)}")
print(f"greeting = {greeting}, type: {type(greeting)}")
print(f"message = {message}, type: {type(message)}")
print(f"\nMultiline string:\n{multiline}")

# String operations
s1, s2 = "Hello", "World"
print(f"\nString operations with '{s1}' and '{s2}':")
print(f"  Concatenation: '{s1}' + ' ' + '{s2}' = '{s1 + ' ' + s2}'")
print(f"  Repetition: '{s1}' * 3 = '{s1 * 3}'")
print(f"  Length: len('{s1}') = {len(s1)}")
print(f"  Indexing: '{s1}[0]' = '{s1[0]}'")
print(f"  Slicing: '{s1}[1:4]' = '{s1[1:4]}'")
print(f"  Membership: 'lo' in '{s1}' = {'lo' in s1}")
print(f"  Upper case: '{s1}'.upper() = '{s1.upper()}'")
print(f"  Lower case: '{s1}'.lower() = '{s1.lower()}'")

# String formatting (f-strings - Python 3.6+)
age = 25
print(f"\nString formatting (f-strings):")
print(f"  My name is {name} and I'm {age} years old")

print()  # Empty line


# ============================================================================
# 4. BOOLEANS (bool)
# ============================================================================
print("=" * 60)
print("4. BOOLEANS (bool)")
print("=" * 60)

# Truth values: True or False (must be capitalized!)
is_active = True
is_complete = False
is_raining = True

print(f"is_active = {is_active}, type: {type(is_active)}")
print(f"is_complete = {is_complete}, type: {type(is_complete)}")
print(f"is_raining = {is_raining}, type: {type(is_raining)}")

# Boolean operations
x, y = True, False
print(f"\nBoolean operations with x={x}, y={y}:")
print(f"  AND: {x} and {y} = {x and y}")
print(f"  OR: {x} or {y} = {x or y}")
print(f"  NOT: not {x} = {not x}")
print(f"  NOT: not {y} = {not y}")

# Boolean values from comparisons
print(f"\nBoolean values from comparisons:")
print(f"  5 > 3 = {5 > 3}")
print(f"  5 < 3 = {5 < 3}")
print(f"  5 == 5 = {5 == 5}")
print(f"  5 != 3 = {5 != 3}")

# Truthiness (values that evaluate to True/False)
print(f"\nTruthiness examples:")
print(f"  bool(1) = {bool(1)}")
print(f"  bool(0) = {bool(0)}")
print(f"  bool('Hello') = {bool('Hello')}")
print(f"  bool('') = {bool('')}")
print(f"  bool([]) = {bool([])}")
print(f"  bool([1, 2, 3]) = {bool([1, 2, 3])}")

print()  # Empty line


# ============================================================================
# 5. NONE TYPE
# ============================================================================
print("=" * 60)
print("5. NONE TYPE")
print("=" * 60)

# Represents the absence of a value
result = None
data = None
value = None

print(f"result = {result}, type: {type(result)}")
print(f"data = {data}, type: {type(data)}")

# None is falsy
print(f"\nNone in boolean context:")
print(f"  bool(None) = {bool(None)}")
print(f"  None == False = {None == False}")  # False (None is not False)
print(f"  None is None = {None is None}")    # True (use 'is' for None)

# Common use case: default value or "not set"
def get_user_data(user_id):
    """Simulate getting user data."""
    if user_id == 1:
        return {"name": "Alice", "age": 25}
    return None  # User not found

user = get_user_data(1)
print(f"\nFunction returning None example:")
print(f"  get_user_data(1) = {user}")
print(f"  get_user_data(999) = {get_user_data(999)}")

print()  # Empty line


# ============================================================================
# 6. TYPE CHECKING
# ============================================================================
print("=" * 60)
print("6. TYPE CHECKING")
print("=" * 60)

# Check the type of a variable
variables = [
    42,
    3.14,
    "Hello",
    True,
    None
]

print("Type checking examples:")
for var in variables:
    print(f"  {repr(var):10} -> type: {type(var).__name__}")

# Using isinstance() (preferred method)
print(f"\nUsing isinstance() (preferred):")
age = 25
print(f"  isinstance({age}, int) = {isinstance(age, int)}")
print(f"  isinstance({age}, str) = {isinstance(age, str)}")
print(f"  isinstance({age}, (int, float)) = {isinstance(age, (int, float))}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("DATA TYPES SUMMARY:")
print("=" * 60)
print("1. int:    Whole numbers (25, -10, 0)")
print("2. float:  Decimal numbers (3.14, -0.5, 1.5e3)")
print("3. str:    Text data ('Hello', \"World\")")
print("4. bool:   Truth values (True, False)")
print("5. None:   Absence of value (None)")
print("=" * 60)
print("\nRemember:")
print("- Python is dynamically typed (types determined at runtime)")
print("- Variables can change types")
print("- Use type() or isinstance() to check types")
print("- Each type has specific operations and behaviors")
print("=" * 60)

