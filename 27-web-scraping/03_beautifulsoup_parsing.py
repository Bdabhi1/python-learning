"""
BeautifulSoup HTML Parsing

This file demonstrates parsing HTML with BeautifulSoup.
"""

# Note: This example demonstrates concepts
# In practice: from bs4 import BeautifulSoup

# ============================================================================
# 1. BASIC PARSING
# ============================================================================
print("=" * 60)
print("1. BASIC PARSING")
print("=" * 60)

html_example = '''
<html>
<head><title>Example Page</title></head>
<body>
    <div class="content">Hello World</div>
</body>
</html>
'''

print("  HTML to parse:")
print(html_example)
print("\n  Parse with BeautifulSoup:")
print("    from bs4 import BeautifulSoup")
print("    soup = BeautifulSoup(html, 'html.parser')")
print("    title = soup.title.string")

print()  # Empty line


# ============================================================================
# 2. PARSERS
# ============================================================================
print("=" * 60)
print("2. PARSERS")
print("=" * 60)

print("  Available parsers:")
print("    - 'html.parser': Built-in (default)")
print("    - 'lxml': Fast, requires lxml library")
print("    - 'html5lib': Very lenient, slow")
print("  ")
print("  Usage:")
print("    soup = BeautifulSoup(html, 'html.parser')")

print()  # Empty line


# ============================================================================
# 3. ACCESSING ELEMENTS
# ============================================================================
print("=" * 60)
print("3. ACCESSING ELEMENTS")
print("=" * 60)

print("  Access elements:")
print("    soup.title          # Get title tag")
print("    soup.title.string   # Get title text")
print("    soup.div            # Get first div")
print("    soup.find('div')    # Find first div")

print()  # Empty line


# ============================================================================
# 4. PRETTY PRINTING
# ============================================================================
print("=" * 60)
print("4. PRETTY PRINTING")
print("=" * 60)

print("  Format HTML:")
print("    print(soup.prettify())")
print("  ")
print("  Makes HTML more readable")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("BEAUTIFULSOUP PARSING SUMMARY:")
print("=" * 60)
print("  - BeautifulSoup(html, 'parser'): Parse HTML")
print("  - soup.find('tag'): Find first element")
print("  - soup.find_all('tag'): Find all elements")
print("  - Use 'html.parser' as default parser")
print("=" * 60)

