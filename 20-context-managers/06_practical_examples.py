"""
Practical Context Manager Examples

This file demonstrates real-world context manager use cases.
"""

import time
from contextlib import contextmanager

# ============================================================================
# 1. DATABASE CONNECTION PATTERN
# ============================================================================
print("=" * 60)
print("1. DATABASE CONNECTION PATTERN")
print("=" * 60)

class DatabaseConnection:
    def __enter__(self):
        print("  Connecting to database...")
        self.connected = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("  Closing database connection...")
        self.connected = False
        return False
    
    def query(self, sql):
        print(f"  Executing: {sql}")

with DatabaseConnection() as db:
    db.query("SELECT * FROM users")

print()  # Empty line


# ============================================================================
# 2. TEMPORARY DIRECTORY
# ============================================================================
print("=" * 60)
print("2. TEMPORARY DIRECTORY")
print("=" * 60)

import tempfile
import os

@contextmanager
def temp_directory():
    temp_dir = tempfile.mkdtemp()
    try:
        yield temp_dir
    finally:
        import shutil
        shutil.rmtree(temp_dir)
        print(f"  Temporary directory removed: {temp_dir}")

with temp_directory() as temp_dir:
    print(f"  Created temp directory: {temp_dir}")
    file_path = os.path.join(temp_dir, 'test.txt')
    with open(file_path, 'w') as f:
        f.write("Test")

print()  # Empty line


# ============================================================================
# 3. PERFORMANCE MONITORING
# ============================================================================
print("=" * 60)
print("3. PERFORMANCE MONITORING")
print("=" * 60)

@contextmanager
def performance_monitor(operation_name):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"  {operation_name} took {end - start:.4f} seconds")

with performance_monitor("Data processing"):
    time.sleep(0.1)
    print("  Processing data...")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL EXAMPLES SUMMARY:")
print("=" * 60)
print("Context managers are useful for:")
print("  - File and resource management")
print("  - Database connections")
print("  - Temporary resources")
print("  - Performance monitoring")
print("  - Locks and synchronization")
print("=" * 60)

