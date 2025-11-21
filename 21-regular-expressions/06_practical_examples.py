"""
Practical Regular Expression Examples

This file demonstrates real-world regex patterns and use cases.
"""

import re

# ============================================================================
# 1. EMAIL VALIDATION
# ============================================================================
print("=" * 60)
print("1. EMAIL VALIDATION")
print("=" * 60)

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

emails = ["user@example.com", "invalid.email", "test@domain.co.uk"]
for email in emails:
    is_valid = bool(re.match(pattern, email))
    print(f"  {email}: {'Valid' if is_valid else 'Invalid'}")

print()  # Empty line


# ============================================================================
# 2. PHONE NUMBER EXTRACTION
# ============================================================================
print("=" * 60)
print("2. PHONE NUMBER EXTRACTION")
print("=" * 60)

text = "Call me at 555-1234 or (555) 987-6543"
pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'

matches = re.findall(pattern, text)
print(f"  Text: {text}")
print(f"  Phone numbers: {matches}")

print()  # Empty line


# ============================================================================
# 3. URL EXTRACTION
# ============================================================================
print("=" * 60)
print("3. URL EXTRACTION")
print("=" * 60)

text = "Visit https://example.com and http://test.org for more info"
pattern = r'https?://[^\s]+'

urls = re.findall(pattern, text)
print(f"  URLs found: {urls}")

print()  # Empty line


# ============================================================================
# 4. DATE EXTRACTION
# ============================================================================
print("=" * 60)
print("4. DATE EXTRACTION")
print("=" * 60)

text = "Date: 2024-01-15, Another: 2023-12-25"
pattern = r'\d{4}-\d{2}-\d{2}'

dates = re.findall(pattern, text)
print(f"  Dates found: {dates}")

print()  # Empty line


# ============================================================================
# 5. TEXT CLEANING
# ============================================================================
print("=" * 60)
print("5. TEXT CLEANING")
print("=" * 60)

text = "Hello!!!   World???   Python..."
# Remove multiple punctuation
cleaned = re.sub(r'[!?.]{2,}', '', text)
# Remove extra spaces
cleaned = re.sub(r'\s+', ' ', cleaned)
print(f"  Original: {text}")
print(f"  Cleaned: {cleaned}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL EXAMPLES SUMMARY:")
print("=" * 60)
print("Regex is useful for:")
print("  - Email and phone validation")
print("  - URL and date extraction")
print("  - Text cleaning and formatting")
print("  - Pattern matching in logs")
print("  - Data parsing")
print("=" * 60)

