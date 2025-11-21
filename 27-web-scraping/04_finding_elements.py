"""
Finding Elements in HTML

This file demonstrates different ways to find elements in HTML.
"""

# ============================================================================
# 1. FINDING BY TAG NAME
# ============================================================================
print("=" * 60)
print("1. FINDING BY TAG NAME")
print("=" * 60)

print("  Find elements:")
print("    soup.find('div')        # First div")
print("    soup.find_all('div')    # All divs")
print("    soup.find_all('a')      # All links")

print()  # Empty line


# ============================================================================
# 2. FINDING BY CLASS AND ID
# ============================================================================
print("=" * 60)
print("2. FINDING BY CLASS AND ID")
print("=" * 60)

print("  Find by attributes:")
print("    soup.find('div', class_='content')  # By class")
print("    soup.find(id='main')                # By ID")
print("    soup.find('div', {'class': 'content'})  # Alternative syntax")

print()  # Empty line


# ============================================================================
# 3. CSS SELECTORS
# ============================================================================
print("=" * 60)
print("3. CSS SELECTORS")
print("=" * 60)

print("  Use CSS selectors:")
print("    soup.select('.content')      # By class")
print("    soup.select('#main')         # By ID")
print("    soup.select('div.content')   # Tag with class")
print("    soup.select('div > p')       # Child selector")

print()  # Empty line


# ============================================================================
# 4. FINDING WITH CONDITIONS
# ============================================================================
print("=" * 60)
print("4. FINDING WITH CONDITIONS")
print("=" * 60)

print("  Find with lambda:")
print("    soup.find_all(lambda tag: tag.name == 'div' and 'content' in tag.get('class', []))")
print("  ")
print("  Find with text:")
print("    soup.find_all(text='Hello')")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("FINDING ELEMENTS SUMMARY:")
print("=" * 60)
print("  - find(): Find first matching element")
print("  - find_all(): Find all matching elements")
print("  - select(): Use CSS selectors")
print("  - Can search by tag, class, ID, attributes")
print("=" * 60)

