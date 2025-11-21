"""
Database Transactions

This file demonstrates working with transactions for data integrity.
"""

import sqlite3
import os

# Setup
if os.path.exists('example.db'):
    os.remove('example.db')

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            balance REAL DEFAULT 0
        )
    ''')
    cursor.execute('INSERT INTO accounts (name, balance) VALUES (?, ?)', ('Alice', 1000.0))
    cursor.execute('INSERT INTO accounts (name, balance) VALUES (?, ?)', ('Bob', 500.0))
    conn.commit()

# ============================================================================
# 1. WHAT ARE TRANSACTIONS?
# ============================================================================
print("=" * 60)
print("1. WHAT ARE TRANSACTIONS?")
print("=" * 60)

print("  Transactions:")
print("    - Group multiple operations together")
print("    - All operations succeed or all fail (ACID)")
print("    - Ensure data integrity")
print("    - Can be rolled back on error")

print()  # Empty line


# ============================================================================
# 2. MANUAL TRANSACTION CONTROL
# ============================================================================
print("=" * 60)
print("2. MANUAL TRANSACTION CONTROL")
print("=" * 60)

conn = sqlite3.connect('example.db')
try:
    cursor = conn.cursor()
    # Transfer money from Alice to Bob
    cursor.execute('UPDATE accounts SET balance = balance - 100 WHERE name = ?', ('Alice',))
    cursor.execute('UPDATE accounts SET balance = balance + 100 WHERE name = ?', ('Bob',))
    conn.commit()
    print("  Transaction committed: Money transferred")
except Exception as e:
    conn.rollback()
    print(f"  Transaction rolled back: {e}")
finally:
    conn.close()

print()  # Empty line


# ============================================================================
# 3. CONTEXT MANAGER (AUTO-COMMIT)
# ============================================================================
print("=" * 60)
print("3. CONTEXT MANAGER (AUTO-COMMIT)")
print("=" * 60)

# Context manager auto-commits on successful exit
with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute('UPDATE accounts SET balance = balance + 50 WHERE name = ?', ('Alice',))
    print("  Auto-commit on successful exit")

print()  # Empty line


# ============================================================================
# 4. TRANSACTION WITH ERROR HANDLING
# ============================================================================
print("=" * 60)
print("4. TRANSACTION WITH ERROR HANDLING")
print("=" * 60)

with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    try:
        # Check balance
        cursor.execute('SELECT balance FROM accounts WHERE name = ?', ('Alice',))
        balance = cursor.fetchone()[0]
        
        if balance >= 200:
            cursor.execute('UPDATE accounts SET balance = balance - 200 WHERE name = ?', ('Alice',))
            cursor.execute('UPDATE accounts SET balance = balance + 200 WHERE name = ?', ('Bob',))
            conn.commit()
            print("  Transaction successful")
        else:
            print("  Insufficient balance - transaction not executed")
    except Exception as e:
        conn.rollback()
        print(f"  Error: {e}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("TRANSACTIONS SUMMARY:")
print("=" * 60)
print("  - Transactions group operations together")
print("  - commit(): Save changes")
print("  - rollback(): Undo changes")
print("  - Context manager auto-commits on success")
print("  - Use for data integrity")
print("=" * 60)

