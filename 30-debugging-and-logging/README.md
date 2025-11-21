# Debugging and Logging in Python

Logging is a crucial tool for understanding what your application is doing, tracking errors, and debugging issues. Python's `logging` module provides a flexible and powerful logging system.

## Table of Contents
1. [What is Logging?](#what-is-logging)
2. [The `logging` Module](#the-logging-module)
3. [Log Levels](#log-levels)
4. [Basic Logging](#basic-logging)
5. [Configuring Loggers](#configuring-loggers)
6. [Log Handlers](#log-handlers)
7. [Formatters](#formatters)
8. [Advanced Logging](#advanced-logging)
9. [Best Practices](#best-practices)

---

## What is Logging?

**Logging** is the process of recording events that happen during program execution:
- **Debug information**: Detailed diagnostic information
- **Info messages**: General informational messages
- **Warnings**: Warning messages for potential issues
- **Errors**: Error messages for problems
- **Critical errors**: Critical errors that may stop execution

**Benefits of Logging:**
- **Debugging**: Understand what happened when errors occur
- **Monitoring**: Track application behavior
- **Auditing**: Record important events
- **Performance**: Identify bottlenecks

**Logging vs Print:**
- **Logging**: Configurable, can be disabled, multiple levels
- **Print**: Always outputs, not configurable, single level

---

## The `logging` Module

Python's `logging` module provides a comprehensive logging system.

### Basic Usage

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
logging.warning("This is a warning")
logging.error("This is an error")
```

### Why Use Logging?

```python
# Instead of print
print("User logged in")  # Always prints, can't disable

# Use logging
logging.info("User logged in")  # Can be configured, filtered
```

---

## Log Levels

Python defines five standard log levels (in order of severity):

### Log Level Hierarchy

```python
import logging

# CRITICAL (50): Critical errors
logging.critical("Critical error occurred")

# ERROR (40): Error events
logging.error("An error occurred")

# WARNING (30): Warning messages
logging.warning("This is a warning")

# INFO (20): Informational messages
logging.info("Informational message")

# DEBUG (10): Detailed diagnostic information
logging.debug("Debug information")
```

### Setting Log Level

```python
import logging

# Set level - only messages at this level and above are logged
logging.basicConfig(level=logging.DEBUG)  # Shows all messages
logging.basicConfig(level=logging.INFO)    # Shows INFO and above
logging.basicConfig(level=logging.WARNING) # Shows WARNING and above
```

---

## Basic Logging

### Simple Logging

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Application started")
logging.warning("Low memory")
logging.error("Failed to connect")
```

### Logging to File

```python
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logging.info("This will be written to app.log")
```

### Logging to Both File and Console

```python
import logging

# Create logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Add handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info("Message goes to both file and console")
```

---

## Configuring Loggers

### Basic Configuration

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
```

### Advanced Configuration

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
```

---

## Log Handlers

Handlers determine where log messages go.

### File Handler

```python
import logging

logger = logging.getLogger()
file_handler = logging.FileHandler('app.log')
logger.addHandler(file_handler)
logger.info("Written to file")
```

### Stream Handler (Console)

```python
import logging

logger = logging.getLogger()
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
logger.info("Printed to console")
```

### Rotating File Handler

```python
import logging
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler(
    'app.log',
    maxBytes=1024*1024,  # 1MB
    backupCount=5
)
logger = logging.getLogger()
logger.addHandler(handler)
```

### Timed Rotating File Handler

```python
import logging
from logging.handlers import TimedRotatingFileHandler

handler = TimedRotatingFileHandler(
    'app.log',
    when='midnight',
    interval=1,
    backupCount=7
)
logger = logging.getLogger()
logger.addHandler(handler)
```

---

## Formatters

Formatters control the format of log messages.

### Basic Formatter

```python
import logging

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(handler)
```

### Format Codes

- `%(asctime)s`: Human-readable time
- `%(name)s`: Logger name
- `%(levelname)s`: Log level
- `%(message)s`: Log message
- `%(filename)s`: Filename
- `%(lineno)d`: Line number
- `%(funcName)s`: Function name
- `%(pathname)s`: Full pathname

---

## Advanced Logging

### Named Loggers

```python
import logging

# Create named logger
logger = logging.getLogger('my_app')
logger.setLevel(logging.INFO)

logger.info("Using named logger")
```

### Logger Hierarchy

```python
import logging

# Parent logger
parent_logger = logging.getLogger('app')
parent_logger.setLevel(logging.INFO)

# Child logger (inherits from parent)
child_logger = logging.getLogger('app.module')
child_logger.info("Child logger message")
```

### Exception Logging

```python
import logging

try:
    result = 10 / 0
except Exception:
    logging.exception("An exception occurred")  # Includes traceback
    # Or
    logging.error("An exception occurred", exc_info=True)
```

---

## Best Practices

### 1. Use Appropriate Log Levels

```python
# DEBUG: Detailed diagnostic info
logging.debug("Variable value: %s", value)

# INFO: General information
logging.info("User %s logged in", username)

# WARNING: Potential issues
logging.warning("Memory usage is high: %d%%", usage)

# ERROR: Errors that don't stop execution
logging.error("Failed to save file: %s", filename)

# CRITICAL: Critical errors
logging.critical("Database connection lost!")
```

### 2. Don't Use Print for Logging

```python
# Wrong
print("Error occurred")

# Correct
logging.error("Error occurred")
```

### 3. Use Format Strings

```python
# Good - lazy evaluation
logging.info("User %s logged in", username)

# Less preferred - evaluates immediately
logging.info(f"User {username} logged in")
```

### 4. Configure Logging Once

```python
# Configure at application startup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

### 5. Use Named Loggers

```python
# Good
logger = logging.getLogger(__name__)
logger.info("Message")

# Less preferred
logging.info("Message")
```

---

## Common Mistakes to Avoid

1. **Using print instead of logging**
   ```python
   # Wrong
   print("Error occurred")
   
   # Correct
   logging.error("Error occurred")
   ```

2. **Not setting log level**
   ```python
   # Wrong - may not show messages
   logging.basicConfig()
   logging.debug("Debug message")  # Won't show
   
   # Correct
   logging.basicConfig(level=logging.DEBUG)
   logging.debug("Debug message")  # Will show
   ```

3. **Logging sensitive information**
   ```python
   # Wrong
   logging.info(f"Password: {password}")
   
   # Correct
   logging.info("User authenticated")
   ```

---

## Summary

- **Logging** records events during program execution
- Use `logging` module instead of `print`
- **Five log levels**: DEBUG, INFO, WARNING, ERROR, CRITICAL
- **Handlers** determine where logs go (file, console, etc.)
- **Formatters** control log message format
- **Use appropriate log levels** for different situations
- **Configure logging** at application startup

**Remember**: Good logging makes debugging and monitoring much easier. Use it throughout your applications!

---

## Next Steps

Now that you understand debugging and logging:
1. Practice with the examples in this folder
2. Add logging to your applications
3. Configure appropriate log levels
4. Use logging for debugging and monitoring

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_logging_basics.py`: Understanding logging concepts
2. `02_log_levels.py`: Working with different log levels
3. `03_basic_logging.py`: Basic logging configuration and usage
4. `04_log_handlers.py`: Using different log handlers
5. `05_log_formatters.py`: Customizing log message formats
6. `06_practical_examples.py`: Real-world logging examples

Run these files in order to see logging in action!

