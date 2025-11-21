# Operators in Python

Operators are special symbols that perform operations on values and variables. Understanding operators is essential for performing calculations, comparisons, and logical operations in Python.

## Table of Contents
1. [What are Operators?](#what-are-operators)
2. [Arithmetic Operators](#arithmetic-operators)
3. [Comparison Operators](#comparison-operators)
4. [Logical Operators](#logical-operators)
5. [Assignment Operators](#assignment-operators)
6. [Identity Operators](#identity-operators)
7. [Membership Operators](#membership-operators)
8. [Bitwise Operators](#bitwise-operators)
9. [Operator Precedence](#operator-precedence)
10. [Best Practices](#best-practices)

---

## What are Operators?

**Operators** are special symbols that tell Python to perform specific mathematical, logical, or other operations on values (operands).

**Components:**
- **Operand**: The value(s) that operators work on
- **Operator**: The symbol that performs the operation
- **Expression**: Combination of operands and operators

**Example:**
```python
5 + 3  # 5 and 3 are operands, + is the operator
```

**Types of Operators:**
1. Arithmetic (+, -, *, /, etc.)
2. Comparison (==, !=, <, >, etc.)
3. Logical (and, or, not)
4. Assignment (=, +=, -=, etc.)
5. Identity (is, is not)
6. Membership (in, not in)
7. Bitwise (&, |, ^, etc.)

---

## Arithmetic Operators

Perform mathematical operations on numbers.

### Addition (+)
```python
5 + 3        # 8
10.5 + 2.3  # 12.8
"Hello" + " " + "World"  # "Hello World" (string concatenation)
```

### Subtraction (-)
```python
10 - 4      # 6
15.5 - 3.2  # 12.3
```

### Multiplication (*)
```python
4 * 5       # 20
3.5 * 2     # 7.0
"Hi" * 3    # "HiHiHi" (string repetition)
```

### Division (/)
```python
10 / 2      # 5.0 (always returns float)
15 / 4      # 3.75
```

### Floor Division (//)
```python
10 // 3     # 3 (returns integer, rounds down)
15 // 4     # 3
-10 // 3    # -4 (rounds toward negative infinity)
```

### Modulo (%)
```python
10 % 3      # 1 (remainder)
15 % 4      # 3
20 % 5      # 0 (no remainder)
```

### Exponentiation (**)
```python
2 ** 3      # 8 (2 to the power of 3)
5 ** 2      # 25
10 ** 0.5   # 3.162... (square root)
```

---

## Comparison Operators

Compare two values and return `True` or `False`.

### Equal (==)
```python
5 == 5      # True
5 == 3      # False
"hello" == "hello"  # True
```

### Not Equal (!=)
```python
5 != 3      # True
5 != 5      # False
```

### Less Than (<)
```python
3 < 5       # True
10 < 5      # False
```

### Greater Than (>)
```python
5 > 3       # True
3 > 5       # False
```

### Less Than or Equal (<=)
```python
5 <= 5      # True
3 <= 5      # True
6 <= 5      # False
```

### Greater Than or Equal (>=)
```python
5 >= 5      # True
6 >= 5      # True
4 >= 5      # False
```

**Note:** Comparison operators can be chained:
```python
1 < 2 < 3   # True (equivalent to: 1 < 2 and 2 < 3)
```

---

## Logical Operators

Perform logical operations on boolean values.

### AND (and)
Returns `True` if both operands are `True`.

```python
True and True    # True
True and False   # False
False and True   # False
False and False  # False
```

**Truth Table:**
| A     | B     | A and B |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

**Short-circuit evaluation:**
- If first operand is `False`, second is not evaluated
- Returns first falsy value or last value

### OR (or)
Returns `True` if at least one operand is `True`.

```python
True or True     # True
True or False    # True
False or True    # True
False or False   # False
```

**Truth Table:**
| A     | B     | A or B |
|-------|-------|--------|
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

**Short-circuit evaluation:**
- If first operand is `True`, second is not evaluated
- Returns first truthy value or last value

### NOT (not)
Returns the opposite boolean value.

```python
not True     # False
not False    # True
not 0        # True
not 1        # False
```

---

## Assignment Operators

Assign values to variables, with optional operations.

### Basic Assignment (=)
```python
x = 5        # Assign 5 to x
```

### Addition Assignment (+=)
```python
x = 5
x += 3       # Equivalent to: x = x + 3
# x is now 8
```

### Subtraction Assignment (-=)
```python
x = 10
x -= 4       # Equivalent to: x = x - 4
# x is now 6
```

### Multiplication Assignment (*=)
```python
x = 5
x *= 3       # Equivalent to: x = x * 3
# x is now 15
```

### Division Assignment (/=)
```python
x = 10
x /= 2       # Equivalent to: x = x / 2
# x is now 5.0
```

### Floor Division Assignment (//=)
```python
x = 10
x //= 3      # Equivalent to: x = x // 3
# x is now 3
```

### Modulo Assignment (%=)
```python
x = 10
x %= 3       # Equivalent to: x = x % 3
# x is now 1
```

### Exponentiation Assignment (**=)
```python
x = 2
x **= 3      # Equivalent to: x = x ** 3
# x is now 8
```

---

## Identity Operators

Check if two variables refer to the same object in memory.

### IS (is)
```python
x = [1, 2, 3]
y = x
x is y       # True (same object)

a = [1, 2, 3]
b = [1, 2, 3]
a is b       # False (different objects, same values)
```

**Use cases:**
- Check for `None`: `x is None`
- Check for `True`/`False`: `x is True`
- Check object identity

### IS NOT (is not)
```python
x = [1, 2, 3]
y = [1, 2, 3]
x is not y   # True (different objects)
```

**Important:** Use `is`/`is not` for identity, `==`/`!=` for equality.

---

## Membership Operators

Check if a value exists in a sequence (string, list, tuple, etc.).

### IN (in)
```python
"a" in "apple"        # True
"x" in "apple"        # False
5 in [1, 2, 3, 4, 5]  # True
"name" in {"name": "Alice"}  # True (checks keys in dict)
```

### NOT IN (not in)
```python
"x" not in "apple"    # True
10 not in [1, 2, 3]   # True
```

---

## Bitwise Operators

Perform operations on binary representations of numbers (advanced topic).

### Bitwise AND (&)
```python
5 & 3        # 1 (binary: 101 & 011 = 001)
```

### Bitwise OR (|)
```python
5 | 3        # 7 (binary: 101 | 011 = 111)
```

### Bitwise XOR (^)
```python
5 ^ 3        # 6 (binary: 101 ^ 011 = 110)
```

### Bitwise NOT (~)
```python
~5           # -6 (inverts bits)
```

### Left Shift (<<)
```python
5 << 2       # 20 (binary: 101 << 2 = 10100)
```

### Right Shift (>>)
```python
20 >> 2      # 5 (binary: 10100 >> 2 = 101)
```

**Note:** Bitwise operators are less commonly used in beginner Python programming.

---

## Operator Precedence

When multiple operators are used, Python follows a specific order (precedence).

### Precedence Order (High to Low):
1. **Parentheses** `()` - Highest precedence
2. **Exponentiation** `**`
3. **Unary operators** `+x`, `-x`, `~x`, `not x`
4. **Multiplication, Division, Floor Division, Modulo** `*`, `/`, `//`, `%`
5. **Addition, Subtraction** `+`, `-`
6. **Bitwise shifts** `<<`, `>>`
7. **Bitwise AND** `&`
8. **Bitwise XOR** `^`
9. **Bitwise OR** `|`
10. **Comparison operators** `==`, `!=`, `<`, `>`, `<=`, `>=`, `is`, `is not`, `in`, `not in`
11. **Logical NOT** `not`
12. **Logical AND** `and`
13. **Logical OR** `or`
14. **Assignment operators** `=`, `+=`, `-=`, etc. - Lowest precedence

### Examples:
```python
2 + 3 * 4        # 14 (multiplication first)
(2 + 3) * 4      # 20 (parentheses override)
not True and False  # False (not has higher precedence)
not (True and False)  # True (parentheses change order)
```

**Best Practice:** Use parentheses to make precedence clear, even when not strictly necessary.

---

## Best Practices

1. **Use parentheses for clarity**
   ```python
   # Unclear
   result = a + b * c
   
   # Clear
   result = a + (b * c)
   ```

2. **Use `is` for None, `==` for values**
   ```python
   # Good
   if x is None:
       pass
   
   # Good
   if x == 5:
       pass
   ```

3. **Use assignment operators for brevity**
   ```python
   # Good
   x += 1
   
   # Also fine, but longer
   x = x + 1
   ```

4. **Be careful with floating-point comparisons**
   ```python
   # Problematic
   0.1 + 0.2 == 0.3  # False (floating-point precision)
   
   # Better
   abs(0.1 + 0.2 - 0.3) < 0.0001  # True
   ```

5. **Use `in` for membership checks**
   ```python
   # Good
   if item in my_list:
       pass
   
   # Less Pythonic
   if my_list.count(item) > 0:
       pass
   ```

---

## Common Mistakes to Avoid

1. **Confusing `=` and `==`**
   ```python
   # Wrong
   if x = 5:  # SyntaxError!
   
   # Correct
   if x == 5:
       pass
   ```

2. **Using `is` instead of `==` for values**
   ```python
   # Wrong (usually)
   if x is 5:  # May work for small integers, but unreliable
   
   # Correct
   if x == 5:
       pass
   ```

3. **Chaining assignment operators incorrectly**
   ```python
   # Wrong
   a = b += 1  # SyntaxError!
   
   # Correct
   b += 1
   a = b
   ```

4. **Forgetting operator precedence**
   ```python
   # Unexpected result
   result = 2 + 3 * 4  # 14, not 20
   
   # Clear
   result = (2 + 3) * 4  # 20
   ```

---

## Summary

- **Arithmetic operators** perform mathematical operations
- **Comparison operators** compare values (return True/False)
- **Logical operators** perform boolean logic (and, or, not)
- **Assignment operators** assign and modify values
- **Identity operators** check object identity (is, is not)
- **Membership operators** check membership (in, not in)
- **Operator precedence** determines evaluation order
- Use **parentheses** to clarify precedence
- Use **`is`** for None/identity, **`==`** for equality

**Remember**: Understanding operators is fundamental to writing Python code. Practice with different operators to become comfortable with them!

---

## Next Steps

Now that you understand operators:
1. Practice with the examples in this folder
2. Experiment with operator precedence
3. Try combining different operators
4. Move on to **05-input-output** to learn about input and output operations

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_arithmetic_operators.py`: Basic arithmetic operations - start here!
2. `02_comparison_operators.py`: Comparison and equality operators
3. `03_logical_operators.py`: Logical operations (and, or, not)
4. `04_assignment_operators.py`: Assignment and compound assignment
5. `05_identity_membership.py`: Identity (is) and membership (in) operators
6. `06_operator_precedence.py`: Understanding operator precedence

Run these files in order to see operators in action!
