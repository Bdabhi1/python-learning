# Date and Time in Python

Python provides powerful modules for working with dates and times: `datetime`, `time`, and `calendar`. These modules make it easy to handle dates, times, timezones, and time-related calculations.

## Table of Contents
1. [The `datetime` Module](#the-datetime-module)
2. [Creating Date and Time Objects](#creating-date-and-time-objects)
3. [Formatting Dates and Times](#formatting-dates-and-times)
4. [Parsing Dates from Strings](#parsing-dates-from-strings)
5. [Date and Time Arithmetic](#date-and-time-arithmetic)
6. [Timezones](#timezones)
7. [The `time` Module](#the-time-module)
8. [The `calendar` Module](#the-calendar-module)
9. [Best Practices](#best-practices)

---

## The `datetime` Module

The `datetime` module provides classes for working with dates and times.

### Main Classes

- `datetime.date`: Date (year, month, day)
- `datetime.time`: Time (hour, minute, second, microsecond)
- `datetime.datetime`: Date and time combined
- `datetime.timedelta`: Duration/difference between dates
- `datetime.tzinfo`: Timezone information

---

## Creating Date and Time Objects

### Date Objects

```python
from datetime import date

# Current date
today = date.today()
print(today)  # 2024-01-15

# Specific date
my_date = date(2024, 1, 15)
print(my_date)  # 2024-01-15
```

### Time Objects

```python
from datetime import time

# Specific time
my_time = time(14, 30, 45)  # 14:30:45
print(my_time)

# Current time (from datetime)
from datetime import datetime
now = datetime.now().time()
```

### DateTime Objects

```python
from datetime import datetime

# Current datetime
now = datetime.now()
print(now)  # 2024-01-15 14:30:45.123456

# Specific datetime
dt = datetime(2024, 1, 15, 14, 30, 45)
print(dt)
```

---

## Formatting Dates and Times

### Using `strftime()`

```python
from datetime import datetime

now = datetime.now()

# Format codes
print(now.strftime("%Y-%m-%d"))        # 2024-01-15
print(now.strftime("%H:%M:%S"))        # 14:30:45
print(now.strftime("%A, %B %d, %Y"))   # Monday, January 15, 2024
print(now.strftime("%I:%M %p"))        # 02:30 PM
```

### Common Format Codes

- `%Y`: Year (4 digits)
- `%m`: Month (01-12)
- `%d`: Day (01-31)
- `%H`: Hour (00-23)
- `%M`: Minute (00-59)
- `%S`: Second (00-59)
- `%A`: Weekday (full name)
- `%B`: Month (full name)
- `%I`: Hour (12-hour format)
- `%p`: AM/PM

---

## Parsing Dates from Strings

### Using `strptime()`

```python
from datetime import datetime

# Parse string to datetime
date_string = "2024-01-15 14:30:45"
dt = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(dt)
```

### Using `dateutil` (Third-party)

```python
from dateutil import parser

# Automatic parsing
dt = parser.parse("January 15, 2024")
dt = parser.parse("2024-01-15")
dt = parser.parse("15/01/2024")
```

---

## Date and Time Arithmetic

### Using `timedelta`

```python
from datetime import datetime, timedelta

now = datetime.now()

# Add/subtract time
tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)
next_week = now + timedelta(weeks=1)
in_2_hours = now + timedelta(hours=2)

# Difference between dates
diff = tomorrow - yesterday
print(diff.days)  # 2
```

### Date Comparisons

```python
from datetime import date

date1 = date(2024, 1, 15)
date2 = date(2024, 1, 20)

print(date1 < date2)   # True
print(date1 == date2)  # False
```

---

## Timezones

### Working with Timezones

```python
from datetime import datetime, timezone, timedelta

# UTC time
utc_now = datetime.now(timezone.utc)

# Specific timezone
eastern = timezone(timedelta(hours=-5))
eastern_time = datetime.now(eastern)

# Convert between timezones
utc_time = eastern_time.astimezone(timezone.utc)
```

### Using `pytz` (Third-party)

```python
import pytz
from datetime import datetime

# Get timezone
tz = pytz.timezone('America/New_York')
now = datetime.now(tz)

# Convert timezone
utc = pytz.UTC
utc_time = now.astimezone(utc)
```

---

## The `time` Module

The `time` module provides time-related functions.

### Current Time

```python
import time

# Unix timestamp
timestamp = time.time()
print(timestamp)  # 1705327845.123456

# Formatted time
formatted = time.ctime(timestamp)
print(formatted)  # Mon Jan 15 14:30:45 2024

# Struct time
struct = time.localtime()
print(struct.tm_year)  # 2024
```

### Sleep

```python
import time

print("Start")
time.sleep(2)  # Sleep for 2 seconds
print("End")
```

---

## The `calendar` Module

The `calendar` module provides calendar-related functions.

### Calendar Functions

```python
import calendar

# Month calendar
print(calendar.month(2024, 1))

# Year calendar
print(calendar.calendar(2024))

# Check leap year
print(calendar.isleap(2024))  # True

# Day name
print(calendar.day_name[0])  # Monday
```

---

## Best Practices

### 1. Use `datetime` for Most Operations

```python
from datetime import datetime

# Good
now = datetime.now()

# Less preferred
import time
timestamp = time.time()
```

### 2. Always Use Timezone-Aware Datetimes

```python
from datetime import datetime, timezone

# Good
now = datetime.now(timezone.utc)

# Less preferred (naive datetime)
now = datetime.now()
```

### 3. Use ISO Format for Storage

```python
dt = datetime.now()
iso_string = dt.isoformat()  # Good for storage
```

### 4. Handle Timezone Conversions Carefully

```python
# Always convert explicitly
utc_time = local_time.astimezone(timezone.utc)
```

---

## Common Mistakes to Avoid

1. **Using naive datetimes**
   ```python
   # Problematic
   dt = datetime.now()  # No timezone
   
   # Better
   dt = datetime.now(timezone.utc)
   ```

2. **Not handling timezone conversions**
   ```python
   # Wrong
   utc_time = local_time  # Doesn't convert!
   
   # Correct
   utc_time = local_time.astimezone(timezone.utc)
   ```

3. **Mixing date formats**
   ```python
   # Be consistent
   date_string = dt.strftime("%Y-%m-%d")  # ISO format
   ```

---

## Summary

- **`datetime`** module provides date and time classes
- Use `strftime()` to format dates
- Use `strptime()` to parse dates
- Use `timedelta` for date arithmetic
- Always use **timezone-aware** datetimes when possible
- `time` module for timestamps and sleep
- `calendar` module for calendar operations

**Remember**: Always be aware of timezones when working with dates and times!

---

## Next Steps

Now that you understand date and time handling:
1. Practice with the examples in this folder
2. Work with timezone-aware datetimes
3. Use date arithmetic for calculations
4. Move on to **23-working-with-json** to learn JSON handling

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_datetime_basics.py`: Understanding datetime module - start here!
2. `02_creating_dates_times.py`: Creating date, time, and datetime objects
3. `03_formatting_parsing.py`: Formatting and parsing dates
4. `04_date_arithmetic.py`: Date and time arithmetic with timedelta
5. `05_timezones.py`: Working with timezones
6. `06_practical_examples.py`: Real-world date and time examples

Run these files in order to see date and time handling in action!

