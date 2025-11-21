# Testing and Debugging in Python

Testing and debugging are essential skills for writing reliable Python code. Python provides built-in testing tools like `unittest` and third-party libraries like `pytest` for comprehensive testing.

## Table of Contents
1. [What is Testing?](#what-is-testing)
2. [The `unittest` Module](#the-unittest-module)
3. [Writing Test Cases](#writing-test-cases)
4. [Test Fixtures](#test-fixtures)
5. [Assertions](#assertions)
6. [Test Discovery](#test-discovery)
7. [Debugging Techniques](#debugging-techniques)
8. [Best Practices](#best-practices)

---

## What is Testing?

**Testing** is the process of verifying that your code works correctly:
- **Unit tests**: Test individual functions/methods
- **Integration tests**: Test how components work together
- **System tests**: Test the entire system

**Benefits of Testing:**
- **Catch bugs early**: Find issues before deployment
- **Documentation**: Tests show how code should work
- **Refactoring confidence**: Change code knowing tests will catch breaks
- **Regression prevention**: Ensure new changes don't break existing features

**Testing Pyramid:**
- Many unit tests (fast, isolated)
- Some integration tests (moderate speed)
- Few system tests (slow, comprehensive)

---

## The `unittest` Module

Python's built-in `unittest` module provides a testing framework.

### Basic Test Structure

```python
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2 + 2, 4)

if __name__ == '__main__':
    unittest.main()
```

### Running Tests

```bash
# Run all tests in file
python test_file.py

# Run with verbose output
python -m unittest -v test_file.py

# Run specific test class
python -m unittest TestMath

# Run specific test method
python -m unittest TestMath.test_add
```

---

## Writing Test Cases

### Test Class

```python
import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = 2 + 2
        self.assertEqual(result, 4)
    
    def test_subtract(self):
        result = 5 - 3
        self.assertEqual(result, 2)
    
    def test_multiply(self):
        result = 3 * 4
        self.assertEqual(result, 12)
```

### Test Methods

Test methods must:
- Start with `test_`
- Be methods of a class that inherits from `unittest.TestCase`
- Use assertions to verify results

```python
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('hello'.upper(), 'HELLO')
    
    def test_isupper(self):
        self.assertTrue('HELLO'.isupper())
        self.assertFalse('Hello'.isupper())
```

---

## Test Fixtures

Fixtures set up and tear down test environment.

### setUp and tearDown

```python
import unittest

class TestDatabase(unittest.TestCase):
    def setUp(self):
        # Run before each test
        self.db = connect_to_database()
    
    def tearDown(self):
        # Run after each test
        self.db.close()
    
    def test_query(self):
        result = self.db.query("SELECT * FROM users")
        self.assertIsNotNone(result)
```

### setUpClass and tearDownClass

```python
import unittest

class TestExpensiveSetup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Run once before all tests
        cls.shared_resource = expensive_setup()
    
    @classmethod
    def tearDownClass(cls):
        # Run once after all tests
        cleanup(cls.shared_resource)
```

---

## Assertions

`unittest` provides many assertion methods.

### Common Assertions

```python
import unittest

class TestAssertions(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(2 + 2, 4)
        self.assertNotEqual(2 + 2, 5)
    
    def test_truthiness(self):
        self.assertTrue(True)
        self.assertFalse(False)
    
    def test_none(self):
        self.assertIsNone(None)
        self.assertIsNotNone(42)
    
    def test_in(self):
        self.assertIn(2, [1, 2, 3])
        self.assertNotIn(4, [1, 2, 3])
    
    def test_type(self):
        self.assertIsInstance(42, int)
        self.assertIsInstance('hello', str)
```

### Assertion Methods

- `assertEqual(a, b)`: a == b
- `assertNotEqual(a, b)`: a != b
- `assertTrue(x)`: bool(x) is True
- `assertFalse(x)`: bool(x) is False
- `assertIsNone(x)`: x is None
- `assertIsNotNone(x)`: x is not None
- `assertIn(a, b)`: a in b
- `assertNotIn(a, b)`: a not in b
- `assertIsInstance(a, b)`: isinstance(a, b)
- `assertRaises(exception, callable, *args)`: callable raises exception

---

## Test Discovery

`unittest` can automatically discover and run tests.

### Automatic Discovery

```bash
# Discover and run all tests
python -m unittest discover

# Discover tests in specific directory
python -m unittest discover -s tests

# Discover with pattern
python -m unittest discover -p "test_*.py"
```

### Test File Naming

- Test files should start with `test_`
- Test classes should start with `Test`
- Test methods should start with `test_`

---

## Debugging Techniques

### Print Debugging

```python
def calculate_total(items):
    total = 0
    print(f"Starting with total: {total}")  # Debug print
    for item in items:
        print(f"Processing item: {item}")  # Debug print
        total += item['price']
        print(f"New total: {total}")  # Debug print
    return total
```

### Using `pdb` Debugger

```python
import pdb

def calculate_total(items):
    total = 0
    pdb.set_trace()  # Breakpoint
    for item in items:
        total += item['price']
    return total
```

### Debugger Commands

- `n` (next): Execute next line
- `s` (step): Step into function
- `c` (continue): Continue execution
- `l` (list): Show current code
- `p variable`: Print variable value
- `q` (quit): Quit debugger

---

## Best Practices

### 1. Write Tests First (TDD)

```python
# Write test first
def test_add():
    assert add(2, 3) == 5

# Then write implementation
def add(a, b):
    return a + b
```

### 2. Test One Thing at a Time

```python
# Good - one assertion per concept
def test_user_creation(self):
    user = create_user('Alice')
    self.assertEqual(user.name, 'Alice')
    self.assertIsNotNone(user.id)

# Less preferred - too many things
def test_everything(self):
    # Tests multiple unrelated things
    pass
```

### 3. Use Descriptive Test Names

```python
# Good
def test_add_positive_numbers(self):
    pass

# Less descriptive
def test_add(self):
    pass
```

### 4. Keep Tests Independent

```python
# Each test should work independently
# Don't rely on order of test execution
```

### 5. Test Edge Cases

```python
def test_divide(self):
    self.assertEqual(divide(10, 2), 5)
    self.assertRaises(ZeroDivisionError, divide, 10, 0)  # Edge case
```

---

## Common Mistakes to Avoid

1. **Not testing edge cases**
   ```python
   # Wrong - only tests happy path
   def test_divide(self):
       self.assertEqual(divide(10, 2), 5)
   
   # Correct - tests edge cases
   def test_divide(self):
       self.assertEqual(divide(10, 2), 5)
       self.assertRaises(ZeroDivisionError, divide, 10, 0)
   ```

2. **Tests that depend on each other**
   ```python
   # Wrong - tests depend on order
   def test_create_user(self):
       self.user = create_user('Alice')
   
   def test_get_user(self):
       user = get_user(self.user.id)  # Depends on previous test
   ```

3. **Not cleaning up after tests**
   ```python
   # Wrong - leaves test data
   def test_create_file(self):
       create_file('test.txt')
   
   # Correct - cleans up
   def tearDown(self):
       if os.path.exists('test.txt'):
           os.remove('test.txt')
   ```

---

## Summary

- **Testing** verifies code works correctly
- Use `unittest` for built-in testing
- Write **test cases** as classes inheriting from `TestCase`
- Use **assertions** to verify results
- Use **fixtures** (setUp/tearDown) for test environment
- **Debug** using print statements or `pdb`
- Write **independent tests** that cover edge cases

**Remember**: Good tests give you confidence to refactor and add features!

---

## Next Steps

Now that you understand testing and debugging:
1. Practice with the examples in this folder
2. Write tests for your own code
3. Learn about `pytest` for more advanced testing
4. Move on to **30-debugging-and-logging** to learn about logging

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_testing_basics.py`: Understanding testing concepts
2. `02_unittest_module.py`: Using the unittest module
3. `03_writing_tests.py`: Writing test cases and test methods
4. `04_test_fixtures.py`: Using setUp, tearDown, and fixtures
5. `05_assertions.py`: Using different assertion methods
6. `06_practical_examples.py`: Real-world testing and debugging examples

Run these files in order to see testing and debugging in action!

