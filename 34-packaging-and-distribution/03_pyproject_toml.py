"""
pyproject.toml for Python Packages

This file demonstrates the modern pyproject.toml approach to packaging.
"""

# ============================================================================
# 1. WHAT IS pyproject.toml?
# ============================================================================
print("=" * 60)
print("1. WHAT IS pyproject.toml?")
print("=" * 60)

print("  pyproject.toml is the modern standard for Python packaging.")
print("  It's a TOML file that replaces setup.py in many cases.")
print("  ")
print("  Benefits:")
print("    - Single configuration file")
print("    - More readable than setup.py")
print("    - Standard format (PEP 518)")
print("    - Can configure multiple tools")

print()  # Empty line


# ============================================================================
# 2. BASIC pyproject.toml
# ============================================================================
print("=" * 60)
print("2. BASIC pyproject.toml")
print("=" * 60)

print("  Basic pyproject.toml:")
print("    ")
print("    [build-system]")
print("    requires = [\"setuptools>=45\", \"wheel\"]")
print("    build-backend = \"setuptools.build_meta\"")
print("    ")
print("    [project]")
print("    name = \"my_package\"")
print("    version = \"0.1.0\"")
print("    description = \"A sample package\"")

print()  # Empty line


# ============================================================================
# 3. COMPLETE pyproject.toml
# ============================================================================
print("=" * 60)
print("3. COMPLETE pyproject.toml")
print("=" * 60)

print("  Complete pyproject.toml:")
print("    ")
print("    [build-system]")
print("    requires = [\"setuptools>=45\", \"wheel\"]")
print("    build-backend = \"setuptools.build_meta\"")
print("    ")
print("    [project]")
print("    name = \"my_package\"")
print("    version = \"0.1.0\"")
print("    description = \"A sample Python package\"")
print("    authors = [{name = \"Your Name\", email = \"your.email@example.com\"}]")
print("    readme = \"README.md\"")
print("    requires-python = \">=3.8\"")
print("    license = {text = \"MIT\"}")
print("    classifiers = [")
print("        \"Development Status :: 3 - Alpha\",")
print("        \"Intended Audience :: Developers\",")
print("    ]")
print("    dependencies = [")
print("        \"requests>=2.25.0\",")
print("        \"numpy>=1.20.0\",")
print("    ]")
print("    ")
print("    [project.optional-dependencies]")
print("    dev = [\"pytest\", \"black\"]")
print("    docs = [\"sphinx\"]")

print()  # Empty line


# ============================================================================
# 4. BUILD SYSTEM
# ============================================================================
print("=" * 60)
print("4. BUILD SYSTEM")
print("=" * 60)

print("  Build system configuration:")
print("    ")
print("    [build-system]")
print("    requires = [\"setuptools>=45\", \"wheel\"]")
print("    build-backend = \"setuptools.build_meta\"")
print("  ")
print("  This tells pip/build tools:")
print("    - What packages are needed to build")
print("    - Which build backend to use")

print()  # Empty line


# ============================================================================
# 5. PROJECT METADATA
# ============================================================================
print("=" * 60)
print("5. PROJECT METADATA")
print("=" * 60)

print("  Project metadata section:")
print("    ")
print("    [project]")
print("    name = \"my_package\"")
print("    version = \"0.1.0\"")
print("    description = \"Short description\"")
print("    readme = \"README.md\"")
print("    requires-python = \">=3.8\"")
print("    license = {text = \"MIT\"}")
print("    authors = [{name = \"Name\", email = \"email@example.com\"}]")
print("    keywords = [\"python\", \"package\"]")
print("    classifiers = [...]")

print()  # Empty line


# ============================================================================
# 6. DEPENDENCIES
# ============================================================================
print("=" * 60)
print("6. DEPENDENCIES")
print("=" * 60)

print("  Specifying dependencies:")
print("    ")
print("    [project]")
print("    dependencies = [")
print("        \"requests>=2.25.0\",")
print("        \"numpy>=1.20.0,<2.0.0\",")
print("    ]")
print("    ")
print("    [project.optional-dependencies]")
print("    dev = [\"pytest\", \"black\", \"flake8\"]")
print("    test = [\"pytest\", \"pytest-cov\"]")
print("    docs = [\"sphinx\", \"sphinx-rtd-theme\"]")
print("  ")
print("  Install with extras:")
print("    pip install my_package[dev]")

print()  # Empty line


# ============================================================================
# 7. ENTRY POINTS
# ============================================================================
print("=" * 60)
print("7. ENTRY POINTS")
print("=" * 60)

print("  Defining entry points:")
print("    ")
print("    [project.scripts]")
print("    my_command = \"my_package.cli:main\"")
print("    ")
print("    [project.gui-scripts]")
print("    my_gui = \"my_package.gui:main\"")
print("  ")
print("  Creates executable commands when installed")

print()  # Empty line


# ============================================================================
# 8. TOOL CONFIGURATION
# ============================================================================
print("=" * 60)
print("8. TOOL CONFIGURATION")
print("=" * 60)

print("  Configuring other tools:")
print("    ")
print("    [tool.setuptools]")
print("    packages = [\"my_package\"]")
print("    ")
print("    [tool.black]")
print("    line-length = 88")
print("    ")
print("    [tool.pytest.ini_options]")
print("    testpaths = [\"tests\"]")
print("  ")
print("  pyproject.toml can configure multiple tools")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("pyproject.toml SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Modern standard for Python packaging")
print("  - More readable than setup.py")
print("  - Single configuration file")
print("  - Can configure multiple tools")
print("  - Use [build-system] for build configuration")
print("  - Use [project] for package metadata")
print("  - Use [project.optional-dependencies] for extras")
print("=" * 60)

