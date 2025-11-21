# Regular Expressions in Python

Regular expressions (regex) are powerful pattern-matching tools that allow you to search, match, and manipulate text based on patterns. Python's `re` module provides comprehensive regex functionality.

## Table of Contents
1. [What are Regular Expressions?](#what-are-regular-expressions)
2. [Basic Pattern Matching](#basic-pattern-matching)
3. [Regex Metacharacters](#regex-metacharacters)
4. [Character Classes](#character-classes)
5. [Quantifiers](#quantifiers)
6. [Groups and Capturing](#groups-and-capturing)
7. [Lookahead and Lookbehind](#lookahead-and-lookbehind)
8. [Common Patterns](#common-patterns)
9. [Best Practices](#best-practices)

---

## What are Regular Expressions?

**Regular expressions** are sequences of characters that define a search pattern. They're used for:
- **Pattern matching**: Find text that matches a pattern
- **Text validation**: Check if text follows a format
- **Text extraction**: Extract specific parts of text
- **Text replacement**: Replace matching patterns

**Python's `re` module:**
- `re.search()`: Find first match
- `re.match()`: Match at start of string
- `re.findall()`: Find all matches
- `re.sub()`: Replace matches
- `re.compile()`: Compile pattern for reuse

---

## Basic Pattern Matching

### Simple Search

```python
import re

text = "Hello, World!"
pattern = "World"

match = re.search(pattern, text)
if match:
    print("Found:", match.group())
```

### Using `re.match()`

```python
import re

text = "Hello, World!"
pattern = "Hello"

match = re.match(pattern, text)  # Only matches at start
if match:
    print("Matched:", match.group())
```

### Using `re.findall()`

```python
import re

text = "The cat sat on the mat"
pattern = "the"

matches = re.findall(pattern, text, re.IGNORECASE)
print(matches)  # ['The', 'the']
```

---

## Regex Metacharacters

### Special Characters

```python
import re

# . (dot) - matches any character except newline
text = "cat bat rat"
pattern = r".at"  # matches cat, bat, rat
matches = re.findall(pattern, text)

# ^ - matches start of string
pattern = r"^Hello"  # matches "Hello" at start

# $ - matches end of string
pattern = r"World!$"  # matches "World!" at end

# \ - escape special characters
pattern = r"\."  # matches literal dot
```

### Common Metacharacters

- `.` - Any character (except newline)
- `^` - Start of string
- `$` - End of string
- `*` - Zero or more
- `+` - One or more
- `?` - Zero or one
- `|` - OR operator
- `\` - Escape character

---

## Character Classes

### Basic Character Classes

```python
import re

# [abc] - matches a, b, or c
pattern = r"[abc]"
text = "apple"
matches = re.findall(pattern, text)  # ['a', 'p', 'p', 'l', 'e'] (only a)

# [a-z] - matches lowercase letters
pattern = r"[a-z]"

# [A-Z] - matches uppercase letters
pattern = r"[A-Z]"

# [0-9] - matches digits
pattern = r"[0-9]"

# [^abc] - matches anything except a, b, or c
pattern = r"[^abc]"
```

### Predefined Character Classes

```python
import re

# \d - digit [0-9]
pattern = r"\d"

# \D - non-digit [^0-9]
pattern = r"\D"

# \w - word character [a-zA-Z0-9_]
pattern = r"\w"

# \W - non-word character
pattern = r"\W"

# \s - whitespace
pattern = r"\s"

# \S - non-whitespace
pattern = r"\S"
```

---

## Quantifiers

### Basic Quantifiers

```python
import re

# * - zero or more
pattern = r"a*"  # matches "", "a", "aa", "aaa", ...

# + - one or more
pattern = r"a+"  # matches "a", "aa", "aaa", ...

# ? - zero or one
pattern = r"a?"  # matches "", "a"

# {n} - exactly n times
pattern = r"a{3}"  # matches "aaa"

# {n,m} - between n and m times
pattern = r"a{2,4}"  # matches "aa", "aaa", "aaaa"
```

### Greedy vs Non-Greedy

```python
import re

text = "<div>content</div>"

# Greedy (default)
pattern = r"<.*>"  # matches entire string
match = re.search(pattern, text)

# Non-greedy
pattern = r"<.*?>"  # matches shortest possible
match = re.search(pattern, text)
```

---

## Groups and Capturing

### Basic Groups

```python
import re

text = "John Doe, Jane Smith"
pattern = r"(\w+) (\w+)"  # Two groups

match = re.search(pattern, text)
if match:
    print(match.group(0))  # Entire match
    print(match.group(1))  # First group: "John"
    print(match.group(2))  # Second group: "Doe"
```

### Named Groups

```python
import re

text = "John Doe"
pattern = r"(?P<first>\w+) (?P<last>\w+)"

match = re.search(pattern, text)
if match:
    print(match.group('first'))  # "John"
    print(match.group('last'))   # "Doe"
```

### Non-Capturing Groups

```python
import re

# (?:...) - non-capturing group
pattern = r"(?:Mr|Mrs|Ms)\. (\w+)"
text = "Mr. Smith"
match = re.search(pattern, text)
# match.group(1) is "Smith" (not "Mr")
```

---

## Lookahead and Lookbehind

### Positive Lookahead

```python
import re

# (?=...) - positive lookahead
pattern = r"\w+(?=@)"  # word before @
text = "email@example.com"
match = re.search(pattern, text)  # matches "email"
```

### Negative Lookahead

```python
import re

# (?!...) - negative lookahead
pattern = r"\d+(?!px)"  # number not followed by "px"
```

### Lookbehind

```python
import re

# (?<=...) - positive lookbehind
pattern = r"(?<=\$)\d+"  # number after $
text = "Price: $100"
match = re.search(pattern, text)  # matches "100"

# (?<!...) - negative lookbehind
pattern = r"(?<!\$)\d+"  # number not after $
```

---

## Common Patterns

### Email Validation

```python
import re

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email = "user@example.com"

if re.match(pattern, email):
    print("Valid email")
```

### Phone Number

```python
import re

pattern = r'^\+?1?\d{9,15}$'
phone = "+1234567890"

if re.match(pattern, phone):
    print("Valid phone")
```

### URL Extraction

```python
import re

text = "Visit https://example.com for more info"
pattern = r'https?://[^\s]+'
urls = re.findall(pattern, text)
```

### Date Extraction

```python
import re

text = "Date: 2024-01-15"
pattern = r'\d{4}-\d{2}-\d{2}'
date = re.search(pattern, text)
```

---

## Best Practices

### 1. Use Raw Strings

```python
# Good
pattern = r"\d+"

# Less preferred
pattern = "\\d+"
```

### 2. Compile Patterns for Reuse

```python
import re

pattern = re.compile(r'\d+')
matches = pattern.findall(text)
```

### 3. Handle Match Objects

```python
import re

match = re.search(pattern, text)
if match:
    result = match.group()
else:
    result = None
```

### 4. Use Appropriate Flags

```python
import re

# re.IGNORECASE - case insensitive
# re.MULTILINE - ^ and $ match line boundaries
# re.DOTALL - . matches newline
pattern = r"hello"
matches = re.findall(pattern, text, re.IGNORECASE)
```

---

## Common Mistakes to Avoid

1. **Forgetting to escape special characters**
   ```python
   # Wrong
   pattern = "."
   
   # Correct
   pattern = r"\."
   ```

2. **Not using raw strings**
   ```python
   # Problematic
   pattern = "\\d+"
   
   # Better
   pattern = r"\d+"
   ```

3. **Not checking if match exists**
   ```python
   # Wrong
   match = re.search(pattern, text)
   result = match.group()  # Error if no match
   
   # Correct
   match = re.search(pattern, text)
   if match:
       result = match.group()
   ```

---

## Summary

- **Regular expressions** are powerful pattern-matching tools
- Use `re.search()`, `re.match()`, `re.findall()`, `re.sub()`
- **Metacharacters** define patterns (., ^, $, *, +, ?, etc.)
- **Character classes** match sets of characters
- **Quantifiers** specify repetition
- **Groups** capture parts of matches
- **Lookahead/lookbehind** for advanced matching
- Always use **raw strings** (r"...") for patterns

**Remember**: Regular expressions are powerful but can be complex. Start simple and build up!

---

## Next Steps

Now that you understand regular expressions:
1. Practice with the examples in this folder
2. Create patterns for your use cases
3. Use regex for text validation and extraction
4. Move on to **22-date-and-time** to learn about date/time handling

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_basic_patterns.py`: Basic pattern matching with re module - start here!
2. `02_metacharacters.py`: Understanding regex metacharacters
3. `03_character_classes.py`: Character classes and predefined classes
4. `04_quantifiers_groups.py`: Quantifiers and capturing groups
5. `05_advanced_patterns.py`: Lookahead, lookbehind, and advanced features
6. `06_practical_examples.py`: Real-world regex patterns and examples

Run these files in order to see regular expressions in action!

