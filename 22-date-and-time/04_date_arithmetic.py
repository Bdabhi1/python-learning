"""
Date and Time Arithmetic

This file demonstrates date arithmetic using timedelta.
"""

from datetime import datetime, timedelta, date

# ============================================================================
# 1. BASIC ARITHMETIC WITH timedelta
# ============================================================================
print("=" * 60)
print("1. BASIC ARITHMETIC WITH timedelta")
print("=" * 60)

now = datetime.now()

# Add/subtract days
tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)

print(f"  Today: {now.strftime('%Y-%m-%d')}")
print(f"  Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")
print(f"  Yesterday: {yesterday.strftime('%Y-%m-%d')}")

print()  # Empty line


# ============================================================================
# 2. DIFFERENT TIME UNITS
# ============================================================================
print("=" * 60)
print("2. DIFFERENT TIME UNITS")
print("=" * 60)

now = datetime.now()

# Weeks
next_week = now + timedelta(weeks=1)
print(f"  Next week: {next_week.strftime('%Y-%m-%d')}")

# Hours
in_2_hours = now + timedelta(hours=2)
print(f"  In 2 hours: {in_2_hours.strftime('%H:%M:%S')}")

# Minutes
in_30_minutes = now + timedelta(minutes=30)
print(f"  In 30 minutes: {in_30_minutes.strftime('%H:%M:%S')}")

# Combined
future = now + timedelta(days=5, hours=3, minutes=30)
print(f"  Future: {future.strftime('%Y-%m-%d %H:%M:%S')}")

print()  # Empty line


# ============================================================================
# 3. DATE DIFFERENCES
# ============================================================================
print("=" * 60)
print("3. DATE DIFFERENCES")
print("=" * 60)

date1 = date(2024, 1, 15)
date2 = date(2024, 1, 20)

diff = date2 - date1
print(f"  Difference: {diff.days} days")

# Time difference
dt1 = datetime(2024, 1, 15, 10, 0, 0)
dt2 = datetime(2024, 1, 15, 14, 30, 0)
diff = dt2 - dt1
print(f"  Time difference: {diff}")
print(f"  Total seconds: {diff.total_seconds()}")

print()  # Empty line


# ============================================================================
# 4. DATE COMPARISONS
# ============================================================================
print("=" * 60)
print("4. DATE COMPARISONS")
print("=" * 60)

date1 = date(2024, 1, 15)
date2 = date(2024, 1, 20)

print(f"  date1 < date2: {date1 < date2}")
print(f"  date1 > date2: {date1 > date2}")
print(f"  date1 == date2: {date1 == date2}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("DATE ARITHMETIC SUMMARY:")
print("=" * 60)
print("  - Use timedelta for date arithmetic")
print("  - Can add/subtract days, weeks, hours, minutes, seconds")
print("  - Subtracting dates gives timedelta")
print("  - Can compare dates with <, >, ==, etc.")
print("=" * 60)

