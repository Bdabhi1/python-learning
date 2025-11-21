"""
Publishing Python Packages

This file demonstrates how to publish packages to PyPI.
"""

# ============================================================================
# 1. WHAT IS PUBLISHING?
# ============================================================================
print("=" * 60)
print("1. WHAT IS PUBLISHING?")
print("=" * 60)

print("  Publishing makes your package available for installation.")
print("  Packages can be published to:")
print("    - PyPI (Python Package Index) - production")
print("    - TestPyPI - testing")
print("    - Private repositories")
print("  ")
print("  Tools needed:")
print("    - twine (for uploading)")
print("    - build (for building)")

print()  # Empty line


# ============================================================================
# 2. PREPARING FOR PUBLICATION
# ============================================================================
print("=" * 60)
print("2. PREPARING FOR PUBLICATION")
print("=" * 60)

print("  Steps before publishing:")
print("    1. Clean previous builds")
print("    2. Update version number")
print("    3. Build fresh distributions")
print("    4. Check distributions")
print("    5. Test installation locally")
print("    6. Update documentation")
print("    7. Check LICENSE file")

print()  # Empty line


# ============================================================================
# 3. TESTPYPI (TESTING)
# ============================================================================
print("=" * 60)
print("3. TESTPYPI (TESTING)")
print("=" * 60)

print("  Publishing to TestPyPI first:")
print("    ")
print("    # Install twine")
print("    pip install twine")
print("    ")
print("    # Build package")
print("    python -m build")
print("    ")
print("    # Upload to TestPyPI")
print("    twine upload --repository testpypi dist/*")
print("  ")
print("  TestPyPI URL: https://test.pypi.org")
print("  Use separate account for TestPyPI")

print()  # Empty line


# ============================================================================
# 4. INSTALLING FROM TESTPYPI
# ============================================================================
print("=" * 60)
print("4. INSTALLING FROM TESTPYPI")
print("=" * 60)

print("  Install from TestPyPI:")
print("    ")
print("    pip install --index-url https://test.pypi.org/simple/ my_package")
print("  ")
print("  Or with extra index:")
print("    ")
print("    pip install --extra-index-url https://test.pypi.org/simple/ my_package")
print("  ")
print("  Always test installation from TestPyPI before PyPI")

print()  # Empty line


# ============================================================================
# 5. PUBLISHING TO PYPI
# ============================================================================
print("=" * 60)
print("5. PUBLISHING TO PYPI")
print("=" * 60)

print("  Publishing to PyPI:")
print("    ")
print("    # Build package")
print("    python -m build")
print("    ")
print("    # Check distributions")
print("    twine check dist/*")
print("    ")
print("    # Upload to PyPI")
print("    twine upload dist/*")
print("  ")
print("  PyPI URL: https://pypi.org")
print("  Requires PyPI account")

print()  # Empty line


# ============================================================================
# 6. API TOKENS
# ============================================================================
print("=" * 60)
print("6. API TOKENS")
print("=" * 60)

print("  Using API tokens (recommended):")
print("    ")
print("    1. Go to PyPI account settings")
print("    2. Create API token")
print("    3. Use token with twine:")
print("    ")
print("    twine upload -u __token__ -p pypi-xxxxx dist/*")
print("  ")
print("  Or set environment variables:")
print("    ")
print("    export TWINE_USERNAME=__token__")
print("    export TWINE_PASSWORD=pypi-xxxxx")
print("    twine upload dist/*")

print()  # Empty line


# ============================================================================
# 7. VERSION MANAGEMENT
# ============================================================================
print("=" * 60)
print("7. VERSION MANAGEMENT")
print("=" * 60)

print("  Version numbering (semantic versioning):")
print("    ")
print("    MAJOR.MINOR.PATCH")
print("    ")
print("    1.0.0 -> 1.0.1 (patch - bug fixes)")
print("    1.0.1 -> 1.1.0 (minor - new features)")
print("    1.1.0 -> 2.0.0 (major - breaking changes)")
print("  ")
print("  Always increment version before publishing")

print()  # Empty line


# ============================================================================
# 8. UPDATING PACKAGES
# ============================================================================
print("=" * 60)
print("8. UPDATING PACKAGES")
print("=" * 60)

print("  Updating existing package:")
print("    ")
print("    1. Update version number")
print("    2. Make changes")
print("    3. Build new distributions")
print("    4. Upload to PyPI")
print("    ")
print("    twine upload dist/*")
print("  ")
print("  PyPI doesn't allow re-uploading same version")
print("  Must increment version for updates")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PUBLISHING SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Test on TestPyPI first")
print("  - Use twine for uploading")
print("  - Use API tokens for authentication")
print("  - Check distributions before uploading")
print("  - Increment version for updates")
print("  - Test installation after publishing")
print("=" * 60)

