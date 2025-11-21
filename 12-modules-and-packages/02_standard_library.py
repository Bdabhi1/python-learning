"""
Standard Library Modules in Python

This file demonstrates commonly used modules from Python's standard library.
Python comes with many built-in modules for common tasks.
"""

# ============================================================================
# 1. MATH MODULE
# ============================================================================
print("=" * 60)
print("1. MATH MODULE")
print("=" * 60)

import math

# Constants
print(f"  math.pi: {math.pi}")
print(f"  math.e: {math.e}")

# Basic functions
print(f"  math.sqrt(16): {math.sqrt(16)}")
print(f"  math.pow(2, 3): {math.pow(2, 3)}")
print(f"  math.abs(-5): {abs(-5)}")  # abs is built-in

# Rounding
print(f"  math.ceil(4.3): {math.ceil(4.3)}")
print(f"  math.floor(4.7): {math.floor(4.7)}")
print(f"  round(3.14159, 2): {round(3.14159, 2)}")

# Trigonometric functions
print(f"  math.sin(math.pi/2): {math.sin(math.pi/2):.2f}")
print(f"  math.cos(0): {math.cos(0)}")

print()  # Empty line


# ============================================================================
# 2. RANDOM MODULE
# ============================================================================
print("=" * 60)
print("2. RANDOM MODULE")
print("=" * 60)

import random

# Random integer
print(f"  random.randint(1, 10): {random.randint(1, 10)}")

# Random float
print(f"  random.random(): {random.random():.4f}")

# Random choice from sequence
choices = ['apple', 'banana', 'orange']
print(f"  random.choice({choices}): {random.choice(choices)}")

# Shuffle list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"  After shuffle: {numbers}")

# Random sample
sample = random.sample(range(1, 11), 3)
print(f"  random.sample(range(1,11), 3): {sample}")

print()  # Empty line


# ============================================================================
# 3. DATETIME MODULE
# ============================================================================
print("=" * 60)
print("3. DATETIME MODULE")
print("=" * 60)

from datetime import datetime, date, timedelta

# Current date and time
now = datetime.now()
print(f"  datetime.now(): {now}")

# Current date
today = date.today()
print(f"  date.today(): {today}")

# Create specific date
birthday = date(1990, 5, 15)
print(f"  date(1990, 5, 15): {birthday}")

# Date arithmetic
tomorrow = today + timedelta(days=1)
print(f"  tomorrow: {tomorrow}")

# Format date
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"  Formatted: {formatted}")

print()  # Empty line


# ============================================================================
# 4. OS MODULE
# ============================================================================
print("=" * 60)
print("4. OS MODULE")
print("=" * 60)

import os

# Current working directory
print(f"  os.getcwd(): {os.getcwd()}")

# List directory contents
print(f"  os.listdir('.'): {os.listdir('.')[:5]}...")  # First 5 items

# Check if path exists
print(f"  os.path.exists('README.md'): {os.path.exists('README.md')}")

# Join paths
path = os.path.join("folder", "subfolder", "file.txt")
print(f"  os.path.join(...): {path}")

# Get file size
if os.path.exists("README.md"):
    size = os.path.getsize("README.md")
    print(f"  os.path.getsize('README.md'): {size} bytes")

print()  # Empty line


# ============================================================================
# 5. SYS MODULE
# ============================================================================
print("=" * 60)
print("5. SYS MODULE")
print("=" * 60)

import sys

# Python version
print(f"  sys.version: {sys.version[:50]}...")

# Command-line arguments
print(f"  sys.argv: {sys.argv}")

# Module search path
print(f"  sys.path (first 3):")
for i, path in enumerate(sys.path[:3], 1):
    print(f"    {i}. {path}")

# Exit program
# sys.exit(0)  # Uncomment to exit

print()  # Empty line


# ============================================================================
# 6. JSON MODULE
# ============================================================================
print("=" * 60)
print("6. JSON MODULE")
print("=" * 60)

import json

# Convert Python to JSON string
data = {"name": "Alice", "age": 25, "city": "New York"}
json_str = json.dumps(data)
print(f"  json.dumps(data): {json_str}")

# Convert JSON string to Python
data_from_json = json.loads(json_str)
print(f"  json.loads(json_str): {data_from_json}")

# Pretty print
pretty = json.dumps(data, indent=2)
print(f"  Pretty JSON:\n{pretty}")

print()  # Empty line


# ============================================================================
# 7. COLLECTIONS MODULE
# ============================================================================
print("=" * 60)
print("7. COLLECTIONS MODULE")
print("=" * 60)

from collections import Counter, defaultdict, deque

# Counter
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(words)
print(f"  Counter({words}): {counter}")
print(f"  Most common: {counter.most_common(2)}")

# Defaultdict
dd = defaultdict(int)
dd['a'] += 1
print(f"  defaultdict: {dict(dd)}")

# Deque
dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
print(f"  deque: {list(dq)}")

print()  # Empty line


# ============================================================================
# 8. STRING MODULE
# ============================================================================
print("=" * 60)
print("8. STRING MODULE")
print("=" * 60)

import string

# String constants
print(f"  string.ascii_letters: {string.ascii_letters}")
print(f"  string.digits: {string.digits}")
print(f"  string.punctuation: {string.punctuation}")

# Template
template = string.Template("Hello, $name!")
result = template.substitute(name="Alice")
print(f"  Template: {result}")

print()  # Empty line


# ============================================================================
# 9. ITERTOOLS MODULE
# ============================================================================
print("=" * 60)
print("9. ITERTOOLS MODULE")
print("=" * 60)

from itertools import count, cycle, repeat, combinations

# Count
print("  count(10, 2) - first 5:")
for i, num in enumerate(count(10, 2)):
    if i >= 5:
        break
    print(f"    {num}")

# Combinations
items = ['a', 'b', 'c']
combs = list(combinations(items, 2))
print(f"  combinations({items}, 2): {combs}")

print()  # Empty line


# ============================================================================
# 10. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("10. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Calculate circle area
import math
radius = 5
area = math.pi * radius ** 2
print(f"  Circle area (r={radius}): {area:.2f}")

# Example 2: Generate random password
import random
import string
password = ''.join(random.choice(string.ascii_letters + string.digits) 
                   for _ in range(8))
print(f"  Random password: {password}")

# Example 3: Format current date
from datetime import datetime
formatted_date = datetime.now().strftime("%B %d, %Y")
print(f"  Today's date: {formatted_date}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("STANDARD LIBRARY MODULES SUMMARY:")
print("=" * 60)
print("Key Modules:")
print("  - math: Mathematical functions and constants")
print("  - random: Random number generation")
print("  - datetime: Date and time operations")
print("  - os: Operating system interface")
print("  - sys: System-specific parameters")
print("  - json: JSON data handling")
print("  - collections: Specialized data structures")
print("  - string: String constants and utilities")
print("  - itertools: Iterator functions")
print("\nRemember:")
print("  - Python has a rich standard library")
print("  - No need to install these modules")
print("  - Always available in Python")
print("  - Explore documentation for more modules")
print("=" * 60)

