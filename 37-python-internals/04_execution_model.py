"""
Execution Model in Python

This file demonstrates Python's execution model - frames, code objects, and execution context.
"""

import sys

# ============================================================================
# 1. CODE OBJECTS
# ============================================================================
print("=" * 60)
print("1. CODE OBJECTS")
print("=" * 60)

def example_func(x, y):
    z = x + y
    return z

print("  Functions have code objects:")
print(f"    Function name: {example_func.__code__.co_name}")
print(f"    Argument names: {example_func.__code__.co_varnames}")
print(f"    Number of arguments: {example_func.__code__.co_argcount}")
print(f"    Constants: {example_func.__code__.co_consts}")

print()  # Empty line


# ============================================================================
# 2. FRAME OBJECTS
# ============================================================================
print("=" * 60)
print("2. FRAME OBJECTS")
print("=" * 60)

def show_frame():
    frame = sys._getframe()
    print(f"    Current function: {frame.f_code.co_name}")
    print(f"    Local variables: {list(frame.f_locals.keys())}")
    print(f"    Line number: {frame.f_lineno}")

print("  Frame information:")
show_frame()

print()  # Empty line


# ============================================================================
# 3. EXECUTION STACK
# ============================================================================
print("=" * 60)
print("3. EXECUTION STACK")
print("=" * 60)

def level1():
    level2()

def level2():
    level3()

def level3():
    frame = sys._getframe()
    depth = 0
    while frame:
        print(f"    Level {depth}: {frame.f_code.co_name}")
        frame = frame.f_back
        depth += 1

print("  Call stack:")
level1()

print()  # Empty line


# ============================================================================
# 4. NAMESPACES IN FRAMES
# ============================================================================
print("=" * 60)
print("4. NAMESPACES IN FRAMES")
print("=" * 60)

def func_with_vars():
    local_var = "local"
    frame = sys._getframe()
    print(f"    Local namespace: {frame.f_locals}")
    print(f"    Global namespace keys: {list(frame.f_globals.keys())[:5]}...")

func_with_vars()

print()  # Empty line


# ============================================================================
# 5. TRACEBACKS
# ============================================================================
print("=" * 60)
print("5. TRACEBACKS")
print("=" * 60)

def func_a():
    func_b()

def func_b():
    func_c()

def func_c():
    raise ValueError("Example error")

try:
    func_a()
except ValueError as e:
    import traceback
    print("  Traceback shows execution path:")
    traceback.print_exc()

print()  # Empty line


# ============================================================================
# 6. EXECUTION CONTEXT
# ============================================================================
print("=" * 60)
print("6. EXECUTION CONTEXT")
print("=" * 60)

print("  Each function call creates:")
print("    - New frame object")
print("    - New local namespace")
print("    - Reference to global namespace")
print("    - Reference to enclosing namespace")

def outer():
    outer_var = "outer"
    
    def inner():
        frame = sys._getframe()
        print(f"    Can access outer_var: {'outer_var' in frame.f_back.f_locals}")
    
    inner()

outer()

print()  # Empty line


# ============================================================================
# 7. RECURSION AND FRAMES
# ============================================================================
print("=" * 60)
print("7. RECURSION AND FRAMES")
print("=" * 60)

def recursive(n, depth=0):
    if n > 0:
        frame = sys._getframe()
        print(f"    Depth {depth}: {frame.f_code.co_name}({n})")
        return recursive(n - 1, depth + 1)
    return depth

print("  Recursive call frames:")
result = recursive(3)
print(f"  Total depth: {result}")

print()  # Empty line


# ============================================================================
# 8. GENERATOR EXECUTION
# ============================================================================
print("=" * 60)
print("8. GENERATOR EXECUTION")
print("=" * 60)

def generator_func():
    yield 1
    yield 2
    yield 3

gen = generator_func()
print(f"  Generator object: {gen}")
print(f"  Generator code: {gen.gi_code.co_name}")
print(f"  Generator frame: {gen.gi_frame is not None}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("EXECUTION MODEL SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Functions have code objects")
print("  - Each call creates a frame")
print("  - Frames contain local namespace")
print("  - Call stack shows execution path")
print("  - Tracebacks show frame chain")
print("  - Recursion creates multiple frames")
print("=" * 60)

