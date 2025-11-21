"""
Test Fixtures

This file demonstrates using setUp, tearDown, and test fixtures.
"""

import unittest
import os

# ============================================================================
# 1. setUp AND tearDown
# ============================================================================
print("=" * 60)
print("1. setUp AND tearDown")
print("=" * 60)

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        # Run before each test
        self.test_file = 'test_file.txt'
        with open(self.test_file, 'w') as f:
            f.write('test content')
    
    def tearDown(self):
        # Run after each test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_read_file(self):
        with open(self.test_file, 'r') as f:
            content = f.read()
        self.assertEqual(content, 'test content')
    
    def test_file_exists(self):
        self.assertTrue(os.path.exists(self.test_file))

print("  setUp() runs before each test")
print("  tearDown() runs after each test")
print("  Ensures clean state for each test")

print()  # Empty line


# ============================================================================
# 2. setUpClass AND tearDownClass
# ============================================================================
print("=" * 60)
print("2. setUpClass AND tearDownClass")
print("=" * 60)

class TestExpensiveSetup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Run once before all tests
        print("  Setting up expensive resource (once)")
        cls.shared_data = "shared resource"
    
    @classmethod
    def tearDownClass(cls):
        # Run once after all tests
        print("  Cleaning up expensive resource (once)")
    
    def test_use_shared_data(self):
        self.assertEqual(self.shared_data, "shared resource")
    
    def test_use_shared_data_again(self):
        self.assertIsNotNone(self.shared_data)

print("  setUpClass() runs once before all tests")
print("  tearDownClass() runs once after all tests")
print("  Use for expensive setup operations")

print()  # Empty line


# ============================================================================
# 3. FIXTURE PATTERN
# ============================================================================
print("=" * 60)
print("3. FIXTURE PATTERN")
print("=" * 60)

class TestDatabase(unittest.TestCase):
    def setUp(self):
        # Simulate database connection
        self.db_connection = "connected"
        self.test_data = []
    
    def tearDown(self):
        # Clean up
        self.test_data.clear()
        self.db_connection = None
    
    def test_insert_data(self):
        self.test_data.append('item1')
        self.assertEqual(len(self.test_data), 1)
    
    def test_query_data(self):
        self.test_data.append('item1')
        self.assertIn('item1', self.test_data)

print("  Fixtures ensure consistent test environment")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("TEST FIXTURES SUMMARY:")
print("=" * 60)
print("  - setUp(): Run before each test")
print("  - tearDown(): Run after each test")
print("  - setUpClass(): Run once before all tests")
print("  - tearDownClass(): Run once after all tests")
print("  - Use for setup and cleanup")
print("=" * 60)

