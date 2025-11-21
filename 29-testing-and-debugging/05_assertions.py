"""
Assertions in unittest

This file demonstrates different assertion methods available in unittest.
"""

import unittest

# ============================================================================
# 1. EQUALITY ASSERTIONS
# ============================================================================
print("=" * 60)
print("1. EQUALITY ASSERTIONS")
print("=" * 60)

class TestEquality(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(2 + 2, 4)
        self.assertEqual('hello', 'hello')
    
    def test_not_equal(self):
        self.assertNotEqual(2 + 2, 5)
        self.assertNotEqual('hello', 'world')

print("  assertEqual(a, b): Check if a == b")
print("  assertNotEqual(a, b): Check if a != b")

print()  # Empty line


# ============================================================================
# 2. TRUTHINESS ASSERTIONS
# ============================================================================
print("=" * 60)
print("2. TRUTHINESS ASSERTIONS")
print("=" * 60)

class TestTruthiness(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)
        self.assertTrue(1)
        self.assertTrue([1, 2, 3])
    
    def test_false(self):
        self.assertFalse(False)
        self.assertFalse(0)
        self.assertFalse([])

print("  assertTrue(x): Check if x is truthy")
print("  assertFalse(x): Check if x is falsy")

print()  # Empty line


# ============================================================================
# 3. NONE ASSERTIONS
# ============================================================================
print("=" * 60)
print("3. NONE ASSERTIONS")
print("=" * 60)

class TestNone(unittest.TestCase):
    def test_is_none(self):
        self.assertIsNone(None)
        value = None
        self.assertIsNone(value)
    
    def test_is_not_none(self):
        self.assertIsNotNone(42)
        self.assertIsNotNone('hello')

print("  assertIsNone(x): Check if x is None")
print("  assertIsNotNone(x): Check if x is not None")

print()  # Empty line


# ============================================================================
# 4. MEMBERSHIP ASSERTIONS
# ============================================================================
print("=" * 60)
print("4. MEMBERSHIP ASSERTIONS")
print("=" * 60)

class TestMembership(unittest.TestCase):
    def test_in(self):
        self.assertIn(2, [1, 2, 3])
        self.assertIn('a', 'hello')
    
    def test_not_in(self):
        self.assertNotIn(4, [1, 2, 3])
        self.assertNotIn('z', 'hello')

print("  assertIn(a, b): Check if a in b")
print("  assertNotIn(a, b): Check if a not in b")

print()  # Empty line


# ============================================================================
# 5. TYPE ASSERTIONS
# ============================================================================
print("=" * 60)
print("5. TYPE ASSERTIONS")
print("=" * 60)

class TestType(unittest.TestCase):
    def test_is_instance(self):
        self.assertIsInstance(42, int)
        self.assertIsInstance('hello', str)
        self.assertIsInstance([1, 2], list)

print("  assertIsInstance(obj, cls): Check if obj is instance of cls")

print()  # Empty line


# ============================================================================
# 6. EXCEPTION ASSERTIONS
# ============================================================================
print("=" * 60)
print("6. EXCEPTION ASSERTIONS")
print("=" * 60)

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

class TestExceptions(unittest.TestCase):
    def test_raises_exception(self):
        self.assertRaises(ZeroDivisionError, divide, 10, 0)
    
    def test_raises_with_context(self):
        with self.assertRaises(ValueError):
            int('not a number')

print("  assertRaises(exception, callable, *args): Check if exception raised")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("ASSERTIONS SUMMARY:")
print("=" * 60)
print("  - assertEqual/assertNotEqual: Equality checks")
print("  - assertTrue/assertFalse: Truthiness checks")
print("  - assertIsNone/assertIsNotNone: None checks")
print("  - assertIn/assertNotIn: Membership checks")
print("  - assertIsInstance: Type checks")
print("  - assertRaises: Exception checks")
print("=" * 60)

