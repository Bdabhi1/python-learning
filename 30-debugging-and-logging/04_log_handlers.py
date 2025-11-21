"""
Log Handlers

This file demonstrates different types of log handlers.
"""

import logging
import os
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

# ============================================================================
# 1. FILE HANDLER
# ============================================================================
print("=" * 60)
print("1. FILE HANDLER")
print("=" * 60)

if os.path.exists('file_handler.log'):
    os.remove('file_handler.log')

logger = logging.getLogger('file_logger')
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('file_handler.log')
logger.addHandler(file_handler)

logger.info("This message goes to file_handler.log")
print("  Message written to file_handler.log")

print()  # Empty line


# ============================================================================
# 2. STREAM HANDLER (CONSOLE)
# ============================================================================
print("=" * 60)
print("2. STREAM HANDLER (CONSOLE)")
print("=" * 60)

logger = logging.getLogger('console_logger')
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

logger.info("This message goes to console")

print()  # Empty line


# ============================================================================
# 3. ROTATING FILE HANDLER
# ============================================================================
print("=" * 60)
print("3. ROTATING FILE HANDLER")
print("=" * 60)

# Remove existing files
for f in ['rotating.log', 'rotating.log.1']:
    if os.path.exists(f):
        os.remove(f)

logger = logging.getLogger('rotating_logger')
logger.setLevel(logging.INFO)

# Rotates when file reaches maxBytes
rotating_handler = RotatingFileHandler(
    'rotating.log',
    maxBytes=1024,  # 1KB for demo
    backupCount=3
)
logger.addHandler(rotating_handler)

logger.info("This creates rotating.log")
print("  RotatingFileHandler: Rotates when file size limit reached")

print()  # Empty line


# ============================================================================
# 4. TIMED ROTATING FILE HANDLER
# ============================================================================
print("=" * 60)
print("4. TIMED ROTATING FILE HANDLER")
print("=" * 60)

if os.path.exists('timed_rotating.log'):
    os.remove('timed_rotating.log')

logger = logging.getLogger('timed_logger')
logger.setLevel(logging.INFO)

# Rotates based on time
timed_handler = TimedRotatingFileHandler(
    'timed_rotating.log',
    when='midnight',
    interval=1,
    backupCount=7
)
logger.addHandler(timed_handler)

logger.info("This creates timed_rotating.log")
print("  TimedRotatingFileHandler: Rotates based on time (daily, hourly, etc.)")

print()  # Empty line


# ============================================================================
# 5. MULTIPLE HANDLERS
# ============================================================================
print("=" * 60)
print("5. MULTIPLE HANDLERS")
print("=" * 60)

if os.path.exists('multi.log'):
    os.remove('multi.log')

logger = logging.getLogger('multi_logger')
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler('multi.log')
file_handler.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)  # Only warnings and above

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info("Info: Goes to file only")
logger.warning("Warning: Goes to both file and console")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("LOG HANDLERS SUMMARY:")
print("=" * 60)
print("  - FileHandler: Log to file")
print("  - StreamHandler: Log to console")
print("  - RotatingFileHandler: Rotate by size")
print("  - TimedRotatingFileHandler: Rotate by time")
print("  - Can use multiple handlers")
print("=" * 60)

