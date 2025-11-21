"""
Custom Context Managers

This file demonstrates how to create custom context manager classes.
"""

import time

# ============================================================================
# 1. BASIC CUSTOM CONTEXT MANAGER
# ============================================================================
print("=" * 60)
print("1. BASIC CUSTOM CONTEXT MANAGER")
print("=" * 60)

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False  # Don't suppress exceptions

# Usage
with FileManager('test.txt', 'w') as f:
    f.write("Test content")

print("  File created and closed automatically")

print()  # Empty line


# ============================================================================
# 2. TIMER CONTEXT MANAGER
# ============================================================================
print("=" * 60)
print("2. TIMER CONTEXT MANAGER")
print("=" * 60)

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        elapsed = self.end - self.start
        print(f"  Elapsed time: {elapsed:.4f} seconds")
        return False

with Timer():
    time.sleep(0.1)
    print("  Code executed")

print()  # Empty line


# ============================================================================
# 3. CONTEXT MANAGER WITH EXCEPTION HANDLING
# ============================================================================
print("=" * 60)
print("3. CONTEXT MANAGER WITH EXCEPTION HANDLING")
print("=" * 60)

class SuppressExceptions:
    def __init__(self, exception_type):
        self.exception_type = exception_type
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type == self.exception_type:
            print(f"  Suppressed {exc_type.__name__}: {exc_val}")
            return True  # Suppress exception
        return False  # Don't suppress other exceptions

with SuppressExceptions(ValueError):
    raise ValueError("This error is suppressed")

print("  Code continues after suppressed exception")

print()  # Empty line


# ============================================================================
# 4. RESOURCE LOCK CONTEXT MANAGER
# ============================================================================
print("=" * 60)
print("4. RESOURCE LOCK CONTEXT MANAGER")
print("=" * 60)

class Lock:
    def __init__(self):
        self.locked = False
    
    def __enter__(self):
        self.locked = True
        print("  Resource locked")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.locked = False
        print("  Resource unlocked")
        return False

with Lock():
    print("  Working with locked resource")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("CUSTOM CONTEXT MANAGERS SUMMARY:")
print("=" * 60)
print("  - Implement __enter__() and __exit__() methods")
print("  - __enter__() can return a value")
print("  - __exit__() receives exception info")
print("  - Return True from __exit__() to suppress exceptions")
print("  - Return False to let exceptions propagate")
print("=" * 60)

