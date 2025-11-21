"""
contextlib Module

This file demonstrates utilities from the contextlib module.
"""

from contextlib import contextmanager, suppress, redirect_stdout
import io
import os

# ============================================================================
# 1. @contextmanager DECORATOR
# ============================================================================
print("=" * 60)
print("1. @contextmanager DECORATOR")
print("=" * 60)

@contextmanager
def file_manager(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

with file_manager('test.txt', 'w') as f:
    f.write("Test content")

print("  File created using @contextmanager")

print()  # Empty line


# ============================================================================
# 2. suppress() CONTEXT MANAGER
# ============================================================================
print("=" * 60)
print("2. suppress() CONTEXT MANAGER")
print("=" * 60)

# Suppress specific exceptions
with suppress(FileNotFoundError):
    os.remove('nonexistent.txt')
    print("  File removed")

print("  Code continues even if file doesn't exist")

print()  # Empty line


# ============================================================================
# 3. redirect_stdout() CONTEXT MANAGER
# ============================================================================
print("=" * 60)
print("3. redirect_stdout() CONTEXT MANAGER")
print("=" * 60)

f = io.StringIO()
with redirect_stdout(f):
    print("This goes to StringIO")
    print("Not to console")

content = f.getvalue()
print(f"  Captured output: {content}")

print()  # Empty line


# ============================================================================
# 4. TIMER WITH @contextmanager
# ============================================================================
print("=" * 60)
print("4. TIMER WITH @contextmanager")
print("=" * 60)

import time

@contextmanager
def timer():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"  Elapsed time: {end - start:.4f} seconds")

with timer():
    time.sleep(0.1)
    print("  Code executed")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("CONTEXTLIB MODULE SUMMARY:")
print("=" * 60)
print("  - @contextmanager: Easy way to create context managers")
print("  - suppress(): Suppress specific exceptions")
print("  - redirect_stdout(): Redirect print output")
print("  - ExitStack: Manage multiple context managers")
print("=" * 60)

