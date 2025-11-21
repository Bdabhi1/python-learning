"""
Writing Test Cases

This file demonstrates how to write effective test cases.
"""

import unittest

# ============================================================================
# 1. BASIC TEST METHODS
# ============================================================================
print("=" * 60)
print("1. BASIC TEST METHODS")
print("=" * 60)

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('hello'.upper(), 'HELLO')
    
    def test_lower(self):
        self.assertEqual('HELLO'.lower(), 'hello')
    
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

print("  Each test method tests one specific behavior")

print()  # Empty line


# ============================================================================
# 2. TESTING FUNCTIONS
# ============================================================================
print("=" * 60)
print("2. TESTING FUNCTIONS")
print("=" * 60)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

class TestMathFunctions(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_add_negative(self):
        self.assertEqual(add(-2, -3), -5)
    
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

print("  Test functions with different inputs")

print()  # Empty line


# ============================================================================
# 3. TESTING EDGE CASES
# ============================================================================
print("=" * 60)
print("3. TESTING EDGE CASES")
print("=" * 60)

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

class TestEdgeCases(unittest.TestCase):
    def test_divide_normal(self):
        self.assertEqual(divide(10, 2), 5)
    
    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, divide, 10, 0)
    
    def test_divide_negative(self):
        self.assertEqual(divide(-10, 2), -5)

print("  Always test edge cases and error conditions")

print()  # Empty line


# ============================================================================
# 4. DESCRIPTIVE TEST NAMES
# ============================================================================
print("=" * 60)
print("4. DESCRIPTIVE TEST NAMES")
print("=" * 60)

class TestUserCreation(unittest.TestCase):
    def test_create_user_with_valid_data(self):
        # Test implementation
        pass
    
    def test_create_user_with_invalid_email(self):
        # Test implementation
        pass
    
    def test_create_user_with_empty_name(self):
        # Test implementation
        pass

print("  Use descriptive names that explain what is being tested")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("WRITING TESTS SUMMARY:")
print("=" * 60)
print("  - Test methods start with 'test_'")
print("  - Test one thing per method")
print("  - Test normal cases and edge cases")
print("  - Use descriptive test names")
print("  - Test error conditions")
print("=" * 60)

