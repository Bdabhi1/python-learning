# Control Flow in Python

Control flow determines the order in which statements are executed in your program. It allows you to make decisions, repeat actions, and control the flow of your code.

## Table of Contents
1. [What is Control Flow?](#what-is-control-flow)
2. [Conditional Statements (if/else)](#conditional-statements-ifelse)
3. [The `elif` Statement](#the-elif-statement)
4. [Nested Conditionals](#nested-conditionals)
5. [For Loops](#for-loops)
6. [While Loops](#while-loops)
7. [Break and Continue](#break-and-continue)
8. [The `pass` Statement](#the-pass-statement)
9. [Best Practices](#best-practices)

---

## What is Control Flow?

**Control flow** refers to the order in which your program's statements are executed. It allows you to:
- Make decisions (if/else)
- Repeat code (loops)
- Skip or exit loops (break/continue)
- Control program execution

**Types of control flow:**
1. **Sequential**: Code executes line by line (default)
2. **Conditional**: Execute code based on conditions (if/else)
3. **Iterative**: Repeat code multiple times (loops)

---

## Conditional Statements (if/else)

Conditional statements allow your program to make decisions based on conditions.

### Basic `if` Statement

```python
age = 18
if age >= 18:
    print("You are an adult")
```

**Syntax:**
- `if` keyword
- Condition (expression that evaluates to True/False)
- Colon `:`
- Indented block (executes if condition is True)

### `if-else` Statement

```python
age = 15
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

**How it works:**
- If condition is `True`, execute `if` block
- If condition is `False`, execute `else` block

### Comparison Operators in Conditions

```python
x = 10
if x > 5:
    print("x is greater than 5")
if x == 10:
    print("x equals 10")
if x != 0:
    print("x is not zero")
```

### Logical Operators in Conditions

```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")

if age < 18 or not has_license:
    print("Cannot drive")
```

---

## The `elif` Statement

`elif` (else-if) allows you to check multiple conditions.

### Basic `elif`

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")
```

**How it works:**
1. Check first `if` condition
2. If False, check first `elif`
3. If False, check next `elif`
4. Continue until one is True or reach `else`

**Important:** Only the first True condition executes!

### Multiple Conditions

```python
temperature = 25

if temperature > 30:
    print("Hot")
elif temperature > 20:
    print("Warm")
elif temperature > 10:
    print("Cool")
else:
    print("Cold")
```

---

## Nested Conditionals

You can nest `if` statements inside other `if` statements.

```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("Can drive")
    else:
        print("Need to get a license")
else:
    print("Too young to drive")
```

**Best Practice:** Use `and`/`or` instead of nesting when possible:
```python
# Better
if age >= 18 and has_license:
    print("Can drive")
```

---

## For Loops

For loops iterate over a sequence (list, string, range, etc.).

### Basic For Loop

```python
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4
```

### Iterating Over Lists

```python
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
```

### Iterating Over Strings

```python
word = "Python"
for char in word:
    print(char)
```

### The `range()` Function

```python
# range(stop) - 0 to stop-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop) - start to stop-1
for i in range(2, 5):
    print(i)  # 2, 3, 4

# range(start, stop, step) - with step
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

### Enumerate

```python
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

---

## While Loops

While loops repeat code as long as a condition is True.

### Basic While Loop

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

**Important:** Make sure the condition eventually becomes False, or you'll have an infinite loop!

### Infinite Loops

```python
# This runs forever!
# while True:
#     print("Infinite loop")
```

**Breaking infinite loops:**
```python
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break  # Exit loop
```

### While with User Input

```python
# Keep asking until valid input
while True:
    age = input("Enter age (0-120): ")
    try:
        age = int(age)
        if 0 <= age <= 120:
            break
        else:
            print("Invalid range!")
    except ValueError:
        print("Invalid input!")
```

---

## Break and Continue

### `break` Statement

Exits the loop immediately.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
# Output: 0, 1, 2, 3, 4
```

### `continue` Statement

Skips the rest of the current iteration and continues to the next.

```python
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
# Output: 1, 3, 5, 7, 9
```

### `break` and `continue` in While Loops

```python
count = 0
while count < 10:
    count += 1
    if count == 5:
        continue  # Skip 5
    if count == 8:
        break  # Exit at 8
    print(count)
```

---

## The `pass` Statement

`pass` is a null operation - it does nothing. Useful as a placeholder.

```python
if condition:
    pass  # Do nothing, but syntax requires something here
else:
    print("Not condition")
```

**Use cases:**
- Placeholder for future code
- Empty function/class body
- Empty conditional block

---

## Nested Loops

Loops can be nested inside other loops.

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
```

**Be careful:** Nested loops can be slow for large iterations!

---

## Best Practices

1. **Use meaningful variable names**
   ```python
   # Good
   for student in students:
       print(student)
   
   # Less clear
   for s in students:
       print(s)
   ```

2. **Avoid deep nesting**
   ```python
   # Better
   if age >= 18 and has_license:
       print("Can drive")
   
   # Less preferred
   if age >= 18:
       if has_license:
           print("Can drive")
   ```

3. **Use `for` when you know iterations**
   ```python
   # Good - known number of iterations
   for i in range(10):
       print(i)
   ```

4. **Use `while` for unknown iterations**
   ```python
   # Good - unknown iterations
   while user_wants_to_continue:
       process_data()
   ```

5. **Always update loop variables**
   ```python
   # Correct
   count = 0
   while count < 5:
       count += 1  # Update variable!
   ```

---

## Common Mistakes to Avoid

1. **Forgetting colons**
   ```python
   # Wrong
   if x > 5
       print("Greater")
   
   # Correct
   if x > 5:
       print("Greater")
   ```

2. **Incorrect indentation**
   ```python
   # Wrong
   if x > 5:
   print("Greater")  # IndentationError!
   
   # Correct
   if x > 5:
       print("Greater")
   ```

3. **Infinite loops**
   ```python
   # Wrong - infinite loop
   count = 0
   while count < 5:
       print(count)
       # Forgot to increment count!
   
   # Correct
   count = 0
   while count < 5:
       print(count)
       count += 1
   ```

4. **Using `=` instead of `==`**
   ```python
   # Wrong
   if x = 5:  # SyntaxError!
   
   # Correct
   if x == 5:
       pass
   ```

---

## Summary

- **Conditional statements** (`if/else/elif`) make decisions
- **For loops** iterate over sequences
- **While loops** repeat while condition is True
- **`break`** exits a loop
- **`continue`** skips to next iteration
- **`pass`** is a null operation (placeholder)
- Use **indentation** to define code blocks
- Always **update loop variables** to avoid infinite loops

**Remember**: Control flow is fundamental to programming. Master these concepts to write powerful Python programs!

---

## Next Steps

Now that you understand control flow:
1. Practice with the examples in this folder
2. Create programs with conditional logic
3. Experiment with different loop patterns
4. Move on to **07-data-structures** to learn about lists, dictionaries, and more

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_conditional_statements.py`: if/else/elif statements - start here!
2. `02_for_loops.py`: Iterating with for loops
3. `03_while_loops.py`: Repeating with while loops
4. `04_break_continue.py`: Controlling loop execution
5. `05_nested_loops.py`: Loops within loops
6. `06_practical_examples.py`: Real-world control flow examples

Run these files in order to see control flow in action!

