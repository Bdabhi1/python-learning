"""
Extracting Data from HTML

This file demonstrates extracting text, links, and attributes from HTML.
"""

# ============================================================================
# 1. EXTRACTING TEXT
# ============================================================================
print("=" * 60)
print("1. EXTRACTING TEXT")
print("=" * 60)

print("  Extract text content:")
print("    element.text          # All text (including children)")
print("    element.get_text()    # Same as .text")
print("    element.string        # Direct text only (None if has children)")
print("    element.get_text(strip=True)  # Remove extra whitespace")

print()  # Empty line


# ============================================================================
# 2. EXTRACTING ATTRIBUTES
# ============================================================================
print("=" * 60)
print("2. EXTRACTING ATTRIBUTES")
print("=" * 60)

print("  Get attributes:")
print("    element['href']           # Get attribute")
print("    element.get('href')      # Safer (returns None if missing)")
print("    element.attrs            # All attributes as dict")

print()  # Empty line


# ============================================================================
# 3. EXTRACTING LINKS
# ============================================================================
print("=" * 60)
print("3. EXTRACTING LINKS")
print("=" * 60)

print("  Extract all links:")
print("    links = soup.find_all('a')")
print("    for link in links:")
print("        href = link.get('href')")
print("        text = link.text")
print("        print(f'{text}: {href}')")

print()  # Empty line


# ============================================================================
# 4. EXTRACTING IMAGES
# ============================================================================
print("=" * 60)
print("4. EXTRACTING IMAGES")
print("=" * 60)

print("  Extract image sources:")
print("    images = soup.find_all('img')")
print("    for img in images:")
print("        src = img.get('src')")
print("        alt = img.get('alt', '')")
print("        print(f'{alt}: {src}')")

print()  # Empty line


# ============================================================================
# 5. EXTRACTING TABLE DATA
# ============================================================================
print("=" * 60)
print("5. EXTRACTING TABLE DATA")
print("=" * 60)

print("  Extract table rows:")
print("    table = soup.find('table')")
print("    rows = table.find_all('tr')")
print("    for row in rows:")
print("        cells = row.find_all('td')")
print("        data = [cell.text for cell in cells]")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("EXTRACTING DATA SUMMARY:")
print("=" * 60)
print("  - .text or .get_text(): Extract text content")
print("  - element['attr'] or .get('attr'): Get attributes")
print("  - find_all() to get multiple elements")
print("  - Process extracted data as needed")
print("=" * 60)

