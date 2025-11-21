"""
Break and Continue Statements

This file demonstrates break and continue - how to control loop
execution by exiting early or skipping iterations.
"""

# ============================================================================
# 1. BREAK STATEMENT
# ============================================================================
print("=" * 60)
print("1. BREAK STATEMENT")
print("=" * 60)

# break exits the loop immediately
print("  Loop with break at 5:")
for i in range(10):
    if i == 5:
        break  # Exit loop
    print(f"    {i}")

print("\n  Key Point: break exits the entire loop immediately")

# break in while loop
print("\n  While loop with break:")
count = 0
while count < 10:
    if count == 5:
        break
    print(f"    {count}")
    count += 1

print()  # Empty line


# ============================================================================
# 2. CONTINUE STATEMENT
# ============================================================================
print("=" * 60)
print("2. CONTINUE STATEMENT")
print("=" * 60)

# continue skips to next iteration
print("  Loop with continue (skip even numbers):")
for i in range(10):
    if i % 2 == 0:
        continue  # Skip to next iteration
    print(f"    {i}")

print("\n  Key Point: continue skips rest of current iteration")

# continue in while loop
print("\n  While loop with continue:")
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # Skip even numbers
    print(f"    {count}")

print()  # Empty line


# ============================================================================
# 3. BREAK VS CONTINUE
# ============================================================================
print("=" * 60)
print("3. BREAK VS CONTINUE")
print("=" * 60)

# break - exits loop
print("  Using break (exits at 5):")
for i in range(10):
    if i == 5:
        break
    print(f"    {i}")
print("    Loop ended")

# continue - skips to next iteration
print("\n  Using continue (skips 5):")
for i in range(10):
    if i == 5:
        continue
    print(f"    {i}")
print("    Loop completed")

print("\n  Difference:")
print("    - break: Exits entire loop")
print("    - continue: Skips to next iteration")

print()  # Empty line


# ============================================================================
# 4. BREAK IN NESTED LOOPS
# ============================================================================
print("=" * 60)
print("4. BREAK IN NESTED LOOPS")
print("=" * 60)

# break only exits innermost loop
print("  Nested loops - break exits inner loop only:")
for i in range(3):
    print(f"    Outer loop: {i}")
    for j in range(5):
        if j == 2:
            break  # Exits inner loop only
        print(f"      Inner loop: {j}")

print("\n  Note: break only exits the loop it's in")

# Breaking out of nested loops
print("\n  Breaking out of nested loops (using flag):")
found = False
for i in range(3):
    if found:
        break
    for j in range(3):
        if i == 1 and j == 1:
            found = True
            break
        print(f"    ({i}, {j})")

print()  # Empty line


# ============================================================================
# 5. CONTINUE IN NESTED LOOPS
# ============================================================================
print("=" * 60)
print("5. CONTINUE IN NESTED LOOPS")
print("=" * 60)

# continue affects current loop only
print("  Nested loops with continue:")
for i in range(3):
    print(f"    Outer: {i}")
    for j in range(3):
        if j == 1:
            continue  # Skips rest of inner loop iteration
        print(f"      Inner: {j}")

print()  # Empty line


# ============================================================================
# 6. BREAK WITH ELSE
# ============================================================================
print("=" * 60)
print("6. BREAK WITH ELSE")
print("=" * 60)

# else does NOT execute if break is used
print("  Loop with break - else doesn't execute:")
for i in range(5):
    if i == 3:
        break
    print(f"    {i}")
else:
    print("    This won't print (break was used)")

# else executes if no break
print("\n  Loop without break - else executes:")
for i in range(3):
    print(f"    {i}")
else:
    print("    Loop completed normally (no break)")

print()  # Empty line


# ============================================================================
# 7. PRACTICAL EXAMPLES - BREAK
# ============================================================================
print("=" * 60)
print("7. PRACTICAL EXAMPLES - BREAK")
print("=" * 60)

# Example 1: Find first occurrence
print("Example 1: Find first occurrence")
numbers = [1, 3, 5, 7, 9, 11, 13]
target = 7
found = False

for num in numbers:
    if num == target:
        print(f"    Found {target}!")
        found = True
        break

if not found:
    print(f"    {target} not found")

# Example 2: Input validation
print("\nExample 2: Input validation (simulated)")
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    attempts += 1
    # Simulated: valid input on attempt 3
    if attempts == 3:
        print(f"    Attempt {attempts}: Valid input received!")
        break
    print(f"    Attempt {attempts}: Invalid, retrying...")

# Example 3: Search and exit
print("\nExample 3: Search in list")
items = ["apple", "banana", "cherry", "date"]
search = "cherry"

for item in items:
    if item == search:
        print(f"    Found: {search}")
        break
else:
    print(f"    Not found: {search}")

print()  # Empty line


# ============================================================================
# 8. PRACTICAL EXAMPLES - CONTINUE
# ============================================================================
print("=" * 60)
print("8. PRACTICAL EXAMPLES - CONTINUE")
print("=" * 60)

# Example 1: Skip invalid items
print("Example 1: Skip invalid items")
numbers = [1, -2, 3, -4, 5, -6, 7]
positive_sum = 0

for num in numbers:
    if num < 0:
        continue  # Skip negative numbers
    positive_sum += num
    print(f"    Added {num}, sum: {positive_sum}")

print(f"  Final sum of positives: {positive_sum}")

# Example 2: Process valid data only
print("\nExample 2: Process valid data only")
data = [10, None, 20, None, 30, None, 40]
processed = []

for item in data:
    if item is None:
        continue  # Skip None values
    processed.append(item * 2)
    print(f"    Processed: {item} -> {item * 2}")

print(f"  Processed items: {processed}")

# Example 3: Filter during iteration
print("\nExample 3: Filter even numbers")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("  Odd numbers:")
for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers
    print(f"    {num}")

print()  # Empty line


# ============================================================================
# 9. COMBINING BREAK AND CONTINUE
# ============================================================================
print("=" * 60)
print("9. COMBINING BREAK AND CONTINUE")
print("=" * 60)

# Process items until condition, skip invalid ones
print("  Process until sum > 20, skip negatives:")
numbers = [5, -2, 8, -1, 10, 3, 7]
total = 0

for num in numbers:
    if num < 0:
        continue  # Skip negative
    total += num
    print(f"    Added {num}, total: {total}")
    if total > 20:
        print(f"    Total exceeded 20, stopping")
        break

print(f"  Final total: {total}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("BREAK AND CONTINUE SUMMARY:")
print("=" * 60)
print("break:")
print("  - Exits the loop immediately")
print("  - Only exits the loop it's in (innermost in nested loops)")
print("  - else clause does NOT execute if break is used")
print("\ncontinue:")
print("  - Skips to next iteration")
print("  - Skips rest of current iteration")
print("  - Loop continues with next item")
print("\nKey Points:")
print("  - Use break to exit early when condition met")
print("  - Use continue to skip invalid/unwanted items")
print("  - Both work in for and while loops")
print("  - In nested loops, affects current loop only")
print("=" * 60)

