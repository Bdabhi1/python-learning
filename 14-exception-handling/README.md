# Exception Handling in Python

Exception handling allows your programs to gracefully handle errors and unexpected situations. Understanding how to catch, handle, and raise exceptions is crucial for writing robust Python programs.

## Table of Contents
1. [What are Exceptions?](#what-are-exceptions)
2. [Try-Except Blocks](#try-except-blocks)
3. [Handling Specific Exceptions](#handling-specific-exceptions)
4. [Multiple Exception Handlers](#multiple-exception-handlers)
5. [Else and Finally Clauses](#else-and-finally-clauses)
6. [Raising Exceptions](#raising-exceptions)
7. [Custom Exceptions](#custom-exceptions)
8. [Best Practices](#best-practices)

---

## What are Exceptions?

**Exceptions** are errors that occur during program execution. When an exception occurs, Python stops normal execution and looks for an exception handler.

**Key concepts:**
- Exceptions are objects representing errors
- Unhandled exceptions crash your program
- Use try-except to handle exceptions gracefully
- Python has many built-in exception types

**Common exceptions:**
- `ValueError` - Invalid value
- `TypeError` - Wrong type
- `IndexError` - Index out of range
- `KeyError` - Dictionary key not found
- `FileNotFoundError` - File doesn't exist
- `ZeroDivisionError` - Division by zero

**Example:**
```python
# This raises an exception
result = 10 / 0  # ZeroDivisionError

# Handle it
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

---

## Try-Except Blocks

The `try-except` block allows you to catch and handle exceptions.

### Basic Syntax

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle the exception
    print("Division by zero!")
```

### Catching All Exceptions

```python
try:
    # Risky code
    result = int("abc")
except Exception as e:
    # Catch any exception
    print(f"An error occurred: {e}")
```

**Note:** Catching all exceptions with `except Exception` is generally discouraged. Catch specific exceptions when possible.

---

## Handling Specific Exceptions

Handle specific exception types for better error handling.

### Single Exception

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter a number.")
```

### Multiple Specific Exceptions

```python
try:
    result = 10 / int(input("Enter divisor: "))
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

---

## Multiple Exception Handlers

You can have multiple `except` clauses to handle different exceptions.

```python
try:
    # Code that might raise different exceptions
    file = open("data.txt", "r")
    number = int(file.read())
    result = 10 / number
except FileNotFoundError:
    print("File not found!")
except ValueError:
    print("Invalid number in file!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### Catching Multiple Exceptions in One Handler

```python
try:
    # Risky code
    pass
except (ValueError, TypeError) as e:
    print(f"Value or type error: {e}")
```

---

## Else and Finally Clauses

### Else Clause

The `else` clause runs if no exception occurs:

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero!")
else:
    print(f"Result: {result}")  # Only runs if no exception
```

### Finally Clause

The `finally` clause always runs, regardless of exceptions:

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    # Always runs, even if exception occurs
    file.close()  # Ensure file is closed
```

**Note:** The `finally` clause is perfect for cleanup operations.

---

## Raising Exceptions

You can raise exceptions using the `raise` statement.

### Basic Raise

```python
if age < 0:
    raise ValueError("Age cannot be negative")
```

### Re-raising Exceptions

```python
try:
    # Some code
    pass
except ValueError:
    print("Handling error...")
    raise  # Re-raise the same exception
```

### Raising with Custom Message

```python
raise ValueError("Invalid input: expected number, got string")
```

---

## Custom Exceptions

Create your own exception classes for specific errors.

### Simple Custom Exception

```python
class CustomError(Exception):
    pass

# Use it
raise CustomError("Something went wrong!")
```

### Custom Exception with Attributes

```python
class ValidationError(Exception):
    def __init__(self, message, field):
        self.message = message
        self.field = field
        super().__init__(f"{field}: {message}")

# Use it
raise ValidationError("Invalid value", "email")
```

---

## Common Built-in Exceptions

Python provides many built-in exceptions:

### ValueError

```python
try:
    int("abc")  # Raises ValueError
except ValueError:
    print("Invalid value!")
```

### TypeError

```python
try:
    "hello" + 5  # Raises TypeError
except TypeError:
    print("Wrong type!")
```

### IndexError

```python
try:
    items = [1, 2, 3]
    print(items[10])  # Raises IndexError
except IndexError:
    print("Index out of range!")
```

### KeyError

```python
try:
    data = {"name": "Alice"}
    print(data["age"])  # Raises KeyError
except KeyError:
    print("Key not found!")
```

### AttributeError

```python
try:
    obj = "hello"
    obj.nonexistent_method()  # Raises AttributeError
except AttributeError:
    print("Attribute not found!")
```

---

## Best Practices

### 1. Be Specific

```python
# Good
try:
    result = int(input("Enter number: "))
except ValueError:
    print("Invalid number!")

# Less preferred
try:
    result = int(input("Enter number: "))
except Exception:
    print("Error!")
```

### 2. Don't Suppress Exceptions

```python
# Bad
try:
    risky_operation()
except:
    pass  # Hides the error!

# Good
try:
    risky_operation()
except SpecificError as e:
    logger.error(f"Error: {e}")
    # Handle appropriately
```

### 3. Use Finally for Cleanup

```python
try:
    file = open("data.txt", "r")
    # Process file
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()  # Always close
```

### 4. Provide Helpful Error Messages

```python
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Invalid input! Please enter a valid number.")
```

### 5. Log Exceptions

```python
import logging

try:
    risky_operation()
except Exception as e:
    logging.error(f"Error occurred: {e}", exc_info=True)
```

---

## Common Mistakes to Avoid

1. **Catching too broad exceptions**
   ```python
   # Bad
   try:
       # code
   except:  # Catches everything, even system exits!
       pass
   
   # Good
   try:
       # code
   except ValueError:
       # Handle specific error
       pass
   ```

2. **Ignoring exceptions**
   ```python
   # Bad
   try:
       risky_operation()
   except:
       pass  # Error is hidden!
   ```

3. **Not handling exceptions at all**
   ```python
   # Bad - program crashes
   result = 10 / 0
   
   # Good
   try:
       result = 10 / 0
   except ZeroDivisionError:
       result = 0
   ```

4. **Using exceptions for control flow**
   ```python
   # Bad
   try:
       value = my_dict["key"]
   except KeyError:
       value = None
   
   # Good
   value = my_dict.get("key", None)
   ```

---

## Summary

- **Exceptions** are errors that occur during execution
- Use **try-except** blocks to handle exceptions
- Handle **specific exceptions** when possible
- Use **else** for code that runs when no exception occurs
- Use **finally** for cleanup operations
- **Raise exceptions** when validation fails
- Create **custom exceptions** for domain-specific errors
- Follow **best practices** for robust error handling

**Remember**: Exception handling makes your programs robust and user-friendly. Master these techniques to write production-quality code!

---

## Next Steps

Now that you understand exception handling:
1. Practice with the examples in this folder
2. Add error handling to your programs
3. Create custom exceptions for your applications
4. Move on to **15-collections-module** to learn about advanced data structures

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_basic_exceptions.py`: Understanding exceptions and try-except - start here!
2. `02_handling_exceptions.py`: Handling different types of exceptions
3. `03_multiple_exceptions.py`: Handling multiple exceptions
4. `04_else_finally.py`: Using else and finally clauses
5. `05_raising_exceptions.py`: Raising and re-raising exceptions
6. `06_practical_examples.py`: Real-world exception handling examples

Run these files in order to see exception handling in action!

