"""
SQLite Connection

This file demonstrates connecting to SQLite databases and creating tables.
"""

import sqlite3
import os

# ============================================================================
# 1. CREATING DATABASE AND TABLE
# ============================================================================
print("=" * 60)
print("1. CREATING DATABASE AND TABLE")
print("=" * 60)

# Remove existing database
if os.path.exists('example.db'):
    os.remove('example.db')

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            age INTEGER
        )
    ''')
    
    conn.commit()
    print("  Table 'users' created successfully")

print()  # Empty line


# ============================================================================
# 2. IN-MEMORY DATABASE
# ============================================================================
print("=" * 60)
print("2. IN-MEMORY DATABASE")
print("=" * 60)

# In-memory database (temporary)
with sqlite3.connect(':memory:') as conn:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE test (
            id INTEGER PRIMARY KEY,
            value TEXT
        )
    ''')
    print("  In-memory database created")
    print("  (Database exists only during connection)")

print()  # Empty line


# ============================================================================
# 3. CONNECTION OPTIONS
# ============================================================================
print("=" * 60)
print("3. CONNECTION OPTIONS")
print("=" * 60)

# Connection with timeout
conn = sqlite3.connect('example.db', timeout=5.0)
print("  Connected with 5 second timeout")
conn.close()

# Connection with row factory (returns dict-like rows)
conn = sqlite3.connect('example.db')
conn.row_factory = sqlite3.Row
print("  Row factory set to return dict-like rows")
conn.close()

print()  # Empty line


# ============================================================================
# 4. CHECKING CONNECTION
# ============================================================================
print("=" * 60)
print("4. CHECKING CONNECTION")
print("=" * 60)

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    
    # Check if table exists
    cursor.execute('''
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name='users'
    ''')
    table_exists = cursor.fetchone()
    
    if table_exists:
        print("  Table 'users' exists")
    else:
        print("  Table 'users' does not exist")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("SQLITE CONNECTION SUMMARY:")
print("=" * 60)
print("  - sqlite3.connect(): Connect to database")
print("  - ':memory:': In-memory database")
print("  - timeout: Set connection timeout")
print("  - row_factory: Customize row format")
print("  - Always use context managers")
print("=" * 60)

