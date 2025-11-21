"""
Log Levels in Python

This file demonstrates the different log levels and their usage.
"""

import logging

# ============================================================================
# 1. LOG LEVEL HIERARCHY
# ============================================================================
print("=" * 60)
print("1. LOG LEVEL HIERARCHY")
print("=" * 60)

print("  Log levels (from lowest to highest severity):")
print("    DEBUG (10): Detailed diagnostic information")
print("    INFO (20):  General informational messages")
print("    WARNING (30): Warning messages")
print("    ERROR (40): Error events")
print("    CRITICAL (50): Critical errors")

print()  # Empty line


# ============================================================================
# 2. USING DIFFERENT LOG LEVELS
# ============================================================================
print("=" * 60)
print("2. USING DIFFERENT LOG LEVELS")
print("=" * 60)

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

logging.debug("Debug: Detailed diagnostic info")
logging.info("Info: General information")
logging.warning("Warning: Potential issue")
logging.error("Error: An error occurred")
logging.critical("Critical: Critical error!")

print()  # Empty line


# ============================================================================
# 3. SETTING LOG LEVEL
# ============================================================================
print("=" * 60)
print("3. SETTING LOG LEVEL")
print("=" * 60)

# Set to DEBUG - shows all messages
print("  Level: DEBUG (shows all)")
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s', force=True)
logging.debug("Debug message")
logging.info("Info message")

# Set to INFO - shows INFO and above
print("\n  Level: INFO (shows INFO and above)")
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s', force=True)
logging.debug("Debug message (won't show)")
logging.info("Info message")

# Set to WARNING - shows WARNING and above
print("\n  Level: WARNING (shows WARNING and above)")
logging.basicConfig(level=logging.WARNING, format='%(levelname)s: %(message)s', force=True)
logging.info("Info message (won't show)")
logging.warning("Warning message")

print()  # Empty line


# ============================================================================
# 4. WHEN TO USE EACH LEVEL
# ============================================================================
print("=" * 60)
print("4. WHEN TO USE EACH LEVEL")
print("=" * 60)

print("  DEBUG: Detailed diagnostic info for debugging")
print("    logging.debug('Variable value: %s', value)")
print("  ")
print("  INFO: General information about program flow")
print("    logging.info('User %s logged in', username)")
print("  ")
print("  WARNING: Potential issues that don't stop execution")
print("    logging.warning('Memory usage is high')")
print("  ")
print("  ERROR: Errors that don't stop execution")
print("    logging.error('Failed to save file')")
print("  ")
print("  CRITICAL: Critical errors that may stop execution")
print("    logging.critical('Database connection lost')")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("LOG LEVELS SUMMARY:")
print("=" * 60)
print("  - DEBUG: Detailed diagnostic info")
print("  - INFO: General information")
print("  - WARNING: Potential issues")
print("  - ERROR: Errors")
print("  - CRITICAL: Critical errors")
print("  - Set level to control what gets logged")
print("=" * 60)

