"""
Basic Logging Configuration

This file demonstrates basic logging setup and usage.
"""

import logging
import os

# ============================================================================
# 1. SIMPLE LOGGING
# ============================================================================
print("=" * 60)
print("1. SIMPLE LOGGING")
print("=" * 60)

logging.basicConfig(level=logging.INFO)

logging.info("Application started")
logging.warning("This is a warning")
logging.error("An error occurred")

print()  # Empty line


# ============================================================================
# 2. LOGGING TO FILE
# ============================================================================
print("=" * 60)
print("2. LOGGING TO FILE")
print("=" * 60)

# Remove existing log file
if os.path.exists('app.log'):
    os.remove('app.log')

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("This message goes to app.log")
logging.warning("Warning also goes to file")

print("  Check app.log file for log messages")

print()  # Empty line


# ============================================================================
# 3. LOGGING WITH FORMAT
# ============================================================================
print("=" * 60)
print("3. LOGGING WITH FORMAT")
print("=" * 60)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True
)

logging.info("Formatted log message")
logging.warning("Another formatted message")

print()  # Empty line


# ============================================================================
# 4. LOGGING TO BOTH FILE AND CONSOLE
# ============================================================================
print("=" * 60)
print("4. LOGGING TO BOTH FILE AND CONSOLE")
print("=" * 60)

# Remove existing log
if os.path.exists('app2.log'):
    os.remove('app2.log')

# Create logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler('app2.log')
file_handler.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info("This message goes to both file and console")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("BASIC LOGGING SUMMARY:")
print("=" * 60)
print("  - basicConfig(): Configure logging")
print("  - filename: Log to file")
print("  - format: Customize log format")
print("  - Can log to file, console, or both")
print("=" * 60)

