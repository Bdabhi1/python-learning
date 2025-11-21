"""
Practical Iterator and Generator Examples

This file demonstrates real-world examples using iterators and generators.
"""

# ============================================================================
# 1. READING LARGE FILES
# ============================================================================
print("=" * 60)
print("1. READING LARGE FILES")
print("=" * 60)

def read_large_file(filename):
    """Generator to read file line by line"""
    with open(filename, 'w') as f:  # Create sample file
        f.write("Line 1\nLine 2\nLine 3\n")
    
    with open(filename) as f:
        for line in f:
            yield line.strip()

print("  Reading file line by line:")
for line in read_large_file('sample.txt'):
    print(f"    {line}")

print()  # Empty line


# ============================================================================
# 2. PIPELINE PATTERN
# ============================================================================
print("=" * 60)
print("2. PIPELINE PATTERN")
print("=" * 60)

def numbers():
    for i in range(10):
        yield i

def square(nums):
    for num in nums:
        yield num ** 2

def even(nums):
    for num in nums:
        if num % 2 == 0:
            yield num

# Chain generators
pipeline = even(square(numbers()))
print(f"  Pipeline result: {list(pipeline)}")

print()  # Empty line


# ============================================================================
# 3. PAGINATION
# ============================================================================
print("=" * 60)
print("3. PAGINATION")
print("=" * 60)

def paginate(items, page_size):
    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]

items = list(range(20))
pages = paginate(items, 5)

print("  Pages:")
for i, page in enumerate(pages, 1):
    print(f"    Page {i}: {page}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL EXAMPLES SUMMARY:")
print("=" * 60)
print("Iterators and generators are perfect for:")
print("  - Processing large datasets")
print("  - Creating data pipelines")
print("  - Pagination and chunking")
print("  - Memory-efficient operations")
print("=" * 60)

