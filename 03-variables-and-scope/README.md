# Variables and Scope in Python

Understanding variable scope is crucial for writing correct Python programs. This guide will teach you how variables are accessed and modified in different parts of your code.

## Table of Contents
1. [What is Scope?](#what-is-scope)
2. [Types of Scope](#types-of-scope)
3. [Local Scope](#local-scope)
4. [Global Scope](#global-scope)
5. [The `global` Keyword](#the-global-keyword)
6. [The `nonlocal` Keyword](#the-nonlocal-keyword)
7. [Scope Resolution (LEGB Rule)](#scope-resolution-legb-rule)
8. [Common Scope Issues](#common-scope-issues)
9. [Best Practices](#best-practices)

---

## What is Scope?

**Scope** determines where in your code a variable can be accessed and modified. It defines the "visibility" and "lifetime" of variables.

**Key concepts:**
- **Visibility**: Where can you see/use the variable?
- **Lifetime**: How long does the variable exist?
- **Namespace**: A container that holds variable names and their values

**Real-world analogy:**
- Think of scope like rooms in a house
- Variables in the "living room" (global scope) can be seen from anywhere
- Variables in a "bedroom" (local scope) can only be seen inside that room
- You need special permission (keywords) to access variables from other rooms

---

## Types of Scope

Python has four types of scope (LEGB rule):

1. **L** - **Local**: Inside the current function
2. **E** - **Enclosing**: In enclosing functions (nested functions)
3. **G** - **Global**: At the module level
4. **B** - **Built-in**: Python's built-in names

We'll focus on **Local** and **Global** scope first, as they're the most common.

---

## Local Scope

Variables defined **inside a function** have **local scope**. They can only be accessed within that function.

### Characteristics:
- Created when the function is called
- Destroyed when the function returns
- Cannot be accessed from outside the function
- Each function call creates a new local namespace

### Example:
```python
def my_function():
    local_var = "I'm local"
    print(local_var)  # ✅ Works - inside the function

my_function()
# print(local_var)  # ❌ Error! local_var doesn't exist here
```

**What happens:**
1. When `my_function()` is called, `local_var` is created
2. `local_var` exists only inside the function
3. When the function ends, `local_var` is destroyed
4. Trying to access it outside causes a `NameError`

### Multiple Local Variables:
```python
def calculate_total(price, quantity):
    # These are all local variables
    tax_rate = 0.08
    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total

result = calculate_total(10, 2)
# print(tax_rate)  # ❌ Error! tax_rate is local to calculate_total
```

---

## Global Scope

Variables defined **at the module level** (outside functions) have **global scope**. They can be accessed from anywhere in the module.

### Characteristics:
- Created when the module is loaded
- Exist for the entire program execution
- Can be accessed from any function
- Can be modified from functions (with restrictions)

### Example:
```python
# Global variable
global_var = "I'm global"

def my_function():
    print(global_var)  # ✅ Works - can read global variables

my_function()  # Output: I'm global
print(global_var)  # ✅ Works - can access from module level
```

### Reading vs. Modifying Global Variables:

**Reading is easy:**
```python
global_var = 10

def read_global():
    print(global_var)  # ✅ Can read without any keyword

read_global()  # Output: 10
```

**Modifying requires the `global` keyword:**
```python
global_var = 10

def modify_global():
    global global_var  # Must declare 'global'
    global_var = 20    # Now we can modify it

modify_global()
print(global_var)  # Output: 20
```

**Without `global` keyword:**
```python
global_var = 10

def try_modify():
    global_var = 20  # This creates a LOCAL variable!
    print(global_var)  # Output: 20 (local)

try_modify()
print(global_var)  # Output: 10 (global unchanged!)
```

---

## The `global` Keyword

Use `global` to modify global variables from inside a function.

### Syntax:
```python
global variable_name
```

### When to use:
- When you need to **modify** a global variable inside a function
- When you want to **create** a global variable from inside a function

### Example 1: Modifying Global Variable
```python
counter = 0

def increment():
    global counter
    counter += 1
    print(f"Counter is now: {counter}")

increment()  # Counter is now: 1
increment()  # Counter is now: 2
print(counter)  # Output: 2
```

### Example 2: Creating Global Variable
```python
def create_global():
    global new_global
    new_global = "I was created in a function!"

create_global()
print(new_global)  # ✅ Works!
```

### Example 3: Multiple Global Variables
```python
x = 1
y = 2
z = 3

def modify_multiple():
    global x, y, z
    x = 10
    y = 20
    z = 30

modify_multiple()
print(x, y, z)  # Output: 10 20 30
```

### ⚠️ Important Notes:
- Only needed when **modifying** global variables
- Not needed for **reading** global variables
- Use sparingly - too many global variables make code hard to maintain
- Consider passing values as parameters instead

---

## The `nonlocal` Keyword

Use `nonlocal` to modify variables in **enclosing (outer) functions** from **nested (inner) functions**.

### When to use:
- When you have nested functions
- When you need to modify a variable from an outer (but not global) scope

### Example:
```python
def outer_function():
    outer_var = "I'm in outer function"
    
    def inner_function():
        nonlocal outer_var  # Refers to outer_var in outer_function
        outer_var = "Modified by inner function"
        print(f"Inner: {outer_var}")
    
    print(f"Before inner: {outer_var}")
    inner_function()
    print(f"After inner: {outer_var}")

outer_function()
# Output:
# Before inner: I'm in outer function
# Inner: Modified by inner function
# After inner: Modified by inner function
```

### Without `nonlocal`:
```python
def outer_function():
    outer_var = "I'm in outer function"
    
    def inner_function():
        outer_var = "New local variable"  # Creates LOCAL variable!
        print(f"Inner: {outer_var}")
    
    print(f"Before inner: {outer_var}")
    inner_function()
    print(f"After inner: {outer_var}")

outer_function()
# Output:
# Before inner: I'm in outer function
# Inner: New local variable
# After inner: I'm in outer function (unchanged!)
```

### Multiple Levels:
```python
def level1():
    var = "Level 1"
    
    def level2():
        var = "Level 2"
        
        def level3():
            nonlocal var  # Modifies var in level2
            var = "Modified in Level 3"
        
        print(f"Before level3: {var}")
        level3()
        print(f"After level3: {var}")
    
    print(f"Before level2: {var}")
    level2()
    print(f"After level2: {var}")

level1()
```

---

## Scope Resolution (LEGB Rule)

Python searches for variables in this order (LEGB):

1. **L** - **Local**: Current function's namespace
2. **E** - **Enclosing**: Enclosing functions' namespaces
3. **G** - **Global**: Module's namespace
4. **B** - **Built-in**: Python's built-in names

### Example:
```python
# Built-in (B)
# print is a built-in function

# Global (G)
x = "global"

def outer():
    # Enclosing (E)
    x = "enclosing"
    
    def inner():
        # Local (L)
        x = "local"
        print(x)  # Prints "local" (found in Local scope)
    
    inner()
    print(x)  # Prints "enclosing" (found in Enclosing scope)

outer()
print(x)  # Prints "global" (found in Global scope)
```

### Shadowing:
When a local variable has the same name as a global variable, it "shadows" (hides) the global variable:

```python
x = "global"

def my_function():
    x = "local"  # Shadows the global x
    print(x)     # Prints "local"

my_function()
print(x)  # Prints "global" (global x unchanged)
```

---

## Common Scope Issues

### Issue 1: Accessing Local Variable Before Assignment
```python
x = 10

def my_function():
    print(x)  # ❌ UnboundLocalError!
    x = 20    # This line makes x local to the function

my_function()
```

**Problem:** Python sees `x = 20` and decides `x` is local. But you're trying to print it before assigning.

**Solution:**
```python
x = 10

def my_function():
    global x  # Declare it's global
    print(x)  # ✅ Works
    x = 20

my_function()
```

### Issue 2: Modifying Global Without `global` Keyword
```python
counter = 0

def increment():
    counter += 1  # ❌ UnboundLocalError!

increment()
```

**Solution:**
```python
counter = 0

def increment():
    global counter
    counter += 1  # ✅ Works

increment()
```

### Issue 3: Confusing Local and Global
```python
x = 10

def my_function():
    x = 20  # Creates LOCAL variable
    print(x)  # Prints 20

my_function()
print(x)  # Prints 10 (global unchanged)
```

**Solution:** Use `global` if you want to modify the global:
```python
x = 10

def my_function():
    global x
    x = 20  # Modifies GLOBAL variable
    print(x)  # Prints 20

my_function()
print(x)  # Prints 20 (global changed)
```

---

## Best Practices

### 1. Minimize Global Variables
**Bad:**
```python
counter = 0
total = 0
name = ""

def process():
    global counter, total, name
    counter += 1
    total += 10
    name = "Alice"
```

**Good:**
```python
def process(counter, total, name):
    counter += 1
    total += 10
    name = "Alice"
    return counter, total, name
```

### 2. Use Parameters and Return Values
**Bad:**
```python
result = 0

def calculate(x, y):
    global result
    result = x + y

calculate(5, 3)
print(result)
```

**Good:**
```python
def calculate(x, y):
    return x + y

result = calculate(5, 3)
print(result)
```

### 3. Use Descriptive Names
Avoid shadowing built-ins or common names:
```python
# Bad
def my_function(list, dict, str):
    pass

# Good
def my_function(items, data, text):
    pass
```

### 4. Be Explicit About Scope
If you need to modify a global, use `global` explicitly:
```python
# Clear and explicit
def modify_counter():
    global counter
    counter += 1
```

### 5. Prefer Local Variables
Keep variables as local as possible:
```python
# Good: Local variable
def calculate_total(price, quantity):
    tax = 0.08  # Local - only needed here
    return price * quantity * (1 + tax)
```

---

## Summary

- **Scope** determines where variables can be accessed
- **Local scope**: Variables inside functions (created/destroyed with function)
- **Global scope**: Variables at module level (exist for entire program)
- **`global` keyword**: Modify global variables from functions
- **`nonlocal` keyword**: Modify variables in enclosing functions
- **LEGB rule**: Python searches Local → Enclosing → Global → Built-in
- **Best practice**: Minimize global variables, use parameters and return values

**Remember**: Understanding scope prevents many bugs and makes your code more maintainable!

---

## Next Steps

Now that you understand variable scope:
1. Practice with the examples in this folder
2. Try creating nested functions with `nonlocal`
3. Experiment with global vs local variables
4. Move on to **04-operators** to learn about Python operators

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_local_scope.py`: Demonstrates local scope and function variables - start here!
2. `02_global_scope.py`: Shows global variables and the `global` keyword
3. `03_nonlocal_scope.py`: Examples of nested functions and `nonlocal`
4. `04_scope_resolution.py`: Demonstrates the LEGB rule
5. `05_common_issues.py`: Common scope-related errors and solutions

Run these files in order to see variable scope in action!

