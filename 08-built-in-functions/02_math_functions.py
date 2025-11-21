"""
Mathematical Built-in Functions

This file demonstrates built-in functions for mathematical operations.
"""

# ============================================================================
# 1. ABS() - ABSOLUTE VALUE
# ============================================================================
print("=" * 60)
print("1. ABS() - ABSOLUTE VALUE")
print("=" * 60)

# Absolute value
result1 = abs(-5)
print(f"  abs(-5): {result1}")

result2 = abs(5)
print(f"  abs(5): {result2}")

result3 = abs(-3.14)
print(f"  abs(-3.14): {result3}")

result4 = abs(0)
print(f"  abs(0): {result4}")

print("\n  Returns the absolute (positive) value of a number")

print()  # Empty line


# ============================================================================
# 2. ROUND() - ROUND NUMBERS
# ============================================================================
print("=" * 60)
print("2. ROUND() - ROUND NUMBERS")
print("=" * 60)

# Round to nearest integer
result1 = round(3.14)
print(f"  round(3.14): {result1}")

result2 = round(3.5)
print(f"  round(3.5): {result2}")

result3 = round(3.49)
print(f"  round(3.49): {result3}")

# Round to specific decimal places
result4 = round(3.14159, 2)
print(f"  round(3.14159, 2): {result4}")

result5 = round(3.14159, 3)
print(f"  round(3.14159, 3): {result5}")

# Round negative numbers
result6 = round(-3.5)
print(f"  round(-3.5): {result6}")

print()  # Empty line


# ============================================================================
# 3. MIN() - MINIMUM VALUE
# ============================================================================
print("=" * 60)
print("3. MIN() - MINIMUM VALUE")
print("=" * 60)

# From multiple arguments
result1 = min(1, 2, 3)
print(f"  min(1, 2, 3): {result1}")

# From iterable
result2 = min([10, 20, 30, 5, 15])
print(f"  min([10, 20, 30, 5, 15]): {result2}")

# From strings (lexicographic)
result3 = min("apple", "banana", "cherry")
print(f"  min('apple', 'banana', 'cherry'): {result3}")

# With key function
result4 = min([(1, 2), (3, 1), (2, 3)], key=lambda x: x[1])
print(f"  min([(1,2), (3,1), (2,3)], key=lambda x: x[1]): {result4}")

print()  # Empty line


# ============================================================================
# 4. MAX() - MAXIMUM VALUE
# ============================================================================
print("=" * 60)
print("4. MAX() - MAXIMUM VALUE")
print("=" * 60)

# From multiple arguments
result1 = max(1, 2, 3)
print(f"  max(1, 2, 3): {result1}")

# From iterable
result2 = max([10, 20, 30, 5, 15])
print(f"  max([10, 20, 30, 5, 15]): {result2}")

# From strings
result3 = max("apple", "banana", "cherry")
print(f"  max('apple', 'banana', 'cherry'): {result3}")

# With key function
result4 = max([(1, 2), (3, 1), (2, 3)], key=lambda x: x[1])
print(f"  max([(1,2), (3,1), (2,3)], key=lambda x: x[1]): {result4}")

print()  # Empty line


# ============================================================================
# 5. SUM() - SUM OF ITERABLE
# ============================================================================
print("=" * 60)
print("5. SUM() - SUM OF ITERABLE")
print("=" * 60)

# Sum of list
result1 = sum([1, 2, 3, 4, 5])
print(f"  sum([1, 2, 3, 4, 5]): {result1}")

# Sum of tuple
result2 = sum((10, 20, 30))
print(f"  sum((10, 20, 30)): {result2}")

# Sum with start value
result3 = sum([1, 2, 3], 10)
print(f"  sum([1, 2, 3], 10): {result3} (starts at 10)")

# Sum of range
result4 = sum(range(1, 6))
print(f"  sum(range(1, 6)): {result4}")

print()  # Empty line


# ============================================================================
# 6. POW() - POWER
# ============================================================================
print("=" * 60)
print("6. POW() - POWER")
print("=" * 60)

# Power operation
result1 = pow(2, 3)
print(f"  pow(2, 3): {result1} (2 to the power of 3)")

result2 = pow(5, 2)
print(f"  pow(5, 2): {result2} (5 squared)")

# Equivalent to ** operator
result3 = 2 ** 3
print(f"  2 ** 3: {result3} (same as pow(2, 3))")

# With modulo (pow(x, y, z) = (x**y) % z)
result4 = pow(2, 3, 5)
print(f"  pow(2, 3, 5): {result4} ((2**3) % 5)")

print()  # Empty line


# ============================================================================
# 7. DIVMOD() - DIVISION AND MODULO
# ============================================================================
print("=" * 60)
print("7. DIVMOD() - DIVISION AND MODULO")
print("=" * 60)

# Returns quotient and remainder
result1 = divmod(10, 3)
print(f"  divmod(10, 3): {result1} (quotient, remainder)")
print(f"    10 // 3 = {result1[0]}, 10 % 3 = {result1[1]}")

result2 = divmod(20, 4)
print(f"  divmod(20, 4): {result2}")

result3 = divmod(17, 5)
print(f"  divmod(17, 5): {result3}")

# Unpacking
quotient, remainder = divmod(17, 5)
print(f"  quotient, remainder = divmod(17, 5)")
print(f"    quotient: {quotient}, remainder: {remainder}")

print()  # Empty line


# ============================================================================
# 8. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("8. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Calculate statistics
print("Example 1: Calculate Statistics")
scores = [85, 90, 78, 92, 88, 95, 87]
print(f"  Scores: {scores}")
print(f"  Minimum: {min(scores)}")
print(f"  Maximum: {max(scores)}")
print(f"  Sum: {sum(scores)}")
print(f"  Average: {sum(scores) / len(scores):.2f}")

# Example 2: Distance calculation
print("\nExample 2: Distance Calculation")
point1 = (0, 0)
point2 = (3, 4)
distance = ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5
print(f"  Point 1: {point1}")
print(f"  Point 2: {point2}")
print(f"  Distance: {distance:.2f}")

# Example 3: Rounding prices
print("\nExample 3: Rounding Prices")
prices = [19.999, 29.995, 39.991]
rounded_prices = [round(price, 2) for price in prices]
print(f"  Original: {prices}")
print(f"  Rounded: {rounded_prices}")

# Example 4: Find extremes
print("\nExample 4: Find Extremes")
temperatures = [25, 30, 22, 28, 35, 20]
print(f"  Temperatures: {temperatures}")
print(f"  Coldest: {min(temperatures)}°C")
print(f"  Hottest: {max(temperatures)}°C")
print(f"  Range: {max(temperatures) - min(temperatures)}°C")

# Example 5: Calculate total with discount
print("\nExample 5: Calculate Total")
items = [10.99, 5.50, 8.25, 12.00]
subtotal = sum(items)
discount = 0.1
total = round(subtotal * (1 - discount), 2)
print(f"  Items: {items}")
print(f"  Subtotal: ${subtotal:.2f}")
print(f"  Discount (10%): ${subtotal * discount:.2f}")
print(f"  Total: ${total}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("MATHEMATICAL FUNCTIONS SUMMARY:")
print("=" * 60)
print("Function  | Description              | Example")
print("-" * 55)
print("abs()     | Absolute value           | abs(-5) -> 5")
print("round()   | Round number             | round(3.14, 2) -> 3.14")
print("min()     | Minimum value            | min(1,2,3) -> 1")
print("max()     | Maximum value            | max(1,2,3) -> 3")
print("sum()     | Sum of iterable          | sum([1,2,3]) -> 6")
print("pow()     | Power                    | pow(2,3) -> 8")
print("divmod()  | Division and modulo      | divmod(10,3) -> (3,1)")
print("=" * 60)
print("\nKey Points:")
print("  - All work with numbers")
print("  - min()/max() work with any comparable types")
print("  - sum() works with iterables of numbers")
print("  - round() can specify decimal places")
print("  - pow() is equivalent to ** operator")
print("=" * 60)

