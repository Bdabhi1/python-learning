# Decorators in Python

Decorators are a powerful Python feature that allows you to modify or extend the behavior of functions and methods without permanently modifying them. They provide a clean way to add functionality to existing code.

## Table of Contents
1. [What are Decorators?](#what-are-decorators)
2. [Function Decorators](#function-decorators)
3. [Decorator Syntax](#decorator-syntax)
4. [Decorators with Arguments](#decorators-with-arguments)
5. [Class Decorators](#class-decorators)
6. [Built-in Decorators](#built-in-decorators)
7. [Chaining Decorators](#chaining-decorators)
8. [Common Decorator Patterns](#common-decorator-patterns)
9. [Best Practices](#best-practices)

---

## What are Decorators?

**Decorators** are functions that modify other functions or classes. They wrap the original function, adding functionality before, after, or around it.

**Key concepts:**
- Decorators are functions that take functions as arguments
- They return modified functions
- Use `@decorator` syntax for convenience
- Decorators follow the decorator pattern

**Benefits:**
- **DRY (Don't Repeat Yourself)**: Reuse code across functions
- **Separation of Concerns**: Keep core logic separate from cross-cutting concerns
- **Clean Code**: Add functionality without cluttering function definitions

---

## Function Decorators

### Basic Decorator

```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call
```

### Decorator Without @ Syntax

```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

def say_hello():
    print("Hello!")

# Manual decoration
say_hello = my_decorator(say_hello)
say_hello()
```

---

## Decorator Syntax

The `@decorator` syntax is syntactic sugar for function decoration.

```python
@decorator
def my_function():
    pass

# Is equivalent to:
def my_function():
    pass
my_function = decorator(my_function)
```

### Preserving Function Metadata

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves function metadata
    def wrapper(*args, **kwargs):
        print("Decorator logic")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def my_function():
    """This is my function"""
    pass

print(my_function.__name__)  # 'my_function' (not 'wrapper')
print(my_function.__doc__)    # 'This is my function'
```

---

## Decorators with Arguments

### Decorator That Takes Arguments

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hello():
    print("Hello!")

say_hello()
# Output: Hello! (printed 3 times)
```

### Decorator Factory Pattern

```python
def timer(unit='seconds'):
    def decorator(func):
        import time
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            elapsed = end - start
            if unit == 'milliseconds':
                elapsed *= 1000
            print(f"{func.__name__} took {elapsed:.2f} {unit}")
            return result
        return wrapper
    return decorator

@timer(unit='milliseconds')
def slow_function():
    time.sleep(0.1)
```

---

## Class Decorators

Decorators can also be applied to classes.

### Basic Class Decorator

```python
def add_method(cls):
    def new_method(self):
        return "New method added!"
    cls.new_method = new_method
    return cls

@add_method
class MyClass:
    pass

obj = MyClass()
print(obj.new_method())  # "New method added!"
```

### Class-Based Decorator

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} called {self.count} times")
        return self.func(*args, **kwargs)

@CountCalls
def greet(name):
    return f"Hello, {name}!"

greet("Alice")
greet("Bob")
```

---

## Built-in Decorators

### `@property`

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

circle = Circle(5)
print(circle.radius)  # 5
circle.radius = 10
```

### `@staticmethod` and `@classmethod`

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def from_string(cls, value):
        return cls(int(value))

result = MathUtils.add(5, 3)  # 8
```

### `@functools.lru_cache`

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Results are cached
print(fibonacci(40))  # Fast (cached)
```

---

## Chaining Decorators

Multiple decorators can be applied to a single function.

```python
def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # <b><i>Hello, Alice!</i></b>
```

**Note:** Decorators are applied from bottom to top.

---

## Common Decorator Patterns

### Timing Decorator

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
```

### Logging Decorator

```python
def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b
```

### Retry Decorator

```python
import time
from functools import wraps

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3)
def unreliable_function():
    import random
    if random.random() < 0.5:
        raise ValueError("Random failure")
    return "Success!"
```

### Validation Decorator

```python
def validate_types(**types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Validate arguments
            for i, (arg, expected_type) in enumerate(zip(args, types.values())):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Argument {i} must be {expected_type}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(a=int, b=int)
def add(a, b):
    return a + b
```

---

## Best Practices

### 1. Use `@wraps` to Preserve Metadata

```python
from functools import wraps

def decorator(func):
    @wraps(func)  # Always use this!
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### 2. Handle Function Arguments Properly

```python
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):  # Accept any arguments
        return func(*args, **kwargs)
    return wrapper
```

### 3. Return Values from Decorated Functions

```python
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # Capture return value
        return result  # Return it
    return wrapper
```

### 4. Use Decorators for Cross-Cutting Concerns

```python
# Good: Logging, timing, caching
@timer
@log_calls
def my_function():
    pass

# Less preferred: Core business logic
@complex_business_logic
def my_function():
    pass
```

---

## Common Mistakes to Avoid

1. **Forgetting `@wraps`**
   ```python
   # Bad - loses function metadata
   def decorator(func):
       def wrapper():
           return func()
       return wrapper
   
   # Good - preserves metadata
   from functools import wraps
   def decorator(func):
       @wraps(func)
       def wrapper():
           return func()
       return wrapper
   ```

2. **Not handling arguments**
   ```python
   # Bad
   def decorator(func):
       def wrapper():  # No arguments!
           return func()
       return wrapper
   
   # Good
   def decorator(func):
       def wrapper(*args, **kwargs):
           return func(*args, **kwargs)
       return wrapper
   ```

3. **Not returning the result**
   ```python
   # Bad
   def decorator(func):
       def wrapper(*args, **kwargs):
           func(*args, **kwargs)  # No return!
       return wrapper
   ```

---

## Summary

- **Decorators** modify or extend function behavior
- Use `@decorator` syntax for convenience
- Always use `@wraps` to preserve function metadata
- Decorators can take arguments (decorator factories)
- Can be applied to functions and classes
- Chain multiple decorators for combined functionality
- Use for cross-cutting concerns (logging, timing, caching)

**Remember**: Decorators are a powerful tool for writing clean, reusable code. Use them to add functionality without modifying core logic!

---

## Next Steps

Now that you understand decorators:
1. Practice with the examples in this folder
2. Create your own decorators
3. Use built-in decorators like `@property` and `@lru_cache`
4. Move on to **20-context-managers** to learn about resource management

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_basic_decorators.py`: Understanding basic decorators - start here!
2. `02_decorator_syntax.py`: Using @ syntax and preserving metadata
3. `03_decorators_with_arguments.py`: Decorators that take parameters
4. `04_class_decorators.py`: Decorating classes and class-based decorators
5. `05_built_in_decorators.py`: Built-in decorators like @property, @staticmethod
6. `06_practical_examples.py`: Real-world decorator patterns and examples

Run these files in order to see decorators in action!

