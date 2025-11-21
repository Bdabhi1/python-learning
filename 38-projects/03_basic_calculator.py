"""
Basic Calculator Project

This file demonstrates a simple calculator implementation.
"""

# ============================================================================
# 1. CALCULATOR CLASS
# ============================================================================
print("=" * 60)
print("1. CALCULATOR CLASS")
print("=" * 60)

class Calculator:
    """Simple calculator class"""
    
    def add(self, a, b):
        """Add two numbers"""
        return a + b
    
    def subtract(self, a, b):
        """Subtract b from a"""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        return a * b
    
    def divide(self, a, b):
        """Divide a by b"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

calc = Calculator()
print(f"  10 + 5 = {calc.add(10, 5)}")
print(f"  10 - 5 = {calc.subtract(10, 5)}")
print(f"  10 * 5 = {calc.multiply(10, 5)}")
print(f"  10 / 5 = {calc.divide(10, 5)}")

print()  # Empty line


# ============================================================================
# 2. CALCULATOR WITH OPERATIONS DICT
# ============================================================================
print("=" * 60)
print("2. CALCULATOR WITH OPERATIONS DICT")
print("=" * 60)

class Calculator:
    """Calculator with operation mapping"""
    
    def __init__(self):
        self.operations = {
            '+': self._add,
            '-': self._subtract,
            '*': self._multiply,
            '/': self._divide
        }
    
    def _add(self, a, b):
        return a + b
    
    def _subtract(self, a, b):
        return a - b
    
    def _multiply(self, a, b):
        return a * b
    
    def _divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def calculate(self, a, operator, b):
        """Calculate result based on operator"""
        if operator not in self.operations:
            raise ValueError(f"Unknown operator: {operator}")
        return self.operations[operator](a, b)

calc = Calculator()
print(f"  10 + 5 = {calc.calculate(10, '+', 5)}")
print(f"  10 * 5 = {calc.calculate(10, '*', 5)}")

print()  # Empty line


# ============================================================================
# 3. COMMAND-LINE INTERFACE
# ============================================================================
print("=" * 60)
print("3. COMMAND-LINE INTERFACE")
print("=" * 60)

def calculator_cli():
    """Simple CLI calculator"""
    calc = Calculator()
    
    print("  Calculator CLI (example):")
    print("    Enter: number1 operator number2")
    print("    Example: 10 + 5")
    print("    ")
    print("    (This is a demonstration)")
    print("    In real implementation:")
    print("      while True:")
    print("          user_input = input('> ')")
    print("          # Parse and calculate")
    print("          # Display result")

calculator_cli()

print()  # Empty line


# ============================================================================
# 4. ERROR HANDLING
# ============================================================================
print("=" * 60)
print("4. ERROR HANDLING")
print("=" * 60)

def safe_calculate(calc, a, operator, b):
    """Calculate with error handling"""
    try:
        result = calc.calculate(a, operator, b)
        return result
    except ValueError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"

calc = Calculator()
print(f"  10 / 0 = {safe_calculate(calc, 10, '/', 0)}")
print(f"  10 ? 5 = {safe_calculate(calc, 10, '?', 5)}")

print()  # Empty line


# ============================================================================
# 5. EXTENDING CALCULATOR
# ============================================================================
print("=" * 60)
print("5. EXTENDING CALCULATOR")
print("=" * 60)

class AdvancedCalculator(Calculator):
    """Extended calculator with more operations"""
    
    def __init__(self):
        super().__init__()
        self.operations.update({
            '**': self._power,
            '%': self._modulo
        })
    
    def _power(self, a, b):
        """Raise a to power of b"""
        return a ** b
    
    def _modulo(self, a, b):
        """Modulo operation"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a % b

adv_calc = AdvancedCalculator()
print(f"  2 ** 3 = {adv_calc.calculate(2, '**', 3)}")
print(f"  10 % 3 = {adv_calc.calculate(10, '%', 3)}")

print()  # Empty line


# ============================================================================
# 6. CALCULATOR WITH HISTORY
# ============================================================================
print("=" * 60)
print("6. CALCULATOR WITH HISTORY")
print("=" * 60)

class CalculatorWithHistory(Calculator):
    """Calculator that remembers calculations"""
    
    def __init__(self):
        super().__init__()
        self.history = []
    
    def calculate(self, a, operator, b):
        """Calculate and store in history"""
        result = super().calculate(a, operator, b)
        self.history.append(f"{a} {operator} {b} = {result}")
        return result
    
    def get_history(self):
        """Get calculation history"""
        return self.history
    
    def clear_history(self):
        """Clear calculation history"""
        self.history.clear()

hist_calc = CalculatorWithHistory()
hist_calc.calculate(10, '+', 5)
hist_calc.calculate(20, '*', 3)
print("  History:")
for entry in hist_calc.get_history():
    print(f"    {entry}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("BASIC CALCULATOR SUMMARY:")
print("=" * 60)
print("Key Features:")
print("  - Basic arithmetic operations")
print("  - Error handling for division by zero")
print("  - Extensible design")
print("  - Operation mapping")
print("  - History tracking")
print("  - CLI interface")
print("=" * 60)

