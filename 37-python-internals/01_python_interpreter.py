"""
Python Interpreter Basics

This file demonstrates how the Python interpreter works.
"""

import sys

# ============================================================================
# 1. WHAT IS THE PYTHON INTERPRETER?
# ============================================================================
print("=" * 60)
print("1. WHAT IS THE PYTHON INTERPRETER?")
print("=" * 60)

print("  The Python interpreter (CPython) is the program that")
print("  executes Python code.")
print("  ")
print("  Steps:")
print("    1. Lexical Analysis (tokenization)")
print("    2. Parsing (AST creation)")
print("    3. Compilation (bytecode generation)")
print("    4. Execution (PVM runs bytecode)")

print()  # Empty line


# ============================================================================
# 2. INTERPRETER INFORMATION
# ============================================================================
print("=" * 60)
print("2. INTERPRETER INFORMATION")
print("=" * 60)

print(f"  Python version: {sys.version}")
print(f"  Python executable: {sys.executable}")
print(f"  Platform: {sys.platform}")
print(f"  Implementation: {sys.implementation.name}")

print()  # Empty line


# ============================================================================
# 3. CODE EXECUTION
# ============================================================================
print("=" * 60)
print("3. CODE EXECUTION")
print("=" * 60)

print("  When you run Python code:")
print("    ")
print("    1. Source code is read")
print("    2. Parsed into Abstract Syntax Tree (AST)")
print("    3. Compiled to bytecode")
print("    4. Bytecode is executed by Python Virtual Machine (PVM)")
print("  ")
print("  Example:")
print("    x = 42")
print("    # Interpreter processes this line by line")

x = 42
print(f"    Result: x = {x}")

print()  # Empty line


# ============================================================================
# 4. PYTHON VIRTUAL MACHINE (PVM)
# ============================================================================
print("=" * 60)
print("4. PYTHON VIRTUAL MACHINE (PVM)")
print("=" * 60)

print("  PVM is a stack-based virtual machine")
print("  that executes bytecode instructions.")
print("  ")
print("  Bytecode is stored in .pyc files")
print("  in __pycache__ directories")

print()  # Empty line


# ============================================================================
# 5. INTERACTIVE MODE
# ============================================================================
print("=" * 60)
print("5. INTERACTIVE MODE")
print("=" * 60)

print("  Python can run in interactive mode:")
print("    ")
print("    $ python")
print("    >>> print('Hello')")
print("    Hello")
print("    >>>")
print("  ")
print("  Or as a script:")
print("    ")
print("    $ python script.py")

print()  # Empty line


# ============================================================================
# 6. MODULE EXECUTION
# ============================================================================
print("=" * 60)
print("6. MODULE EXECUTION")
print("=" * 60)

print("  When a module is imported:")
print("    1. Python searches for the module")
print("    2. Compiles to bytecode if needed")
print("    3. Executes the module code")
print("    4. Creates module object")
print("  ")
print("  __pycache__ contains compiled .pyc files")

print()  # Empty line


# ============================================================================
# 7. INTERPRETER OPTIONS
# ============================================================================
print("=" * 60)
print("7. INTERPRETER OPTIONS")
print("=" * 60)

print("  Common Python interpreter options:")
print("    ")
print("    python -c 'code'     # Execute code string")
print("    python -m module     # Run module as script")
print("    python -i script.py  # Interactive mode after script")
print("    python -O script.py  # Optimize (remove asserts)")
print("    python -u script.py  # Unbuffered output")

print()  # Empty line


# ============================================================================
# 8. EXECUTION ENVIRONMENT
# ============================================================================
print("=" * 60)
print("8. EXECUTION ENVIRONMENT")
print("=" * 60)

print("  Execution environment includes:")
print(f"    - sys.path: {sys.path[:3]}...")
print(f"    - sys.argv: {sys.argv}")
print(f"    - __name__: {__name__}")
print("  ")
print("  Each script/module has its own namespace")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PYTHON INTERPRETER SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - CPython is the reference implementation")
print("  - Code goes through: parse -> compile -> execute")
print("  - PVM executes bytecode")
print("  - .pyc files store compiled bytecode")
print("  - Interactive and script modes available")
print("=" * 60)

