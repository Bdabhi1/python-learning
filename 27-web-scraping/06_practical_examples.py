"""
Practical Web Scraping Examples

This file demonstrates real-world web scraping patterns.
"""

# ============================================================================
# 1. SCRAPING WITH ERROR HANDLING
# ============================================================================
print("=" * 60)
print("1. SCRAPING WITH ERROR HANDLING")
print("=" * 60)

print("  Always include error handling:")
print("    try:")
print("        response = requests.get(url, timeout=5)")
print("        response.raise_for_status()")
print("        soup = BeautifulSoup(response.text, 'html.parser')")
print("        # Extract data")
print("    except requests.exceptions.RequestException as e:")
print("        print(f'Error fetching page: {e}')")

print()  # Empty line


# ============================================================================
# 2. RATE LIMITING
# ============================================================================
print("=" * 60)
print("2. RATE LIMITING")
print("=" * 60)

print("  Be polite - add delays:")
print("    import time")
print("    ")
print("    for url in urls:")
print("        response = requests.get(url)")
print("        # Process response")
print("        time.sleep(1)  # Wait 1 second between requests")

print()  # Empty line


# ============================================================================
# 3. SAVING SCRAPED DATA
# ============================================================================
print("=" * 60)
print("3. SAVING SCRAPED DATA")
print("=" * 60)

print("  Save to file:")
print("    import json")
print("    ")
print("    data = {'title': title, 'content': content}")
print("    with open('scraped_data.json', 'w') as f:")
print("        json.dump(data, f)")

print()  # Empty line


# ============================================================================
# 4. USER AGENT
# ============================================================================
print("=" * 60)
print("4. USER AGENT")
print("=" * 60)

print("  Set User-Agent header:")
print("    headers = {")
print("        'User-Agent': 'Mozilla/5.0 (Educational Bot)'")
print("    }")
print("    response = requests.get(url, headers=headers)")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("PRACTICAL EXAMPLES SUMMARY:")
print("=" * 60)
print("Web scraping best practices:")
print("  - Always handle errors")
print("  - Use rate limiting")
print("  - Set appropriate User-Agent")
print("  - Respect robots.txt")
print("  - Save data appropriately")
print("=" * 60)

