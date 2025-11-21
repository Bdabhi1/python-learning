"""
Practical Logging Examples

This file demonstrates real-world logging scenarios.
"""

import logging
import os

# ============================================================================
# 1. APPLICATION LOGGING SETUP
# ============================================================================
print("=" * 60)
print("1. APPLICATION LOGGING SETUP")
print("=" * 60)

def setup_logging(log_file='app.log'):
    """Configure logging for application"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logging('application.log')
logger.info("Application logging configured")
logger.warning("This is a warning message")

print()  # Empty line


# ============================================================================
# 2. LOGGING EXCEPTIONS
# ============================================================================
print("=" * 60)
print("2. LOGGING EXCEPTIONS")
print("=" * 60)

logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s', force=True)

try:
    result = 10 / 0
except ZeroDivisionError:
    logging.exception("Exception occurred")  # Includes full traceback
    # Or
    # logging.error("Exception occurred", exc_info=True)

print()  # Empty line


# ============================================================================
# 3. NAMED LOGGERS
# ============================================================================
print("=" * 60)
print("3. NAMED LOGGERS")
print("=" * 60)

# Create logger for specific module
module_logger = logging.getLogger('my_app.database')
module_logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
module_logger.addHandler(handler)

module_logger.info("Database connection established")
module_logger.error("Database query failed")

print()  # Empty line


# ============================================================================
# 4. CONDITIONAL LOGGING
# ============================================================================
print("=" * 60)
print("4. CONDITIONAL LOGGING")
print("=" * 60)

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s', force=True)

def process_data(data, debug=False):
    logger = logging.getLogger(__name__)
    
    if debug:
        logger.debug(f"Processing data: {data}")
    
    logger.info("Processing started")
    
    try:
        # Process data
        result = len(data)
        logger.info(f"Processing completed: {result} items")
        return result
    except Exception as e:
        logger.error(f"Processing failed: {e}")
        raise

process_data([1, 2, 3], debug=False)
process_data([1, 2, 3], debug=True)

print()  # Empty line


# ============================================================================
# 5. LOGGING WITH CONTEXT
# ============================================================================
print("=" * 60)
print("5. LOGGING WITH CONTEXT")
print("=" * 60)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
    force=True
)

def user_action(username, action):
    logger = logging.getLogger(__name__)
    logger.info(f"User '{username}' performed action: {action}")

user_action("Alice", "login")
user_action("Bob", "logout")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL EXAMPLES SUMMARY:")
print("=" * 60)
print("Logging best practices:")
print("  - Set up logging at application startup")
print("  - Use named loggers for different modules")
print("  - Log exceptions with exception() or exc_info=True")
print("  - Include context in log messages")
print("  - Use appropriate log levels")
print("=" * 60)

