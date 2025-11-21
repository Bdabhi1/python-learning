"""
Log Formatters

This file demonstrates customizing log message formats.
"""

import logging

# ============================================================================
# 1. BASIC FORMATTER
# ============================================================================
print("=" * 60)
print("1. BASIC FORMATTER")
print("=" * 60)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)

logger.info("Formatted log message")

print()  # Empty line


# ============================================================================
# 2. DETAILED FORMATTER
# ============================================================================
print("=" * 60)
print("2. DETAILED FORMATTER")
print("=" * 60)

detailed_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s() - %(message)s'
)

handler = logging.StreamHandler()
handler.setFormatter(detailed_formatter)

logger = logging.getLogger('detailed')
logger.addHandler(handler)
logger.setLevel(logging.INFO)

logger.info("Detailed formatted message")

print()  # Empty line


# ============================================================================
# 3. FORMAT CODES
# ============================================================================
print("=" * 60)
print("3. FORMAT CODES")
print("=" * 60)

print("  Common format codes:")
print("    %(asctime)s    - Human-readable time")
print("    %(name)s       - Logger name")
print("    %(levelname)s - Log level (DEBUG, INFO, etc.)")
print("    %(message)s    - Log message")
print("    %(filename)s   - Filename")
print("    %(lineno)d     - Line number")
print("    %(funcName)s   - Function name")
print("    %(pathname)s   - Full pathname")

print()  # Empty line


# ============================================================================
# 4. CUSTOM DATE FORMAT
# ============================================================================
print("=" * 60)
print("4. CUSTOM DATE FORMAT")
print("=" * 60)

formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)

logger.info("Message with custom date format")

print()  # Empty line


# ============================================================================
# 5. DIFFERENT FORMATS FOR DIFFERENT HANDLERS
# ============================================================================
print("=" * 60)
print("5. DIFFERENT FORMATS FOR DIFFERENT HANDLERS")
print("=" * 60)

logger = logging.getLogger('multi_format')
logger.setLevel(logging.INFO)

# Simple format for console
console_formatter = logging.Formatter('%(levelname)s: %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(console_formatter)

# Detailed format for file
file_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler = logging.FileHandler('formatted.log')
file_handler.setFormatter(file_formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.info("Different formats for console and file")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("LOG FORMATTERS SUMMARY:")
print("=" * 60)
print("  - Formatter controls log message format")
print("  - Use format codes for different information")
print("  - Can customize date format")
print("  - Different handlers can have different formats")
print("=" * 60)

