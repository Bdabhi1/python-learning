"""
URL Handling in Python

This file demonstrates how to parse and manipulate URLs.
"""

from urllib.parse import urlparse, urlunparse, urljoin, urlencode, quote, unquote, parse_qs

# ============================================================================
# 1. WHAT IS URL HANDLING?
# ============================================================================
print("=" * 60)
print("1. WHAT IS URL HANDLING?")
print("=" * 60)

print("  URL handling involves:")
print("    - Parsing URLs into components")
print("    - Constructing URLs from components")
print("    - Encoding/decoding URL components")
print("    - Joining URLs")
print("    - Parsing query strings")

print()  # Empty line


# ============================================================================
# 2. PARSING URLs
# ============================================================================
print("=" * 60)
print("2. PARSING URLs")
print("=" * 60)

url = "https://www.example.com:8080/path/to/page?param=value&other=123#fragment"
print(f"  URL: {url}")
print("  ")

parsed = urlparse(url)

print("  Parsed components:")
print(f"    Scheme: {parsed.scheme}")      # https
print(f"    Netloc: {parsed.netloc}")      # www.example.com:8080
print(f"    Path: {parsed.path}")          # /path/to/page
print(f"    Query: {parsed.query}")        # param=value&other=123
print(f"    Fragment: {parsed.fragment}")  # fragment
print(f"    Username: {parsed.username}")   # None
print(f"    Password: {parsed.password}")  # None
print(f"    Hostname: {parsed.hostname}")  # www.example.com
print(f"    Port: {parsed.port}")          # 8080

print()  # Empty line


# ============================================================================
# 3. RECONSTRUCTING URLs
# ============================================================================
print("=" * 60)
print("3. RECONSTRUCTING URLs")
print("=" * 60)

parsed = urlparse("https://www.example.com/path?param=value")

print("  Original components:")
print(f"    {parsed}")

# Reconstruct URL
reconstructed = urlunparse(parsed)
print(f"  Reconstructed: {reconstructed}")

# Modify and reconstruct
modified = parsed._replace(path="/new/path", query="new=param")
new_url = urlunparse(modified)
print(f"  Modified URL: {new_url}")

print()  # Empty line


# ============================================================================
# 4. URL ENCODING
# ============================================================================
print("=" * 60)
print("4. URL ENCODING")
print("=" * 60)

# Encode parameters
params = {'name': 'John Doe', 'age': 30, 'city': 'New York'}
encoded = urlencode(params)
print(f"  Parameters: {params}")
print(f"  Encoded: {encoded}")

# Quote individual values
name = quote("John Doe")
print(f"  Quoted 'John Doe': {name}")

# Special characters
special = quote("Hello & World!")
print(f"  Quoted 'Hello & World!': {special}")

print()  # Empty line


# ============================================================================
# 5. URL DECODING
# ============================================================================
print("=" * 60)
print("5. URL DECODING")
print("=" * 60)

# Decode
encoded_name = "John%20Doe"
decoded = unquote(encoded_name)
print(f"  Encoded: {encoded_name}")
print(f"  Decoded: {decoded}")

# Decode query string
encoded_query = "name=John+Doe&age=30"
decoded_query = unquote(encoded_query)
print(f"  Encoded query: {encoded_query}")
print(f"  Decoded query: {decoded_query}")

print()  # Empty line


# ============================================================================
# 6. PARSING QUERY STRINGS
# ============================================================================
print("=" * 60)
print("6. PARSING QUERY STRINGS")
print("=" * 60)

query_string = "name=John+Doe&age=30&city=New+York&hobbies=reading&hobbies=coding"
print(f"  Query string: {query_string}")

# Parse query string
parsed_qs = parse_qs(query_string)
print(f"  Parsed: {parsed_qs}")

# Parse with single values
parsed_qsl = parse_qs(query_string, keep_blank_values=True)
print(f"  Parsed (keep blank): {parsed_qsl}")

print()  # Empty line


# ============================================================================
# 7. JOINING URLs
# ============================================================================
print("=" * 60)
print("7. JOINING URLs")
print("=" * 60)

base = "https://www.example.com/path/"
relative = "to/page.html"

# Join URLs
full_url = urljoin(base, relative)
print(f"  Base: {base}")
print(f"  Relative: {relative}")
print(f"  Joined: {full_url}")

# Absolute URL
absolute = urljoin(base, "/absolute/path.html")
print(f"  Absolute: {absolute}")

# Different base
base2 = "https://www.example.com/path/page.html"
relative2 = "../other/page.html"
joined2 = urljoin(base2, relative2)
print(f"  Base: {base2}")
print(f"  Relative: {relative2}")
print(f"  Joined: {joined2}")

print()  # Empty line


# ============================================================================
# 8. BUILDING QUERY STRINGS
# ============================================================================
print("=" * 60)
print("8. BUILDING QUERY STRINGS")
print("=" * 60)

# Build query string from dict
params = {
    'page': 1,
    'limit': 10,
    'sort': 'name',
    'filter': 'active'
}

query_string = urlencode(params)
print(f"  Parameters: {params}")
print(f"  Query string: {query_string}")

# With custom separator
query_string_custom = urlencode(params, doseq=True)
print(f"  Query string (doseq): {query_string_custom}")

# Multiple values
params_multi = {
    'tags': ['python', 'web', 'api']
}
query_multi = urlencode(params_multi, doseq=True)
print(f"  Multi-value params: {params_multi}")
print(f"  Query string: {query_multi}")

print()  # Empty line


# ============================================================================
# 9. URL VALIDATION
# ============================================================================
print("=" * 60)
print("9. URL VALIDATION")
print("=" * 60)

def is_valid_url(url):
    """Check if URL is valid"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False

test_urls = [
    "https://www.example.com",
    "http://localhost:8000",
    "not-a-url",
    "ftp://files.example.com",
    "https://"
]

print("  URL validation:")
for url in test_urls:
    valid = is_valid_url(url)
    print(f"    {url}: {'Valid' if valid else 'Invalid'}")

print()  # Empty line


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("URL HANDLING SUMMARY:")
print("=" * 60)
print("Key Points:")
print("  - Use urlparse() to parse URLs")
print("  - Use urlunparse() to reconstruct URLs")
print("  - Use urlencode() to encode parameters")
print("  - Use quote()/unquote() for individual values")
print("  - Use parse_qs() to parse query strings")
print("  - Use urljoin() to join URLs")
print("  - Validate URLs before using")
print("  - Handle encoding/decoding properly")
print("=" * 60)

