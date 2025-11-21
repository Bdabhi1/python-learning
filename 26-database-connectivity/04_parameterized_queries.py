"""
Parameterized Queries

This file demonstrates using parameterized queries to prevent SQL injection.
"""

import sqlite3
import os

# Setup
if os.path.exists('example.db'):
    os.remove('example.db')

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT
        )
    ''')
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', ('Alice', 'alice@example.com'))
    conn.commit()

# ============================================================================
# 1. WHY PARAMETERIZED QUERIES?
# ============================================================================
print("=" * 60)
print("1. WHY PARAMETERIZED QUERIES?")
print("=" * 60)

print("  Parameterized queries:")
print("    - Prevent SQL injection attacks")
print("    - Handle special characters safely")
print("    - Improve performance (query caching)")
print("    - Make code more readable")

print()  # Empty line


# ============================================================================
# 2. USING PLACEHOLDERS
# ============================================================================
print("=" * 60)
print("2. USING PLACEHOLDERS")
print("=" * 60)

name = "Alice"

# SQLite uses ? placeholders
with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
    result = cursor.fetchone()
    print(f"  Found user: {result}")

print()  # Empty line


# ============================================================================
# 3. MULTIPLE PARAMETERS
# ============================================================================
print("=" * 60)
print("3. MULTIPLE PARAMETERS")
print("=" * 60)

name = "Alice"
email = "alice@example.com"

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute(
        'SELECT * FROM users WHERE name = ? AND email = ?',
        (name, email)
    )
    result = cursor.fetchone()
    print(f"  Found user with name and email: {result}")

print()  # Empty line


# ============================================================================
# 4. NAMED PARAMETERS
# ============================================================================
print("=" * 60)
print("4. NAMED PARAMETERS")
print("=" * 60)

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute(
        'SELECT * FROM users WHERE name = :name',
        {'name': 'Alice'}
    )
    result = cursor.fetchone()
    print(f"  Found user with named parameter: {result}")

print()  # Empty line


# ============================================================================
# 5. SQL INJECTION PREVENTION
# ============================================================================
print("=" * 60)
print("5. SQL INJECTION PREVENTION")
print("=" * 60)

print("  NEVER do this (vulnerable to SQL injection):")
print("    name = \"'; DROP TABLE users; --\"")
print("    query = f\"SELECT * FROM users WHERE name = '{name}'\"")
print("  ")
print("  ALWAYS use parameterized queries:")
print("    cursor.execute('SELECT * FROM users WHERE name = ?', (name,))")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PARAMETERIZED QUERIES SUMMARY:")
print("=" * 60)
print("  - Always use parameterized queries")
print("  - SQLite uses ? placeholders")
print("  - Can use named parameters (:name)")
print("  - Prevents SQL injection attacks")
print("  - Handles special characters safely")
print("=" * 60)

