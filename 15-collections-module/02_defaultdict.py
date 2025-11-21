"""
defaultdict in Python Collections Module

This file demonstrates how to use defaultdict, a dictionary with default values.
"""

from collections import defaultdict

# ============================================================================
# 1. CREATING A DEFAULTDICT
# ============================================================================
print("=" * 60)
print("1. CREATING A DEFAULTDICT")
print("=" * 60)

# Default factory: int (default value is 0)
dd_int = defaultdict(int)
print(f"  defaultdict(int): {dict(dd_int)}")
print(f"  Accessing missing key 'a': {dd_int['a']}")
print(f"  After access: {dict(dd_int)}")

# Default factory: list (default value is empty list)
dd_list = defaultdict(list)
print(f"\n  defaultdict(list): {dict(dd_list)}")
print(f"  Accessing missing key 'fruits': {dd_list['fruits']}")
print(f"  After access: {dict(dd_list)}")

# Default factory: set (default value is empty set)
dd_set = defaultdict(set)
print(f"\n  defaultdict(set): {dict(dd_set)}")
print(f"  Accessing missing key 'colors': {dd_set['colors']}")
print(f"  After access: {dict(dd_set)}")

# Default factory: str (default value is empty string)
dd_str = defaultdict(str)
print(f"\n  defaultdict(str): {dict(dd_str)}")
print(f"  Accessing missing key 'name': '{dd_str['name']}'")

print()  # Empty line


# ============================================================================
# 2. GROUPING ITEMS
# ============================================================================
print("=" * 60)
print("2. GROUPING ITEMS")
print("=" * 60)

# Group items by category
items = [
    ('fruit', 'apple'),
    ('fruit', 'banana'),
    ('vegetable', 'carrot'),
    ('fruit', 'orange'),
    ('vegetable', 'broccoli')
]

grouped = defaultdict(list)
for category, item in items:
    grouped[category].append(item)

print(f"  Items: {items}")
print(f"  Grouped: {dict(grouped)}")

# Without defaultdict (more verbose)
grouped_manual = {}
for category, item in items:
    if category not in grouped_manual:
        grouped_manual[category] = []
    grouped_manual[category].append(item)
print(f"  Manual grouping: {dict(grouped_manual)}")

print()  # Empty line


# ============================================================================
# 3. COUNTING OCCURRENCES
# ============================================================================
print("=" * 60)
print("3. COUNTING OCCURRENCES")
print("=" * 60)

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = defaultdict(int)

for word in words:
    counter[word] += 1

print(f"  Words: {words}")
print(f"  Counts: {dict(counter)}")

# Without defaultdict (more verbose)
counter_manual = {}
for word in words:
    if word not in counter_manual:
        counter_manual[word] = 0
    counter_manual[word] += 1
print(f"  Manual counting: {dict(counter_manual)}")

print()  # Empty line


# ============================================================================
# 4. BUILDING INDEXES
# ============================================================================
print("=" * 60)
print("4. BUILDING INDEXES")
print("=" * 60)

# Index words by first letter
words = ['apple', 'banana', 'apricot', 'blueberry', 'cherry', 'coconut']
index = defaultdict(list)

for word in words:
    first_letter = word[0]
    index[first_letter].append(word)

print(f"  Words: {words}")
print(f"  Index by first letter: {dict(index)}")

print()  # Empty line


# ============================================================================
# 5. COLLECTING UNIQUE VALUES
# ============================================================================
print("=" * 60)
print("5. COLLECTING UNIQUE VALUES")
print("=" * 60)

# Collect unique tags for each category
items = [
    ('fruit', 'red'),
    ('fruit', 'yellow'),
    ('vegetable', 'green'),
    ('fruit', 'red'),  # duplicate
    ('vegetable', 'orange')
]

tags_by_category = defaultdict(set)
for category, tag in items:
    tags_by_category[category].add(tag)

print(f"  Items: {items}")
print(f"  Unique tags by category: {dict(tags_by_category)}")

print()  # Empty line


# ============================================================================
# 6. CUSTOM DEFAULT FACTORY
# ============================================================================
print("=" * 60)
print("6. CUSTOM DEFAULT FACTORY")
print("=" * 60)

# Custom default value function
def default_value():
    return "Not Found"

dd_custom = defaultdict(default_value)
dd_custom['existing'] = 'Found'
print(f"  Existing key: {dd_custom['existing']}")
print(f"  Missing key: {dd_custom['missing']}")

# Lambda as default factory
dd_lambda = defaultdict(lambda: 'Unknown')
print(f"\n  Missing key with lambda: {dd_lambda['name']}")

print()  # Empty line


# ============================================================================
# 7. NESTED DICTIONARIES
# ============================================================================
print("=" * 60)
print("7. NESTED DICTIONARIES")
print("=" * 60)

# Create nested defaultdict
nested = defaultdict(lambda: defaultdict(int))

nested['group1']['item1'] = 1
nested['group1']['item2'] = 2
nested['group2']['item1'] = 3

print(f"  Nested defaultdict: {dict(nested)}")
print(f"  Access nested: nested['group1']['item1'] = {nested['group1']['item1']}")
print(f"  Access new nested: nested['group3']['new'] = {nested['group3']['new']}")

print()  # Empty line


# ============================================================================
# 8. CONFIGURATION WITH DEFAULTS
# ============================================================================
print("=" * 60)
print("8. CONFIGURATION WITH DEFAULTS")
print("=" * 60)

# Configuration with defaults
default_config = defaultdict(lambda: 'default_value')
default_config.update({
    'theme': 'dark',
    'language': 'en',
    'font_size': 12
})

# User can override defaults
user_config = {
    'theme': 'light',
    'notifications': True
}

# Merge (user config overrides defaults)
config = defaultdict(lambda: 'default_value', default_config)
config.update(user_config)

print(f"  Default config: {dict(default_config)}")
print(f"  User config: {user_config}")
print(f"  Final config: {dict(config)}")
print(f"  Accessing missing key: config['missing'] = '{config['missing']}'")

print()  # Empty line


# ============================================================================
# 9. PRACTICAL EXAMPLE: STUDENT GRADES
# ============================================================================
print("=" * 60)
print("9. PRACTICAL EXAMPLE: STUDENT GRADES")
print("=" * 60)

# Group students by grade
students = [
    ('Alice', 'A'),
    ('Bob', 'B'),
    ('Charlie', 'A'),
    ('David', 'C'),
    ('Eve', 'A')
]

students_by_grade = defaultdict(list)
for name, grade in students:
    students_by_grade[grade].append(name)

print(f"  Students: {students}")
print(f"  Students by grade: {dict(students_by_grade)}")

# Calculate average scores by subject
scores = [
    ('Math', 85),
    ('Math', 90),
    ('Science', 78),
    ('Math', 88),
    ('Science', 92)
]

scores_by_subject = defaultdict(list)
for subject, score in scores:
    scores_by_subject[subject].append(score)

averages = {subject: sum(scores) / len(scores) 
            for subject, scores in scores_by_subject.items()}

print(f"\n  Scores: {scores}")
print(f"  Scores by subject: {dict(scores_by_subject)}")
print(f"  Averages: {averages}")

print()  # Empty line


# ============================================================================
# 10. COMPARISON WITH REGULAR DICT
# ============================================================================
print("=" * 60)
print("10. COMPARISON WITH REGULAR DICT")
print("=" * 60)

# With defaultdict (clean)
dd = defaultdict(list)
dd['key1'].append('value1')
print(f"  defaultdict: {dict(dd)}")

# With regular dict (verbose)
regular = {}
if 'key1' not in regular:
    regular['key1'] = []
regular['key1'].append('value1')
print(f"  Regular dict: {regular}")

# Using get() method (still verbose)
regular2 = {}
regular2.setdefault('key1', []).append('value1')
print(f"  Regular dict with setdefault: {regular2}")

print("\n  defaultdict is cleaner and more readable!")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("DEFAULTDICT SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - defaultdict provides default values for missing keys")
print("  - No KeyError when accessing missing keys")
print("  - Common factories: int, list, set, str")
print("  - Perfect for grouping and counting")
print("  - Cleaner code than regular dict with checks")
print("  - Can use custom factory functions")
print("=" * 60)

