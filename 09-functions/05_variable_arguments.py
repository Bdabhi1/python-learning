"""
Variable Arguments in Functions

This file demonstrates *args and **kwargs - how to create functions
that accept variable numbers of arguments.
"""

# ============================================================================
# 1. *ARGS - VARIABLE POSITIONAL ARGUMENTS
# ============================================================================
print("=" * 60)
print("1. *ARGS - VARIABLE POSITIONAL ARGUMENTS")
print("=" * 60)

def sum_all(*args):
    """Sum all arguments."""
    return sum(args)

# Call with different numbers of arguments
result1 = sum_all(1, 2, 3)
print(f"  sum_all(1, 2, 3) = {result1}")

result2 = sum_all(1, 2, 3, 4, 5)
print(f"  sum_all(1, 2, 3, 4, 5) = {result2}")

result3 = sum_all(10, 20)
print(f"  sum_all(10, 20) = {result3}")

# args is a tuple
def print_args(*args):
    """Print all arguments."""
    print(f"    Type: {type(args)}")
    print(f"    Values: {args}")

print("\n  print_args(1, 2, 3):")
print_args(1, 2, 3)

print()  # Empty line


# ============================================================================
# 2. **KWARGS - VARIABLE KEYWORD ARGUMENTS
# ============================================================================
print("=" * 60)
print("2. **KWARGS - VARIABLE KEYWORD ARGUMENTS")
print("=" * 60)

def print_info(**kwargs):
    """Print all keyword arguments."""
    for key, value in kwargs.items():
        print(f"    {key}: {value}")

# Call with different keyword arguments
print("  print_info(name='Alice', age=25):")
print_info(name="Alice", age=25)

print("\n  print_info(name='Bob', age=30, city='NYC'):")
print_info(name="Bob", age=30, city="NYC")

# kwargs is a dictionary
def show_kwargs(**kwargs):
    """Show kwargs structure."""
    print(f"    Type: {type(kwargs)}")
    print(f"    Dictionary: {kwargs}")

print("\n  show_kwargs(a=1, b=2):")
show_kwargs(a=1, b=2)

print()  # Empty line


# ============================================================================
# 3. COMBINING *ARGS AND **KWARGS
# ============================================================================
print("=" * 60)
print("3. COMBINING *ARGS AND **KWARGS")
print("=" * 60)

def process_data(*args, **kwargs):
    """Process positional and keyword arguments."""
    print("    Positional arguments:")
    for arg in args:
        print(f"      - {arg}")
    
    print("    Keyword arguments:")
    for key, value in kwargs.items():
        print(f"      - {key}: {value}")

print("  process_data(1, 2, 3, name='Alice', age=25):")
process_data(1, 2, 3, name="Alice", age=25)

print("\n  Order: regular params, *args, **kwargs")

print()  # Empty line


# ============================================================================
# 4. UNPACKING ARGUMENTS
# ============================================================================
print("=" * 60)
print("4. UNPACKING ARGUMENTS")
print("=" * 60)

def greet(name, age, city):
    """Greet with name, age, and city."""
    print(f"    {name}, {age}, lives in {city}")

# Unpack list/tuple as positional arguments
person_data = ["Alice", 25, "NYC"]
print("  Unpacking list as arguments:")
greet(*person_data)

# Unpack dictionary as keyword arguments
person_dict = {"name": "Bob", "age": 30, "city": "London"}
print("\n  Unpacking dict as keyword arguments:")
greet(**person_dict)

print()  # Empty line


# ============================================================================
# 5. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("5. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Flexible calculator
print("Example 1: Flexible Calculator")
def calculate(operation, *numbers):
    """Perform operation on numbers."""
    if operation == "add":
        return sum(numbers)
    elif operation == "multiply":
        result = 1
        for num in numbers:
            result *= num
        return result
    elif operation == "max":
        return max(numbers)
    elif operation == "min":
        return min(numbers)

print(f"  calculate('add', 1, 2, 3, 4): {calculate('add', 1, 2, 3, 4)}")
print(f"  calculate('multiply', 2, 3, 4): {calculate('multiply', 2, 3, 4)}")
print(f"  calculate('max', 10, 5, 20, 15): {calculate('max', 10, 5, 20, 15)}")

# Example 2: Create object with flexible attributes
print("\nExample 2: Flexible Object Creation")
def create_person(name, **attributes):
    """Create person with flexible attributes."""
    person = {"name": name}
    person.update(attributes)
    return person

person1 = create_person("Alice")
print(f"  create_person('Alice'): {person1}")

person2 = create_person("Bob", age=30, city="NYC", email="bob@example.com")
print(f"  create_person('Bob', ...): {person2}")

# Example 3: Wrapper function
print("\nExample 3: Wrapper Function")
def log_function_call(func, *args, **kwargs):
    """Log function call and execute."""
    print(f"    Calling {func.__name__} with args={args}, kwargs={kwargs}")
    result = func(*args, **kwargs)
    print(f"    Result: {result}")
    return result

def add(a, b):
    return a + b

result = log_function_call(add, 3, 5)

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("VARIABLE ARGUMENTS SUMMARY:")
print("=" * 60)
print("*args:")
print("  - Collects variable positional arguments")
print("  - Stored as tuple")
print("  - Allows function to accept any number of positional args")
print("\n**kwargs:")
print("  - Collects variable keyword arguments")
print("  - Stored as dictionary")
print("  - Allows function to accept any number of keyword args")
print("\nOrder:")
print("  - Regular parameters")
print("  - *args")
print("  - **kwargs")
print("\nUnpacking:")
print("  - *list unpacks as positional arguments")
print("  - **dict unpacks as keyword arguments")
print("=" * 60)

