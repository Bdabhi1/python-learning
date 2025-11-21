# Packaging and Distribution in Python

Packaging your Python code allows you to share it with others, install it easily, and distribute it via PyPI (Python Package Index). This guide covers creating packages, building distributions, and publishing to PyPI.

## Table of Contents
1. [What is Packaging?](#what-is-packaging)
2. [Project Structure](#project-structure)
3. [setup.py and pyproject.toml](#setuppy-and-pyprojecttoml)
4. [Building Packages](#building-packages)
5. [Installing Packages](#installing-packages)
6. [Publishing to PyPI](#publishing-to-pypi)
7. [Virtual Environments](#virtual-environments)
8. [Best Practices](#best-practices)

---

## What is Packaging?

**Packaging** is the process of preparing your Python code for distribution and installation. It involves:
- Organizing code into a package structure
- Creating metadata files
- Building distribution files
- Publishing to package repositories

**Key concepts:**
- **Package**: A directory containing Python modules
- **Distribution**: A packaged version of your code (wheel, source distribution)
- **PyPI**: Python Package Index - the official repository
- **pip**: Package installer for Python

**Benefits:**
- **Easy Installation**: Users can install with `pip install`
- **Version Management**: Track and manage versions
- **Dependencies**: Specify required packages
- **Distribution**: Share code easily

---

## Project Structure

A well-organized package follows a standard structure:

```
my_package/
├── my_package/
│   ├── __init__.py
│   ├── module1.py
│   ├── module2.py
│   └── subpackage/
│       ├── __init__.py
│       └── module3.py
├── tests/
│   ├── __init__.py
│   └── test_module1.py
├── docs/
│   └── README.md
├── setup.py          # or pyproject.toml
├── README.md
├── LICENSE
├── requirements.txt
└── MANIFEST.in
```

### Key Files:
- `__init__.py`: Makes directory a Python package
- `setup.py` or `pyproject.toml`: Package configuration
- `README.md`: Project documentation
- `LICENSE`: License file
- `requirements.txt`: Dependencies
- `MANIFEST.in`: Additional files to include

---

## setup.py and pyproject.toml

### setup.py (Traditional)

```python
from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1.0',
    description='A sample Python package',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/username/my_package',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.0',
        'numpy>=1.20.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.8',
)
```

### pyproject.toml (Modern)

```toml
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my_package"
version = "0.1.0"
description = "A sample Python package"
authors = [{name = "Your Name", email = "your.email@example.com"}]
readme = "README.md"
requires-python = ">=3.8"
license = {text = "MIT"}
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

[project.optional-dependencies]
dev = [
    "pytest>=6.0",
    "black>=21.0",
]

[tool.setuptools]
packages = ["my_package"]
```

---

## Building Packages

### Source Distribution (sdist)

```bash
# Using setup.py
python setup.py sdist

# Using build tool (recommended)
python -m build
```

Creates a `.tar.gz` file containing source code.

### Wheel Distribution

```bash
# Using setup.py
python setup.py bdist_wheel

# Using build tool (recommended)
python -m build
```

Creates a `.whl` file - pre-built, faster to install.

### Using build (Recommended)

```bash
# Install build tool
pip install build

# Build both sdist and wheel
python -m build
```

This creates both source and wheel distributions in the `dist/` directory.

---

## Installing Packages

### Install from Local Directory

```bash
# Development mode (editable)
pip install -e .

# Regular install
pip install .
```

### Install from Distribution Files

```bash
# From wheel
pip install dist/my_package-0.1.0-py3-none-any.whl

# From source distribution
pip install dist/my_package-0.1.0.tar.gz
```

### Install from Git

```bash
pip install git+https://github.com/username/my_package.git
```

### Install from PyPI

```bash
pip install my_package
```

---

## Publishing to PyPI

### TestPyPI (Testing)

```bash
# Install twine
pip install twine

# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ my_package
```

### PyPI (Production)

```bash
# Upload to PyPI
twine upload dist/*

# Or with credentials
twine upload -u __token__ -p pypi-xxxxx dist/*
```

### API Tokens

1. Go to PyPI account settings
2. Create API token
3. Use token with twine:
   ```bash
   twine upload -u __token__ -p pypi-xxxxx dist/*
   ```

---

## Virtual Environments

Virtual environments isolate package installations.

### Creating Virtual Environment

```bash
# Python 3.3+
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### Using Virtual Environment

```bash
# Install packages
pip install package_name

# Freeze dependencies
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt
```

### Virtualenv (Alternative)

```bash
# Install virtualenv
pip install virtualenv

# Create environment
virtualenv venv

# Activate
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

---

## Best Practices

### 1. Use pyproject.toml

```toml
# Modern standard, preferred over setup.py
[project]
name = "my_package"
version = "0.1.0"
```

### 2. Version Management

```python
# Use semantic versioning
# MAJOR.MINOR.PATCH
# 1.0.0 -> 1.0.1 (patch)
# 1.0.1 -> 1.1.0 (minor)
# 1.1.0 -> 2.0.0 (major)
```

### 3. Include README and LICENSE

```python
setup(
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
)
```

### 4. Specify Dependencies

```python
# In setup.py or pyproject.toml
install_requires=[
    'requests>=2.25.0',  # Minimum version
    'numpy>=1.20.0,<2.0.0',  # Version range
]
```

### 5. Use find_packages()

```python
from setuptools import find_packages

setup(
    packages=find_packages(),  # Automatically finds all packages
)
```

### 6. Include Tests

```python
setup(
    test_suite='tests',
    tests_require=['pytest'],
)
```

### 7. Use MANIFEST.in for Additional Files

```
include README.md
include LICENSE
recursive-include docs *.md
```

### 8. Build Before Publishing

```bash
# Clean previous builds
rm -rf dist/ build/ *.egg-info

# Build fresh
python -m build

# Check before uploading
twine check dist/*
```

---

## Common Mistakes to Avoid

1. **Forgetting __init__.py**
   ```python
   # Wrong - directory not a package
   my_package/
       module.py
   
   # Correct
   my_package/
       __init__.py
       module.py
   ```

2. **Not specifying dependencies**
   ```python
   # Wrong
   setup(install_requires=[])
   
   # Correct
   setup(install_requires=['requests', 'numpy'])
   ```

3. **Hardcoding version**
   ```python
   # Better - read from file
   version = open('VERSION').read().strip()
   ```

4. **Including unnecessary files**
   ```python
   # Use MANIFEST.in to control what's included
   ```

5. **Not testing installation**
   ```bash
   # Always test before publishing
   pip install dist/my_package-0.1.0-py3-none-any.whl
   ```

---

## Summary

- **Packaging** prepares code for distribution
- Use **pyproject.toml** (modern) or **setup.py** (traditional)
- **Build** distributions with `python -m build`
- **Publish** to PyPI with `twine`
- Use **virtual environments** for isolation
- Follow **best practices** for maintainability
- **Test** before publishing

**Remember**: Good packaging makes your code easy to install and use. Follow standards and best practices!

---

## Next Steps

Now that you understand packaging and distribution:
1. Organize your code into a package structure
2. Create setup.py or pyproject.toml
3. Build distribution files
4. Test installation locally
5. Publish to TestPyPI first
6. Publish to PyPI when ready
7. Move on to **35-best-practices** to learn Python best practices

---

## Example Files in This Folder

**Follow these files in order (numbered for learning sequence):**

1. `01_package_structure.py`: Understanding package structure - start here!
2. `02_setup_py.py`: Creating setup.py files
3. `03_pyproject_toml.py`: Using pyproject.toml
4. `04_building_packages.py`: Building distribution files
5. `05_publishing.py`: Publishing to PyPI
6. `06_practical_examples.py`: Real-world packaging examples

Run these files in order to see packaging in action!

