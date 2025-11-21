"""
While Loops in Python

This file demonstrates while loops - how to repeat code as long as
a condition is True.
"""

# ============================================================================
# 1. BASIC WHILE LOOP
# ============================================================================
print("=" * 60)
print("1. BASIC WHILE LOOP")
print("=" * 60)

# Count from 0 to 4
count = 0
print("  Counting:")
while count < 5:
    print(f"    {count}")
    count += 1  # Important: Update the variable!

print("\n  Structure:")
print("    while condition:")
print("        # Code to execute")
print("        # Update condition variable")

print()  # Empty line


# ============================================================================
# 2. WHILE VS FOR LOOP
# ============================================================================
print("=" * 60)
print("2. WHILE VS FOR LOOP")
print("=" * 60)

# Same result with for loop
print("  Using for loop:")
for i in range(5):
    print(f"    {i}")

# Same result with while loop
print("\n  Using while loop:")
count = 0
while count < 5:
    print(f"    {count}")
    count += 1

print("\n  Use 'for' when you know iterations")
print("  Use 'while' when iterations depend on condition")

print()  # Empty line


# ============================================================================
# 3. CONDITION-BASED ITERATION
# ============================================================================
print("=" * 60)
print("3. CONDITION-BASED ITERATION")
print("=" * 60)

# Keep asking until valid input (simulated)
print("  Simulated input validation:")
attempts = 0
valid_input = False

while not valid_input:
    attempts += 1
    # Simulated: assume valid input after 3 attempts
    if attempts >= 3:
        valid_input = True
        print(f"    Attempt {attempts}: Valid input received!")

print(f"  Total attempts: {attempts}")

# Countdown
print("\n  Countdown:")
timer = 5
while timer > 0:
    print(f"    {timer}...")
    timer -= 1
print("    Blast off!")

print()  # Empty line


# ============================================================================
# 4. INFINITE LOOPS
# ============================================================================
print("=" * 60)
print("4. INFINITE LOOPS")
print("=" * 60)

# Infinite loop (commented out to avoid actual infinite loop)
print("  Example of infinite loop structure:")
print("    while True:")
print("        # This runs forever!")
print("        # Use break to exit")

# Controlled infinite loop with break
print("\n  Controlled infinite loop:")
count = 0
while True:
    count += 1
    print(f"    Iteration {count}")
    if count >= 5:
        break  # Exit loop
print("    Loop exited with break")

print()  # Empty line


# ============================================================================
# 5. WHILE LOOP WITH ELSE
# ============================================================================
print("=" * 60)
print("5. WHILE LOOP WITH ELSE")
print("=" * 60)

# else executes if loop completes normally (no break)
print("  Loop without break:")
count = 0
while count < 3:
    print(f"    {count}")
    count += 1
else:
    print("    Loop completed normally")

# else does NOT execute if break is used
print("\n  Loop with break:")
count = 0
while count < 5:
    if count == 3:
        break
    print(f"    {count}")
    count += 1
else:
    print("    This won't print (break was used)")

print()  # Empty line


# ============================================================================
# 6. COMMON PATTERNS
# ============================================================================
print("=" * 60)
print("6. COMMON PATTERNS")
print("=" * 60)

# Pattern 1: Input validation
print("  Pattern 1: Input validation (simulated)")
max_attempts = 3
attempts = 0
valid = False

while attempts < max_attempts and not valid:
    attempts += 1
    # Simulated validation
    if attempts == 2:
        valid = True
        print(f"    Attempt {attempts}: Valid!")

# Pattern 2: Processing until condition
print("\n  Pattern 2: Process until condition")
total = 0
number = 1
while total < 20:
    total += number
    number += 1
    print(f"    Number: {number-1}, Total: {total}")

# Pattern 3: Menu loop
print("\n  Pattern 3: Menu loop (simulated)")
choice = ""
attempts = 0
while choice not in ["1", "2", "3"] and attempts < 3:
    attempts += 1
    # Simulated: user selects valid option
    if attempts == 2:
        choice = "2"
        print(f"    Selected option: {choice}")

print()  # Empty line


# ============================================================================
# 7. NESTED WHILE LOOPS
# ============================================================================
print("=" * 60)
print("7. NESTED WHILE LOOPS")
print("=" * 60)

# Multiplication table with while
print("  Multiplication table (3x3) with while:")
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"    {i} x {j} = {i * j}")
        j += 1
    i += 1

print()  # Empty line


# ============================================================================
# 8. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("8. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Guessing game (simulated)
print("Example 1: Guessing game (simulated)")
secret_number = 7
guess = 0
attempts = 0

while guess != secret_number and attempts < 5:
    attempts += 1
    # Simulated guesses
    if attempts == 3:
        guess = 7
        print(f"    Attempt {attempts}: Correct! The number was {secret_number}")
    else:
        print(f"    Attempt {attempts}: Wrong guess")

# Example 2: Fibonacci sequence
print("\nExample 2: Fibonacci sequence")
a, b = 0, 1
count = 0
print("  First 10 Fibonacci numbers:")
while count < 10:
    print(f"    {a}")
    a, b = b, a + b
    count += 1

# Example 3: Processing queue
print("\nExample 3: Processing queue")
queue = [1, 2, 3, 4, 5]
processed = []
while queue:
    item = queue.pop(0)
    processed.append(item)
    print(f"    Processing: {item}")
print(f"  Processed items: {processed}")

# Example 4: Retry mechanism
print("\nExample 4: Retry mechanism (simulated)")
max_retries = 3
retry_count = 0
success = False

while retry_count < max_retries and not success:
    retry_count += 1
    # Simulated: succeed on second try
    if retry_count == 2:
        success = True
        print(f"    Retry {retry_count}: Success!")
    else:
        print(f"    Retry {retry_count}: Failed, retrying...")

print()  # Empty line


# ============================================================================
# 9. COMMON MISTAKES
# ============================================================================
print("=" * 60)
print("9. COMMON MISTAKES")
print("=" * 60)

print("Mistake 1: Forgetting to update loop variable")
print("  ❌ Wrong:")
print("    count = 0")
print("    while count < 5:")
print("        print(count)")
print("        # Forgot count += 1 - infinite loop!")
print("\n  ✅ Correct:")
print("    count = 0")
print("    while count < 5:")
print("        print(count)")
print("        count += 1")

print("\nMistake 2: Infinite loop without exit condition")
print("  ❌ Wrong:")
print("    while True:")
print("        print('Forever!')")
print("\n  ✅ Correct:")
print("    while True:")
print("        if condition:")
print("            break")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("WHILE LOOPS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Repeats code while condition is True")
print("  - Syntax: while condition:")
print("  - Must update condition variable to avoid infinite loop")
print("  - Use when iterations depend on condition")
print("  - Use 'break' to exit loop early")
print("  - else clause executes if loop completes normally")
print("  - Can be nested like for loops")
print("\nWhen to use:")
print("  - Input validation")
print("  - Processing until condition met")
print("  - Unknown number of iterations")
print("  - Menu systems")
print("  - Retry mechanisms")
print("=" * 60)

