"""
Practical String Manipulation Examples

This file demonstrates real-world examples of string manipulation for
common programming tasks.
"""

# ============================================================================
# 1. TEXT PROCESSING UTILITIES
# ============================================================================
print("=" * 60)
print("1. TEXT PROCESSING UTILITIES")
print("=" * 60)

def clean_text(text):
    """Remove extra whitespace and normalize text."""
    words = text.split()
    return " ".join(words)

text = "  Hello    World   Python  "
cleaned = clean_text(text)
print(f"  Original: '{text}'")
print(f"  Cleaned: '{cleaned}'")

def capitalize_sentences(text):
    """Capitalize first letter of each sentence."""
    sentences = text.split(". ")
    capitalized = ". ".join(s.capitalize() for s in sentences)
    return capitalized

text = "hello world. python is great. learn programming."
result = capitalize_sentences(text)
print(f"  Original: '{text}'")
print(f"  Capitalized: '{result}'")

print()  # Empty line


# ============================================================================
# 2. DATA VALIDATION
# ============================================================================
print("=" * 60)
print("2. DATA VALIDATION")
print("=" * 60)

def validate_username(username):
    """Validate username (3-20 chars, alphanumeric and underscore)."""
    if not username:
        return False, "Username cannot be empty"
    if len(username) < 3:
        return False, "Username must be at least 3 characters"
    if len(username) > 20:
        return False, "Username must be at most 20 characters"
    if not username.replace("_", "").isalnum():
        return False, "Username can only contain letters, numbers, and underscore"
    return True, "Valid username"

test_usernames = ["alice", "ab", "user_123", "user-name"]
for username in test_usernames:
    valid, message = validate_username(username)
    print(f"  '{username}': {message}")

print()  # Empty line


# ============================================================================
# 3. TEXT FORMATTING
# ============================================================================
print("=" * 60)
print("3. TEXT FORMATTING")
print("=" * 60)

def format_receipt(items, tax_rate=0.1):
    """Format a receipt with items and totals."""
    lines = ["RECEIPT", "=" * 40]
    subtotal = 0
    
    for item, price, quantity in items:
        line_total = price * quantity
        subtotal += line_total
        lines.append(f"{item:20s} {quantity:3d} x ${price:6.2f} = ${line_total:6.2f}")
    
    lines.append("-" * 40)
    lines.append(f"{'Subtotal':30s} ${subtotal:6.2f}")
    tax = subtotal * tax_rate
    lines.append(f"{'Tax':30s} ${tax:6.2f}")
    lines.append(f"{'Total':30s} ${subtotal + tax:6.2f}")
    
    return "\n".join(lines)

items = [
    ("Apple", 1.50, 3),
    ("Banana", 0.75, 5),
    ("Orange", 2.00, 2)
]
print(format_receipt(items))

print()  # Empty line


# ============================================================================
# 4. TEXT ANALYSIS
# ============================================================================
print("=" * 60)
print("4. TEXT ANALYSIS")
print("=" * 60)

def analyze_text(text):
    """Analyze text and return statistics."""
    words = text.split()
    chars = len(text)
    chars_no_spaces = len(text.replace(" ", ""))
    sentences = text.count(".") + text.count("!") + text.count("?")
    
    return {
        "characters": chars,
        "characters_no_spaces": chars_no_spaces,
        "words": len(words),
        "sentences": sentences,
        "average_word_length": sum(len(w) for w in words) / len(words) if words else 0
    }

text = """Python is a great language. It's easy to learn!
Programming is fun. Keep learning."""
stats = analyze_text(text)
print("  Text analysis:")
for key, value in stats.items():
    print(f"    {key}: {value}")

print()  # Empty line


# ============================================================================
# 5. STRING TRANSFORMATIONS
# ============================================================================
print("=" * 60)
print("5. STRING TRANSFORMATIONS")
print("=" * 60)

def reverse_words(text):
    """Reverse the order of words in a sentence."""
    words = text.split()
    return " ".join(reversed(words))

text = "Hello World Python"
print(f"  Original: '{text}'")
print(f"  Reversed words: '{reverse_words(text)}'")

def extract_initials(name):
    """Extract initials from full name."""
    return "".join(word[0].upper() for word in name.split())

name = "John Doe Smith"
print(f"  Name: '{name}'")
print(f"  Initials: {extract_initials(name)}")

print()  # Empty line


# ============================================================================
# 6. DATA EXTRACTION
# ============================================================================
print("=" * 60)
print("6. DATA EXTRACTION")
print("=" * 60)

def extract_emails(text):
    """Extract email addresses from text."""
    import re
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

text = "Contact alice@example.com or bob@test.org for more info."
emails = extract_emails(text)
print(f"  Text: '{text}'")
print(f"  Emails: {emails}")

def extract_phone_numbers(text):
    """Extract phone numbers from text."""
    import re
    pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    return re.findall(pattern, text)

text = "Call 123-456-7890 or 987.654.3210 for support."
phones = extract_phone_numbers(text)
print(f"  Text: '{text}'")
print(f"  Phone numbers: {phones}")

print()  # Empty line


# ============================================================================
# 7. TEXT SANITIZATION
# ============================================================================
print("=" * 60)
print("7. TEXT SANITIZATION")
print("=" * 60)

def sanitize_filename(filename):
    """Sanitize filename by removing invalid characters."""
    import string
    valid_chars = "-_.() " + string.ascii_letters + string.digits
    sanitized = "".join(c if c in valid_chars else "_" for c in filename)
    return sanitized.strip()

filenames = ["my file.txt", "file<>name?.txt", "file:name|.txt"]
for filename in filenames:
    print(f"  '{filename}' -> '{sanitize_filename(filename)}'")

def normalize_whitespace(text):
    """Normalize all whitespace to single spaces."""
    import re
    return re.sub(r'\s+', ' ', text).strip()

text = "Hello    World\n\nPython\t\tProgramming"
normalized = normalize_whitespace(text)
print(f"  Original: '{text}'")
print(f"  Normalized: '{normalized}'")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL STRING EXAMPLES SUMMARY:")
print("=" * 60)
print("Key Applications:")
print("  - Text processing: cleaning, normalizing, formatting")
print("  - Data validation: checking format, length, content")
print("  - Text formatting: receipts, tables, reports")
print("  - Text analysis: word count, statistics")
print("  - String transformations: reversing, extracting")
print("  - Data extraction: emails, phone numbers, URLs")
print("  - Text sanitization: cleaning filenames, removing invalid chars")
print("\nRemember:")
print("  - Combine multiple string methods for complex operations")
print("  - Use regular expressions for pattern matching")
print("  - Always validate and sanitize user input")
print("=" * 60)

