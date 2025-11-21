"""
Database Connectivity Basics

This file demonstrates the fundamental concepts of database connectivity.
"""

import sqlite3
import os

# ============================================================================
# 1. WHAT IS DATABASE CONNECTIVITY?
# ============================================================================
print("=" * 60)
print("1. WHAT IS DATABASE CONNECTIVITY?")
print("=" * 60)

print("  Database connectivity allows Python to:")
print("    - Connect to databases")
print("    - Execute SQL queries")
print("    - Retrieve data")
print("    - Insert, update, delete data")
print("    - Manage transactions")
print("  ")
print("  Common databases:")
print("    - SQLite: Built-in, file-based")
print("    - MySQL: Popular open-source")
print("    - PostgreSQL: Advanced open-source")
print("    - SQL Server, Oracle: Enterprise")

print()  # Empty line


# ============================================================================
# 2. SQLITE - BUILT-IN DATABASE
# ============================================================================
print("=" * 60)
print("2. SQLITE - BUILT-IN DATABASE")
print("=" * 60)

print("  SQLite is:")
print("    - Built into Python (no installation needed)")
print("    - File-based database")
print("    - Perfect for learning and small projects")
print("    - No separate server required")
print("    - Great for prototyping")

print()  # Empty line


# ============================================================================
# 3. BASIC CONNECTION
# ============================================================================
print("=" * 60)
print("3. BASIC CONNECTION")
print("=" * 60)

# Remove existing database if it exists
if os.path.exists('example.db'):
    os.remove('example.db')

# Connect to database (creates if doesn't exist)
conn = sqlite3.connect('example.db')
print("  Connected to database: example.db")

# Create cursor
cursor = conn.cursor()
print("  Cursor created")

# Close connection
conn.close()
print("  Connection closed")

print()  # Empty line


# ============================================================================
# 4. USING CONTEXT MANAGER
# ============================================================================
print("=" * 60)
print("4. USING CONTEXT MANAGER")
print("=" * 60)

# Context manager automatically closes connection
with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    print("  Using context manager - connection will auto-close")

print("  Connection automatically closed")

print()  # Empty line


# ============================================================================
# 5. DATABASE OPERATIONS FLOW
# ============================================================================
print("=" * 60)
print("5. DATABASE OPERATIONS FLOW")
print("=" * 60)

print("  Typical flow:")
print("    1. Connect to database")
print("    2. Create cursor")
print("    3. Execute SQL queries")
print("    4. Commit changes (for INSERT/UPDATE/DELETE)")
print("    5. Close connection")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("DATABASE BASICS SUMMARY:")
print("=" * 60)
print("  - Database connectivity allows Python to work with databases")
print("  - SQLite is built-in and great for learning")
print("  - Connect → Create cursor → Execute queries → Commit → Close")
print("  - Use context managers for automatic connection management")
print("=" * 60)

