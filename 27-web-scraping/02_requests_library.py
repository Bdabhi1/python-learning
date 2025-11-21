"""
The requests Library

This file demonstrates using the requests library to fetch web pages.
"""

# Note: This example demonstrates concepts without making actual requests
# In practice, you would use: import requests

# ============================================================================
# 1. BASIC GET REQUEST
# ============================================================================
print("=" * 60)
print("1. BASIC GET REQUEST")
print("=" * 60)

print("  Basic usage:")
print("    import requests")
print("    response = requests.get('https://example.com')")
print("    print(response.status_code)")
print("    print(response.text)")

print()  # Empty line


# ============================================================================
# 2. RESPONSE OBJECT
# ============================================================================
print("=" * 60)
print("2. RESPONSE OBJECT")
print("=" * 60)

print("  Response object attributes:")
print("    - response.status_code: HTTP status code (200, 404, etc.)")
print("    - response.text: Text content of response")
print("    - response.content: Binary content")
print("    - response.headers: Response headers")
print("    - response.url: Final URL (after redirects)")

print()  # Empty line


# ============================================================================
# 3. ERROR HANDLING
# ============================================================================
print("=" * 60)
print("3. ERROR HANDLING")
print("=" * 60)

print("  Always handle errors:")
print("    try:")
print("        response = requests.get(url)")
print("        response.raise_for_status()  # Raises exception for bad codes")
print("    except requests.exceptions.RequestException as e:")
print("        print(f'Error: {e}')")

print()  # Empty line


# ============================================================================
# 4. HEADERS
# ============================================================================
print("=" * 60)
print("4. HEADERS")
print("=" * 60)

print("  Set custom headers:")
print("    headers = {")
print("        'User-Agent': 'Mozilla/5.0',")
print("        'Accept': 'text/html'")
print("    }")
print("    response = requests.get(url, headers=headers)")

print()  # Empty line


# ============================================================================
# 5. TIMEOUT
# ============================================================================
print("=" * 60)
print("5. TIMEOUT")
print("=" * 60)

print("  Always set timeout:")
print("    response = requests.get(url, timeout=5)")
print("  ")
print("  Prevents hanging on slow/unresponsive servers")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("REQUESTS LIBRARY SUMMARY:")
print("=" * 60)
print("  - requests.get(): Fetch webpage")
print("  - response.status_code: Check status")
print("  - response.text: Get HTML content")
print("  - Always handle errors and set timeout")
print("  - Use headers for better compatibility")
print("=" * 60)

