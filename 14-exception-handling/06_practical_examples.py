"""
Practical Exception Handling Examples

This file demonstrates real-world examples of exception handling
for common programming scenarios.
"""

# ============================================================================
# 1. SAFE INPUT VALIDATION
# ============================================================================
print("=" * 60)
print("1. SAFE INPUT VALIDATION")
print("=" * 60)

def get_positive_number(prompt):
    """Get positive number from user safely."""
    while True:
        try:
            number = float(input(prompt))
            if number < 0:
                raise ValueError("Number must be positive")
            return number
        except ValueError as e:
            print(f"  Invalid input: {e}. Please try again.")

# Simulated example
print("  Simulated: get_positive_number('Enter number: ')")
print("  User enters: '5'")
result = 5.0  # Simulated
print(f"  Result: {result}")

print()  # Empty line


# ============================================================================
# 2. SAFE FILE OPERATIONS
# ============================================================================
print("=" * 60)
print("2. SAFE FILE OPERATIONS")
print("=" * 60)

def read_config_file(filename):
    """Read configuration file safely."""
    config = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line and "=" in line:
                    key, value = line.split("=", 1)
                    config[key] = value
        return config
    except FileNotFoundError:
        print(f"  Config file '{filename}' not found, using defaults")
        return {}
    except PermissionError:
        print(f"  Permission denied for '{filename}'")
        return {}
    except Exception as e:
        print(f"  Error reading config: {e}")
        return {}

# Test
config = read_config_file("nonexistent_config.txt")
print(f"  Config: {config}")

print()  # Empty line


# ============================================================================
# 3. SAFE DATA PROCESSING
# ============================================================================
print("=" * 60)
print("3. SAFE DATA PROCESSING")
print("=" * 60)

def process_numbers(numbers):
    """Process list of numbers safely."""
    results = {
        "sum": 0,
        "average": 0,
        "max": None,
        "min": None,
        "count": 0
    }
    
    try:
        if not numbers:
            raise ValueError("List is empty")
        
        # Convert to numbers
        numeric = []
        for item in numbers:
            try:
                numeric.append(float(item))
            except (ValueError, TypeError):
                continue  # Skip invalid items
        
        if not numeric:
            raise ValueError("No valid numbers found")
        
        results["sum"] = sum(numeric)
        results["count"] = len(numeric)
        results["average"] = results["sum"] / results["count"]
        results["max"] = max(numeric)
        results["min"] = min(numeric)
        
    except ValueError as e:
        print(f"  Error: {e}")
    
    return results

# Test
test_data = [1, 2, 3, "4", 5, "abc", 6]
result = process_numbers(test_data)
print(f"  Processed {test_data}:")
for key, value in result.items():
    print(f"    {key}: {value}")

print()  # Empty line


# ============================================================================
# 4. API REQUEST HANDLER
# ============================================================================
print("=" * 60)
print("4. API REQUEST HANDLER")
print("=" * 60)

def make_api_request(url):
    """Simulate API request with error handling."""
    # Simulated API call
    import random
    
    try:
        # Simulate network error
        if random.random() < 0.3:
            raise ConnectionError("Network connection failed")
        
        # Simulate invalid response
        if random.random() < 0.2:
            raise ValueError("Invalid response format")
        
        return {"status": "success", "data": "API response"}
    except ConnectionError as e:
        print(f"  ConnectionError: {e}")
        return {"status": "error", "message": str(e)}
    except ValueError as e:
        print(f"  ValueError: {e}")
        return {"status": "error", "message": str(e)}
    except Exception as e:
        print(f"  Unexpected error: {e}")
        return {"status": "error", "message": "Unknown error"}

# Test (simulated)
print("  Simulated API request:")
response = make_api_request("https://api.example.com")
print(f"  Response: {response}")

print()  # Empty line


# ============================================================================
# 5. DATABASE OPERATIONS
# ============================================================================
print("=" * 60)
print("5. DATABASE OPERATIONS")
print("=" * 60)

class DatabaseError(Exception):
    """Custom exception for database errors."""
    pass

def execute_query(query):
    """Simulate database query with error handling."""
    # Simulated database
    if "SELECT" not in query.upper():
        raise DatabaseError("Only SELECT queries allowed")
    
    if "users" in query.lower():
        return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    
    raise DatabaseError("Table not found")

# Test queries
queries = [
    "SELECT * FROM users",
    "DELETE FROM users",  # Should fail
    "SELECT * FROM products"  # Should fail
]

for query in queries:
    try:
        result = execute_query(query)
        print(f"  Query: '{query}'")
        print(f"  Result: {result}")
    except DatabaseError as e:
        print(f"  Query: '{query}'")
        print(f"  Error: {e}")

print()  # Empty line


# ============================================================================
# 6. VALIDATION WITH CUSTOM EXCEPTIONS
# ============================================================================
print("=" * 60)
print("6. VALIDATION WITH CUSTOM EXCEPTIONS")
print("=" * 60)

class ValidationError(Exception):
    """Custom exception for validation errors."""
    def __init__(self, message, field=None):
        self.message = message
        self.field = field
        super().__init__(f"{field}: {message}" if field else message)

def validate_user_data(username, email, age):
    """Validate user data with custom exceptions."""
    if not username or len(username) < 3:
        raise ValidationError("Must be at least 3 characters", "username")
    
    if "@" not in email:
        raise ValidationError("Invalid email format", "email")
    
    if not isinstance(age, int) or age < 0:
        raise ValidationError("Must be non-negative integer", "age")
    
    return True

# Test validation
test_cases = [
    ("alice", "alice@example.com", 25),
    ("ab", "alice@example.com", 25),
    ("alice", "invalid", 25),
    ("alice", "alice@example.com", -5),
]

for username, email, age in test_cases:
    try:
        validate_user_data(username, email, age)
        print(f"  Valid: {username}")
    except ValidationError as e:
        print(f"  Invalid: {e}")

print()  # Empty line


# ============================================================================
# 7. RETRY MECHANISM
# ============================================================================
print("=" * 60)
print("7. RETRY MECHANISM")
print("=" * 60)

def retry_operation(operation, max_attempts=3):
    """Retry operation with exception handling."""
    for attempt in range(1, max_attempts + 1):
        try:
            return operation()
        except Exception as e:
            if attempt == max_attempts:
                print(f"  Failed after {max_attempts} attempts: {e}")
                raise
            print(f"  Attempt {attempt} failed: {e}, retrying...")
    return None

# Simulated operation
def unreliable_operation():
    """Operation that might fail."""
    import random
    if random.random() < 0.7:
        raise ConnectionError("Connection failed")
    return "Success"

# Test retry
print("  Retrying unreliable operation:")
try:
    result = retry_operation(unreliable_operation, max_attempts=3)
    print(f"  Result: {result}")
except Exception as e:
    print(f"  Final error: {e}")

print()  # Empty line


# ============================================================================
# 8. CONTEXT MANAGER WITH EXCEPTIONS
# ============================================================================
print("=" * 60)
print("8. CONTEXT MANAGER WITH EXCEPTIONS")
print("=" * 60)

class SafeFileHandler:
    """Context manager for safe file operations."""
    def __init__(self, filename, mode="r"):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            return self.file
        except FileNotFoundError:
            print(f"  File '{self.filename}' not found")
            return None
        except PermissionError:
            print(f"  Permission denied for '{self.filename}'")
            return None
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False  # Don't suppress exceptions

# Use context manager
with SafeFileHandler("nonexistent.txt") as file:
    if file:
        content = file.read()
        print(f"  Content: {content}")

print()  # Empty line


# ============================================================================
# 9. ERROR LOGGING
# ============================================================================
print("=" * 60)
print("9. ERROR LOGGING")
print("=" * 60)

import traceback

def log_error(func):
    """Decorator to log errors."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"  Error in {func.__name__}: {e}")
            print("  Traceback:")
            traceback.print_exc()
            raise
    return wrapper

@log_error
def risky_function(x, y):
    """Function that might fail."""
    return x / y

# Test
try:
    result = risky_function(10, 0)
except ZeroDivisionError:
    print("  ZeroDivisionError handled")

print()  # Empty line


# ============================================================================
# 10. COMPREHENSIVE ERROR HANDLER
# ============================================================================
print("=" * 60)
print("10. COMPREHENSIVE ERROR HANDLER")
print("=" * 60)

def safe_execute(operation, *args, **kwargs):
    """Execute operation with comprehensive error handling."""
    try:
        return operation(*args, **kwargs)
    except ValueError as e:
        return {"success": False, "error": "Invalid value", "details": str(e)}
    except TypeError as e:
        return {"success": False, "error": "Wrong type", "details": str(e)}
    except ZeroDivisionError as e:
        return {"success": False, "error": "Division by zero", "details": str(e)}
    except FileNotFoundError as e:
        return {"success": False, "error": "File not found", "details": str(e)}
    except Exception as e:
        return {"success": False, "error": "Unknown error", "details": str(e)}

# Test with different operations
def divide(a, b):
    return a / b

def read_file(filename):
    with open(filename, "r") as f:
        return f.read()

results = [
    safe_execute(divide, 10, 2),
    safe_execute(divide, 10, 0),
    safe_execute(read_file, "nonexistent.txt"),
]

for i, result in enumerate(results, 1):
    print(f"  Operation {i}: {result}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL EXCEPTION HANDLING SUMMARY:")
print("=" * 60)
print("Key Applications:")
print("  - Input validation: Validate user input")
print("  - File operations: Handle file errors")
print("  - Data processing: Handle invalid data")
print("  - API requests: Handle network errors")
print("  - Database operations: Handle DB errors")
print("  - Retry mechanisms: Retry failed operations")
print("  - Error logging: Log exceptions for debugging")
print("\nRemember:")
print("  - Always handle exceptions appropriately")
print("  - Provide helpful error messages")
print("  - Use specific exception types")
print("  - Log errors for debugging")
print("  - Create custom exceptions when needed")
print("=" * 60)

