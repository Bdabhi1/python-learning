"""
Creating Date and Time Objects

This file demonstrates different ways to create date, time, and datetime objects.
"""

from datetime import date, time, datetime

# ============================================================================
# 1. CREATING DATE OBJECTS
# ============================================================================
print("=" * 60)
print("1. CREATING DATE OBJECTS")
print("=" * 60)

# From constructor
date1 = date(2024, 1, 15)
print(f"  date(2024, 1, 15): {date1}")

# From today
today = date.today()
print(f"  date.today(): {today}")

# From timestamp
from datetime import datetime
timestamp = datetime.now().timestamp()
date2 = date.fromtimestamp(timestamp)
print(f"  date.fromtimestamp(): {date2}")

print()  # Empty line


# ============================================================================
# 2. CREATING TIME OBJECTS
# ============================================================================
print("=" * 60)
print("2. CREATING TIME OBJECTS")
print("=" * 60)

# From constructor
time1 = time(14, 30, 45)
print(f"  time(14, 30, 45): {time1}")

# With microseconds
time2 = time(14, 30, 45, 123456)
print(f"  time(14, 30, 45, 123456): {time2}")

# From datetime
now = datetime.now()
current_time = now.time()
print(f"  datetime.now().time(): {current_time}")

print()  # Empty line


# ============================================================================
# 3. CREATING DATETIME OBJECTS
# ============================================================================
print("=" * 60)
print("3. CREATING DATETIME OBJECTS")
print("=" * 60)

# From constructor
dt1 = datetime(2024, 1, 15, 14, 30, 45)
print(f"  datetime(2024, 1, 15, 14, 30, 45): {dt1}")

# Current datetime
now = datetime.now()
print(f"  datetime.now(): {now}")

# Combine date and time
my_date = date(2024, 1, 15)
my_time = time(14, 30, 45)
dt2 = datetime.combine(my_date, my_time)
print(f"  datetime.combine(date, time): {dt2}")

print()  # Empty line


# ============================================================================
# 4. ACCESSING COMPONENTS
# ============================================================================
print("=" * 60)
print("4. ACCESSING COMPONENTS")
print("=" * 60)

dt = datetime(2024, 1, 15, 14, 30, 45)

print(f"  Year: {dt.year}")
print(f"  Month: {dt.month}")
print(f"  Day: {dt.day}")
print(f"  Hour: {dt.hour}")
print(f"  Minute: {dt.minute}")
print(f"  Second: {dt.second}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("CREATING DATES AND TIMES SUMMARY:")
print("=" * 60)
print("  - date(year, month, day): Create date")
print("  - time(hour, minute, second): Create time")
print("  - datetime(...): Create datetime")
print("  - date.today(): Current date")
print("  - datetime.now(): Current datetime")
print("=" * 60)

