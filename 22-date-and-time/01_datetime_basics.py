"""
Date and Time Basics in Python

This file demonstrates the fundamental concepts of the datetime module.
"""

from datetime import date, time, datetime

# ============================================================================
# 1. WHAT IS THE DATETIME MODULE?
# ============================================================================
print("=" * 60)
print("1. WHAT IS THE DATETIME MODULE?")
print("=" * 60)

print("  The datetime module provides classes for working with:")
print("    - date: Date (year, month, day)")
print("    - time: Time (hour, minute, second)")
print("    - datetime: Date and time combined")
print("    - timedelta: Duration between dates")
print("    - tzinfo: Timezone information")

print()  # Empty line


# ============================================================================
# 2. CURRENT DATE AND TIME
# ============================================================================
print("=" * 60)
print("2. CURRENT DATE AND TIME")
print("=" * 60)

# Current date
today = date.today()
print(f"  Today's date: {today}")

# Current datetime
now = datetime.now()
print(f"  Current datetime: {now}")

# Current time
current_time = now.time()
print(f"  Current time: {current_time}")

print()  # Empty line


# ============================================================================
# 3. DATE OBJECT
# ============================================================================
print("=" * 60)
print("3. DATE OBJECT")
print("=" * 60)

# Create specific date
my_date = date(2024, 1, 15)
print(f"  Date: {my_date}")
print(f"  Year: {my_date.year}")
print(f"  Month: {my_date.month}")
print(f"  Day: {my_date.day}")

print()  # Empty line


# ============================================================================
# 4. TIME OBJECT
# ============================================================================
print("=" * 60)
print("4. TIME OBJECT")
print("=" * 60)

# Create specific time
my_time = time(14, 30, 45)
print(f"  Time: {my_time}")
print(f"  Hour: {my_time.hour}")
print(f"  Minute: {my_time.minute}")
print(f"  Second: {my_time.second}")

print()  # Empty line


# ============================================================================
# 5. DATETIME OBJECT
# ============================================================================
print("=" * 60)
print("5. DATETIME OBJECT")
print("=" * 60)

# Create specific datetime
dt = datetime(2024, 1, 15, 14, 30, 45)
print(f"  DateTime: {dt}")
print(f"  Date part: {dt.date()}")
print(f"  Time part: {dt.time()}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("DATETIME BASICS SUMMARY:")
print("=" * 60)
print("  - date: Represents a date (year, month, day)")
print("  - time: Represents a time (hour, minute, second)")
print("  - datetime: Represents date and time together")
print("  - date.today(): Get current date")
print("  - datetime.now(): Get current datetime")
print("=" * 60)

