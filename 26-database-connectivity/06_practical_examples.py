"""
Practical Database Examples

This file demonstrates real-world database use cases.
"""

import sqlite3
import os

# Setup
if os.path.exists('example.db'):
    os.remove('example.db')

# ============================================================================
# 1. SIMPLE USER MANAGEMENT
# ============================================================================
print("=" * 60)
print("1. SIMPLE USER MANAGEMENT")
print("=" * 60)

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Insert users
    users = [
        ('alice', 'alice@example.com'),
        ('bob', 'bob@example.com')
    ]
    cursor.executemany(
        'INSERT INTO users (username, email) VALUES (?, ?)',
        users
    )
    conn.commit()
    
    # Query users
    cursor.execute('SELECT * FROM users')
    all_users = cursor.fetchall()
    print(f"  Total users: {len(all_users)}")

print()  # Empty line


# ============================================================================
# 2. SEARCH FUNCTIONALITY
# ============================================================================
print("=" * 60)
print("2. SEARCH FUNCTIONALITY")
print("=" * 60)

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    
    # Search by username
    search_term = 'alice'
    cursor.execute(
        'SELECT * FROM users WHERE username LIKE ?',
        (f'%{search_term}%',)
    )
    results = cursor.fetchall()
    print(f"  Search results for '{search_term}': {len(results)} found")

print()  # Empty line


# ============================================================================
# 3. COUNTING RECORDS
# ============================================================================
print("=" * 60)
print("3. COUNTING RECORDS")
print("=" * 60)

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    
    # Count all users
    cursor.execute('SELECT COUNT(*) FROM users')
    total = cursor.fetchone()[0]
    print(f"  Total users: {total}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL EXAMPLES SUMMARY:")
print("=" * 60)
print("Database operations are useful for:")
print("  - User management systems")
print("  - Data storage and retrieval")
print("  - Search functionality")
print("  - Data analytics and reporting")
print("=" * 60)

