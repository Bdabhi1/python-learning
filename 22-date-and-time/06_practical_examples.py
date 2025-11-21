"""
Practical Date and Time Examples

This file demonstrates real-world date and time use cases.
"""

from datetime import datetime, timedelta, date

# ============================================================================
# 1. AGE CALCULATION
# ============================================================================
print("=" * 60)
print("1. AGE CALCULATION")
print("=" * 60)

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

birth_date = date(1990, 5, 15)
age = calculate_age(birth_date)
print(f"  Birth date: {birth_date}")
print(f"  Age: {age} years")

print()  # Empty line


# ============================================================================
# 2. DAYS UNTIL EVENT
# ============================================================================
print("=" * 60)
print("2. DAYS UNTIL EVENT")
print("=" * 60)

def days_until(event_date):
    today = date.today()
    return (event_date - today).days

event = date(2024, 12, 25)
days = days_until(event)
print(f"  Event date: {event}")
print(f"  Days until event: {days}")

print()  # Empty line


# ============================================================================
# 3. FORMATTING FOR DISPLAY
# ============================================================================
print("=" * 60)
print("3. FORMATTING FOR DISPLAY")
print("=" * 60)

now = datetime.now()

formats = {
    "Short date": now.strftime("%m/%d/%Y"),
    "Long date": now.strftime("%A, %B %d, %Y"),
    "Time": now.strftime("%I:%M %p"),
    "Full": now.strftime("%A, %B %d, %Y at %I:%M %p")
}

for label, formatted in formats.items():
    print(f"  {label}: {formatted}")

print()  # Empty line


# ============================================================================
# 4. WORKING DAYS CALCULATION
# ============================================================================
print("=" * 60)
print("4. WORKING DAYS CALCULATION")
print("=" * 60)

def working_days(start_date, end_date):
    current = start_date
    count = 0
    while current <= end_date:
        if current.weekday() < 5:  # Monday = 0, Friday = 4
            count += 1
        current += timedelta(days=1)
    return count

start = date(2024, 1, 15)
end = date(2024, 1, 25)
days = working_days(start, end)
print(f"  Start: {start}, End: {end}")
print(f"  Working days: {days}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL EXAMPLES SUMMARY:")
print("=" * 60)
print("Date and time operations are useful for:")
print("  - Age and duration calculations")
print("  - Event scheduling")
print("  - Date formatting for display")
print("  - Business day calculations")
print("  - Time-based filtering")
print("=" * 60)

