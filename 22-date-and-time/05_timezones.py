"""
Working with Timezones

This file demonstrates timezone handling in Python.
"""

from datetime import datetime, timezone, timedelta

# ============================================================================
# 1. UTC TIME
# ============================================================================
print("=" * 60)
print("1. UTC TIME")
print("=" * 60)

# UTC time
utc_now = datetime.now(timezone.utc)
print(f"  UTC time: {utc_now}")

# Naive datetime (no timezone)
naive_now = datetime.now()
print(f"  Naive datetime: {naive_now}")

print()  # Empty line


# ============================================================================
# 2. SPECIFIC TIMEZONE
# ============================================================================
print("=" * 60)
print("2. SPECIFIC TIMEZONE")
print("=" * 60)

# Create timezone (UTC-5 for Eastern Time)
eastern = timezone(timedelta(hours=-5))
eastern_time = datetime.now(eastern)
print(f"  Eastern time: {eastern_time}")

# Convert to UTC
utc_time = eastern_time.astimezone(timezone.utc)
print(f"  Converted to UTC: {utc_time}")

print()  # Empty line


# ============================================================================
# 3. TIMEZONE AWARENESS
# ============================================================================
print("=" * 60)
print("3. TIMEZONE AWARENESS")
print("=" * 60)

naive = datetime.now()
aware = datetime.now(timezone.utc)

print(f"  Naive datetime: {naive}")
print(f"  Is timezone-aware: {naive.tzinfo is None}")

print(f"  Aware datetime: {aware}")
print(f"  Is timezone-aware: {aware.tzinfo is not None}")

print("\n  Always use timezone-aware datetimes when possible!")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("TIMEZONES SUMMARY:")
print("=" * 60)
print("  - Use timezone.utc for UTC time")
print("  - Create timezones with timezone(timedelta(...))")
print("  - Use astimezone() to convert between timezones")
print("  - Prefer timezone-aware datetimes")
print("  - Consider using pytz library for more timezones")
print("=" * 60)

