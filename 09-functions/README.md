# Functions in Python

Functions are reusable blocks of code that perform specific tasks. They help organize code, avoid repetition, and make programs easier to understand and maintain.

## Table of Contents
1. [What are Functions?](#what-are-functions)
2. [Defining Functions](#defining-functions)
3. [Function Parameters](#function-parameters)
4. [Return Values](#return-values)
5. [Default Parameters](#default-parameters)
6. [Keyword Arguments](#keyword-arguments)
7. [Variable Arguments](#variable-arguments)
8. [Scope and Functions](#scope-and-functions)
9. [Best Practices](#best-practices)

---

## What are Functions?

**Functions** are named blocks of code that perform a specific task. They:
- Take input (parameters)
- Perform operations
- Return output (optional)
- Can be called multiple times

**Benefits:**
- **Reusability**: Write once, use many times
- **Modularity**: Break code into logical pieces
- **Readability**: Code is easier to understand
- **Maintainability**: Easier to fix and update

---

## Defining Functions

Use the `def` keyword to define a function.

### Basic Function

```python
def greet():
    print("Hello, World!")

# Call the function
greet()  # Output: Hello, World!
```

### Function with Parameters

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
```

### Function with Return Value

```python
def add(a, b):
    return a + b

result = add(3, 5)  # result = 8
```

---

## Function Parameters

Parameters are variables that receive values when the function is called.

### Positional Parameters

```python
def greet(name, age):
    print(f"{name} is {age} years old")

greet("Alice", 25)  # Position matters
```

### Default Parameters

```python
def greet(name, age=18):
    print(f"{name} is {age} years old")

greet("Alice")      # Uses default age=18
greet("Bob", 30)    # Overrides default
```

### Keyword Arguments

```python
def greet(name, age, city):
    print(f"{name}, {age}, lives in {city}")

greet(name="Alice", age=25, city="NYC")
greet(city="NYC", name="Alice", age=25)  # Order doesn't matter
```

---

## Return Values

Functions can return values using the `return` statement.

### Single Return Value

```python
def square(x):
    return x * x

result = square(5)  # result = 25
```

### Multiple Return Values

```python
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide(17, 5)  # q = 3, r = 2
```

### No Return Value

```python
def print_message(msg):
    print(msg)
    # No return statement (returns None)

result = print_message("Hello")  # result = None
```

---

## Default Parameters

Provide default values for parameters.

```python
def power(x, n=2):
    return x ** n

power(5)      # 25 (uses default n=2)
power(5, 3)   # 125 (overrides default)
```

**Important:** Default parameters are evaluated once when the function is defined, not each time it's called.

---

## Variable Arguments

### `*args` - Variable Positional Arguments

```python
def sum_all(*args):
    return sum(args)

sum_all(1, 2, 3)        # 6
sum_all(1, 2, 3, 4, 5)  # 15
```

### `**kwargs` - Variable Keyword Arguments

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
```

---

## Scope and Functions

Variables defined inside functions are local to that function.

```python
x = 10  # Global variable

def my_function():
    x = 5  # Local variable
    print(x)  # 5

my_function()
print(x)  # 10 (global unchanged)
```

**See folder 03-variables-and-scope for detailed information.**

---

## Best Practices

1. **Use descriptive function names**
   ```python
   # Good
   def calculate_total_price(items):
       pass
   
   # Bad
   def calc(items):
       pass
   ```

2. **Keep functions focused**
   ```python
   # Good - does one thing
   def calculate_area(length, width):
       return length * width
   
   # Less preferred - does multiple things
   def process_data_and_save():
       pass
   ```

3. **Use docstrings**
   ```python
   def add(a, b):
       """Add two numbers and return the result."""
       return a + b
   ```

4. **Return early for clarity**
   ```python
   def is_positive(n):
       if n <= 0:
           return False
       return True
   ```

---

## Common Mistakes to Avoid

1. **Forgetting return statement**
   ```python
   # Wrong
   def add(a, b):
       a + b  # No return!
   
   # Correct
   def add(a, b):
       return a + b
   ```

2. **Modifying mutable defaults**
   ```python
   # Problematic
   def add_item(item, items=[]):
       items.append(item)
       return items
   
   # Better
   def add_item(item, items=None):
       if items is None:
           items = []
       items.append(item)
       return items
   ```

3. **Using global variables unnecessarily**
   ```python
   # Less preferred
   counter = 0
   def increment():
       global counter
       counter += 1
   
   # Better
   def increment(counter):
       return counter + 1
   ```

---

## Summary

- **Functions** are reusable blocks of code
- Use `def` to define functions
- **Parameters** receive input values
- Use `return` to send output back
- **Default parameters** provide fallback values
- `*args` and `**kwargs` handle variable arguments
- Functions have their own **local scope**
- Use **descriptive names** and **docstrings**

**Remember**: Functions are the building blocks of well-organized Python programs. Master them to write clean, reusable code!

---

## Next Steps

Now that you understand functions:
1. Practice with the examples in this folder
2. Create your own functions
3. Learn about function decorators (advanced)
4. Move on to **10-string-manipulation** to learn string operations

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_basic_functions.py`: Defining and calling functions - start here!
2. `02_parameters_arguments.py`: Function parameters and arguments
3. `03_return_values.py`: Returning values from functions
4. `04_default_parameters.py`: Default parameter values
5. `05_variable_arguments.py`: *args and **kwargs
6. `06_practical_examples.py`: Real-world function examples

Run these files in order to see functions in action!

