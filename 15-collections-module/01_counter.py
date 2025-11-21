"""
Counter in Python Collections Module

This file demonstrates how to use Counter for counting hashable objects.
Counter is a dictionary subclass designed for counting.
"""

from collections import Counter

# ============================================================================
# 1. CREATING A COUNTER
# ============================================================================
print("=" * 60)
print("1. CREATING A COUNTER")
print("=" * 60)

# From a list
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter1 = Counter(fruits)
print(f"  Counter from list: {counter1}")
print(f"  Result: {dict(counter1)}")

# From a string
text = "hello"
counter2 = Counter(text)
print(f"\n  Counter from string '{text}': {dict(counter2)}")

# From a dictionary
counter3 = Counter({'red': 4, 'blue': 2, 'green': 1})
print(f"\n  Counter from dict: {dict(counter3)}")

# Empty counter
counter4 = Counter()
print(f"\n  Empty counter: {dict(counter4)}")

print()  # Empty line


# ============================================================================
# 2. ACCESSING COUNTS
# ============================================================================
print("=" * 60)
print("2. ACCESSING COUNTS")
print("=" * 60)

counter = Counter(['apple', 'banana', 'apple', 'orange'])

# Access existing key
print(f"  counter['apple']: {counter['apple']}")

# Access non-existing key (returns 0, no KeyError)
print(f"  counter['grape']: {counter['grape']}")

# Get all elements
print(f"  All elements: {list(counter.elements())}")

# Get unique elements
print(f"  Unique elements: {list(counter.keys())}")

# Get counts
print(f"  Counts: {list(counter.values())}")

print()  # Empty line


# ============================================================================
# 3. UPDATING COUNTER
# ============================================================================
print("=" * 60)
print("3. UPDATING COUNTER")
print("=" * 60)

counter = Counter(['apple', 'banana', 'apple'])
print(f"  Initial: {dict(counter)}")

# Update with iterable
counter.update(['apple', 'grape'])
print(f"  After update(['apple', 'grape']): {dict(counter)}")

# Update with another Counter
counter.update(Counter({'apple': 2, 'orange': 1}))
print(f"  After update(Counter): {dict(counter)}")

# Update with dictionary
counter.update({'banana': 3})
print(f"  After update(dict): {dict(counter)}")

print()  # Empty line


# ============================================================================
# 4. MOST COMMON ELEMENTS
# ============================================================================
print("=" * 60)
print("4. MOST COMMON ELEMENTS")
print("=" * 60)

counter = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'grape'])

# Most common (all)
print(f"  Most common (all): {counter.most_common()}")

# Most common (top 2)
print(f"  Most common (top 2): {counter.most_common(2)}")

# Most common (top 1)
print(f"  Most common (top 1): {counter.most_common(1)}")

print()  # Empty line


# ============================================================================
# 5. SUBTRACTING COUNTS
# ============================================================================
print("=" * 60)
print("5. SUBTRACTING COUNTS")
print("=" * 60)

counter = Counter(['apple', 'banana', 'apple', 'orange'])
print(f"  Initial: {dict(counter)}")

# Subtract with iterable
counter.subtract(['apple', 'banana'])
print(f"  After subtract(['apple', 'banana']): {dict(counter)}")

# Subtract can result in negative counts
counter.subtract(['apple', 'apple'])
print(f"  After subtract(['apple', 'apple']): {dict(counter)}")

print()  # Empty line


# ============================================================================
# 6. ARITHMETIC OPERATIONS
# ============================================================================
print("=" * 60)
print("6. ARITHMETIC OPERATIONS")
print("=" * 60)

counter1 = Counter(['a', 'b', 'c', 'a'])
counter2 = Counter(['a', 'b', 'b', 'd'])

print(f"  Counter1: {dict(counter1)}")
print(f"  Counter2: {dict(counter2)}")

# Addition
result = counter1 + counter2
print(f"  Addition (counter1 + counter2): {dict(result)}")

# Subtraction (keeps only positive counts)
result = counter1 - counter2
print(f"  Subtraction (counter1 - counter2): {dict(result)}")

# Intersection (minimum of corresponding counts)
result = counter1 & counter2
print(f"  Intersection (counter1 & counter2): {dict(result)}")

# Union (maximum of corresponding counts)
result = counter1 | counter2
print(f"  Union (counter1 | counter2): {dict(result)}")

print()  # Empty line


# ============================================================================
# 7. COUNTING WORDS IN TEXT
# ============================================================================
print("=" * 60)
print("7. COUNTING WORDS IN TEXT")
print("=" * 60)

text = "the quick brown fox jumps over the lazy dog the dog"
words = text.split()
word_count = Counter(words)

print(f"  Text: '{text}'")
print(f"  Word counts: {dict(word_count)}")
print(f"  Most common 3 words: {word_count.most_common(3)}")

print()  # Empty line


# ============================================================================
# 8. COUNTING CHARACTERS
# ============================================================================
print("=" * 60)
print("8. COUNTING CHARACTERS")
print("=" * 60)

text = "mississippi"
char_count = Counter(text)

print(f"  Text: '{text}'")
print(f"  Character counts: {dict(char_count)}")
print(f"  Most common 3 characters: {char_count.most_common(3)}")

print()  # Empty line


# ============================================================================
# 9. FINDING DUPLICATES
# ============================================================================
print("=" * 60)
print("9. FINDING DUPLICATES")
print("=" * 60)

items = [1, 2, 3, 2, 4, 3, 5, 3, 2]
counter = Counter(items)

# Find duplicates (count > 1)
duplicates = {item: count for item, count in counter.items() if count > 1}
print(f"  Items: {items}")
print(f"  Duplicates: {duplicates}")

print()  # Empty line


# ============================================================================
# 10. PRACTICAL EXAMPLE: VOTING SYSTEM
# ============================================================================
print("=" * 60)
print("10. PRACTICAL EXAMPLE: VOTING SYSTEM")
print("=" * 60)

votes = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice', 'Bob', 'Alice']
vote_count = Counter(votes)

print(f"  Votes: {votes}")
print(f"  Vote counts: {dict(vote_count)}")
print(f"  Winner: {vote_count.most_common(1)[0][0]} with {vote_count.most_common(1)[0][1]} votes")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("COUNTER SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Counter is a dict subclass for counting")
print("  - Accessing missing keys returns 0 (no KeyError)")
print("  - Use update() to add counts")
print("  - Use subtract() to decrease counts")
print("  - Use most_common(n) to get top n elements")
print("  - Supports arithmetic operations (+, -, &, |)")
print("  - Perfect for counting frequencies")
print("=" * 60)

