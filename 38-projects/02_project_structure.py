"""
Project Structure in Python

This file demonstrates how to organize a Python project.
"""

import os

# ============================================================================
# 1. STANDARD PROJECT STRUCTURE
# ============================================================================
print("=" * 60)
print("1. STANDARD PROJECT STRUCTURE")
print("=" * 60)

print("  Standard project structure:")
print("    ")
print("    project_name/")
print("    ├── README.md")
print("    ├── requirements.txt")
print("    ├── .gitignore")
print("    ├── LICENSE")
print("    ├── setup.py (or pyproject.toml)")
print("    ├── src/")
print("    │   └── project_name/")
print("    │       ├── __init__.py")
print("    │       ├── main.py")
print("    │       └── modules/")
print("    ├── tests/")
print("    │   ├── __init__.py")
print("    │   └── test_main.py")
print("    ├── docs/")
print("    └── data/ (if needed)")

print()  # Empty line


# ============================================================================
# 2. README.md
# ============================================================================
print("=" * 60)
print("2. README.md")
print("=" * 60)

print("  README.md should include:")
print("    - Project description")
print("    - Installation instructions")
print("    - Usage examples")
print("    - Features list")
print("    - Contributing guidelines")
print("    - License information")
print("  ")
print("  Example structure:")
print("    # Project Name")
print("    ")
print("    Brief description")
print("    ")
print("    ## Installation")
print("    pip install -r requirements.txt")
print("    ")
print("    ## Usage")
print("    python main.py")

print()  # Empty line


# ============================================================================
# 3. requirements.txt
# ============================================================================
print("=" * 60)
print("3. requirements.txt")
print("=" * 60)

print("  requirements.txt lists dependencies:")
print("    ")
print("    requests>=2.25.0")
print("    flask==2.0.1")
print("    numpy>=1.20.0")
print("  ")
print("  Install with:")
print("    pip install -r requirements.txt")
print("  ")
print("  Generate from current environment:")
print("    pip freeze > requirements.txt")

print()  # Empty line


# ============================================================================
# 4. .gitignore
# ============================================================================
print("=" * 60)
print("4. .gitignore")
print("=" * 60)

print("  .gitignore excludes files from git:")
print("    ")
print("    # Python")
print("    __pycache__/")
print("    *.py[cod]")
print("    *.so")
print("    .Python")
print("    ")
print("    # Virtual environment")
print("    venv/")
print("    env/")
print("    ")
print("    # IDE")
print("    .vscode/")
print("    .idea/")
print("    ")
print("    # Environment variables")
print("    .env")

print()  # Empty line


# ============================================================================
# 5. SOURCE CODE ORGANIZATION
# ============================================================================
print("=" * 60)
print("5. SOURCE CODE ORGANIZATION")
print("=" * 60)

print("  Organize source code:")
print("    ")
print("    src/project_name/")
print("    ├── __init__.py")
print("    ├── main.py          # Entry point")
print("    ├── config.py        # Configuration")
print("    ├── models.py         # Data models")
print("    ├── utils.py          # Utility functions")
print("    └── modules/          # Feature modules")
print("        ├── __init__.py")
print("        └── feature1.py")
print("  ")
print("  Keep related code together")

print()  # Empty line


# ============================================================================
# 6. TEST STRUCTURE
# ============================================================================
print("=" * 60)
print("6. TEST STRUCTURE")
print("=" * 60)

print("  Test directory structure:")
print("    ")
print("    tests/")
print("    ├── __init__.py")
print("    ├── test_main.py")
print("    ├── test_models.py")
print("    └── test_utils.py")
print("  ")
print("  Mirror source structure:")
print("    tests/")
print("    └── project_name/")
print("        ├── test_main.py")
print("        └── test_utils.py")

print()  # Empty line


# ============================================================================
# 7. DOCUMENTATION STRUCTURE
# ============================================================================
print("=" * 60)
print("7. DOCUMENTATION STRUCTURE")
print("=" * 60)

print("  Documentation organization:")
print("    ")
print("    docs/")
print("    ├── README.md")
print("    ├── installation.md")
print("    ├── usage.md")
print("    ├── api.md")
print("    └── examples/")
print("  ")
print("  Keep documentation up to date")

print()  # Empty line


# ============================================================================
# 8. SETUP.PY OR pyproject.toml
# ============================================================================
print("=" * 60)
print("8. SETUP.PY OR pyproject.toml")
print("=" * 60)

print("  For installable packages:")
print("    ")
print("    setup.py or pyproject.toml")
print("    - Package metadata")
print("    - Dependencies")
print("    - Entry points")
print("  ")
print("  Allows installation with:")
print("    pip install -e .")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PROJECT STRUCTURE SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Follow standard project structure")
print("  - Include README.md with clear instructions")
print("  - List dependencies in requirements.txt")
print("  - Use .gitignore for version control")
print("  - Organize source code logically")
print("  - Structure tests properly")
print("  - Include documentation")
print("=" * 60)

