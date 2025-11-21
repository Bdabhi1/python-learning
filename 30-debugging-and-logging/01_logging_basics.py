"""
Logging Basics in Python

This file demonstrates the fundamental concepts of logging.
"""

import logging

# ============================================================================
# 1. WHAT IS LOGGING?
# ============================================================================
print("=" * 60)
print("1. WHAT IS LOGGING?")
print("=" * 60)

print("  Logging is the process of recording events during execution:")
print("    - Debug information")
print("    - Info messages")
print("    - Warnings")
print("    - Errors")
print("    - Critical errors")
print("  ")
print("  Benefits:")
print("    - Debugging: Understand what happened")
print("    - Monitoring: Track application behavior")
print("    - Auditing: Record important events")

print()  # Empty line


# ============================================================================
# 2. LOGGING VS PRINT
# ============================================================================
print("=" * 60)
print("2. LOGGING VS PRINT")
print("=" * 60)

print("  Print statements:")
print("    - Always output")
print("    - Not configurable")
print("    - Single level")
print("    - Hard to disable")
print("  ")
print("  Logging:")
print("    - Configurable levels")
print("    - Can be disabled")
print("    - Multiple output destinations")
print("    - Professional approach")

print()  # Empty line


# ============================================================================
# 3. BASIC LOGGING SETUP
# ============================================================================
print("=" * 60)
print("3. BASIC LOGGING SETUP")
print("=" * 60)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Log messages
logging.debug("Debug message (won't show)")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")

print()  # Empty line


# ============================================================================
# 4. LOGGING TO FILE
# ============================================================================
print("=" * 60)
print("4. LOGGING TO FILE")
print("=" * 60)

logging.basicConfig(
    filename='example.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("This message goes to example.log file")
print("  Check example.log file for the log message")

print()  # Empty line


# ============================================================================
# 5. LOGGING MODULE STRUCTURE
# ============================================================================
print("=" * 60)
print("5. LOGGING MODULE STRUCTURE")
print("=" * 60)

print("  Logging components:")
print("    - Logger: Creates log records")
print("    - Handler: Sends logs to destination (file, console)")
print("    - Formatter: Formats log messages")
print("    - Filter: Filters log records")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("LOGGING BASICS SUMMARY:")
print("=" * 60)
print("  - Logging records events during execution")
print("  - Use logging instead of print")
print("  - Configure with basicConfig()")
print("  - Can log to file or console")
print("  - Multiple log levels available")
print("=" * 60)

