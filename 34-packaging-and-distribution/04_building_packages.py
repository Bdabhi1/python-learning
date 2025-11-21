"""
Building Python Packages

This file demonstrates how to build distribution files for packages.
"""

# ============================================================================
# 1. WHAT IS BUILDING?
# ============================================================================
print("=" * 60)
print("1. WHAT IS BUILDING?")
print("=" * 60)

print("  Building creates distribution files from your package.")
print("  These files can be installed or published to PyPI.")
print("  ")
print("  Distribution types:")
print("    - Source distribution (.tar.gz)")
print("    - Wheel distribution (.whl)")

print()  # Empty line


# ============================================================================
# 2. BUILDING WITH setup.py
# ============================================================================
print("=" * 60)
print("2. BUILDING WITH setup.py")
print("=" * 60)

print("  Building source distribution:")
print("    python setup.py sdist")
print("  ")
print("  Building wheel:")
print("    python setup.py bdist_wheel")
print("  ")
print("  Building both:")
print("    python setup.py sdist bdist_wheel")
print("  ")
print("  Files are created in dist/ directory")

print()  # Empty line


# ============================================================================
# 3. BUILDING WITH build TOOL
# ============================================================================
print("=" * 60)
print("3. BUILDING WITH build TOOL")
print("=" * 60)

print("  Install build tool:")
print("    pip install build")
print("  ")
print("  Build package:")
print("    python -m build")
print("  ")
print("  This creates both:")
print("    - Source distribution (.tar.gz)")
print("    - Wheel distribution (.whl)")
print("  ")
print("  Recommended method (works with pyproject.toml)")

print()  # Empty line


# ============================================================================
# 4. SOURCE DISTRIBUTION
# ============================================================================
print("=" * 60)
print("4. SOURCE DISTRIBUTION")
print("=" * 60)

print("  Source distribution (sdist):")
print("    - Contains source code")
print("    - .tar.gz file")
print("    - Requires build tools to install")
print("    - More portable")
print("  ")
print("  Create with:")
print("    python setup.py sdist")
print("    # or")
print("    python -m build --sdist")

print()  # Empty line


# ============================================================================
# 5. WHEEL DISTRIBUTION
# ============================================================================
print("=" * 60)
print("5. WHEEL DISTRIBUTION")
print("=" * 60)

print("  Wheel distribution:")
print("    - Pre-built package")
print("    - .whl file")
print("    - Faster to install")
print("    - Platform-specific or universal")
print("  ")
print("  Create with:")
print("    python setup.py bdist_wheel")
print("    # or")
print("    python -m build --wheel")
print("  ")
print("  Universal wheel: py3-none-any.whl")
print("  Platform wheel: cp38-cp38-win_amd64.whl")

print()  # Empty line


# ============================================================================
# 6. CLEANING BUILDS
# ============================================================================
print("=" * 60)
print("6. CLEANING BUILDS")
print("=" * 60)

print("  Clean previous builds:")
print("    ")
print("    # Remove build artifacts")
print("    rm -rf build/")
print("    rm -rf dist/")
print("    rm -rf *.egg-info")
print("    ")
print("    # Or use setup.py")
print("    python setup.py clean --all")
print("  ")
print("  Always clean before building fresh distributions")

print()  # Empty line


# ============================================================================
# 7. CHECKING DISTRIBUTIONS
# ============================================================================
print("=" * 60)
print("7. CHECKING DISTRIBUTIONS")
print("=" * 60)

print("  Check distribution before uploading:")
print("    ")
print("    # Install twine")
print("    pip install twine")
print("    ")
print("    # Check distribution")
print("    twine check dist/*")
print("  ")
print("  This validates:")
print("    - Package metadata")
print("    - File structure")
print("    - Compatibility")

print()  # Empty line


# ============================================================================
# 8. INSTALLING FROM BUILT PACKAGES
# ============================================================================
print("=" * 60)
print("8. INSTALLING FROM BUILT PACKAGES")
print("=" * 60)

print("  Install from wheel:")
print("    pip install dist/my_package-0.1.0-py3-none-any.whl")
print("  ")
print("  Install from source distribution:")
print("    pip install dist/my_package-0.1.0.tar.gz")
print("  ")
print("  Install in development mode:")
print("    pip install -e .")
print("  ")
print("  Test installation before publishing!")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("BUILDING PACKAGES SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Build creates distribution files")
print("  - Use 'python -m build' (recommended)")
print("  - Source distribution: .tar.gz")
print("  - Wheel distribution: .whl")
print("  - Clean before building")
print("  - Check with twine check")
print("  - Test installation before publishing")
print("=" * 60)

