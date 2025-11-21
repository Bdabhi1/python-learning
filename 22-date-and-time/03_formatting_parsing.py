"""
Formatting and Parsing Dates

This file demonstrates how to format dates to strings and parse strings to dates.
"""

from datetime import datetime

# ============================================================================
# 1. FORMATTING DATES (strftime)
# ============================================================================
print("=" * 60)
print("1. FORMATTING DATES (strftime)")
print("=" * 60)

now = datetime.now()

# Common formats
print(f"  %Y-%m-%d: {now.strftime('%Y-%m-%d')}")
print(f"  %H:%M:%S: {now.strftime('%H:%M:%S')}")
print(f"  %A, %B %d, %Y: {now.strftime('%A, %B %d, %Y')}")
print(f"  %I:%M %p: {now.strftime('%I:%M %p')}")

print()  # Empty line


# ============================================================================
# 2. PARSING DATES (strptime)
# ============================================================================
print("=" * 60)
print("2. PARSING DATES (strptime)")
print("=" * 60)

# Parse string to datetime
date_string = "2024-01-15 14:30:45"
dt = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"  String: {date_string}")
print(f"  Parsed: {dt}")

# Different format
date_string2 = "January 15, 2024"
dt2 = datetime.strptime(date_string2, "%B %d, %Y")
print(f"  String: {date_string2}")
print(f"  Parsed: {dt2}")

print()  # Empty line


# ============================================================================
# 3. ISO FORMAT
# ============================================================================
print("=" * 60)
print("3. ISO FORMAT")
print("=" * 60)

now = datetime.now()

# To ISO string
iso_string = now.isoformat()
print(f"  ISO format: {iso_string}")

# From ISO string
dt = datetime.fromisoformat(iso_string)
print(f"  From ISO: {dt}")

print()  # Empty line


# ============================================================================
# 4. COMMON FORMAT CODES
# ============================================================================
print("=" * 60)
print("4. COMMON FORMAT CODES")
print("=" * 60)

now = datetime.now()

print("  %Y: 4-digit year")
print("  %m: Month (01-12)")
print("  %d: Day (01-31)")
print("  %H: Hour (00-23)")
print("  %M: Minute (00-59)")
print("  %S: Second (00-59)")
print("  %A: Weekday (full name)")
print("  %B: Month (full name)")
print("  %I: Hour (12-hour format)")
print("  %p: AM/PM")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("FORMATTING AND PARSING SUMMARY:")
print("=" * 60)
print("  - strftime(): Format datetime to string")
print("  - strptime(): Parse string to datetime")
print("  - isoformat(): ISO 8601 format")
print("  - Use format codes for custom formats")
print("=" * 60)

