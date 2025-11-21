"""
Practical Testing and Debugging Examples

This file demonstrates real-world testing and debugging scenarios.
"""

import unittest

# ============================================================================
# 1. TESTING A CALCULATOR CLASS
# ============================================================================
print("=" * 60)
print("1. TESTING A CALCULATOR CLASS")
print("=" * 60)

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertRaises(ZeroDivisionError, self.calc.divide, 10, 0)

print("  Complete test suite for Calculator class")

print()  # Empty line


# ============================================================================
# 2. DEBUGGING WITH PRINT
# ============================================================================
print("=" * 60)
print("2. DEBUGGING WITH PRINT")
print("=" * 60)

def calculate_total(items):
    total = 0
    print(f"  DEBUG: Starting with total: {total}")
    for item in items:
        print(f"  DEBUG: Processing item: {item}")
        total += item
        print(f"  DEBUG: New total: {total}")
    return total

result = calculate_total([10, 20, 30])
print(f"  Final result: {result}")

print("\n  Print statements help track execution flow")

print()  # Empty line


# ============================================================================
# 3. USING PDB DEBUGGER
# ============================================================================
print("=" * 60)
print("3. USING PDB DEBUGGER")
print("=" * 60)

print("  Use pdb for interactive debugging:")
print("    import pdb")
print("    ")
print("    def function():")
print("        pdb.set_trace()  # Breakpoint")
print("        # Code here")
print("  ")
print("  Debugger commands:")
print("    n (next): Execute next line")
print("    s (step): Step into function")
print("    c (continue): Continue execution")
print("    l (list): Show current code")
print("    p variable: Print variable value")
print("    q (quit): Quit debugger")

print()  # Empty line


# ============================================================================
# 4. TESTING WITH MOCK DATA
# ============================================================================
print("=" * 60)
print("4. TESTING WITH MOCK DATA")
print("=" * 60)

class TestWithMockData(unittest.TestCase):
    def test_process_users(self):
        # Mock user data
        users = [
            {'id': 1, 'name': 'Alice', 'age': 30},
            {'id': 2, 'name': 'Bob', 'age': 25}
        ]
        
        # Test processing
        names = [user['name'] for user in users]
        self.assertEqual(names, ['Alice', 'Bob'])

print("  Use mock data to test without external dependencies")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL EXAMPLES SUMMARY:")
print("=" * 60)
print("Testing and debugging techniques:")
print("  - Write comprehensive test suites")
print("  - Use print statements for simple debugging")
print("  - Use pdb for interactive debugging")
print("  - Test with mock data")
print("  - Test edge cases and error conditions")
print("=" * 60)

