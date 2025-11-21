"""
Practical Best Practices Examples

This file demonstrates real-world best practices scenarios.
"""

# ============================================================================
# 1. CLEAN FUNCTION DESIGN
# ============================================================================
print("=" * 60)
print("1. CLEAN FUNCTION DESIGN")
print("=" * 60)

print("  Good function design:")
print("    ")
print("    def calculate_discount(price: float, discount_percent: float) -> float:")
print("        \"\"\"")
print("        Calculate discounted price.")
print("        ")
print("        Args:")
print("            price: Original price")
print("            discount_percent: Discount percentage (0-100)")
print("        ")
print("        Returns:")
print("            Discounted price")
print("        \"\"\"")
print("        if price < 0:")
print("            raise ValueError(\"Price cannot be negative\")")
print("        if not 0 <= discount_percent <= 100:")
print("            raise ValueError(\"Discount must be between 0 and 100\")")
print("        ")
print("        return price * (1 - discount_percent / 100)")

print()  # Empty line


# ============================================================================
# 2. PROPER ERROR HANDLING
# ============================================================================
print("=" * 60)
print("2. PROPER ERROR HANDLING")
print("=" * 60)

print("  Good error handling:")
print("    ")
print("    def process_file(filename: str) -> str:")
print("        \"\"\"Process file and return content.\"\"\"")
print("        try:")
print("            with open(filename, 'r') as f:")
print("                return f.read()")
print("        except FileNotFoundError:")
print("            raise FileNotFoundError(f\"File not found: {filename}\")")
print("        except PermissionError:")
print("            raise PermissionError(f\"Permission denied: {filename}\")")
print("        except Exception as e:")
print("            raise RuntimeError(f\"Error processing file: {e}\")")

print()  # Empty line


# ============================================================================
# 3. TYPE HINTS
# ============================================================================
print("=" * 60)
print("3. TYPE HINTS")
print("=" * 60)

print("  Using type hints:")
print("    ")
print("    from typing import List, Optional, Dict")
print("    ")
print("    def process_users(users: List[Dict[str, str]]) -> Optional[int]:")
print("        \"\"\"Process list of user dictionaries.\"\"\"")
print("        if not users:")
print("            return None")
print("        return len(users)")
print("  ")
print("  Type hints improve:")
print("    - Code readability")
print("    - IDE support")
print("    - Type checking")

print()  # Empty line


# ============================================================================
# 4. DOCUMENTATION
# ============================================================================
print("=" * 60)
print("4. DOCUMENTATION")
print("=" * 60)

print("  Good documentation:")
print("    ")
print("    class UserAccount:")
print("        \"\"\"")
print("        Represents a user account.")
print("        ")
print("        Attributes:")
print("            name: User's full name")
print("            email: User's email address")
print("            age: User's age in years")
print("        \"\"\"")
print("        ")
print("        def __init__(self, name: str, email: str, age: int):")
print("            self.name = name")
print("            self.email = email")
print("            self.age = age")

print()  # Empty line


# ============================================================================
# 5. CODE ORGANIZATION
# ============================================================================
print("=" * 60)
print("5. CODE ORGANIZATION")
print("=" * 60)

print("  Well-organized code:")
print("    ")
print("    # Constants at top")
print("    MAX_RETRIES = 3")
print("    DEFAULT_TIMEOUT = 30")
print("    ")
print("    # Helper functions")
print("    def validate_input(data):")
print("        pass")
print("    ")
print("    # Main functions")
print("    def process_data(data):")
print("        validate_input(data)")
print("        # Process...")
print("    ")
print("    # Main execution")
print("    if __name__ == '__main__':")
print("        main()")

print()  # Empty line


# ============================================================================
# 6. AVOIDING COMMON MISTAKES
# ============================================================================
print("=" * 60)
print("6. AVOIDING COMMON MISTAKES")
print("=" * 60)

print("  Common mistakes to avoid:")
print("    ")
print("    # Bad - mutable default")
print("    def add_item(item, list=[]):")
print("        list.append(item)")
print("        return list")
print("    ")
print("    # Good")
print("    def add_item(item, list=None):")
print("        if list is None:")
print("            list = []")
print("        list.append(item)")
print("        return list")

print()  # Empty line


# ============================================================================
# 7. USING BUILT-INS
# ============================================================================
print("=" * 60)
print("7. USING BUILT-INS")
print("=" * 60)

print("  Use Python built-ins:")
print("    ")
print("    # Good")
print("    total = sum(prices)")
print("    max_price = max(prices)")
print("    sorted_items = sorted(items, key=lambda x: x.price)")
print("    ")
print("    # Less efficient")
print("    total = 0")
print("    for price in prices:")
print("        total += price")

print()  # Empty line


# ============================================================================
# 8. LIST COMPREHENSIONS
# ============================================================================
print("=" * 60)
print("8. LIST COMPREHENSIONS")
print("=" * 60)

print("  Use list comprehensions:")
print("    ")
print("    # Good")
print("    squares = [x**2 for x in range(10)]")
print("    evens = [x for x in range(10) if x % 2 == 0]")
print("    ")
print("    # Less Pythonic")
print("    squares = []")
print("    for x in range(10):")
print("        squares.append(x**2)")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL BEST PRACTICES SUMMARY:")
print("=" * 60)
print("Real-world Patterns:")
print("  - Clean, well-documented functions")
print("  - Proper error handling")
print("  - Type hints for clarity")
print("  - Good code organization")
print("  - Avoid common mistakes")
print("  - Use Python built-ins")
print("  - Prefer list comprehensions")
print("=" * 60)

