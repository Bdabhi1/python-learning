"""
setup.py for Python Packages

This file demonstrates how to create setup.py files for packaging.
"""

# ============================================================================
# 1. WHAT IS setup.py?
# ============================================================================
print("=" * 60)
print("1. WHAT IS setup.py?")
print("=" * 60)

print("  setup.py is a Python file that describes your package.")
print("  It contains metadata and configuration for distribution.")
print("  ")
print("  Key information:")
print("    - Package name and version")
print("    - Author information")
print("    - Dependencies")
print("    - Package contents")

print()  # Empty line


# ============================================================================
# 2. BASIC setup.py
# ============================================================================
print("=" * 60)
print("2. BASIC setup.py")
print("=" * 60)

print("  Basic setup.py example:")
print("    ")
print("    from setuptools import setup")
print("    ")
print("    setup(")
print("        name='my_package',")
print("        version='0.1.0',")
print("        description='A sample package',")
print("        author='Your Name',")
print("        author_email='your.email@example.com',")
print("        py_modules=['my_module'],")
print("    )")

print()  # Empty line


# ============================================================================
# 3. COMPLETE setup.py
# ============================================================================
print("=" * 60)
print("3. COMPLETE setup.py")
print("=" * 60)

print("  Complete setup.py example:")
print("    ")
print("    from setuptools import setup, find_packages")
print("    ")
print("    with open('README.md') as f:")
print("        long_description = f.read()")
print("    ")
print("    setup(")
print("        name='my_package',")
print("        version='0.1.0',")
print("        description='A sample Python package',")
print("        long_description=long_description,")
print("        long_description_content_type='text/markdown',")
print("        author='Your Name',")
print("        author_email='your.email@example.com',")
print("        url='https://github.com/username/my_package',")
print("        packages=find_packages(),")
print("        install_requires=[")
print("            'requests>=2.25.0',")
print("            'numpy>=1.20.0',")
print("        ],")
print("        classifiers=[")
print("            'Development Status :: 3 - Alpha',")
print("            'Intended Audience :: Developers',")
print("            'License :: OSI Approved :: MIT License',")
print("            'Programming Language :: Python :: 3',")
print("        ],")
print("        python_requires='>=3.8',")
print("    )")

print()  # Empty line


# ============================================================================
# 4. FINDING PACKAGES
# ============================================================================
print("=" * 60)
print("4. FINDING PACKAGES")
print("=" * 60)

print("  Using find_packages():")
print("    ")
print("    from setuptools import setup, find_packages")
print("    ")
print("    setup(")
print("        name='my_package',")
print("        packages=find_packages(),  # Automatically finds all packages")
print("    )")
print("  ")
print("  find_packages() automatically discovers:")
print("    - All directories with __init__.py")
print("    - Excludes test directories by default")
print("    - Can specify include/exclude patterns")

print()  # Empty line


# ============================================================================
# 5. DEPENDENCIES
# ============================================================================
print("=" * 60)
print("5. DEPENDENCIES")
print("=" * 60)

print("  Specifying dependencies:")
print("    ")
print("    setup(")
print("        name='my_package',")
print("        install_requires=[")
print("            'requests>=2.25.0',  # Minimum version")
print("            'numpy>=1.20.0,<2.0.0',  # Version range")
print("            'pandas',  # Any version")
print("        ],")
print("        extras_require={")
print("            'dev': ['pytest', 'black'],")
print("            'docs': ['sphinx'],")
print("        },")
print("    )")
print("  ")
print("  install_requires: Required dependencies")
print("  extras_require: Optional dependencies")

print()  # Empty line


# ============================================================================
# 6. ENTRY POINTS
# ============================================================================
print("=" * 60)
print("6. ENTRY POINTS")
print("=" * 60)

print("  Creating command-line scripts:")
print("    ")
print("    setup(")
print("        name='my_package',")
print("        entry_points={")
print("            'console_scripts': [")
print("                'my_command=my_package.cli:main',")
print("            ],")
print("        },")
print("    )")
print("  ")
print("  This creates a 'my_command' executable")
print("  that calls my_package.cli.main()")

print()  # Empty line


# ============================================================================
# 7. INCLUDING DATA FILES
# ============================================================================
print("=" * 60)
print("7. INCLUDING DATA FILES")
print("=" * 60)

print("  Including non-Python files:")
print("    ")
print("    setup(")
print("        name='my_package',")
print("        packages=find_packages(),")
print("        package_data={")
print("            'my_package': ['data/*.json', 'templates/*.html'],")
print("        },")
print("        include_package_data=True,")
print("    )")
print("  ")
print("  Also create MANIFEST.in file:")
print("    include README.md")
print("    include LICENSE")
print("    recursive-include my_package/data *.json")

print()  # Empty line


# ============================================================================
# 8. VERSION MANAGEMENT
# ============================================================================
print("=" * 60)
print("8. VERSION MANAGEMENT")
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
print("  Or from __init__.py:")
print("    ")
print("    import my_package")
print("    setup(")
print("        version=my_package.__version__,")
print("    )")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("setup.py SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - setup.py describes your package")
print("  - Use find_packages() to auto-discover packages")
print("  - Specify dependencies in install_requires")
print("  - Use entry_points for CLI scripts")
print("  - Include data files with package_data")
print("  - Read version from file or __init__.py")
print("  - Include README and LICENSE")
print("=" * 60)

