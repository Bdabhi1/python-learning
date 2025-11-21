"""
Practical Built-in Functions Examples

This file demonstrates real-world examples combining multiple
built-in functions to solve common problems.
"""

# ============================================================================
# 1. DATA PROCESSING PIPELINE
# ============================================================================
print("=" * 60)
print("1. DATA PROCESSING PIPELINE")
print("=" * 60)

# Process and analyze data
raw_data = ["10", "20", "30", "40", "50"]
print(f"  Raw data: {raw_data}")

# Convert to integers
numbers = [int(x) for x in raw_data]
print(f"  Converted to int: {numbers}")

# Calculate statistics
print(f"  Count: {len(numbers)}")
print(f"  Sum: {sum(numbers)}")
print(f"  Average: {sum(numbers) / len(numbers):.2f}")
print(f"  Min: {min(numbers)}")
print(f"  Max: {max(numbers)}")

print()  # Empty line


# ============================================================================
# 2. USER INPUT VALIDATION
# ============================================================================
print("=" * 60)
print("2. USER INPUT VALIDATION")
print("=" * 60)

def validate_input(value, expected_type):
    """Validate and convert input."""
    try:
        if expected_type == int:
            return int(value)
        elif expected_type == float:
            return float(value)
        elif expected_type == str:
            return str(value)
        else:
            return value
    except (ValueError, TypeError):
        return None

# Simulated inputs
inputs = ["25", "3.14", "hello", "42"]
print("  Validating inputs:")
for inp in inputs:
    result = validate_input(inp, int)
    if result is not None:
        print(f"    '{inp}' -> {result} (valid int)")
    else:
        print(f"    '{inp}' -> Invalid")

print()  # Empty line


# ============================================================================
# 3. SORTING AND FILTERING
# ============================================================================
print("=" * 60)
print("3. SORTING AND FILTERING")
print("=" * 60)

# Student data
students = [
    {"name": "Alice", "score": 85, "age": 20},
    {"name": "Bob", "score": 92, "age": 19},
    {"name": "Charlie", "score": 78, "age": 21},
    {"name": "David", "score": 95, "age": 20}
]

# Sort by score
sorted_by_score = sorted(students, key=lambda x: x["score"], reverse=True)
print("  Sorted by score (descending):")
for student in sorted_by_score:
    print(f"    {student['name']}: {student['score']}")

# Filter passing students
passing = [s for s in students if s["score"] >= 80]
print(f"\n  Passing students (>=80): {len(passing)}")
for student in passing:
    print(f"    {student['name']}: {student['score']}")

print()  # Empty line


# ============================================================================
# 4. COMBINING DATA FROM MULTIPLE SOURCES
# ============================================================================
print("=" * 60)
print("4. COMBINING DATA FROM MULTIPLE SOURCES")
print("=" * 60)

# Combine related data
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Paris"]

# Using zip
people = list(zip(names, ages, cities))
print("  Combined data:")
for name, age, city in people:
    print(f"    {name}, {age}, {city}")

# Create dictionary
people_dict = {name: {"age": age, "city": city} 
               for name, age, city in zip(names, ages, cities)}
print(f"\n  As dictionary: {people_dict}")

print()  # Empty line


# ============================================================================
# 5. TYPE-SAFE OPERATIONS
# ============================================================================
print("=" * 60)
print("5. TYPE-SAFE OPERATIONS")
print("=" * 60)

def safe_operation(data, operation):
    """Perform operation with type checking."""
    if isinstance(data, (list, tuple)):
        if operation == "sum":
            return sum(data)
        elif operation == "len":
            return len(data)
        elif operation == "max":
            return max(data) if data else None
    elif isinstance(data, str):
        if operation == "len":
            return len(data)
        elif operation == "upper":
            return data.upper()
    return None

# Test
numbers = [1, 2, 3, 4, 5]
text = "hello"

print(f"  safe_operation([1,2,3,4,5], 'sum'): {safe_operation(numbers, 'sum')}")
print(f"  safe_operation([1,2,3,4,5], 'max'): {safe_operation(numbers, 'max')}")
print(f"  safe_operation('hello', 'upper'): {safe_operation(text, 'upper')}")

print()  # Empty line


# ============================================================================
# 6. DATA VALIDATION AND CLEANING
# ============================================================================
print("=" * 60)
print("6. DATA VALIDATION AND CLEANING")
print("=" * 60)

# Clean and validate data
raw_scores = ["85", "90", "invalid", "78", "92", "", "88"]
print(f"  Raw scores: {raw_scores}")

# Clean: convert valid strings to int, filter invalid
valid_scores = []
for score in raw_scores:
    try:
        num = int(score)
        if 0 <= num <= 100:  # Valid range
            valid_scores.append(num)
    except (ValueError, TypeError):
        continue

print(f"  Valid scores: {valid_scores}")
if valid_scores:
    print(f"  Average: {sum(valid_scores) / len(valid_scores):.2f}")
    print(f"  All passing: {all(s >= 60 for s in valid_scores)}")
    print(f"  Any excellent: {any(s >= 90 for s in valid_scores)}")

print()  # Empty line


# ============================================================================
# 7. DYNAMIC FUNCTION CALLING
# ============================================================================
print("=" * 60)
print("7. DYNAMIC FUNCTION CALLING")
print("=" * 60)

# Map operation names to functions
operations = {
    "add": sum,
    "max": max,
    "min": min,
    "len": len
}

data = [10, 20, 30, 40, 50]
operation_name = "add"

if operation_name in operations and callable(operations[operation_name]):
    func = operations[operation_name]
    if operation_name == "add":
        result = func(data)
    else:
        result = func(data)
    print(f"  Operation '{operation_name}' on {data}: {result}")

print()  # Empty line


# ============================================================================
# 8. COMPREHENSIVE DATA ANALYSIS
# ============================================================================
print("=" * 60)
print("8. COMPREHENSIVE DATA ANALYSIS")
print("=" * 60)

# Analyze dataset
sales = [100, 150, 120, 180, 200, 160, 140]
print(f"  Sales data: {sales}")

# Basic statistics
print(f"  Count: {len(sales)}")
print(f"  Total: {sum(sales)}")
print(f"  Average: {sum(sales) / len(sales):.2f}")
print(f"  Minimum: {min(sales)}")
print(f"  Maximum: {max(sales)}")

# Sorted
sorted_sales = sorted(sales)
print(f"  Sorted: {sorted_sales}")

# Reversed
reversed_sales = list(reversed(sorted_sales))
print(f"  Reversed: {reversed_sales}")

# Validation
all_positive = all(s > 0 for s in sales)
any_high = any(s > 150 for s in sales)
print(f"  All positive: {all_positive}")
print(f"  Any high (>150): {any_high}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL EXAMPLES SUMMARY:")
print("=" * 60)
print("These examples demonstrate:")
print("  - Combining multiple built-in functions")
print("  - Type checking and conversion")
print("  - Data validation and cleaning")
print("  - Sorting and filtering")
print("  - Dynamic operations")
print("  - Comprehensive data analysis")
print("\nKey Patterns:")
print("  - Use isinstance() for type checking")
print("  - Use try-except for safe conversion")
print("  - Combine sorted(), filter, and list comprehensions")
print("  - Use zip() to combine related data")
print("  - Use any()/all() for validation")
print("=" * 60)

