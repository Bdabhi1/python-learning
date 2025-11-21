"""
Naming Conventions in Python

This file demonstrates Python naming conventions and best practices.
"""

# ============================================================================
# 1. VARIABLE NAMES
# ============================================================================
print("=" * 60)
print("1. VARIABLE NAMES")
print("=" * 60)

print("  Variable naming:")
print("    - Use lowercase with underscores")
print("    - Be descriptive")
print("    - Avoid single letters (except for loops)")
print("  ")
print("  Good:")
print("    user_name = \"John\"")
print("    total_count = 100")
print("    is_active = True")
print("  ")
print("  Bad:")
print("    u = \"John\"")
print("    tc = 100")
print("    flag = True")

print()  # Empty line


# ============================================================================
# 2. FUNCTION NAMES
# ============================================================================
print("=" * 60)
print("2. FUNCTION NAMES")
print("=" * 60)

print("  Function naming:")
print("    - Use lowercase with underscores")
print("    - Use verbs (actions)")
print("    - Be descriptive")
print("  ")
print("  Good:")
print("    def calculate_total():")
print("    def get_user_by_id():")
print("    def is_valid_email():")
print("  ")
print("  Bad:")
print("    def calc():")
print("    def get():")
print("    def check():")

print()  # Empty line


# ============================================================================
# 3. CLASS NAMES
# ============================================================================
print("=" * 60)
print("3. CLASS NAMES")
print("=" * 60)

print("  Class naming:")
print("    - Use PascalCase (CapitalizedWords)")
print("    - Use nouns")
print("    - Be descriptive")
print("  ")
print("  Good:")
print("    class UserAccount:")
print("    class DatabaseConnection:")
print("    class HTTPRequestHandler:")
print("  ")
print("  Bad:")
print("    class user:")
print("    class db_conn:")
print("    class handler:")

print()  # Empty line


# ============================================================================
# 4. CONSTANTS
# ============================================================================
print("=" * 60)
print("4. CONSTANTS")
print("=" * 60)

print("  Constant naming:")
print("    - Use UPPERCASE with underscores")
print("    - For values that don't change")
print("  ")
print("  Good:")
print("    MAX_CONNECTIONS = 100")
print("    DEFAULT_TIMEOUT = 30")
print("    PI = 3.14159")
print("  ")
print("  Bad:")
print("    maxConnections = 100")
print("    default_timeout = 30")

print()  # Empty line


# ============================================================================
# 5. PRIVATE VARIABLES
# ============================================================================
print("=" * 60)
print("5. PRIVATE VARIABLES")
print("=" * 60)

print("  Private naming:")
print("    - Single underscore: \"internal use\"")
print("    - Double underscore: name mangling")
print("  ")
print("  Examples:")
print("    ")
print("    class MyClass:")
print("        _internal = 10  # Internal use")
print("        __private = 20   # Name mangling")
print("  ")
print("  Single underscore: convention (not enforced)")
print("  Double underscore: Python name mangling")

print()  # Empty line


# ============================================================================
# 6. MODULE NAMES
# ============================================================================
print("=" * 60)
print("6. MODULE NAMES")
print("=" * 60)

print("  Module naming:")
print("    - Use short, lowercase names")
print("    - Use underscores if needed")
print("    - Avoid hyphens")
print("  ")
print("  Good:")
print("    my_module.py")
print("    user_utils.py")
print("    database.py")
print("  ")
print("  Bad:")
print("    MyModule.py")
print("    user-utils.py")
print("    Database.py")

print()  # Empty line


# ============================================================================
# 7. SPECIAL METHODS
# ============================================================================
print("=" * 60)
print("7. SPECIAL METHODS")
print("=" * 60)

print("  Special method naming:")
print("    - Use double underscores")
print("    - Follow Python conventions")
print("  ")
print("  Examples:")
print("    __init__()")
print("    __str__()")
print("    __repr__()")
print("    __eq__()")
print("    __len__()")
print("  ")
print("  These are Python's magic methods")

print()  # Empty line


# ============================================================================
# 8. NAMING BEST PRACTICES
# ============================================================================
print("=" * 60)
print("8. NAMING BEST PRACTICES")
print("=" * 60)

print("  Best practices:")
print("    - Use descriptive names")
print("    - Avoid abbreviations (unless common)")
print("    - Use consistent style")
print("    - Don't use reserved words")
print("    - Use nouns for classes, verbs for functions")
print("  ")
print("  Common abbreviations (OK):")
print("    id, url, html, xml, api")
print("  ")
print("  Avoid:")
print("    def, class, import, if, else")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("NAMING CONVENTIONS SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Variables/functions: snake_case")
print("  - Classes: PascalCase")
print("  - Constants: UPPER_CASE")
print("  - Private: _single or __double underscore")
print("  - Be descriptive and consistent")
print("  - Use verbs for functions, nouns for classes")
print("=" * 60)

