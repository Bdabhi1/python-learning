"""
Bytecode and Compilation in Python

This file demonstrates Python bytecode and the compilation process.
"""

import dis
import ast

# ============================================================================
# 1. WHAT IS BYTECODE?
# ============================================================================
print("=" * 60)
print("1. WHAT IS BYTECODE?")
print("=" * 60)

print("  Bytecode is the intermediate representation of Python code.")
print("  It's what the Python Virtual Machine (PVM) executes.")
print("  ")
print("  Compilation process:")
print("    Source code -> AST -> Bytecode -> Execution")

print()  # Empty line


# ============================================================================
# 2. VIEWING BYTECODE
# ============================================================================
print("=" * 60)
print("2. VIEWING BYTECODE")
print("=" * 60)

def add(a, b):
    return a + b

print("  Function: add(a, b)")
print("  Bytecode:")
dis.dis(add)

print()  # Empty line


# ============================================================================
# 3. BYTECODE INSTRUCTIONS
# ============================================================================
print("=" * 60)
print("3. BYTECODE INSTRUCTIONS")
print("=" * 60)

def example():
    x = 1
    y = 2
    z = x + y
    return z

print("  Function bytecode:")
dis.dis(example)
print("  ")
print("  Common instructions:")
print("    LOAD_CONST: Load constant")
print("    STORE_FAST: Store in local variable")
print("    LOAD_FAST: Load local variable")
print("    BINARY_ADD: Add two values")
print("    RETURN_VALUE: Return value")

print()  # Empty line


# ============================================================================
# 4. AST (ABSTRACT SYNTAX TREE)
# ============================================================================
print("=" * 60)
print("4. AST (ABSTRACT SYNTAX TREE)")
print("=" * 60)

code = "x = 1 + 2"
tree = ast.parse(code)

print(f"  Source code: {code}")
print("  AST dump:")
print(ast.dump(tree, indent=2))

print()  # Empty line


# ============================================================================
# 5. COMPILING CODE
# ============================================================================
print("=" * 60)
print("5. COMPILING CODE")
print("=" * 60)

code_str = """
def greet(name):
    return f"Hello, {name}!"
"""

print("  Compiling code string:")
code_obj = compile(code_str, "<string>", "exec")
print(f"  Code object: {code_obj}")
print(f"  Code object type: {type(code_obj)}")

# Execute compiled code
exec(code_obj)
print("  Executed compiled code")
print(f"  greet('World'): {greet('World')}")

print()  # Empty line


# ============================================================================
# 6. .pyc FILES
# ============================================================================
print("=" * 60)
print("6. .pyc FILES")
print("=" * 60)

print("  Python automatically creates .pyc files:")
print("    - Stored in __pycache__/ directory")
print("    - Contains compiled bytecode")
print("    - Faster loading on subsequent runs")
print("    - Created automatically by Python")
print("  ")
print("  Check for __pycache__ directory in your project")

print()  # Empty line


# ============================================================================
# 7. CODE OBJECT ATTRIBUTES
# ============================================================================
print("=" * 60)
print("7. CODE OBJECT ATTRIBUTES")
print("=" * 60)

def sample_function(x, y):
    z = x + y
    return z

code_obj = sample_function.__code__

print("  Code object attributes:")
print(f"    co_name: {code_obj.co_name}")
print(f"    co_argcount: {code_obj.co_argcount}")
print(f"    co_varnames: {code_obj.co_varnames}")
print(f"    co_consts: {code_obj.co_consts}")
print(f"    co_code: {code_obj.co_code}")

print()  # Empty line


# ============================================================================
# 8. COMPARING BYTECODE
# ============================================================================
print("=" * 60)
print("8. COMPARING BYTECODE")
print("=" * 60)

def version1():
    result = []
    for i in range(10):
        result.append(i * 2)
    return result

def version2():
    return [i * 2 for i in range(10)]

print("  Version 1 (loop):")
dis.dis(version1)
print("  ")
print("  Version 2 (list comprehension):")
dis.dis(version2)
print("  ")
print("  List comprehension is more efficient")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("BYTECODE SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Bytecode is intermediate representation")
print("  - Use dis.dis() to view bytecode")
print("  - AST is created before bytecode")
print("  - .pyc files cache bytecode")
print("  - Code objects contain bytecode")
print("  - Understanding bytecode helps optimization")
print("=" * 60)

