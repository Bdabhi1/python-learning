"""
The unittest Module

This file demonstrates using Python's built-in unittest module.
"""

import unittest

# ============================================================================
# 1. BASIC TEST STRUCTURE
# ============================================================================
print("=" * 60)
print("1. BASIC TEST STRUCTURE")
print("=" * 60)

class TestMath(unittest.TestCase):
    def test_add(self):
        result = 2 + 2
        self.assertEqual(result, 4)

# Run test
if __name__ == '__main__':
    unittest.main()

print("\n  Test class must inherit from unittest.TestCase")
print("  Test methods must start with 'test_'")

print()  # Empty line


# ============================================================================
# 2. RUNNING TESTS
# ============================================================================
print("=" * 60)
print("2. RUNNING TESTS")
print("=" * 60)

print("  Ways to run tests:")
print("    python test_file.py                    # Run all tests")
print("    python -m unittest test_file           # Run module")
print("    python -m unittest -v test_file        # Verbose output")
print("    python -m unittest TestMath            # Run specific class")
print("    python -m unittest TestMath.test_add    # Run specific test")

print()  # Empty line


# ============================================================================
# 3. TEST CLASS EXAMPLE
# ============================================================================
print("=" * 60)
print("3. TEST CLASS EXAMPLE")
print("=" * 60)

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2 + 2, 4)
    
    def test_subtract(self):
        self.assertEqual(5 - 3, 2)
    
    def test_multiply(self):
        self.assertEqual(3 * 4, 12)
    
    def test_divide(self):
        self.assertEqual(10 / 2, 5)

print("  Test class with multiple test methods")
print("  Each method tests one aspect")

print()  # Empty line


# ============================================================================
# 4. TEST DISCOVERY
# ============================================================================
print("=" * 60)
print("4. TEST DISCOVERY")
print("=" * 60)

print("  Automatic test discovery:")
print("    python -m unittest discover              # Find all tests")
print("    python -m unittest discover -s tests     # In specific dir")
print("    python -m unittest discover -p 'test_*'  # With pattern")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("UNITTEST MODULE SUMMARY:")
print("=" * 60)
print("  - unittest.TestCase: Base class for tests")
print("  - Test methods start with 'test_'")
print("  - Run with unittest.main() or command line")
print("  - Can discover tests automatically")
print("=" * 60)

