"""
Practical Packaging Examples

This file demonstrates real-world packaging scenarios.
"""

# ============================================================================
# 1. SIMPLE UTILITY PACKAGE
# ============================================================================
print("=" * 60)
print("1. SIMPLE UTILITY PACKAGE")
print("=" * 60)

print("  Example: Simple utility package")
print("    ")
print("    my_utils/")
print("    ├── my_utils/")
print("    │   ├── __init__.py")
print("    │   ├── string_utils.py")
print("    │   └── math_utils.py")
print("    ├── setup.py")
print("    └── README.md")
print("  ")
print("  setup.py:")
print("    from setuptools import setup, find_packages")
print("    ")
print("    setup(")
print("        name='my_utils',")
print("        version='0.1.0',")
print("        packages=find_packages(),")
print("    )")

print()  # Empty line


# ============================================================================
# 2. PACKAGE WITH DEPENDENCIES
# ============================================================================
print("=" * 60)
print("2. PACKAGE WITH DEPENDENCIES")
print("=" * 60)

print("  Package requiring external libraries:")
print("    ")
print("    setup(")
print("        name='my_api_client',")
print("        install_requires=[")
print("            'requests>=2.25.0',")
print("            'python-dateutil>=2.8.0',")
print("        ],")
print("    )")
print("  ")
print("  Dependencies are installed automatically")

print()  # Empty line


# ============================================================================
# 3. PACKAGE WITH CLI TOOL
# ============================================================================
print("=" * 60)
print("3. PACKAGE WITH CLI TOOL")
print("=" * 60)

print("  Package with command-line interface:")
print("    ")
print("    setup(")
print("        name='my_tool',")
print("        entry_points={")
print("            'console_scripts': [")
print("                'my_command=my_tool.cli:main',")
print("            ],")
print("        },")
print("    )")
print("  ")
print("  Creates 'my_command' executable")

print()  # Empty line


# ============================================================================
# 4. PACKAGE WITH DATA FILES
# ============================================================================
print("=" * 60)
print("4. PACKAGE WITH DATA FILES")
print("=" * 60)

print("  Including data files:")
print("    ")
print("    setup(")
print("        name='my_package',")
print("        package_data={")
print("            'my_package': ['data/*.json', 'templates/*.html'],")
print("        },")
print("        include_package_data=True,")
print("    )")
print("  ")
print("  Also create MANIFEST.in:")
print("    include README.md")
print("    include LICENSE")
print("    recursive-include my_package/data *.json")

print()  # Empty line


# ============================================================================
# 5. VERSION FROM FILE
# ============================================================================
print("=" * 60)
print("5. VERSION FROM FILE")
print("=" * 60)

print("  Reading version from file:")
print("    ")
print("    # In setup.py")
print("    def get_version():")
print("        with open('VERSION') as f:")
print("            return f.read().strip()")
print("    ")
print("    setup(")
print("        version=get_version(),")
print("    )")
print("  ")
print("  Keep version in single place")

print()  # Empty line


# ============================================================================
# 6. DEVELOPMENT INSTALL
# ============================================================================
print("=" * 60)
print("6. DEVELOPMENT INSTALL")
print("=" * 60)

print("  Installing in development mode:")
print("    ")
print("    pip install -e .")
print("  ")
print("  Benefits:")
print("    - Changes to source code are immediately available")
print("    - No need to reinstall after changes")
print("    - Perfect for development")

print()  # Empty line


# ============================================================================
# 7. MULTI-PACKAGE PROJECT
# ============================================================================
print("=" * 60)
print("7. MULTI-PACKAGE PROJECT")
print("=" * 60)

print("  Project with multiple packages:")
print("    ")
print("    my_project/")
print("    ├── package1/")
print("    │   └── __init__.py")
print("    ├── package2/")
print("    │   └── __init__.py")
print("    └── setup.py")
print("    ")
print("    setup(")
print("        packages=find_packages(),")
print("    )")
print("  ")
print("  find_packages() finds all packages")

print()  # Empty line


# ============================================================================
# 8. PUBLISHING WORKFLOW
# ============================================================================
print("=" * 60)
print("8. PUBLISHING WORKFLOW")
print("=" * 60)

print("  Complete publishing workflow:")
print("    ")
print("    1. Update version")
print("    2. Update CHANGELOG")
print("    3. Clean builds: rm -rf dist/ build/")
print("    4. Build: python -m build")
print("    5. Check: twine check dist/*")
print("    6. Test install: pip install dist/my_package-*.whl")
print("    7. Upload to TestPyPI: twine upload --repository testpypi dist/*")
print("    8. Test from TestPyPI")
print("    9. Upload to PyPI: twine upload dist/*")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL PACKAGING EXAMPLES SUMMARY:")
print("=" * 60)
print("Real-world Patterns:")
print("  - Simple utility packages")
print("  - Packages with dependencies")
print("  - CLI tools with entry points")
print("  - Packages with data files")
print("  - Version management")
print("  - Development installations")
print("  - Multi-package projects")
print("  - Complete publishing workflow")
print("=" * 60)

