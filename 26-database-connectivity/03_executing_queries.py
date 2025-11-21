"""
Executing Database Queries

This file demonstrates executing SELECT, INSERT, UPDATE, and DELETE queries.
"""

import sqlite3
import os

# Setup: Create database and table
if os.path.exists('example.db'):
    os.remove('example.db')

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT,
            age INTEGER
        )
    ''')
    conn.commit()

# ============================================================================
# 1. INSERT QUERIES
# ============================================================================
print("=" * 60)
print("1. INSERT QUERIES")
print("=" * 60)

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    
    # Insert single row
    cursor.execute(
        'INSERT INTO users (name, email, age) VALUES (?, ?, ?)',
        ('Alice', 'alice@example.com', 30)
    )
    
    # Insert multiple rows
    users = [
        ('Bob', 'bob@example.com', 25),
        ('Charlie', 'charlie@example.com', 35)
    ]
    cursor.executemany(
        'INSERT INTO users (name, email, age) VALUES (?, ?, ?)',
        users
    )
    
    conn.commit()
    print("  Inserted 3 users")

print()  # Empty line


# ============================================================================
# 2. SELECT QUERIES
# ============================================================================
print("=" * 60)
print("2. SELECT QUERIES")
print("=" * 60)

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    
    # Fetch all rows
    cursor.execute('SELECT * FROM users')
    all_rows = cursor.fetchall()
    print("  All users:")
    for row in all_rows:
        print(f"    {row}")
    
    # Fetch one row
    cursor.execute('SELECT * FROM users WHERE id = ?', (1,))
    one_row = cursor.fetchone()
    print(f"\n  User with id=1: {one_row}")
    
    # Fetch many rows
    cursor.execute('SELECT * FROM users')
    many_rows = cursor.fetchmany(2)
    print(f"\n  First 2 users: {many_rows}")

print()  # Empty line


# ============================================================================
# 3. UPDATE QUERIES
# ============================================================================
print("=" * 60)
print("3. UPDATE QUERIES")
print("=" * 60)

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    
    # Update age
    cursor.execute(
        'UPDATE users SET age = ? WHERE id = ?',
        (31, 1)
    )
    
    conn.commit()
    print("  Updated user id=1 age to 31")
    
    # Verify update
    cursor.execute('SELECT * FROM users WHERE id = ?', (1,))
    updated = cursor.fetchone()
    print(f"  Updated user: {updated}")

print()  # Empty line


# ============================================================================
# 4. DELETE QUERIES
# ============================================================================
print("=" * 60)
print("4. DELETE QUERIES")
print("=" * 60)

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    
    # Count before delete
    cursor.execute('SELECT COUNT(*) FROM users')
    count_before = cursor.fetchone()[0]
    print(f"  Users before delete: {count_before}")
    
    # Delete user
    cursor.execute('DELETE FROM users WHERE id = ?', (3,))
    conn.commit()
    
    # Count after delete
    cursor.execute('SELECT COUNT(*) FROM users')
    count_after = cursor.fetchone()[0]
    print(f"  Users after delete: {count_after}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("EXECUTING QUERIES SUMMARY:")
print("=" * 60)
print("  - INSERT: cursor.execute() or cursor.executemany()")
print("  - SELECT: cursor.execute() then fetchall/fetchone/fetchmany")
print("  - UPDATE: cursor.execute() with SET clause")
print("  - DELETE: cursor.execute() with WHERE clause")
print("  - Always commit() after INSERT/UPDATE/DELETE")
print("=" * 60)

