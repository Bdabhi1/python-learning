"""
Working with File Paths in Python

This file demonstrates how to work with file paths, including
absolute paths, relative paths, and path manipulation.
"""

# ============================================================================
# 1. CURRENT WORKING DIRECTORY
# ============================================================================
print("=" * 60)
print("1. CURRENT WORKING DIRECTORY")
print("=" * 60)

import os

# Get current working directory
cwd = os.getcwd()
print(f"  Current directory: {cwd}")

# Change directory (if needed)
# os.chdir('/path/to/directory')

print("\n  os.getcwd() - Get current working directory")
print("  os.chdir(path) - Change directory")

print()  # Empty line


# ============================================================================
# 2. ABSOLUTE VS RELATIVE PATHS
# ============================================================================
print("=" * 60)
print("2. ABSOLUTE VS RELATIVE PATHS")
print("=" * 60)

# Relative path
relative_path = "data.txt"
print(f"  Relative path: {relative_path}")

# Absolute path
absolute_path = os.path.abspath(relative_path)
print(f"  Absolute path: {absolute_path}")

print("\n  Relative: From current directory")
print("  Absolute: Full path from root")

print()  # Empty line


# ============================================================================
# 3. JOINING PATHS
# ============================================================================
print("=" * 60)
print("3. JOINING PATHS")
print("=" * 60)

# Join paths (cross-platform)
path1 = os.path.join("folder", "subfolder", "file.txt")
print(f"  Joined path: {path1}")

# Multiple joins
base = "project"
subdir = "data"
filename = "output.txt"
full_path = os.path.join(base, subdir, filename)
print(f"  Full path: {full_path}")

print("\n  os.path.join() - Join paths (handles OS differences)")

print()  # Empty line


# ============================================================================
# 4. PATH COMPONENTS
# ============================================================================
print("=" * 60)
print("4. PATH COMPONENTS")
print("=" * 60)

# Example path
example_path = "/Users/username/project/data/file.txt"

# Get directory name
directory = os.path.dirname(example_path)
print(f"  Directory: {directory}")

# Get filename
filename = os.path.basename(example_path)
print(f"  Filename: {filename}")

# Split path
head, tail = os.path.split(example_path)
print(f"  Head: {head}")
print(f"  Tail: {tail}")

# Split extension
name, ext = os.path.splitext(example_path)
print(f"  Name: {name}")
print(f"  Extension: {ext}")

print()  # Empty line


# ============================================================================
# 5. PATHLIB (MODERN APPROACH)
# ============================================================================
print("=" * 60)
print("5. PATHLIB (MODERN APPROACH)")
print("=" * 60)

from pathlib import Path

# Create Path object
path = Path("folder") / "subfolder" / "file.txt"
print(f"  Path object: {path}")

# Get parts
print(f"  Parts: {path.parts}")
print(f"  Name: {path.name}")
print(f"  Stem: {path.stem}")
print(f"  Suffix: {path.suffix}")
print(f"  Parent: {path.parent}")

print("\n  pathlib.Path - Modern, object-oriented path handling")

print()  # Empty line


# ============================================================================
# 6. CHECKING PATH EXISTENCE
# ============================================================================
print("=" * 60)
print("6. CHECKING PATH EXISTENCE")
print("=" * 60)

# Check if path exists
test_file = "test_path.txt"
with open(test_file, "w") as f:
    f.write("test")

exists = os.path.exists(test_file)
print(f"  os.path.exists('{test_file}'): {exists}")

# Check if file
is_file = os.path.isfile(test_file)
print(f"  os.path.isfile('{test_file}'): {is_file}")

# Check if directory
is_dir = os.path.isdir(".")
print(f"  os.path.isdir('.'): {is_dir}")

# Using pathlib
path_obj = Path(test_file)
print(f"  Path('{test_file}').exists(): {path_obj.exists()}")

# Clean up
os.remove(test_file)

print()  # Empty line


# ============================================================================
# 7. LISTING DIRECTORY CONTENTS
# ============================================================================
print("=" * 60)
print("7. LISTING DIRECTORY CONTENTS")
print("=" * 60)

# List directory
items = os.listdir(".")
print(f"  Current directory items (first 5):")
for item in items[:5]:
    print(f"    {item}")

# List with pathlib
path = Path(".")
items = list(path.iterdir())[:5]
print(f"  Using pathlib (first 5):")
for item in items:
    print(f"    {item}")

print()  # Empty line


# ============================================================================
# 8. PATH MANIPULATION
# ============================================================================
print("=" * 60)
print("8. PATH MANIPULATION")
print("=" * 60)

# Get absolute path
relative = "data.txt"
absolute = os.path.abspath(relative)
print(f"  Absolute: {absolute}")

# Normalize path
path_with_dots = "folder/../other_folder/./file.txt"
normalized = os.path.normpath(path_with_dots)
print(f"  Normalized: {normalized}")

# Expand user home
home_path = os.path.expanduser("~/Documents")
print(f"  Home path: {home_path}")

print()  # Empty line


# ============================================================================
# 9. CREATING DIRECTORIES
# ============================================================================
print("=" * 60)
print("9. CREATING DIRECTORIES")
print("=" * 60)

# Create directory
test_dir = "test_directory"
if not os.path.exists(test_dir):
    os.mkdir(test_dir)
    print(f"  Created directory: {test_dir}")

# Create nested directories
nested_dir = os.path.join("parent", "child", "grandchild")
os.makedirs(nested_dir, exist_ok=True)
print(f"  Created nested directories: {nested_dir}")

# Clean up
import shutil
if os.path.exists(test_dir):
    os.rmdir(test_dir)
if os.path.exists("parent"):
    shutil.rmtree("parent")

print()  # Empty line


# ============================================================================
# 10. PRACTICAL EXAMPLES
# ============================================================================
print("=" * 60)
print("10. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Build file path
base_dir = "data"
subdir = "2024"
filename = "report.txt"
file_path = os.path.join(base_dir, subdir, filename)
print(f"  File path: {file_path}")

# Example 2: Check and create directory
if not os.path.exists(base_dir):
    os.makedirs(base_dir)
    print(f"  Created directory: {base_dir}")

# Example 3: Get file info
if os.path.exists(__file__):
    size = os.path.getsize(__file__)
    print(f"  Current file size: {size} bytes")

# Example 4: Using pathlib
from pathlib import Path
data_path = Path("data") / "2024" / "report.txt"
print(f"  Pathlib path: {data_path}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("FILE PATHS SUMMARY:")
print("=" * 60)
print("Key Functions:")
print("  - os.getcwd() - Current directory")
print("  - os.path.join() - Join paths")
print("  - os.path.exists() - Check if exists")
print("  - os.path.dirname() - Get directory")
print("  - os.path.basename() - Get filename")
print("  - os.path.splitext() - Split extension")
print("\nModern Approach:")
print("  - pathlib.Path - Object-oriented paths")
print("  - Path('/') / 'folder' / 'file.txt'")
print("  - path.exists(), path.mkdir(), etc.")
print("\nBest Practices:")
print("  - Use os.path.join() for cross-platform")
print("  - Check if path exists before operations")
print("  - Use absolute paths when needed")
print("=" * 60)

